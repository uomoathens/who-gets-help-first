from pathlib import Path

import numpy as np
import pandas as pd

from whf.analyze import origin_signal, reportable_summary, signal_summary, without_origins
from whf.attributes import Attributes
from whf.compare import compare_fairness, summarise
from whf.config import load_config
from whf.review import cohens_kappa, make_sheet, read_sheet, sample_cases
from whf.run import load_study

ROOT = Path(__file__).resolve().parent.parent


def test_unsourced_origins_are_only_the_syrian_names():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    assert attributes.unsourced_origins() == ["syrian"]


def test_origin_signal_follows_the_task_mode():
    assert origin_signal("dispatch") == "name"
    assert origin_signal("housing") == "name"
    assert origin_signal("evacuation") == "statement"
    assert origin_signal("relief") == "statement"
    assert origin_signal("triage") == "statement"


def test_without_origins_keeps_other_attributes():
    pairs = pd.DataFrame({"attribute": ["origin", "origin", "area"], "value": ["syrian", "romanian", "syrian"]})
    out = without_origins(pairs, ["syrian"])
    assert list(zip(out["attribute"], out["value"])) == [("origin", "romanian"), ("area", "syrian")]


def _fair(model, rows):
    return pd.DataFrame([dict(model=model, task=t, attribute=a, value=v, cases=15, shift=s, p_holm=p, reportable=r, signal=g)
                         for t, a, v, s, p, r, g in rows])


def test_summaries_count_reportable_rows():
    cfg = load_config(ROOT / "config" / "study-cpu.yaml")
    full = _fair("m", [("evacuation", "origin", "syrian", 0.5, 0.0, True, "statement"),
                       ("dispatch", "origin", "syrian", 0.1, 0.9, False, "name"),
                       ("housing", "area", "villas", -0.4, 0.0, True, "")])
    reduced = full[full["value"] != "syrian"]
    s = reportable_summary(full, reduced, cfg)
    assert s["reportable"].tolist() == [2, 1]
    assert s["raised"].tolist() == [1, 0]
    g = signal_summary(full, cfg).set_index("signal")
    assert g.loc["statement", "reportable"] == 1 and g.loc["name", "reportable"] == 0


def test_comparison_of_identical_runs_agrees_fully():
    rows = [("evacuation", "origin", "syrian", 0.5, 0.0, True, "statement"),
            ("dispatch", "origin", "syrian", -0.1, 0.9, False, "name"),
            ("housing", "area", "villas", -0.4, 0.0, True, "")]
    m = compare_fairness(_fair("m", rows), _fair("m", rows), "m", "m", 8)
    s = summarise(m, "fairness")
    assert s["rows"] == 3 and s["reportable_both"] == 2 and s["same_sign"] == 1.0
    assert np.isclose(s["correlation"], 1.0) and s["kappa_reportable"] == 1.0


def test_cohens_kappa():
    assert cohens_kappa([True, False, True, False], [True, False, True, False]) == 1.0
    assert np.isnan(cohens_kappa([True], [True]))


def test_review_sheet_round_trip(tmp_path):
    cfg = load_config(ROOT / "config" / "study-cpu.yaml")
    _, _, cases = load_study(cfg)
    chosen = sample_cases(cases, 3, cfg.seed)
    assert len(chosen) == 15
    for task in {c.task for c in chosen}:
        group = [c for c in chosen if c.task == task]
        assert len({c.setting for c in group}) == 3 and len({c.clarity for c in group}) == 2
    path = tmp_path / "sheet.xlsx"
    ids = make_sheet(cfg, path)
    assert ids == [c.id for c in chosen]
    read = read_sheet(path)
    assert set(read) == set(ids) and all(v["clear"] is None for v in read.values())
