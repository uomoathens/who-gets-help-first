import numpy as np

from whf.metrics import changed, cluster_bootstrap, holm, kendalls_w, krippendorff_interval, target_outcome


def test_target_outcome_scales():
    assert target_outcome("ranking", {"ranking": ["u2", "u1", "u3"]}, "u2", 3) == 2
    assert target_outcome("ranking", {"ranking": ["u2", "u1", "u3"]}, "u3", 3) == 0
    assert target_outcome("shares", {"shares": {"u1": 60.0, "u2": 40.0}}, "u2", 2) == 40
    assert target_outcome("score", {"score": 6, "decision": "decline"}, "u1", 1) == 6


def test_changed():
    assert changed("ranking", {"ranking": ["a", "b"]}, {"ranking": ["b", "a"]}, "a", 5)
    assert not changed("shares", {"shares": {"a": 40}}, {"shares": {"a": 43}}, "a", 5)
    assert changed("score", {"score": 6, "decision": "decline"}, {"score": 6, "decision": "approve"}, "u", 5)


def test_kendalls_w_bounds():
    same = np.array([[1, 2, 3, 4]] * 5)
    assert kendalls_w(same) == 1.0
    opposite = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
    assert kendalls_w(opposite) == 0.0


def test_kendalls_w_textbook_value():
    r = np.array([[1, 2, 3], [1, 3, 2], [2, 1, 3]])
    assert abs(kendalls_w(r) - 4 / 9) < 1e-12


def test_krippendorff_interval():
    assert krippendorff_interval(np.array([[1, 2, 3, 4], [1, 2, 3, 4]])) == 1.0
    noisy = krippendorff_interval(np.array([[1, 2, 3, 4], [4, 1, 2, 3]]))
    assert noisy < 0.5
    missing = np.array([[1, 2, np.nan], [1, 2, 3]])
    assert krippendorff_interval(missing) == 1.0


def test_bootstrap_detects_a_shift_and_not_noise():
    rng = np.random.default_rng(1)
    clusters = np.repeat(np.arange(30), 10)
    shifted = rng.normal(-1, 1, size=300)
    est, lo, hi, p = cluster_bootstrap(shifted, clusters, 1000, 0)
    assert hi < 0 and p < 0.01
    flat = np.zeros(300)
    assert cluster_bootstrap(flat, clusters, 200, 0)[3] == 1.0


def test_holm_known_values():
    adj = holm([0.01, 0.04, 0.03])
    assert np.allclose(adj, [0.03, 0.06, 0.06])
