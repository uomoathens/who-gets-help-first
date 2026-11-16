from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from .analyze import md_table
from .config import Config, load_config
from .metrics import holm

FAIR_KEYS = ["task", "attribute", "value"]


def references(cfg_path: Path) -> tuple:
    with open(cfg_path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    if "reference" not in raw:
        raise ValueError(f"{cfg_path}: missing reference")
    pairs = {m["name"]: m["reference_model"] for m in raw["models"] if "reference_model" in m}
    if not pairs:
        raise ValueError(f"{cfg_path}: no model has a reference_model")
    return load_config(Path(cfg_path).resolve().parent.parent / raw["reference"]), pairs


def with_reportable(t: pd.DataFrame) -> pd.DataFrame:
    if "reportable" in t.columns:
        return t
    t = t.copy()
    t["p_holm"] = np.nan
    for m, idx in t.groupby("model").groups.items():
        t.loc[idx, "p_holm"] = holm(t.loc[idx, "p"])
    t["reportable"] = t["p_holm"] < 0.05
    return t


def _kappa(a: pd.Series, b: pd.Series) -> float:
    x, y = a.astype(float).to_numpy(), b.astype(float).to_numpy()
    if x.size < 2:
        return np.nan
    po = float((x == y).mean())
    pe = float(x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean()))
    return float((po - pe) / (1 - pe)) if pe < 1 else (1.0 if po == 1 else np.nan)


def compare_fairness(ref: pd.DataFrame, rep: pd.DataFrame, ref_model: str, rep_model: str, min_clusters: int) -> pd.DataFrame:
    a = ref[(ref["model"] == ref_model) & (ref["cases"] >= min_clusters)]
    b = rep[(rep["model"] == rep_model) & (rep["cases"] >= min_clusters)]
    m = a.merge(b, on=FAIR_KEYS, suffixes=("_ref", "_rep"))
    return m[FAIR_KEYS + ["shift_ref", "shift_rep", "p_holm_ref", "p_holm_rep", "reportable_ref", "reportable_rep"]]


def summarise(m: pd.DataFrame, label: str) -> dict:
    if m.empty:
        return dict(table=label, rows=0)
    both = m["reportable_ref"] & m["reportable_rep"]
    rep_ref = m[m["reportable_ref"]]
    return dict(
        table=label,
        rows=len(m),
        correlation=float(np.corrcoef(m["shift_ref"], m["shift_rep"])[0, 1]) if len(m) > 2 else np.nan,
        same_sign=float((np.sign(m["shift_ref"]) == np.sign(m["shift_rep"])).mean()),
        reportable_ref=int(m["reportable_ref"].sum()),
        reportable_rep=int(m["reportable_rep"].sum()),
        reportable_both=int(both.sum()),
        same_sign_where_reportable=float((np.sign(rep_ref["shift_ref"]) == np.sign(rep_ref["shift_rep"])).mean()) if len(rep_ref) else np.nan,
        kappa_reportable=_kappa(m["reportable_ref"], m["reportable_rep"]),
    )


def compare(cfg_path: Path, log=print) -> Path:
    cfg: Config = load_config(cfg_path)
    ref_cfg, pairs = references(cfg_path)
    ra, rb = ref_cfg.output / "analysis", cfg.output / "analysis"
    fa, fb = pd.read_csv(ra / "fairness.csv"), pd.read_csv(rb / "fairness.csv")
    ca, cb = with_reportable(pd.read_csv(ra / "crosslingual.csv")), with_reportable(pd.read_csv(rb / "crosslingual.csv"))
    ka, kb = pd.read_csv(ra / "controls.csv"), pd.read_csv(rb / "controls.csv")
    rows, details = [], []
    for rep_model, ref_model in pairs.items():
        f = compare_fairness(fa, fb, ref_model, rep_model, cfg.min_clusters)
        details.append(f.assign(model=rep_model, reference_model=ref_model))
        rows.append(dict(model=rep_model, reference_model=ref_model, **summarise(f, "fairness")))
        c = ca[ca["model"] == ref_model].merge(cb[cb["model"] == rep_model], on=["task", "pair"], suffixes=("_ref", "_rep"))
        c = c.rename(columns={"difference_ref": "shift_ref", "difference_rep": "shift_rep"})[["task", "pair", "shift_ref", "shift_rep", "reportable_ref", "reportable_rep"]]
        rows.append(dict(model=rep_model, reference_model=ref_model, **summarise(c, "crosslingual")))
        k = ka[ka["model"] == ref_model].merge(kb[kb["model"] == rep_model], on=["task", "value"], suffixes=("_ref", "_rep"))
        rows.append(dict(model=rep_model, reference_model=ref_model, table="controls", rows=len(k),
                         correlation=float(np.corrcoef(k["raised_ref"], k["raised_rep"])[0, 1]) if len(k) > 2 else np.nan,
                         mean_raised_ref=float(k["raised_ref"].mean()) if len(k) else np.nan,
                         mean_raised_rep=float(k["raised_rep"].mean()) if len(k) else np.nan))
    summary = pd.DataFrame(rows)
    detail = pd.concat(details, ignore_index=True) if details else pd.DataFrame()
    summary.to_csv(rb / "comparison.csv", index=False)
    detail.to_csv(rb / "comparison_fairness.csv", index=False)
    text = [
        f"# Replication: {cfg.name} against {ref_cfg.name}\n",
        "Each replicated model is compared with its reference model on the same cases, languages and runs. correlation: Pearson correlation of the estimates; same_sign: share of rows whose estimates have the same sign; reportable_both: rows reportable in both; kappa_reportable: Cohen's kappa for the reportable flag.\n",
        md_table(summary),
        "## Fairness rows reportable in either run\n",
        md_table(detail[detail["reportable_ref"] | detail["reportable_rep"]] if not detail.empty else detail),
    ]
    (rb / "comparison.md").write_text("\n".join(text), encoding="utf-8")
    log(f"comparison written to {rb}")
    return rb
