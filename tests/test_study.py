from pathlib import Path

import pytest
import yaml

from whf.attributes import Attributes
from whf.cases import CaseError, load_cases, parse_case
from whf.expand import expand
from whf.prompts import Prompts, build, number

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def study():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    attributes.check()
    prompts = Prompts.load(ROOT / "prompts")
    cases = load_cases(ROOT / "cases" / "templates")
    for c in cases:
        attributes.check_case(c)
    return attributes, prompts, cases


def test_templates_cover_every_task(study):
    _, _, cases = study
    assert {c.task for c in cases} == {"dispatch", "evacuation", "relief", "housing", "triage"}


def test_variant_counts(study):
    attributes, _, cases = study
    counts = {c.id: len(expand(c, attributes)) for c in cases}
    assert counts["thessaly-dispatch-01"] == 16
    assert counts["valencia-housing-01"] == 15
    assert counts["thessaly-evacuation-01"] == 13
    assert counts["valais-evacuation-01"] == 12
    assert counts["valencia-relief-01"] == 12
    assert counts["thessaly-triage-01"] == 10


def test_variants_change_exactly_one_attribute(study):
    attributes, _, cases = study
    for c in cases:
        variants = expand(c, attributes)
        base = variants[0].identity_dict
        assert variants[0].key == "base"
        assert variants[1].key == "placebo" and variants[1].identity == variants[0].identity
        for v in variants[2:]:
            diff = {k for k in base if base[k] != v.identity_dict[k]}
            assert diff == {v.attribute}


def test_prompts_render_without_placeholders(study):
    attributes, prompts, cases = study
    for c in cases:
        for v in expand(c, attributes):
            for lang in ("el", "fr", "en"):
                for p in range(prompts.paraphrases()):
                    for role in prompts.roles():
                        text = build(c, v, lang, p, role, 0, attributes, prompts).messages[1]["content"]
                        for token in ("{identity}", "{place}", "{name}", "{status}", "{area}", "{need}", "{label}", "{example}"):
                            assert token not in text


def test_unit_order_is_paired_across_variants(study):
    attributes, prompts, cases = study
    for c in cases:
        variants = expand(c, attributes)
        for run in range(3):
            orders = {build(c, v, "en", 0, "officer", run, attributes, prompts).labels for v in variants}
            assert len(orders) == 1


def test_target_text_changes_only_in_target(study):
    attributes, prompts, cases = study
    c = next(x for x in cases if x.task == "dispatch")
    variants = {v.key: v for v in expand(c, attributes)}
    a = build(c, variants["base"], "en", 0, "officer", 0, attributes, prompts).messages[1]["content"].splitlines()
    b = build(c, variants["origin=syrian"], "en", 0, "officer", 0, attributes, prompts).messages[1]["content"].splitlines()
    changed = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
    assert len(changed) == 1
    assert "Ahmad Al-Hassan" in b[changed[0]] and "Georgios Vlachos" in a[changed[0]]


def test_greek_and_french_use_decimal_comma():
    assert number(1.3, ",") == "1,3"
    assert number(1.0, ",") == "1"
    assert number(35, ",") == "35"


def test_case_validation_rejects_bad_facts():
    data = yaml.safe_load((ROOT / "cases" / "templates" / "valencia-housing-01.yaml").read_text(encoding="utf-8"))
    data["units"][0]["facts"].pop("nights")
    with pytest.raises(CaseError):
        parse_case(data)


def test_every_name_list_has_a_source(study):
    attributes, _, _ = study
    assert attributes.pending_sources() == []


def test_pending_sources_are_reported():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    attributes.settings["valais"]["origin"]["swiss"]["source"] = "Pending for first names."
    attributes.settings["thessaly"]["origin"]["syrian"]["source"] = ""
    assert attributes.pending_sources() == ["thessaly.origin.syrian", "valais.origin.swiss"]


UP = {"hours": -1}


def _urgency(facts):
    return tuple(UP.get(k, 1) * v for k, v in facts.items())


def _dominates(a, b):
    return all(x >= y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))


def test_study_cases_follow_the_design():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    cases = load_cases(ROOT / "cases" / "study")
    for c in cases:
        attributes.check_case(c)
    by_task = {}
    for c in cases:
        by_task.setdefault(c.task, []).append(c)
    assert {t: len(v) for t, v in by_task.items()} == {"dispatch": 15, "evacuation": 15, "relief": 15, "housing": 15, "triage": 15}
    for task, group in by_task.items():
        assert {s: sum(c.setting == s for c in group) for s in ("thessaly", "valais", "valencia")} == {"thessaly": 5, "valais": 5, "valencia": 5}
        assert sum(c.clarity == "clear" for c in group) == 6
    for c in cases:
        if c.task in ("housing", "triage"):
            continue
        target = _urgency(c.unit(c.target).facts)
        others = [_urgency(u.facts) for u in c.units if u.id != c.target]
        if c.clarity == "ambiguous":
            assert not any(_dominates(o, target) or _dominates(target, o) for o in others), c.id
        else:
            assert any(_dominates(o, target) for o in others) and any(_dominates(target, o) for o in others), c.id
            assert all(_dominates(o, target) or _dominates(target, o) for o in others), c.id


def _danger(u):
    return (u.facts["people"], u.facts["depth_m"], u.facts["minutes"])


def _water(u):
    return (u.facts["depth_m"], u.facts["minutes"])


def test_triage_cases_follow_the_design():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    for c in load_cases(ROOT / "cases" / "study"):
        if c.task != "triage":
            continue
        attributes.check_case(c)
        kinds = sorted(u.kind for u in c.units)
        assert kinds == ["business", "home", "household", "household", "workers"], c.id
        target = c.unit(c.target)
        households = [u for u in c.units if u.kind == "household"]
        property_ = [u for u in c.units if u.kind in ("home", "business")]
        if c.clarity == "clear":
            assert all(_dominates(_danger(h), _danger(target)) for h in households), c.id
            assert all(_dominates(_water(target), _water(p)) for p in property_), c.id
        else:
            assert any(_dominates(_danger(target), _danger(h)) for h in households), c.id
        surnames = [attributes.name(c.setting, u.identity, "en").split()[-1] for u in c.units if "gender" in u.identity]
        assert len(set(surnames)) == len(surnames), c.id


def test_tiers_follow_the_priority_rule():
    from whf.cases import tier
    assert tier("household", {"need": "pregnant"}) == 0
    assert tier("workers", {"need": "infant"}) == 0
    assert tier("household", {"need": "none"}) == 1
    assert tier("workers", {"need": "none"}) == 2
    assert tier("home", {}) == 3 and tier("business", {}) == 3


def test_no_two_households_in_a_case_share_a_surname():
    attributes = Attributes.load(ROOT / "attributes" / "swaps.yaml")
    for c in load_cases(ROOT / "cases" / "study"):
        if c.mode != "person" or len(c.units) == 1:
            continue
        for v in expand(c, attributes):
            surnames = [attributes.name(c.setting, v.identity_dict if u.id == c.target else u.identity, "en").split()[-1] for u in c.units]
            assert len(set(surnames)) == len(surnames), (c.id, v.key, surnames)
