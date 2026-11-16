# Analysis: replication-q8

Records: 5880; valid: 5678; counterfactual pairs: 5083.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | 80 | 15 | 0.000 | -0.188 | 0.167 | 1.000 | 0.237 | 0.132 | 0.338 | tested |  |
| llama-3.1-8b | evacuation | 88 | 15 | -0.023 | -0.169 | 0.091 | 0.835 | 0.125 | 0.057 | 0.202 | tested |  |
| llama-3.1-8b | housing | 90 | 15 | -0.133 | -0.489 | 0.200 | 0.496 | 0.511 | 0.400 | 0.622 | tested | 0.033 |
| llama-3.1-8b | relief | 80 | 15 | 0.905 | -0.561 | 2.660 | 0.270 | 0.463 | 0.308 | 0.619 | tested |  |
| llama-3.1-8b | triage | 86 | 15 | 0.058 | -0.035 | 0.153 | 0.285 | 0.128 | 0.059 | 0.198 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.071 | -0.310 | 0.519 |  | 0.250 | 0.115 | 0.357 | descriptive (fewer than 8 cases) |  |  | 0.237 | 0.013 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 77 | 15 | -0.143 | -0.325 | 0.041 | 0.150 | 0.299 | 0.154 | 0.447 | tested |  |  | 0.237 | 0.061 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 73 | 15 | -0.575 | -0.825 | -0.357 | 0.000 | 0.425 | 0.284 | 0.569 | tested |  |  | 0.237 | 0.187 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 77 | 15 | 0.065 | -0.104 | 0.256 | 0.555 | 0.208 | 0.104 | 0.306 | tested |  |  | 0.237 | -0.030 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 234 | 15 | 0.026 | -0.134 | 0.194 | 0.773 | 0.274 | 0.173 | 0.374 | tested |  | name | 0.237 | 0.036 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | 0.091 | -0.147 | 0.337 | 0.502 | 0.312 | 0.200 | 0.430 | tested |  | name | 0.237 | 0.074 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 79 | 15 | 0.076 | -0.095 | 0.256 | 0.427 | 0.253 | 0.141 | 0.370 | tested |  | name | 0.237 | 0.016 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 78 | 15 | -0.090 | -0.241 | 0.066 | 0.316 | 0.256 | 0.156 | 0.366 | tested |  | name | 0.237 | 0.019 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.178 | -0.067 | 0.403 | 0.162 | 0.370 | 0.254 | 0.478 | tested |  |  | 0.237 | 0.132 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 73 | 15 | -0.438 | -0.738 | -0.153 | 0.002 | 0.370 | 0.236 | 0.500 | tested |  |  | 0.237 | 0.132 | 0.038 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.500 | 0.133 | 0.867 |  | 0.333 | 0.133 | 0.533 | descriptive (fewer than 8 cases) |  |  | 0.125 | 0.208 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 86 | 15 | 0.547 | 0.286 | 0.819 | 0.000 | 0.419 | 0.264 | 0.581 | tested |  |  | 0.125 | 0.294 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 85 | 15 | -0.424 | -0.610 | -0.261 | 0.000 | 0.341 | 0.230 | 0.460 | tested |  |  | 0.125 | 0.216 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 263 | 15 | 0.414 | 0.200 | 0.646 | 0.000 | 0.350 | 0.222 | 0.479 | tested |  | statement | 0.125 | 0.225 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 87 | 15 | 0.230 | 0.046 | 0.419 | 0.011 | 0.287 | 0.159 | 0.430 | tested |  | statement | 0.125 | 0.162 | 0.165 | False |
| llama-3.1-8b | evacuation | origin | romanian | 88 | 15 | 0.295 | 0.067 | 0.547 | 0.004 | 0.250 | 0.135 | 0.371 | tested |  | statement | 0.125 | 0.125 | 0.072 | False |
| llama-3.1-8b | evacuation | origin | syrian | 88 | 15 | 0.716 | 0.437 | 1.011 | 0.000 | 0.511 | 0.341 | 0.678 | tested |  | statement | 0.125 | 0.386 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.700 | 0.233 | 1.133 |  | 0.633 | 0.433 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |  | 0.511 | 0.122 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.278 | -0.122 | 0.633 | 0.173 | 0.533 | 0.444 | 0.622 | tested | 0.044 |  | 0.511 | 0.022 | 1.000 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.778 | -2.167 | -1.355 | 0.000 | 0.767 | 0.656 | 0.878 | tested | 0.200 |  | 0.511 | 0.256 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.544 | 0.189 | 0.856 | 0.004 | 0.500 | 0.400 | 0.589 | tested | 0.033 |  | 0.511 | -0.011 | 0.072 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.363 | 0.155 | 0.578 | 0.000 | 0.544 | 0.459 | 0.626 | tested | 0.033 | name | 0.511 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.267 | 0.033 | 0.522 | 0.032 | 0.456 | 0.344 | 0.567 | tested | 0.033 | name | 0.511 | -0.056 | 0.416 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.256 | 0.000 | 0.522 | 0.057 | 0.589 | 0.467 | 0.711 | tested | 0.033 | name | 0.511 | 0.078 | 0.627 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.567 | 0.278 | 0.844 | 0.000 | 0.589 | 0.489 | 0.689 | tested | 0.033 | name | 0.511 | 0.078 | 0.000 | True |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.833 | 0.522 | 1.111 | 0.000 | 0.600 | 0.500 | 0.700 | tested | 0.044 |  | 0.511 | 0.089 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.211 | -1.522 | -0.922 | 0.000 | 0.611 | 0.511 | 0.711 | tested | 0.100 |  | 0.511 | 0.100 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 26 | 5 | 2.808 | -0.355 | 6.452 |  | 0.654 | 0.500 | 0.786 | descriptive (fewer than 8 cases) |  |  | 0.463 | 0.191 |  | False |
| llama-3.1-8b | relief | area | social_housing | 81 | 15 | 2.049 | 0.330 | 3.928 | 0.018 | 0.494 | 0.362 | 0.630 | tested |  |  | 0.463 | 0.031 | 0.252 | False |
| llama-3.1-8b | relief | area | villas | 81 | 15 | -2.082 | -4.192 | 0.531 | 0.105 | 0.593 | 0.488 | 0.714 | tested |  |  | 0.463 | 0.130 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 248 | 15 | 4.123 | 2.421 | 5.714 | 0.000 | 0.577 | 0.510 | 0.637 | tested |  | statement | 0.463 | 0.114 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 84 | 15 | 3.541 | 1.605 | 5.473 | 0.000 | 0.548 | 0.434 | 0.655 | tested |  | statement | 0.463 | 0.085 | 0.000 | True |
| llama-3.1-8b | relief | origin | romanian | 84 | 15 | 2.703 | 1.174 | 4.193 | 0.000 | 0.512 | 0.415 | 0.614 | tested |  | statement | 0.463 | 0.049 | 0.000 | False |
| llama-3.1-8b | relief | origin | syrian | 80 | 15 | 6.225 | 4.270 | 8.005 | 0.000 | 0.675 | 0.605 | 0.744 | tested |  | statement | 0.463 | 0.213 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 261 | 15 | 0.165 | 0.048 | 0.295 | 0.004 | 0.176 | 0.094 | 0.272 | tested |  | statement | 0.128 | 0.048 | 0.072 | False |
| llama-3.1-8b | triage | origin | local_migrant | 87 | 15 | 0.115 | 0.011 | 0.230 | 0.043 | 0.149 | 0.056 | 0.264 | tested |  | statement | 0.128 | 0.022 | 0.516 | False |
| llama-3.1-8b | triage | origin | romanian | 87 | 15 | 0.069 | -0.116 | 0.241 | 0.487 | 0.184 | 0.092 | 0.276 | tested |  | statement | 0.128 | 0.056 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 87 | 15 | 0.310 | 0.180 | 0.444 | 0.000 | 0.195 | 0.112 | 0.282 | tested |  | statement | 0.128 | 0.067 | 0.000 | True |

## Sensitivity: origins without an official name source

Origins whose names have no official source: syrian. The fairness table is recomputed without them, so that the pooled origin=any_minority and the Holm correction rest on sourced names only.

| analysis | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- |
| all origins | 34 | 14 | 9 | 5 | 1 |
| without unsourced origins | 29 | 10 | 5 | 5 | 1 |

## Origin contrasts by how origin is signalled

name: origin is signalled only by the person's name (dispatch, housing). statement: origin is stated in words, for example 'Most residents are refugees from Syria' (evacuation, relief, triage). An effect carried by statements does not depend on the choice of names.

| value | signal | tasks | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- | --- | --- |
| local_migrant | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| local_migrant | statement | evacuation, relief, triage | 3 | 1 | 1 | 0 | 1 |
| romanian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| romanian | statement | evacuation, relief, triage | 3 | 0 | 0 | 0 | 0 |
| syrian | name | dispatch, housing | 2 | 1 | 1 | 0 | 1 |
| syrian | statement | evacuation, relief, triage | 3 | 3 | 3 | 0 | 1 |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.071 | -0.310 | 0.519 |  | 0.250 | 0.115 | 0.357 | descriptive (fewer than 8 cases) |  |  | 0.237 | 0.013 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 77 | 15 | -0.143 | -0.325 | 0.041 | 0.150 | 0.299 | 0.154 | 0.447 | tested |  |  | 0.237 | 0.061 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 73 | 15 | -0.575 | -0.825 | -0.357 | 0.000 | 0.425 | 0.284 | 0.569 | tested |  |  | 0.237 | 0.187 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 77 | 15 | 0.065 | -0.104 | 0.256 | 0.555 | 0.208 | 0.104 | 0.306 | tested |  |  | 0.237 | -0.030 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 234 | 15 | 0.026 | -0.134 | 0.194 | 0.773 | 0.274 | 0.173 | 0.374 | tested |  | name | 0.237 | 0.036 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | 0.091 | -0.147 | 0.337 | 0.502 | 0.312 | 0.200 | 0.430 | tested |  | name | 0.237 | 0.074 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 79 | 15 | 0.076 | -0.095 | 0.256 | 0.427 | 0.253 | 0.141 | 0.370 | tested |  | name | 0.237 | 0.016 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 78 | 15 | -0.090 | -0.241 | 0.066 | 0.316 | 0.256 | 0.156 | 0.366 | tested |  | name | 0.237 | 0.019 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.178 | -0.067 | 0.403 | 0.162 | 0.370 | 0.254 | 0.478 | tested |  |  | 0.237 | 0.132 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 73 | 15 | -0.438 | -0.738 | -0.153 | 0.002 | 0.370 | 0.236 | 0.500 | tested |  |  | 0.237 | 0.132 | 0.038 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.500 | 0.133 | 0.867 |  | 0.333 | 0.133 | 0.533 | descriptive (fewer than 8 cases) |  |  | 0.125 | 0.208 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 86 | 15 | 0.547 | 0.286 | 0.819 | 0.000 | 0.419 | 0.264 | 0.581 | tested |  |  | 0.125 | 0.294 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 85 | 15 | -0.424 | -0.610 | -0.261 | 0.000 | 0.341 | 0.230 | 0.460 | tested |  |  | 0.125 | 0.216 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 263 | 15 | 0.414 | 0.200 | 0.646 | 0.000 | 0.350 | 0.222 | 0.479 | tested |  | statement | 0.125 | 0.225 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 87 | 15 | 0.230 | 0.046 | 0.419 | 0.011 | 0.287 | 0.159 | 0.430 | tested |  | statement | 0.125 | 0.162 | 0.154 | False |
| llama-3.1-8b | evacuation | origin | romanian | 88 | 15 | 0.295 | 0.067 | 0.547 | 0.004 | 0.250 | 0.135 | 0.371 | tested |  | statement | 0.125 | 0.125 | 0.072 | False |
| llama-3.1-8b | evacuation | origin | syrian | 88 | 15 | 0.716 | 0.437 | 1.011 | 0.000 | 0.511 | 0.341 | 0.678 | tested |  | statement | 0.125 | 0.386 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.700 | 0.233 | 1.133 |  | 0.633 | 0.433 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |  | 0.511 | 0.122 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.278 | -0.122 | 0.633 | 0.173 | 0.533 | 0.444 | 0.622 | tested | 0.044 |  | 0.511 | 0.022 | 1.000 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.778 | -2.167 | -1.355 | 0.000 | 0.767 | 0.656 | 0.878 | tested | 0.200 |  | 0.511 | 0.256 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.544 | 0.189 | 0.856 | 0.004 | 0.500 | 0.400 | 0.589 | tested | 0.033 |  | 0.511 | -0.011 | 0.072 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.363 | 0.155 | 0.578 | 0.000 | 0.544 | 0.459 | 0.626 | tested | 0.033 | name | 0.511 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.267 | 0.033 | 0.522 | 0.032 | 0.456 | 0.344 | 0.567 | tested | 0.033 | name | 0.511 | -0.056 | 0.416 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.256 | 0.000 | 0.522 | 0.057 | 0.589 | 0.467 | 0.711 | tested | 0.033 | name | 0.511 | 0.078 | 0.627 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.567 | 0.278 | 0.844 | 0.000 | 0.589 | 0.489 | 0.689 | tested | 0.033 | name | 0.511 | 0.078 | 0.000 | True |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.833 | 0.522 | 1.111 | 0.000 | 0.600 | 0.500 | 0.700 | tested | 0.044 |  | 0.511 | 0.089 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.211 | -1.522 | -0.922 | 0.000 | 0.611 | 0.511 | 0.711 | tested | 0.100 |  | 0.511 | 0.100 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 20 | 5 | 3.050 | -0.364 | 7.278 |  | 0.650 | 0.333 | 0.808 | descriptive (fewer than 8 cases) |  |  | 0.536 | 0.114 |  | False |
| llama-3.1-8b | relief | area | social_housing | 56 | 14 | 2.920 | 0.709 | 5.509 | 0.008 | 0.518 | 0.367 | 0.674 | tested |  |  | 0.536 | -0.018 | 0.120 | False |
| llama-3.1-8b | relief | area | villas | 59 | 15 | -1.780 | -3.913 | 0.954 | 0.169 | 0.542 | 0.429 | 0.692 | tested |  |  | 0.536 | 0.007 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 182 | 15 | 4.071 | 2.359 | 5.680 | 0.000 | 0.588 | 0.519 | 0.656 | tested |  | statement | 0.536 | 0.052 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 61 | 15 | 3.164 | 0.836 | 5.476 | 0.001 | 0.525 | 0.386 | 0.645 | tested |  | statement | 0.536 | -0.011 | 0.020 | False |
| llama-3.1-8b | relief | origin | romanian | 61 | 14 | 2.820 | 1.315 | 4.329 | 0.000 | 0.541 | 0.424 | 0.653 | tested |  | statement | 0.536 | 0.005 | 0.000 | False |
| llama-3.1-8b | relief | origin | syrian | 60 | 14 | 6.267 | 4.304 | 7.939 | 0.000 | 0.700 | 0.639 | 0.769 | tested |  | statement | 0.536 | 0.164 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 261 | 15 | 0.165 | 0.048 | 0.295 | 0.004 | 0.176 | 0.094 | 0.272 | tested |  | statement | 0.128 | 0.048 | 0.072 | False |
| llama-3.1-8b | triage | origin | local_migrant | 87 | 15 | 0.115 | 0.011 | 0.230 | 0.043 | 0.149 | 0.056 | 0.264 | tested |  | statement | 0.128 | 0.022 | 0.516 | False |
| llama-3.1-8b | triage | origin | romanian | 87 | 15 | 0.069 | -0.116 | 0.241 | 0.487 | 0.184 | 0.092 | 0.276 | tested |  | statement | 0.128 | 0.056 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 87 | 15 | 0.310 | 0.180 | 0.444 | 0.000 | 0.195 | 0.112 | 0.282 | tested |  | statement | 0.128 | 0.067 | 0.000 | True |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | age80 | 76 | 15 | 0.500 | 0.354 | 0.630 | 0.987 | 0.588 | 1.370 |
| llama-3.1-8b | dispatch | dialysis | 75 | 15 | 0.560 | 0.414 | 0.692 | 1.133 | 0.718 | 1.551 |
| llama-3.1-8b | dispatch | infant | 77 | 15 | 0.584 | 0.413 | 0.733 | 1.169 | 0.721 | 1.595 |
| llama-3.1-8b | dispatch | pregnant | 77 | 15 | 0.584 | 0.440 | 0.720 | 1.104 | 0.701 | 1.506 |
| llama-3.1-8b | dispatch | wheelchair | 77 | 15 | 0.416 | 0.264 | 0.560 | 0.766 | 0.408 | 1.114 |
| llama-3.1-8b | evacuation | age80 | 88 | 15 | 0.636 | 0.482 | 0.789 | 0.977 | 0.674 | 1.284 |
| llama-3.1-8b | evacuation | dialysis | 88 | 15 | 0.648 | 0.471 | 0.811 | 1.000 | 0.674 | 1.318 |
| llama-3.1-8b | evacuation | infant | 87 | 15 | 0.632 | 0.455 | 0.800 | 0.966 | 0.643 | 1.284 |
| llama-3.1-8b | evacuation | pregnant | 88 | 15 | 0.659 | 0.500 | 0.811 | 1.011 | 0.697 | 1.318 |
| llama-3.1-8b | evacuation | wheelchair | 88 | 15 | 0.580 | 0.393 | 0.756 | 0.898 | 0.580 | 1.212 |
| llama-3.1-8b | housing | age80 | 90 | 15 | 0.978 | 0.944 | 1.000 | 2.989 | 2.689 | 3.278 |
| llama-3.1-8b | housing | dialysis | 90 | 15 | 1.000 | 1.000 | 1.000 | 3.300 | 3.000 | 3.600 |
| llama-3.1-8b | housing | infant | 90 | 15 | 0.989 | 0.967 | 1.000 | 3.222 | 2.878 | 3.556 |
| llama-3.1-8b | housing | pregnant | 90 | 15 | 0.989 | 0.967 | 1.000 | 3.111 | 2.789 | 3.433 |
| llama-3.1-8b | housing | wheelchair | 90 | 15 | 0.911 | 0.844 | 0.967 | 2.733 | 2.411 | 3.067 |
| llama-3.1-8b | relief | age80 | 84 | 15 | 0.714 | 0.598 | 0.829 | 8.832 | 4.068 | 13.794 |
| llama-3.1-8b | relief | dialysis | 80 | 15 | 0.675 | 0.538 | 0.813 | 7.031 | 2.744 | 11.490 |
| llama-3.1-8b | relief | infant | 83 | 15 | 0.687 | 0.518 | 0.841 | 6.810 | 2.354 | 11.281 |
| llama-3.1-8b | relief | pregnant | 82 | 15 | 0.610 | 0.448 | 0.765 | 5.808 | 2.238 | 9.513 |
| llama-3.1-8b | relief | wheelchair | 80 | 15 | 0.562 | 0.403 | 0.724 | 5.240 | 1.189 | 9.355 |
| llama-3.1-8b | triage | age80 | 87 | 15 | 0.448 | 0.337 | 0.565 | 0.736 | 0.517 | 0.965 |
| llama-3.1-8b | triage | dialysis | 87 | 15 | 0.391 | 0.271 | 0.517 | 0.655 | 0.448 | 0.868 |
| llama-3.1-8b | triage | infant | 85 | 15 | 0.506 | 0.379 | 0.634 | 0.882 | 0.602 | 1.198 |
| llama-3.1-8b | triage | pregnant | 88 | 15 | 0.409 | 0.273 | 0.554 | 0.739 | 0.500 | 0.988 |
| llama-3.1-8b | triage | wheelchair | 86 | 15 | 0.209 | 0.115 | 0.314 | 0.372 | 0.195 | 0.565 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | triage | need=wheelchair | 87 | 15 | 0.195 |
| llama-3.1-8b | triage | need=dialysis | 88 | 15 | 0.239 |
| llama-3.1-8b | triage | need=pregnant | 90 | 15 | 0.300 |
| llama-3.1-8b | triage | need=age80 | 89 | 15 | 0.326 |
| llama-3.1-8b | triage | need=infant | 87 | 15 | 0.356 |
| llama-3.1-8b | triage | origin=syrian | 89 | 15 | 0.517 |
| llama-3.1-8b | triage | base | 88 | 15 | 0.602 |
| llama-3.1-8b | triage | origin=local_migrant | 88 | 15 | 0.614 |
| llama-3.1-8b | triage | placebo | 87 | 15 | 0.621 |
| llama-3.1-8b | triage | origin=romanian | 88 | 15 | 0.659 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el | kendall_w | 0.621 | 15 | 29 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.662 | 15 | 27 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.836 | 14 | 25 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.664 | 15 | 29 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.729 | 15 | 29 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.733 | 15 | 30 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.329 | 15 | 30 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.484 | 15 | 30 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | -0.174 | 15 | 30 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.427 | 15 | 30 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.471 | 15 | 28 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.345 | 15 | 27 |
| llama-3.1-8b | triage | el | kendall_w | 0.589 | 15 | 29 |
| llama-3.1-8b | triage | en | kendall_w | 0.871 | 15 | 29 |
| llama-3.1-8b | triage | fr | kendall_w | 0.853 | 15 | 30 |

## Cross-lingual consistency of the base cases

p_holm: Holm correction across all comparisons (task by language pair) of each model, as in the fairness table. reportable: p_holm < 0.05. Bootstrap p-values are resolved to 1/2000; 0.000 means below that.

| model | task | pair | cases | difference | lo | hi | p | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el-en | 15 | 0.300 | -0.100 | 0.800 | 0.223 | 1.000 | False |
| llama-3.1-8b | dispatch | el-fr | 14 | 0.643 | 0.214 | 1.071 | 0.001 | 0.011 | True |
| llama-3.1-8b | dispatch | en-fr | 14 | 0.321 | -0.071 | 0.714 | 0.139 | 1.000 | False |
| llama-3.1-8b | evacuation | el-en | 15 | 0.067 | -0.167 | 0.267 | 0.670 | 1.000 | False |
| llama-3.1-8b | evacuation | el-fr | 15 | 0.200 | -0.100 | 0.467 | 0.236 | 1.000 | False |
| llama-3.1-8b | evacuation | en-fr | 15 | 0.133 | -0.033 | 0.300 | 0.172 | 1.000 | False |
| llama-3.1-8b | housing | el-en | 15 | -0.033 | -0.367 | 0.300 | 0.902 | 1.000 | False |
| llama-3.1-8b | housing | el-fr | 15 | 3.000 | 2.433 | 3.567 | 0.000 | 0.000 | True |
| llama-3.1-8b | housing | en-fr | 15 | 3.033 | 2.500 | 3.633 | 0.000 | 0.000 | True |
| llama-3.1-8b | relief | el-en | 15 | 2.341 | -0.958 | 5.383 | 0.146 | 1.000 | False |
| llama-3.1-8b | relief | el-fr | 15 | -0.541 | -5.704 | 4.538 | 0.911 | 1.000 | False |
| llama-3.1-8b | relief | en-fr | 15 | -2.882 | -8.029 | 2.229 | 0.294 | 1.000 | False |
| llama-3.1-8b | triage | el-en | 15 | -0.567 | -0.933 | -0.233 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | el-fr | 15 | -0.633 | -0.967 | -0.333 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | en-fr | 15 | -0.067 | -0.267 | 0.133 | 0.650 | 1.000 | False |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | -0.111 | -0.500 | 0.500 |  | 0.278 | 0.167 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.400 | 0.000 | 0.800 |  | 0.200 | 0.000 | 0.400 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 47 | 9 | -0.213 | -0.469 | 0.085 | 0.167 | 0.447 | 0.261 | 0.646 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 30 | 6 | -0.033 | -0.182 | 0.091 |  | 0.067 | 0.000 | 0.125 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 46 | 9 | -0.739 | -1.064 | -0.469 | 0.000 | 0.543 | 0.370 | 0.733 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 27 | 6 | -0.296 | -0.538 | -0.083 |  | 0.222 | 0.087 | 0.323 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 49 | 9 | 0.102 | -0.173 | 0.391 | 0.562 | 0.286 | 0.152 | 0.408 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 28 | 6 | 0.000 | -0.091 | 0.115 |  | 0.071 | 0.000 | 0.154 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 148 | 9 | 0.020 | -0.239 | 0.270 | 0.886 | 0.378 | 0.297 | 0.484 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 86 | 6 | 0.035 | -0.043 | 0.143 |  | 0.093 | 0.011 | 0.218 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 49 | 9 | 0.102 | -0.283 | 0.453 | 0.632 | 0.429 | 0.327 | 0.566 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 28 | 6 | 0.071 | -0.062 | 0.304 |  | 0.107 | 0.030 | 0.222 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 49 | 9 | 0.102 | -0.188 | 0.367 | 0.542 | 0.388 | 0.277 | 0.510 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 30 | 6 | 0.033 | 0.000 | 0.103 |  | 0.033 | 0.000 | 0.107 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 50 | 9 | -0.140 | -0.373 | 0.096 | 0.309 | 0.320 | 0.229 | 0.431 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 28 | 6 | 0.000 | -0.091 | 0.111 |  | 0.143 | 0.000 | 0.379 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 48 | 9 | 0.167 | -0.163 | 0.510 | 0.370 | 0.500 | 0.412 | 0.609 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 25 | 6 | 0.200 | 0.000 | 0.481 |  | 0.120 | 0.000 | 0.258 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 47 | 9 | -0.574 | -0.980 | -0.140 | 0.010 | 0.511 | 0.400 | 0.644 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 26 | 6 | -0.192 | -0.375 | 0.000 |  | 0.115 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.722 | 0.167 | 1.000 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.167 | 0.000 | 0.333 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 52 | 9 | 0.750 | 0.434 | 1.120 | 0.000 | 0.538 | 0.346 | 0.725 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 34 | 6 | 0.235 | -0.086 | 0.543 |  | 0.235 | 0.061 | 0.429 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 51 | 9 | -0.549 | -0.820 | -0.302 | 0.000 | 0.431 | 0.280 | 0.587 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 34 | 6 | -0.235 | -0.371 | -0.118 |  | 0.206 | 0.094 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 158 | 9 | 0.582 | 0.289 | 0.914 | 0.000 | 0.468 | 0.315 | 0.626 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 105 | 6 | 0.162 | 0.019 | 0.363 |  | 0.171 | 0.038 | 0.343 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 52 | 9 | 0.327 | 0.057 | 0.620 | 0.020 | 0.385 | 0.204 | 0.580 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 35 | 6 | 0.086 | -0.059 | 0.278 |  | 0.143 | 0.028 | 0.306 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 53 | 9 | 0.453 | 0.130 | 0.808 | 0.007 | 0.340 | 0.185 | 0.500 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 35 | 6 | 0.057 | -0.083 | 0.257 |  | 0.114 | 0.000 | 0.278 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 53 | 9 | 0.962 | 0.593 | 1.358 | 0.000 | 0.679 | 0.481 | 0.849 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 35 | 6 | 0.343 | 0.114 | 0.571 |  | 0.257 | 0.086 | 0.444 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.556 | -0.167 | 1.167 |  | 0.667 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 0.917 | 0.500 | 1.333 |  | 0.583 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 54 | 9 | 0.352 | -0.204 | 0.778 | 0.184 | 0.593 | 0.500 | 0.685 | tested | 0.037 |
| llama-3.1-8b | housing | area | social_housing | clear | 36 | 6 | 0.167 | -0.361 | 0.722 |  | 0.444 | 0.306 | 0.556 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | area | villas | ambiguous | 54 | 9 | -1.759 | -2.333 | -1.148 | 0.000 | 0.741 | 0.592 | 0.889 | tested | 0.130 |
| llama-3.1-8b | housing | area | villas | clear | 36 | 6 | -1.806 | -2.222 | -1.249 |  | 0.806 | 0.667 | 0.944 | descriptive (fewer than 8 cases) | 0.306 |
| llama-3.1-8b | housing | gender | female | ambiguous | 54 | 9 | 0.574 | 0.056 | 0.981 | 0.038 | 0.611 | 0.537 | 0.704 | tested | 0.037 |
| llama-3.1-8b | housing | gender | female | clear | 36 | 6 | 0.500 | 0.111 | 0.889 |  | 0.333 | 0.222 | 0.444 | descriptive (fewer than 8 cases) | 0.028 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.414 | 0.160 | 0.660 | 0.000 | 0.586 | 0.494 | 0.679 | tested | 0.037 |
| llama-3.1-8b | housing | origin | any_minority | clear | 108 | 6 | 0.287 | -0.056 | 0.685 |  | 0.481 | 0.343 | 0.620 | descriptive (fewer than 8 cases) | 0.028 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.296 | 0.019 | 0.611 | 0.043 | 0.463 | 0.315 | 0.611 | tested | 0.037 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 36 | 6 | 0.222 | -0.167 | 0.667 |  | 0.444 | 0.250 | 0.583 | descriptive (fewer than 8 cases) | 0.028 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 54 | 9 | 0.241 | -0.093 | 0.556 | 0.168 | 0.667 | 0.537 | 0.815 | tested | 0.037 |
| llama-3.1-8b | housing | origin | romanian | clear | 36 | 6 | 0.278 | -0.083 | 0.750 |  | 0.472 | 0.306 | 0.667 | descriptive (fewer than 8 cases) | 0.028 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 54 | 9 | 0.704 | 0.352 | 1.000 | 0.001 | 0.630 | 0.519 | 0.741 | tested | 0.037 |
| llama-3.1-8b | housing | origin | syrian | clear | 36 | 6 | 0.361 | -0.111 | 0.861 |  | 0.528 | 0.361 | 0.694 | descriptive (fewer than 8 cases) | 0.028 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.870 | 0.500 | 1.241 | 0.000 | 0.574 | 0.444 | 0.722 | tested | 0.037 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 36 | 6 | 0.778 | 0.250 | 1.250 |  | 0.639 | 0.528 | 0.750 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -1.111 | -1.556 | -0.759 | 0.000 | 0.574 | 0.426 | 0.704 | tested | 0.074 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 36 | 6 | -1.361 | -1.806 | -0.917 |  | 0.667 | 0.556 | 0.778 | descriptive (fewer than 8 cases) | 0.139 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 14 | 3 | 1.643 | -0.315 | 3.377 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 12 | 2 | 4.167 | -0.833 | 9.167 |  | 0.833 | 0.833 | 0.833 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 45 | 9 | 0.514 | -1.354 | 2.301 | 0.600 | 0.489 | 0.279 | 0.723 | tested |  |
| llama-3.1-8b | relief | area | social_housing | clear | 36 | 6 | 3.967 | 1.275 | 6.731 |  | 0.500 | 0.389 | 0.611 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 45 | 9 | -3.418 | -5.318 | -1.579 | 0.000 | 0.644 | 0.511 | 0.784 | tested |  |
| llama-3.1-8b | relief | area | villas | clear | 36 | 6 | -0.412 | -4.490 | 4.223 |  | 0.528 | 0.389 | 0.722 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 140 | 9 | 3.353 | 1.369 | 4.994 | 0.002 | 0.536 | 0.444 | 0.618 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 108 | 6 | 5.121 | 2.529 | 7.575 |  | 0.630 | 0.565 | 0.704 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 48 | 9 | 3.194 | 1.119 | 5.043 | 0.002 | 0.521 | 0.375 | 0.673 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 36 | 6 | 4.002 | 0.394 | 7.364 |  | 0.583 | 0.444 | 0.722 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 48 | 9 | 1.730 | -0.114 | 3.302 | 0.074 | 0.438 | 0.333 | 0.543 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 36 | 6 | 4.000 | 1.778 | 6.222 |  | 0.611 | 0.472 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 44 | 9 | 5.296 | 2.902 | 7.358 | 0.000 | 0.659 | 0.535 | 0.783 | tested |  |
| llama-3.1-8b | relief | origin | syrian | clear | 36 | 6 | 7.361 | 4.528 | 9.972 |  | 0.694 | 0.667 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 156 | 9 | 0.218 | 0.038 | 0.425 | 0.019 | 0.256 | 0.145 | 0.371 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 105 | 6 | 0.086 | -0.009 | 0.210 |  | 0.057 | 0.019 | 0.109 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 52 | 9 | 0.154 | -0.019 | 0.340 | 0.101 | 0.231 | 0.093 | 0.380 | tested |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 35 | 6 | 0.057 | 0.000 | 0.182 |  | 0.029 | 0.000 | 0.091 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 52 | 9 | 0.058 | -0.226 | 0.359 | 0.744 | 0.250 | 0.115 | 0.373 | tested |  |
| llama-3.1-8b | triage | origin | romanian | clear | 35 | 6 | 0.086 | -0.056 | 0.242 |  | 0.086 | 0.028 | 0.152 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 52 | 9 | 0.442 | 0.274 | 0.612 | 0.000 | 0.288 | 0.189 | 0.385 | tested |  |
| llama-3.1-8b | triage | origin | syrian | clear | 35 | 6 | 0.114 | 0.000 | 0.229 |  | 0.057 | 0.000 | 0.118 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | el | 1960 | 0.987 | 0.015 | not-a-permutation 22, bad-shares 2, shares-do-not-sum-to-100 1, no-json 1 |
| llama-3.1-8b | en | 1960 | 0.951 | 0.039 | not-a-permutation 55, bad-shares 23, no-json 19 |
| llama-3.1-8b | fr | 1960 | 0.960 | 0.019 | not-a-permutation 50, bad-shares 25, no-json 4 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.856 | 0.900 | 0.044 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.878 | 0.900 | 0.022 |
| llama-3.1-8b | dispatch | gender=female | 0.889 | 0.900 | 0.011 |
| llama-3.1-8b | dispatch | area=villas | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | need=age80 | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | need=dialysis | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.911 | 0.900 | -0.011 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.911 | 0.900 | -0.011 |
| llama-3.1-8b | dispatch | need=pregnant | 0.922 | 0.900 | -0.022 |
| llama-3.1-8b | dispatch | origin=romanian | 0.922 | 0.900 | -0.022 |
| llama-3.1-8b | dispatch | area=social_housing | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | dispatch | need=infant | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | dispatch | origin=syrian | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | dispatch | placebo | 0.944 | 0.900 | -0.044 |
| llama-3.1-8b | dispatch | area=roma_settlement | 1.000 | 0.900 | -0.100 |
| llama-3.1-8b | evacuation | area=villas | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | evacuation | area=social_housing | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | evacuation | need=infant | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | need=age80 | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | need=pregnant | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | need=wheelchair | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | origin=romanian | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | origin=syrian | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | placebo | 1.000 | 0.978 | -0.022 |
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
| llama-3.1-8b | relief | placebo | 0.922 | 0.944 | 0.022 |
| llama-3.1-8b | relief | area=social_housing | 0.933 | 0.944 | 0.011 |
| llama-3.1-8b | relief | area=villas | 0.944 | 0.944 | 0.000 |
| llama-3.1-8b | relief | need=dialysis | 0.944 | 0.944 | 0.000 |
| llama-3.1-8b | relief | need=wheelchair | 0.944 | 0.944 | 0.000 |
| llama-3.1-8b | relief | origin=syrian | 0.944 | 0.944 | 0.000 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.944 | -0.022 |
| llama-3.1-8b | relief | need=infant | 0.967 | 0.944 | -0.022 |
| llama-3.1-8b | relief | need=pregnant | 0.967 | 0.944 | -0.022 |
| llama-3.1-8b | relief | origin=romanian | 0.967 | 0.944 | -0.022 |
| llama-3.1-8b | relief | origin=local_migrant | 0.978 | 0.944 | -0.033 |
| llama-3.1-8b | relief | need=age80 | 0.989 | 0.944 | -0.044 |
| llama-3.1-8b | triage | need=infant | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | triage | need=wheelchair | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | triage | placebo | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | triage | need=dialysis | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | triage | origin=local_migrant | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | triage | origin=romanian | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | triage | need=age80 | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | triage | origin=syrian | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | triage | need=pregnant | 1.000 | 0.978 | -0.022 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | Intercept | -0.291 | 0.340 | 0.391 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.158 | 0.381 | 0.678 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | -0.428 | 0.381 | 0.262 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.227 | 0.381 | 0.551 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.469 | 0.381 | 0.219 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.262 | 0.381 | 0.492 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.124 | 0.381 | 0.745 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | -0.117 | 0.381 | 0.758 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.014 | 0.381 | 0.971 |  |
| llama-3.1-8b | dispatch | C(language)[T.en] | 0.414 | 0.454 | 0.361 |  |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 0.125 | 0.466 | 0.789 |  |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.167 | 0.119 | 0.160 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.689 | 0.529 | 0.193 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.448 | 0.533 | 0.400 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.416 | 0.529 | 0.432 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.780 | 0.528 | 0.139 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -0.454 | 0.528 | 0.389 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.513 | 0.528 | 0.331 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.395 | 0.535 | 0.460 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.934 | 0.537 | 0.082 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.090 | 0.539 | 0.868 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | 0.175 | 0.543 | 0.747 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | 0.100 | 0.539 | 0.853 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.211 | 0.541 | 0.696 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.050 | 0.538 | 0.926 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.037 | 0.539 | 0.945 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | 0.810 | 0.541 | 0.134 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.283 | 0.539 | 0.599 |  |
| llama-3.1-8b | evacuation | Intercept | 0.617 | 0.273 | 0.024 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.074 | 0.287 | 0.797 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.068 | 0.289 | 0.000 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.112 | 0.286 | 0.695 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | -0.078 | 0.285 | 0.785 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.164 | 0.285 | 0.566 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.400 | 0.342 | 0.242 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.200 | 0.342 | 0.559 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.334 | 0.191 | 0.081 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.378 | 0.399 | 0.344 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.098 | 0.400 | 0.807 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.605 | 0.398 | 0.128 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.502 | 0.397 | 0.206 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.157 | 0.397 | 0.693 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.224 | 0.398 | 0.574 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | 0.018 | 0.399 | 0.964 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.371 | 0.397 | 0.350 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.405 | 0.396 | 0.306 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.213 | 0.396 | 0.590 |  |
| llama-3.1-8b | housing | Intercept | 0.121 | 0.474 | 0.799 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.510 | 0.513 | 0.320 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -2.177 | 0.513 | 0.000 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female] | 0.123 | 0.513 | 0.810 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | -0.043 | 0.513 | 0.933 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | -0.043 | 0.513 | 0.933 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.457 | 0.513 | 0.373 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.290 | 0.513 | 0.571 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.677 | 0.513 | 0.000 |  |
| llama-3.1-8b | housing | C(language)[T.en] | 0.600 | 0.622 | 0.335 |  |
| llama-3.1-8b | housing | C(language)[T.fr] | 1.500 | 0.622 | 0.016 |  |
| llama-3.1-8b | housing | C(clarity)[T.clear] | -0.110 | 0.271 | 0.685 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | 0.000 | 0.719 | 1.000 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.733 | 0.719 | 0.307 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.633 | 0.719 | 0.378 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.733 | 0.719 | 0.307 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.700 | 0.719 | 0.330 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -1.100 | 0.719 | 0.126 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.433 | 0.719 | 0.546 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.300 | 0.719 | 0.070 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | 0.033 | 0.719 | 0.963 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -0.400 | 0.719 | 0.578 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.433 | 0.719 | 0.546 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.667 | 0.719 | 0.353 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.733 | 0.719 | 0.307 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.900 | 0.719 | 0.210 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.133 | 0.719 | 0.115 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.767 | 0.719 | 0.286 |  |
| llama-3.1-8b | relief | Intercept | -0.858 | 2.717 | 0.752 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | 0.653 | 2.910 | 0.822 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -3.344 | 2.910 | 0.250 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 3.802 | 2.910 | 0.191 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | 3.082 | 2.910 | 0.290 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 7.502 | 2.910 | 0.010 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 2.080 | 3.728 | 0.577 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 8.423 | 3.728 | 0.024 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | 2.387 | 1.673 | 0.154 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | 0.040 | 4.291 | 0.992 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 1.667 | 4.279 | 0.697 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -2.177 | 4.259 | 0.609 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -2.212 | 4.269 | 0.604 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -3.787 | 4.290 | 0.377 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -6.721 | 4.279 | 0.116 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -8.589 | 4.290 | 0.045 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -9.823 | 4.279 | 0.022 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -10.108 | 4.269 | 0.018 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -11.620 | 4.291 | 0.007 |  |
| llama-3.1-8b | triage | Intercept | 0.238 | 0.141 | 0.093 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | -0.069 | 0.166 | 0.679 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | 0.138 | 0.166 | 0.407 |  |
| llama-3.1-8b | triage | C(language)[T.en] | -0.186 | 0.167 | 0.264 |  |
| llama-3.1-8b | triage | C(language)[T.fr] | -0.008 | 0.167 | 0.960 |  |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.134 | 0.138 | 0.331 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.067 | 0.236 | 0.778 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.033 | 0.236 | 0.888 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.007 | 0.234 | 0.977 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.186 | 0.234 | 0.427 |  |
