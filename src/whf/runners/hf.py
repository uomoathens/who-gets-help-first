from __future__ import annotations


class HFRunner:
    def __init__(self, name: str, model: str, revision: str | None = None, dtype: str = "auto", load_in_4bit: bool = False):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.torch = torch
        self.name = name
        self.model_id = model
        self.tokenizer = AutoTokenizer.from_pretrained(model, revision=revision)
        kwargs = {"revision": revision, "device_map": "auto", "torch_dtype": dtype}
        if load_in_4bit:
            from transformers import BitsAndBytesConfig
            kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)
        self.model = AutoModelForCausalLM.from_pretrained(model, **kwargs)
        self.revision = revision or getattr(self.model.config, "_commit_hash", None) or "unpinned"

    def _encode(self, messages):
        try:
            return self.tokenizer.apply_chat_template(list(messages), add_generation_prompt=True, return_tensors="pt")
        except Exception:
            merged = [{"role": "user", "content": messages[0]["content"] + "\n\n" + messages[1]["content"]}]
            return self.tokenizer.apply_chat_template(merged, add_generation_prompt=True, return_tensors="pt")

    def generate(self, messages, *, seed: int, temperature: float, max_tokens: int, context: dict) -> str:
        self.torch.manual_seed(seed % (2 ** 31))
        ids = self._encode(messages).to(self.model.device)
        kwargs = {"max_new_tokens": max_tokens, "pad_token_id": self.tokenizer.eos_token_id}
        if temperature > 0:
            kwargs.update(do_sample=True, temperature=temperature)
        else:
            kwargs.update(do_sample=False)
        with self.torch.no_grad():
            out = self.model.generate(ids, **kwargs)
        return self.tokenizer.decode(out[0][ids.shape[-1]:], skip_special_tokens=True)
