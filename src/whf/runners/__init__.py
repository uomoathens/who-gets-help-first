from __future__ import annotations


def make_runner(spec: dict):
    kind = spec.get("kind")
    if kind == "mock":
        from .mock import MockRunner
        return MockRunner(name=spec["name"], bias=spec.get("bias") or {}, noise=float(spec.get("noise", 0.5)))
    if kind == "openai":
        from .openai_compat import OpenAICompatRunner
        return OpenAICompatRunner(
            name=spec["name"],
            base_url=spec["base_url"],
            model=spec["model"],
            api_key_env=spec.get("api_key_env"),
            revision=spec.get("revision"),
            send_seed=bool(spec.get("send_seed", True)),
            timeout=int(spec.get("timeout", 180)),
        )
    if kind == "hf":
        from .hf import HFRunner
        return HFRunner(name=spec["name"], model=spec["model"], revision=spec.get("revision"),
                        dtype=spec.get("dtype", "auto"), load_in_4bit=bool(spec.get("load_in_4bit", False)))
    raise ValueError(f"unknown runner kind {kind!r}")
