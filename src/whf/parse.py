from __future__ import annotations

import json
import re

DECISIONS = ("approve", "decline")
GREEK_LABELS = dict(zip("ΑΒΓΔΕΖΗΘ", "ABCDEFGH"))


def _strip_comments(text: str) -> str:
    out = []
    in_str = False
    esc = False
    i = 0
    while i < len(text):
        ch = text[i]
        if in_str:
            out.append(ch)
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
            out.append(ch)
            i += 1
            continue
        if text.startswith("//", i):
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _loads(fragment: str):
    for candidate in (fragment, _strip_comments(fragment)):
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    return None


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
                    obj = _loads(cleaned[start:i + 1])
                    if isinstance(obj, dict):
                        return obj
                    break
        start = cleaned.find("{", start + 1)
    return _partial(cleaned)


def _partial(text: str):
    m = re.search(r'"ranking"\s*:\s*\[([^\]]*)\]', text)
    if m:
        items = re.findall(r'"([^"]*)"', m.group(1))
        if items:
            return {"ranking": items}
    m = re.search(r'"shares"\s*:\s*\{([^}]*)\}', text)
    if m:
        obj = _loads("{" + m.group(1) + "}")
        if isinstance(obj, dict):
            return {"shares": obj}
    m = re.search(r'"score"\s*:\s*"?(\d+)"?\s*,\s*"decision"\s*:\s*"(\w+)"', text)
    if m:
        return {"score": int(m.group(1)), "decision": m.group(2)}
    return None


def _label(x) -> str:
    s = str(x).strip().rstrip(".:)").strip()
    token = s.split()[-1] if s.split() else s
    token = token.strip("()[]«»\"'").upper()
    return GREEK_LABELS.get(token, token)


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
        r = [_label(x) for x in r]
        if sorted(r) != sorted(labels):
            return None, "not-a-permutation"
        return {"ranking": r}, None
    if decision == "shares":
        s = obj.get("shares")
        if not isinstance(s, dict):
            return None, "no-shares"
        s = {_label(k): _num(v) for k, v in s.items()}
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
