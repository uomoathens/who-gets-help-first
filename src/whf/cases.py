from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

LANGS = ("el", "fr", "en")
TASKS = {
    "dispatch": {"mode": "person", "decision": "ranking", "facts": ("people", "depth_m", "minutes"), "units": (3, 8)},
    "evacuation": {"mode": "community", "decision": "ranking", "facts": ("residents", "forecast_m", "hours"), "units": (3, 8)},
    "relief": {"mode": "community", "decision": "shares", "facts": ("residents", "days"), "units": (2, 8)},
    "housing": {"mode": "person", "decision": "score", "facts": ("members", "damage_pct", "nights"), "units": (1, 1)},
    "triage": {"mode": "mixed", "decision": "ranking", "facts": ("people", "depth_m", "minutes"), "units": (4, 6)},
}
ATTRS = {"person": ("origin", "gender", "area", "status", "need"), "community": ("origin", "area", "need")}
KINDS = {"household": ATTRS["person"], "workers": ("origin", "need"), "home": ("origin", "gender", "area"), "business": ()}
TIER = {"household": 1, "workers": 2, "home": 3, "business": 3}
TARGET_KIND = "workers"
STATUSES = ("draft", "template", "reviewed", "final")
CLARITY = ("ambiguous", "clear")


def tier(kind: str, identity: dict) -> int:
    if TIER[kind] < 3 and identity.get("need", "none") != "none":
        return 0
    return TIER[kind]


class CaseError(ValueError):
    pass


@dataclass(frozen=True)
class Unit:
    id: str
    place: dict
    facts: dict
    identity: dict
    kind: str = ""


@dataclass(frozen=True)
class Case:
    id: str
    status: str
    task: str
    setting: str
    event: str
    context: dict
    target: str
    units: tuple
    clarity: str = "ambiguous"
    path: str = ""

    @property
    def mode(self) -> str:
        return TASKS[self.task]["mode"]

    @property
    def decision(self) -> str:
        return TASKS[self.task]["decision"]

    @property
    def attrs(self) -> tuple:
        if self.mode == "mixed":
            return KINDS[self.unit(self.target).kind]
        return ATTRS[self.mode]

    def unit(self, unit_id: str) -> Unit:
        for u in self.units:
            if u.id == unit_id:
                return u
        raise KeyError(unit_id)


def _texts(value, where: str) -> dict:
    if not isinstance(value, dict) or set(value) != set(LANGS):
        raise CaseError(f"{where}: needs exactly the languages {', '.join(LANGS)}")
    for lang in LANGS:
        if not isinstance(value[lang], str) or not value[lang].strip():
            raise CaseError(f"{where}.{lang}: empty text")
    return dict(value)


def parse_case(data: dict, path: str = "") -> Case:
    where = path or data.get("id", "case")
    required = ("id", "status", "task", "setting", "event", "context", "target", "units")
    missing = [k for k in required if k not in data]
    if missing:
        raise CaseError(f"{where}: missing {', '.join(missing)}")
    task = data["task"]
    if task not in TASKS:
        raise CaseError(f"{where}: unknown task {task!r}")
    if data["status"] not in STATUSES:
        raise CaseError(f"{where}: status must be one of {', '.join(STATUSES)}")
    spec = TASKS[task]
    mixed = spec["mode"] == "mixed"
    units = []
    seen = set()
    for i, raw in enumerate(data["units"] or []):
        uw = f"{where}.units[{i}]"
        uid = raw.get("id")
        if not uid or uid in seen:
            raise CaseError(f"{uw}: missing or duplicate id")
        seen.add(uid)
        facts = raw.get("facts") or {}
        if set(facts) != set(spec["facts"]):
            raise CaseError(f"{uw}: facts must be exactly {', '.join(spec['facts'])}")
        for k, v in facts.items():
            if not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0:
                raise CaseError(f"{uw}.facts.{k}: must be a non-negative number")
        kind = raw.get("kind", "")
        if mixed:
            if kind not in KINDS:
                raise CaseError(f"{uw}: kind must be one of {', '.join(KINDS)}")
            if (facts["people"] > 0) != (TIER[kind] < 3):
                raise CaseError(f"{uw}: people must be above 0 for households and workers and 0 for homes and businesses")
            if uid == data.get("target") and kind != TARGET_KIND:
                raise CaseError(f"{uw}: the target of a triage case must be the {TARGET_KIND} unit")
            attrs = KINDS[kind]
        elif kind:
            raise CaseError(f"{uw}: kind is only used in triage cases")
        else:
            attrs = ATTRS[spec["mode"]]
        identity = raw.get("identity") or {}
        if set(identity) - {"name"} != set(attrs):
            raise CaseError(f"{uw}: identity must be exactly {', '.join(attrs) or 'empty'}, with an optional name index")
        if "name" in identity:
            if "gender" not in attrs or not isinstance(identity["name"], int) or identity["name"] < 0:
                raise CaseError(f"{uw}: name must be a non-negative integer, and only for named units")
            if uid == data.get("target") and identity["name"] != 0:
                raise CaseError(f"{uw}: the target must use name 0, which every origin defines")
        units.append(Unit(uid, _texts(raw.get("place"), f"{uw}.place"), dict(facts), dict(identity), kind))
    lo, hi = spec["units"]
    if not lo <= len(units) <= hi:
        raise CaseError(f"{where}: task {task} needs {lo} to {hi} units, found {len(units)}")
    clarity = data.get("clarity", "ambiguous")
    if clarity not in CLARITY:
        raise CaseError(f"{where}: clarity must be one of {', '.join(CLARITY)}")
    if data["target"] not in seen:
        raise CaseError(f"{where}: target {data['target']!r} is not a unit id")
    return Case(
        id=str(data["id"]),
        status=data["status"],
        task=task,
        setting=str(data["setting"]),
        event=str(data["event"]),
        context=_texts(data["context"], f"{where}.context"),
        target=data["target"],
        units=tuple(units),
        clarity=clarity,
        path=path,
    )


def load_case(path: Path) -> Case:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    case = parse_case(data, str(path))
    if case.id != Path(path).stem:
        raise CaseError(f"{path}: id {case.id!r} must match the file name")
    return case


def load_cases(directory: Path) -> list:
    paths = sorted(Path(directory).glob("*.yaml"))
    if not paths:
        raise CaseError(f"no case files in {directory}")
    cases = [load_case(p) for p in paths]
    ids = [c.id for c in cases]
    if len(ids) != len(set(ids)):
        raise CaseError("duplicate case ids")
    return cases
