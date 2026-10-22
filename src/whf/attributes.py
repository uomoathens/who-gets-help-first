from __future__ import annotations

from pathlib import Path

import yaml

from .cases import LANGS, Case, CaseError

GENDERS = ("male", "female")


class Attributes:
    def __init__(self, data: dict):
        self.data = data
        self.controls = data["controls"]
        self.status = data["status"]
        self.settings = data["settings"]

    @classmethod
    def load(cls, path: Path) -> "Attributes":
        with open(path, encoding="utf-8") as f:
            return cls(yaml.safe_load(f))

    def setting(self, name: str) -> dict:
        if name not in self.settings:
            raise CaseError(f"unknown setting {name!r}")
        return self.settings[name]

    def values(self, setting: str, attr: str) -> list:
        s = self.setting(setting)
        if attr == "origin":
            return list(s["origin"])
        if attr == "area":
            return list(s["area"])
        if attr == "gender":
            return list(GENDERS)
        if attr == "status":
            return list(self.status)
        if attr == "need":
            return list(self.controls)
        raise KeyError(attr)

    def pending_sources(self) -> list:
        out = []
        for sname, s in self.settings.items():
            for oname, o in s["origin"].items():
                if str(o.get("source", "pending")).strip().lower().startswith("pending") or not str(o.get("source", "")).strip():
                    out.append(f"{sname}.origin.{oname}")
        return out

    def name(self, setting: str, identity: dict, lang: str) -> str:
        names = self.setting(setting)["origin"][identity["origin"]]["person"][identity["gender"]]
        return names[identity.get("name", 0)][lang]

    def check_case(self, case: Case) -> None:
        for u in case.units:
            for attr, value in u.identity.items():
                if attr == "name":
                    continue
                if value not in self.values(case.setting, attr):
                    raise CaseError(f"{case.id}.{u.id}: {attr}={value!r} is not defined for setting {case.setting}")
            if "gender" in u.identity:
                names = self.setting(case.setting)["origin"][u.identity["origin"]]["person"][u.identity["gender"]]
                if u.identity.get("name", 0) >= len(names):
                    raise CaseError(f"{case.id}.{u.id}: name index {u.identity.get('name', 0)} is not defined")
        named = [u for u in case.units if "gender" in u.identity]
        if named:
            seen = set()
            tid = case.unit(case.target).identity
            tkey = (tid["origin"], tid["gender"], 0) if "gender" in tid else None
            for u in named:
                if u.id == case.target:
                    continue
                key = (u.identity["origin"], u.identity["gender"], u.identity.get("name", 0))
                if key in seen or key == tkey:
                    raise CaseError(f"{case.id}.{u.id}: another unit already uses this name")
                seen.add(key)

    def check(self) -> None:
        for name in self.controls:
            for mode in ("person", "community", "workers"):
                self._langs(self.controls[name][mode], f"controls.{name}.{mode}", allow_empty=name == "none")
        for name, st in self.status.items():
            for g in GENDERS:
                self._langs(st[g], f"status.{name}.{g}")
        for sname, s in self.settings.items():
            ref = s["reference"]
            for oname, o in s["origin"].items():
                for g in GENDERS:
                    names = o["person"][g]
                    if not isinstance(names, list) or not names:
                        raise CaseError(f"{sname}.origin.{oname}.person.{g}: needs a list of names")
                    for i, n in enumerate(names):
                        self._langs(n, f"{sname}.origin.{oname}.person.{g}[{i}]")
                self._langs(o["community"], f"{sname}.origin.{oname}.community")
                self._langs(o["workers"], f"{sname}.origin.{oname}.workers")
            for aname, a in s["area"].items():
                for mode in ("person", "community"):
                    self._langs(a[mode], f"{sname}.area.{aname}.{mode}")
                    for lang in LANGS:
                        if "{place}" not in a[mode][lang]:
                            raise CaseError(f"{sname}.area.{aname}.{mode}.{lang}: missing {{place}}")
            for attr, value in ref.items():
                if value not in self.values(sname, attr):
                    raise CaseError(f"{sname}.reference.{attr}: {value!r} undefined")

    @staticmethod
    def _langs(value, where: str, allow_empty: bool = False) -> None:
        if not isinstance(value, dict) or set(value) != set(LANGS):
            raise CaseError(f"{where}: needs exactly the languages {', '.join(LANGS)}")
        if not allow_empty and any(not str(value[lang]).strip() for lang in LANGS):
            raise CaseError(f"{where}: empty text")
