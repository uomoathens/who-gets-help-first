from __future__ import annotations

from dataclasses import dataclass

from .attributes import Attributes
from .cases import Case


@dataclass(frozen=True)
class Variant:
    case_id: str
    key: str
    attribute: str | None
    value: str | None
    identity: tuple
    control: bool
    placebo: bool = False

    @property
    def identity_dict(self) -> dict:
        return dict(self.identity)


def expand(case: Case, attributes: Attributes) -> list:
    base = case.unit(case.target).identity
    out = [Variant(case.id, "base", None, None, tuple(sorted(base.items())), False),
           Variant(case.id, "placebo", "placebo", "rerun", tuple(sorted(base.items())), False, True)]
    for attr in case.attrs:
        for value in attributes.values(case.setting, attr):
            if value == base[attr]:
                continue
            ident = dict(base)
            ident[attr] = value
            out.append(Variant(case.id, f"{attr}={value}", attr, value, tuple(sorted(ident.items())), attr == "need"))
    return out
