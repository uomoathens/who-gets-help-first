from __future__ import annotations

import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .attributes import Attributes
from .cases import Case, CaseError, load_cases, tier
from .config import Config
from .expand import Variant, expand
from .parse import parse, to_units
from .prompts import Prompts, build, stable_int
from .runners import make_runner


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_study(cfg: Config):
    attributes = Attributes.load(cfg.attributes)
    attributes.check()
    prompts = Prompts.load(cfg.prompts)
    cases = load_cases(cfg.cases)
    for c in cases:
        attributes.check_case(c)
    pending = attributes.pending_sources()
    if pending and not cfg.allow_pending_sources:
        raise CaseError("names without a published source: " + ", ".join(pending) + " (set allow_pending_sources only for pilots)")
    templates = [c.id for c in cases if c.status in ("draft", "template")]
    if templates and not cfg.allow_template_cases:
        raise CaseError("cases not yet reviewed: " + ", ".join(templates) + " (set allow_template_cases only for pilots)")
    return attributes, prompts, cases


def jobs(cfg: Config, cases: list, attributes: Attributes, prompts: Prompts):
    paraphrases = cfg.paraphrases if cfg.paraphrases is not None else list(range(prompts.paraphrases()))
    roles = cfg.roles if cfg.roles is not None else prompts.roles()
    for model in cfg.models:
        for case in cases:
            for variant in expand(case, attributes):
                for lang in cfg.languages:
                    for p in paraphrases:
                        for role in roles:
                            for run in range(cfg.runs):
                                yield model, case, variant, lang, p, role, run


def job_id(model: str, case: Case, variant: Variant, lang: str, p: int, role: str, run: int) -> str:
    return hashlib.sha256(f"{model}|{case.id}|{variant.key}|{lang}|{p}|{role}|{run}".encode()).hexdigest()[:16]


def _done(path: Path) -> set:
    if not path.exists():
        return set()
    out = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.add(json.loads(line)["job_id"])
    return out


def _file_hash(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def write_manifest(cfg: Config, cases: list) -> None:
    cfg.output.mkdir(parents=True, exist_ok=True)
    manifest = {
        "study": cfg.name,
        "package_version": __version__,
        "python": platform.python_version(),
        "written": now(),
        "languages": cfg.languages,
        "runs": cfg.runs,
        "temperature": cfg.temperature,
        "max_tokens": cfg.max_tokens,
        "models": cfg.models,
        "cases": {c.id: {"status": c.status, "sha": _file_hash(Path(c.path))} for c in cases},
        "attributes_sha": _file_hash(cfg.attributes),
        "prompts_sha": {p.name: _file_hash(p) for p in sorted(Path(cfg.prompts).glob("*.yaml"))},
    }
    with open(cfg.output / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def execute(cfg: Config, limit: int | None = None, only_model: str | None = None, log=print) -> int:
    attributes, prompts, cases = load_study(cfg)
    write_manifest(cfg, cases)
    raw_dir = cfg.output / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    runners = {}
    done = {}
    written = 0
    for model, case, variant, lang, p, role, run in jobs(cfg, cases, attributes, prompts):
        name = model["name"]
        if only_model and name != only_model:
            continue
        path = raw_dir / f"{name}.jsonl"
        if name not in done:
            done[name] = _done(path)
        jid = job_id(name, case, variant, lang, p, role, run)
        if jid in done[name]:
            continue
        if name not in runners:
            runners[name] = make_runner(model)
        runner = runners[name]
        prompt = build(case, variant, lang, p, role, run, attributes, prompts)
        mapping = dict(prompt.labels)
        seed = stable_int(cfg.seed, jid)
        context = {
            "task": case.task,
            "decision": case.decision,
            "units": {label: {"facts": case.unit(uid).facts, "kind": case.unit(uid).kind,
                              "identity": variant.identity_dict if uid == case.target else case.unit(uid).identity}
                      for label, uid in prompt.labels},
        }
        output = runner.generate(prompt.messages, seed=seed, temperature=cfg.temperature,
                                 max_tokens=cfg.max_tokens, context=context)
        parsed, error = parse(case.decision, output, list(mapping))
        record = {
            "job_id": jid, "model": name, "model_id": runner.model_id, "revision": runner.revision,
            "case": case.id, "task": case.task, "decision": case.decision, "setting": case.setting,
            "target": case.target, "units": [u.id for u in case.units], "tiers": {u.id: tier(u.kind, variant.identity_dict if u.id == case.target else u.identity) for u in case.units if u.kind},
            "variant": variant.key, "attribute": variant.attribute, "value": variant.value, "control": variant.control,
            "placebo": variant.placebo, "clarity": case.clarity,
            "language": lang, "paraphrase": p, "role": role, "run": run, "seed": seed,
            "temperature": cfg.temperature, "prompt_sha": prompt.sha, "labels": dict(prompt.labels),
            "output": output, "valid": parsed is not None, "error": error,
            "result": to_units(case.decision, parsed, mapping) if parsed else None,
            "timestamp": now(),
        }
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        done[name].add(jid)
        written += 1
        if limit and written >= limit:
            break
    log(f"wrote {written} new records to {raw_dir}")
    return written
