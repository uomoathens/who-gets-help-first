# Analysis: study-cpu

Records: 5308; valid: 5180; counterfactual pairs: 2132.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | 5 | 1 | -0.200 |  |  |  | 0.200 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | housing | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | dispatch | 24 | 9 | -0.083 | -0.238 | 0.077 | 0.415 | 0.167 | 0.042 | 0.316 | tested |  |
| krikri-8b | evacuation | 13 | 8 | -0.154 | -0.364 | 0.000 | 0.193 | 0.154 | 0.000 | 0.357 | tested |  |
| krikri-8b | housing | 13 | 7 | 0.154 | 0.000 | 0.375 |  | 0.154 | 0.000 | 0.375 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | relief | 8 | 5 | 0.625 | -2.000 | 1.875 |  | 0.375 | 0.143 | 0.625 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | 15 | 5 | 0.133 | 0.000 | 0.250 |  | 0.133 | 0.000 | 0.267 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | 12 | 7 | -0.083 | -0.250 | 0.000 |  | 0.083 | 0.000 | 0.273 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | 6 | 5 | 0.167 | 0.000 | 0.600 |  | 0.167 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | 12 | 5 | 0.167 | 0.000 | 0.308 |  | 0.500 | 0.143 | 0.786 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | relief | 7 | 4 | 2.673 | -0.500 | 3.943 |  | 0.286 | 0.000 | 0.462 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | 4 | 3 | -0.250 | -1.000 | 0.000 |  | 0.250 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | 11 | 6 | 0.364 | 0.000 | 1.500 |  | 0.091 | 0.000 | 0.377 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | 7 | 5 | -0.143 | -1.143 | 1.000 |  | 0.429 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | housing | 7 | 5 | 0.000 | -0.429 | 0.429 |  | 0.571 | 0.200 | 0.857 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | relief | 8 | 3 | -4.072 | -8.333 | -1.667 |  | 0.375 | 0.333 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | 6 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | housing | 5 | 4 | 0.200 | 0.000 | 0.750 |  | 0.200 | 0.000 | 0.750 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | relief | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 2 | 1 | 2.500 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | area | social_housing | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | -0.200 |  | False |
| apertus-8b | dispatch | area | villas | 4 | 2 | -0.750 | -2.000 | -0.333 |  | 0.500 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.300 |  | False |
| apertus-8b | dispatch | gender | female | 3 | 2 | 0.667 | 0.000 | 2.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | origin | any_minority | 10 | 3 | 0.200 | -2.000 | 0.625 |  | 0.600 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.400 |  | False |
| apertus-8b | dispatch | origin | local_migrant | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | origin | romanian | 6 | 2 | 0.333 | -2.000 | 0.800 |  | 0.667 | 0.600 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.467 |  | False |
| apertus-8b | dispatch | origin | syrian | 3 | 1 | 0.333 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.133 |  | False |
| apertus-8b | dispatch | status | asylum_seeker | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | status | seasonal_worker | 3 | 2 | 0.333 | -0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.467 |  | False |
| apertus-8b | evacuation | area | roma_settlement | 4 | 2 | 0.750 | 0.000 | 1.500 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.250 |  | False |
| apertus-8b | evacuation | area | social_housing | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | area | villas | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | origin | any_minority | 7 | 3 | 0.143 | 0.000 | 0.200 |  | 0.143 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  | 0.000 | 0.143 |  | False |
| apertus-8b | evacuation | origin | local_migrant | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | origin | romanian | 2 | 1 | 0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| apertus-8b | evacuation | origin | syrian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | housing | area | roma_settlement | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.000 |  | False |
| apertus-8b | housing | area | social_housing | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | area | villas | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | origin | any_minority | 4 | 2 | 0.500 | 0.000 | 2.000 |  | 0.750 | 0.667 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.750 |  | False |
| apertus-8b | housing | origin | local_migrant | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | origin | syrian | 3 | 2 | 1.000 | 0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.667 |  | False |
| apertus-8b | housing | status | seasonal_worker | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| krikri-8b | dispatch | area | roma_settlement | 16 | 5 | 0.688 | 0.500 | 0.812 |  | 0.438 | 0.312 | 0.636 | descriptive (fewer than 8 cases) |  | 0.167 | 0.271 |  | False |
| krikri-8b | dispatch | area | social_housing | 23 | 10 | 0.304 | 0.150 | 0.414 | 0.001 | 0.348 | 0.182 | 0.538 | tested |  | 0.167 | 0.181 | 0.011 | True |
| krikri-8b | dispatch | area | villas | 28 | 11 | -0.321 | -0.562 | -0.115 | 0.004 | 0.250 | 0.095 | 0.414 | tested |  | 0.167 | 0.083 | 0.036 | True |
| krikri-8b | dispatch | gender | female | 18 | 8 | 0.167 | -0.072 | 0.370 | 0.291 | 0.222 | 0.077 | 0.333 | tested |  | 0.167 | 0.056 | 1.000 | False |
| krikri-8b | dispatch | origin | any_minority | 74 | 11 | 0.095 | -0.109 | 0.299 | 0.424 | 0.149 | 0.048 | 0.250 | tested |  | 0.167 | -0.018 | 1.000 | False |
| krikri-8b | dispatch | origin | local_migrant | 24 | 10 | 0.167 | -0.053 | 0.368 | 0.219 | 0.208 | 0.050 | 0.400 | tested |  | 0.167 | 0.042 | 1.000 | False |
| krikri-8b | dispatch | origin | romanian | 25 | 11 | 0.040 | -0.103 | 0.222 | 0.901 | 0.080 | 0.000 | 0.161 | tested |  | 0.167 | -0.087 | 1.000 | False |
| krikri-8b | dispatch | origin | syrian | 25 | 9 | 0.080 | -0.190 | 0.389 | 0.687 | 0.160 | 0.000 | 0.321 | tested |  | 0.167 | -0.007 | 1.000 | False |
| krikri-8b | dispatch | status | asylum_seeker | 15 | 9 | 0.867 | 0.267 | 1.533 | 0.001 | 0.400 | 0.154 | 0.643 | tested |  | 0.167 | 0.233 | 0.011 | True |
| krikri-8b | dispatch | status | seasonal_worker | 22 | 9 | 0.182 | 0.037 | 0.333 | 0.048 | 0.136 | 0.000 | 0.278 | tested |  | 0.167 | -0.030 | 0.352 | False |
| krikri-8b | evacuation | area | roma_settlement | 12 | 5 | 0.583 | 0.000 | 0.933 |  | 0.417 | 0.000 | 0.688 | descriptive (fewer than 8 cases) |  | 0.154 | 0.263 |  | False |
| krikri-8b | evacuation | area | social_housing | 11 | 7 | 0.273 | 0.000 | 0.800 |  | 0.182 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.154 | 0.028 |  | False |
| krikri-8b | evacuation | area | villas | 17 | 6 | -0.588 | -1.000 | -0.333 |  | 0.471 | 0.273 | 0.750 | descriptive (fewer than 8 cases) |  | 0.154 | 0.317 |  | False |
| krikri-8b | evacuation | origin | any_minority | 33 | 8 | 0.273 | 0.029 | 0.606 | 0.044 | 0.242 | 0.057 | 0.433 | tested |  | 0.154 | 0.089 | 0.352 | False |
| krikri-8b | evacuation | origin | local_migrant | 14 | 6 | 0.286 | 0.062 | 0.778 |  | 0.214 | 0.053 | 0.500 | descriptive (fewer than 8 cases) |  | 0.154 | 0.060 |  | False |
| krikri-8b | evacuation | origin | romanian | 8 | 6 | 0.125 | -0.375 | 0.833 |  | 0.250 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.154 | 0.096 |  | False |
| krikri-8b | evacuation | origin | syrian | 11 | 6 | 0.364 | 0.000 | 0.833 |  | 0.273 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  | 0.154 | 0.119 |  | False |
| krikri-8b | housing | area | roma_settlement | 12 | 5 | 0.250 | 0.100 | 0.333 |  | 0.250 | 0.100 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.096 |  | False |
| krikri-8b | housing | area | social_housing | 13 | 6 | 0.231 | 0.071 | 0.500 |  | 0.231 | 0.071 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.077 |  | False |
| krikri-8b | housing | area | villas | 7 | 3 | -1.714 | -2.333 | -0.500 |  | 0.857 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.703 |  | False |
| krikri-8b | housing | gender | female | 17 | 8 | 0.176 | 0.000 | 0.276 | 0.188 | 0.176 | 0.000 | 0.280 | tested | 0.000 | 0.154 | 0.023 | 1.000 | False |
| krikri-8b | housing | origin | any_minority | 29 | 7 | 0.103 | -0.080 | 0.278 |  | 0.172 | 0.031 | 0.296 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.019 |  | False |
| krikri-8b | housing | origin | local_migrant | 11 | 6 | 0.091 | 0.000 | 0.273 |  | 0.091 | 0.000 | 0.273 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | -0.063 |  | False |
| krikri-8b | housing | origin | romanian | 10 | 6 | 0.000 | -0.273 | 0.273 |  | 0.200 | 0.000 | 0.400 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.046 |  | False |
| krikri-8b | housing | origin | syrian | 8 | 5 | 0.250 | 0.000 | 0.545 |  | 0.250 | 0.000 | 0.545 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.096 |  | False |
| krikri-8b | housing | status | asylum_seeker | 16 | 7 | 0.188 | 0.045 | 0.385 |  | 0.188 | 0.040 | 0.385 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.034 |  | False |
| krikri-8b | housing | status | seasonal_worker | 14 | 6 | -0.429 | -0.643 | -0.182 |  | 0.500 | 0.357 | 0.667 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.346 |  | False |
| krikri-8b | relief | area | roma_settlement | 6 | 4 | -0.500 | -1.286 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.375 | -0.375 |  | False |
| krikri-8b | relief | area | social_housing | 8 | 5 | 0.000 | -3.333 | 3.000 |  | 0.250 | 0.000 | 0.444 | descriptive (fewer than 8 cases) |  | 0.375 | -0.125 |  | False |
| krikri-8b | relief | area | villas | 6 | 4 | -3.787 | -8.860 | 0.714 |  | 0.833 | 0.571 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.458 |  | False |
| krikri-8b | relief | origin | any_minority | 22 | 5 | 0.136 | -1.292 | 2.667 |  | 0.227 | 0.130 | 0.400 | descriptive (fewer than 8 cases) |  | 0.375 | -0.148 |  | False |
| krikri-8b | relief | origin | local_migrant | 7 | 3 | -2.429 | -6.000 | 0.000 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.375 | -0.089 |  | False |
| krikri-8b | relief | origin | romanian | 7 | 4 | 0.714 | 0.000 | 1.875 |  | 0.143 | 0.000 | 0.375 | descriptive (fewer than 8 cases) |  | 0.375 | -0.232 |  | False |
| krikri-8b | relief | origin | syrian | 8 | 5 | 1.875 | 0.000 | 6.000 |  | 0.250 | 0.000 | 0.800 | descriptive (fewer than 8 cases) |  | 0.375 | -0.125 |  | False |
| krikri-8b | triage | origin | any_minority | 30 | 6 | 0.167 | 0.037 | 0.333 |  | 0.167 | 0.037 | 0.333 | descriptive (fewer than 8 cases) |  | 0.133 | 0.033 |  | False |
| krikri-8b | triage | origin | local_migrant | 10 | 6 | 0.100 | 0.000 | 0.300 |  | 0.100 | 0.000 | 0.300 | descriptive (fewer than 8 cases) |  | 0.133 | -0.033 |  | False |
| krikri-8b | triage | origin | romanian | 8 | 5 | 0.250 | 0.000 | 0.625 |  | 0.250 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.133 | 0.117 |  | False |
| krikri-8b | triage | origin | syrian | 12 | 5 | 0.167 | 0.000 | 0.267 |  | 0.167 | 0.000 | 0.267 | descriptive (fewer than 8 cases) |  | 0.133 | 0.033 |  | False |
| llama-3.1-8b | dispatch | area | roma_settlement | 5 | 3 | 0.000 | -0.333 | 1.000 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.083 | 0.317 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 10 | 7 | -0.200 | -0.500 | 0.182 |  | 0.400 | 0.125 | 0.600 | descriptive (fewer than 8 cases) |  | 0.083 | 0.317 |  | False |
| llama-3.1-8b | dispatch | area | villas | 12 | 8 | -0.750 | -1.300 | -0.357 | 0.000 | 0.500 | 0.308 | 0.727 | tested |  | 0.083 | 0.417 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 13 | 6 | -0.308 | -0.600 | 0.000 |  | 0.308 | 0.000 | 0.615 | descriptive (fewer than 8 cases) |  | 0.083 | 0.224 |  | False |
| llama-3.1-8b | dispatch | origin | any_minority | 28 | 8 | -0.179 | -0.355 | -0.033 | 0.039 | 0.143 | 0.033 | 0.241 | tested |  | 0.083 | 0.060 | 0.078 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 9 | 5 | -0.444 | -1.111 | 0.000 |  | 0.222 | 0.000 | 0.444 | descriptive (fewer than 8 cases) |  | 0.083 | 0.139 |  | False |
| llama-3.1-8b | dispatch | origin | romanian | 12 | 6 | -0.083 | -0.273 | 0.000 |  | 0.167 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.083 | 0.083 |  | False |
| llama-3.1-8b | dispatch | origin | syrian | 7 | 5 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.083 | -0.083 |  | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 12 | 7 | -0.083 | -0.727 | 0.357 |  | 0.250 | 0.083 | 0.455 | descriptive (fewer than 8 cases) |  | 0.083 | 0.167 |  | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 9 | 6 | -0.556 | -1.083 | -0.111 |  | 0.444 | 0.111 | 0.800 | descriptive (fewer than 8 cases) |  | 0.083 | 0.361 |  | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 12 | 5 | 0.583 | 0.000 | 1.188 |  | 0.333 | 0.000 | 0.643 | descriptive (fewer than 8 cases) |  | 0.167 | 0.167 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 8 | 6 | 0.500 | 0.000 | 1.143 |  | 0.375 | 0.000 | 0.778 | descriptive (fewer than 8 cases) |  | 0.167 | 0.208 |  | False |
| llama-3.1-8b | evacuation | area | villas | 12 | 6 | -0.833 | -1.385 | -0.200 |  | 0.417 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  | 0.167 | 0.250 |  | False |
| llama-3.1-8b | evacuation | origin | any_minority | 38 | 9 | 0.500 | 0.160 | 0.776 | 0.000 | 0.289 | 0.120 | 0.417 | tested |  | 0.167 | 0.123 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 14 | 9 | 0.286 | 0.000 | 0.556 | 0.192 | 0.143 | 0.000 | 0.286 | tested |  | 0.167 | -0.024 | 0.192 | False |
| llama-3.1-8b | evacuation | origin | romanian | 11 | 6 | 0.455 | 0.111 | 0.727 |  | 0.273 | 0.091 | 0.417 | descriptive (fewer than 8 cases) |  | 0.167 | 0.106 |  | False |
| llama-3.1-8b | evacuation | origin | syrian | 13 | 7 | 0.769 | 0.333 | 1.188 |  | 0.462 | 0.250 | 0.637 | descriptive (fewer than 8 cases) |  | 0.167 | 0.295 |  | False |
| llama-3.1-8b | housing | area | roma_settlement | 8 | 4 | 1.250 | 0.375 | 3.000 |  | 0.750 | 0.400 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.250 |  | False |
| llama-3.1-8b | housing | area | social_housing | 13 | 6 | -0.462 | -1.083 | 0.091 |  | 0.615 | 0.429 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.115 |  | False |
| llama-3.1-8b | housing | area | villas | 14 | 6 | -2.857 | -3.462 | -2.091 |  | 0.929 | 0.850 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.429 |  | False |
| llama-3.1-8b | housing | gender | female | 16 | 6 | 0.438 | 0.000 | 0.818 |  | 0.438 | 0.250 | 0.615 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.062 |  | False |
| llama-3.1-8b | housing | origin | any_minority | 31 | 7 | 0.226 | -0.368 | 1.143 |  | 0.387 | 0.214 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.113 |  | False |
| llama-3.1-8b | housing | origin | local_migrant | 13 | 6 | 0.154 | -0.455 | 1.182 |  | 0.385 | 0.222 | 0.471 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.115 |  | False |
| llama-3.1-8b | housing | origin | romanian | 7 | 5 | 0.000 | -0.600 | 0.273 |  | 0.286 | 0.000 | 0.600 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.214 |  | False |
| llama-3.1-8b | housing | origin | syrian | 11 | 6 | 0.455 | -0.700 | 2.000 |  | 0.455 | 0.167 | 0.750 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.045 |  | False |
| llama-3.1-8b | housing | status | asylum_seeker | 15 | 6 | 0.533 | 0.278 | 0.923 |  | 0.467 | 0.300 | 0.615 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.033 |  | False |
| llama-3.1-8b | housing | status | seasonal_worker | 13 | 6 | -1.000 | -2.000 | 0.000 |  | 0.538 | 0.333 | 0.714 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.038 |  | False |
| llama-3.1-8b | relief | area | roma_settlement | 8 | 3 | 4.535 | -0.098 | 11.500 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.286 | 0.214 |  | False |
| llama-3.1-8b | relief | area | social_housing | 9 | 5 | 3.635 | -1.700 | 9.804 |  | 0.778 | 0.556 | 1.000 | descriptive (fewer than 8 cases) |  | 0.286 | 0.492 |  | False |
| llama-3.1-8b | relief | area | villas | 6 | 4 | -0.938 | -4.286 | 5.500 |  | 0.500 | 0.200 | 0.800 | descriptive (fewer than 8 cases) |  | 0.286 | 0.214 |  | False |
| llama-3.1-8b | relief | origin | any_minority | 22 | 5 | 3.901 | 0.769 | 6.067 |  | 0.409 | 0.278 | 0.478 | descriptive (fewer than 8 cases) |  | 0.286 | 0.123 |  | False |
| llama-3.1-8b | relief | origin | local_migrant | 7 | 4 | 5.356 | -0.500 | 9.196 |  | 0.429 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  | 0.286 | 0.143 |  | False |
| llama-3.1-8b | relief | origin | romanian | 6 | 4 | 2.952 | -1.500 | 5.179 |  | 0.333 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  | 0.286 | 0.048 |  | False |
| llama-3.1-8b | relief | origin | syrian | 9 | 5 | 3.401 | -1.149 | 7.571 |  | 0.444 | 0.111 | 0.778 | descriptive (fewer than 8 cases) |  | 0.286 | 0.159 |  | False |
| llama-3.1-8b | triage | origin | any_minority | 10 | 4 | 0.100 | 0.000 | 0.333 |  | 0.100 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  | 0.250 | -0.150 |  | False |
| llama-3.1-8b | triage | origin | local_migrant | 3 | 3 | 0.333 | 0.000 | 1.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.250 | 0.083 |  | False |
| llama-3.1-8b | triage | origin | romanian | 4 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.250 | -0.250 |  | False |
| llama-3.1-8b | triage | origin | syrian | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.250 | -0.250 |  | False |
| meltemi-7b | dispatch | area | roma_settlement | 11 | 5 | 0.273 | 0.000 | 0.667 |  | 0.273 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.091 | 0.182 |  | False |
| meltemi-7b | dispatch | area | social_housing | 8 | 6 | 0.500 | 0.000 | 1.721 |  | 0.125 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.091 | 0.034 |  | False |
| meltemi-7b | dispatch | area | villas | 5 | 4 | -0.200 | -0.429 | 0.000 |  | 0.200 | 0.000 | 0.429 | descriptive (fewer than 8 cases) |  | 0.091 | 0.109 |  | False |
| meltemi-7b | dispatch | gender | female | 14 | 6 | -0.143 | -0.500 | 0.000 |  | 0.071 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  | 0.091 | -0.019 |  | False |
| meltemi-7b | dispatch | origin | any_minority | 39 | 6 | 0.231 | -0.262 | 1.001 |  | 0.256 | 0.105 | 0.467 | descriptive (fewer than 8 cases) |  | 0.091 | 0.166 |  | False |
| meltemi-7b | dispatch | origin | local_migrant | 13 | 4 | 0.154 | 0.000 | 0.222 |  | 0.154 | 0.000 | 0.222 | descriptive (fewer than 8 cases) |  | 0.091 | 0.063 |  | False |
| meltemi-7b | dispatch | origin | romanian | 14 | 6 | 0.357 | -0.334 | 1.500 |  | 0.286 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.091 | 0.195 |  | False |
| meltemi-7b | dispatch | origin | syrian | 12 | 6 | 0.167 | -1.091 | 1.000 |  | 0.333 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  | 0.091 | 0.242 |  | False |
| meltemi-7b | dispatch | status | asylum_seeker | 11 | 6 | -0.455 | -1.571 | 0.250 |  | 0.273 | 0.100 | 0.556 | descriptive (fewer than 8 cases) |  | 0.091 | 0.182 |  | False |
| meltemi-7b | dispatch | status | seasonal_worker | 13 | 6 | -0.154 | -0.929 | 0.727 |  | 0.231 | 0.071 | 0.462 | descriptive (fewer than 8 cases) |  | 0.091 | 0.140 |  | False |
| meltemi-7b | evacuation | area | roma_settlement | 9 | 5 | 0.889 | 0.333 | 1.800 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  | 0.429 | 0.016 |  | False |
| meltemi-7b | evacuation | area | social_housing | 3 | 2 | -1.000 | -3.000 | 0.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | -0.095 |  | False |
| meltemi-7b | evacuation | area | villas | 10 | 6 | -0.700 | -1.800 | 0.000 |  | 0.300 | 0.000 | 0.636 | descriptive (fewer than 8 cases) |  | 0.429 | -0.129 |  | False |
| meltemi-7b | evacuation | origin | any_minority | 22 | 7 | 0.000 | -0.947 | 0.577 |  | 0.455 | 0.321 | 0.667 | descriptive (fewer than 8 cases) |  | 0.429 | 0.026 |  | False |
| meltemi-7b | evacuation | origin | local_migrant | 5 | 5 | -0.200 | -1.600 | 0.800 |  | 0.600 | 0.200 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | 0.171 |  | False |
| meltemi-7b | evacuation | origin | romanian | 11 | 5 | -0.091 | -0.889 | 0.444 |  | 0.273 | 0.083 | 0.571 | descriptive (fewer than 8 cases) |  | 0.429 | -0.156 |  | False |
| meltemi-7b | evacuation | origin | syrian | 6 | 5 | 0.333 | -1.400 | 1.286 |  | 0.667 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | 0.238 |  | False |
| meltemi-7b | housing | area | roma_settlement | 6 | 5 | 0.667 | 0.125 | 1.400 |  | 0.500 | 0.125 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.071 |  | False |
| meltemi-7b | housing | area | social_housing | 7 | 4 | -0.143 | -0.750 | 0.375 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.286 |  | False |
| meltemi-7b | housing | area | villas | 11 | 6 | 0.000 | -0.400 | 0.333 |  | 0.364 | 0.133 | 0.625 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.208 |  | False |
| meltemi-7b | housing | gender | female | 7 | 5 | 0.000 | -1.167 | 0.889 |  | 0.571 | 0.167 | 0.875 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | 0.000 |  | False |
| meltemi-7b | housing | origin | any_minority | 24 | 6 | 0.208 | 0.147 | 0.312 |  | 0.333 | 0.158 | 0.583 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.238 |  | False |
| meltemi-7b | housing | origin | local_migrant | 12 | 5 | 0.167 | 0.000 | 0.364 |  | 0.333 | 0.091 | 0.571 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.238 |  | False |
| meltemi-7b | housing | origin | romanian | 6 | 4 | 0.667 | 0.250 | 1.500 |  | 0.500 | 0.250 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.071 |  | False |
| meltemi-7b | housing | origin | syrian | 6 | 5 | -0.167 | -0.600 | 0.000 |  | 0.167 | 0.000 | 0.600 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.405 |  | False |
| meltemi-7b | housing | status | asylum_seeker | 7 | 4 | 0.286 | 0.000 | 0.750 |  | 0.429 | 0.000 | 0.857 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.143 |  | False |
| meltemi-7b | housing | status | seasonal_worker | 6 | 4 | 0.167 | 0.000 | 0.429 |  | 0.167 | 0.000 | 0.429 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.405 |  | False |
| meltemi-7b | relief | area | roma_settlement | 3 | 2 | 0.000 | -5.000 | 2.500 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.292 |  | False |
| meltemi-7b | relief | area | social_housing | 4 | 3 | 2.083 | 0.000 | 3.333 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.375 | -0.125 |  | False |
| meltemi-7b | relief | area | villas | 4 | 3 | -2.917 | -8.333 | 5.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.125 |  | False |
| meltemi-7b | relief | origin | any_minority | 17 | 5 | -2.112 | -8.125 | 4.272 |  | 0.588 | 0.400 | 0.737 | descriptive (fewer than 8 cases) |  | 0.375 | 0.213 |  | False |
| meltemi-7b | relief | origin | local_migrant | 4 | 3 | -3.275 | -5.186 | 2.273 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.125 |  | False |
| meltemi-7b | relief | origin | romanian | 7 | 5 | -4.469 | -8.722 | -0.455 |  | 0.429 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  | 0.375 | 0.054 |  | False |
| meltemi-7b | relief | origin | syrian | 6 | 5 | 1.414 | -9.659 | 14.424 |  | 0.833 | 0.400 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.458 |  | False |
| meltemi-7b | triage | origin | any_minority | 17 | 5 | 0.000 | 0.000 | 0.000 |  | 0.118 | 0.000 | 0.194 | descriptive (fewer than 8 cases) |  | 0.000 | 0.118 |  | False |
| meltemi-7b | triage | origin | local_migrant | 6 | 3 | 0.000 | 0.000 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.333 |  | False |
| meltemi-7b | triage | origin | romanian | 6 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| meltemi-7b | triage | origin | syrian | 5 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 1 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | dispatch | area | villas | 1 | 1 | -4.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | dispatch | gender | female | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | any_minority | 3 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | syrian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 2 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | evacuation | area | villas | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | any_minority | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | local_migrant | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | housing | area | roma_settlement | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | area | social_housing | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | area | villas | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | housing | gender | female | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | origin | any_minority | 5 | 4 | 0.200 | 0.000 | 0.429 |  | 0.200 | 0.000 | 0.429 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.000 |  | False |
| qwen2.5-7b | housing | origin | local_migrant | 2 | 2 | 0.500 | 0.000 | 1.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | housing | origin | romanian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | origin | syrian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | status | asylum_seeker | 5 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | status | seasonal_worker | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | relief | area | roma_settlement | 3 | 2 | -1.667 | -2.500 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.333 |  | False |
| qwen2.5-7b | relief | area | villas | 2 | 2 | -2.500 | -5.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| qwen2.5-7b | relief | origin | any_minority | 5 | 2 | -1.000 | -1.667 | 0.000 |  | 0.600 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.600 |  | False |
| qwen2.5-7b | relief | origin | local_migrant | 2 | 2 | -5.000 | -5.000 | -5.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | relief | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | relief | origin | syrian | 2 | 2 | 2.500 | 0.000 | 5.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| qwen2.5-7b | triage | origin | any_minority | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | triage | origin | syrian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 2 | 1 | 2.500 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | area | social_housing | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | -0.200 |  | False |
| apertus-8b | dispatch | area | villas | 4 | 2 | -0.750 | -2.000 | -0.333 |  | 0.500 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.300 |  | False |
| apertus-8b | dispatch | gender | female | 3 | 2 | 0.667 | 0.000 | 2.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | origin | any_minority | 10 | 3 | 0.200 | -2.000 | 0.625 |  | 0.600 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.400 |  | False |
| apertus-8b | dispatch | origin | local_migrant | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | origin | romanian | 6 | 2 | 0.333 | -2.000 | 0.800 |  | 0.667 | 0.600 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.467 |  | False |
| apertus-8b | dispatch | origin | syrian | 3 | 1 | 0.333 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.133 |  | False |
| apertus-8b | dispatch | status | asylum_seeker | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.200 | 0.800 |  | False |
| apertus-8b | dispatch | status | seasonal_worker | 3 | 2 | 0.333 | -0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.467 |  | False |
| apertus-8b | evacuation | area | roma_settlement | 4 | 2 | 0.750 | 0.000 | 1.500 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.250 |  | False |
| apertus-8b | evacuation | area | social_housing | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | area | villas | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | origin | any_minority | 7 | 3 | 0.143 | 0.000 | 0.200 |  | 0.143 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  | 0.000 | 0.143 |  | False |
| apertus-8b | evacuation | origin | local_migrant | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | evacuation | origin | romanian | 2 | 1 | 0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| apertus-8b | evacuation | origin | syrian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| apertus-8b | housing | area | roma_settlement | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.000 |  | False |
| apertus-8b | housing | area | social_housing | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | area | villas | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | origin | any_minority | 4 | 2 | 0.500 | 0.000 | 2.000 |  | 0.750 | 0.667 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.750 |  | False |
| apertus-8b | housing | origin | local_migrant | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| apertus-8b | housing | origin | syrian | 3 | 2 | 1.000 | 0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 0.667 |  | False |
| apertus-8b | housing | status | seasonal_worker | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.000 | 1.000 |  | False |
| krikri-8b | dispatch | area | roma_settlement | 16 | 5 | 0.688 | 0.500 | 0.812 |  | 0.438 | 0.312 | 0.636 | descriptive (fewer than 8 cases) |  | 0.167 | 0.271 |  | False |
| krikri-8b | dispatch | area | social_housing | 23 | 10 | 0.304 | 0.150 | 0.414 | 0.001 | 0.348 | 0.182 | 0.538 | tested |  | 0.167 | 0.181 | 0.011 | True |
| krikri-8b | dispatch | area | villas | 28 | 11 | -0.321 | -0.562 | -0.115 | 0.004 | 0.250 | 0.095 | 0.414 | tested |  | 0.167 | 0.083 | 0.036 | True |
| krikri-8b | dispatch | gender | female | 18 | 8 | 0.167 | -0.072 | 0.370 | 0.291 | 0.222 | 0.077 | 0.333 | tested |  | 0.167 | 0.056 | 1.000 | False |
| krikri-8b | dispatch | origin | any_minority | 74 | 11 | 0.095 | -0.109 | 0.299 | 0.424 | 0.149 | 0.048 | 0.250 | tested |  | 0.167 | -0.018 | 1.000 | False |
| krikri-8b | dispatch | origin | local_migrant | 24 | 10 | 0.167 | -0.053 | 0.368 | 0.219 | 0.208 | 0.050 | 0.400 | tested |  | 0.167 | 0.042 | 1.000 | False |
| krikri-8b | dispatch | origin | romanian | 25 | 11 | 0.040 | -0.103 | 0.222 | 0.901 | 0.080 | 0.000 | 0.161 | tested |  | 0.167 | -0.087 | 1.000 | False |
| krikri-8b | dispatch | origin | syrian | 25 | 9 | 0.080 | -0.190 | 0.389 | 0.687 | 0.160 | 0.000 | 0.321 | tested |  | 0.167 | -0.007 | 1.000 | False |
| krikri-8b | dispatch | status | asylum_seeker | 15 | 9 | 0.867 | 0.267 | 1.533 | 0.001 | 0.400 | 0.154 | 0.643 | tested |  | 0.167 | 0.233 | 0.011 | True |
| krikri-8b | dispatch | status | seasonal_worker | 22 | 9 | 0.182 | 0.037 | 0.333 | 0.048 | 0.136 | 0.000 | 0.278 | tested |  | 0.167 | -0.030 | 0.352 | False |
| krikri-8b | evacuation | area | roma_settlement | 12 | 5 | 0.583 | 0.000 | 0.933 |  | 0.417 | 0.000 | 0.688 | descriptive (fewer than 8 cases) |  | 0.154 | 0.263 |  | False |
| krikri-8b | evacuation | area | social_housing | 11 | 7 | 0.273 | 0.000 | 0.800 |  | 0.182 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.154 | 0.028 |  | False |
| krikri-8b | evacuation | area | villas | 17 | 6 | -0.588 | -1.000 | -0.333 |  | 0.471 | 0.273 | 0.750 | descriptive (fewer than 8 cases) |  | 0.154 | 0.317 |  | False |
| krikri-8b | evacuation | origin | any_minority | 33 | 8 | 0.273 | 0.029 | 0.606 | 0.044 | 0.242 | 0.057 | 0.433 | tested |  | 0.154 | 0.089 | 0.352 | False |
| krikri-8b | evacuation | origin | local_migrant | 14 | 6 | 0.286 | 0.062 | 0.778 |  | 0.214 | 0.053 | 0.500 | descriptive (fewer than 8 cases) |  | 0.154 | 0.060 |  | False |
| krikri-8b | evacuation | origin | romanian | 8 | 6 | 0.125 | -0.375 | 0.833 |  | 0.250 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.154 | 0.096 |  | False |
| krikri-8b | evacuation | origin | syrian | 11 | 6 | 0.364 | 0.000 | 0.833 |  | 0.273 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  | 0.154 | 0.119 |  | False |
| krikri-8b | housing | area | roma_settlement | 12 | 5 | 0.250 | 0.100 | 0.333 |  | 0.250 | 0.100 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.096 |  | False |
| krikri-8b | housing | area | social_housing | 13 | 6 | 0.231 | 0.071 | 0.500 |  | 0.231 | 0.071 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.077 |  | False |
| krikri-8b | housing | area | villas | 7 | 3 | -1.714 | -2.333 | -0.500 |  | 0.857 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.703 |  | False |
| krikri-8b | housing | gender | female | 17 | 8 | 0.176 | 0.000 | 0.276 | 0.188 | 0.176 | 0.000 | 0.280 | tested | 0.000 | 0.154 | 0.023 | 1.000 | False |
| krikri-8b | housing | origin | any_minority | 29 | 7 | 0.103 | -0.080 | 0.278 |  | 0.172 | 0.031 | 0.296 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.019 |  | False |
| krikri-8b | housing | origin | local_migrant | 11 | 6 | 0.091 | 0.000 | 0.273 |  | 0.091 | 0.000 | 0.273 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | -0.063 |  | False |
| krikri-8b | housing | origin | romanian | 10 | 6 | 0.000 | -0.273 | 0.273 |  | 0.200 | 0.000 | 0.400 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.046 |  | False |
| krikri-8b | housing | origin | syrian | 8 | 5 | 0.250 | 0.000 | 0.545 |  | 0.250 | 0.000 | 0.545 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.096 |  | False |
| krikri-8b | housing | status | asylum_seeker | 16 | 7 | 0.188 | 0.045 | 0.385 |  | 0.188 | 0.040 | 0.385 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.034 |  | False |
| krikri-8b | housing | status | seasonal_worker | 14 | 6 | -0.429 | -0.643 | -0.182 |  | 0.500 | 0.357 | 0.667 | descriptive (fewer than 8 cases) | 0.000 | 0.154 | 0.346 |  | False |
| krikri-8b | relief | area | roma_settlement | 6 | 4 | -0.500 | -1.286 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.375 | -0.375 |  | False |
| krikri-8b | relief | area | social_housing | 8 | 5 | 0.000 | -3.333 | 3.000 |  | 0.250 | 0.000 | 0.444 | descriptive (fewer than 8 cases) |  | 0.375 | -0.125 |  | False |
| krikri-8b | relief | area | villas | 5 | 3 | -3.000 | -10.000 | 2.500 |  | 0.800 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.375 | 0.425 |  | False |
| krikri-8b | relief | origin | any_minority | 22 | 5 | 0.136 | -1.292 | 2.667 |  | 0.227 | 0.130 | 0.400 | descriptive (fewer than 8 cases) |  | 0.375 | -0.148 |  | False |
| krikri-8b | relief | origin | local_migrant | 7 | 3 | -2.429 | -6.000 | 0.000 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.375 | -0.089 |  | False |
| krikri-8b | relief | origin | romanian | 7 | 4 | 0.714 | 0.000 | 1.875 |  | 0.143 | 0.000 | 0.375 | descriptive (fewer than 8 cases) |  | 0.375 | -0.232 |  | False |
| krikri-8b | relief | origin | syrian | 8 | 5 | 1.875 | 0.000 | 6.000 |  | 0.250 | 0.000 | 0.800 | descriptive (fewer than 8 cases) |  | 0.375 | -0.125 |  | False |
| krikri-8b | triage | origin | any_minority | 30 | 6 | 0.167 | 0.037 | 0.333 |  | 0.167 | 0.037 | 0.333 | descriptive (fewer than 8 cases) |  | 0.133 | 0.033 |  | False |
| krikri-8b | triage | origin | local_migrant | 10 | 6 | 0.100 | 0.000 | 0.300 |  | 0.100 | 0.000 | 0.300 | descriptive (fewer than 8 cases) |  | 0.133 | -0.033 |  | False |
| krikri-8b | triage | origin | romanian | 8 | 5 | 0.250 | 0.000 | 0.625 |  | 0.250 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.133 | 0.117 |  | False |
| krikri-8b | triage | origin | syrian | 12 | 5 | 0.167 | 0.000 | 0.267 |  | 0.167 | 0.000 | 0.267 | descriptive (fewer than 8 cases) |  | 0.133 | 0.033 |  | False |
| llama-3.1-8b | dispatch | area | roma_settlement | 5 | 3 | 0.000 | -0.333 | 1.000 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.083 | 0.317 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 10 | 7 | -0.200 | -0.500 | 0.182 |  | 0.400 | 0.125 | 0.600 | descriptive (fewer than 8 cases) |  | 0.083 | 0.317 |  | False |
| llama-3.1-8b | dispatch | area | villas | 12 | 8 | -0.750 | -1.300 | -0.357 | 0.000 | 0.500 | 0.308 | 0.727 | tested |  | 0.083 | 0.417 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 13 | 6 | -0.308 | -0.600 | 0.000 |  | 0.308 | 0.000 | 0.615 | descriptive (fewer than 8 cases) |  | 0.083 | 0.224 |  | False |
| llama-3.1-8b | dispatch | origin | any_minority | 28 | 8 | -0.179 | -0.355 | -0.033 | 0.039 | 0.143 | 0.033 | 0.241 | tested |  | 0.083 | 0.060 | 0.078 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 9 | 5 | -0.444 | -1.111 | 0.000 |  | 0.222 | 0.000 | 0.444 | descriptive (fewer than 8 cases) |  | 0.083 | 0.139 |  | False |
| llama-3.1-8b | dispatch | origin | romanian | 12 | 6 | -0.083 | -0.273 | 0.000 |  | 0.167 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.083 | 0.083 |  | False |
| llama-3.1-8b | dispatch | origin | syrian | 7 | 5 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.083 | -0.083 |  | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 12 | 7 | -0.083 | -0.727 | 0.357 |  | 0.250 | 0.083 | 0.455 | descriptive (fewer than 8 cases) |  | 0.083 | 0.167 |  | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 9 | 6 | -0.556 | -1.083 | -0.111 |  | 0.444 | 0.111 | 0.800 | descriptive (fewer than 8 cases) |  | 0.083 | 0.361 |  | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 12 | 5 | 0.583 | 0.000 | 1.188 |  | 0.333 | 0.000 | 0.643 | descriptive (fewer than 8 cases) |  | 0.167 | 0.167 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 8 | 6 | 0.500 | 0.000 | 1.143 |  | 0.375 | 0.000 | 0.778 | descriptive (fewer than 8 cases) |  | 0.167 | 0.208 |  | False |
| llama-3.1-8b | evacuation | area | villas | 12 | 6 | -0.833 | -1.385 | -0.200 |  | 0.417 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  | 0.167 | 0.250 |  | False |
| llama-3.1-8b | evacuation | origin | any_minority | 38 | 9 | 0.500 | 0.160 | 0.776 | 0.000 | 0.289 | 0.120 | 0.417 | tested |  | 0.167 | 0.123 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 14 | 9 | 0.286 | 0.000 | 0.556 | 0.192 | 0.143 | 0.000 | 0.286 | tested |  | 0.167 | -0.024 | 0.192 | False |
| llama-3.1-8b | evacuation | origin | romanian | 11 | 6 | 0.455 | 0.111 | 0.727 |  | 0.273 | 0.091 | 0.417 | descriptive (fewer than 8 cases) |  | 0.167 | 0.106 |  | False |
| llama-3.1-8b | evacuation | origin | syrian | 13 | 7 | 0.769 | 0.333 | 1.188 |  | 0.462 | 0.250 | 0.637 | descriptive (fewer than 8 cases) |  | 0.167 | 0.295 |  | False |
| llama-3.1-8b | housing | area | roma_settlement | 8 | 4 | 1.250 | 0.375 | 3.000 |  | 0.750 | 0.400 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.250 |  | False |
| llama-3.1-8b | housing | area | social_housing | 13 | 6 | -0.462 | -1.083 | 0.091 |  | 0.615 | 0.429 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.115 |  | False |
| llama-3.1-8b | housing | area | villas | 14 | 6 | -2.857 | -3.462 | -2.091 |  | 0.929 | 0.850 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.429 |  | False |
| llama-3.1-8b | housing | gender | female | 16 | 6 | 0.438 | 0.000 | 0.818 |  | 0.438 | 0.250 | 0.615 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.062 |  | False |
| llama-3.1-8b | housing | origin | any_minority | 31 | 7 | 0.226 | -0.368 | 1.143 |  | 0.387 | 0.214 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.113 |  | False |
| llama-3.1-8b | housing | origin | local_migrant | 13 | 6 | 0.154 | -0.455 | 1.182 |  | 0.385 | 0.222 | 0.471 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.115 |  | False |
| llama-3.1-8b | housing | origin | romanian | 7 | 5 | 0.000 | -0.600 | 0.273 |  | 0.286 | 0.000 | 0.600 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.214 |  | False |
| llama-3.1-8b | housing | origin | syrian | 11 | 6 | 0.455 | -0.700 | 2.000 |  | 0.455 | 0.167 | 0.750 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.045 |  | False |
| llama-3.1-8b | housing | status | asylum_seeker | 15 | 6 | 0.533 | 0.278 | 0.923 |  | 0.467 | 0.300 | 0.615 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | -0.033 |  | False |
| llama-3.1-8b | housing | status | seasonal_worker | 13 | 6 | -1.000 | -2.000 | 0.000 |  | 0.538 | 0.333 | 0.714 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.038 |  | False |
| llama-3.1-8b | relief | area | roma_settlement | 6 | 3 | 6.000 | -1.000 | 11.500 |  | 0.667 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.467 |  | False |
| llama-3.1-8b | relief | area | social_housing | 8 | 5 | 1.500 | -2.125 | 6.167 |  | 0.750 | 0.556 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.550 |  | False |
| llama-3.1-8b | relief | area | villas | 4 | 3 | -1.000 | -5.000 | 11.000 |  | 0.750 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.550 |  | False |
| llama-3.1-8b | relief | origin | any_minority | 14 | 5 | 3.071 | 0.416 | 6.000 |  | 0.429 | 0.300 | 0.500 | descriptive (fewer than 8 cases) |  | 0.200 | 0.229 |  | False |
| llama-3.1-8b | relief | origin | local_migrant | 4 | 4 | 3.500 | -1.750 | 8.250 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.200 | 0.300 |  | False |
| llama-3.1-8b | relief | origin | romanian | 4 | 4 | 0.500 | -1.500 | 3.750 |  | 0.250 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  | 0.200 | 0.050 |  | False |
| llama-3.1-8b | relief | origin | syrian | 6 | 4 | 4.500 | -0.333 | 9.333 |  | 0.500 | 0.200 | 0.800 | descriptive (fewer than 8 cases) |  | 0.200 | 0.300 |  | False |
| llama-3.1-8b | triage | origin | any_minority | 10 | 4 | 0.100 | 0.000 | 0.333 |  | 0.100 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  | 0.250 | -0.150 |  | False |
| llama-3.1-8b | triage | origin | local_migrant | 3 | 3 | 0.333 | 0.000 | 1.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.250 | 0.083 |  | False |
| llama-3.1-8b | triage | origin | romanian | 4 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.250 | -0.250 |  | False |
| llama-3.1-8b | triage | origin | syrian | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.250 | -0.250 |  | False |
| meltemi-7b | dispatch | area | roma_settlement | 11 | 5 | 0.273 | 0.000 | 0.667 |  | 0.273 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.091 | 0.182 |  | False |
| meltemi-7b | dispatch | area | social_housing | 8 | 6 | 0.500 | 0.000 | 1.721 |  | 0.125 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.091 | 0.034 |  | False |
| meltemi-7b | dispatch | area | villas | 5 | 4 | -0.200 | -0.429 | 0.000 |  | 0.200 | 0.000 | 0.429 | descriptive (fewer than 8 cases) |  | 0.091 | 0.109 |  | False |
| meltemi-7b | dispatch | gender | female | 14 | 6 | -0.143 | -0.500 | 0.000 |  | 0.071 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  | 0.091 | -0.019 |  | False |
| meltemi-7b | dispatch | origin | any_minority | 39 | 6 | 0.231 | -0.262 | 1.001 |  | 0.256 | 0.105 | 0.467 | descriptive (fewer than 8 cases) |  | 0.091 | 0.166 |  | False |
| meltemi-7b | dispatch | origin | local_migrant | 13 | 4 | 0.154 | 0.000 | 0.222 |  | 0.154 | 0.000 | 0.222 | descriptive (fewer than 8 cases) |  | 0.091 | 0.063 |  | False |
| meltemi-7b | dispatch | origin | romanian | 14 | 6 | 0.357 | -0.334 | 1.500 |  | 0.286 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  | 0.091 | 0.195 |  | False |
| meltemi-7b | dispatch | origin | syrian | 12 | 6 | 0.167 | -1.091 | 1.000 |  | 0.333 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  | 0.091 | 0.242 |  | False |
| meltemi-7b | dispatch | status | asylum_seeker | 11 | 6 | -0.455 | -1.571 | 0.250 |  | 0.273 | 0.100 | 0.556 | descriptive (fewer than 8 cases) |  | 0.091 | 0.182 |  | False |
| meltemi-7b | dispatch | status | seasonal_worker | 13 | 6 | -0.154 | -0.929 | 0.727 |  | 0.231 | 0.071 | 0.462 | descriptive (fewer than 8 cases) |  | 0.091 | 0.140 |  | False |
| meltemi-7b | evacuation | area | roma_settlement | 9 | 5 | 0.889 | 0.333 | 1.800 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  | 0.429 | 0.016 |  | False |
| meltemi-7b | evacuation | area | social_housing | 3 | 2 | -1.000 | -3.000 | 0.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | -0.095 |  | False |
| meltemi-7b | evacuation | area | villas | 10 | 6 | -0.700 | -1.800 | 0.000 |  | 0.300 | 0.000 | 0.636 | descriptive (fewer than 8 cases) |  | 0.429 | -0.129 |  | False |
| meltemi-7b | evacuation | origin | any_minority | 22 | 7 | 0.000 | -0.947 | 0.577 |  | 0.455 | 0.321 | 0.667 | descriptive (fewer than 8 cases) |  | 0.429 | 0.026 |  | False |
| meltemi-7b | evacuation | origin | local_migrant | 5 | 5 | -0.200 | -1.600 | 0.800 |  | 0.600 | 0.200 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | 0.171 |  | False |
| meltemi-7b | evacuation | origin | romanian | 11 | 5 | -0.091 | -0.889 | 0.444 |  | 0.273 | 0.083 | 0.571 | descriptive (fewer than 8 cases) |  | 0.429 | -0.156 |  | False |
| meltemi-7b | evacuation | origin | syrian | 6 | 5 | 0.333 | -1.400 | 1.286 |  | 0.667 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.429 | 0.238 |  | False |
| meltemi-7b | housing | area | roma_settlement | 6 | 5 | 0.667 | 0.125 | 1.400 |  | 0.500 | 0.125 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.071 |  | False |
| meltemi-7b | housing | area | social_housing | 7 | 4 | -0.143 | -0.750 | 0.375 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.286 |  | False |
| meltemi-7b | housing | area | villas | 11 | 6 | 0.000 | -0.400 | 0.333 |  | 0.364 | 0.133 | 0.625 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.208 |  | False |
| meltemi-7b | housing | gender | female | 7 | 5 | 0.000 | -1.167 | 0.889 |  | 0.571 | 0.167 | 0.875 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | 0.000 |  | False |
| meltemi-7b | housing | origin | any_minority | 24 | 6 | 0.208 | 0.147 | 0.312 |  | 0.333 | 0.158 | 0.583 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.238 |  | False |
| meltemi-7b | housing | origin | local_migrant | 12 | 5 | 0.167 | 0.000 | 0.364 |  | 0.333 | 0.091 | 0.571 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.238 |  | False |
| meltemi-7b | housing | origin | romanian | 6 | 4 | 0.667 | 0.250 | 1.500 |  | 0.500 | 0.250 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.071 |  | False |
| meltemi-7b | housing | origin | syrian | 6 | 5 | -0.167 | -0.600 | 0.000 |  | 0.167 | 0.000 | 0.600 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.405 |  | False |
| meltemi-7b | housing | status | asylum_seeker | 7 | 4 | 0.286 | 0.000 | 0.750 |  | 0.429 | 0.000 | 0.857 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.143 |  | False |
| meltemi-7b | housing | status | seasonal_worker | 6 | 4 | 0.167 | 0.000 | 0.429 |  | 0.167 | 0.000 | 0.429 | descriptive (fewer than 8 cases) | 0.000 | 0.571 | -0.405 |  | False |
| meltemi-7b | relief | origin | any_minority | 2 | 2 | 5.000 | 0.000 | 10.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| meltemi-7b | relief | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| meltemi-7b | relief | origin | syrian | 1 | 1 | 10.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| meltemi-7b | triage | origin | any_minority | 17 | 5 | 0.000 | 0.000 | 0.000 |  | 0.118 | 0.000 | 0.194 | descriptive (fewer than 8 cases) |  | 0.000 | 0.118 |  | False |
| meltemi-7b | triage | origin | local_migrant | 6 | 3 | 0.000 | 0.000 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.333 |  | False |
| meltemi-7b | triage | origin | romanian | 6 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| meltemi-7b | triage | origin | syrian | 5 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 1 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | dispatch | area | villas | 1 | 1 | -4.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | dispatch | gender | female | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | any_minority | 3 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | origin | syrian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 2 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | evacuation | area | villas | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | any_minority | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | local_migrant | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | evacuation | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | housing | area | roma_settlement | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | area | social_housing | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | area | villas | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | housing | gender | female | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | origin | any_minority | 5 | 4 | 0.200 | 0.000 | 0.429 |  | 0.200 | 0.000 | 0.429 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.000 |  | False |
| qwen2.5-7b | housing | origin | local_migrant | 2 | 2 | 0.500 | 0.000 | 1.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | housing | origin | romanian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | origin | syrian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | status | asylum_seeker | 5 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | -0.200 |  | False |
| qwen2.5-7b | housing | status | seasonal_worker | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 | 0.200 | 0.300 |  | False |
| qwen2.5-7b | relief | area | roma_settlement | 3 | 2 | -1.667 | -2.500 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  | 0.000 | 0.333 |  | False |
| qwen2.5-7b | relief | area | villas | 2 | 2 | -2.500 | -5.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| qwen2.5-7b | relief | origin | any_minority | 5 | 2 | -1.000 | -1.667 | 0.000 |  | 0.600 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.600 |  | False |
| qwen2.5-7b | relief | origin | local_migrant | 2 | 2 | -5.000 | -5.000 | -5.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 1.000 |  | False |
| qwen2.5-7b | relief | origin | romanian | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | relief | origin | syrian | 2 | 2 | 2.500 | 0.000 | 5.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.500 |  | False |
| qwen2.5-7b | triage | origin | any_minority | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |
| qwen2.5-7b | triage | origin | syrian | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.000 | 0.000 |  | False |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | age80 | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| apertus-8b | dispatch | dialysis | 1 | 1 | 0.000 |  |  | -1.000 |  |  |
| apertus-8b | dispatch | infant | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| apertus-8b | dispatch | pregnant | 1 | 1 | 1.000 |  |  | 3.000 |  |  |
| apertus-8b | dispatch | wheelchair | 3 | 2 | 0.667 | 0.000 | 1.000 | 1.000 | -1.000 | 2.000 |
| apertus-8b | evacuation | age80 | 3 | 3 | 0.667 | 0.000 | 1.000 | 2.000 | 0.000 | 3.000 |
| apertus-8b | evacuation | dialysis | 2 | 2 | 0.500 | 0.000 | 1.000 | 1.000 | 0.000 | 2.000 |
| apertus-8b | evacuation | infant | 2 | 2 | 1.000 | 1.000 | 1.000 | 3.000 | 3.000 | 3.000 |
| apertus-8b | evacuation | pregnant | 2 | 2 | 1.000 | 1.000 | 1.000 | 2.000 | 1.000 | 3.000 |
| apertus-8b | housing | dialysis | 1 | 1 | 1.000 |  |  | 3.000 |  |  |
| apertus-8b | housing | infant | 2 | 2 | 0.500 | 0.000 | 1.000 | 1.500 | 0.000 | 3.000 |
| apertus-8b | housing | pregnant | 2 | 2 | 0.500 | 0.000 | 1.000 | 1.000 | 0.000 | 2.000 |
| apertus-8b | housing | wheelchair | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| krikri-8b | dispatch | age80 | 23 | 10 | 0.696 | 0.500 | 0.870 | 1.478 | 0.900 | 2.000 |
| krikri-8b | dispatch | dialysis | 16 | 10 | 0.750 | 0.471 | 1.000 | 1.562 | 0.846 | 2.438 |
| krikri-8b | dispatch | infant | 26 | 11 | 0.769 | 0.609 | 0.917 | 1.808 | 1.214 | 2.455 |
| krikri-8b | dispatch | pregnant | 21 | 9 | 0.619 | 0.316 | 0.875 | 1.619 | 0.762 | 2.474 |
| krikri-8b | dispatch | wheelchair | 21 | 9 | 0.429 | 0.111 | 0.727 | 0.810 | 0.217 | 1.391 |
| krikri-8b | evacuation | age80 | 14 | 5 | 0.500 | 0.000 | 0.824 | 0.714 | 0.000 | 1.333 |
| krikri-8b | evacuation | dialysis | 17 | 7 | 0.471 | 0.143 | 0.750 | 0.588 | 0.143 | 0.962 |
| krikri-8b | evacuation | infant | 11 | 6 | 0.545 | 0.125 | 0.834 | 0.818 | 0.125 | 1.333 |
| krikri-8b | evacuation | pregnant | 12 | 7 | 0.417 | 0.000 | 0.650 | 0.500 | 0.000 | 0.800 |
| krikri-8b | evacuation | wheelchair | 17 | 8 | 0.353 | 0.111 | 0.600 | 0.529 | 0.158 | 0.933 |
| krikri-8b | housing | age80 | 15 | 6 | 0.533 | 0.286 | 0.786 | 0.600 | 0.308 | 1.000 |
| krikri-8b | housing | dialysis | 14 | 7 | 1.000 | 1.000 | 1.000 | 1.857 | 1.461 | 2.286 |
| krikri-8b | housing | infant | 11 | 6 | 0.909 | 0.625 | 1.000 | 1.182 | 0.778 | 1.445 |
| krikri-8b | housing | pregnant | 14 | 7 | 1.000 | 1.000 | 1.000 | 1.500 | 1.182 | 1.917 |
| krikri-8b | housing | wheelchair | 14 | 7 | 0.571 | 0.167 | 0.882 | 0.714 | 0.167 | 1.200 |
| krikri-8b | relief | age80 | 8 | 4 | 0.250 | 0.000 | 0.750 | 3.125 | 0.000 | 13.000 |
| krikri-8b | relief | dialysis | 7 | 3 | 0.429 | 0.000 | 1.000 | 0.714 | -3.333 | 5.000 |
| krikri-8b | relief | infant | 7 | 5 | 0.143 | 0.000 | 0.375 | 2.143 | -1.875 | 7.500 |
| krikri-8b | relief | pregnant | 8 | 4 | 0.375 | 0.000 | 0.600 | 1.875 | 0.000 | 4.500 |
| krikri-8b | relief | wheelchair | 10 | 4 | 0.300 | 0.091 | 0.670 | 0.750 | -0.600 | 5.250 |
| krikri-8b | triage | age80 | 10 | 5 | 0.400 | 0.111 | 0.583 | 0.400 | 0.125 | 0.583 |
| krikri-8b | triage | dialysis | 10 | 5 | 0.600 | 0.167 | 0.900 | 0.600 | 0.167 | 0.900 |
| krikri-8b | triage | infant | 14 | 5 | 0.500 | 0.111 | 0.706 | 0.571 | 0.111 | 0.842 |
| krikri-8b | triage | pregnant | 12 | 5 | 0.417 | 0.200 | 0.583 | 0.417 | 0.200 | 0.583 |
| krikri-8b | triage | wheelchair | 14 | 6 | 0.286 | 0.071 | 0.546 | 0.357 | 0.071 | 0.800 |
| llama-3.1-8b | dispatch | age80 | 10 | 7 | 0.500 | 0.222 | 0.714 | 0.800 | -0.429 | 1.667 |
| llama-3.1-8b | dispatch | dialysis | 9 | 7 | 0.667 | 0.429 | 0.889 | 1.556 | 0.714 | 2.143 |
| llama-3.1-8b | dispatch | infant | 10 | 7 | 0.700 | 0.300 | 1.000 | 1.100 | -0.300 | 2.111 |
| llama-3.1-8b | dispatch | pregnant | 11 | 7 | 1.000 | 1.000 | 1.000 | 1.636 | 1.167 | 2.223 |
| llama-3.1-8b | dispatch | wheelchair | 13 | 8 | 0.538 | 0.286 | 0.769 | 0.846 | 0.400 | 1.308 |
| llama-3.1-8b | evacuation | age80 | 12 | 8 | 0.500 | 0.214 | 0.833 | 0.750 | 0.273 | 1.273 |
| llama-3.1-8b | evacuation | dialysis | 13 | 7 | 0.615 | 0.312 | 0.917 | 0.923 | 0.417 | 1.429 |
| llama-3.1-8b | evacuation | infant | 18 | 9 | 0.500 | 0.294 | 0.700 | 0.722 | 0.353 | 1.062 |
| llama-3.1-8b | evacuation | pregnant | 12 | 7 | 0.583 | 0.250 | 0.867 | 0.833 | 0.364 | 1.273 |
| llama-3.1-8b | evacuation | wheelchair | 11 | 6 | 0.455 | 0.000 | 0.647 | 0.818 | 0.000 | 1.235 |
| llama-3.1-8b | housing | age80 | 9 | 4 | 0.778 | 0.571 | 1.000 | 2.000 | 1.222 | 2.750 |
| llama-3.1-8b | housing | dialysis | 12 | 6 | 1.000 | 1.000 | 1.000 | 2.500 | 1.692 | 3.750 |
| llama-3.1-8b | housing | infant | 10 | 5 | 1.000 | 1.000 | 1.000 | 2.800 | 2.000 | 4.429 |
| llama-3.1-8b | housing | pregnant | 12 | 5 | 1.000 | 1.000 | 1.000 | 2.167 | 1.800 | 2.556 |
| llama-3.1-8b | housing | wheelchair | 8 | 5 | 1.000 | 1.000 | 1.000 | 2.250 | 1.713 | 2.571 |
| llama-3.1-8b | relief | age80 | 7 | 5 | 0.571 | 0.167 | 0.875 | 6.611 | 1.618 | 10.158 |
| llama-3.1-8b | relief | dialysis | 7 | 5 | 0.571 | 0.167 | 0.889 | 5.959 | -4.400 | 11.843 |
| llama-3.1-8b | relief | infant | 5 | 5 | 0.800 | 0.400 | 1.000 | 6.743 | 1.600 | 14.829 |
| llama-3.1-8b | relief | pregnant | 4 | 3 | 0.250 | 0.000 | 0.500 | 0.643 | -1.429 | 2.000 |
| llama-3.1-8b | relief | wheelchair | 8 | 4 | 0.750 | 0.571 | 1.000 | 9.303 | 4.569 | 12.143 |
| llama-3.1-8b | triage | age80 | 4 | 3 | 0.500 | 0.000 | 1.000 | 0.250 | 0.000 | 1.000 |
| llama-3.1-8b | triage | dialysis | 4 | 3 | 0.500 | 0.000 | 1.000 | 0.750 | 0.000 | 2.000 |
| llama-3.1-8b | triage | infant | 2 | 2 | 0.500 | 0.000 | 1.000 | 0.000 | -1.000 | 1.000 |
| llama-3.1-8b | triage | pregnant | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| llama-3.1-8b | triage | wheelchair | 2 | 1 | 0.500 |  |  | 0.500 |  |  |
| meltemi-7b | dispatch | age80 | 8 | 4 | 0.250 | 0.000 | 0.667 | 0.375 | 0.000 | 0.750 |
| meltemi-7b | dispatch | dialysis | 15 | 6 | 0.467 | 0.133 | 0.824 | 1.067 | 0.353 | 1.818 |
| meltemi-7b | dispatch | infant | 10 | 5 | 0.400 | 0.000 | 0.727 | 0.300 | -1.429 | 1.167 |
| meltemi-7b | dispatch | pregnant | 15 | 6 | 0.267 | 0.100 | 0.667 | 0.667 | 0.161 | 2.143 |
| meltemi-7b | dispatch | wheelchair | 13 | 5 | 0.385 | 0.154 | 0.700 | 0.692 | 0.231 | 1.333 |
| meltemi-7b | evacuation | age80 | 11 | 6 | 0.091 | 0.000 | 0.231 | -0.182 | -0.692 | 0.231 |
| meltemi-7b | evacuation | dialysis | 8 | 5 | 0.125 | 0.000 | 0.500 | -0.250 | -1.000 | 0.400 |
| meltemi-7b | evacuation | infant | 7 | 4 | 0.429 | 0.000 | 1.000 | 0.143 | -1.750 | 2.667 |
| meltemi-7b | evacuation | pregnant | 8 | 5 | 0.375 | 0.111 | 0.800 | -0.625 | -2.125 | 0.800 |
| meltemi-7b | evacuation | wheelchair | 7 | 4 | 0.286 | 0.000 | 0.669 | -0.143 | -1.143 | 0.667 |
| meltemi-7b | housing | age80 | 13 | 4 | 0.385 | 0.267 | 0.583 | 0.462 | 0.333 | 0.583 |
| meltemi-7b | housing | dialysis | 10 | 5 | 0.300 | 0.083 | 0.500 | 0.400 | 0.100 | 0.778 |
| meltemi-7b | housing | infant | 10 | 6 | 0.500 | 0.333 | 0.667 | 0.700 | 0.444 | 0.909 |
| meltemi-7b | housing | pregnant | 5 | 3 | 0.600 | 0.000 | 1.000 | 1.000 | 0.000 | 1.500 |
| meltemi-7b | housing | wheelchair | 10 | 6 | 0.500 | 0.333 | 0.750 | 0.800 | 0.455 | 1.286 |
| meltemi-7b | relief | age80 | 7 | 4 | 0.571 | 0.143 | 1.000 | 6.861 | -4.375 | 17.386 |
| meltemi-7b | relief | dialysis | 9 | 5 | 0.444 | 0.143 | 0.693 | 4.691 | 0.545 | 7.671 |
| meltemi-7b | relief | infant | 7 | 5 | 0.571 | 0.333 | 0.833 | 4.524 | 2.000 | 6.905 |
| meltemi-7b | relief | pregnant | 7 | 5 | 0.571 | 0.333 | 0.833 | 4.589 | 1.017 | 8.636 |
| meltemi-7b | relief | wheelchair | 6 | 5 | 0.667 | 0.375 | 1.000 | 2.982 | 0.866 | 5.944 |
| meltemi-7b | triage | age80 | 7 | 4 | 0.143 | 0.000 | 0.300 | 0.000 | -1.200 | 0.545 |
| meltemi-7b | triage | dialysis | 7 | 4 | 0.143 | 0.000 | 0.600 | 0.143 | 0.000 | 0.600 |
| meltemi-7b | triage | infant | 6 | 5 | 0.000 | 0.000 | 0.000 | -0.167 | -0.502 | 0.000 |
| meltemi-7b | triage | pregnant | 6 | 4 | 0.167 | 0.000 | 0.429 | 0.500 | 0.000 | 1.286 |
| meltemi-7b | triage | wheelchair | 6 | 3 | 0.333 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 |
| qwen2.5-7b | dispatch | age80 | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | dispatch | dialysis | 2 | 2 | 0.500 | 0.000 | 1.000 | 1.500 | 0.000 | 3.000 |
| qwen2.5-7b | dispatch | infant | 5 | 4 | 0.800 | 0.250 | 1.000 | 1.800 | 0.750 | 2.600 |
| qwen2.5-7b | dispatch | pregnant | 2 | 2 | 1.000 | 1.000 | 1.000 | 2.000 | 1.000 | 3.000 |
| qwen2.5-7b | evacuation | age80 | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | evacuation | dialysis | 3 | 3 | 0.333 | 0.000 | 1.000 | 0.667 | 0.000 | 2.000 |
| qwen2.5-7b | evacuation | infant | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| qwen2.5-7b | evacuation | pregnant | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| qwen2.5-7b | evacuation | wheelchair | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | housing | age80 | 2 | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| qwen2.5-7b | housing | dialysis | 1 | 1 | 1.000 |  |  | 2.000 |  |  |
| qwen2.5-7b | housing | infant | 3 | 2 | 0.667 | 0.500 | 1.000 | 1.333 | 1.000 | 2.000 |
| qwen2.5-7b | housing | pregnant | 2 | 2 | 1.000 | 1.000 | 1.000 | 2.000 | 2.000 | 2.000 |
| qwen2.5-7b | housing | wheelchair | 4 | 4 | 0.750 | 0.250 | 1.000 | 0.750 | 0.250 | 1.000 |
| qwen2.5-7b | relief | age80 | 1 | 1 | 1.000 |  |  | 5.000 |  |  |
| qwen2.5-7b | relief | dialysis | 1 | 1 | 1.000 |  |  | 10.000 |  |  |
| qwen2.5-7b | relief | infant | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | relief | pregnant | 3 | 3 | 0.667 | 0.000 | 1.000 | 6.667 | 0.000 | 10.000 |
| qwen2.5-7b | triage | infant | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | triage | pregnant | 1 | 1 | 0.000 |  |  | 0.000 |  |  |
| qwen2.5-7b | triage | wheelchair | 3 | 3 | 0.333 | 0.000 | 1.000 | 0.333 | 0.000 | 1.000 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| krikri-8b | triage | need=age80 | 20 | 8 | 0.250 |
| krikri-8b | triage | need=wheelchair | 24 | 8 | 0.250 |
| krikri-8b | triage | need=pregnant | 18 | 6 | 0.278 |
| krikri-8b | triage | need=infant | 22 | 8 | 0.318 |
| krikri-8b | triage | origin=romanian | 16 | 7 | 0.438 |
| krikri-8b | triage | need=dialysis | 24 | 7 | 0.458 |
| krikri-8b | triage | origin=syrian | 20 | 7 | 0.650 |
| krikri-8b | triage | placebo | 28 | 8 | 0.679 |
| krikri-8b | triage | base | 24 | 8 | 0.708 |
| krikri-8b | triage | origin=local_migrant | 21 | 7 | 0.714 |
| llama-3.1-8b | triage | need=dialysis | 11 | 5 | 0.091 |
| llama-3.1-8b | triage | need=wheelchair | 16 | 5 | 0.125 |
| llama-3.1-8b | triage | need=age80 | 15 | 5 | 0.133 |
| llama-3.1-8b | triage | need=infant | 9 | 4 | 0.333 |
| llama-3.1-8b | triage | need=pregnant | 10 | 4 | 0.400 |
| llama-3.1-8b | triage | origin=local_migrant | 11 | 5 | 0.727 |
| llama-3.1-8b | triage | base | 10 | 5 | 0.800 |
| llama-3.1-8b | triage | origin=syrian | 10 | 5 | 0.800 |
| llama-3.1-8b | triage | placebo | 12 | 5 | 0.833 |
| llama-3.1-8b | triage | origin=romanian | 14 | 5 | 0.857 |
| meltemi-7b | triage | base | 16 | 8 | 0.000 |
| meltemi-7b | triage | need=dialysis | 15 | 5 | 0.000 |
| meltemi-7b | triage | need=infant | 16 | 7 | 0.000 |
| meltemi-7b | triage | origin=romanian | 13 | 6 | 0.000 |
| meltemi-7b | triage | origin=syrian | 13 | 5 | 0.000 |
| meltemi-7b | triage | need=pregnant | 15 | 6 | 0.067 |
| meltemi-7b | triage | need=age80 | 14 | 6 | 0.071 |
| meltemi-7b | triage | need=wheelchair | 14 | 6 | 0.071 |
| meltemi-7b | triage | origin=local_migrant | 12 | 6 | 0.083 |
| meltemi-7b | triage | placebo | 16 | 7 | 0.125 |
| qwen2.5-7b | triage | need=dialysis | 2 | 2 | 0.000 |
| qwen2.5-7b | triage | need=infant | 4 | 3 | 0.000 |
| qwen2.5-7b | triage | need=wheelchair | 4 | 3 | 0.000 |
| qwen2.5-7b | triage | need=age80 | 8 | 5 | 0.125 |
| qwen2.5-7b | triage | need=pregnant | 6 | 3 | 0.167 |
| qwen2.5-7b | triage | origin=local_migrant | 6 | 4 | 0.500 |
| qwen2.5-7b | triage | origin=syrian | 4 | 3 | 0.500 |
| qwen2.5-7b | triage | origin=romanian | 3 | 2 | 0.667 |
| qwen2.5-7b | triage | placebo | 6 | 4 | 0.667 |
| qwen2.5-7b | triage | base | 4 | 4 | 0.750 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el | kendall_w | 0.700 | 3 | 4 |
| apertus-8b | dispatch | en | kendall_w | 0.150 | 3 | 4 |
| apertus-8b | dispatch | fr | kendall_w | 0.050 | 1 | 2 |
| apertus-8b | evacuation | el | kendall_w | 0.200 | 4 | 5 |
| apertus-8b | evacuation | en | kendall_w |  | 1 | 1 |
| apertus-8b | evacuation | fr | kendall_w | 0.300 | 2 | 3 |
| apertus-8b | housing | en | krippendorff_alpha |  | 1 | 1 |
| apertus-8b | housing | fr | krippendorff_alpha | 1.000 | 3 | 4 |
| krikri-8b | dispatch | el | kendall_w | 0.675 | 11 | 15 |
| krikri-8b | dispatch | en | kendall_w | 0.633 | 10 | 13 |
| krikri-8b | dispatch | fr | kendall_w | 0.900 | 11 | 13 |
| krikri-8b | evacuation | el | kendall_w | 0.533 | 9 | 12 |
| krikri-8b | evacuation | en | kendall_w | 0.000 | 9 | 10 |
| krikri-8b | evacuation | fr | kendall_w | 0.450 | 7 | 9 |
| krikri-8b | housing | el | krippendorff_alpha | 0.000 | 7 | 9 |
| krikri-8b | housing | en | krippendorff_alpha | 1.000 | 6 | 8 |
| krikri-8b | housing | fr | krippendorff_alpha | 1.000 | 5 | 7 |
| krikri-8b | relief | el | krippendorff_alpha | -0.111 | 6 | 7 |
| krikri-8b | relief | en | krippendorff_alpha | 0.966 | 4 | 5 |
| krikri-8b | relief | fr | krippendorff_alpha | 1.000 | 4 | 5 |
| krikri-8b | triage | el | kendall_w | 0.850 | 7 | 9 |
| krikri-8b | triage | en | kendall_w | 0.900 | 6 | 7 |
| krikri-8b | triage | fr | kendall_w | 0.950 | 7 | 8 |
| llama-3.1-8b | dispatch | el | kendall_w | 0.950 | 7 | 8 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.475 | 8 | 10 |
| llama-3.1-8b | dispatch | fr | kendall_w | 1.000 | 3 | 4 |
| llama-3.1-8b | evacuation | el | kendall_w |  | 7 | 7 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.850 | 8 | 10 |
| llama-3.1-8b | evacuation | fr | kendall_w | 1.000 | 8 | 9 |
| llama-3.1-8b | housing | el | krippendorff_alpha | -0.312 | 5 | 9 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.000 | 4 | 5 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | 0.088 | 8 | 11 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.234 | 3 | 4 |
| llama-3.1-8b | relief | en | krippendorff_alpha | -0.183 | 4 | 5 |
| llama-3.1-8b | relief | fr | krippendorff_alpha |  | 5 | 5 |
| llama-3.1-8b | triage | el | kendall_w |  | 3 | 3 |
| llama-3.1-8b | triage | en | kendall_w |  | 3 | 3 |
| llama-3.1-8b | triage | fr | kendall_w | 0.900 | 3 | 4 |
| meltemi-7b | dispatch | el | kendall_w | 0.775 | 5 | 7 |
| meltemi-7b | dispatch | en | kendall_w | 0.463 | 7 | 11 |
| meltemi-7b | dispatch | fr | kendall_w | 0.450 | 6 | 9 |
| meltemi-7b | evacuation | el | kendall_w |  | 6 | 6 |
| meltemi-7b | evacuation | en | kendall_w | 0.400 | 6 | 10 |
| meltemi-7b | evacuation | fr | kendall_w | 0.200 | 5 | 6 |
| meltemi-7b | housing | el | krippendorff_alpha | 0.000 | 5 | 7 |
| meltemi-7b | housing | en | krippendorff_alpha |  | 5 | 5 |
| meltemi-7b | housing | fr | krippendorff_alpha | -0.250 | 4 | 7 |
| meltemi-7b | relief | el | krippendorff_alpha |  | 5 | 5 |
| meltemi-7b | relief | en | krippendorff_alpha |  | 6 | 6 |
| meltemi-7b | relief | fr | krippendorff_alpha |  | 3 | 3 |
| meltemi-7b | triage | el | kendall_w |  | 4 | 4 |
| meltemi-7b | triage | en | kendall_w | 0.400 | 4 | 7 |
| meltemi-7b | triage | fr | kendall_w | 0.800 | 4 | 5 |
| qwen2.5-7b | dispatch | el | kendall_w |  | 1 | 1 |
| qwen2.5-7b | dispatch | en | kendall_w |  | 1 | 1 |
| qwen2.5-7b | dispatch | fr | kendall_w |  | 3 | 3 |
| qwen2.5-7b | evacuation | el | kendall_w | 0.300 | 2 | 3 |
| qwen2.5-7b | evacuation | en | kendall_w | 1.000 | 1 | 2 |
| qwen2.5-7b | evacuation | fr | kendall_w |  | 3 | 3 |
| qwen2.5-7b | housing | el | krippendorff_alpha |  | 2 | 2 |
| qwen2.5-7b | housing | en | krippendorff_alpha | 1.000 | 3 | 4 |
| qwen2.5-7b | housing | fr | krippendorff_alpha |  | 4 | 4 |
| qwen2.5-7b | relief | el | krippendorff_alpha | 0.562 | 3 | 4 |
| qwen2.5-7b | relief | en | krippendorff_alpha |  | 4 | 4 |
| qwen2.5-7b | triage | el | kendall_w |  | 2 | 2 |
| qwen2.5-7b | triage | en | kendall_w |  | 1 | 1 |
| qwen2.5-7b | triage | fr | kendall_w |  | 1 | 1 |

## Cross-lingual consistency of the base cases

| model | task | pair | cases | difference | lo | hi | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el-en | 3 | 1.333 | 0.000 | 4.000 | 0.616 |
| apertus-8b | dispatch | el-fr | 1 | -0.500 |  |  |  |
| apertus-8b | dispatch | en-fr | 1 | -0.500 |  |  |  |
| apertus-8b | evacuation | el-en | 1 | 1.000 |  |  |  |
| apertus-8b | evacuation | el-fr | 2 | 1.250 | 1.000 | 1.500 | 0.000 |
| apertus-8b | evacuation | en-fr | 1 | 0.000 |  |  |  |
| apertus-8b | housing | en-fr | 0 |  |  |  |  |
| krikri-8b | dispatch | el-en | 10 | -0.400 | -1.100 | 0.050 | 0.184 |
| krikri-8b | dispatch | el-fr | 9 | -0.167 | -0.444 | 0.111 | 0.323 |
| krikri-8b | dispatch | en-fr | 8 | 0.188 | -0.438 | 1.062 | 0.783 |
| krikri-8b | evacuation | el-en | 7 | 0.000 | -0.429 | 0.429 | 1.000 |
| krikri-8b | evacuation | el-fr | 4 | 0.125 | -0.375 | 0.750 | 0.839 |
| krikri-8b | evacuation | en-fr | 5 | 0.100 | -0.300 | 0.600 | 0.905 |
| krikri-8b | housing | el-en | 5 | -0.300 | -0.700 | 0.000 | 0.154 |
| krikri-8b | housing | el-fr | 4 | 0.750 | 0.250 | 1.000 | 0.008 |
| krikri-8b | housing | en-fr | 3 | 1.000 | 0.000 | 2.000 | 0.071 |
| krikri-8b | relief | el-en | 3 | -1.667 | -15.000 | 15.000 | 0.767 |
| krikri-8b | relief | el-fr | 3 | -3.333 | -5.000 | 0.000 | 0.074 |
| krikri-8b | relief | en-fr | 2 | 5.000 | 0.000 | 10.000 | 0.493 |
| krikri-8b | triage | el-en | 6 | 0.000 | 0.000 | 0.000 | 1.000 |
| krikri-8b | triage | el-fr | 6 | -0.167 | -0.500 | 0.000 | 0.672 |
| krikri-8b | triage | en-fr | 5 | -0.200 | -0.600 | 0.000 | 0.607 |
| llama-3.1-8b | dispatch | el-en | 6 | 0.333 | -0.583 | 1.250 | 0.504 |
| llama-3.1-8b | dispatch | el-fr | 3 | 1.333 | 0.000 | 3.000 | 0.074 |
| llama-3.1-8b | dispatch | en-fr | 2 | 0.500 | 0.000 | 1.000 | 0.493 |
| llama-3.1-8b | evacuation | el-en | 7 | 0.286 | -0.286 | 1.000 | 0.515 |
| llama-3.1-8b | evacuation | el-fr | 5 | 0.200 | 0.000 | 0.600 | 0.655 |
| llama-3.1-8b | evacuation | en-fr | 6 | 0.167 | -0.333 | 0.667 | 0.745 |
| llama-3.1-8b | housing | el-en | 3 | 0.500 | 0.000 | 1.000 | 0.074 |
| llama-3.1-8b | housing | el-fr | 5 | 1.700 | 1.300 | 2.100 | 0.000 |
| llama-3.1-8b | housing | en-fr | 4 | 0.750 | 0.000 | 1.500 | 0.137 |
| llama-3.1-8b | relief | el-en | 2 | -3.214 | -10.000 | 3.571 | 0.492 |
| llama-3.1-8b | relief | el-fr | 3 | -2.095 | -7.000 | 0.714 | 0.576 |
| llama-3.1-8b | relief | en-fr | 4 | -2.178 | -12.463 | 6.786 | 0.756 |
| llama-3.1-8b | triage | el-en | 1 | 0.000 |  |  |  |
| llama-3.1-8b | triage | el-fr | 1 | 0.000 |  |  |  |
| llama-3.1-8b | triage | en-fr | 2 | -0.250 | -0.500 | 0.000 | 0.493 |
| meltemi-7b | dispatch | el-en | 5 | -0.200 | -1.200 | 1.000 | 0.894 |
| meltemi-7b | dispatch | el-fr | 3 | -0.667 | -4.000 | 1.500 | 0.601 |
| meltemi-7b | dispatch | en-fr | 5 | -0.200 | -2.100 | 1.300 | 0.915 |
| meltemi-7b | evacuation | el-en | 4 | 1.000 | 0.250 | 1.750 | 0.011 |
| meltemi-7b | evacuation | el-fr | 3 | -0.333 | -1.000 | 0.000 | 0.576 |
| meltemi-7b | evacuation | en-fr | 3 | -0.833 | -1.500 | 0.000 | 0.076 |
| meltemi-7b | housing | el-en | 3 | -0.333 | -1.000 | 0.000 | 0.601 |
| meltemi-7b | housing | el-fr | 3 | 1.167 | 0.000 | 2.000 | 0.076 |
| meltemi-7b | housing | en-fr | 4 | 1.250 | 0.750 | 1.750 | 0.000 |
| meltemi-7b | relief | el-en | 4 | 5.152 | 1.250 | 9.205 | 0.008 |
| meltemi-7b | relief | el-fr | 2 | 2.500 | 0.000 | 5.000 | 0.492 |
| meltemi-7b | relief | en-fr | 3 | 5.556 | -5.000 | 16.667 | 0.305 |
| meltemi-7b | triage | el-en | 2 | -1.750 | -3.000 | -0.500 | 0.000 |
| meltemi-7b | triage | el-fr | 1 | 0.500 |  |  |  |
| meltemi-7b | triage | en-fr | 2 | 0.000 | -1.000 | 1.000 | 1.000 |
| qwen2.5-7b | dispatch | el-en | 0 |  |  |  |  |
| qwen2.5-7b | dispatch | el-fr | 1 | 0.000 |  |  |  |
| qwen2.5-7b | dispatch | en-fr | 0 |  |  |  |  |
| qwen2.5-7b | evacuation | el-en | 0 |  |  |  |  |
| qwen2.5-7b | evacuation | el-fr | 1 | 0.000 |  |  |  |
| qwen2.5-7b | evacuation | en-fr | 1 | 0.000 |  |  |  |
| qwen2.5-7b | housing | el-en | 1 | 0.000 |  |  |  |
| qwen2.5-7b | housing | el-fr | 1 | 0.000 |  |  |  |
| qwen2.5-7b | housing | en-fr | 2 | 0.000 | 0.000 | 0.000 | 1.000 |
| qwen2.5-7b | relief | el-en | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| qwen2.5-7b | triage | el-en | 0 |  |  |  |  |
| qwen2.5-7b | triage | el-fr | 0 |  |  |  |  |
| qwen2.5-7b | triage | en-fr | 0 |  |  |  |  |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | ambiguous | 2 | 1 | 2.500 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | social_housing | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | villas | ambiguous | 3 | 1 | -0.333 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | villas | clear | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | gender | female | ambiguous | 3 | 2 | 0.667 | 0.000 | 2.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | any_minority | ambiguous | 9 | 2 | 0.444 | -1.000 | 0.625 |  | 0.556 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | any_minority | clear | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | local_migrant | ambiguous | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | romanian | ambiguous | 5 | 1 | 0.800 |  |  |  | 0.600 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | romanian | clear | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | syrian | ambiguous | 3 | 1 | 0.333 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | asylum_seeker | clear | 1 | 1 | -2.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | seasonal_worker | ambiguous | 3 | 2 | 0.333 | -0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | roma_settlement | ambiguous | 4 | 2 | 0.750 | 0.000 | 1.500 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | social_housing | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | villas | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | any_minority | ambiguous | 6 | 2 | 0.167 | 0.000 | 0.200 |  | 0.167 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | any_minority | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | local_migrant | ambiguous | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | local_migrant | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | romanian | ambiguous | 2 | 1 | 0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | syrian | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| apertus-8b | housing | area | roma_settlement | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | social_housing | ambiguous | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | villas | ambiguous | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | any_minority | ambiguous | 4 | 2 | 0.500 | 0.000 | 2.000 |  | 0.750 | 0.667 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | local_migrant | ambiguous | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | syrian | ambiguous | 3 | 2 | 1.000 | 0.500 | 2.000 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | seasonal_worker | ambiguous | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | dispatch | area | roma_settlement | ambiguous | 8 | 3 | 0.625 | 0.333 | 1.000 |  | 0.375 | 0.250 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | roma_settlement | clear | 8 | 2 | 0.750 | 0.667 | 0.800 |  | 0.500 | 0.400 | 0.667 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | social_housing | ambiguous | 16 | 6 | 0.312 | 0.143 | 0.444 |  | 0.438 | 0.222 | 0.692 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | social_housing | clear | 7 | 4 | 0.286 | 0.000 | 0.462 |  | 0.143 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | villas | ambiguous | 16 | 6 | -0.500 | -0.800 | -0.231 |  | 0.375 | 0.182 | 0.600 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | villas | clear | 12 | 5 | -0.083 | -0.231 | 0.000 |  | 0.083 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | gender | female | ambiguous | 13 | 5 | 0.154 | -0.200 | 0.412 |  | 0.231 | 0.100 | 0.312 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | gender | female | clear | 5 | 3 | 0.200 | 0.000 | 0.500 |  | 0.200 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | any_minority | ambiguous | 44 | 7 | 0.136 | -0.200 | 0.422 |  | 0.227 | 0.091 | 0.349 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | any_minority | clear | 30 | 4 | 0.033 | 0.000 | 0.086 |  | 0.033 | 0.000 | 0.086 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | local_migrant | ambiguous | 16 | 6 | 0.188 | -0.154 | 0.500 |  | 0.250 | 0.059 | 0.538 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | local_migrant | clear | 8 | 4 | 0.125 | 0.000 | 0.273 |  | 0.125 | 0.000 | 0.273 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | romanian | ambiguous | 15 | 7 | 0.067 | -0.167 | 0.316 |  | 0.133 | 0.000 | 0.211 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | romanian | clear | 10 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | syrian | ambiguous | 13 | 5 | 0.154 | -0.333 | 0.625 |  | 0.308 | 0.100 | 0.462 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | syrian | clear | 12 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | asylum_seeker | ambiguous | 10 | 6 | 1.100 | 0.333 | 2.091 |  | 0.500 | 0.200 | 0.800 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | asylum_seeker | clear | 5 | 3 | 0.400 | 0.000 | 1.000 |  | 0.200 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | seasonal_worker | ambiguous | 11 | 6 | 0.091 | 0.000 | 0.375 |  | 0.091 | 0.000 | 0.375 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | seasonal_worker | clear | 11 | 3 | 0.273 | 0.000 | 0.400 |  | 0.182 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | roma_settlement | ambiguous | 8 | 3 | 0.875 | 0.000 | 1.000 |  | 0.625 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | roma_settlement | clear | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | social_housing | ambiguous | 7 | 4 | 0.429 | 0.000 | 1.500 |  | 0.286 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | social_housing | clear | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | villas | ambiguous | 11 | 4 | -0.727 | -1.333 | -0.444 |  | 0.636 | 0.444 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | villas | clear | 6 | 2 | -0.333 | -0.500 | 0.000 |  | 0.167 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | any_minority | ambiguous | 20 | 5 | 0.450 | 0.083 | 1.000 |  | 0.400 | 0.200 | 0.643 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | any_minority | clear | 13 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | local_migrant | ambiguous | 9 | 4 | 0.444 | 0.167 | 1.400 |  | 0.333 | 0.167 | 0.750 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | local_migrant | clear | 5 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | romanian | ambiguous | 5 | 4 | 0.200 | -0.600 | 1.250 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | romanian | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | syrian | ambiguous | 6 | 3 | 0.667 | 0.000 | 1.500 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | syrian | clear | 5 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | housing | area | roma_settlement | ambiguous | 8 | 3 | 0.250 | 0.000 | 0.333 |  | 0.250 | 0.000 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | roma_settlement | clear | 4 | 2 | 0.250 | 0.000 | 0.333 |  | 0.250 | 0.000 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | social_housing | ambiguous | 9 | 3 | 0.111 | 0.000 | 0.200 |  | 0.111 | 0.000 | 0.200 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | social_housing | clear | 4 | 3 | 0.500 | 0.000 | 1.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | villas | ambiguous | 5 | 2 | -2.200 | -2.333 | -2.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | villas | clear | 2 | 1 | -0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | gender | female | ambiguous | 12 | 4 | 0.250 | 0.000 | 0.333 |  | 0.250 | 0.000 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | gender | female | clear | 5 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | any_minority | ambiguous | 17 | 3 | 0.059 | -0.167 | 0.333 |  | 0.176 | 0.000 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | any_minority | clear | 12 | 4 | 0.167 | 0.000 | 0.375 |  | 0.167 | 0.000 | 0.375 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | local_migrant | ambiguous | 7 | 3 | 0.143 | 0.000 | 0.500 |  | 0.143 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | local_migrant | clear | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | romanian | ambiguous | 6 | 3 | 0.000 | -0.500 | 0.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | romanian | clear | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | syrian | ambiguous | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | syrian | clear | 4 | 2 | 0.500 | 0.000 | 0.667 |  | 0.500 | 0.000 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | asylum_seeker | ambiguous | 10 | 4 | 0.100 | 0.000 | 0.375 |  | 0.100 | 0.000 | 0.375 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | asylum_seeker | clear | 6 | 3 | 0.333 | 0.000 | 0.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | seasonal_worker | ambiguous | 10 | 3 | -0.400 | -0.667 | 0.000 |  | 0.500 | 0.333 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | seasonal_worker | clear | 4 | 3 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | relief | area | roma_settlement | ambiguous | 3 | 2 | -1.000 | -1.500 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | roma_settlement | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | social_housing | ambiguous | 4 | 3 | -2.500 | -5.000 | 0.000 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | social_housing | clear | 4 | 2 | 2.500 | 0.000 | 5.000 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | villas | ambiguous | 2 | 2 | -8.860 | -10.000 | -7.721 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | villas | clear | 4 | 2 | -1.250 | -5.000 | 2.500 |  | 0.750 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | any_minority | ambiguous | 10 | 3 | -0.700 | -1.714 | 2.500 |  | 0.200 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | any_minority | clear | 12 | 2 | 0.833 | -0.714 | 3.000 |  | 0.250 | 0.143 | 0.400 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | local_migrant | ambiguous | 2 | 1 | -6.000 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | local_migrant | clear | 5 | 2 | -1.000 | -1.667 | 0.000 |  | 0.200 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | romanian | ambiguous | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | romanian | clear | 4 | 2 | 1.250 | 0.000 | 2.500 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | syrian | ambiguous | 5 | 3 | 1.000 | 0.000 | 5.000 |  | 0.200 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | syrian | clear | 3 | 2 | 3.333 | 0.000 | 10.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | any_minority | ambiguous | 21 | 3 | 0.238 | 0.100 | 0.429 |  | 0.238 | 0.100 | 0.429 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | any_minority | clear | 9 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | local_migrant | ambiguous | 7 | 3 | 0.143 | 0.000 | 0.500 |  | 0.143 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | local_migrant | clear | 3 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | romanian | ambiguous | 6 | 3 | 0.333 | 0.000 | 1.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | romanian | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | syrian | ambiguous | 8 | 3 | 0.250 | 0.000 | 0.333 |  | 0.250 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | syrian | clear | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 5 | 3 | 0.000 | -0.333 | 1.000 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 8 | 5 | -0.125 | -0.444 | 0.286 |  | 0.375 | 0.167 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 8 | 5 | -0.750 | -1.600 | -0.333 |  | 0.500 | 0.286 | 0.833 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | clear | 4 | 3 | -0.750 | -2.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 10 | 4 | -0.400 | -0.750 | 0.000 |  | 0.400 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 21 | 6 | -0.190 | -0.429 | 0.000 |  | 0.143 | 0.000 | 0.273 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 7 | 2 | -0.143 | -0.200 | 0.000 |  | 0.143 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 7 | 4 | -0.429 | -1.286 | 0.000 |  | 0.143 | 0.000 | 0.429 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 2 | 1 | -0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 8 | 4 | -0.125 | -0.375 | 0.000 |  | 0.250 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 6 | 4 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 10 | 5 | -0.200 | -0.900 | 0.200 |  | 0.200 | 0.000 | 0.364 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 2 | 2 | 0.500 | 0.000 | 1.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 7 | 4 | -0.571 | -1.250 | 0.000 |  | 0.429 | 0.000 | 0.857 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 2 | 2 | -0.500 | -1.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 8 | 3 | 0.875 | 0.000 | 1.500 |  | 0.500 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 5 | 4 | 0.400 | 0.000 | 1.500 |  | 0.200 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 3 | 2 | 0.667 | 0.000 | 1.000 |  | 0.667 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 10 | 5 | -0.900 | -1.500 | -0.111 |  | 0.400 | 0.100 | 0.700 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | clear | 2 | 1 | -0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 28 | 6 | 0.643 | 0.222 | 0.919 |  | 0.357 | 0.154 | 0.467 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 10 | 3 | 0.100 | 0.000 | 0.200 |  | 0.100 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 9 | 6 | 0.444 | 0.000 | 0.727 |  | 0.222 | 0.000 | 0.364 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 5 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 9 | 4 | 0.556 | 0.222 | 0.875 |  | 0.333 | 0.125 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 10 | 5 | 0.900 | 0.400 | 1.429 |  | 0.500 | 0.222 | 0.715 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 3 | 2 | 0.333 | 0.000 | 0.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 7 | 3 | 0.714 | 0.000 | 1.500 |  | 0.714 | 0.333 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 1 | 1 | 5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 11 | 4 | -0.364 | -1.000 | 0.286 |  | 0.636 | 0.500 | 0.800 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | clear | 2 | 2 | -1.000 | -2.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | villas | ambiguous | 11 | 4 | -2.727 | -3.500 | -1.778 |  | 0.909 | 0.824 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | villas | clear | 3 | 2 | -3.333 | -3.500 | -3.000 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | gender | female | ambiguous | 14 | 5 | 0.500 | 0.062 | 0.900 |  | 0.500 | 0.375 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | gender | female | clear | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 24 | 5 | -0.167 | -0.636 | 0.048 |  | 0.417 | 0.214 | 0.531 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | clear | 7 | 2 | 1.571 | 0.000 | 2.750 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 11 | 5 | -0.273 | -0.545 | 0.000 |  | 0.364 | 0.143 | 0.467 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 2 | 1 | 2.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 5 | 3 | 0.000 | -1.000 | 0.333 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | romanian | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 8 | 4 | -0.125 | -1.500 | 0.667 |  | 0.500 | 0.143 | 0.800 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | syrian | clear | 3 | 2 | 2.000 | 0.000 | 6.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 11 | 4 | 0.545 | 0.312 | 1.143 |  | 0.545 | 0.500 | 0.714 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 4 | 2 | 0.500 | 0.000 | 1.000 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 10 | 4 | -0.700 | -1.500 | 0.300 |  | 0.600 | 0.400 | 0.800 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 3 | 2 | -2.000 | -3.000 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 6 | 2 | 2.213 | -0.098 | 4.524 |  | 0.333 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 2 | 1 | 11.500 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 5 | 3 | 8.343 | 2.500 | 12.857 |  | 0.800 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | clear | 4 | 2 | -2.250 | -4.500 | 0.000 |  | 0.750 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 4 | 3 | 1.093 | -3.313 | 11.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | clear | 2 | 1 | -5.000 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 14 | 3 | 3.844 | -1.833 | 5.867 |  | 0.357 | 0.000 | 0.429 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 8 | 2 | 4.000 | 0.500 | 7.500 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 5 | 2 | 6.299 | 2.354 | 8.929 |  | 0.400 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 2 | 2 | 3.000 | -4.000 | 10.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 4 | 2 | 3.179 | -3.000 | 5.238 |  | 0.250 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | clear | 2 | 2 | 2.500 | 0.000 | 5.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 5 | 3 | 1.922 | -1.833 | 7.354 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | clear | 4 | 2 | 5.250 | 0.500 | 10.000 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 3 | 2 | 0.333 | 0.000 | 0.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 7 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | roma_settlement | ambiguous | 6 | 3 | 0.333 | 0.000 | 1.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | roma_settlement | clear | 5 | 2 | 0.200 | 0.000 | 0.333 |  | 0.200 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | social_housing | ambiguous | 5 | 4 | 0.800 | 0.000 | 3.000 |  | 0.200 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | social_housing | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | villas | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | villas | clear | 3 | 2 | -0.333 | -0.500 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | gender | female | ambiguous | 9 | 4 | -0.222 | -0.750 | 0.000 |  | 0.111 | 0.000 | 0.375 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | gender | female | clear | 5 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | any_minority | ambiguous | 21 | 4 | 0.381 | -0.333 | 1.571 |  | 0.286 | 0.045 | 0.619 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | any_minority | clear | 18 | 2 | 0.056 | 0.000 | 0.125 |  | 0.222 | 0.125 | 0.300 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | local_migrant | ambiguous | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | local_migrant | clear | 9 | 2 | 0.222 | 0.200 | 0.250 |  | 0.222 | 0.200 | 0.250 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | romanian | ambiguous | 9 | 4 | 0.778 | 0.000 | 1.909 |  | 0.333 | 0.000 | 0.818 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | romanian | clear | 5 | 2 | -0.400 | -0.500 | 0.000 |  | 0.200 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | syrian | ambiguous | 8 | 4 | 0.125 | -1.600 | 1.333 |  | 0.375 | 0.091 | 0.800 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | syrian | clear | 4 | 2 | 0.250 | 0.000 | 0.500 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | asylum_seeker | ambiguous | 5 | 4 | -0.600 | -3.000 | 0.429 |  | 0.400 | 0.000 | 0.750 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | asylum_seeker | clear | 6 | 2 | -0.333 | -0.400 | 0.000 |  | 0.167 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | seasonal_worker | ambiguous | 7 | 4 | -0.143 | -1.500 | 1.800 |  | 0.286 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | seasonal_worker | clear | 6 | 2 | -0.167 | -0.250 | 0.000 |  | 0.167 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | roma_settlement | ambiguous | 3 | 3 | 1.000 | 0.000 | 3.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | roma_settlement | clear | 6 | 2 | 0.833 | 0.750 | 1.000 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | social_housing | ambiguous | 3 | 2 | -1.000 | -3.000 | 0.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | villas | ambiguous | 4 | 3 | -1.500 | -3.000 | 0.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | villas | clear | 6 | 3 | -0.167 | -0.333 | 0.000 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | any_minority | ambiguous | 12 | 5 | -0.417 | -1.615 | 0.615 |  | 0.583 | 0.385 | 0.889 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | any_minority | clear | 10 | 2 | 0.500 | 0.250 | 0.667 |  | 0.300 | 0.250 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | local_migrant | ambiguous | 4 | 4 | -0.250 | -2.000 | 1.000 |  | 0.750 | 0.250 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | local_migrant | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | romanian | ambiguous | 5 | 3 | -0.400 | -1.500 | 1.000 |  | 0.400 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | romanian | clear | 6 | 2 | 0.167 | 0.000 | 0.250 |  | 0.167 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | syrian | ambiguous | 3 | 3 | -0.667 | -3.000 | 1.000 |  | 0.667 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | syrian | clear | 3 | 2 | 1.333 | 1.000 | 1.500 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | housing | area | roma_settlement | ambiguous | 3 | 3 | 1.000 | 0.000 | 2.000 |  | 0.667 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | roma_settlement | clear | 3 | 2 | 0.333 | 0.000 | 1.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | social_housing | ambiguous | 4 | 2 | -0.250 | -1.000 | 0.500 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | social_housing | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | villas | ambiguous | 5 | 3 | 0.000 | -0.500 | 0.500 |  | 0.400 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | villas | clear | 6 | 3 | 0.000 | -1.000 | 0.500 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | gender | female | ambiguous | 4 | 3 | 0.750 | 0.000 | 1.500 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | gender | female | clear | 3 | 2 | -1.000 | -2.000 | -0.500 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | any_minority | ambiguous | 11 | 3 | 0.273 | 0.200 | 0.500 |  | 0.545 | 0.250 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | any_minority | clear | 13 | 3 | 0.154 | 0.000 | 0.250 |  | 0.154 | 0.000 | 0.250 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | local_migrant | ambiguous | 5 | 2 | 0.200 | 0.000 | 0.500 |  | 0.600 | 0.500 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | local_migrant | clear | 7 | 3 | 0.143 | 0.000 | 0.333 |  | 0.143 | 0.000 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | romanian | ambiguous | 3 | 3 | 1.000 | 0.000 | 2.000 |  | 0.667 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | romanian | clear | 3 | 1 | 0.333 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | syrian | ambiguous | 3 | 3 | -0.333 | -1.000 | 0.000 |  | 0.333 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | syrian | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | asylum_seeker | ambiguous | 6 | 3 | 0.333 | 0.000 | 1.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | asylum_seeker | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | seasonal_worker | ambiguous | 2 | 1 | 0.500 |  |  |  | 0.500 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | seasonal_worker | clear | 4 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | relief | area | roma_settlement | ambiguous | 3 | 2 | 0.000 | -5.000 | 2.500 |  | 0.667 | 0.500 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | social_housing | ambiguous | 3 | 2 | 1.667 | 0.000 | 2.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | social_housing | clear | 1 | 1 | 3.333 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | villas | ambiguous | 4 | 3 | -2.917 | -8.333 | 5.000 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | any_minority | ambiguous | 10 | 3 | -4.924 | -12.311 | 1.667 |  | 0.600 | 0.333 | 0.750 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | any_minority | clear | 7 | 2 | 1.906 | -2.914 | 8.333 |  | 0.571 | 0.333 | 0.750 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | local_migrant | ambiguous | 1 | 1 | -5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | local_migrant | clear | 3 | 2 | -2.700 | -5.186 | 2.273 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | romanian | ambiguous | 5 | 3 | -4.333 | -8.333 | 0.000 |  | 0.400 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | romanian | clear | 2 | 2 | -4.808 | -11.888 | 2.273 |  | 0.500 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | syrian | ambiguous | 4 | 3 | -5.644 | -16.288 | 10.000 |  | 0.750 | 0.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | syrian | clear | 2 | 2 | 15.530 | 10.606 | 20.455 |  | 1.000 | 1.000 | 1.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | any_minority | ambiguous | 15 | 3 | 0.000 | 0.000 | 0.000 |  | 0.133 | 0.000 | 0.222 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | any_minority | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | local_migrant | ambiguous | 6 | 3 | 0.000 | 0.000 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | romanian | ambiguous | 5 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | romanian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | syrian | ambiguous | 4 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | syrian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | social_housing | ambiguous | 1 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | villas | ambiguous | 1 | 1 | -4.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | gender | female | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | any_minority | ambiguous | 3 | 3 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | romanian | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | syrian | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | status | asylum_seeker | ambiguous | 2 | 1 | 3.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | social_housing | ambiguous | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | villas | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | any_minority | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | any_minority | clear | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | local_migrant | clear | 2 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | romanian | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | housing | area | roma_settlement | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | social_housing | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | social_housing | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | villas | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | villas | clear | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | gender | female | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | ambiguous | 3 | 2 | 0.333 | 0.000 | 0.500 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | clear | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | ambiguous | 1 | 1 | 1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | romanian | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | romanian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | syrian | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | clear | 3 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | seasonal_worker | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | seasonal_worker | clear | 1 | 1 | -1.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | relief | area | roma_settlement | clear | 3 | 2 | -1.667 | -2.500 | 0.000 |  | 0.333 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | villas | ambiguous | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | villas | clear | 1 | 1 | -5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | any_minority | ambiguous | 2 | 1 | 0.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | any_minority | clear | 3 | 1 | -1.667 |  |  |  | 0.333 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | local_migrant | ambiguous | 1 | 1 | -5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | local_migrant | clear | 1 | 1 | -5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | romanian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | syrian | ambiguous | 1 | 1 | 5.000 |  |  |  | 1.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | syrian | clear | 1 | 1 | 0.000 |  |  |  | 0.000 |  |  | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | any_minority | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | syrian | ambiguous | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | el | 81 | 1.000 | 0.000 |  |
| apertus-8b | en | 88 | 0.989 | 0.000 | not-a-permutation 1 |
| apertus-8b | fr | 99 | 0.960 | 0.010 | not-a-permutation 4 |
| krikri-8b | el | 627 | 0.995 | 0.008 | bad-shares 2, not-a-permutation 1 |
| krikri-8b | en | 622 | 0.998 | 0.002 | bad-shares 1 |
| krikri-8b | fr | 609 | 0.987 | 0.005 | not-a-permutation 8 |
| llama-3.1-8b | el | 490 | 0.951 | 0.002 | not-a-permutation 24 |
| llama-3.1-8b | en | 492 | 0.961 | 0.024 | not-a-permutation 16, bad-shares 3 |
| llama-3.1-8b | fr | 473 | 0.968 | 0.013 | not-a-permutation 13, bad-shares 2 |
| meltemi-7b | el | 396 | 0.987 | 0.149 | no-json 2, not-a-permutation 2, shares-do-not-sum-to-100 1 |
| meltemi-7b | en | 414 | 0.998 | 0.147 | shares-do-not-sum-to-100 1 |
| meltemi-7b | fr | 419 | 0.902 | 0.064 | shares-do-not-sum-to-100 41 |
| qwen2.5-7b | el | 155 | 1.000 | 0.000 |  |
| qwen2.5-7b | en | 166 | 0.970 | 0.000 | not-a-permutation 5 |
| qwen2.5-7b | fr | 177 | 0.994 | 0.000 | not-a-permutation 1 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | origin=syrian | 0.625 | 1.000 | 0.375 |
| apertus-8b | dispatch | need=pregnant | 0.800 | 1.000 | 0.200 |
| apertus-8b | dispatch | gender=female | 0.875 | 1.000 | 0.125 |
| apertus-8b | dispatch | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | area=social_housing | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | area=villas | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | need=age80 | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | need=dialysis | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | need=infant | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | need=wheelchair | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | origin=romanian | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | placebo | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| apertus-8b | dispatch | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | area=social_housing | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | area=villas | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | need=age80 | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | need=dialysis | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | need=infant | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | need=pregnant | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | need=wheelchair | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | origin=romanian | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | origin=syrian | 1.000 | 1.000 | 0.000 |
| apertus-8b | evacuation | placebo | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | area=social_housing | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | area=villas | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | gender=female | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | need=age80 | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | need=dialysis | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | need=infant | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | need=pregnant | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | need=wheelchair | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | origin=romanian | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | origin=syrian | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | placebo | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| apertus-8b | housing | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | area=roma_settlement | 1.000 |  |  |
| apertus-8b | relief | origin=syrian | 1.000 |  |  |
| krikri-8b | dispatch | status=asylum_seeker | 0.969 | 1.000 | 0.031 |
| krikri-8b | dispatch | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | area=social_housing | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | area=villas | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | gender=female | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | need=age80 | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | need=dialysis | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | need=infant | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | need=pregnant | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | need=wheelchair | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | origin=romanian | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | origin=syrian | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | placebo | 1.000 | 1.000 | 0.000 |
| krikri-8b | dispatch | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | area=social_housing | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | area=villas | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | need=age80 | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | need=dialysis | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | need=infant | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | need=pregnant | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | need=wheelchair | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | origin=romanian | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | origin=syrian | 1.000 | 1.000 | 0.000 |
| krikri-8b | evacuation | placebo | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | area=social_housing | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | area=villas | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | gender=female | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | need=age80 | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | need=dialysis | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | need=infant | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | need=pregnant | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | need=wheelchair | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | origin=romanian | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | origin=syrian | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | placebo | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| krikri-8b | housing | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| krikri-8b | relief | origin=romanian | 0.917 | 0.944 | 0.028 |
| krikri-8b | relief | area=roma_settlement | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | area=social_housing | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | area=villas | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=age80 | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=dialysis | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=infant | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=pregnant | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=wheelchair | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | origin=local_migrant | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | origin=syrian | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | placebo | 1.000 | 0.944 | -0.056 |
| krikri-8b | triage | placebo | 0.933 | 0.960 | 0.027 |
| krikri-8b | triage | need=pregnant | 0.947 | 0.960 | 0.013 |
| krikri-8b | triage | need=age80 | 0.952 | 0.960 | 0.008 |
| krikri-8b | triage | origin=syrian | 0.952 | 0.960 | 0.008 |
| krikri-8b | triage | origin=local_migrant | 0.955 | 0.960 | 0.005 |
| krikri-8b | triage | need=dialysis | 0.960 | 0.960 | 0.000 |
| krikri-8b | triage | need=infant | 1.000 | 0.960 | -0.040 |
| krikri-8b | triage | need=wheelchair | 1.000 | 0.960 | -0.040 |
| krikri-8b | triage | origin=romanian | 1.000 | 0.960 | -0.040 |
| llama-3.1-8b | dispatch | area=roma_settlement | 0.812 | 0.880 | 0.068 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.853 | 0.880 | 0.027 |
| llama-3.1-8b | dispatch | origin=syrian | 0.875 | 0.880 | 0.005 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.903 | 0.880 | -0.023 |
| llama-3.1-8b | dispatch | need=dialysis | 0.906 | 0.880 | -0.026 |
| llama-3.1-8b | dispatch | origin=romanian | 0.909 | 0.880 | -0.029 |
| llama-3.1-8b | dispatch | need=pregnant | 0.914 | 0.880 | -0.034 |
| llama-3.1-8b | dispatch | gender=female | 0.917 | 0.880 | -0.037 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.926 | 0.880 | -0.046 |
| llama-3.1-8b | dispatch | need=age80 | 0.933 | 0.880 | -0.053 |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.933 | 0.880 | -0.053 |
| llama-3.1-8b | dispatch | placebo | 0.939 | 0.880 | -0.059 |
| llama-3.1-8b | dispatch | area=villas | 0.941 | 0.880 | -0.061 |
| llama-3.1-8b | dispatch | need=infant | 0.966 | 0.880 | -0.086 |
| llama-3.1-8b | dispatch | area=social_housing | 0.971 | 0.880 | -0.091 |
| llama-3.1-8b | evacuation | area=social_housing | 0.917 | 1.000 | 0.083 |
| llama-3.1-8b | evacuation | need=infant | 0.941 | 1.000 | 0.059 |
| llama-3.1-8b | evacuation | need=age80 | 0.964 | 1.000 | 0.036 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.966 | 1.000 | 0.034 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | area=villas | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | need=pregnant | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | need=wheelchair | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | origin=romanian | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | origin=syrian | 1.000 | 1.000 | 0.000 |
| llama-3.1-8b | evacuation | placebo | 1.000 | 1.000 | 0.000 |
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
| llama-3.1-8b | relief | area=villas | 0.933 | 0.933 | 0.000 |
| llama-3.1-8b | relief | origin=romanian | 0.933 | 0.933 | 0.000 |
| llama-3.1-8b | relief | area=social_housing | 0.938 | 0.933 | -0.004 |
| llama-3.1-8b | relief | placebo | 0.938 | 0.933 | -0.004 |
| llama-3.1-8b | relief | area=roma_settlement | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | need=age80 | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | need=dialysis | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | need=infant | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | need=pregnant | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | need=wheelchair | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | origin=local_migrant | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | relief | origin=syrian | 1.000 | 0.933 | -0.067 |
| llama-3.1-8b | triage | need=infant | 0.900 | 0.833 | -0.067 |
| llama-3.1-8b | triage | need=dialysis | 0.917 | 0.833 | -0.083 |
| llama-3.1-8b | triage | need=age80 | 0.938 | 0.833 | -0.104 |
| llama-3.1-8b | triage | need=wheelchair | 0.941 | 0.833 | -0.108 |
| llama-3.1-8b | triage | need=pregnant | 1.000 | 0.833 | -0.167 |
| llama-3.1-8b | triage | origin=local_migrant | 1.000 | 0.833 | -0.167 |
| llama-3.1-8b | triage | origin=romanian | 1.000 | 0.833 | -0.167 |
| llama-3.1-8b | triage | origin=syrian | 1.000 | 0.833 | -0.167 |
| llama-3.1-8b | triage | placebo | 1.000 | 0.833 | -0.167 |
| meltemi-7b | dispatch | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | area=social_housing | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | area=villas | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | gender=female | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=infant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=pregnant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | origin=romanian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | origin=syrian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | placebo | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | area=social_housing | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | area=villas | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | need=infant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | need=pregnant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | origin=romanian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | origin=syrian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | evacuation | placebo | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | area=social_housing | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | area=villas | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | gender=female | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | need=infant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | need=pregnant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | origin=romanian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | origin=syrian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | placebo | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| meltemi-7b | housing | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| meltemi-7b | relief | area=villas | 0.588 | 0.824 | 0.235 |
| meltemi-7b | relief | need=dialysis | 0.739 | 0.824 | 0.084 |
| meltemi-7b | relief | need=pregnant | 0.762 | 0.824 | 0.062 |
| meltemi-7b | relief | need=wheelchair | 0.783 | 0.824 | 0.041 |
| meltemi-7b | relief | area=social_housing | 0.786 | 0.824 | 0.038 |
| meltemi-7b | relief | origin=romanian | 0.800 | 0.824 | 0.024 |
| meltemi-7b | relief | origin=syrian | 0.850 | 0.824 | -0.026 |
| meltemi-7b | relief | area=roma_settlement | 0.857 | 0.824 | -0.034 |
| meltemi-7b | relief | need=age80 | 0.889 | 0.824 | -0.065 |
| meltemi-7b | relief | origin=local_migrant | 0.889 | 0.824 | -0.065 |
| meltemi-7b | relief | placebo | 0.889 | 0.824 | -0.065 |
| meltemi-7b | relief | need=infant | 0.895 | 0.824 | -0.071 |
| meltemi-7b | triage | origin=local_migrant | 0.923 | 1.000 | 0.077 |
| meltemi-7b | triage | need=pregnant | 0.938 | 1.000 | 0.062 |
| meltemi-7b | triage | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=infant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | origin=romanian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | origin=syrian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | area=villas | 0.889 | 1.000 | 0.111 |
| qwen2.5-7b | dispatch | status=seasonal_worker | 0.900 | 1.000 | 0.100 |
| qwen2.5-7b | dispatch | area=social_housing | 0.917 | 1.000 | 0.083 |
| qwen2.5-7b | dispatch | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | gender=female | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | need=dialysis | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | need=infant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | need=pregnant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | need=wheelchair | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | origin=romanian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | origin=syrian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | area=social_housing | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | area=villas | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | need=dialysis | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | need=infant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | need=pregnant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | need=wheelchair | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | origin=romanian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | origin=syrian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | evacuation | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | area=social_housing | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | area=villas | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | gender=female | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | need=dialysis | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | need=infant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | need=pregnant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | need=wheelchair | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | origin=romanian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | origin=syrian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | housing | status=seasonal_worker | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | area=social_housing | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | area=villas | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | need=dialysis | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | need=infant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | need=pregnant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | need=wheelchair | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | origin=romanian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | origin=syrian | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | relief | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | triage | need=dialysis | 0.667 | 0.800 | 0.133 |
| qwen2.5-7b | triage | origin=romanian | 0.750 | 0.800 | 0.050 |
| qwen2.5-7b | triage | need=age80 | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | need=infant | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | need=pregnant | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | need=wheelchair | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | origin=local_migrant | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | origin=syrian | 1.000 | 0.800 | -0.200 |
| qwen2.5-7b | triage | placebo | 1.000 | 0.800 | -0.200 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch |  |  |  |  | did not fit: Singular matrix |
| apertus-8b | evacuation |  |  |  |  | did not fit: Singular matrix |
| apertus-8b | housing |  |  |  |  | did not fit: Singular matrix |
| krikri-8b | dispatch | Intercept | 0.592 | 0.267 | 0.026 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing] | -0.064 | 0.351 | 0.856 |  |
| krikri-8b | dispatch | C(key)[T.area=villas] | -0.856 | 0.313 | 0.006 |  |
| krikri-8b | dispatch | C(key)[T.gender=female] | -0.083 | 0.376 | 0.826 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant] | -0.378 | 0.325 | 0.245 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian] | -0.383 | 0.336 | 0.255 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian] | -0.366 | 0.345 | 0.290 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker] | 0.285 | 0.339 | 0.401 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.726 | 0.360 | 0.043 |  |
| krikri-8b | dispatch | C(language)[T.en] | -0.312 | 0.428 | 0.465 |  |
| krikri-8b | dispatch | C(language)[T.fr] | 0.465 | 0.427 | 0.275 |  |
| krikri-8b | dispatch | C(clarity)[T.clear] | 0.003 | 0.180 | 0.989 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.271 | 0.545 | 0.620 |  |
| krikri-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.241 | 0.536 | 0.653 |  |
| krikri-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.364 | 0.616 | 0.554 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.024 | 0.551 | 0.966 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | 0.047 | 0.533 | 0.930 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | 0.107 | 0.538 | 0.842 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.310 | 0.630 | 0.623 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.365 | 0.554 | 0.510 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.611 | 0.568 | 0.282 |  |
| krikri-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -0.320 | 0.527 | 0.544 |  |
| krikri-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.943 | 0.565 | 0.095 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.479 | 0.543 | 0.377 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.758 | 0.559 | 0.175 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.741 | 0.555 | 0.181 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.689 | 0.632 | 0.276 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.390 | 0.573 | 0.496 |  |
| krikri-8b | evacuation |  |  |  |  | did not fit: Singular matrix |
| krikri-8b | housing | Intercept | 0.116 | 0.230 | 0.614 |  |
| krikri-8b | housing | C(key)[T.area=social_housing] | 0.046 | 0.275 | 0.866 |  |
| krikri-8b | housing | C(key)[T.area=villas] | -1.934 | 0.469 | 0.000 |  |
| krikri-8b | housing | C(key)[T.gender=female] | -0.023 | 0.257 | 0.929 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant] | 0.050 | 0.277 | 0.857 |  |
| krikri-8b | housing | C(key)[T.origin=romanian] | 0.698 | 0.456 | 0.126 |  |
| krikri-8b | housing | C(key)[T.origin=syrian] | -0.233 | 0.310 | 0.452 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker] | -0.020 | 0.259 | 0.939 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker] | -0.449 | 0.288 | 0.118 |  |
| krikri-8b | housing | C(language)[T.en] | -0.145 | 0.292 | 0.619 |  |
| krikri-8b | housing | C(language)[T.fr] | 0.352 | 0.294 | 0.230 |  |
| krikri-8b | housing | C(clarity)[T.clear] | 0.091 | 0.158 | 0.567 |  |
| krikri-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.087 | 0.390 | 0.823 |  |
| krikri-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | 1.207 | 0.547 | 0.027 |  |
| krikri-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | 0.008 | 0.358 | 0.982 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.027 | 0.398 | 0.947 |  |
| krikri-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.708 | 0.527 | 0.179 |  |
| krikri-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | 0.123 | 0.471 | 0.794 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.031 | 0.388 | 0.937 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.295 | 0.390 | 0.449 |  |
| krikri-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | 0.151 | 0.417 | 0.717 |  |
| krikri-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.954 | 0.582 | 0.001 |  |
| krikri-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | 0.534 | 0.441 | 0.226 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.499 | 0.446 | 0.263 |  |
| krikri-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.542 | 0.552 | 0.005 |  |
| krikri-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.396 | 0.438 | 0.366 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.106 | 0.375 | 0.777 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.020 | 0.408 | 0.012 |  |
| krikri-8b | relief | Intercept | -2.223 | 2.864 | 0.438 |  |
| krikri-8b | relief | C(key)[T.area=social_housing] | 2.735 | 3.703 | 0.460 |  |
| krikri-8b | relief | C(key)[T.area=villas] | -5.497 | 4.818 | 0.254 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant] | -0.390 | 3.243 | 0.904 |  |
| krikri-8b | relief | C(key)[T.origin=romanian] | 3.089 | 4.389 | 0.481 |  |
| krikri-8b | relief | C(key)[T.origin=syrian] | 2.735 | 3.703 | 0.460 |  |
| krikri-8b | relief | C(language)[T.en] | 0.016 | 3.677 | 0.997 |  |
| krikri-8b | relief | C(language)[T.fr] | -0.540 | 3.644 | 0.882 |  |
| krikri-8b | relief | C(clarity)[T.clear] | 4.352 | 2.116 | 0.040 |  |
| krikri-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -3.362 | 4.835 | 0.487 |  |
| krikri-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 2.785 | 6.031 | 0.644 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -4.016 | 4.660 | 0.389 |  |
| krikri-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -2.717 | 5.354 | 0.612 |  |
| krikri-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | 2.649 | 4.993 | 0.596 |  |
| krikri-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.364 | 5.766 | 0.560 |  |
| krikri-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -0.132 | 6.045 | 0.983 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -5.239 | 5.374 | 0.330 |  |
| krikri-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -3.718 | 6.236 | 0.551 |  |
| krikri-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.945 | 4.916 | 0.692 |  |
| krikri-8b | triage | Intercept | 0.413 | 0.159 | 0.009 |  |
| krikri-8b | triage | C(key)[T.origin=romanian] | 0.372 | 0.225 | 0.098 |  |
| krikri-8b | triage | C(key)[T.origin=syrian] | 0.176 | 0.209 | 0.400 |  |
| krikri-8b | triage | C(language)[T.en] | -0.413 | 0.220 | 0.060 |  |
| krikri-8b | triage | C(language)[T.fr] | -0.413 | 0.353 | 0.243 |  |
| krikri-8b | triage | C(clarity)[T.clear] | -0.355 | 0.137 | 0.009 |  |
| krikri-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.195 | 0.360 | 0.588 |  |
| krikri-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.034 | 0.305 | 0.911 |  |
| krikri-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.372 | 0.419 | 0.375 |  |
| krikri-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.058 | 0.420 | 0.891 |  |
| llama-3.1-8b | dispatch |  |  |  |  | did not fit: Singular matrix |
| llama-3.1-8b | evacuation | Intercept | 0.471 | 0.446 | 0.290 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.108 | 0.587 | 0.854 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.257 | 0.593 | 0.034 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.036 | 0.546 | 0.947 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | -0.486 | 0.742 | 0.513 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.108 | 0.548 | 0.844 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | -0.058 | 0.583 | 0.921 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.503 | 0.633 | 0.427 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.313 | 0.434 | 0.471 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | 0.195 | 0.971 | 0.841 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | 0.212 | 0.832 | 0.799 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.203 | 0.820 | 0.805 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | 0.536 | 0.955 | 0.575 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | 0.075 | 0.801 | 0.926 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.299 | 1.013 | 0.768 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.683 | 0.926 | 0.461 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.143 | 0.859 | 0.183 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.091 | 0.971 | 0.925 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.189 | 0.913 | 0.836 |  |
| llama-3.1-8b | housing | Intercept | -0.442 | 0.904 | 0.625 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.110 | 1.102 | 0.920 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -2.807 | 1.101 | 0.011 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female] | 0.537 | 1.139 | 0.637 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | 0.137 | 1.139 | 0.904 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | 0.333 | 1.270 | 0.793 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.263 | 1.421 | 0.853 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.246 | 1.101 | 0.823 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.772 | 1.191 | 0.020 | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.en] | -7.393 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.fr] | 2.471 | 1.140 | 0.030 | did not converge; read with care |
| llama-3.1-8b | housing | C(clarity)[T.clear] | 0.231 | 0.534 | 0.665 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | 7.284 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | 9.018 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | 8.084 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | 7.536 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | 7.533 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | 8.015 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 8.837 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 10.800 |  |  | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -2.371 | 1.484 | 0.110 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -2.627 | 1.480 | 0.076 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -2.162 | 1.444 | 0.134 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.867 | 1.480 | 0.207 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -2.506 | 1.708 | 0.142 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.744 | 1.707 | 0.307 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.711 | 1.430 | 0.232 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.277 | 1.531 | 0.856 | did not converge; read with care |
| llama-3.1-8b | relief |  |  |  |  | did not fit: Singular matrix |
| llama-3.1-8b | triage |  |  |  |  | did not fit: Singular matrix |
| meltemi-7b | dispatch | Intercept | 0.335 | 0.769 | 0.663 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing] | 0.192 | 0.930 | 0.837 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas] | -0.702 | 1.051 | 0.504 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female] | 0.086 | 1.037 | 0.934 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant] | -0.041 | 0.868 | 0.963 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian] | -0.899 | 1.036 | 0.386 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian] | -0.163 | 1.359 | 0.905 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker] | -0.856 | 0.942 | 0.364 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker] | -0.313 | 0.883 | 0.723 |  |
| meltemi-7b | dispatch | C(language)[T.en] | 0.339 | 0.809 | 0.675 |  |
| meltemi-7b | dispatch | C(language)[T.fr] | 0.342 | 1.053 | 0.745 |  |
| meltemi-7b | dispatch | C(clarity)[T.clear] | -0.148 | 0.674 | 0.826 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | 0.194 | 1.249 | 0.877 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | 0.477 | 1.420 | 0.737 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.796 | 1.216 | 0.513 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.171 | 1.109 | 0.877 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | 0.563 | 1.206 | 0.640 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.408 | 1.505 | 0.786 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.222 | 1.236 | 0.857 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.121 | 1.118 | 0.914 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.720 | 1.486 | 0.628 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | 0.189 | 1.758 | 0.914 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.972 | 1.427 | 0.496 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.238 | 1.328 | 0.858 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | 1.056 | 1.432 | 0.461 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.323 | 1.651 | 0.845 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.356 | 1.338 | 0.790 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.072 | 1.332 | 0.421 |  |
| meltemi-7b | evacuation | Intercept | 0.832 | 1.056 | 0.431 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing] | 1.902 |  |  |  |
| meltemi-7b | evacuation | C(key)[T.area=villas] | -1.505 | 1.115 | 0.177 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant] | -1.525 | 1.060 | 0.150 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian] | -1.769 |  |  |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian] | -3.223 | 1.384 | 0.020 |  |
| meltemi-7b | evacuation | C(language)[T.en] | 1.054 | 0.666 | 0.114 |  |
| meltemi-7b | evacuation | C(language)[T.fr] | -0.465 | 0.704 | 0.509 |  |
| meltemi-7b | evacuation | C(clarity)[T.clear] | 0.030 | 0.872 | 0.972 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -3.696 |  |  |  |
| meltemi-7b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.261 | 1.223 | 0.831 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.163 | 1.508 | 0.914 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | 0.124 |  |  |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | 3.412 | 1.555 | 0.028 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -4.280 |  |  |  |
| meltemi-7b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.873 | 1.488 | 0.557 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 2.147 | 1.475 | 0.145 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | 1.958 | 0.419 | 0.000 |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | 2.987 | 1.552 | 0.054 |  |
| meltemi-7b | housing |  |  |  |  | did not fit: Singular matrix |
| meltemi-7b | relief |  |  |  |  | did not fit: Singular matrix |
| meltemi-7b | triage |  |  |  |  | did not fit: Singular matrix |
| qwen2.5-7b | dispatch |  |  |  |  | did not fit: Singular matrix |
| qwen2.5-7b | evacuation |  |  |  |  | did not fit: Singular matrix |
| qwen2.5-7b | housing |  |  |  |  | did not fit: Singular matrix |
| qwen2.5-7b | relief |  |  |  |  | did not fit: Singular matrix |
| qwen2.5-7b | triage |  |  |  |  | needs at least two cases and some variation |
