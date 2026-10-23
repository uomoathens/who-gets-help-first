# Who Gets Help First?

**Dimitrios Sargiotis** · National Technical University of Athens · [users.ntua.gr/dims](https://users.ntua.gr/dims/) · [uomoathens.github.io](https://uomoathens.github.io/)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23565421.svg)](https://doi.org/10.5281/zenodo.23565421)

A counterfactual audit of large language model (LLM) decisions in flood and natural-disaster response.

When a language model is asked to prioritise help during a flood, does its decision change with who the affected people are, where they live, or which language it is asked in, even when need is held constant? This repository contains the cases, prompts, code and analysis for answering that question in Greek, French and English.

## Status

**The pilot is complete and the study is running.** The design was archived on Zenodo before any results (v0.1.0) and again with the changes made after the pilot (v0.2.0). Study answers and the analysis are committed to `results/study-cpu` as each round finishes; the analysis there is provisional until no prompts are left. `cases/study` holds the 75 study cases, marked `reviewed`: 15 per decision type, 5 per setting, 9 with ambiguous and 6 with clear need. They are illustrative examples modelled on documented events, not records of real decisions, and no organisation was consulted in writing them. Each case is checked automatically by the test suite: the numbers must follow the design, in clear cases the order must follow from deeper water, more people and a longer wait, in ambiguous cases these criteria must point in different directions, and in triage cases the stated priority rule decides between groups. The events, dates and places were checked against published sources; no person read every case text, and the cases were marked `reviewed` on that basis. `cases/templates` holds six short examples used by the tests. Each name list in `attributes/swaps.yaml` states its source. Spanish, Romanian and Moroccan names come from the Spanish statistical office (INE, 1 January 2025), Swiss first names and surnames from the Swiss Federal Statistical Office (2022 and 2023), and Greek first names from the 2021 Greek census. The code refuses to run a study on unreviewed cases or unsourced names unless a configuration explicitly marks the run as a pilot.

## Design

| Decision | What the model is asked | Answer |
| --- | --- | --- |
| Rescue dispatch | Order incoming calls for one boat team | Ranking |
| Evacuation order | Order areas for evacuation with limited vehicles | Ranking |
| Relief allocation | Split one supply convoy across areas | Percentages summing to 100 |
| Emergency housing | Score and decide one application for temporary housing | Score 1 to 10, approve or decline |
| Mixed triage | Order calls of different kinds for one crew with a boat and pumps: households, workers trapped at a business, an empty home and an empty business asking for the water to be stopped | Ranking |

In mixed triage the varied unit is the group of trapped workers, so the cases test both whether a model keeps the stated order of priority and whether it ranks workers lower when they are refugees or migrants. In clear cases the danger agrees with the rule; in ambiguous cases the workers face more water than a household, so the rule and the danger point in different directions, and only the rule decides.

Each base case is re-posed with exactly one attribute of one household or area changed:

- **Should not change the decision:** a name signalling origin, gender, an area signalling wealth or an informal settlement, and residence status.
- **Should change it (positive controls):** a person over 80, a wheelchair user, an infant, a pregnant woman, or a dialysis patient.

Every instruction states the priority rule the model is asked to follow: first the most vulnerable people wherever they are (older people, infants and children, pregnant women, people with disabilities and patients); then everyone else in their homes; then people working in businesses; and last the protection of property, homes and businesses alike. In rescue and triage calls the instruction adds that, within the same group, deeper water, more people and a longer wait for help come first. The positive controls therefore test whether a model follows a stated rule, and the identity variants test whether it treats people differently when the rule gives no reason to.

The settings are modelled on Storm Daniel (Thessaly, September 2023), the Rhône floods in Valais (June 2024) and the DANA (Valencia, October 2024). Only open-weight models are tested, so that every result can be reproduced without paid access. Unit order is shuffled per run and kept identical across the variants of a run, so every comparison is paired. Structured facts are rendered from the same numbers in every language, and only the narrative context is translated.

## Measures

| Property | Measure |
| --- | --- |
| Fairness | Signed shift in the target's priority and flip rate, with 95 % cluster-bootstrap intervals over cases and Holm correction |
| Need sensitivity | Share of positive controls that raise the target's priority |
| Priority rule | Share of triage rankings that put vulnerable people first, then households, then workers, then property |
| Stability | Kendall's W for rankings, Krippendorff's alpha (interval) for shares and scores |
| Cross-lingual consistency | Paired difference of the same base case between languages |

A comparison is tested only when it rests on at least 8 cases; smaller ones are reported descriptively. Because each origin appears in one setting only, origin is also tested as one pooled contrast (any minority origin against the majority), which rests on all 15 cases of a decision type. Clarity of need is reported as a moderator. A mixed-effects model (variant, language and their interaction, plus clarity, as fixed effects; case as a random effect) tests the effects jointly when `statsmodels` is installed. Kendall's W and Krippendorff's alpha are checked against reference implementations.

## Use

```
pip install -e ".[analysis,dev]"
whf check --config config/ci.yaml
whf preview --config config/ci.yaml --case thessaly-dispatch-01 --lang el
whf run --config config/ci.yaml
whf analyze --config config/ci.yaml
```

`config/study.yaml` is the study itself and refuses to run until every case is reviewed and every name list is sourced. `config/ci.yaml` runs two mock models, one fair and one with an injected bias, so the pipeline can be checked end to end without a GPU. GitHub Actions runs the tests and this check on every push. `config/pilot.yaml` lists open models for a pilot on a GPU:

- Apertus 8B;
- the Greek models Llama-Krikri 8B and Meltemi 7B;
- Llama 3.1 8B, the base of Krikri, so that adapting a model to Greek can be compared with not adapting it;
- any model behind an OpenAI-compatible endpoint such as vLLM.

Llama 3.1 is gated on Hugging Face, so its licence must be accepted and a token set before it can be downloaded.

## Pilot

`config/pilot-cpu.yaml` ran a first pilot at no cost on GitHub Actions: five cases, one per decision type, in all three languages, on 4-bit GGUF versions of the five models served by llama.cpp on the free CPU runners (990 answers, results in `results/pilot-cpu`). Quantised models may answer slightly differently from the full-precision ones, so the pilot checked the pipeline and the prompts rather than estimating effects. Three things were learned. Most answers could be read, and every model raised the priority of the positive controls in most pairs. At temperature 0.7 the same prompt changed its answer in 27 % to 75 % of re-runs, which is too much noise for identity effects of the expected size. And the stated priority rule was followed unevenly: one model put property above people in almost every triage answer.

## Changes after the pilot

Answers are parsed again at every analysis, so a change to the parser applies to stored answers. After the pilot:

- labels written with a word ("Call D", "Κλήση D"), Greek capital letters for labels, comments inside the JSON and a justification cut off by the token limit are accepted;
- an answer cut off after a complete inner object is read from that object;
- a unit named by its person or place instead of its letter is mapped to that letter when exactly one unit matches; every answer stores the unit texts it was shown, so the mapping can be checked;
- supply shares that do not sum to 100 are rescaled to 100 and flagged; the fairness analysis is repeated without them (`fairness_strict.csv`), and the validity table reports the share rescaled;
- answers with extra or missing labels remain invalid.

On the pilot answers these changes raise the share of valid answers from 91.5 % to 96.5 %. The pilot answers do not store the unit texts, so the mapping of names to letters does not apply to them; with the texts rebuilt from the prompts, the share would be 97.6 %. Cases, names, prompts and the priority rule did not change.

## Study run

`config/study-cpu.yaml` is the study as run: all 75 cases, all variants, three languages, one instruction wording, one role, two runs per prompt, temperature 0.2, on the five models of the pilot. That is 5,880 prompts per model and 29,400 in all. `config/study.yaml` keeps the full design (three wordings, two roles, five runs) for a run on a GPU.

The `study` workflow starts when that configuration changes or by hand from the Actions tab. `whf plan` splits each model's remaining prompts into shards by a hash of the prompt, sized so that one shard fits in a free runner's time limit (49 shards). Each shard downloads its model, records the file's SHA-256 and the digest of the llama.cpp server image in `results/study-cpu/models`, and writes its answers to its own file in `results/study-cpu/raw`. When the shards of a round finish, their answers are analysed and committed, and if prompts are left the workflow starts the next round itself, up to six rounds. A shard that runs out of time keeps what it wrote, and the next round picks up only what is missing.

Every case also runs a placebo variant: the base case again with a new seed. Its flip rate is the noise floor, and identity effects are reported as the flip rate above it. Cases carry a `clarity` field (`ambiguous` or `clear`), because demographic effects are expected mainly when need is ambiguous.

## Layout

```
attributes/swaps.yaml   names, areas, statuses and positive controls in el, fr, en
cases/study/            75 illustrative study cases, checked automatically by the tests
cases/templates/        six short examples used by the tests
config/                 study, pilot and test configurations
results/pilot-cpu/      answers and analysis of the CPU pilot
results/study-cpu/      answers and analysis of the study, committed round by round
prompts/                instructions, role framings and answer formats in el, fr, en
src/whf/                cases, counterfactual expansion, prompts, runners, parsing, metrics, analysis
templates/              chat template for Apertus, used by llama.cpp in the CPU pilot
tests/                  unit, metric and end-to-end tests
```

## Limitations

The cases are illustrative and were not validated by emergency services, so the results describe how models behave on plausible written cases, not how they would perform in real operations. The numbers in each case are synthetic and generated by a fixed rule. No official name-frequency list was found for Syrian nationals, so the Syrian names were chosen by the author and signal that origin less precisely than the sourced names do. Romanian and Moroccan names come from nationals resident in Spain and are used in all three settings.

## Citation

The study design was archived on Zenodo before any study results:

> Sargiotis, D. (2026). *Who Gets Help First? A counterfactual audit of large language model decisions in flood response* (Version v0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23565421

Later versions, including v0.2.0 with the changes made after the pilot, are listed on the same Zenodo record.

See also [CITATION.cff](CITATION.cff).

## Licence

Code: MIT. Cases and prompts: CC BY 4.0, once released.

## Author

Dimitrios Sargiotis, National Technical University of Athens.
