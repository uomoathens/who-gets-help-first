from __future__ import annotations

import numpy as np


def target_outcome(decision: str, result: dict, target: str, n_units: int) -> float:
    if decision == "ranking":
        return float(n_units - 1 - result["ranking"].index(target))
    if decision == "shares":
        return float(result["shares"][target])
    return float(result["score"])


def changed(decision: str, base: dict, other: dict, target: str, share_tolerance: float) -> bool:
    if decision == "ranking":
        return base["ranking"].index(target) != other["ranking"].index(target)
    if decision == "shares":
        return abs(base["shares"][target] - other["shares"][target]) >= share_tolerance
    return base["score"] != other["score"] or base["decision"] != other["decision"]


def cluster_bootstrap(values, clusters, n_boot: int = 2000, seed: int = 0):
    values = np.asarray(values, dtype=float)
    clusters = np.asarray(clusters)
    if values.size == 0:
        return np.nan, np.nan, np.nan, np.nan
    est = float(values.mean())
    keys, idx = np.unique(clusters, return_inverse=True)
    k = keys.size
    sums = np.bincount(idx, weights=values, minlength=k)
    counts = np.bincount(idx, minlength=k).astype(float)
    if k < 2:
        return est, np.nan, np.nan, np.nan
    rng = np.random.default_rng(seed)
    draw = rng.integers(0, k, size=(n_boot, k))
    boot = sums[draw].sum(axis=1) / counts[draw].sum(axis=1)
    lo, hi = np.quantile(boot, [0.025, 0.975])
    if np.allclose(boot, 0):
        p = 1.0
    else:
        p = float(min(1.0, 2 * min((boot <= 0).mean(), (boot >= 0).mean())))
    return est, float(lo), float(hi), p


def holm(pvalues):
    p = np.asarray(pvalues, dtype=float)
    out = np.full_like(p, np.nan)
    ok = ~np.isnan(p)
    if not ok.any():
        return out
    q = p[ok]
    order = np.argsort(q)
    m = q.size
    adj = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * q[i])
        adj[i] = min(1.0, running)
    out[ok] = adj
    return out


def kendalls_w(ranks) -> float:
    r = np.asarray(ranks, dtype=float)
    m, n = r.shape
    if m < 2 or n < 2:
        return np.nan
    totals = r.sum(axis=0)
    s = float(((totals - totals.mean()) ** 2).sum())
    return 12 * s / (m ** 2 * (n ** 3 - n))


def krippendorff_interval(data) -> float:
    d = np.asarray(data, dtype=float)
    pairable = []
    within = 0.0
    for col in d.T:
        v = col[~np.isnan(col)]
        mu = v.size
        if mu < 2:
            continue
        diff = (v[:, None] - v[None, :]) ** 2
        within += diff.sum() / (mu - 1)
        pairable.append(v)
    if not pairable:
        return np.nan
    allv = np.concatenate(pairable)
    n = allv.size
    expected = ((allv[:, None] - allv[None, :]) ** 2).sum() / (n * (n - 1))
    observed = within / n
    if expected == 0:
        return 1.0 if observed == 0 else np.nan
    return float(1 - observed / expected)
