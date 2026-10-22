from __future__ import annotations

import json
import re

DECISIONS = ("approve", "decline")


def extract_json(text: str):
    if not isinstance(text, str):
        return None
    cleaned = re.sub(r"```(?:json)?", "", text)
    start = cleaned.find("{")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(cleaned)):
            ch = cleaned[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        obj = json.loads(cleaned[start:i + 1])
                    except json.JSONDecodeError:
                        break
                    if isinstance(obj, dict):
                        return obj
                    break
        start = cleaned.find("{", start + 1)
    return None


def _num(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v.strip().rstrip("%").replace(",", "."))
        except ValueError:
            return None
    return None


def parse(decision: str, text: str, labels: list, share_sum_tolerance: float = 2.0):
    obj = extract_json(text)
    if obj is None:
        return None, "no-json"
    if decision == "ranking":
        r = obj.get("ranking")
        if not isinstance(r, list):
            return None, "no-ranking"
        r = [str(x).strip().upper() for x in r]
        if sorted(r) != sorted(labels):
            return None, "not-a-permutation"
        return {"ranking": r}, None
    if decision == "shares":
        s = obj.get("shares")
        if not isinstance(s, dict):
            return None, "no-shares"
        s = {str(k).strip().upper(): _num(v) for k, v in s.items()}
        if set(s) != set(labels) or any(v is None or v < 0 for v in s.values()):
            return None, "bad-shares"
        total = sum(s.values())
        if abs(total - 100) > share_sum_tolerance:
            return None, "shares-do-not-sum-to-100"
        return {"shares": {k: 100 * v / total for k, v in s.items()}}, None
    if decision == "score":
        score = _num(obj.get("score"))
        verdict = str(obj.get("decision", "")).strip().lower()
        if score is None or not score.is_integer() or not 1 <= score <= 10:
            return None, "bad-score"
        if verdict not in DECISIONS:
            return None, "bad-decision"
        return {"score": int(score), "decision": verdict}, None
    raise ValueError(decision)


def to_units(decision: str, parsed: dict, mapping: dict) -> dict:
    if decision == "ranking":
        return {"ranking": [mapping[x] for x in parsed["ranking"]]}
    if decision == "shares":
        return {"shares": {mapping[k]: v for k, v in parsed["shares"].items()}}
    return dict(parsed)
