from __future__ import annotations

import json

import numpy as np

from ..cases import tier

NEED_BONUS = {"none": 0.0, "age80": 3.0, "wheelchair": 3.0, "infant": 3.0, "dialysis": 4.0, "pregnant": 3.0}
TIER_BONUS = {0: 60.0, 1: 40.0, 2: 20.0, 3: 0.0}


def _need_score(task: str, facts: dict) -> float:
    if task in ("dispatch", "triage"):
        return facts["people"] + 3 * facts["depth_m"] + facts["minutes"] / 20
    if task == "evacuation":
        return facts["residents"] / 100 + 3 * facts["forecast_m"] - 0.5 * facts["hours"]
    if task == "relief":
        return facts["residents"] / 100 + 1.5 * facts["days"]
    return 0.6 * facts["members"] + facts["damage_pct"] / 25 + facts["nights"] / 4


def _largest_remainder(weights: dict) -> dict:
    total = sum(weights.values())
    raw = {k: 100 * v / total for k, v in weights.items()}
    out = {k: int(np.floor(v)) for k, v in raw.items()}
    rest = 100 - sum(out.values())
    for k in sorted(raw, key=lambda k: raw[k] - out[k], reverse=True)[:rest]:
        out[k] += 1
    return out


class MockRunner:
    def __init__(self, name: str, bias: dict, noise: float = 0.5):
        self.name = name
        self.model_id = f"mock:{name}"
        self.revision = "1"
        self.bias = {str(k): float(v) for k, v in bias.items()}
        self.noise = noise

    def generate(self, messages, *, seed: int, temperature: float, max_tokens: int, context: dict) -> str:
        rng = np.random.default_rng(seed)
        task = context["task"]
        scores = {}
        for label, unit in context["units"].items():
            s = _need_score(task, unit["facts"]) + NEED_BONUS[unit["identity"].get("need", "none")] + (TIER_BONUS[tier(unit["kind"], unit["identity"])] if unit.get("kind") else 0.0)
            for attr, value in unit["identity"].items():
                s += self.bias.get(f"{attr}={value}", 0.0)
            scores[label] = s + rng.normal(0, self.noise)
        if context["decision"] == "ranking":
            ranking = sorted(scores, key=lambda k: scores[k], reverse=True)
            return json.dumps({"ranking": ranking, "justification": "mock"})
        if context["decision"] == "shares":
            weights = {k: max(v, 0.1) for k, v in scores.items()}
            return json.dumps({"shares": _largest_remainder(weights), "justification": "mock"})
        (label, score), = scores.items()
        value = int(min(10, max(1, round(score))))
        return json.dumps({"score": value, "decision": "approve" if value >= 7 else "decline", "justification": "mock"})
