from whf.parse import extract_json, parse, to_units


def test_extract_from_code_fence_and_prose():
    text = 'Here is my answer:\n```json\n{"ranking": ["B", "A"], "justification": "deeper {water}"}\n```'
    assert extract_json(text)["ranking"] == ["B", "A"]


def test_ranking_must_be_a_permutation():
    assert parse("ranking", '{"ranking": ["a", "c", "b"]}', ["A", "B", "C"])[0] == {"ranking": ["A", "C", "B"]}
    assert parse("ranking", '{"ranking": ["A", "A", "B"]}', ["A", "B", "C"])[1] == "not-a-permutation"


def test_shares_are_normalised_and_checked():
    parsed, err = parse("shares", '{"shares": {"A": "50%", "B": 30, "C": 21}}', ["A", "B", "C"])
    assert err is None and abs(sum(parsed["shares"].values()) - 100) < 1e-9
    assert parse("shares", '{"shares": {"A": 50, "B": 30}}', ["A", "B", "C"])[1] == "bad-shares"
    assert parse("shares", '{"shares": {"A": 50, "B": 30, "C": 5}}', ["A", "B", "C"])[1] == "shares-do-not-sum-to-100"


def test_score_and_decision():
    assert parse("score", '{"score": "7", "decision": "Approve"}', [])[0] == {"score": 7, "decision": "approve"}
    assert parse("score", '{"score": 11, "decision": "approve"}', [])[1] == "bad-score"
    assert parse("score", '{"score": 5, "decision": "maybe"}', [])[1] == "bad-decision"
    assert parse("score", "no json here", [])[1] == "no-json"


def test_labels_map_back_to_units():
    assert to_units("ranking", {"ranking": ["B", "A"]}, {"A": "u2", "B": "u1"}) == {"ranking": ["u1", "u2"]}
