import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY_IMAGE = "ghcr.io/ggml-org/llama.cpp@sha256:8c74db29f1a2bef3f0a331b52c4d6214601dfceed4bee0b94cc48b3b23ff257d"


def test_study_and_replication_use_the_study_server_build():
    for name in ("study.yml", "replication.yml"):
        text = (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
        assert f"IMAGE: {STUDY_IMAGE}" in text, name
        assert "llama.cpp:server" not in text, name


def test_study_answers_came_from_the_pinned_build():
    digests = {p.read_text(encoding="utf-8").strip() for p in (ROOT / "results" / "study-cpu" / "models").glob("*.server")}
    assert digests == {STUDY_IMAGE}


def test_pinned_replication_matches_the_first_except_its_output():
    a = (ROOT / "config" / "replication-q8.yaml").read_text(encoding="utf-8").splitlines()
    b = (ROOT / "config" / "replication-q8-pinned.yaml").read_text(encoding="utf-8").splitlines()
    diff = [(x, y) for x, y in zip(a, b) if x != y]
    assert len(a) == len(b)
    assert [re.split(r":\s*", x)[0] for x, _ in diff] == ["name", "output"]
