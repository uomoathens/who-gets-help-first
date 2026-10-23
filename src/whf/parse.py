from __future__ import annotations

import json
import re
import unicodedata

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


EXPECTED_KEYS = ("ranking", "shares", "score", "decision")


def extract_json(text: str):
    if not isinstance(text, str):
        return None
    cleaned = re.sub(r"```(?:json)?", "", text)
    first = None
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
                        if any(k in obj for k in EXPECTED_KEYS):
                            return obj
                        if first is None:
                            first = obj
                    break
        start = cleaned.find("{", start + 1)
    partial = _partial(cleaned)
    return partial if partial is not None else first


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


def _fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s).casefold())
    return " ".join("".join(c for c in s if not unicodedata.combining(c)).split())


def _label(x, labels=None, texts=None) -> str:
    s = str(x).strip().rstrip(".:)").strip()
    token = s.split()[-1] if s.split() else s
    token = token.strip("()[]«»\"'").upper()
    token = GREEK_LABELS.get(token, token)
    if labels is None or token in labels or not texts:
        return token
    key = _fold(s)
    if len(key) < 4:
        return token
    hits = [k for k, v in texts.items() if key in _fold(v)]
    return hits[0] if len(hits) == 1 else token


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


def parse(decision: str, text: str, labels: list, share_sum_tolerance: float = 2.0, texts: dict | None = None):
    obj = extract_json(text)
    if obj is None:
        return None, "no-json"
    if decision == "ranking":
        r = obj.get("ranking")
        if not isinstance(r, list):
            return None, "no-ranking"
        r = [_label(x, labels, texts) for x in r]
        if sorted(r) != sorted(labels):
            return None, "not-a-permutation"
        return {"ranking": r}, None
    if decision == "shares":
        s = obj.get("shares")
        if not isinstance(s, dict):
            return None, "no-shares"
        s = {_label(k, labels, texts): _num(v) for k, v in s.items()}
        if set(s) != set(labels) or any(v is None or v < 0 for v in s.values()):
            return None, "bad-shares"
        total = sum(s.values())
        if total <= 0:
            return None, "shares-do-not-sum-to-100"
        out = {"shares": {k: 100 * v / total for k, v in s.items()}}
        if abs(total - 100) > share_sum_tolerance:
            out["rescaled"] = True
        return out, None
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
        out = {"shares": {mapping[k]: v for k, v in parsed["shares"].items()}}
        if parsed.get("rescaled"):
            out["rescaled"] = True
        return out
    return dict(parsed)
