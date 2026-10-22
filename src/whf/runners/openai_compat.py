from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request


class OpenAICompatRunner:
    def __init__(self, name: str, base_url: str, model: str, api_key_env: str | None = None,
                 revision: str | None = None, send_seed: bool = True, timeout: int = 180, retries: int = 4):
        self.name = name
        self.model_id = model
        self.revision = revision or "unpinned"
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.api_key = os.environ.get(api_key_env, "") if api_key_env else ""
        if api_key_env and not self.api_key:
            raise RuntimeError(f"environment variable {api_key_env} is not set")
        self.send_seed = send_seed
        self.timeout = timeout
        self.retries = retries

    def generate(self, messages, *, seed: int, temperature: float, max_tokens: int, context: dict) -> str:
        body = {"model": self.model_id, "messages": list(messages), "temperature": temperature, "max_tokens": max_tokens}
        if self.send_seed:
            body["seed"] = seed
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        data = json.dumps(body).encode("utf-8")
        last = None
        for attempt in range(self.retries):
            req = urllib.request.Request(self.url, data=data, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    payload = json.loads(resp.read().decode("utf-8"))
                return payload["choices"][0]["message"]["content"] or ""
            except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as e:
                last = e
                time.sleep(2 ** attempt)
        raise RuntimeError(f"{self.name}: request failed after {self.retries} attempts: {last}")
