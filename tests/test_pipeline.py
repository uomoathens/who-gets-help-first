import json
import shutil
from pathlib import Path

import pandas as pd
import yaml

from whf.analyze import analyze
from whf.config import load_config
from whf.run import execute

ROOT = Path(__file__).resolve().parent.parent


def _config(tmp_path: Path) -> Path:
    for d in ("cases", "attributes", "prompts"):
        shutil.copytree(ROOT / d, tmp_path / d)
    (tmp_path / "config").mkdir()
    raw = yaml.safe_load((ROOT / "config" / "ci.yaml").read_text(encoding="utf-8"))
    raw["output"] = "results/test"
    raw["runs"] = 2
    raw["bootstrap"] = 300
    path = tmp_path / "config" / "test.yaml"
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    return path


def test_mock_pipeline_finds_injected_bias_only(tmp_path):
    cfg = load_config(_config(tmp_path))
    n = execute(cfg, log=lambda *_: None)
    assert n > 0
    assert execute(cfg, log=lambda *_: None) == 0
    out = analyze(cfg, log=lambda *_: None)
    f = pd.read_csv(out / "fairness.csv")
    dispatch = f[(f["task"] == "dispatch") & (f["attribute"] == "origin") & (f["value"] == "syrian")]
    biased = dispatch[dispatch["model"] == "mock-biased"].iloc[0]
    fair = dispatch[dispatch["model"] == "mock-fair"].iloc[0]
    assert biased["shift"] < 0 and biased["flip_rate"] > fair["flip_rate"]
    assert abs(fair["shift"]) < abs(biased["shift"])
    assert abs(fair["excess_flip"]) < 0.15 and biased["excess_flip"] > 0.2
    noise = pd.read_csv(out / "noise_floor.csv")
    assert set(noise["model"]) == {"mock-fair", "mock-biased"}
    c = pd.read_csv(out / "controls.csv")
    assert (c["raised"] > 0.5).all()
    v = pd.read_csv(out / "validity.csv")
    assert (v["valid_share"] == 1).all()
    r = pd.read_csv(out / "priority_rule.csv")
    assert set(r["task"]) == {"triage"} and (r["follows_rule"] == 1).all()
    assert (out / "report.md").exists()


def test_run_refuses_unreviewed_cases_by_default(tmp_path):
    path = _config(tmp_path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw["allow_template_cases"] = False
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    cfg = load_config(path)
    try:
        execute(cfg, log=lambda *_: None)
    except ValueError as e:
        assert "not yet reviewed" in str(e)
    else:
        raise AssertionError("expected a refusal")


def test_many_cases_give_intervals_and_find_only_the_planted_bias(tmp_path):
    path = _config(tmp_path)
    src = tmp_path / "cases" / "templates"
    many = tmp_path / "cases" / "many"
    many.mkdir()
    for f in src.glob("*.yaml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        for i in range(8):
            d = yaml.safe_load(f.read_text(encoding="utf-8"))
            d["id"] = f"{data['id']}-{i}"
            for u in d["units"]:
                for k, v in u["facts"].items():
                    u["facts"][k] = round(v * (1 + 0.04 * ((i + len(u["id"])) % 5 - 2)), 1) if isinstance(v, float) else (v + (i % 3) if v else v)
            (many / f"{d['id']}.yaml").write_text(yaml.safe_dump(d, allow_unicode=True), encoding="utf-8")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw.update(cases="cases/many", runs=1, paraphrases=[0], roles=["officer"], bootstrap=400)
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    cfg = load_config(path)
    execute(cfg, log=lambda *_: None)
    out = analyze(cfg, log=lambda *_: None)
    f = pd.read_csv(out / "fairness.csv")
    assert f["shift_lo"].notna().all()
    planted = f[(f["model"] == "mock-biased") & (f["task"] != "triage") & (f["value"].isin(["syrian", "local_migrant", "roma_settlement"]))]
    assert (planted["shift_hi"] < 0).all() and planted["reportable"].all()
    fair = f[f["model"] == "mock-fair"]
    assert not fair["reportable"].any()
    m = pd.read_csv(out / "mixed_models.csv")
    assert m["estimate"].notna().any()


def test_case_ids_select_cases_and_reject_unknown_ids(tmp_path):
    from whf.cases import CaseError
    from whf.run import load_study
    path = _config(tmp_path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw["case_ids"] = ["thessaly-dispatch-01", "valencia-housing-01"]
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    _, _, cases = load_study(load_config(path))
    assert sorted(c.id for c in cases) == ["thessaly-dispatch-01", "valencia-housing-01"]
    raw["case_ids"] = ["no-such-case"]
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    try:
        load_study(load_config(path))
    except CaseError as e:
        assert "no-such-case" in str(e)
    else:
        raise AssertionError("unknown case id accepted")


def test_shards_split_the_work_and_resume(tmp_path):
    from whf.run import plan
    path = _config(tmp_path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    for m in raw["models"]:
        m["shards"] = 3
        m["gguf"] = {"repo": "org/repo", "file": "model.gguf"}
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    cfg = load_config(path)
    work = plan(cfg)
    total = sum(w["left"] for w in work)
    assert len(work) == 6 and work[0]["repo"] == "org/repo" and work[1]["tag"] == "mock-fair--01"
    assert execute(cfg, log=lambda *_: None, only_model="mock-fair", shard=1, shards=3, limit=5) == 5
    assert sum(w["left"] for w in plan(cfg)) == total - 5
    for k in range(3):
        execute(cfg, log=lambda *_: None, only_model="mock-fair", shard=k, shards=3)
    assert {w["name"] for w in plan(cfg)} == {"mock-biased"}
    files = sorted(p.name for p in (cfg.output / "raw").glob("mock-fair*.jsonl"))
    assert files == ["mock-fair--00.jsonl", "mock-fair--01.jsonl", "mock-fair--02.jsonl"]
    ids = [json.loads(line)["job_id"] for f in files for line in open(cfg.output / "raw" / f, encoding="utf-8")]
    assert len(ids) == len(set(ids)) == total // 2
    assert execute(cfg, log=lambda *_: None, only_model="mock-fair") == 0


def test_a_cut_last_line_is_skipped_and_rerun(tmp_path):
    cfg = load_config(_config(tmp_path))
    execute(cfg, log=lambda *_: None, only_model="mock-fair", limit=3)
    path = cfg.output / "raw" / "mock-fair.jsonl"
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(lines[:2]) + "\n" + lines[2][:40], encoding="utf-8")
    assert execute(cfg, log=lambda *_: None, only_model="mock-fair", limit=1) == 1
    ids = [json.loads(x)["job_id"] for x in path.read_text(encoding="utf-8").splitlines() if x.startswith("{") and x.endswith("}")]
    assert len(ids) == 3 and ids[2] == json.loads(lines[2])["job_id"]
