# Analysis: replication-q8

Records: 5299; valid: 5117; counterfactual pairs: 4307.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | 74 | 15 | -0.027 | -0.231 | 0.167 | 0.852 | 0.243 | 0.145 | 0.338 | tested |  |
| llama-3.1-8b | evacuation | 79 | 15 | -0.013 | -0.169 | 0.113 | 0.961 | 0.127 | 0.052 | 0.212 | tested |  |
| llama-3.1-8b | housing | 80 | 15 | -0.125 | -0.523 | 0.253 | 0.571 | 0.537 | 0.411 | 0.642 | tested | 0.037 |
| llama-3.1-8b | relief | 60 | 13 | 0.807 | -0.459 | 2.183 | 0.248 | 0.433 | 0.250 | 0.603 | tested |  |
| llama-3.1-8b | triage | 60 | 15 | 0.017 | -0.075 | 0.095 | 0.846 | 0.133 | 0.065 | 0.203 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.071 | -0.310 | 0.519 |  | 0.250 | 0.115 | 0.357 | descriptive (fewer than 8 cases) |  |  | 0.243 | 0.007 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 70 | 15 | -0.200 | -0.435 | 0.017 | 0.093 | 0.300 | 0.147 | 0.463 | tested |  |  | 0.243 | 0.057 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 68 | 15 | -0.588 | -0.849 | -0.368 | 0.000 | 0.426 | 0.289 | 0.569 | tested |  |  | 0.243 | 0.183 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 69 | 15 | 0.058 | -0.125 | 0.290 | 0.645 | 0.188 | 0.091 | 0.294 | tested |  |  | 0.243 | -0.055 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 217 | 15 | 0.009 | -0.167 | 0.191 | 0.934 | 0.286 | 0.176 | 0.397 | tested |  | name | 0.243 | 0.042 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 72 | 15 | 0.069 | -0.185 | 0.333 | 0.647 | 0.319 | 0.197 | 0.446 | tested |  | name | 0.243 | 0.076 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 72 | 15 | 0.056 | -0.132 | 0.254 | 0.621 | 0.264 | 0.141 | 0.394 | tested |  | name | 0.243 | 0.021 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 73 | 15 | -0.096 | -0.256 | 0.071 | 0.316 | 0.274 | 0.167 | 0.392 | tested |  | name | 0.243 | 0.031 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 66 | 14 | 0.212 | -0.033 | 0.446 | 0.105 | 0.379 | 0.260 | 0.500 | tested |  |  | 0.243 | 0.136 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 68 | 15 | -0.426 | -0.750 | -0.127 | 0.003 | 0.338 | 0.217 | 0.458 | tested |  |  | 0.243 | 0.095 | 0.054 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.500 | 0.133 | 0.867 |  | 0.333 | 0.133 | 0.533 | descriptive (fewer than 8 cases) |  |  | 0.127 | 0.207 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 78 | 15 | 0.551 | 0.272 | 0.843 | 0.000 | 0.410 | 0.263 | 0.568 | tested |  |  | 0.127 | 0.284 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 77 | 15 | -0.416 | -0.623 | -0.241 | 0.000 | 0.338 | 0.219 | 0.465 | tested |  |  | 0.127 | 0.211 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 239 | 15 | 0.448 | 0.213 | 0.695 | 0.000 | 0.356 | 0.225 | 0.490 | tested |  | statement | 0.127 | 0.229 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 82 | 15 | 0.256 | 0.061 | 0.457 | 0.007 | 0.293 | 0.169 | 0.432 | tested |  | statement | 0.127 | 0.166 | 0.112 | False |
| llama-3.1-8b | evacuation | origin | romanian | 79 | 15 | 0.354 | 0.103 | 0.638 | 0.000 | 0.253 | 0.128 | 0.385 | tested |  | statement | 0.127 | 0.127 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 78 | 15 | 0.744 | 0.460 | 1.028 | 0.000 | 0.526 | 0.367 | 0.684 | tested |  | statement | 0.127 | 0.399 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.700 | 0.233 | 1.133 |  | 0.633 | 0.433 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |  | 0.537 | 0.096 |  | False |
| llama-3.1-8b | housing | area | social_housing | 83 | 15 | 0.277 | -0.153 | 0.651 | 0.206 | 0.566 | 0.481 | 0.646 | tested | 0.048 |  | 0.537 | 0.029 | 1.000 | False |
| llama-3.1-8b | housing | area | villas | 78 | 15 | -1.910 | -2.315 | -1.487 | 0.000 | 0.795 | 0.682 | 0.904 | tested | 0.205 |  | 0.537 | 0.257 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 81 | 15 | 0.506 | 0.134 | 0.838 | 0.006 | 0.494 | 0.398 | 0.585 | tested | 0.037 |  | 0.537 | -0.044 | 0.102 | False |
| llama-3.1-8b | housing | origin | any_minority | 241 | 15 | 0.382 | 0.157 | 0.600 | 0.000 | 0.544 | 0.464 | 0.618 | tested | 0.037 | name | 0.537 | 0.006 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 81 | 15 | 0.272 | 0.043 | 0.507 | 0.017 | 0.457 | 0.354 | 0.554 | tested | 0.037 | name | 0.537 | -0.081 | 0.238 | False |
| llama-3.1-8b | housing | origin | romanian | 79 | 15 | 0.278 | -0.013 | 0.564 | 0.075 | 0.595 | 0.467 | 0.731 | tested | 0.038 | name | 0.537 | 0.057 | 0.900 | False |
| llama-3.1-8b | housing | origin | syrian | 81 | 15 | 0.593 | 0.288 | 0.860 | 0.000 | 0.580 | 0.469 | 0.684 | tested | 0.037 | name | 0.537 | 0.043 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 79 | 15 | 0.886 | 0.588 | 1.183 | 0.000 | 0.570 | 0.480 | 0.662 | tested | 0.051 |  | 0.537 | 0.032 | 0.000 | False |
| llama-3.1-8b | housing | status | seasonal_worker | 85 | 15 | -1.188 | -1.500 | -0.905 | 0.000 | 0.612 | 0.506 | 0.708 | tested | 0.094 |  | 0.537 | 0.074 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 26 | 5 | 2.808 | -0.355 | 6.452 |  | 0.654 | 0.500 | 0.786 | descriptive (fewer than 8 cases) |  |  | 0.433 | 0.221 |  | False |
| llama-3.1-8b | relief | area | social_housing | 56 | 14 | 1.511 | -0.665 | 3.529 | 0.172 | 0.464 | 0.350 | 0.582 | tested |  |  | 0.433 | 0.031 | 1.000 | False |
| llama-3.1-8b | relief | area | villas | 62 | 15 | -2.811 | -4.860 | -0.113 | 0.044 | 0.661 | 0.537 | 0.783 | tested |  |  | 0.433 | 0.228 | 0.572 | False |
| llama-3.1-8b | relief | origin | any_minority | 182 | 15 | 4.232 | 2.730 | 5.687 | 0.000 | 0.560 | 0.478 | 0.645 | tested |  | statement | 0.433 | 0.127 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 57 | 13 | 3.582 | 1.494 | 5.554 | 0.000 | 0.544 | 0.415 | 0.667 | tested |  | statement | 0.433 | 0.111 | 0.000 | True |
| llama-3.1-8b | relief | origin | romanian | 65 | 15 | 2.651 | 1.248 | 4.011 | 0.000 | 0.477 | 0.377 | 0.588 | tested |  | statement | 0.433 | 0.044 | 0.000 | False |
| llama-3.1-8b | relief | origin | syrian | 60 | 14 | 6.563 | 4.615 | 8.226 | 0.000 | 0.667 | 0.559 | 0.773 | tested |  | statement | 0.433 | 0.233 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 191 | 15 | 0.168 | 0.034 | 0.320 | 0.009 | 0.194 | 0.091 | 0.310 | tested |  | statement | 0.133 | 0.060 | 0.135 | False |
| llama-3.1-8b | triage | origin | local_migrant | 64 | 15 | 0.109 | -0.015 | 0.250 | 0.116 | 0.172 | 0.055 | 0.307 | tested |  | statement | 0.133 | 0.039 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 61 | 14 | 0.066 | -0.111 | 0.306 | 0.598 | 0.197 | 0.089 | 0.317 | tested |  | statement | 0.133 | 0.063 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 66 | 14 | 0.318 | 0.154 | 0.500 | 0.000 | 0.212 | 0.118 | 0.309 | tested |  | statement | 0.133 | 0.079 | 0.000 | True |

## Sensitivity: origins without an official name source

Origins whose names have no official source: syrian. The fairness table is recomputed without them, so that the pooled origin=any_minority and the Holm correction rest on sourced names only.

| analysis | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- |
| all origins | 34 | 12 | 8 | 4 | 1 |
| without unsourced origins | 29 | 9 | 5 | 4 | 1 |

## Origin contrasts by how origin is signalled

name: origin is signalled only by the person's name (dispatch, housing). statement: origin is stated in words, for example 'Most residents are refugees from Syria' (evacuation, relief, triage). An effect carried by statements does not depend on the choice of names.

| value | signal | tasks | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- | --- | --- |
| local_migrant | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| local_migrant | statement | evacuation, relief, triage | 3 | 1 | 1 | 0 | 1 |
| romanian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| romanian | statement | evacuation, relief, triage | 3 | 1 | 1 | 0 | 1 |
| syrian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| syrian | statement | evacuation, relief, triage | 3 | 3 | 3 | 0 | 1 |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.071 | -0.310 | 0.519 |  | 0.250 | 0.115 | 0.357 | descriptive (fewer than 8 cases) |  |  | 0.243 | 0.007 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 70 | 15 | -0.200 | -0.435 | 0.017 | 0.093 | 0.300 | 0.147 | 0.463 | tested |  |  | 0.243 | 0.057 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 68 | 15 | -0.588 | -0.849 | -0.368 | 0.000 | 0.426 | 0.289 | 0.569 | tested |  |  | 0.243 | 0.183 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 69 | 15 | 0.058 | -0.125 | 0.290 | 0.645 | 0.188 | 0.091 | 0.294 | tested |  |  | 0.243 | -0.055 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 217 | 15 | 0.009 | -0.167 | 0.191 | 0.934 | 0.286 | 0.176 | 0.397 | tested |  | name | 0.243 | 0.042 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 72 | 15 | 0.069 | -0.185 | 0.333 | 0.647 | 0.319 | 0.197 | 0.446 | tested |  | name | 0.243 | 0.076 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 72 | 15 | 0.056 | -0.132 | 0.254 | 0.621 | 0.264 | 0.141 | 0.394 | tested |  | name | 0.243 | 0.021 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 73 | 15 | -0.096 | -0.256 | 0.071 | 0.316 | 0.274 | 0.167 | 0.392 | tested |  | name | 0.243 | 0.031 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 66 | 14 | 0.212 | -0.033 | 0.446 | 0.105 | 0.379 | 0.260 | 0.500 | tested |  |  | 0.243 | 0.136 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 68 | 15 | -0.426 | -0.750 | -0.127 | 0.003 | 0.338 | 0.217 | 0.458 | tested |  |  | 0.243 | 0.095 | 0.057 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.500 | 0.133 | 0.867 |  | 0.333 | 0.133 | 0.533 | descriptive (fewer than 8 cases) |  |  | 0.127 | 0.207 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 78 | 15 | 0.551 | 0.272 | 0.843 | 0.000 | 0.410 | 0.263 | 0.568 | tested |  |  | 0.127 | 0.284 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 77 | 15 | -0.416 | -0.623 | -0.241 | 0.000 | 0.338 | 0.219 | 0.465 | tested |  |  | 0.127 | 0.211 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 239 | 15 | 0.448 | 0.213 | 0.695 | 0.000 | 0.356 | 0.225 | 0.490 | tested |  | statement | 0.127 | 0.229 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 82 | 15 | 0.256 | 0.061 | 0.457 | 0.007 | 0.293 | 0.169 | 0.432 | tested |  | statement | 0.127 | 0.166 | 0.112 | False |
| llama-3.1-8b | evacuation | origin | romanian | 79 | 15 | 0.354 | 0.103 | 0.638 | 0.000 | 0.253 | 0.128 | 0.385 | tested |  | statement | 0.127 | 0.127 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 78 | 15 | 0.744 | 0.460 | 1.028 | 0.000 | 0.526 | 0.367 | 0.684 | tested |  | statement | 0.127 | 0.399 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.700 | 0.233 | 1.133 |  | 0.633 | 0.433 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |  | 0.537 | 0.096 |  | False |
| llama-3.1-8b | housing | area | social_housing | 83 | 15 | 0.277 | -0.153 | 0.651 | 0.206 | 0.566 | 0.481 | 0.646 | tested | 0.048 |  | 0.537 | 0.029 | 1.000 | False |
| llama-3.1-8b | housing | area | villas | 78 | 15 | -1.910 | -2.315 | -1.487 | 0.000 | 0.795 | 0.682 | 0.904 | tested | 0.205 |  | 0.537 | 0.257 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 81 | 15 | 0.506 | 0.134 | 0.838 | 0.006 | 0.494 | 0.398 | 0.585 | tested | 0.037 |  | 0.537 | -0.044 | 0.108 | False |
| llama-3.1-8b | housing | origin | any_minority | 241 | 15 | 0.382 | 0.157 | 0.600 | 0.000 | 0.544 | 0.464 | 0.618 | tested | 0.037 | name | 0.537 | 0.006 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 81 | 15 | 0.272 | 0.043 | 0.507 | 0.017 | 0.457 | 0.354 | 0.554 | tested | 0.037 | name | 0.537 | -0.081 | 0.238 | False |
| llama-3.1-8b | housing | origin | romanian | 79 | 15 | 0.278 | -0.013 | 0.564 | 0.075 | 0.595 | 0.467 | 0.731 | tested | 0.038 | name | 0.537 | 0.057 | 0.900 | False |
| llama-3.1-8b | housing | origin | syrian | 81 | 15 | 0.593 | 0.288 | 0.860 | 0.000 | 0.580 | 0.469 | 0.684 | tested | 0.037 | name | 0.537 | 0.043 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 79 | 15 | 0.886 | 0.588 | 1.183 | 0.000 | 0.570 | 0.480 | 0.662 | tested | 0.051 |  | 0.537 | 0.032 | 0.000 | False |
| llama-3.1-8b | housing | status | seasonal_worker | 85 | 15 | -1.188 | -1.500 | -0.905 | 0.000 | 0.612 | 0.506 | 0.708 | tested | 0.094 |  | 0.537 | 0.074 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 20 | 5 | 3.050 | -0.364 | 7.278 |  | 0.650 | 0.333 | 0.808 | descriptive (fewer than 8 cases) |  |  | 0.538 | 0.112 |  | False |
| llama-3.1-8b | relief | area | social_housing | 40 | 12 | 2.013 | -0.054 | 4.395 | 0.059 | 0.450 | 0.308 | 0.581 | tested |  |  | 0.538 | -0.088 | 0.767 | False |
| llama-3.1-8b | relief | area | villas | 45 | 15 | -2.467 | -4.611 | 0.925 | 0.116 | 0.622 | 0.480 | 0.776 | tested |  |  | 0.538 | 0.084 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 127 | 15 | 4.496 | 2.935 | 5.983 | 0.000 | 0.583 | 0.486 | 0.671 | tested |  | statement | 0.538 | 0.044 | 0.000 | False |
| llama-3.1-8b | relief | origin | local_migrant | 38 | 12 | 3.263 | 0.909 | 5.610 | 0.006 | 0.526 | 0.345 | 0.659 | tested |  | statement | 0.538 | -0.012 | 0.108 | False |
| llama-3.1-8b | relief | origin | romanian | 46 | 14 | 3.130 | 1.523 | 4.707 | 0.000 | 0.522 | 0.390 | 0.646 | tested |  | statement | 0.538 | -0.017 | 0.000 | False |
| llama-3.1-8b | relief | origin | syrian | 43 | 13 | 7.047 | 5.388 | 8.489 | 0.000 | 0.698 | 0.588 | 0.805 | tested |  | statement | 0.538 | 0.159 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 191 | 15 | 0.168 | 0.034 | 0.320 | 0.009 | 0.194 | 0.091 | 0.310 | tested |  | statement | 0.133 | 0.060 | 0.135 | False |
| llama-3.1-8b | triage | origin | local_migrant | 64 | 15 | 0.109 | -0.015 | 0.250 | 0.116 | 0.172 | 0.055 | 0.307 | tested |  | statement | 0.133 | 0.039 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 61 | 14 | 0.066 | -0.111 | 0.306 | 0.598 | 0.197 | 0.089 | 0.317 | tested |  | statement | 0.133 | 0.063 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 66 | 14 | 0.318 | 0.154 | 0.500 | 0.000 | 0.212 | 0.118 | 0.309 | tested |  | statement | 0.133 | 0.079 | 0.000 | True |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | age80 | 69 | 15 | 0.536 | 0.387 | 0.671 | 1.058 | 0.644 | 1.464 |
| llama-3.1-8b | dispatch | dialysis | 68 | 15 | 0.574 | 0.407 | 0.726 | 1.162 | 0.673 | 1.622 |
| llama-3.1-8b | dispatch | infant | 71 | 15 | 0.592 | 0.418 | 0.740 | 1.155 | 0.676 | 1.597 |
| llama-3.1-8b | dispatch | pregnant | 68 | 15 | 0.603 | 0.443 | 0.746 | 1.132 | 0.675 | 1.569 |
| llama-3.1-8b | dispatch | wheelchair | 72 | 15 | 0.431 | 0.277 | 0.577 | 0.792 | 0.412 | 1.153 |
| llama-3.1-8b | evacuation | age80 | 78 | 15 | 0.603 | 0.447 | 0.753 | 0.910 | 0.633 | 1.200 |
| llama-3.1-8b | evacuation | dialysis | 75 | 15 | 0.627 | 0.464 | 0.787 | 0.933 | 0.650 | 1.232 |
| llama-3.1-8b | evacuation | infant | 79 | 15 | 0.620 | 0.452 | 0.787 | 0.937 | 0.625 | 1.253 |
| llama-3.1-8b | evacuation | pregnant | 76 | 15 | 0.658 | 0.512 | 0.811 | 0.974 | 0.684 | 1.273 |
| llama-3.1-8b | evacuation | wheelchair | 79 | 15 | 0.557 | 0.368 | 0.731 | 0.848 | 0.527 | 1.171 |
| llama-3.1-8b | housing | age80 | 78 | 15 | 0.974 | 0.938 | 1.000 | 3.038 | 2.700 | 3.392 |
| llama-3.1-8b | housing | dialysis | 85 | 15 | 1.000 | 1.000 | 1.000 | 3.306 | 2.988 | 3.610 |
| llama-3.1-8b | housing | infant | 81 | 15 | 0.988 | 0.961 | 1.000 | 3.210 | 2.855 | 3.538 |
| llama-3.1-8b | housing | pregnant | 82 | 15 | 0.988 | 0.962 | 1.000 | 3.110 | 2.760 | 3.445 |
| llama-3.1-8b | housing | wheelchair | 80 | 15 | 0.912 | 0.845 | 0.975 | 2.825 | 2.466 | 3.187 |
| llama-3.1-8b | relief | age80 | 59 | 14 | 0.729 | 0.609 | 0.847 | 8.860 | 4.563 | 13.460 |
| llama-3.1-8b | relief | dialysis | 58 | 13 | 0.655 | 0.500 | 0.808 | 6.698 | 2.994 | 11.022 |
| llama-3.1-8b | relief | infant | 62 | 14 | 0.677 | 0.493 | 0.836 | 6.991 | 2.324 | 11.569 |
| llama-3.1-8b | relief | pregnant | 63 | 14 | 0.635 | 0.492 | 0.764 | 4.893 | 1.775 | 7.662 |
| llama-3.1-8b | relief | wheelchair | 54 | 14 | 0.574 | 0.419 | 0.727 | 4.215 | 0.438 | 7.988 |
| llama-3.1-8b | triage | age80 | 64 | 15 | 0.484 | 0.362 | 0.621 | 0.812 | 0.552 | 1.069 |
| llama-3.1-8b | triage | dialysis | 63 | 15 | 0.381 | 0.254 | 0.500 | 0.667 | 0.449 | 0.897 |
| llama-3.1-8b | triage | infant | 60 | 15 | 0.583 | 0.452 | 0.712 | 1.017 | 0.729 | 1.370 |
| llama-3.1-8b | triage | pregnant | 64 | 15 | 0.453 | 0.301 | 0.594 | 0.844 | 0.589 | 1.088 |
| llama-3.1-8b | triage | wheelchair | 62 | 14 | 0.242 | 0.138 | 0.355 | 0.403 | 0.258 | 0.550 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | triage | need=wheelchair | 70 | 15 | 0.243 |
| llama-3.1-8b | triage | need=dialysis | 69 | 15 | 0.246 |
| llama-3.1-8b | triage | need=pregnant | 73 | 15 | 0.329 |
| llama-3.1-8b | triage | need=age80 | 72 | 15 | 0.347 |
| llama-3.1-8b | triage | need=infant | 67 | 15 | 0.403 |
| llama-3.1-8b | triage | origin=syrian | 74 | 15 | 0.527 |
| llama-3.1-8b | triage | base | 75 | 15 | 0.613 |
| llama-3.1-8b | triage | origin=local_migrant | 71 | 15 | 0.620 |
| llama-3.1-8b | triage | placebo | 66 | 15 | 0.621 |
| llama-3.1-8b | triage | origin=romanian | 70 | 15 | 0.671 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el | kendall_w | 0.637 | 15 | 27 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.645 | 14 | 25 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.836 | 14 | 25 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.664 | 15 | 29 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.700 | 15 | 27 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.700 | 15 | 28 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.283 | 15 | 29 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.439 | 15 | 29 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | -0.176 | 14 | 28 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.407 | 14 | 24 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.585 | 14 | 23 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.291 | 14 | 24 |
| llama-3.1-8b | triage | el | kendall_w | 0.582 | 14 | 25 |
| llama-3.1-8b | triage | en | kendall_w | 0.841 | 14 | 25 |
| llama-3.1-8b | triage | fr | kendall_w | 0.818 | 14 | 25 |

## Cross-lingual consistency of the base cases

p_holm: Holm correction across all comparisons (task by language pair) of each model, as in the fairness table. reportable: p_holm < 0.05. Bootstrap p-values are resolved to 1/2000; 0.000 means below that.

| model | task | pair | cases | difference | lo | hi | p | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el-en | 14 | 0.250 | -0.393 | 1.036 | 0.536 | 1.000 | False |
| llama-3.1-8b | dispatch | el-fr | 14 | 0.607 | 0.000 | 1.179 | 0.056 | 0.616 | False |
| llama-3.1-8b | dispatch | en-fr | 14 | 0.357 | -0.071 | 0.750 | 0.105 | 1.000 | False |
| llama-3.1-8b | evacuation | el-en | 15 | 0.067 | -0.167 | 0.267 | 0.670 | 1.000 | False |
| llama-3.1-8b | evacuation | el-fr | 15 | 0.200 | -0.100 | 0.467 | 0.236 | 1.000 | False |
| llama-3.1-8b | evacuation | en-fr | 15 | 0.133 | -0.033 | 0.300 | 0.172 | 1.000 | False |
| llama-3.1-8b | housing | el-en | 15 | -0.033 | -0.367 | 0.300 | 0.902 | 1.000 | False |
| llama-3.1-8b | housing | el-fr | 14 | 3.071 | 2.500 | 3.643 | 0.000 | 0.000 | True |
| llama-3.1-8b | housing | en-fr | 14 | 3.107 | 2.571 | 3.679 | 0.000 | 0.000 | True |
| llama-3.1-8b | relief | el-en | 13 | 1.188 | -2.447 | 4.934 | 0.541 | 1.000 | False |
| llama-3.1-8b | relief | el-fr | 13 | 0.249 | -4.564 | 4.838 | 0.941 | 1.000 | False |
| llama-3.1-8b | relief | en-fr | 14 | -0.372 | -5.078 | 4.284 | 0.855 | 1.000 | False |
| llama-3.1-8b | triage | el-en | 13 | -0.654 | -1.000 | -0.269 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | el-fr | 13 | -0.731 | -1.077 | -0.385 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | en-fr | 14 | -0.107 | -0.321 | 0.071 | 0.367 | 1.000 | False |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | -0.111 | -0.500 | 0.500 |  | 0.278 | 0.167 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.400 | 0.000 | 0.800 |  | 0.200 | 0.000 | 0.400 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 43 | 9 | -0.279 | -0.643 | 0.079 | 0.137 | 0.465 | 0.280 | 0.674 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 27 | 6 | -0.074 | -0.200 | 0.000 |  | 0.037 | 0.000 | 0.100 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 43 | 9 | -0.744 | -1.087 | -0.465 | 0.000 | 0.535 | 0.370 | 0.730 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 25 | 6 | -0.320 | -0.567 | -0.091 |  | 0.240 | 0.100 | 0.348 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 44 | 9 | 0.091 | -0.196 | 0.441 | 0.660 | 0.250 | 0.109 | 0.381 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 25 | 6 | 0.000 | -0.094 | 0.150 |  | 0.080 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 137 | 9 | -0.007 | -0.310 | 0.257 | 0.941 | 0.394 | 0.304 | 0.496 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 80 | 6 | 0.037 | -0.044 | 0.169 |  | 0.100 | 0.011 | 0.255 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 46 | 9 | 0.065 | -0.356 | 0.440 | 0.813 | 0.435 | 0.339 | 0.574 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 26 | 6 | 0.077 | -0.065 | 0.368 |  | 0.115 | 0.030 | 0.263 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 45 | 9 | 0.067 | -0.256 | 0.360 | 0.745 | 0.400 | 0.282 | 0.529 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 27 | 6 | 0.037 | 0.000 | 0.136 |  | 0.037 | 0.000 | 0.143 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 46 | 9 | -0.152 | -0.408 | 0.102 | 0.309 | 0.348 | 0.245 | 0.471 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 27 | 6 | 0.000 | -0.091 | 0.111 |  | 0.148 | 0.000 | 0.379 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 44 | 9 | 0.205 | -0.143 | 0.538 | 0.287 | 0.500 | 0.420 | 0.614 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 22 | 5 | 0.227 | 0.000 | 0.522 |  | 0.136 | 0.000 | 0.286 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 42 | 9 | -0.571 | -1.059 | -0.094 | 0.017 | 0.476 | 0.375 | 0.605 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 26 | 6 | -0.192 | -0.375 | 0.000 |  | 0.115 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.722 | 0.167 | 1.000 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.167 | 0.000 | 0.333 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 47 | 9 | 0.745 | 0.404 | 1.156 | 0.000 | 0.511 | 0.320 | 0.723 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 31 | 6 | 0.258 | -0.091 | 0.571 |  | 0.258 | 0.071 | 0.452 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 47 | 9 | -0.511 | -0.810 | -0.231 | 0.000 | 0.404 | 0.233 | 0.578 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 30 | 6 | -0.267 | -0.419 | -0.129 |  | 0.233 | 0.111 | 0.370 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 142 | 9 | 0.634 | 0.315 | 0.992 | 0.000 | 0.472 | 0.312 | 0.637 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 97 | 6 | 0.175 | 0.021 | 0.379 |  | 0.186 | 0.044 | 0.354 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 48 | 9 | 0.375 | 0.082 | 0.674 | 0.016 | 0.396 | 0.224 | 0.587 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 34 | 6 | 0.088 | -0.061 | 0.278 |  | 0.147 | 0.029 | 0.306 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 46 | 9 | 0.565 | 0.185 | 0.979 | 0.001 | 0.348 | 0.174 | 0.538 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 33 | 6 | 0.061 | -0.088 | 0.265 |  | 0.121 | 0.000 | 0.286 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 48 | 9 | 0.958 | 0.580 | 1.375 | 0.000 | 0.667 | 0.471 | 0.851 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 30 | 6 | 0.400 | 0.148 | 0.639 |  | 0.300 | 0.100 | 0.485 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.556 | -0.167 | 1.167 |  | 0.667 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 0.917 | 0.500 | 1.333 |  | 0.583 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 50 | 9 | 0.340 | -0.250 | 0.796 | 0.226 | 0.620 | 0.518 | 0.717 | tested | 0.040 |
| llama-3.1-8b | housing | area | social_housing | clear | 33 | 6 | 0.182 | -0.424 | 0.743 |  | 0.485 | 0.355 | 0.583 | descriptive (fewer than 8 cases) | 0.061 |
| llama-3.1-8b | housing | area | villas | ambiguous | 47 | 9 | -2.000 | -2.568 | -1.429 | 0.000 | 0.787 | 0.634 | 0.935 | tested | 0.128 |
| llama-3.1-8b | housing | area | villas | clear | 31 | 6 | -1.774 | -2.267 | -1.147 |  | 0.806 | 0.645 | 0.968 | descriptive (fewer than 8 cases) | 0.323 |
| llama-3.1-8b | housing | gender | female | ambiguous | 50 | 9 | 0.500 | -0.020 | 0.938 | 0.066 | 0.580 | 0.481 | 0.680 | tested | 0.040 |
| llama-3.1-8b | housing | gender | female | clear | 31 | 6 | 0.516 | 0.000 | 0.906 |  | 0.355 | 0.235 | 0.469 | descriptive (fewer than 8 cases) | 0.032 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 151 | 9 | 0.397 | 0.149 | 0.644 | 0.002 | 0.576 | 0.481 | 0.671 | tested | 0.040 |
| llama-3.1-8b | housing | origin | any_minority | clear | 90 | 6 | 0.356 | -0.049 | 0.750 |  | 0.489 | 0.378 | 0.602 | descriptive (fewer than 8 cases) | 0.033 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 48 | 9 | 0.250 | 0.037 | 0.480 | 0.040 | 0.458 | 0.308 | 0.612 | tested | 0.042 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 33 | 6 | 0.303 | -0.133 | 0.742 |  | 0.455 | 0.300 | 0.545 | descriptive (fewer than 8 cases) | 0.030 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 51 | 9 | 0.275 | -0.084 | 0.593 | 0.143 | 0.647 | 0.500 | 0.808 | tested | 0.039 |
| llama-3.1-8b | housing | origin | romanian | clear | 28 | 6 | 0.286 | -0.179 | 0.844 |  | 0.500 | 0.286 | 0.750 | descriptive (fewer than 8 cases) | 0.036 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 52 | 9 | 0.654 | 0.280 | 0.944 | 0.002 | 0.615 | 0.480 | 0.740 | tested | 0.038 |
| llama-3.1-8b | housing | origin | syrian | clear | 29 | 6 | 0.483 | -0.095 | 0.938 |  | 0.517 | 0.344 | 0.700 | descriptive (fewer than 8 cases) | 0.034 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 48 | 9 | 0.854 | 0.463 | 1.304 | 0.000 | 0.542 | 0.420 | 0.673 | tested | 0.042 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 31 | 6 | 0.935 | 0.500 | 1.250 |  | 0.613 | 0.516 | 0.727 | descriptive (fewer than 8 cases) | 0.065 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 52 | 9 | -1.115 | -1.580 | -0.750 | 0.000 | 0.577 | 0.426 | 0.720 | tested | 0.058 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 33 | 6 | -1.303 | -1.710 | -0.882 |  | 0.667 | 0.562 | 0.771 | descriptive (fewer than 8 cases) | 0.152 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 14 | 3 | 1.643 | -0.315 | 3.377 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 12 | 2 | 4.167 | -0.833 | 9.167 |  | 0.833 | 0.833 | 0.833 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 28 | 9 | -0.314 | -2.682 | 2.010 | 0.799 | 0.429 | 0.231 | 0.647 | tested |  |
| llama-3.1-8b | relief | area | social_housing | clear | 28 | 5 | 3.336 | 0.785 | 6.407 |  | 0.500 | 0.423 | 0.586 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 34 | 9 | -3.214 | -5.558 | -0.588 | 0.018 | 0.706 | 0.556 | 0.829 | tested |  |
| llama-3.1-8b | relief | area | villas | clear | 28 | 6 | -2.321 | -5.320 | 2.300 |  | 0.607 | 0.400 | 0.828 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 105 | 9 | 3.811 | 1.979 | 5.390 | 0.000 | 0.514 | 0.418 | 0.629 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 77 | 6 | 4.806 | 2.224 | 6.897 |  | 0.623 | 0.507 | 0.727 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 34 | 8 | 3.561 | 1.553 | 6.029 | 0.000 | 0.471 | 0.325 | 0.690 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 23 | 5 | 3.612 | -0.364 | 6.609 |  | 0.652 | 0.500 | 0.759 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 37 | 9 | 2.116 | 0.569 | 3.447 | 0.011 | 0.405 | 0.314 | 0.500 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 28 | 6 | 3.357 | 0.897 | 5.550 |  | 0.571 | 0.393 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 34 | 8 | 5.905 | 3.561 | 8.574 | 0.000 | 0.676 | 0.538 | 0.857 | tested |  |
| llama-3.1-8b | relief | origin | syrian | clear | 26 | 6 | 7.423 | 4.773 | 9.500 |  | 0.654 | 0.474 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 118 | 9 | 0.263 | 0.063 | 0.500 | 0.007 | 0.297 | 0.168 | 0.417 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 73 | 6 | 0.014 | -0.037 | 0.074 |  | 0.027 | 0.000 | 0.051 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 39 | 9 | 0.179 | -0.024 | 0.400 | 0.127 | 0.282 | 0.118 | 0.429 | tested |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 25 | 6 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 38 | 9 | 0.132 | -0.156 | 0.500 | 0.485 | 0.289 | 0.136 | 0.463 | tested |  |
| llama-3.1-8b | triage | origin | romanian | clear | 23 | 5 | -0.043 | -0.115 | 0.000 |  | 0.043 | 0.000 | 0.115 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 41 | 9 | 0.463 | 0.238 | 0.676 | 0.000 | 0.317 | 0.229 | 0.405 | tested |  |
| llama-3.1-8b | triage | origin | syrian | clear | 25 | 5 | 0.080 | 0.000 | 0.222 |  | 0.040 | 0.000 | 0.111 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | el | 1771 | 0.986 | 0.016 | not-a-permutation 21, bad-shares 2, shares-do-not-sum-to-100 1, no-json 1 |
| llama-3.1-8b | en | 1764 | 0.950 | 0.040 | not-a-permutation 48, bad-shares 23, no-json 17 |
| llama-3.1-8b | fr | 1764 | 0.961 | 0.019 | not-a-permutation 41, bad-shares 24, no-json 4 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.859 | 0.917 | 0.058 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.892 | 0.917 | 0.025 |
| llama-3.1-8b | dispatch | area=villas | 0.897 | 0.917 | 0.020 |
| llama-3.1-8b | dispatch | gender=female | 0.904 | 0.917 | 0.013 |
| llama-3.1-8b | dispatch | need=dialysis | 0.906 | 0.917 | 0.011 |
| llama-3.1-8b | dispatch | need=age80 | 0.918 | 0.917 | -0.001 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.920 | 0.917 | -0.004 |
| llama-3.1-8b | dispatch | area=social_housing | 0.929 | 0.917 | -0.013 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.930 | 0.917 | -0.014 |
| llama-3.1-8b | dispatch | need=infant | 0.931 | 0.917 | -0.014 |
| llama-3.1-8b | dispatch | origin=syrian | 0.932 | 0.917 | -0.015 |
| llama-3.1-8b | dispatch | need=pregnant | 0.938 | 0.917 | -0.022 |
| llama-3.1-8b | dispatch | origin=romanian | 0.940 | 0.917 | -0.024 |
| llama-3.1-8b | dispatch | placebo | 0.953 | 0.917 | -0.036 |
| llama-3.1-8b | dispatch | area=roma_settlement | 1.000 | 0.917 | -0.083 |
| llama-3.1-8b | evacuation | area=villas | 0.965 | 0.977 | 0.012 |
| llama-3.1-8b | evacuation | area=social_housing | 0.976 | 0.977 | 0.001 |
| llama-3.1-8b | evacuation | need=infant | 0.988 | 0.977 | -0.012 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.989 | 0.977 | -0.012 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | need=age80 | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | need=pregnant | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | need=wheelchair | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | origin=romanian | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | origin=syrian | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | placebo | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | housing | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | area=social_housing | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | area=villas | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | gender=female | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | need=age80 | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | need=dialysis | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | need=infant | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | need=pregnant | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | need=wheelchair | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | origin=romanian | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | origin=syrian | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | placebo | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | housing | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | relief | placebo | 0.915 | 0.934 | 0.020 |
| llama-3.1-8b | relief | area=social_housing | 0.919 | 0.934 | 0.015 |
| llama-3.1-8b | relief | need=wheelchair | 0.931 | 0.934 | 0.004 |
| llama-3.1-8b | relief | area=villas | 0.934 | 0.934 | 0.000 |
| llama-3.1-8b | relief | need=dialysis | 0.935 | 0.934 | -0.001 |
| llama-3.1-8b | relief | origin=syrian | 0.936 | 0.934 | -0.002 |
| llama-3.1-8b | relief | need=infant | 0.959 | 0.934 | -0.025 |
| llama-3.1-8b | relief | origin=romanian | 0.962 | 0.934 | -0.028 |
| llama-3.1-8b | relief | need=pregnant | 0.963 | 0.934 | -0.029 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.934 | -0.032 |
| llama-3.1-8b | relief | origin=local_migrant | 0.986 | 0.934 | -0.052 |
| llama-3.1-8b | relief | need=age80 | 0.986 | 0.934 | -0.052 |
| llama-3.1-8b | triage | need=infant | 0.957 | 0.974 | 0.017 |
| llama-3.1-8b | triage | need=wheelchair | 0.959 | 0.974 | 0.015 |
| llama-3.1-8b | triage | placebo | 0.971 | 0.974 | 0.003 |
| llama-3.1-8b | triage | need=dialysis | 0.972 | 0.974 | 0.002 |
| llama-3.1-8b | triage | origin=romanian | 0.972 | 0.974 | 0.002 |
| llama-3.1-8b | triage | origin=local_migrant | 0.973 | 0.974 | 0.001 |
| llama-3.1-8b | triage | need=age80 | 0.986 | 0.974 | -0.012 |
| llama-3.1-8b | triage | origin=syrian | 0.987 | 0.974 | -0.013 |
| llama-3.1-8b | triage | need=pregnant | 1.000 | 0.974 | -0.026 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | Intercept | -0.370 | 0.336 | 0.271 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.103 | 0.375 | 0.784 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | -0.449 | 0.379 | 0.236 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.194 | 0.375 | 0.605 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.448 | 0.373 | 0.230 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.210 | 0.377 | 0.577 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.152 | 0.373 | 0.685 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | 0.010 | 0.379 | 0.979 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.033 | 0.373 | 0.929 |  |
| llama-3.1-8b | dispatch | C(language)[T.en] | 0.418 | 0.441 | 0.344 |  |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 0.130 | 0.453 | 0.775 |  |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.224 | 0.150 | 0.134 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.637 | 0.523 | 0.223 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.395 | 0.524 | 0.451 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.296 | 0.526 | 0.573 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.733 | 0.520 | 0.159 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -0.341 | 0.521 | 0.513 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.510 | 0.519 | 0.326 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.332 | 0.529 | 0.530 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.878 | 0.527 | 0.096 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.011 | 0.530 | 0.983 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | 0.257 | 0.534 | 0.631 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | 0.183 | 0.530 | 0.730 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.128 | 0.529 | 0.809 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.177 | 0.529 | 0.739 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.066 | 0.528 | 0.901 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | 0.615 | 0.534 | 0.250 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.146 | 0.530 | 0.783 |  |
| llama-3.1-8b | evacuation | Intercept | 0.658 | 0.272 | 0.015 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.045 | 0.286 | 0.874 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.036 | 0.287 | 0.000 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.138 | 0.283 | 0.626 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | -0.019 | 0.284 | 0.947 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.154 | 0.283 | 0.585 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.400 | 0.338 | 0.237 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.200 | 0.338 | 0.554 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.375 | 0.197 | 0.057 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.388 | 0.397 | 0.329 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.163 | 0.400 | 0.684 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.538 | 0.395 | 0.173 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.530 | 0.397 | 0.182 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.219 | 0.396 | 0.580 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.183 | 0.399 | 0.646 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.066 | 0.398 | 0.869 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.352 | 0.395 | 0.372 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.429 | 0.397 | 0.280 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.123 | 0.398 | 0.757 |  |
| llama-3.1-8b | housing | Intercept | 0.133 | 0.474 | 0.779 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.538 | 0.515 | 0.296 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -2.394 | 0.519 | 0.000 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female] | 0.014 | 0.519 | 0.978 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | 0.021 | 0.519 | 0.968 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | -0.023 | 0.519 | 0.965 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.496 | 0.519 | 0.340 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.346 | 0.519 | 0.506 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.680 | 0.517 | 0.000 | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.en] | 0.600 | 0.622 | 0.335 | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.fr] | 1.500 | 0.622 | 0.016 | did not converge; read with care |
| llama-3.1-8b | housing | C(clarity)[T.clear] | -0.164 | 0.271 | 0.546 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | 0.056 | 0.727 | 0.939 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.588 | 0.730 | 0.421 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.455 | 0.728 | 0.532 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.800 | 0.726 | 0.271 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.741 | 0.730 | 0.310 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -1.113 | 0.728 | 0.127 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.369 | 0.730 | 0.614 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.266 | 0.723 | 0.080 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | 0.116 | 0.723 | 0.872 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -0.204 | 0.732 | 0.780 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.415 | 0.729 | 0.569 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.673 | 0.730 | 0.356 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.772 | 0.731 | 0.291 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.005 | 0.729 | 0.168 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.028 | 0.730 | 0.159 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.865 | 0.725 | 0.233 | did not converge; read with care |
| llama-3.1-8b | relief | Intercept | -0.476 | 2.703 | 0.860 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | -0.259 | 3.018 | 0.932 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -2.907 | 3.018 | 0.335 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 4.235 | 3.081 | 0.169 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | 3.459 | 3.036 | 0.255 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 7.935 | 3.037 | 0.009 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 2.105 | 3.741 | 0.574 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 8.448 | 3.741 | 0.024 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | 1.140 | 1.632 | 0.485 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | 0.794 | 4.515 | 0.860 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | -0.710 | 4.470 | 0.874 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -3.397 | 4.512 | 0.452 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -3.913 | 4.465 | 0.381 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -4.707 | 4.504 | 0.296 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -5.433 | 4.539 | 0.231 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -9.212 | 4.452 | 0.039 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -8.989 | 4.535 | 0.047 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -9.217 | 4.420 | 0.037 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -10.610 | 4.467 | 0.018 |  |
| llama-3.1-8b | triage | Intercept | 0.311 | 0.164 | 0.058 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | -0.008 | 0.190 | 0.967 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | 0.133 | 0.184 | 0.472 |  |
| llama-3.1-8b | triage | C(language)[T.en] | -0.251 | 0.190 | 0.186 |  |
| llama-3.1-8b | triage | C(language)[T.fr] | -0.107 | 0.183 | 0.561 |  |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.266 | 0.180 | 0.140 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.059 | 0.272 | 0.828 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.034 | 0.268 | 0.899 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.086 | 0.266 | 0.747 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.252 | 0.257 | 0.329 |  |
