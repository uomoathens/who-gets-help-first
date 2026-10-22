# Writing a case

One YAML file per case, named after its `id`. The files in `templates/` show the format.

| Field | Meaning |
| --- | --- |
| `id` | Unique, equal to the file name |
| `status` | `draft`, `template`, `reviewed` or `final`; only `reviewed` and `final` run outside a pilot. Cases are illustrative examples; `reviewed` means the case passes the automatic design checks in `tests/test_study.py`, not that a person or an outside body has approved it |
| `task` | `dispatch`, `evacuation`, `relief`, `housing` or `triage` |
| `setting` | A setting in `attributes/swaps.yaml` (`thessaly`, `valais`, `valencia`) |
| `event` | The documented event the case is modelled on |
| `context` | One to three sentences of situation, in `el`, `fr` and `en` |
| `target` | The unit whose identity is varied |
| `clarity` | `ambiguous` (default) when the needs are close, `clear` when one need plainly dominates |
| `units` | Calls, areas or applicants, each with `place`, `facts` and `identity` |

Facts per task:

| Task | Facts |
| --- | --- |
| dispatch | `people`, `depth_m`, `minutes` |
| evacuation | `residents`, `forecast_m`, `hours` |
| relief | `residents`, `days` |
| housing | `members`, `damage_pct`, `nights` |
| triage | `people`, `depth_m`, `minutes` |

Triage units also carry a `kind`: `household` (people at home), `workers` (people trapped at a business, always the target), `home` or `business` (nobody inside; `people` is 0). Households take the household identity, workers take `origin` and `need`, homes take the owner's `origin`, `gender` and `area`, and businesses take no identity.

Identity uses `origin`, `gender`, `area`, `status` and `need` for households (dispatch, housing), and `origin`, `area` and `need` for areas (evacuation, relief). Households may add `name: 1` or `name: 2` to take another name from the same list, so that no two households share a name. The target always uses the first name.

Three rules keep the comparisons clean:

1. Give the target a mid-ranking need in the base case, so that a shift up or down can both be seen.
2. Keep every other unit at the reference identity, so that only the target changes.
3. Use whole numbers or one decimal; Greek and French prompts print decimals with a comma.

Run `whf preview` to read every variant of a case in every language before marking it `reviewed`.
