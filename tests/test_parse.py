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
    parsed, err = parse("shares", '{"shares": {"A": 50, "B": 30, "C": 5}}', ["A", "B", "C"])
    assert err is None and parsed["rescaled"] and abs(sum(parsed["shares"].values()) - 100) < 1e-9
    assert "rescaled" not in parse("shares", '{"shares": {"A": 50, "B": 30, "C": 21}}', ["A", "B", "C"])[0]
    assert parse("shares", '{"shares": {"A": 0, "B": 0, "C": 0}}', ["A", "B", "C"])[1] == "shares-do-not-sum-to-100"


def test_score_and_decision():
    assert parse("score", '{"score": "7", "decision": "Approve"}', [])[0] == {"score": 7, "decision": "approve"}
    assert parse("score", '{"score": 11, "decision": "approve"}', [])[1] == "bad-score"
    assert parse("score", '{"score": 5, "decision": "maybe"}', [])[1] == "bad-decision"
    assert parse("score", "no json here", [])[1] == "no-json"


def test_labels_map_back_to_units():
    assert to_units("ranking", {"ranking": ["B", "A"]}, {"A": "u2", "B": "u1"}) == {"ranking": ["u1", "u2"]}


def test_labels_with_words_or_greek_letters_are_accepted():
    labels = ["A", "B", "C", "D", "E"]
    out, err = parse("ranking", '{"ranking": ["Κλήση D", "Κλήση A", "Κλήση E", "Κλήση C", "Κλήση B"]}', labels)
    assert err is None and out["ranking"] == ["D", "A", "E", "C", "B"]
    out, err = parse("ranking", '{"ranking": ["Area C", "Area A", "Area D", "Area B", "Area E"]}', labels)
    assert err is None and out["ranking"][0] == "C"
    out, err = parse("ranking", '{"ranking": ["Δ", "Α", "Ε", "Β", "Γ"]}', labels)
    assert err is None and out["ranking"] == ["D", "A", "E", "B", "C"]


def test_comments_and_truncated_justifications_are_tolerated():
    labels = ["A", "B", "C", "D"]
    text = '```json\n{"shares": {"A": 25, "B": 23, "C": 30, // dialysis\n "D": 22}, "justification": "x"}\n```'
    out, err = parse("shares", text, labels)
    assert err is None and abs(out["shares"]["C"] - 30) < 1e-9
    text = '{"ranking": ["Κλήση B", "Κλήση D", "Κλήση A", "Κλήση C"], "justification": "Η Κλήση B έχει το πιο βαθύ νερό'
    out, err = parse("ranking", text, labels)
    assert err is None and out["ranking"] == ["B", "D", "A", "C"]


def test_extra_labels_and_wrong_sums_stay_invalid():
    labels = ["A", "B", "C", "D", "E"]
    assert parse("ranking", '{"ranking": ["B", "A", "D", "C", "E", "G"]}', labels)[1] == "not-a-permutation"
    assert parse("ranking", '{"ranking": ["Δ", "Α", "Ε", "Β", "Κ", "Κ"]}', labels)[1] == "not-a-permutation"


def test_wrong_sums_are_rescaled_and_flagged():
    out, err = parse("shares", '{"shares": {"A": 800, "B": 800, "C": 600, "D": 400}}', ["A", "B", "C", "D"])
    assert err is None and out["rescaled"] and abs(out["shares"]["D"] - 200 / 13) < 1e-9
    assert to_units("shares", out, {"A": "u1", "B": "u2", "C": "u3", "D": "u4"})["rescaled"]


def test_truncated_answer_with_inner_object_is_read():
    text = '```json\n{\n  "shares": {\n    "A": 35,\n    "B": 30,\n    "C": 20,\n    "D": 15\n  },\n  "justification": "Η συνοικία A με τον μεγαλύτερο'
    out, err = parse("shares", text, ["A", "B", "C", "D"])
    assert err is None and abs(out["shares"]["A"] - 35) < 1e-9


def test_names_map_to_their_labels():
    labels = ["A", "B", "C", "D", "E"]
    texts = {"A": "A: María José López, 4 people", "B": "B: Francisco Pérez, 2 people", "C": "C: shop", "D": "D: home", "E": "E: workers at a warehouse"}
    out, err = parse("ranking", '{"ranking": ["María José López", "Francisco Perez", "C", "E", "D"]}', labels, texts=texts)
    assert err is None and out["ranking"] == ["A", "B", "C", "E", "D"]
    assert parse("ranking", '{"ranking": ["María José López", "Francisco Pérez", "C", "B", "D"]}', labels, texts=texts)[1] == "not-a-permutation"
    assert parse("ranking", '{"ranking": ["people", "A", "C", "E", "D"]}', labels, texts=texts)[1] == "not-a-permutation"
