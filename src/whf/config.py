from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .cases import LANGS


@dataclass
class Config:
    name: str
    root: Path
    cases: Path
    attributes: Path
    prompts: Path
    output: Path
    models: list
    languages: list = field(default_factory=lambda: list(LANGS))
    paraphrases: list | None = None
    roles: list | None = None
    runs: int = 5
    temperature: float = 0.7
    max_tokens: int = 400
    allow_pending_sources: bool = False
    allow_template_cases: bool = False
    bootstrap: int = 2000
    share_flip_tolerance: float = 5.0
    smallest_effect: float = 0.05
    min_clusters: int = 8
    seed: int = 20261022


def load_config(path: Path) -> Config:
    path = Path(path)
    root = path.resolve().parent.parent
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    for key in ("name", "cases", "attributes", "prompts", "output", "models"):
        if key not in raw:
            raise ValueError(f"{path}: missing {key}")
    names = [m["name"] for m in raw["models"]]
    if len(names) != len(set(names)):
        raise ValueError(f"{path}: model names must be unique")
    for lang in raw.get("languages", LANGS):
        if lang not in LANGS:
            raise ValueError(f"{path}: unknown language {lang}")
    kw = {k: raw[k] for k in ("languages", "paraphrases", "roles", "runs", "temperature", "max_tokens",
                              "allow_pending_sources", "allow_template_cases", "bootstrap",
                              "share_flip_tolerance", "smallest_effect", "min_clusters", "seed") if k in raw}
    return Config(
        name=raw["name"],
        root=root,
        cases=root / raw["cases"],
        attributes=root / raw["attributes"],
        prompts=root / raw["prompts"],
        output=root / raw["output"],
        models=raw["models"],
        **kw,
    )
