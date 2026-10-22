from __future__ import annotations

import hashlib
import string
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import yaml

from .attributes import Attributes
from .cases import KINDS, LANGS, TASKS, Case, CaseError
from .expand import Variant

LABELS = string.ascii_uppercase


def stable_int(*parts) -> int:
    h = hashlib.sha256("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return int(h[:15], 16)


@dataclass(frozen=True)
class Prompt:
    messages: tuple
    labels: tuple
    sha: str

    def unit_for(self, label: str) -> str:
        return dict(self.labels)[label]


class Prompts:
    def __init__(self, data: dict):
        self.data = data

    @classmethod
    def load(cls, directory: Path) -> "Prompts":
        data = {}
        for lang in LANGS:
            with open(Path(directory) / f"{lang}.yaml", encoding="utf-8") as f:
                data[lang] = yaml.safe_load(f)
        p = cls(data)
        p.check()
        return p

    def check(self) -> None:
        for lang in LANGS:
            d = self.data[lang]
            for key in ("decimal", "roles", "rule", "person", "person_need_join", "community", "community_need_join", "home", "tasks"):
                if key not in d:
                    raise CaseError(f"prompts/{lang}: missing {key}")
            for task in TASKS:
                t = d["tasks"].get(task)
                if not t or len(t.get("instructions", [])) < 1 or "answer" not in t:
                    raise CaseError(f"prompts/{lang}.tasks.{task}: incomplete")
                if TASKS[task]["mode"] == "mixed":
                    if set(t.get("units", {})) != set(KINDS):
                        raise CaseError(f"prompts/{lang}.tasks.{task}: needs a unit template for each of {', '.join(KINDS)}")
                elif "unit" not in t:
                    raise CaseError(f"prompts/{lang}.tasks.{task}: incomplete")
            if set(d["roles"]) != set(self.data[LANGS[0]]["roles"]):
                raise CaseError(f"prompts/{lang}: roles differ between languages")
            n = {len(d["tasks"][t]["instructions"]) for t in TASKS}
            if len(n) != 1:
                raise CaseError(f"prompts/{lang}: every task needs the same number of paraphrases")

    def paraphrases(self) -> int:
        return len(self.data[LANGS[0]]["tasks"]["dispatch"]["instructions"])

    def roles(self) -> list:
        return list(self.data[LANGS[0]]["roles"])


def number(x, decimal: str) -> str:
    if isinstance(x, float) and not x.is_integer():
        text = f"{x:.2f}".rstrip("0").rstrip(".")
        return text.replace(".", decimal)
    return str(int(x))


def identity_text(case: Case, unit_place: dict, identity: dict, lang: str, attributes: Attributes, prompts: Prompts, kind: str = "") -> str:
    p = prompts.data[lang]
    s = attributes.setting(case.setting)
    mode = case.mode
    if mode == "mixed":
        if kind == "business":
            return ""
        if kind == "workers":
            need_text = attributes.controls[identity["need"]]["workers"][lang]
            origin = s["origin"][identity["origin"]]["workers"][lang]
            return f"{origin} {need_text}".strip()
        area = s["area"][identity["area"]]["person"][lang].replace("{place}", unit_place[lang])
        name = attributes.name(case.setting, identity, lang)
        if kind == "home":
            return p["home"].format(name=name, area=area)
        mode = "person"
    area = s["area"][identity["area"]][mode][lang].replace("{place}", unit_place[lang])
    need_text = attributes.controls[identity["need"]][mode][lang]
    if mode == "person":
        need = f"{p['person_need_join']}{need_text}" if need_text else ""
        name = attributes.name(case.setting, identity, lang)
        status = attributes.status[identity["status"]][identity["gender"]][lang]
        return p["person"].format(name=name, status=status, area=area, need=need)
    need = f"{p['community_need_join']}{need_text}" if need_text else ""
    origin = s["origin"][identity["origin"]]["community"][lang]
    return p["community"].format(area=area, origin=origin, need=need)


def example(decision: str, labels: list) -> str:
    if decision == "ranking":
        return '{"ranking": ["<first>", "<second>", "...", "<last>"], "justification": "..."}'
    if decision == "shares":
        inner = ", ".join(f'"{x}": <%>' for x in labels)
        return '{"shares": {' + inner + '}, "justification": "..."}'
    return '{"score": <1-10>, "decision": "approve" | "decline", "justification": "..."}'


def build(case: Case, variant: Variant, lang: str, paraphrase: int, role: str, run: int,
          attributes: Attributes, prompts: Prompts) -> Prompt:
    p = prompts.data[lang]
    t = p["tasks"][case.task]
    rng = np.random.default_rng(stable_int(case.id, run))
    order = [case.units[i] for i in rng.permutation(len(case.units))]
    labels = []
    lines = []
    for i, u in enumerate(order):
        label = LABELS[i]
        ident = variant.identity_dict if u.id == case.target else u.identity
        facts = {k: number(v, p["decimal"]) for k, v in u.facts.items()}
        template = t["units"][u.kind] if case.mode == "mixed" else t["unit"]
        text = template.format(label=label, place=u.place[lang], identity=identity_text(case, u.place, ident, lang, attributes, prompts, u.kind), **facts)
        labels.append((label, u.id))
        lines.append(text)
    shown = [x for x, _ in labels] if case.decision != "score" else []
    answer = t["answer"].replace("{example}", example(case.decision, shown))
    user = "\n\n".join([case.context[lang], " ".join(x for x in (t["instructions"][paraphrase], p["rule"], t.get("criteria", "")) if x), "\n".join(lines), answer])
    messages = ({"role": "system", "content": p["roles"][role]}, {"role": "user", "content": user})
    sha = hashlib.sha256((messages[0]["content"] + "\n" + user).encode("utf-8")).hexdigest()[:16]
    return Prompt(messages, tuple(labels), sha)
