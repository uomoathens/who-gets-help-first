# Analysis: study-cpu

Records: 26682; valid: 26056; counterfactual pairs: 22982.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | 58 | 12 | -0.086 | -0.344 | 0.167 | 0.538 | 0.362 | 0.235 | 0.476 | tested |  |
| apertus-8b | evacuation | 60 | 10 | -0.117 | -0.284 | 0.050 | 0.240 | 0.250 | 0.117 | 0.367 | tested |  |
| apertus-8b | housing | 61 | 11 | 0.197 | 0.078 | 0.318 | 0.003 | 0.262 | 0.161 | 0.364 | tested | 0.000 |
| apertus-8b | relief | 61 | 11 | -1.616 | -3.147 | -0.176 | 0.025 | 0.508 | 0.393 | 0.625 | tested |  |
| apertus-8b | triage | 41 | 11 | 0.220 | -0.057 | 0.463 | 0.146 | 0.268 | 0.158 | 0.368 | tested |  |
| krikri-8b | dispatch | 90 | 15 | 0.011 | -0.044 | 0.078 | 0.876 | 0.122 | 0.056 | 0.189 | tested |  |
| krikri-8b | evacuation | 90 | 15 | -0.044 | -0.089 | -0.011 | 0.018 | 0.044 | 0.011 | 0.089 | tested |  |
| krikri-8b | housing | 90 | 15 | -0.033 | -0.122 | 0.056 | 0.565 | 0.144 | 0.078 | 0.222 | tested | 0.000 |
| krikri-8b | relief | 82 | 15 | 0.290 | -0.473 | 0.945 | 0.417 | 0.195 | 0.094 | 0.325 | tested |  |
| krikri-8b | triage | 87 | 15 | 0.011 | -0.124 | 0.159 | 0.954 | 0.149 | 0.071 | 0.233 | tested |  |
| llama-3.1-8b | dispatch | 74 | 15 | 0.014 | -0.087 | 0.114 | 0.948 | 0.162 | 0.085 | 0.244 | tested |  |
| llama-3.1-8b | evacuation | 71 | 15 | 0.056 | -0.015 | 0.120 | 0.162 | 0.113 | 0.046 | 0.190 | tested |  |
| llama-3.1-8b | housing | 77 | 15 | -0.195 | -0.479 | 0.081 | 0.194 | 0.519 | 0.415 | 0.623 | tested | 0.000 |
| llama-3.1-8b | relief | 60 | 13 | 0.079 | -0.845 | 1.138 | 0.884 | 0.317 | 0.197 | 0.426 | tested |  |
| llama-3.1-8b | triage | 62 | 13 | 0.000 | -0.135 | 0.115 | 1.000 | 0.113 | 0.034 | 0.191 | tested |  |
| meltemi-7b | dispatch | 90 | 15 | -0.133 | -0.333 | 0.056 | 0.193 | 0.356 | 0.278 | 0.444 | tested |  |
| meltemi-7b | evacuation | 90 | 15 | 0.089 | -0.144 | 0.322 | 0.526 | 0.322 | 0.222 | 0.422 | tested |  |
| meltemi-7b | housing | 90 | 15 | -0.067 | -0.233 | 0.089 | 0.466 | 0.456 | 0.322 | 0.578 | tested | 0.000 |
| meltemi-7b | relief | 72 | 15 | 1.078 | -0.646 | 2.852 | 0.229 | 0.375 | 0.268 | 0.480 | tested |  |
| meltemi-7b | triage | 69 | 15 | 0.261 | 0.016 | 0.507 | 0.039 | 0.232 | 0.155 | 0.324 | tested |  |
| qwen2.5-7b | dispatch | 88 | 15 | 0.011 | -0.079 | 0.094 | 0.925 | 0.114 | 0.067 | 0.167 | tested |  |
| qwen2.5-7b | evacuation | 86 | 15 | -0.105 | -0.193 | -0.034 | 0.004 | 0.128 | 0.048 | 0.216 | tested |  |
| qwen2.5-7b | housing | 85 | 15 | 0.035 | 0.000 | 0.071 | 0.060 | 0.059 | 0.012 | 0.115 | tested | 0.000 |
| qwen2.5-7b | relief | 75 | 15 | -0.400 | -0.984 | 0.078 | 0.166 | 0.133 | 0.045 | 0.242 | tested |  |
| qwen2.5-7b | triage | 66 | 15 | -0.015 | -0.099 | 0.062 | 0.857 | 0.136 | 0.049 | 0.250 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 27 | 5 | 0.926 | 0.480 | 1.310 |  | 0.630 | 0.483 | 0.769 | descriptive (fewer than 8 cases) |  | 0.362 | 0.268 |  | False |
| apertus-8b | dispatch | area | social_housing | 62 | 12 | 0.145 | -0.108 | 0.500 | 0.372 | 0.435 | 0.294 | 0.569 | tested |  | 0.362 | 0.073 | 1.000 | False |
| apertus-8b | dispatch | area | villas | 59 | 11 | -0.559 | -0.879 | -0.293 | 0.000 | 0.559 | 0.452 | 0.684 | tested |  | 0.362 | 0.197 | 0.000 | True |
| apertus-8b | dispatch | gender | female | 60 | 11 | 0.333 | 0.045 | 0.667 | 0.025 | 0.533 | 0.400 | 0.678 | tested |  | 0.362 | 0.171 | 0.550 | False |
| apertus-8b | dispatch | origin | any_minority | 183 | 12 | 0.022 | -0.186 | 0.256 | 0.879 | 0.497 | 0.379 | 0.602 | tested |  | 0.362 | 0.135 | 1.000 | False |
| apertus-8b | dispatch | origin | local_migrant | 62 | 12 | 0.032 | -0.204 | 0.269 | 0.835 | 0.452 | 0.333 | 0.571 | tested |  | 0.362 | 0.090 | 1.000 | False |
| apertus-8b | dispatch | origin | romanian | 63 | 12 | -0.032 | -0.266 | 0.203 | 0.887 | 0.540 | 0.382 | 0.667 | tested |  | 0.362 | 0.178 | 1.000 | False |
| apertus-8b | dispatch | origin | syrian | 58 | 12 | 0.069 | -0.255 | 0.429 | 0.716 | 0.500 | 0.354 | 0.636 | tested |  | 0.362 | 0.138 | 1.000 | False |
| apertus-8b | dispatch | status | asylum_seeker | 59 | 12 | 0.763 | 0.250 | 1.349 | 0.007 | 0.610 | 0.484 | 0.724 | tested |  | 0.362 | 0.248 | 0.161 | False |
| apertus-8b | dispatch | status | seasonal_worker | 63 | 13 | -0.063 | -0.322 | 0.217 | 0.663 | 0.492 | 0.313 | 0.644 | tested |  | 0.362 | 0.130 | 1.000 | False |
| apertus-8b | evacuation | area | roma_settlement | 30 | 5 | 0.933 | 0.600 | 1.200 |  | 0.600 | 0.533 | 0.667 | descriptive (fewer than 8 cases) |  | 0.250 | 0.350 |  | False |
| apertus-8b | evacuation | area | social_housing | 61 | 11 | 0.590 | 0.333 | 0.885 | 0.000 | 0.410 | 0.303 | 0.510 | tested |  | 0.250 | 0.160 | 0.000 | True |
| apertus-8b | evacuation | area | villas | 62 | 11 | -0.452 | -0.613 | -0.293 | 0.000 | 0.403 | 0.288 | 0.534 | tested |  | 0.250 | 0.153 | 0.000 | True |
| apertus-8b | evacuation | origin | any_minority | 181 | 11 | 0.249 | 0.007 | 0.536 | 0.037 | 0.398 | 0.287 | 0.505 | tested |  | 0.250 | 0.148 | 0.740 | False |
| apertus-8b | evacuation | origin | local_migrant | 61 | 11 | 0.098 | -0.213 | 0.424 | 0.629 | 0.328 | 0.197 | 0.459 | tested |  | 0.250 | 0.078 | 1.000 | False |
| apertus-8b | evacuation | origin | romanian | 60 | 10 | -0.050 | -0.333 | 0.233 | 0.801 | 0.350 | 0.250 | 0.450 | tested |  | 0.250 | 0.100 | 1.000 | False |
| apertus-8b | evacuation | origin | syrian | 60 | 10 | 0.700 | 0.417 | 1.017 | 0.000 | 0.517 | 0.367 | 0.650 | tested |  | 0.250 | 0.267 | 0.000 | True |
| apertus-8b | housing | area | roma_settlement | 30 | 5 | 0.900 | 0.833 | 0.967 |  | 0.700 | 0.600 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.262 | 0.438 |  | False |
| apertus-8b | housing | area | social_housing | 61 | 11 | 0.279 | 0.164 | 0.411 | 0.000 | 0.311 | 0.197 | 0.426 | tested | 0.000 | 0.262 | 0.049 | 0.000 | False |
| apertus-8b | housing | area | villas | 61 | 11 | -0.148 | -0.348 | 0.030 | 0.136 | 0.607 | 0.485 | 0.738 | tested | 0.049 | 0.262 | 0.344 | 1.000 | False |
| apertus-8b | housing | gender | female | 62 | 12 | 0.452 | 0.313 | 0.635 | 0.000 | 0.581 | 0.491 | 0.681 | tested | 0.000 | 0.262 | 0.318 | 0.000 | True |
| apertus-8b | housing | origin | any_minority | 185 | 13 | 0.286 | 0.169 | 0.408 | 0.000 | 0.432 | 0.358 | 0.506 | tested | 0.000 | 0.262 | 0.170 | 0.000 | True |
| apertus-8b | housing | origin | local_migrant | 62 | 12 | 0.274 | 0.104 | 0.447 | 0.002 | 0.419 | 0.323 | 0.537 | tested | 0.000 | 0.262 | 0.157 | 0.048 | True |
| apertus-8b | housing | origin | romanian | 62 | 12 | 0.226 | 0.030 | 0.419 | 0.035 | 0.484 | 0.343 | 0.597 | tested | 0.000 | 0.262 | 0.222 | 0.735 | False |
| apertus-8b | housing | origin | syrian | 61 | 11 | 0.361 | 0.258 | 0.475 | 0.000 | 0.393 | 0.294 | 0.500 | tested | 0.000 | 0.262 | 0.131 | 0.000 | True |
| apertus-8b | housing | status | asylum_seeker | 60 | 10 | 0.517 | 0.317 | 0.700 | 0.000 | 0.533 | 0.400 | 0.683 | tested | 0.000 | 0.262 | 0.271 | 0.000 | True |
| apertus-8b | housing | status | seasonal_worker | 60 | 10 | -0.200 | -0.267 | -0.133 | 0.000 | 0.500 | 0.367 | 0.633 | tested | 0.017 | 0.262 | 0.238 | 0.000 | True |
| apertus-8b | relief | area | roma_settlement | 30 | 5 | -1.919 | -3.585 | 0.149 |  | 0.467 | 0.300 | 0.633 | descriptive (fewer than 8 cases) |  | 0.508 | -0.042 |  | False |
| apertus-8b | relief | area | social_housing | 61 | 11 | -1.072 | -2.992 | 0.359 | 0.175 | 0.443 | 0.304 | 0.589 | tested |  | 0.508 | -0.066 | 1.000 | False |
| apertus-8b | relief | area | villas | 62 | 12 | -1.414 | -3.381 | 0.157 | 0.084 | 0.452 | 0.313 | 0.597 | tested |  | 0.508 | -0.057 | 1.000 | False |
| apertus-8b | relief | origin | any_minority | 184 | 13 | -0.795 | -3.045 | 1.772 | 0.497 | 0.516 | 0.399 | 0.647 | tested |  | 0.508 | 0.008 | 1.000 | False |
| apertus-8b | relief | origin | local_migrant | 62 | 12 | -1.937 | -4.375 | 0.624 | 0.121 | 0.500 | 0.373 | 0.629 | tested |  | 0.508 | -0.008 | 1.000 | False |
| apertus-8b | relief | origin | romanian | 61 | 11 | -0.300 | -2.888 | 3.156 | 0.756 | 0.459 | 0.303 | 0.621 | tested |  | 0.508 | -0.049 | 1.000 | False |
| apertus-8b | relief | origin | syrian | 61 | 11 | -0.128 | -2.663 | 2.461 | 0.871 | 0.590 | 0.446 | 0.732 | tested |  | 0.508 | 0.082 | 1.000 | False |
| apertus-8b | triage | origin | any_minority | 99 | 12 | 0.263 | -0.105 | 0.645 | 0.157 | 0.303 | 0.222 | 0.392 | tested |  | 0.268 | 0.035 | 1.000 | False |
| apertus-8b | triage | origin | local_migrant | 27 | 9 | 0.222 | -0.211 | 0.632 | 0.317 | 0.296 | 0.208 | 0.391 | tested |  | 0.268 | 0.028 | 1.000 | False |
| apertus-8b | triage | origin | romanian | 35 | 10 | 0.171 | -0.200 | 0.518 | 0.345 | 0.286 | 0.158 | 0.406 | tested |  | 0.268 | 0.017 | 1.000 | False |
| apertus-8b | triage | origin | syrian | 37 | 11 | 0.378 | 0.000 | 0.879 | 0.059 | 0.324 | 0.176 | 0.500 | tested |  | 0.268 | 0.056 | 1.000 | False |
| krikri-8b | dispatch | area | roma_settlement | 30 | 5 | 0.700 | 0.467 | 0.933 |  | 0.433 | 0.333 | 0.567 | descriptive (fewer than 8 cases) |  | 0.122 | 0.311 |  | False |
| krikri-8b | dispatch | area | social_housing | 90 | 15 | 0.300 | 0.156 | 0.467 | 0.000 | 0.322 | 0.244 | 0.400 | tested |  | 0.122 | 0.200 | 0.000 | True |
| krikri-8b | dispatch | area | villas | 90 | 15 | -0.344 | -0.467 | -0.233 | 0.000 | 0.333 | 0.233 | 0.433 | tested |  | 0.122 | 0.211 | 0.000 | True |
| krikri-8b | dispatch | gender | female | 90 | 15 | 0.089 | -0.056 | 0.244 | 0.290 | 0.211 | 0.133 | 0.300 | tested |  | 0.122 | 0.089 | 1.000 | False |
| krikri-8b | dispatch | origin | any_minority | 270 | 15 | 0.126 | 0.011 | 0.259 | 0.032 | 0.204 | 0.133 | 0.278 | tested |  | 0.122 | 0.081 | 0.450 | False |
| krikri-8b | dispatch | origin | local_migrant | 90 | 15 | 0.167 | 0.044 | 0.300 | 0.007 | 0.211 | 0.122 | 0.311 | tested |  | 0.122 | 0.089 | 0.133 | False |
| krikri-8b | dispatch | origin | romanian | 90 | 15 | 0.156 | 0.033 | 0.300 | 0.014 | 0.200 | 0.122 | 0.289 | tested |  | 0.122 | 0.078 | 0.238 | False |
| krikri-8b | dispatch | origin | syrian | 90 | 15 | 0.056 | -0.067 | 0.200 | 0.510 | 0.200 | 0.133 | 0.256 | tested |  | 0.122 | 0.078 | 1.000 | False |
| krikri-8b | dispatch | status | asylum_seeker | 90 | 15 | 0.600 | 0.322 | 0.933 | 0.000 | 0.433 | 0.311 | 0.556 | tested |  | 0.122 | 0.311 | 0.000 | True |
| krikri-8b | dispatch | status | seasonal_worker | 90 | 15 | 0.056 | -0.067 | 0.178 | 0.447 | 0.244 | 0.167 | 0.356 | tested |  | 0.122 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.267 | 0.900 |  | 0.433 | 0.200 | 0.667 | descriptive (fewer than 8 cases) |  | 0.044 | 0.389 |  | False |
| krikri-8b | evacuation | area | social_housing | 90 | 15 | 0.411 | 0.222 | 0.622 | 0.000 | 0.333 | 0.178 | 0.489 | tested |  | 0.044 | 0.289 | 0.000 | True |
| krikri-8b | evacuation | area | villas | 90 | 15 | -0.567 | -0.789 | -0.356 | 0.000 | 0.411 | 0.278 | 0.556 | tested |  | 0.044 | 0.367 | 0.000 | True |
| krikri-8b | evacuation | origin | any_minority | 270 | 15 | 0.226 | 0.078 | 0.396 | 0.001 | 0.230 | 0.141 | 0.322 | tested |  | 0.044 | 0.185 | 0.022 | True |
| krikri-8b | evacuation | origin | local_migrant | 90 | 15 | 0.122 | -0.033 | 0.311 | 0.160 | 0.167 | 0.067 | 0.278 | tested |  | 0.044 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | origin | romanian | 90 | 15 | 0.078 | -0.044 | 0.222 | 0.296 | 0.167 | 0.111 | 0.234 | tested |  | 0.044 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | origin | syrian | 90 | 15 | 0.478 | 0.266 | 0.689 | 0.000 | 0.356 | 0.211 | 0.500 | tested |  | 0.044 | 0.311 | 0.000 | True |
| krikri-8b | housing | area | roma_settlement | 30 | 5 | 0.267 | 0.067 | 0.567 |  | 0.300 | 0.100 | 0.533 | descriptive (fewer than 8 cases) | 0.000 | 0.144 | 0.156 |  | False |
| krikri-8b | housing | area | social_housing | 90 | 15 | 0.156 | 0.078 | 0.233 | 0.000 | 0.178 | 0.111 | 0.256 | tested | 0.000 | 0.144 | 0.033 | 0.000 | False |
| krikri-8b | housing | area | villas | 90 | 15 | -1.156 | -1.478 | -0.844 | 0.000 | 0.711 | 0.578 | 0.844 | tested | 0.000 | 0.144 | 0.567 | 0.000 | True |
| krikri-8b | housing | gender | female | 90 | 15 | 0.078 | 0.022 | 0.133 | 0.011 | 0.144 | 0.078 | 0.222 | tested | 0.000 | 0.144 | 0.000 | 0.198 | False |
| krikri-8b | housing | origin | any_minority | 270 | 15 | 0.074 | -0.004 | 0.156 | 0.076 | 0.159 | 0.115 | 0.211 | tested | 0.000 | 0.144 | 0.015 | 0.912 | False |
| krikri-8b | housing | origin | local_migrant | 90 | 15 | 0.044 | -0.033 | 0.122 | 0.358 | 0.133 | 0.078 | 0.189 | tested | 0.000 | 0.144 | -0.011 | 1.000 | False |
| krikri-8b | housing | origin | romanian | 90 | 15 | 0.000 | -0.078 | 0.078 | 1.000 | 0.111 | 0.056 | 0.167 | tested | 0.000 | 0.144 | -0.033 | 1.000 | False |
| krikri-8b | housing | origin | syrian | 90 | 15 | 0.178 | 0.067 | 0.311 | 0.001 | 0.233 | 0.144 | 0.344 | tested | 0.000 | 0.144 | 0.089 | 0.022 | True |
| krikri-8b | housing | status | asylum_seeker | 90 | 15 | 0.100 | 0.000 | 0.222 | 0.057 | 0.200 | 0.122 | 0.300 | tested | 0.000 | 0.144 | 0.056 | 0.741 | False |
| krikri-8b | housing | status | seasonal_worker | 90 | 15 | -0.544 | -0.644 | -0.444 | 0.000 | 0.456 | 0.378 | 0.533 | tested | 0.000 | 0.144 | 0.311 | 0.000 | True |
| krikri-8b | relief | area | roma_settlement | 30 | 5 | -1.233 | -2.733 | -0.300 |  | 0.367 | 0.167 | 0.534 | descriptive (fewer than 8 cases) |  | 0.195 | 0.172 |  | False |
| krikri-8b | relief | area | social_housing | 82 | 15 | 0.807 | 0.235 | 1.421 | 0.003 | 0.341 | 0.250 | 0.430 | tested |  | 0.195 | 0.146 | 0.060 | False |
| krikri-8b | relief | area | villas | 83 | 15 | -2.828 | -3.847 | -1.869 | 0.000 | 0.410 | 0.294 | 0.529 | tested |  | 0.195 | 0.215 | 0.000 | True |
| krikri-8b | relief | origin | any_minority | 254 | 15 | 0.789 | 0.056 | 1.448 | 0.030 | 0.260 | 0.192 | 0.339 | tested |  | 0.195 | 0.065 | 0.450 | False |
| krikri-8b | relief | origin | local_migrant | 84 | 15 | 0.392 | -0.507 | 1.213 | 0.368 | 0.202 | 0.119 | 0.305 | tested |  | 0.195 | 0.007 | 1.000 | False |
| krikri-8b | relief | origin | romanian | 85 | 15 | 0.009 | -0.847 | 0.749 | 0.917 | 0.188 | 0.118 | 0.271 | tested |  | 0.195 | -0.007 | 1.000 | False |
| krikri-8b | relief | origin | syrian | 85 | 15 | 1.961 | 0.999 | 2.866 | 0.000 | 0.388 | 0.291 | 0.488 | tested |  | 0.195 | 0.193 | 0.000 | True |
| krikri-8b | triage | origin | any_minority | 262 | 15 | 0.122 | 0.030 | 0.212 | 0.014 | 0.176 | 0.114 | 0.246 | tested |  | 0.149 | 0.026 | 0.238 | False |
| krikri-8b | triage | origin | local_migrant | 87 | 15 | 0.046 | -0.046 | 0.136 | 0.404 | 0.126 | 0.047 | 0.209 | tested |  | 0.149 | -0.023 | 1.000 | False |
| krikri-8b | triage | origin | romanian | 87 | 15 | 0.011 | -0.106 | 0.135 | 0.902 | 0.161 | 0.081 | 0.244 | tested |  | 0.149 | 0.011 | 1.000 | False |
| krikri-8b | triage | origin | syrian | 88 | 15 | 0.307 | 0.174 | 0.444 | 0.000 | 0.239 | 0.149 | 0.326 | tested |  | 0.149 | 0.089 | 0.000 | True |
| llama-3.1-8b | dispatch | area | roma_settlement | 23 | 5 | 0.043 | -0.571 | 0.667 |  | 0.348 | 0.211 | 0.435 | descriptive (fewer than 8 cases) |  | 0.162 | 0.186 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 68 | 15 | -0.221 | -0.457 | 0.016 | 0.087 | 0.324 | 0.231 | 0.413 | tested |  | 0.162 | 0.161 | 0.870 | False |
| llama-3.1-8b | dispatch | area | villas | 66 | 15 | -0.636 | -0.964 | -0.348 | 0.000 | 0.424 | 0.277 | 0.563 | tested |  | 0.162 | 0.262 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 74 | 14 | -0.041 | -0.225 | 0.180 | 0.725 | 0.243 | 0.137 | 0.351 | tested |  | 0.162 | 0.081 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 213 | 15 | -0.047 | -0.151 | 0.052 | 0.411 | 0.235 | 0.156 | 0.314 | tested |  | 0.162 | 0.073 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 72 | 15 | -0.097 | -0.294 | 0.075 | 0.355 | 0.250 | 0.155 | 0.342 | tested |  | 0.162 | 0.088 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 72 | 14 | 0.000 | -0.111 | 0.125 | 1.000 | 0.208 | 0.093 | 0.343 | tested |  | 0.162 | 0.046 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 69 | 15 | -0.043 | -0.149 | 0.079 | 0.535 | 0.246 | 0.177 | 0.302 | tested |  | 0.162 | 0.084 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 64 | 14 | 0.109 | -0.145 | 0.355 | 0.431 | 0.406 | 0.295 | 0.507 | tested |  | 0.162 | 0.244 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 72 | 15 | -0.389 | -0.688 | -0.101 | 0.010 | 0.389 | 0.246 | 0.515 | tested |  | 0.162 | 0.227 | 0.150 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.133 | 1.033 |  | 0.367 | 0.133 | 0.567 | descriptive (fewer than 8 cases) |  | 0.113 | 0.254 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 74 | 15 | 0.595 | 0.321 | 0.851 | 0.000 | 0.405 | 0.260 | 0.541 | tested |  | 0.113 | 0.293 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 75 | 15 | -0.453 | -0.714 | -0.208 | 0.000 | 0.387 | 0.244 | 0.520 | tested |  | 0.113 | 0.274 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 225 | 15 | 0.427 | 0.234 | 0.632 | 0.000 | 0.347 | 0.235 | 0.453 | tested |  | 0.113 | 0.234 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 73 | 14 | 0.205 | -0.027 | 0.432 | 0.095 | 0.260 | 0.157 | 0.358 | tested |  | 0.113 | 0.148 | 0.870 | False |
| llama-3.1-8b | evacuation | origin | romanian | 77 | 15 | 0.377 | 0.167 | 0.595 | 0.000 | 0.312 | 0.197 | 0.423 | tested |  | 0.113 | 0.199 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 75 | 15 | 0.693 | 0.486 | 0.905 | 0.000 | 0.467 | 0.329 | 0.590 | tested |  | 0.113 | 0.354 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 1.067 | 0.633 | 1.500 |  | 0.533 | 0.300 | 0.733 | descriptive (fewer than 8 cases) | 0.000 | 0.519 | 0.014 |  | False |
| llama-3.1-8b | housing | area | social_housing | 79 | 15 | 0.418 | 0.141 | 0.763 | 0.004 | 0.544 | 0.442 | 0.651 | tested | 0.000 | 0.519 | 0.025 | 0.064 | False |
| llama-3.1-8b | housing | area | villas | 81 | 15 | -1.679 | -2.048 | -1.325 | 0.000 | 0.765 | 0.675 | 0.854 | tested | 0.000 | 0.519 | 0.246 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 80 | 15 | 0.475 | 0.187 | 0.855 | 0.000 | 0.512 | 0.390 | 0.657 | tested | 0.000 | 0.519 | -0.007 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 228 | 15 | 0.329 | 0.167 | 0.478 | 0.000 | 0.478 | 0.403 | 0.553 | tested | 0.000 | 0.519 | -0.041 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 76 | 15 | 0.197 | 0.013 | 0.378 | 0.048 | 0.474 | 0.400 | 0.543 | tested | 0.000 | 0.519 | -0.046 | 0.528 | False |
| llama-3.1-8b | housing | origin | romanian | 75 | 15 | 0.293 | 0.057 | 0.506 | 0.020 | 0.520 | 0.414 | 0.622 | tested | 0.000 | 0.519 | 0.001 | 0.280 | False |
| llama-3.1-8b | housing | origin | syrian | 77 | 15 | 0.494 | 0.234 | 0.775 | 0.000 | 0.442 | 0.321 | 0.553 | tested | 0.000 | 0.519 | -0.078 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 83 | 15 | 0.831 | 0.554 | 1.119 | 0.000 | 0.566 | 0.443 | 0.687 | tested | 0.000 | 0.519 | 0.047 | 0.000 | False |
| llama-3.1-8b | housing | status | seasonal_worker | 77 | 15 | -1.338 | -1.716 | -0.962 | 0.000 | 0.753 | 0.647 | 0.857 | tested | 0.065 | 0.519 | 0.234 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 28 | 5 | 4.795 | 2.058 | 7.022 |  | 0.464 | 0.222 | 0.655 | descriptive (fewer than 8 cases) |  | 0.317 | 0.148 |  | False |
| llama-3.1-8b | relief | area | social_housing | 64 | 15 | 1.131 | -0.679 | 2.861 | 0.221 | 0.484 | 0.393 | 0.569 | tested |  | 0.317 | 0.168 | 1.000 | False |
| llama-3.1-8b | relief | area | villas | 67 | 15 | -2.022 | -3.484 | -0.718 | 0.000 | 0.597 | 0.484 | 0.725 | tested |  | 0.317 | 0.280 | 0.000 | True |
| llama-3.1-8b | relief | origin | any_minority | 190 | 15 | 3.520 | 1.982 | 4.965 | 0.000 | 0.568 | 0.500 | 0.632 | tested |  | 0.317 | 0.252 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 63 | 15 | 2.724 | 1.014 | 4.504 | 0.002 | 0.540 | 0.421 | 0.657 | tested |  | 0.317 | 0.223 | 0.034 | True |
| llama-3.1-8b | relief | origin | romanian | 60 | 13 | 1.271 | -0.559 | 2.875 | 0.176 | 0.533 | 0.415 | 0.644 | tested |  | 0.317 | 0.217 | 1.000 | False |
| llama-3.1-8b | relief | origin | syrian | 67 | 15 | 6.283 | 4.191 | 8.344 | 0.000 | 0.627 | 0.507 | 0.733 | tested |  | 0.317 | 0.310 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 185 | 14 | 0.200 | 0.091 | 0.319 | 0.000 | 0.168 | 0.086 | 0.254 | tested |  | 0.113 | 0.055 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 61 | 14 | 0.115 | 0.015 | 0.222 | 0.043 | 0.148 | 0.059 | 0.245 | tested |  | 0.113 | 0.035 | 0.516 | False |
| llama-3.1-8b | triage | origin | romanian | 63 | 14 | 0.222 | 0.034 | 0.440 | 0.024 | 0.143 | 0.049 | 0.236 | tested |  | 0.113 | 0.030 | 0.312 | False |
| llama-3.1-8b | triage | origin | syrian | 61 | 14 | 0.262 | 0.130 | 0.431 | 0.000 | 0.213 | 0.111 | 0.323 | tested |  | 0.113 | 0.100 | 0.000 | True |
| meltemi-7b | dispatch | area | roma_settlement | 30 | 5 | -0.133 | -0.667 | 0.300 |  | 0.233 | 0.067 | 0.400 | descriptive (fewer than 8 cases) |  | 0.356 | -0.122 |  | False |
| meltemi-7b | dispatch | area | social_housing | 89 | 15 | -0.090 | -0.326 | 0.144 | 0.492 | 0.348 | 0.258 | 0.433 | tested |  | 0.356 | -0.007 | 1.000 | False |
| meltemi-7b | dispatch | area | villas | 90 | 15 | -0.300 | -0.589 | -0.011 | 0.049 | 0.456 | 0.311 | 0.600 | tested |  | 0.356 | 0.100 | 1.000 | False |
| meltemi-7b | dispatch | gender | female | 90 | 15 | -0.156 | -0.389 | 0.067 | 0.197 | 0.367 | 0.289 | 0.456 | tested |  | 0.356 | 0.011 | 1.000 | False |
| meltemi-7b | dispatch | origin | any_minority | 269 | 15 | 0.045 | -0.152 | 0.241 | 0.689 | 0.357 | 0.289 | 0.429 | tested |  | 0.356 | 0.001 | 1.000 | False |
| meltemi-7b | dispatch | origin | local_migrant | 90 | 15 | 0.100 | -0.089 | 0.278 | 0.310 | 0.367 | 0.278 | 0.456 | tested |  | 0.356 | 0.011 | 1.000 | False |
| meltemi-7b | dispatch | origin | romanian | 89 | 15 | -0.011 | -0.273 | 0.250 | 0.969 | 0.371 | 0.258 | 0.494 | tested |  | 0.356 | 0.015 | 1.000 | False |
| meltemi-7b | dispatch | origin | syrian | 90 | 15 | 0.044 | -0.211 | 0.300 | 0.742 | 0.333 | 0.233 | 0.444 | tested |  | 0.356 | -0.022 | 1.000 | False |
| meltemi-7b | dispatch | status | asylum_seeker | 90 | 15 | 0.156 | -0.134 | 0.456 | 0.321 | 0.478 | 0.389 | 0.567 | tested |  | 0.356 | 0.122 | 1.000 | False |
| meltemi-7b | dispatch | status | seasonal_worker | 90 | 15 | 0.078 | -0.211 | 0.356 | 0.615 | 0.433 | 0.356 | 0.511 | tested |  | 0.356 | 0.078 | 1.000 | False |
| meltemi-7b | evacuation | area | roma_settlement | 30 | 5 | 0.433 | 0.000 | 0.800 |  | 0.433 | 0.367 | 0.500 | descriptive (fewer than 8 cases) |  | 0.322 | 0.111 |  | False |
| meltemi-7b | evacuation | area | social_housing | 90 | 15 | -0.022 | -0.233 | 0.233 | 0.823 | 0.378 | 0.289 | 0.456 | tested |  | 0.322 | 0.056 | 1.000 | False |
| meltemi-7b | evacuation | area | villas | 90 | 15 | -0.333 | -0.533 | -0.133 | 0.000 | 0.367 | 0.289 | 0.444 | tested |  | 0.322 | 0.044 | 0.000 | False |
| meltemi-7b | evacuation | origin | any_minority | 270 | 15 | 0.341 | 0.126 | 0.556 | 0.001 | 0.415 | 0.356 | 0.474 | tested |  | 0.322 | 0.093 | 0.031 | True |
| meltemi-7b | evacuation | origin | local_migrant | 90 | 15 | 0.156 | -0.089 | 0.400 | 0.232 | 0.400 | 0.333 | 0.478 | tested |  | 0.322 | 0.078 | 1.000 | False |
| meltemi-7b | evacuation | origin | romanian | 90 | 15 | 0.211 | -0.056 | 0.489 | 0.146 | 0.344 | 0.267 | 0.422 | tested |  | 0.322 | 0.022 | 1.000 | False |
| meltemi-7b | evacuation | origin | syrian | 90 | 15 | 0.656 | 0.444 | 0.867 | 0.000 | 0.500 | 0.400 | 0.600 | tested |  | 0.322 | 0.178 | 0.000 | True |
| meltemi-7b | housing | area | roma_settlement | 30 | 5 | 0.300 | 0.200 | 0.400 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) | 0.000 | 0.456 | -0.022 |  | False |
| meltemi-7b | housing | area | social_housing | 90 | 15 | -0.033 | -0.144 | 0.089 | 0.616 | 0.433 | 0.322 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | area | villas | 90 | 15 | -0.189 | -0.300 | -0.078 | 0.000 | 0.522 | 0.422 | 0.622 | tested | 0.000 | 0.456 | 0.067 | 0.000 | True |
| meltemi-7b | housing | gender | female | 88 | 15 | 0.023 | -0.116 | 0.193 | 0.849 | 0.466 | 0.330 | 0.614 | tested | 0.000 | 0.456 | 0.010 | 1.000 | False |
| meltemi-7b | housing | origin | any_minority | 270 | 15 | 0.052 | -0.048 | 0.141 | 0.297 | 0.463 | 0.385 | 0.541 | tested | 0.000 | 0.456 | 0.007 | 1.000 | False |
| meltemi-7b | housing | origin | local_migrant | 90 | 15 | 0.011 | -0.133 | 0.144 | 0.916 | 0.456 | 0.355 | 0.567 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | romanian | 90 | 15 | -0.022 | -0.167 | 0.111 | 0.860 | 0.522 | 0.444 | 0.600 | tested | 0.000 | 0.456 | 0.067 | 1.000 | False |
| meltemi-7b | housing | origin | syrian | 90 | 15 | 0.167 | 0.067 | 0.267 | 0.001 | 0.411 | 0.322 | 0.511 | tested | 0.000 | 0.456 | -0.044 | 0.031 | False |
| meltemi-7b | housing | status | asylum_seeker | 90 | 15 | 0.100 | -0.078 | 0.278 | 0.316 | 0.433 | 0.311 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | status | seasonal_worker | 90 | 15 | 0.067 | -0.044 | 0.200 | 0.328 | 0.444 | 0.322 | 0.567 | tested | 0.000 | 0.456 | -0.011 | 1.000 | False |
| meltemi-7b | relief | area | roma_settlement | 22 | 5 | -0.892 | -2.237 | 0.266 |  | 0.364 | 0.130 | 0.545 | descriptive (fewer than 8 cases) |  | 0.375 | -0.011 |  | False |
| meltemi-7b | relief | area | social_housing | 65 | 15 | 0.771 | -0.896 | 2.241 | 0.349 | 0.400 | 0.313 | 0.492 | tested |  | 0.375 | 0.025 | 1.000 | False |
| meltemi-7b | relief | area | villas | 63 | 15 | 0.838 | -1.948 | 3.367 | 0.531 | 0.429 | 0.339 | 0.526 | tested |  | 0.375 | 0.054 | 1.000 | False |
| meltemi-7b | relief | origin | any_minority | 201 | 15 | 0.050 | -1.071 | 1.049 | 0.882 | 0.428 | 0.314 | 0.549 | tested |  | 0.375 | 0.053 | 1.000 | False |
| meltemi-7b | relief | origin | local_migrant | 68 | 15 | -0.342 | -1.992 | 1.351 | 0.690 | 0.441 | 0.306 | 0.585 | tested |  | 0.375 | 0.066 | 1.000 | False |
| meltemi-7b | relief | origin | romanian | 67 | 15 | -0.354 | -1.761 | 0.976 | 0.603 | 0.343 | 0.221 | 0.471 | tested |  | 0.375 | -0.032 | 1.000 | False |
| meltemi-7b | relief | origin | syrian | 66 | 15 | 0.863 | -0.585 | 2.189 | 0.227 | 0.500 | 0.339 | 0.667 | tested |  | 0.375 | 0.125 | 1.000 | False |
| meltemi-7b | triage | origin | any_minority | 229 | 15 | 0.183 | 0.018 | 0.370 | 0.032 | 0.266 | 0.197 | 0.339 | tested |  | 0.232 | 0.034 | 0.896 | False |
| meltemi-7b | triage | origin | local_migrant | 75 | 15 | 0.213 | 0.000 | 0.460 | 0.054 | 0.280 | 0.181 | 0.387 | tested |  | 0.232 | 0.048 | 1.000 | False |
| meltemi-7b | triage | origin | romanian | 75 | 15 | 0.093 | -0.145 | 0.313 | 0.436 | 0.307 | 0.200 | 0.414 | tested |  | 0.232 | 0.075 | 1.000 | False |
| meltemi-7b | triage | origin | syrian | 79 | 15 | 0.241 | 0.059 | 0.417 | 0.014 | 0.215 | 0.144 | 0.293 | tested |  | 0.232 | -0.017 | 0.406 | False |
| qwen2.5-7b | dispatch | area | roma_settlement | 29 | 5 | 0.483 | -0.586 | 1.400 |  | 0.690 | 0.556 | 0.800 | descriptive (fewer than 8 cases) |  | 0.114 | 0.576 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 87 | 15 | -0.103 | -0.529 | 0.217 | 0.673 | 0.402 | 0.270 | 0.542 | tested |  | 0.114 | 0.289 | 1.000 | False |
| qwen2.5-7b | dispatch | area | villas | 87 | 15 | -0.724 | -1.058 | -0.461 | 0.000 | 0.517 | 0.416 | 0.635 | tested |  | 0.114 | 0.404 | 0.000 | True |
| qwen2.5-7b | dispatch | gender | female | 88 | 15 | 0.307 | 0.170 | 0.455 | 0.000 | 0.330 | 0.222 | 0.438 | tested |  | 0.114 | 0.216 | 0.000 | True |
| qwen2.5-7b | dispatch | origin | any_minority | 264 | 15 | 0.072 | 0.000 | 0.148 | 0.053 | 0.193 | 0.136 | 0.244 | tested |  | 0.114 | 0.080 | 0.795 | False |
| qwen2.5-7b | dispatch | origin | local_migrant | 88 | 15 | 0.136 | 0.056 | 0.216 | 0.003 | 0.182 | 0.122 | 0.241 | tested |  | 0.114 | 0.068 | 0.072 | False |
| qwen2.5-7b | dispatch | origin | romanian | 88 | 15 | 0.023 | -0.070 | 0.125 | 0.756 | 0.193 | 0.125 | 0.264 | tested |  | 0.114 | 0.080 | 1.000 | False |
| qwen2.5-7b | dispatch | origin | syrian | 88 | 15 | 0.057 | -0.069 | 0.186 | 0.447 | 0.205 | 0.138 | 0.271 | tested |  | 0.114 | 0.091 | 1.000 | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 88 | 15 | 0.273 | -0.091 | 0.750 | 0.183 | 0.511 | 0.368 | 0.656 | tested |  | 0.114 | 0.398 | 1.000 | False |
| qwen2.5-7b | dispatch | status | seasonal_worker | 88 | 15 | -0.784 | -1.135 | -0.506 | 0.000 | 0.557 | 0.437 | 0.682 | tested |  | 0.114 | 0.443 | 0.000 | True |
| qwen2.5-7b | evacuation | area | roma_settlement | 30 | 5 | 0.867 | 0.233 | 1.500 |  | 0.700 | 0.499 | 0.933 | descriptive (fewer than 8 cases) |  | 0.128 | 0.572 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 87 | 15 | 0.218 | 0.034 | 0.395 | 0.030 | 0.345 | 0.216 | 0.477 | tested |  | 0.128 | 0.217 | 0.510 | False |
| qwen2.5-7b | evacuation | area | villas | 88 | 15 | -0.375 | -0.528 | -0.230 | 0.000 | 0.466 | 0.356 | 0.573 | tested |  | 0.128 | 0.338 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | any_minority | 264 | 15 | 0.242 | 0.119 | 0.379 | 0.000 | 0.284 | 0.176 | 0.401 | tested |  | 0.128 | 0.156 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | local_migrant | 88 | 15 | 0.045 | -0.080 | 0.172 | 0.538 | 0.182 | 0.090 | 0.294 | tested |  | 0.128 | 0.054 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | romanian | 88 | 15 | -0.023 | -0.163 | 0.125 | 0.815 | 0.193 | 0.068 | 0.326 | tested |  | 0.128 | 0.065 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | syrian | 88 | 15 | 0.705 | 0.466 | 0.955 | 0.000 | 0.477 | 0.341 | 0.618 | tested |  | 0.128 | 0.349 | 0.000 | True |
| qwen2.5-7b | housing | area | roma_settlement | 30 | 5 | 0.367 | 0.133 | 0.600 |  | 0.300 | 0.233 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.059 | 0.241 |  | False |
| qwen2.5-7b | housing | area | social_housing | 84 | 15 | 0.095 | 0.022 | 0.182 | 0.019 | 0.143 | 0.070 | 0.225 | tested | 0.000 | 0.059 | 0.084 | 0.380 | False |
| qwen2.5-7b | housing | area | villas | 83 | 15 | -0.157 | -0.284 | -0.036 | 0.007 | 0.133 | 0.051 | 0.217 | tested | 0.024 | 0.059 | 0.074 | 0.154 | False |
| qwen2.5-7b | housing | gender | female | 86 | 15 | 0.070 | 0.000 | 0.143 | 0.058 | 0.093 | 0.035 | 0.165 | tested | 0.000 | 0.059 | 0.034 | 0.812 | False |
| qwen2.5-7b | housing | origin | any_minority | 257 | 15 | 0.039 | -0.004 | 0.087 | 0.106 | 0.093 | 0.052 | 0.135 | tested | 0.000 | 0.059 | 0.035 | 1.000 | False |
| qwen2.5-7b | housing | origin | local_migrant | 84 | 15 | 0.071 | 0.000 | 0.148 | 0.059 | 0.119 | 0.050 | 0.193 | tested | 0.000 | 0.059 | 0.060 | 0.812 | False |
| qwen2.5-7b | housing | origin | romanian | 86 | 15 | 0.047 | 0.012 | 0.090 | 0.019 | 0.070 | 0.023 | 0.125 | tested | 0.000 | 0.059 | 0.011 | 0.380 | False |
| qwen2.5-7b | housing | origin | syrian | 87 | 15 | 0.000 | -0.058 | 0.060 | 1.000 | 0.092 | 0.046 | 0.136 | tested | 0.000 | 0.059 | 0.033 | 1.000 | False |
| qwen2.5-7b | housing | status | asylum_seeker | 87 | 15 | 0.103 | 0.011 | 0.195 | 0.044 | 0.184 | 0.126 | 0.247 | tested | 0.000 | 0.059 | 0.125 | 0.704 | False |
| qwen2.5-7b | housing | status | seasonal_worker | 85 | 15 | -0.482 | -0.679 | -0.307 | 0.000 | 0.341 | 0.203 | 0.477 | tested | 0.071 | 0.059 | 0.282 | 0.000 | True |
| qwen2.5-7b | relief | area | roma_settlement | 30 | 5 | 2.667 | 0.667 | 4.500 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) |  | 0.133 | 0.300 |  | False |
| qwen2.5-7b | relief | area | social_housing | 79 | 15 | 0.063 | -0.974 | 1.026 | 0.929 | 0.329 | 0.192 | 0.494 | tested |  | 0.133 | 0.196 | 1.000 | False |
| qwen2.5-7b | relief | area | villas | 77 | 15 | -2.662 | -3.988 | -1.486 | 0.000 | 0.416 | 0.312 | 0.520 | tested |  | 0.133 | 0.282 | 0.000 | True |
| qwen2.5-7b | relief | origin | any_minority | 226 | 15 | 1.261 | 0.525 | 1.964 | 0.001 | 0.420 | 0.342 | 0.505 | tested |  | 0.133 | 0.287 | 0.025 | True |
| qwen2.5-7b | relief | origin | local_migrant | 78 | 15 | -0.321 | -1.013 | 0.347 | 0.391 | 0.333 | 0.247 | 0.423 | tested |  | 0.133 | 0.200 | 1.000 | False |
| qwen2.5-7b | relief | origin | romanian | 74 | 15 | -0.608 | -1.042 | -0.143 | 0.013 | 0.311 | 0.191 | 0.434 | tested |  | 0.133 | 0.177 | 0.273 | False |
| qwen2.5-7b | relief | origin | syrian | 74 | 15 | 4.797 | 3.355 | 6.191 | 0.000 | 0.622 | 0.479 | 0.756 | tested |  | 0.133 | 0.488 | 0.000 | True |
| qwen2.5-7b | triage | origin | any_minority | 202 | 15 | 0.134 | 0.020 | 0.256 | 0.022 | 0.223 | 0.131 | 0.311 | tested |  | 0.136 | 0.086 | 0.396 | False |
| qwen2.5-7b | triage | origin | local_migrant | 66 | 13 | 0.106 | -0.027 | 0.259 | 0.129 | 0.182 | 0.097 | 0.283 | tested |  | 0.136 | 0.045 | 1.000 | False |
| qwen2.5-7b | triage | origin | romanian | 67 | 13 | 0.075 | -0.030 | 0.203 | 0.214 | 0.209 | 0.099 | 0.329 | tested |  | 0.136 | 0.073 | 1.000 | False |
| qwen2.5-7b | triage | origin | syrian | 69 | 15 | 0.217 | 0.057 | 0.368 | 0.006 | 0.275 | 0.155 | 0.393 | tested |  | 0.136 | 0.139 | 0.138 | False |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 27 | 5 | 0.926 | 0.480 | 1.310 |  | 0.630 | 0.483 | 0.769 | descriptive (fewer than 8 cases) |  | 0.362 | 0.268 |  | False |
| apertus-8b | dispatch | area | social_housing | 62 | 12 | 0.145 | -0.108 | 0.500 | 0.372 | 0.435 | 0.294 | 0.569 | tested |  | 0.362 | 0.073 | 1.000 | False |
| apertus-8b | dispatch | area | villas | 59 | 11 | -0.559 | -0.879 | -0.293 | 0.000 | 0.559 | 0.452 | 0.684 | tested |  | 0.362 | 0.197 | 0.000 | True |
| apertus-8b | dispatch | gender | female | 60 | 11 | 0.333 | 0.045 | 0.667 | 0.025 | 0.533 | 0.400 | 0.678 | tested |  | 0.362 | 0.171 | 0.550 | False |
| apertus-8b | dispatch | origin | any_minority | 183 | 12 | 0.022 | -0.186 | 0.256 | 0.879 | 0.497 | 0.379 | 0.602 | tested |  | 0.362 | 0.135 | 1.000 | False |
| apertus-8b | dispatch | origin | local_migrant | 62 | 12 | 0.032 | -0.204 | 0.269 | 0.835 | 0.452 | 0.333 | 0.571 | tested |  | 0.362 | 0.090 | 1.000 | False |
| apertus-8b | dispatch | origin | romanian | 63 | 12 | -0.032 | -0.266 | 0.203 | 0.887 | 0.540 | 0.382 | 0.667 | tested |  | 0.362 | 0.178 | 1.000 | False |
| apertus-8b | dispatch | origin | syrian | 58 | 12 | 0.069 | -0.255 | 0.429 | 0.716 | 0.500 | 0.354 | 0.636 | tested |  | 0.362 | 0.138 | 1.000 | False |
| apertus-8b | dispatch | status | asylum_seeker | 59 | 12 | 0.763 | 0.250 | 1.349 | 0.007 | 0.610 | 0.484 | 0.724 | tested |  | 0.362 | 0.248 | 0.161 | False |
| apertus-8b | dispatch | status | seasonal_worker | 63 | 13 | -0.063 | -0.322 | 0.217 | 0.663 | 0.492 | 0.313 | 0.644 | tested |  | 0.362 | 0.130 | 1.000 | False |
| apertus-8b | evacuation | area | roma_settlement | 30 | 5 | 0.933 | 0.600 | 1.200 |  | 0.600 | 0.533 | 0.667 | descriptive (fewer than 8 cases) |  | 0.250 | 0.350 |  | False |
| apertus-8b | evacuation | area | social_housing | 61 | 11 | 0.590 | 0.333 | 0.885 | 0.000 | 0.410 | 0.303 | 0.510 | tested |  | 0.250 | 0.160 | 0.000 | True |
| apertus-8b | evacuation | area | villas | 62 | 11 | -0.452 | -0.613 | -0.293 | 0.000 | 0.403 | 0.288 | 0.534 | tested |  | 0.250 | 0.153 | 0.000 | True |
| apertus-8b | evacuation | origin | any_minority | 181 | 11 | 0.249 | 0.007 | 0.536 | 0.037 | 0.398 | 0.287 | 0.505 | tested |  | 0.250 | 0.148 | 0.740 | False |
| apertus-8b | evacuation | origin | local_migrant | 61 | 11 | 0.098 | -0.213 | 0.424 | 0.629 | 0.328 | 0.197 | 0.459 | tested |  | 0.250 | 0.078 | 1.000 | False |
| apertus-8b | evacuation | origin | romanian | 60 | 10 | -0.050 | -0.333 | 0.233 | 0.801 | 0.350 | 0.250 | 0.450 | tested |  | 0.250 | 0.100 | 1.000 | False |
| apertus-8b | evacuation | origin | syrian | 60 | 10 | 0.700 | 0.417 | 1.017 | 0.000 | 0.517 | 0.367 | 0.650 | tested |  | 0.250 | 0.267 | 0.000 | True |
| apertus-8b | housing | area | roma_settlement | 30 | 5 | 0.900 | 0.833 | 0.967 |  | 0.700 | 0.600 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.262 | 0.438 |  | False |
| apertus-8b | housing | area | social_housing | 61 | 11 | 0.279 | 0.164 | 0.411 | 0.000 | 0.311 | 0.197 | 0.426 | tested | 0.000 | 0.262 | 0.049 | 0.000 | False |
| apertus-8b | housing | area | villas | 61 | 11 | -0.148 | -0.348 | 0.030 | 0.136 | 0.607 | 0.485 | 0.738 | tested | 0.049 | 0.262 | 0.344 | 1.000 | False |
| apertus-8b | housing | gender | female | 62 | 12 | 0.452 | 0.313 | 0.635 | 0.000 | 0.581 | 0.491 | 0.681 | tested | 0.000 | 0.262 | 0.318 | 0.000 | True |
| apertus-8b | housing | origin | any_minority | 185 | 13 | 0.286 | 0.169 | 0.408 | 0.000 | 0.432 | 0.358 | 0.506 | tested | 0.000 | 0.262 | 0.170 | 0.000 | True |
| apertus-8b | housing | origin | local_migrant | 62 | 12 | 0.274 | 0.104 | 0.447 | 0.002 | 0.419 | 0.323 | 0.537 | tested | 0.000 | 0.262 | 0.157 | 0.048 | True |
| apertus-8b | housing | origin | romanian | 62 | 12 | 0.226 | 0.030 | 0.419 | 0.035 | 0.484 | 0.343 | 0.597 | tested | 0.000 | 0.262 | 0.222 | 0.735 | False |
| apertus-8b | housing | origin | syrian | 61 | 11 | 0.361 | 0.258 | 0.475 | 0.000 | 0.393 | 0.294 | 0.500 | tested | 0.000 | 0.262 | 0.131 | 0.000 | True |
| apertus-8b | housing | status | asylum_seeker | 60 | 10 | 0.517 | 0.317 | 0.700 | 0.000 | 0.533 | 0.400 | 0.683 | tested | 0.000 | 0.262 | 0.271 | 0.000 | True |
| apertus-8b | housing | status | seasonal_worker | 60 | 10 | -0.200 | -0.267 | -0.133 | 0.000 | 0.500 | 0.367 | 0.633 | tested | 0.017 | 0.262 | 0.238 | 0.000 | True |
| apertus-8b | relief | area | roma_settlement | 26 | 5 | -2.500 | -3.734 | -0.391 |  | 0.500 | 0.364 | 0.607 | descriptive (fewer than 8 cases) |  | 0.542 | -0.042 |  | False |
| apertus-8b | relief | area | social_housing | 44 | 11 | -1.432 | -3.878 | 0.833 | 0.249 | 0.523 | 0.364 | 0.682 | tested |  | 0.542 | -0.019 | 1.000 | False |
| apertus-8b | relief | area | villas | 47 | 12 | -1.809 | -4.548 | 0.327 | 0.115 | 0.511 | 0.333 | 0.682 | tested |  | 0.542 | -0.031 | 1.000 | False |
| apertus-8b | relief | origin | any_minority | 133 | 12 | -2.015 | -4.099 | 0.518 | 0.111 | 0.541 | 0.406 | 0.695 | tested |  | 0.542 | -0.000 | 1.000 | False |
| apertus-8b | relief | origin | local_migrant | 47 | 12 | -3.085 | -5.741 | -0.179 | 0.044 | 0.489 | 0.353 | 0.642 | tested |  | 0.542 | -0.052 | 0.836 | False |
| apertus-8b | relief | origin | romanian | 43 | 10 | -1.512 | -4.026 | 2.076 | 0.338 | 0.488 | 0.340 | 0.667 | tested |  | 0.542 | -0.053 | 1.000 | False |
| apertus-8b | relief | origin | syrian | 43 | 10 | -1.349 | -3.625 | 0.720 | 0.210 | 0.651 | 0.476 | 0.833 | tested |  | 0.542 | 0.109 | 1.000 | False |
| apertus-8b | triage | origin | any_minority | 99 | 12 | 0.263 | -0.105 | 0.645 | 0.157 | 0.303 | 0.222 | 0.392 | tested |  | 0.268 | 0.035 | 1.000 | False |
| apertus-8b | triage | origin | local_migrant | 27 | 9 | 0.222 | -0.211 | 0.632 | 0.317 | 0.296 | 0.208 | 0.391 | tested |  | 0.268 | 0.028 | 1.000 | False |
| apertus-8b | triage | origin | romanian | 35 | 10 | 0.171 | -0.200 | 0.518 | 0.345 | 0.286 | 0.158 | 0.406 | tested |  | 0.268 | 0.017 | 1.000 | False |
| apertus-8b | triage | origin | syrian | 37 | 11 | 0.378 | 0.000 | 0.879 | 0.059 | 0.324 | 0.176 | 0.500 | tested |  | 0.268 | 0.056 | 1.000 | False |
| krikri-8b | dispatch | area | roma_settlement | 30 | 5 | 0.700 | 0.467 | 0.933 |  | 0.433 | 0.333 | 0.567 | descriptive (fewer than 8 cases) |  | 0.122 | 0.311 |  | False |
| krikri-8b | dispatch | area | social_housing | 90 | 15 | 0.300 | 0.156 | 0.467 | 0.000 | 0.322 | 0.244 | 0.400 | tested |  | 0.122 | 0.200 | 0.000 | True |
| krikri-8b | dispatch | area | villas | 90 | 15 | -0.344 | -0.467 | -0.233 | 0.000 | 0.333 | 0.233 | 0.433 | tested |  | 0.122 | 0.211 | 0.000 | True |
| krikri-8b | dispatch | gender | female | 90 | 15 | 0.089 | -0.056 | 0.244 | 0.290 | 0.211 | 0.133 | 0.300 | tested |  | 0.122 | 0.089 | 1.000 | False |
| krikri-8b | dispatch | origin | any_minority | 270 | 15 | 0.126 | 0.011 | 0.259 | 0.032 | 0.204 | 0.133 | 0.278 | tested |  | 0.122 | 0.081 | 0.480 | False |
| krikri-8b | dispatch | origin | local_migrant | 90 | 15 | 0.167 | 0.044 | 0.300 | 0.007 | 0.211 | 0.122 | 0.311 | tested |  | 0.122 | 0.089 | 0.133 | False |
| krikri-8b | dispatch | origin | romanian | 90 | 15 | 0.156 | 0.033 | 0.300 | 0.014 | 0.200 | 0.122 | 0.289 | tested |  | 0.122 | 0.078 | 0.238 | False |
| krikri-8b | dispatch | origin | syrian | 90 | 15 | 0.056 | -0.067 | 0.200 | 0.510 | 0.200 | 0.133 | 0.256 | tested |  | 0.122 | 0.078 | 1.000 | False |
| krikri-8b | dispatch | status | asylum_seeker | 90 | 15 | 0.600 | 0.322 | 0.933 | 0.000 | 0.433 | 0.311 | 0.556 | tested |  | 0.122 | 0.311 | 0.000 | True |
| krikri-8b | dispatch | status | seasonal_worker | 90 | 15 | 0.056 | -0.067 | 0.178 | 0.447 | 0.244 | 0.167 | 0.356 | tested |  | 0.122 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.267 | 0.900 |  | 0.433 | 0.200 | 0.667 | descriptive (fewer than 8 cases) |  | 0.044 | 0.389 |  | False |
| krikri-8b | evacuation | area | social_housing | 90 | 15 | 0.411 | 0.222 | 0.622 | 0.000 | 0.333 | 0.178 | 0.489 | tested |  | 0.044 | 0.289 | 0.000 | True |
| krikri-8b | evacuation | area | villas | 90 | 15 | -0.567 | -0.789 | -0.356 | 0.000 | 0.411 | 0.278 | 0.556 | tested |  | 0.044 | 0.367 | 0.000 | True |
| krikri-8b | evacuation | origin | any_minority | 270 | 15 | 0.226 | 0.078 | 0.396 | 0.001 | 0.230 | 0.141 | 0.322 | tested |  | 0.044 | 0.185 | 0.022 | True |
| krikri-8b | evacuation | origin | local_migrant | 90 | 15 | 0.122 | -0.033 | 0.311 | 0.160 | 0.167 | 0.067 | 0.278 | tested |  | 0.044 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | origin | romanian | 90 | 15 | 0.078 | -0.044 | 0.222 | 0.296 | 0.167 | 0.111 | 0.234 | tested |  | 0.044 | 0.122 | 1.000 | False |
| krikri-8b | evacuation | origin | syrian | 90 | 15 | 0.478 | 0.266 | 0.689 | 0.000 | 0.356 | 0.211 | 0.500 | tested |  | 0.044 | 0.311 | 0.000 | True |
| krikri-8b | housing | area | roma_settlement | 30 | 5 | 0.267 | 0.067 | 0.567 |  | 0.300 | 0.100 | 0.533 | descriptive (fewer than 8 cases) | 0.000 | 0.144 | 0.156 |  | False |
| krikri-8b | housing | area | social_housing | 90 | 15 | 0.156 | 0.078 | 0.233 | 0.000 | 0.178 | 0.111 | 0.256 | tested | 0.000 | 0.144 | 0.033 | 0.000 | False |
| krikri-8b | housing | area | villas | 90 | 15 | -1.156 | -1.478 | -0.844 | 0.000 | 0.711 | 0.578 | 0.844 | tested | 0.000 | 0.144 | 0.567 | 0.000 | True |
| krikri-8b | housing | gender | female | 90 | 15 | 0.078 | 0.022 | 0.133 | 0.011 | 0.144 | 0.078 | 0.222 | tested | 0.000 | 0.144 | 0.000 | 0.198 | False |
| krikri-8b | housing | origin | any_minority | 270 | 15 | 0.074 | -0.004 | 0.156 | 0.076 | 0.159 | 0.115 | 0.211 | tested | 0.000 | 0.144 | 0.015 | 0.988 | False |
| krikri-8b | housing | origin | local_migrant | 90 | 15 | 0.044 | -0.033 | 0.122 | 0.358 | 0.133 | 0.078 | 0.189 | tested | 0.000 | 0.144 | -0.011 | 1.000 | False |
| krikri-8b | housing | origin | romanian | 90 | 15 | 0.000 | -0.078 | 0.078 | 1.000 | 0.111 | 0.056 | 0.167 | tested | 0.000 | 0.144 | -0.033 | 1.000 | False |
| krikri-8b | housing | origin | syrian | 90 | 15 | 0.178 | 0.067 | 0.311 | 0.001 | 0.233 | 0.144 | 0.344 | tested | 0.000 | 0.144 | 0.089 | 0.022 | True |
| krikri-8b | housing | status | asylum_seeker | 90 | 15 | 0.100 | 0.000 | 0.222 | 0.057 | 0.200 | 0.122 | 0.300 | tested | 0.000 | 0.144 | 0.056 | 0.798 | False |
| krikri-8b | housing | status | seasonal_worker | 90 | 15 | -0.544 | -0.644 | -0.444 | 0.000 | 0.456 | 0.378 | 0.533 | tested | 0.000 | 0.144 | 0.311 | 0.000 | True |
| krikri-8b | relief | area | roma_settlement | 30 | 5 | -1.233 | -2.733 | -0.300 |  | 0.367 | 0.167 | 0.534 | descriptive (fewer than 8 cases) |  | 0.203 | 0.164 |  | False |
| krikri-8b | relief | area | social_housing | 77 | 15 | 0.929 | 0.308 | 1.623 | 0.001 | 0.364 | 0.270 | 0.450 | tested |  | 0.203 | 0.161 | 0.022 | True |
| krikri-8b | relief | area | villas | 71 | 15 | -2.620 | -3.630 | -1.692 | 0.000 | 0.394 | 0.268 | 0.520 | tested |  | 0.203 | 0.192 | 0.000 | True |
| krikri-8b | relief | origin | any_minority | 229 | 15 | 0.631 | -0.085 | 1.273 | 0.089 | 0.262 | 0.190 | 0.342 | tested |  | 0.203 | 0.059 | 1.000 | False |
| krikri-8b | relief | origin | local_migrant | 76 | 15 | 0.197 | -0.674 | 0.953 | 0.594 | 0.197 | 0.111 | 0.301 | tested |  | 0.203 | -0.005 | 1.000 | False |
| krikri-8b | relief | origin | romanian | 76 | 15 | -0.197 | -1.107 | 0.575 | 0.705 | 0.184 | 0.107 | 0.270 | tested |  | 0.203 | -0.018 | 1.000 | False |
| krikri-8b | relief | origin | syrian | 77 | 15 | 1.877 | 0.887 | 2.809 | 0.000 | 0.403 | 0.296 | 0.506 | tested |  | 0.203 | 0.200 | 0.000 | True |
| krikri-8b | triage | origin | any_minority | 262 | 15 | 0.122 | 0.030 | 0.212 | 0.014 | 0.176 | 0.114 | 0.246 | tested |  | 0.149 | 0.026 | 0.238 | False |
| krikri-8b | triage | origin | local_migrant | 87 | 15 | 0.046 | -0.046 | 0.136 | 0.404 | 0.126 | 0.047 | 0.209 | tested |  | 0.149 | -0.023 | 1.000 | False |
| krikri-8b | triage | origin | romanian | 87 | 15 | 0.011 | -0.106 | 0.135 | 0.902 | 0.161 | 0.081 | 0.244 | tested |  | 0.149 | 0.011 | 1.000 | False |
| krikri-8b | triage | origin | syrian | 88 | 15 | 0.307 | 0.174 | 0.444 | 0.000 | 0.239 | 0.149 | 0.326 | tested |  | 0.149 | 0.089 | 0.000 | True |
| llama-3.1-8b | dispatch | area | roma_settlement | 23 | 5 | 0.043 | -0.571 | 0.667 |  | 0.348 | 0.211 | 0.435 | descriptive (fewer than 8 cases) |  | 0.162 | 0.186 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 68 | 15 | -0.221 | -0.457 | 0.016 | 0.087 | 0.324 | 0.231 | 0.413 | tested |  | 0.162 | 0.161 | 0.783 | False |
| llama-3.1-8b | dispatch | area | villas | 66 | 15 | -0.636 | -0.964 | -0.348 | 0.000 | 0.424 | 0.277 | 0.563 | tested |  | 0.162 | 0.262 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 74 | 14 | -0.041 | -0.225 | 0.180 | 0.725 | 0.243 | 0.137 | 0.351 | tested |  | 0.162 | 0.081 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 213 | 15 | -0.047 | -0.151 | 0.052 | 0.411 | 0.235 | 0.156 | 0.314 | tested |  | 0.162 | 0.073 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 72 | 15 | -0.097 | -0.294 | 0.075 | 0.355 | 0.250 | 0.155 | 0.342 | tested |  | 0.162 | 0.088 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 72 | 14 | 0.000 | -0.111 | 0.125 | 1.000 | 0.208 | 0.093 | 0.343 | tested |  | 0.162 | 0.046 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 69 | 15 | -0.043 | -0.149 | 0.079 | 0.535 | 0.246 | 0.177 | 0.302 | tested |  | 0.162 | 0.084 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 64 | 14 | 0.109 | -0.145 | 0.355 | 0.431 | 0.406 | 0.295 | 0.507 | tested |  | 0.162 | 0.244 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 72 | 15 | -0.389 | -0.688 | -0.101 | 0.010 | 0.389 | 0.246 | 0.515 | tested |  | 0.162 | 0.227 | 0.140 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.133 | 1.033 |  | 0.367 | 0.133 | 0.567 | descriptive (fewer than 8 cases) |  | 0.113 | 0.254 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 74 | 15 | 0.595 | 0.321 | 0.851 | 0.000 | 0.405 | 0.260 | 0.541 | tested |  | 0.113 | 0.293 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 75 | 15 | -0.453 | -0.714 | -0.208 | 0.000 | 0.387 | 0.244 | 0.520 | tested |  | 0.113 | 0.274 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 225 | 15 | 0.427 | 0.234 | 0.632 | 0.000 | 0.347 | 0.235 | 0.453 | tested |  | 0.113 | 0.234 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 73 | 14 | 0.205 | -0.027 | 0.432 | 0.095 | 0.260 | 0.157 | 0.358 | tested |  | 0.113 | 0.148 | 0.783 | False |
| llama-3.1-8b | evacuation | origin | romanian | 77 | 15 | 0.377 | 0.167 | 0.595 | 0.000 | 0.312 | 0.197 | 0.423 | tested |  | 0.113 | 0.199 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 75 | 15 | 0.693 | 0.486 | 0.905 | 0.000 | 0.467 | 0.329 | 0.590 | tested |  | 0.113 | 0.354 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 1.067 | 0.633 | 1.500 |  | 0.533 | 0.300 | 0.733 | descriptive (fewer than 8 cases) | 0.000 | 0.519 | 0.014 |  | False |
| llama-3.1-8b | housing | area | social_housing | 79 | 15 | 0.418 | 0.141 | 0.763 | 0.004 | 0.544 | 0.442 | 0.651 | tested | 0.000 | 0.519 | 0.025 | 0.060 | False |
| llama-3.1-8b | housing | area | villas | 81 | 15 | -1.679 | -2.048 | -1.325 | 0.000 | 0.765 | 0.675 | 0.854 | tested | 0.000 | 0.519 | 0.246 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 80 | 15 | 0.475 | 0.187 | 0.855 | 0.000 | 0.512 | 0.390 | 0.657 | tested | 0.000 | 0.519 | -0.007 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 228 | 15 | 0.329 | 0.167 | 0.478 | 0.000 | 0.478 | 0.403 | 0.553 | tested | 0.000 | 0.519 | -0.041 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 76 | 15 | 0.197 | 0.013 | 0.378 | 0.048 | 0.474 | 0.400 | 0.543 | tested | 0.000 | 0.519 | -0.046 | 0.480 | False |
| llama-3.1-8b | housing | origin | romanian | 75 | 15 | 0.293 | 0.057 | 0.506 | 0.020 | 0.520 | 0.414 | 0.622 | tested | 0.000 | 0.519 | 0.001 | 0.260 | False |
| llama-3.1-8b | housing | origin | syrian | 77 | 15 | 0.494 | 0.234 | 0.775 | 0.000 | 0.442 | 0.321 | 0.553 | tested | 0.000 | 0.519 | -0.078 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 83 | 15 | 0.831 | 0.554 | 1.119 | 0.000 | 0.566 | 0.443 | 0.687 | tested | 0.000 | 0.519 | 0.047 | 0.000 | False |
| llama-3.1-8b | housing | status | seasonal_worker | 77 | 15 | -1.338 | -1.716 | -0.962 | 0.000 | 0.753 | 0.647 | 0.857 | tested | 0.065 | 0.519 | 0.234 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 22 | 5 | 4.591 | 1.588 | 6.882 |  | 0.500 | 0.222 | 0.727 | descriptive (fewer than 8 cases) |  | 0.222 | 0.278 |  | False |
| llama-3.1-8b | relief | area | social_housing | 49 | 15 | 1.857 | 0.758 | 3.050 | 0.001 | 0.469 | 0.356 | 0.560 | tested |  | 0.222 | 0.247 | 0.017 | True |
| llama-3.1-8b | relief | area | villas | 50 | 15 | -2.900 | -5.393 | -1.109 | 0.000 | 0.600 | 0.462 | 0.756 | tested |  | 0.222 | 0.378 | 0.000 | True |
| llama-3.1-8b | relief | origin | any_minority | 148 | 15 | 4.075 | 2.317 | 5.698 | 0.000 | 0.595 | 0.496 | 0.679 | tested |  | 0.222 | 0.372 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 49 | 15 | 3.000 | 0.909 | 5.155 | 0.002 | 0.592 | 0.474 | 0.703 | tested |  | 0.222 | 0.370 | 0.032 | True |
| llama-3.1-8b | relief | origin | romanian | 47 | 13 | 1.662 | -0.468 | 3.532 | 0.135 | 0.532 | 0.388 | 0.660 | tested |  | 0.222 | 0.310 | 0.945 | False |
| llama-3.1-8b | relief | origin | syrian | 52 | 14 | 7.269 | 5.259 | 9.240 | 0.000 | 0.654 | 0.500 | 0.796 | tested |  | 0.222 | 0.432 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 185 | 14 | 0.200 | 0.091 | 0.319 | 0.000 | 0.168 | 0.086 | 0.254 | tested |  | 0.113 | 0.055 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 61 | 14 | 0.115 | 0.015 | 0.222 | 0.043 | 0.148 | 0.059 | 0.245 | tested |  | 0.113 | 0.035 | 0.473 | False |
| llama-3.1-8b | triage | origin | romanian | 63 | 14 | 0.222 | 0.034 | 0.440 | 0.024 | 0.143 | 0.049 | 0.236 | tested |  | 0.113 | 0.030 | 0.288 | False |
| llama-3.1-8b | triage | origin | syrian | 61 | 14 | 0.262 | 0.130 | 0.431 | 0.000 | 0.213 | 0.111 | 0.323 | tested |  | 0.113 | 0.100 | 0.000 | True |
| meltemi-7b | dispatch | area | roma_settlement | 30 | 5 | -0.133 | -0.667 | 0.300 |  | 0.233 | 0.067 | 0.400 | descriptive (fewer than 8 cases) |  | 0.356 | -0.122 |  | False |
| meltemi-7b | dispatch | area | social_housing | 89 | 15 | -0.090 | -0.326 | 0.144 | 0.492 | 0.348 | 0.258 | 0.433 | tested |  | 0.356 | -0.007 | 1.000 | False |
| meltemi-7b | dispatch | area | villas | 90 | 15 | -0.300 | -0.589 | -0.011 | 0.049 | 0.456 | 0.311 | 0.600 | tested |  | 0.356 | 0.100 | 1.000 | False |
| meltemi-7b | dispatch | gender | female | 90 | 15 | -0.156 | -0.389 | 0.067 | 0.197 | 0.367 | 0.289 | 0.456 | tested |  | 0.356 | 0.011 | 1.000 | False |
| meltemi-7b | dispatch | origin | any_minority | 269 | 15 | 0.045 | -0.152 | 0.241 | 0.689 | 0.357 | 0.289 | 0.429 | tested |  | 0.356 | 0.001 | 1.000 | False |
| meltemi-7b | dispatch | origin | local_migrant | 90 | 15 | 0.100 | -0.089 | 0.278 | 0.310 | 0.367 | 0.278 | 0.456 | tested |  | 0.356 | 0.011 | 1.000 | False |
| meltemi-7b | dispatch | origin | romanian | 89 | 15 | -0.011 | -0.273 | 0.250 | 0.969 | 0.371 | 0.258 | 0.494 | tested |  | 0.356 | 0.015 | 1.000 | False |
| meltemi-7b | dispatch | origin | syrian | 90 | 15 | 0.044 | -0.211 | 0.300 | 0.742 | 0.333 | 0.233 | 0.444 | tested |  | 0.356 | -0.022 | 1.000 | False |
| meltemi-7b | dispatch | status | asylum_seeker | 90 | 15 | 0.156 | -0.134 | 0.456 | 0.321 | 0.478 | 0.389 | 0.567 | tested |  | 0.356 | 0.122 | 1.000 | False |
| meltemi-7b | dispatch | status | seasonal_worker | 90 | 15 | 0.078 | -0.211 | 0.356 | 0.615 | 0.433 | 0.356 | 0.511 | tested |  | 0.356 | 0.078 | 1.000 | False |
| meltemi-7b | evacuation | area | roma_settlement | 30 | 5 | 0.433 | 0.000 | 0.800 |  | 0.433 | 0.367 | 0.500 | descriptive (fewer than 8 cases) |  | 0.322 | 0.111 |  | False |
| meltemi-7b | evacuation | area | social_housing | 90 | 15 | -0.022 | -0.233 | 0.233 | 0.823 | 0.378 | 0.289 | 0.456 | tested |  | 0.322 | 0.056 | 1.000 | False |
| meltemi-7b | evacuation | area | villas | 90 | 15 | -0.333 | -0.533 | -0.133 | 0.000 | 0.367 | 0.289 | 0.444 | tested |  | 0.322 | 0.044 | 0.000 | False |
| meltemi-7b | evacuation | origin | any_minority | 270 | 15 | 0.341 | 0.126 | 0.556 | 0.001 | 0.415 | 0.356 | 0.474 | tested |  | 0.322 | 0.093 | 0.027 | True |
| meltemi-7b | evacuation | origin | local_migrant | 90 | 15 | 0.156 | -0.089 | 0.400 | 0.232 | 0.400 | 0.333 | 0.478 | tested |  | 0.322 | 0.078 | 1.000 | False |
| meltemi-7b | evacuation | origin | romanian | 90 | 15 | 0.211 | -0.056 | 0.489 | 0.146 | 0.344 | 0.267 | 0.422 | tested |  | 0.322 | 0.022 | 1.000 | False |
| meltemi-7b | evacuation | origin | syrian | 90 | 15 | 0.656 | 0.444 | 0.867 | 0.000 | 0.500 | 0.400 | 0.600 | tested |  | 0.322 | 0.178 | 0.000 | True |
| meltemi-7b | housing | area | roma_settlement | 30 | 5 | 0.300 | 0.200 | 0.400 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) | 0.000 | 0.456 | -0.022 |  | False |
| meltemi-7b | housing | area | social_housing | 90 | 15 | -0.033 | -0.144 | 0.089 | 0.616 | 0.433 | 0.322 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | area | villas | 90 | 15 | -0.189 | -0.300 | -0.078 | 0.000 | 0.522 | 0.422 | 0.622 | tested | 0.000 | 0.456 | 0.067 | 0.000 | True |
| meltemi-7b | housing | gender | female | 88 | 15 | 0.023 | -0.116 | 0.193 | 0.849 | 0.466 | 0.330 | 0.614 | tested | 0.000 | 0.456 | 0.010 | 1.000 | False |
| meltemi-7b | housing | origin | any_minority | 270 | 15 | 0.052 | -0.048 | 0.141 | 0.297 | 0.463 | 0.385 | 0.541 | tested | 0.000 | 0.456 | 0.007 | 1.000 | False |
| meltemi-7b | housing | origin | local_migrant | 90 | 15 | 0.011 | -0.133 | 0.144 | 0.916 | 0.456 | 0.355 | 0.567 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | romanian | 90 | 15 | -0.022 | -0.167 | 0.111 | 0.860 | 0.522 | 0.444 | 0.600 | tested | 0.000 | 0.456 | 0.067 | 1.000 | False |
| meltemi-7b | housing | origin | syrian | 90 | 15 | 0.167 | 0.067 | 0.267 | 0.001 | 0.411 | 0.322 | 0.511 | tested | 0.000 | 0.456 | -0.044 | 0.027 | False |
| meltemi-7b | housing | status | asylum_seeker | 90 | 15 | 0.100 | -0.078 | 0.278 | 0.316 | 0.433 | 0.311 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | status | seasonal_worker | 90 | 15 | 0.067 | -0.044 | 0.200 | 0.328 | 0.444 | 0.322 | 0.567 | tested | 0.000 | 0.456 | -0.011 | 1.000 | False |
| meltemi-7b | relief | area | roma_settlement | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.750 | -0.750 |  | False |
| meltemi-7b | relief | area | social_housing | 7 | 7 | 0.714 | -3.571 | 5.000 |  | 0.714 | 0.429 | 1.000 | descriptive (fewer than 8 cases) |  | 0.750 | -0.036 |  | False |
| meltemi-7b | relief | area | villas | 6 | 6 | 0.833 | -4.167 | 5.833 |  | 0.500 | 0.167 | 0.833 | descriptive (fewer than 8 cases) |  | 0.750 | -0.250 |  | False |
| meltemi-7b | relief | origin | any_minority | 22 | 11 | 0.682 | -2.402 | 3.750 | 0.676 | 0.591 | 0.346 | 0.833 | tested |  | 0.750 | -0.159 | 1.000 | False |
| meltemi-7b | relief | origin | local_migrant | 7 | 6 | 0.000 | -3.750 | 5.000 |  | 0.714 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.750 | -0.036 |  | False |
| meltemi-7b | relief | origin | romanian | 6 | 6 | 2.500 | -3.333 | 7.500 |  | 0.667 | 0.333 | 1.000 | descriptive (fewer than 8 cases) |  | 0.750 | -0.083 |  | False |
| meltemi-7b | relief | origin | syrian | 9 | 8 | 0.000 | -3.500 | 3.750 | 1.000 | 0.444 | 0.111 | 0.875 | tested |  | 0.750 | -0.306 | 1.000 | False |
| meltemi-7b | triage | origin | any_minority | 229 | 15 | 0.183 | 0.018 | 0.370 | 0.032 | 0.266 | 0.197 | 0.339 | tested |  | 0.232 | 0.034 | 0.768 | False |
| meltemi-7b | triage | origin | local_migrant | 75 | 15 | 0.213 | 0.000 | 0.460 | 0.054 | 0.280 | 0.181 | 0.387 | tested |  | 0.232 | 0.048 | 1.000 | False |
| meltemi-7b | triage | origin | romanian | 75 | 15 | 0.093 | -0.145 | 0.313 | 0.436 | 0.307 | 0.200 | 0.414 | tested |  | 0.232 | 0.075 | 1.000 | False |
| meltemi-7b | triage | origin | syrian | 79 | 15 | 0.241 | 0.059 | 0.417 | 0.014 | 0.215 | 0.144 | 0.293 | tested |  | 0.232 | -0.017 | 0.350 | False |
| qwen2.5-7b | dispatch | area | roma_settlement | 29 | 5 | 0.483 | -0.586 | 1.400 |  | 0.690 | 0.556 | 0.800 | descriptive (fewer than 8 cases) |  | 0.114 | 0.576 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 87 | 15 | -0.103 | -0.529 | 0.217 | 0.673 | 0.402 | 0.270 | 0.542 | tested |  | 0.114 | 0.289 | 1.000 | False |
| qwen2.5-7b | dispatch | area | villas | 87 | 15 | -0.724 | -1.058 | -0.461 | 0.000 | 0.517 | 0.416 | 0.635 | tested |  | 0.114 | 0.404 | 0.000 | True |
| qwen2.5-7b | dispatch | gender | female | 88 | 15 | 0.307 | 0.170 | 0.455 | 0.000 | 0.330 | 0.222 | 0.438 | tested |  | 0.114 | 0.216 | 0.000 | True |
| qwen2.5-7b | dispatch | origin | any_minority | 264 | 15 | 0.072 | 0.000 | 0.148 | 0.053 | 0.193 | 0.136 | 0.244 | tested |  | 0.114 | 0.080 | 0.795 | False |
| qwen2.5-7b | dispatch | origin | local_migrant | 88 | 15 | 0.136 | 0.056 | 0.216 | 0.003 | 0.182 | 0.122 | 0.241 | tested |  | 0.114 | 0.068 | 0.072 | False |
| qwen2.5-7b | dispatch | origin | romanian | 88 | 15 | 0.023 | -0.070 | 0.125 | 0.756 | 0.193 | 0.125 | 0.264 | tested |  | 0.114 | 0.080 | 1.000 | False |
| qwen2.5-7b | dispatch | origin | syrian | 88 | 15 | 0.057 | -0.069 | 0.186 | 0.447 | 0.205 | 0.138 | 0.271 | tested |  | 0.114 | 0.091 | 1.000 | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 88 | 15 | 0.273 | -0.091 | 0.750 | 0.183 | 0.511 | 0.368 | 0.656 | tested |  | 0.114 | 0.398 | 1.000 | False |
| qwen2.5-7b | dispatch | status | seasonal_worker | 88 | 15 | -0.784 | -1.135 | -0.506 | 0.000 | 0.557 | 0.437 | 0.682 | tested |  | 0.114 | 0.443 | 0.000 | True |
| qwen2.5-7b | evacuation | area | roma_settlement | 30 | 5 | 0.867 | 0.233 | 1.500 |  | 0.700 | 0.499 | 0.933 | descriptive (fewer than 8 cases) |  | 0.128 | 0.572 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 87 | 15 | 0.218 | 0.034 | 0.395 | 0.030 | 0.345 | 0.216 | 0.477 | tested |  | 0.128 | 0.217 | 0.510 | False |
| qwen2.5-7b | evacuation | area | villas | 88 | 15 | -0.375 | -0.528 | -0.230 | 0.000 | 0.466 | 0.356 | 0.573 | tested |  | 0.128 | 0.338 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | any_minority | 264 | 15 | 0.242 | 0.119 | 0.379 | 0.000 | 0.284 | 0.176 | 0.401 | tested |  | 0.128 | 0.156 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | local_migrant | 88 | 15 | 0.045 | -0.080 | 0.172 | 0.538 | 0.182 | 0.090 | 0.294 | tested |  | 0.128 | 0.054 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | romanian | 88 | 15 | -0.023 | -0.163 | 0.125 | 0.815 | 0.193 | 0.068 | 0.326 | tested |  | 0.128 | 0.065 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | syrian | 88 | 15 | 0.705 | 0.466 | 0.955 | 0.000 | 0.477 | 0.341 | 0.618 | tested |  | 0.128 | 0.349 | 0.000 | True |
| qwen2.5-7b | housing | area | roma_settlement | 30 | 5 | 0.367 | 0.133 | 0.600 |  | 0.300 | 0.233 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.059 | 0.241 |  | False |
| qwen2.5-7b | housing | area | social_housing | 84 | 15 | 0.095 | 0.022 | 0.182 | 0.019 | 0.143 | 0.070 | 0.225 | tested | 0.000 | 0.059 | 0.084 | 0.380 | False |
| qwen2.5-7b | housing | area | villas | 83 | 15 | -0.157 | -0.284 | -0.036 | 0.007 | 0.133 | 0.051 | 0.217 | tested | 0.024 | 0.059 | 0.074 | 0.154 | False |
| qwen2.5-7b | housing | gender | female | 86 | 15 | 0.070 | 0.000 | 0.143 | 0.058 | 0.093 | 0.035 | 0.165 | tested | 0.000 | 0.059 | 0.034 | 0.812 | False |
| qwen2.5-7b | housing | origin | any_minority | 257 | 15 | 0.039 | -0.004 | 0.087 | 0.106 | 0.093 | 0.052 | 0.135 | tested | 0.000 | 0.059 | 0.035 | 1.000 | False |
| qwen2.5-7b | housing | origin | local_migrant | 84 | 15 | 0.071 | 0.000 | 0.148 | 0.059 | 0.119 | 0.050 | 0.193 | tested | 0.000 | 0.059 | 0.060 | 0.812 | False |
| qwen2.5-7b | housing | origin | romanian | 86 | 15 | 0.047 | 0.012 | 0.090 | 0.019 | 0.070 | 0.023 | 0.125 | tested | 0.000 | 0.059 | 0.011 | 0.380 | False |
| qwen2.5-7b | housing | origin | syrian | 87 | 15 | 0.000 | -0.058 | 0.060 | 1.000 | 0.092 | 0.046 | 0.136 | tested | 0.000 | 0.059 | 0.033 | 1.000 | False |
| qwen2.5-7b | housing | status | asylum_seeker | 87 | 15 | 0.103 | 0.011 | 0.195 | 0.044 | 0.184 | 0.126 | 0.247 | tested | 0.000 | 0.059 | 0.125 | 0.704 | False |
| qwen2.5-7b | housing | status | seasonal_worker | 85 | 15 | -0.482 | -0.679 | -0.307 | 0.000 | 0.341 | 0.203 | 0.477 | tested | 0.071 | 0.059 | 0.282 | 0.000 | True |
| qwen2.5-7b | relief | area | roma_settlement | 30 | 5 | 2.667 | 0.667 | 4.500 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) |  | 0.133 | 0.300 |  | False |
| qwen2.5-7b | relief | area | social_housing | 79 | 15 | 0.063 | -0.974 | 1.026 | 0.929 | 0.329 | 0.192 | 0.494 | tested |  | 0.133 | 0.196 | 1.000 | False |
| qwen2.5-7b | relief | area | villas | 77 | 15 | -2.662 | -3.988 | -1.486 | 0.000 | 0.416 | 0.312 | 0.520 | tested |  | 0.133 | 0.282 | 0.000 | True |
| qwen2.5-7b | relief | origin | any_minority | 226 | 15 | 1.261 | 0.525 | 1.964 | 0.001 | 0.420 | 0.342 | 0.505 | tested |  | 0.133 | 0.287 | 0.025 | True |
| qwen2.5-7b | relief | origin | local_migrant | 78 | 15 | -0.321 | -1.013 | 0.347 | 0.391 | 0.333 | 0.247 | 0.423 | tested |  | 0.133 | 0.200 | 1.000 | False |
| qwen2.5-7b | relief | origin | romanian | 74 | 15 | -0.608 | -1.042 | -0.143 | 0.013 | 0.311 | 0.191 | 0.434 | tested |  | 0.133 | 0.177 | 0.273 | False |
| qwen2.5-7b | relief | origin | syrian | 74 | 15 | 4.797 | 3.355 | 6.191 | 0.000 | 0.622 | 0.479 | 0.756 | tested |  | 0.133 | 0.488 | 0.000 | True |
| qwen2.5-7b | triage | origin | any_minority | 202 | 15 | 0.134 | 0.020 | 0.256 | 0.022 | 0.223 | 0.131 | 0.311 | tested |  | 0.136 | 0.086 | 0.396 | False |
| qwen2.5-7b | triage | origin | local_migrant | 66 | 13 | 0.106 | -0.027 | 0.259 | 0.129 | 0.182 | 0.097 | 0.283 | tested |  | 0.136 | 0.045 | 1.000 | False |
| qwen2.5-7b | triage | origin | romanian | 67 | 13 | 0.075 | -0.030 | 0.203 | 0.214 | 0.209 | 0.099 | 0.329 | tested |  | 0.136 | 0.073 | 1.000 | False |
| qwen2.5-7b | triage | origin | syrian | 69 | 15 | 0.217 | 0.057 | 0.368 | 0.006 | 0.275 | 0.155 | 0.393 | tested |  | 0.136 | 0.139 | 0.138 | False |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | age80 | 59 | 11 | 0.492 | 0.371 | 0.623 | 0.847 | 0.574 | 1.164 |
| apertus-8b | dispatch | dialysis | 57 | 11 | 0.702 | 0.607 | 0.793 | 1.509 | 1.159 | 2.000 |
| apertus-8b | dispatch | infant | 59 | 11 | 0.695 | 0.596 | 0.792 | 1.508 | 1.207 | 1.982 |
| apertus-8b | dispatch | pregnant | 55 | 11 | 0.727 | 0.655 | 0.809 | 1.582 | 1.283 | 1.957 |
| apertus-8b | dispatch | wheelchair | 59 | 13 | 0.746 | 0.646 | 0.865 | 1.593 | 1.203 | 2.118 |
| apertus-8b | evacuation | age80 | 63 | 12 | 0.714 | 0.642 | 0.797 | 1.524 | 1.274 | 1.790 |
| apertus-8b | evacuation | dialysis | 62 | 11 | 0.710 | 0.613 | 0.815 | 1.516 | 1.274 | 1.788 |
| apertus-8b | evacuation | infant | 61 | 11 | 0.672 | 0.554 | 0.788 | 1.443 | 1.118 | 1.742 |
| apertus-8b | evacuation | pregnant | 61 | 11 | 0.721 | 0.639 | 0.803 | 1.475 | 1.229 | 1.689 |
| apertus-8b | evacuation | wheelchair | 61 | 11 | 0.656 | 0.561 | 0.758 | 1.475 | 1.197 | 1.758 |
| apertus-8b | housing | age80 | 60 | 10 | 0.817 | 0.683 | 0.933 | 1.150 | 0.917 | 1.367 |
| apertus-8b | housing | dialysis | 61 | 11 | 0.885 | 0.773 | 0.978 | 1.230 | 1.020 | 1.439 |
| apertus-8b | housing | infant | 60 | 10 | 0.917 | 0.850 | 0.983 | 1.400 | 1.183 | 1.617 |
| apertus-8b | housing | pregnant | 61 | 11 | 0.852 | 0.725 | 0.967 | 1.246 | 0.967 | 1.536 |
| apertus-8b | housing | wheelchair | 61 | 11 | 0.803 | 0.643 | 0.951 | 1.016 | 0.754 | 1.261 |
| apertus-8b | relief | age80 | 61 | 11 | 0.393 | 0.262 | 0.525 | 0.721 | -1.006 | 2.362 |
| apertus-8b | relief | dialysis | 60 | 10 | 0.467 | 0.283 | 0.633 | 1.168 | -1.666 | 3.904 |
| apertus-8b | relief | infant | 60 | 10 | 0.467 | 0.300 | 0.633 | 1.497 | -1.227 | 4.115 |
| apertus-8b | relief | pregnant | 60 | 10 | 0.367 | 0.250 | 0.483 | 0.426 | -2.084 | 2.816 |
| apertus-8b | relief | wheelchair | 60 | 10 | 0.317 | 0.167 | 0.467 | -1.344 | -3.014 | 0.251 |
| apertus-8b | triage | age80 | 33 | 11 | 0.394 | 0.206 | 0.576 | 0.667 | 0.312 | 1.129 |
| apertus-8b | triage | dialysis | 37 | 10 | 0.432 | 0.250 | 0.633 | 0.595 | 0.176 | 1.143 |
| apertus-8b | triage | infant | 33 | 9 | 0.667 | 0.514 | 0.818 | 1.242 | 0.833 | 1.731 |
| apertus-8b | triage | pregnant | 30 | 10 | 0.533 | 0.409 | 0.611 | 0.800 | 0.571 | 1.000 |
| apertus-8b | triage | wheelchair | 33 | 10 | 0.455 | 0.286 | 0.583 | 0.667 | 0.308 | 1.069 |
| krikri-8b | dispatch | age80 | 90 | 15 | 0.700 | 0.544 | 0.856 | 1.478 | 0.967 | 2.000 |
| krikri-8b | dispatch | dialysis | 90 | 15 | 0.833 | 0.711 | 0.944 | 1.878 | 1.311 | 2.444 |
| krikri-8b | dispatch | infant | 90 | 15 | 0.789 | 0.656 | 0.911 | 1.911 | 1.389 | 2.433 |
| krikri-8b | dispatch | pregnant | 90 | 15 | 0.789 | 0.667 | 0.900 | 1.789 | 1.256 | 2.333 |
| krikri-8b | dispatch | wheelchair | 90 | 15 | 0.633 | 0.500 | 0.778 | 1.367 | 0.856 | 1.900 |
| krikri-8b | evacuation | age80 | 90 | 15 | 0.578 | 0.422 | 0.733 | 0.867 | 0.556 | 1.200 |
| krikri-8b | evacuation | dialysis | 90 | 15 | 0.556 | 0.389 | 0.722 | 0.833 | 0.511 | 1.178 |
| krikri-8b | evacuation | infant | 90 | 15 | 0.522 | 0.344 | 0.700 | 0.811 | 0.478 | 1.167 |
| krikri-8b | evacuation | pregnant | 90 | 15 | 0.522 | 0.356 | 0.700 | 0.800 | 0.467 | 1.156 |
| krikri-8b | evacuation | wheelchair | 90 | 15 | 0.489 | 0.333 | 0.644 | 0.733 | 0.433 | 1.044 |
| krikri-8b | housing | age80 | 90 | 15 | 0.556 | 0.422 | 0.678 | 0.611 | 0.422 | 0.800 |
| krikri-8b | housing | dialysis | 90 | 15 | 0.978 | 0.944 | 1.000 | 1.733 | 1.489 | 1.989 |
| krikri-8b | housing | infant | 90 | 15 | 0.933 | 0.844 | 1.000 | 1.256 | 1.044 | 1.500 |
| krikri-8b | housing | pregnant | 90 | 15 | 0.944 | 0.889 | 0.989 | 1.189 | 1.000 | 1.411 |
| krikri-8b | housing | wheelchair | 90 | 15 | 0.533 | 0.400 | 0.656 | 0.600 | 0.411 | 0.822 |
| krikri-8b | relief | age80 | 83 | 15 | 0.602 | 0.488 | 0.709 | 4.190 | 3.067 | 5.292 |
| krikri-8b | relief | dialysis | 84 | 15 | 0.524 | 0.414 | 0.627 | 3.142 | 2.134 | 4.113 |
| krikri-8b | relief | infant | 85 | 15 | 0.529 | 0.395 | 0.651 | 3.156 | 1.593 | 4.809 |
| krikri-8b | relief | pregnant | 84 | 15 | 0.476 | 0.372 | 0.588 | 2.571 | 1.491 | 3.589 |
| krikri-8b | relief | wheelchair | 85 | 15 | 0.376 | 0.264 | 0.500 | 0.846 | -0.506 | 1.972 |
| krikri-8b | triage | age80 | 87 | 15 | 0.322 | 0.233 | 0.411 | 0.437 | 0.333 | 0.534 |
| krikri-8b | triage | dialysis | 87 | 15 | 0.506 | 0.411 | 0.593 | 0.736 | 0.598 | 0.871 |
| krikri-8b | triage | infant | 88 | 15 | 0.523 | 0.414 | 0.621 | 0.761 | 0.584 | 0.931 |
| krikri-8b | triage | pregnant | 88 | 15 | 0.443 | 0.345 | 0.539 | 0.648 | 0.489 | 0.800 |
| krikri-8b | triage | wheelchair | 87 | 15 | 0.264 | 0.167 | 0.364 | 0.345 | 0.209 | 0.483 |
| llama-3.1-8b | dispatch | age80 | 69 | 15 | 0.551 | 0.419 | 0.676 | 0.884 | 0.472 | 1.303 |
| llama-3.1-8b | dispatch | dialysis | 72 | 15 | 0.639 | 0.493 | 0.768 | 1.250 | 0.714 | 1.798 |
| llama-3.1-8b | dispatch | infant | 71 | 14 | 0.648 | 0.516 | 0.773 | 1.197 | 0.676 | 1.743 |
| llama-3.1-8b | dispatch | pregnant | 71 | 15 | 0.648 | 0.500 | 0.775 | 1.239 | 0.776 | 1.720 |
| llama-3.1-8b | dispatch | wheelchair | 70 | 14 | 0.471 | 0.348 | 0.594 | 0.857 | 0.471 | 1.212 |
| llama-3.1-8b | evacuation | age80 | 77 | 15 | 0.623 | 0.432 | 0.789 | 1.000 | 0.676 | 1.333 |
| llama-3.1-8b | evacuation | dialysis | 76 | 15 | 0.632 | 0.487 | 0.758 | 1.000 | 0.769 | 1.239 |
| llama-3.1-8b | evacuation | infant | 74 | 15 | 0.527 | 0.365 | 0.681 | 0.811 | 0.500 | 1.127 |
| llama-3.1-8b | evacuation | pregnant | 77 | 15 | 0.610 | 0.475 | 0.732 | 0.974 | 0.720 | 1.256 |
| llama-3.1-8b | evacuation | wheelchair | 76 | 15 | 0.513 | 0.366 | 0.658 | 0.829 | 0.562 | 1.090 |
| llama-3.1-8b | housing | age80 | 80 | 15 | 0.938 | 0.878 | 0.987 | 2.250 | 2.000 | 2.519 |
| llama-3.1-8b | housing | dialysis | 75 | 15 | 0.987 | 0.958 | 1.000 | 2.733 | 2.500 | 2.986 |
| llama-3.1-8b | housing | infant | 76 | 15 | 1.000 | 1.000 | 1.000 | 2.500 | 2.206 | 2.780 |
| llama-3.1-8b | housing | pregnant | 78 | 15 | 0.974 | 0.932 | 1.000 | 2.372 | 2.114 | 2.632 |
| llama-3.1-8b | housing | wheelchair | 74 | 15 | 0.946 | 0.880 | 1.000 | 2.149 | 1.884 | 2.383 |
| llama-3.1-8b | relief | age80 | 66 | 14 | 0.652 | 0.500 | 0.787 | 6.919 | 3.965 | 9.832 |
| llama-3.1-8b | relief | dialysis | 68 | 15 | 0.618 | 0.492 | 0.733 | 5.240 | 2.878 | 7.606 |
| llama-3.1-8b | relief | infant | 64 | 15 | 0.625 | 0.515 | 0.732 | 4.921 | 3.015 | 6.888 |
| llama-3.1-8b | relief | pregnant | 65 | 15 | 0.631 | 0.493 | 0.758 | 4.431 | 2.604 | 6.074 |
| llama-3.1-8b | relief | wheelchair | 64 | 15 | 0.547 | 0.441 | 0.657 | 2.485 | 1.143 | 3.661 |
| llama-3.1-8b | triage | age80 | 62 | 14 | 0.516 | 0.348 | 0.690 | 0.790 | 0.515 | 1.091 |
| llama-3.1-8b | triage | dialysis | 57 | 13 | 0.421 | 0.294 | 0.588 | 0.544 | 0.293 | 0.893 |
| llama-3.1-8b | triage | infant | 60 | 14 | 0.483 | 0.333 | 0.651 | 0.750 | 0.500 | 1.048 |
| llama-3.1-8b | triage | pregnant | 60 | 13 | 0.533 | 0.362 | 0.723 | 0.833 | 0.571 | 1.151 |
| llama-3.1-8b | triage | wheelchair | 58 | 12 | 0.310 | 0.194 | 0.429 | 0.500 | 0.276 | 0.746 |
| meltemi-7b | dispatch | age80 | 90 | 15 | 0.411 | 0.278 | 0.556 | 0.500 | 0.200 | 0.800 |
| meltemi-7b | dispatch | dialysis | 90 | 15 | 0.478 | 0.344 | 0.622 | 0.744 | 0.400 | 1.089 |
| meltemi-7b | dispatch | infant | 90 | 15 | 0.500 | 0.356 | 0.644 | 0.856 | 0.522 | 1.189 |
| meltemi-7b | dispatch | pregnant | 90 | 15 | 0.467 | 0.333 | 0.611 | 0.789 | 0.511 | 1.067 |
| meltemi-7b | dispatch | wheelchair | 90 | 15 | 0.444 | 0.333 | 0.578 | 0.722 | 0.478 | 0.956 |
| meltemi-7b | evacuation | age80 | 90 | 15 | 0.378 | 0.311 | 0.444 | 0.489 | 0.311 | 0.678 |
| meltemi-7b | evacuation | dialysis | 90 | 15 | 0.422 | 0.333 | 0.511 | 0.556 | 0.389 | 0.733 |
| meltemi-7b | evacuation | infant | 90 | 15 | 0.400 | 0.278 | 0.533 | 0.444 | 0.122 | 0.756 |
| meltemi-7b | evacuation | pregnant | 90 | 15 | 0.478 | 0.367 | 0.578 | 0.589 | 0.311 | 0.856 |
| meltemi-7b | evacuation | wheelchair | 90 | 15 | 0.422 | 0.333 | 0.500 | 0.444 | 0.189 | 0.711 |
| meltemi-7b | housing | age80 | 90 | 15 | 0.356 | 0.256 | 0.467 | 0.433 | 0.322 | 0.533 |
| meltemi-7b | housing | dialysis | 90 | 15 | 0.356 | 0.256 | 0.456 | 0.456 | 0.356 | 0.544 |
| meltemi-7b | housing | infant | 89 | 15 | 0.360 | 0.261 | 0.456 | 0.337 | 0.202 | 0.455 |
| meltemi-7b | housing | pregnant | 90 | 15 | 0.367 | 0.256 | 0.478 | 0.411 | 0.311 | 0.511 |
| meltemi-7b | housing | wheelchair | 90 | 15 | 0.333 | 0.233 | 0.433 | 0.367 | 0.267 | 0.456 |
| meltemi-7b | relief | age80 | 59 | 15 | 0.644 | 0.533 | 0.750 | 8.300 | 4.882 | 11.778 |
| meltemi-7b | relief | dialysis | 64 | 15 | 0.500 | 0.379 | 0.629 | 7.124 | 4.355 | 10.402 |
| meltemi-7b | relief | infant | 63 | 15 | 0.460 | 0.333 | 0.576 | 2.864 | 0.993 | 4.512 |
| meltemi-7b | relief | pregnant | 62 | 15 | 0.484 | 0.328 | 0.644 | 4.976 | 2.351 | 7.616 |
| meltemi-7b | relief | wheelchair | 62 | 15 | 0.500 | 0.381 | 0.590 | 3.203 | 0.699 | 5.590 |
| meltemi-7b | triage | age80 | 74 | 15 | 0.270 | 0.185 | 0.364 | 0.486 | 0.284 | 0.694 |
| meltemi-7b | triage | dialysis | 75 | 15 | 0.360 | 0.260 | 0.456 | 0.547 | 0.221 | 0.853 |
| meltemi-7b | triage | infant | 75 | 15 | 0.347 | 0.227 | 0.464 | 0.493 | 0.181 | 0.760 |
| meltemi-7b | triage | pregnant | 74 | 15 | 0.392 | 0.284 | 0.488 | 0.743 | 0.392 | 1.079 |
| meltemi-7b | triage | wheelchair | 74 | 15 | 0.311 | 0.190 | 0.425 | 0.541 | 0.242 | 0.872 |
| qwen2.5-7b | dispatch | age80 | 88 | 15 | 0.568 | 0.427 | 0.705 | 1.125 | 0.750 | 1.460 |
| qwen2.5-7b | dispatch | dialysis | 88 | 15 | 0.670 | 0.517 | 0.807 | 1.341 | 0.909 | 1.770 |
| qwen2.5-7b | dispatch | infant | 88 | 15 | 0.636 | 0.517 | 0.756 | 1.273 | 0.900 | 1.651 |
| qwen2.5-7b | dispatch | pregnant | 88 | 15 | 0.659 | 0.544 | 0.770 | 1.375 | 1.045 | 1.699 |
| qwen2.5-7b | dispatch | wheelchair | 88 | 15 | 0.523 | 0.409 | 0.628 | 1.011 | 0.667 | 1.333 |
| qwen2.5-7b | evacuation | age80 | 89 | 15 | 0.697 | 0.578 | 0.807 | 1.124 | 0.811 | 1.427 |
| qwen2.5-7b | evacuation | dialysis | 86 | 15 | 0.721 | 0.598 | 0.830 | 1.198 | 0.849 | 1.529 |
| qwen2.5-7b | evacuation | infant | 87 | 15 | 0.690 | 0.568 | 0.816 | 1.149 | 0.807 | 1.500 |
| qwen2.5-7b | evacuation | pregnant | 87 | 15 | 0.667 | 0.545 | 0.788 | 1.126 | 0.775 | 1.477 |
| qwen2.5-7b | evacuation | wheelchair | 89 | 15 | 0.629 | 0.506 | 0.747 | 1.034 | 0.711 | 1.360 |
| qwen2.5-7b | housing | age80 | 85 | 15 | 0.765 | 0.683 | 0.849 | 0.835 | 0.719 | 0.954 |
| qwen2.5-7b | housing | dialysis | 85 | 15 | 0.988 | 0.964 | 1.000 | 1.859 | 1.704 | 2.011 |
| qwen2.5-7b | housing | infant | 83 | 15 | 0.711 | 0.645 | 0.777 | 1.157 | 1.038 | 1.256 |
| qwen2.5-7b | housing | pregnant | 85 | 15 | 1.000 | 1.000 | 1.000 | 1.929 | 1.871 | 1.989 |
| qwen2.5-7b | housing | wheelchair | 85 | 15 | 0.753 | 0.671 | 0.839 | 0.765 | 0.686 | 0.841 |
| qwen2.5-7b | relief | age80 | 75 | 15 | 0.680 | 0.562 | 0.792 | 7.800 | 6.089 | 9.460 |
| qwen2.5-7b | relief | dialysis | 75 | 15 | 0.707 | 0.542 | 0.842 | 8.400 | 6.111 | 10.541 |
| qwen2.5-7b | relief | infant | 76 | 15 | 0.658 | 0.500 | 0.792 | 6.513 | 4.598 | 8.228 |
| qwen2.5-7b | relief | pregnant | 77 | 15 | 0.662 | 0.507 | 0.789 | 7.338 | 5.522 | 8.824 |
| qwen2.5-7b | relief | wheelchair | 73 | 13 | 0.534 | 0.408 | 0.654 | 4.521 | 3.285 | 5.733 |
| qwen2.5-7b | triage | age80 | 65 | 13 | 0.338 | 0.164 | 0.529 | 0.446 | 0.191 | 0.750 |
| qwen2.5-7b | triage | dialysis | 68 | 14 | 0.250 | 0.143 | 0.369 | 0.206 | 0.053 | 0.378 |
| qwen2.5-7b | triage | infant | 69 | 14 | 0.406 | 0.236 | 0.587 | 0.609 | 0.300 | 0.943 |
| qwen2.5-7b | triage | pregnant | 65 | 14 | 0.462 | 0.299 | 0.651 | 0.538 | 0.319 | 0.783 |
| qwen2.5-7b | triage | wheelchair | 66 | 13 | 0.258 | 0.139 | 0.382 | 0.273 | 0.137 | 0.413 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | triage | need=age80 | 44 | 12 | 0.136 |
| apertus-8b | triage | need=pregnant | 43 | 13 | 0.163 |
| apertus-8b | triage | need=dialysis | 48 | 11 | 0.250 |
| apertus-8b | triage | need=wheelchair | 44 | 13 | 0.273 |
| apertus-8b | triage | origin=local_migrant | 39 | 12 | 0.333 |
| apertus-8b | triage | need=infant | 50 | 12 | 0.340 |
| apertus-8b | triage | base | 44 | 12 | 0.386 |
| apertus-8b | triage | origin=syrian | 49 | 15 | 0.388 |
| apertus-8b | triage | origin=romanian | 45 | 14 | 0.422 |
| apertus-8b | triage | placebo | 48 | 13 | 0.500 |
| krikri-8b | triage | need=wheelchair | 87 | 15 | 0.241 |
| krikri-8b | triage | need=age80 | 87 | 15 | 0.287 |
| krikri-8b | triage | need=pregnant | 88 | 15 | 0.386 |
| krikri-8b | triage | need=dialysis | 88 | 15 | 0.443 |
| krikri-8b | triage | origin=syrian | 89 | 15 | 0.461 |
| krikri-8b | triage | need=infant | 89 | 15 | 0.472 |
| krikri-8b | triage | origin=romanian | 87 | 15 | 0.598 |
| krikri-8b | triage | placebo | 87 | 15 | 0.598 |
| krikri-8b | triage | base | 88 | 15 | 0.602 |
| krikri-8b | triage | origin=local_migrant | 88 | 15 | 0.602 |
| llama-3.1-8b | triage | need=dialysis | 66 | 15 | 0.242 |
| llama-3.1-8b | triage | need=wheelchair | 64 | 14 | 0.266 |
| llama-3.1-8b | triage | need=pregnant | 67 | 15 | 0.313 |
| llama-3.1-8b | triage | need=age80 | 72 | 15 | 0.333 |
| llama-3.1-8b | triage | need=infant | 68 | 15 | 0.338 |
| llama-3.1-8b | triage | origin=syrian | 63 | 14 | 0.540 |
| llama-3.1-8b | triage | origin=local_migrant | 70 | 15 | 0.629 |
| llama-3.1-8b | triage | origin=romanian | 69 | 15 | 0.638 |
| llama-3.1-8b | triage | placebo | 69 | 15 | 0.667 |
| llama-3.1-8b | triage | base | 69 | 14 | 0.696 |
| meltemi-7b | triage | need=age80 | 80 | 15 | 0.037 |
| meltemi-7b | triage | origin=syrian | 81 | 15 | 0.049 |
| meltemi-7b | triage | need=wheelchair | 79 | 15 | 0.051 |
| meltemi-7b | triage | need=dialysis | 79 | 15 | 0.063 |
| meltemi-7b | triage | need=infant | 79 | 15 | 0.076 |
| meltemi-7b | triage | base | 84 | 15 | 0.083 |
| meltemi-7b | triage | origin=romanian | 80 | 15 | 0.087 |
| meltemi-7b | triage | need=pregnant | 78 | 15 | 0.090 |
| meltemi-7b | triage | placebo | 73 | 15 | 0.096 |
| meltemi-7b | triage | origin=local_migrant | 81 | 15 | 0.099 |
| qwen2.5-7b | triage | need=dialysis | 75 | 15 | 0.080 |
| qwen2.5-7b | triage | need=wheelchair | 69 | 14 | 0.087 |
| qwen2.5-7b | triage | need=pregnant | 70 | 15 | 0.100 |
| qwen2.5-7b | triage | need=age80 | 69 | 14 | 0.145 |
| qwen2.5-7b | triage | need=infant | 74 | 15 | 0.203 |
| qwen2.5-7b | triage | origin=romanian | 71 | 15 | 0.592 |
| qwen2.5-7b | triage | base | 74 | 15 | 0.622 |
| qwen2.5-7b | triage | origin=syrian | 76 | 15 | 0.632 |
| qwen2.5-7b | triage | origin=local_migrant | 72 | 13 | 0.639 |
| qwen2.5-7b | triage | placebo | 73 | 15 | 0.671 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el | kendall_w | 0.672 | 12 | 21 |
| apertus-8b | dispatch | en | kendall_w | 0.486 | 13 | 24 |
| apertus-8b | dispatch | fr | kendall_w | 0.455 | 12 | 23 |
| apertus-8b | evacuation | el | kendall_w | 0.570 | 10 | 20 |
| apertus-8b | evacuation | en | kendall_w | 0.420 | 11 | 21 |
| apertus-8b | evacuation | fr | kendall_w | 0.364 | 12 | 23 |
| apertus-8b | housing | el | krippendorff_alpha | 0.667 | 10 | 20 |
| apertus-8b | housing | en | krippendorff_alpha | 0.632 | 12 | 22 |
| apertus-8b | housing | fr | krippendorff_alpha | 0.568 | 12 | 22 |
| apertus-8b | relief | el | krippendorff_alpha | 0.546 | 12 | 23 |
| apertus-8b | relief | en | krippendorff_alpha | 0.467 | 11 | 21 |
| apertus-8b | relief | fr | krippendorff_alpha | 0.462 | 10 | 20 |
| apertus-8b | triage | el | kendall_w | 0.630 | 9 | 14 |
| apertus-8b | triage | en | kendall_w | 0.883 | 10 | 19 |
| apertus-8b | triage | fr | kendall_w | 0.775 | 9 | 11 |
| krikri-8b | dispatch | el | kendall_w | 0.777 | 15 | 30 |
| krikri-8b | dispatch | en | kendall_w | 0.723 | 15 | 30 |
| krikri-8b | dispatch | fr | kendall_w | 0.667 | 15 | 30 |
| krikri-8b | evacuation | el | kendall_w | 0.773 | 15 | 30 |
| krikri-8b | evacuation | en | kendall_w | 0.713 | 15 | 30 |
| krikri-8b | evacuation | fr | kendall_w | 0.653 | 15 | 30 |
| krikri-8b | housing | el | krippendorff_alpha | 0.878 | 15 | 30 |
| krikri-8b | housing | en | krippendorff_alpha | 1.000 | 15 | 30 |
| krikri-8b | housing | fr | krippendorff_alpha | 0.744 | 15 | 30 |
| krikri-8b | relief | el | krippendorff_alpha | 0.528 | 15 | 29 |
| krikri-8b | relief | en | krippendorff_alpha | 0.540 | 15 | 28 |
| krikri-8b | relief | fr | krippendorff_alpha | 0.364 | 15 | 28 |
| krikri-8b | triage | el | kendall_w | 0.920 | 15 | 30 |
| krikri-8b | triage | en | kendall_w | 0.910 | 15 | 30 |
| krikri-8b | triage | fr | kendall_w | 0.908 | 15 | 28 |
| llama-3.1-8b | dispatch | el | kendall_w | 0.612 | 15 | 27 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.654 | 14 | 26 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.630 | 14 | 24 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.554 | 15 | 28 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.650 | 15 | 27 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.736 | 15 | 29 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.493 | 15 | 27 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.649 | 15 | 29 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | -0.384 | 15 | 29 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.427 | 15 | 28 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.545 | 15 | 24 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.413 | 12 | 21 |
| llama-3.1-8b | triage | el | kendall_w | 0.783 | 12 | 21 |
| llama-3.1-8b | triage | en | kendall_w | 0.850 | 14 | 25 |
| llama-3.1-8b | triage | fr | kendall_w | 0.905 | 13 | 23 |
| meltemi-7b | dispatch | el | kendall_w | 0.510 | 15 | 30 |
| meltemi-7b | dispatch | en | kendall_w | 0.447 | 15 | 30 |
| meltemi-7b | dispatch | fr | kendall_w | 0.493 | 15 | 30 |
| meltemi-7b | evacuation | el | kendall_w | 0.467 | 15 | 30 |
| meltemi-7b | evacuation | en | kendall_w | 0.560 | 15 | 30 |
| meltemi-7b | evacuation | fr | kendall_w | 0.480 | 15 | 30 |
| meltemi-7b | housing | el | krippendorff_alpha | 0.341 | 15 | 30 |
| meltemi-7b | housing | en | krippendorff_alpha | 0.099 | 15 | 30 |
| meltemi-7b | housing | fr | krippendorff_alpha | -0.278 | 15 | 30 |
| meltemi-7b | relief | el | krippendorff_alpha | 0.574 | 15 | 29 |
| meltemi-7b | relief | en | krippendorff_alpha | 0.443 | 15 | 30 |
| meltemi-7b | relief | fr | krippendorff_alpha | 0.437 | 12 | 15 |
| meltemi-7b | triage | el | kendall_w | 0.486 | 15 | 29 |
| meltemi-7b | triage | en | kendall_w | 0.633 | 14 | 26 |
| meltemi-7b | triage | fr | kendall_w | 0.554 | 15 | 29 |
| qwen2.5-7b | dispatch | el | kendall_w | 0.607 | 15 | 30 |
| qwen2.5-7b | dispatch | en | kendall_w | 0.823 | 15 | 28 |
| qwen2.5-7b | dispatch | fr | kendall_w | 0.780 | 15 | 30 |
| qwen2.5-7b | evacuation | el | kendall_w | 0.640 | 15 | 30 |
| qwen2.5-7b | evacuation | en | kendall_w | 0.879 | 15 | 29 |
| qwen2.5-7b | evacuation | fr | kendall_w | 0.913 | 15 | 30 |
| qwen2.5-7b | housing | el | krippendorff_alpha | 0.000 | 15 | 30 |
| qwen2.5-7b | housing | en | krippendorff_alpha | 1.000 | 15 | 29 |
| qwen2.5-7b | housing | fr | krippendorff_alpha | 0.833 | 15 | 28 |
| qwen2.5-7b | relief | el | krippendorff_alpha | 0.415 | 15 | 27 |
| qwen2.5-7b | relief | en | krippendorff_alpha | 0.440 | 15 | 28 |
| qwen2.5-7b | relief | fr | krippendorff_alpha | 0.209 | 13 | 26 |
| qwen2.5-7b | triage | el | kendall_w | 0.685 | 12 | 22 |
| qwen2.5-7b | triage | en | kendall_w | 0.962 | 14 | 26 |
| qwen2.5-7b | triage | fr | kendall_w | 0.904 | 14 | 26 |

## Cross-lingual consistency of the base cases

| model | task | pair | cases | difference | lo | hi | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el-en | 12 | 0.000 | -0.875 | 0.959 | 0.997 |
| apertus-8b | dispatch | el-fr | 11 | 0.182 | -0.547 | 0.955 | 0.674 |
| apertus-8b | dispatch | en-fr | 12 | 0.083 | -0.500 | 0.708 | 0.819 |
| apertus-8b | evacuation | el-en | 10 | -0.100 | -0.750 | 0.601 | 0.849 |
| apertus-8b | evacuation | el-fr | 10 | -0.350 | -0.950 | 0.150 | 0.244 |
| apertus-8b | evacuation | en-fr | 11 | -0.182 | -0.864 | 0.409 | 0.670 |
| apertus-8b | housing | el-en | 10 | 0.100 | -0.100 | 0.300 | 0.403 |
| apertus-8b | housing | el-fr | 10 | 0.550 | 0.150 | 0.950 | 0.011 |
| apertus-8b | housing | en-fr | 11 | 0.591 | 0.182 | 1.001 | 0.006 |
| apertus-8b | relief | el-en | 10 | -1.333 | -5.084 | 2.819 | 0.486 |
| apertus-8b | relief | el-fr | 10 | -1.376 | -3.702 | 0.829 | 0.239 |
| apertus-8b | relief | en-fr | 10 | -0.043 | -2.955 | 2.578 | 1.000 |
| apertus-8b | triage | el-en | 8 | -0.375 | -1.312 | 0.438 | 0.444 |
| apertus-8b | triage | el-fr | 7 | -0.714 | -1.359 | -0.071 | 0.044 |
| apertus-8b | triage | en-fr | 7 | -0.214 | -1.143 | 0.929 | 0.714 |
| krikri-8b | dispatch | el-en | 15 | -0.067 | -0.267 | 0.167 | 0.658 |
| krikri-8b | dispatch | el-fr | 15 | 0.033 | -0.167 | 0.267 | 0.906 |
| krikri-8b | dispatch | en-fr | 15 | 0.100 | -0.133 | 0.333 | 0.505 |
| krikri-8b | evacuation | el-en | 15 | -0.167 | -0.367 | 0.067 | 0.177 |
| krikri-8b | evacuation | el-fr | 15 | -0.200 | -0.433 | 0.033 | 0.136 |
| krikri-8b | evacuation | en-fr | 15 | -0.033 | -0.200 | 0.133 | 0.867 |
| krikri-8b | housing | el-en | 15 | -0.200 | -0.400 | -0.033 | 0.023 |
| krikri-8b | housing | el-fr | 15 | 0.267 | 0.067 | 0.467 | 0.018 |
| krikri-8b | housing | en-fr | 15 | 0.467 | 0.200 | 0.800 | 0.001 |
| krikri-8b | relief | el-en | 15 | 0.912 | -1.344 | 3.504 | 0.458 |
| krikri-8b | relief | el-fr | 15 | -1.062 | -2.423 | 0.387 | 0.153 |
| krikri-8b | relief | en-fr | 15 | -1.974 | -4.182 | 0.174 | 0.071 |
| krikri-8b | triage | el-en | 15 | 0.000 | -0.167 | 0.200 | 1.000 |
| krikri-8b | triage | el-fr | 15 | 0.033 | -0.100 | 0.167 | 0.786 |
| krikri-8b | triage | en-fr | 15 | 0.033 | -0.133 | 0.200 | 0.822 |
| llama-3.1-8b | dispatch | el-en | 14 | 0.643 | 0.071 | 1.286 | 0.026 |
| llama-3.1-8b | dispatch | el-fr | 14 | 0.714 | 0.071 | 1.357 | 0.025 |
| llama-3.1-8b | dispatch | en-fr | 14 | 0.071 | -0.357 | 0.429 | 0.787 |
| llama-3.1-8b | evacuation | el-en | 15 | 0.000 | -0.300 | 0.333 | 1.000 |
| llama-3.1-8b | evacuation | el-fr | 15 | 0.233 | -0.134 | 0.567 | 0.228 |
| llama-3.1-8b | evacuation | en-fr | 15 | 0.233 | -0.033 | 0.467 | 0.095 |
| llama-3.1-8b | housing | el-en | 15 | 0.133 | -0.433 | 0.733 | 0.714 |
| llama-3.1-8b | housing | el-fr | 15 | 2.500 | 1.933 | 3.067 | 0.000 |
| llama-3.1-8b | housing | en-fr | 15 | 2.367 | 1.700 | 3.000 | 0.000 |
| llama-3.1-8b | relief | el-en | 15 | 1.113 | -3.020 | 5.860 | 0.657 |
| llama-3.1-8b | relief | el-fr | 12 | -0.282 | -2.991 | 2.793 | 0.811 |
| llama-3.1-8b | relief | en-fr | 12 | -2.715 | -7.040 | 1.153 | 0.189 |
| llama-3.1-8b | triage | el-en | 12 | -0.292 | -0.667 | 0.000 | 0.069 |
| llama-3.1-8b | triage | el-fr | 12 | -0.500 | -1.083 | -0.125 | 0.002 |
| llama-3.1-8b | triage | en-fr | 13 | -0.231 | -0.423 | -0.077 | 0.002 |
| meltemi-7b | dispatch | el-en | 15 | -0.033 | -0.534 | 0.433 | 0.931 |
| meltemi-7b | dispatch | el-fr | 15 | -0.333 | -1.133 | 0.367 | 0.418 |
| meltemi-7b | dispatch | en-fr | 15 | -0.300 | -1.233 | 0.567 | 0.554 |
| meltemi-7b | evacuation | el-en | 15 | 0.500 | 0.267 | 0.733 | 0.000 |
| meltemi-7b | evacuation | el-fr | 15 | 0.333 | -0.067 | 0.733 | 0.115 |
| meltemi-7b | evacuation | en-fr | 15 | -0.167 | -0.567 | 0.267 | 0.487 |
| meltemi-7b | housing | el-en | 15 | -0.033 | -0.167 | 0.100 | 0.794 |
| meltemi-7b | housing | el-fr | 15 | 0.700 | 0.300 | 1.067 | 0.002 |
| meltemi-7b | housing | en-fr | 15 | 0.733 | 0.400 | 1.067 | 0.001 |
| meltemi-7b | relief | el-en | 15 | -0.327 | -3.841 | 2.598 | 0.839 |
| meltemi-7b | relief | el-fr | 12 | -0.495 | -2.885 | 2.429 | 0.639 |
| meltemi-7b | relief | en-fr | 12 | 0.643 | -3.858 | 5.133 | 0.831 |
| meltemi-7b | triage | el-en | 14 | -0.107 | -0.357 | 0.143 | 0.504 |
| meltemi-7b | triage | el-fr | 15 | 0.100 | -0.333 | 0.500 | 0.673 |
| meltemi-7b | triage | en-fr | 14 | 0.357 | -0.071 | 0.786 | 0.117 |
| qwen2.5-7b | dispatch | el-en | 15 | -0.200 | -0.500 | 0.067 | 0.194 |
| qwen2.5-7b | dispatch | el-fr | 15 | 0.133 | -0.200 | 0.500 | 0.507 |
| qwen2.5-7b | dispatch | en-fr | 15 | 0.333 | -0.033 | 0.733 | 0.100 |
| qwen2.5-7b | evacuation | el-en | 15 | 0.300 | -0.033 | 0.600 | 0.085 |
| qwen2.5-7b | evacuation | el-fr | 15 | 0.100 | -0.200 | 0.400 | 0.562 |
| qwen2.5-7b | evacuation | en-fr | 15 | -0.200 | -0.333 | -0.033 | 0.025 |
| qwen2.5-7b | housing | el-en | 15 | -0.100 | -0.267 | 0.000 | 0.229 |
| qwen2.5-7b | housing | el-fr | 15 | -0.633 | -0.967 | -0.333 | 0.000 |
| qwen2.5-7b | housing | en-fr | 15 | -0.533 | -0.867 | -0.267 | 0.000 |
| qwen2.5-7b | relief | el-en | 15 | 1.500 | -1.500 | 4.833 | 0.375 |
| qwen2.5-7b | relief | el-fr | 13 | 2.308 | -0.577 | 5.000 | 0.117 |
| qwen2.5-7b | relief | en-fr | 13 | 1.538 | 0.000 | 3.269 | 0.062 |
| qwen2.5-7b | triage | el-en | 12 | -0.208 | -0.583 | 0.167 | 0.334 |
| qwen2.5-7b | triage | el-fr | 12 | -0.042 | -0.333 | 0.250 | 0.905 |
| qwen2.5-7b | triage | en-fr | 13 | 0.154 | -0.077 | 0.385 | 0.272 |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | ambiguous | 17 | 3 | 1.235 | 0.800 | 1.500 |  | 0.588 | 0.400 | 0.833 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.400 | 0.250 | 0.500 |  | 0.700 | 0.667 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | social_housing | ambiguous | 39 | 8 | 0.205 | -0.174 | 0.771 | 0.423 | 0.333 | 0.186 | 0.447 | tested |  |
| apertus-8b | dispatch | area | social_housing | clear | 23 | 4 | 0.043 | -0.182 | 0.250 |  | 0.609 | 0.333 | 0.792 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | villas | ambiguous | 36 | 7 | -0.556 | -1.027 | -0.205 |  | 0.556 | 0.415 | 0.724 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | villas | clear | 23 | 4 | -0.565 | -0.952 | -0.250 |  | 0.565 | 0.417 | 0.727 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | gender | female | ambiguous | 37 | 7 | 0.405 | -0.026 | 0.921 |  | 0.514 | 0.351 | 0.676 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | gender | female | clear | 23 | 4 | 0.217 | 0.000 | 0.455 |  | 0.565 | 0.375 | 0.857 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | any_minority | ambiguous | 113 | 8 | 0.177 | -0.053 | 0.454 | 0.156 | 0.469 | 0.323 | 0.594 | tested |  |
| apertus-8b | dispatch | origin | any_minority | clear | 70 | 4 | -0.229 | -0.486 | 0.056 |  | 0.543 | 0.362 | 0.739 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | local_migrant | ambiguous | 38 | 8 | 0.105 | -0.233 | 0.452 | 0.628 | 0.395 | 0.286 | 0.476 | tested |  |
| apertus-8b | dispatch | origin | local_migrant | clear | 24 | 4 | -0.083 | -0.250 | 0.083 |  | 0.542 | 0.292 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | romanian | ambiguous | 39 | 8 | 0.128 | -0.054 | 0.311 | 0.235 | 0.513 | 0.286 | 0.682 | tested |  |
| apertus-8b | dispatch | origin | romanian | clear | 24 | 4 | -0.292 | -0.667 | 0.208 |  | 0.583 | 0.417 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | syrian | ambiguous | 36 | 8 | 0.306 | -0.071 | 0.730 | 0.135 | 0.500 | 0.289 | 0.707 | tested |  |
| apertus-8b | dispatch | origin | syrian | clear | 22 | 4 | -0.318 | -0.727 | 0.091 |  | 0.500 | 0.364 | 0.700 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | asylum_seeker | ambiguous | 37 | 8 | 1.324 | 0.833 | 1.973 | 0.000 | 0.649 | 0.512 | 0.784 | tested |  |
| apertus-8b | dispatch | status | asylum_seeker | clear | 22 | 4 | -0.182 | -0.619 | 0.208 |  | 0.545 | 0.333 | 0.727 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | seasonal_worker | ambiguous | 40 | 9 | 0.075 | -0.238 | 0.432 | 0.724 | 0.425 | 0.216 | 0.605 | tested |  |
| apertus-8b | dispatch | status | seasonal_worker | clear | 23 | 4 | -0.304 | -0.636 | 0.000 |  | 0.609 | 0.304 | 0.818 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 1.167 | 1.000 | 1.333 |  | 0.556 | 0.500 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.583 | 0.333 | 0.833 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | social_housing | ambiguous | 37 | 7 | 0.622 | 0.333 | 0.977 |  | 0.378 | 0.216 | 0.548 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | social_housing | clear | 24 | 4 | 0.542 | 0.167 | 1.042 |  | 0.458 | 0.375 | 0.500 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | villas | ambiguous | 38 | 7 | -0.342 | -0.524 | -0.147 |  | 0.395 | 0.262 | 0.530 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | villas | clear | 24 | 4 | -0.625 | -0.875 | -0.500 |  | 0.417 | 0.208 | 0.708 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | any_minority | ambiguous | 109 | 7 | 0.431 | 0.076 | 0.817 |  | 0.394 | 0.246 | 0.523 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | any_minority | clear | 72 | 4 | -0.028 | -0.056 | 0.028 |  | 0.403 | 0.222 | 0.556 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | local_migrant | ambiguous | 37 | 7 | 0.297 | -0.062 | 0.688 |  | 0.324 | 0.143 | 0.500 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | local_migrant | clear | 24 | 4 | -0.208 | -0.583 | 0.167 |  | 0.333 | 0.125 | 0.500 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | romanian | ambiguous | 36 | 6 | 0.167 | -0.278 | 0.528 |  | 0.361 | 0.222 | 0.500 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | romanian | clear | 24 | 4 | -0.375 | -0.500 | -0.250 |  | 0.333 | 0.208 | 0.458 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | syrian | ambiguous | 36 | 6 | 0.833 | 0.389 | 1.278 |  | 0.500 | 0.306 | 0.639 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | syrian | clear | 24 | 4 | 0.500 | 0.250 | 0.833 |  | 0.542 | 0.292 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.944 | 0.833 | 1.000 |  | 0.667 | 0.500 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | roma_settlement | clear | 12 | 2 | 0.833 | 0.833 | 0.833 |  | 0.750 | 0.667 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | social_housing | ambiguous | 36 | 6 | 0.278 | 0.111 | 0.472 |  | 0.306 | 0.139 | 0.444 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | social_housing | clear | 25 | 5 | 0.280 | 0.167 | 0.467 |  | 0.320 | 0.200 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | villas | ambiguous | 37 | 7 | -0.243 | -0.541 | 0.000 |  | 0.676 | 0.514 | 0.844 | descriptive (fewer than 8 cases) | 0.027 |
| apertus-8b | housing | area | villas | clear | 24 | 4 | 0.000 | -0.208 | 0.167 |  | 0.500 | 0.375 | 0.625 | descriptive (fewer than 8 cases) | 0.083 |
| apertus-8b | housing | gender | female | ambiguous | 37 | 7 | 0.432 | 0.297 | 0.625 |  | 0.514 | 0.405 | 0.625 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | gender | female | clear | 25 | 5 | 0.480 | 0.240 | 0.840 |  | 0.680 | 0.567 | 0.800 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | any_minority | ambiguous | 111 | 8 | 0.252 | 0.074 | 0.442 | 0.002 | 0.423 | 0.312 | 0.505 | tested | 0.000 |
| apertus-8b | housing | origin | any_minority | clear | 74 | 5 | 0.338 | 0.216 | 0.500 |  | 0.446 | 0.365 | 0.571 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | local_migrant | ambiguous | 37 | 7 | 0.297 | 0.048 | 0.562 |  | 0.459 | 0.312 | 0.622 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | local_migrant | clear | 25 | 5 | 0.240 | 0.033 | 0.467 |  | 0.360 | 0.240 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | romanian | ambiguous | 37 | 7 | 0.108 | -0.143 | 0.405 |  | 0.432 | 0.216 | 0.622 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | romanian | clear | 25 | 5 | 0.400 | 0.267 | 0.550 |  | 0.560 | 0.500 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | syrian | ambiguous | 37 | 7 | 0.351 | 0.216 | 0.500 |  | 0.378 | 0.250 | 0.514 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | syrian | clear | 24 | 4 | 0.375 | 0.208 | 0.583 |  | 0.417 | 0.250 | 0.583 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | asylum_seeker | ambiguous | 36 | 6 | 0.583 | 0.389 | 0.778 |  | 0.583 | 0.444 | 0.750 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | asylum_seeker | clear | 24 | 4 | 0.417 | 0.042 | 0.750 |  | 0.458 | 0.250 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | seasonal_worker | ambiguous | 36 | 6 | -0.222 | -0.278 | -0.167 |  | 0.417 | 0.278 | 0.556 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | seasonal_worker | clear | 24 | 4 | -0.167 | -0.292 | -0.042 |  | 0.625 | 0.417 | 0.792 | descriptive (fewer than 8 cases) | 0.042 |
| apertus-8b | relief | area | roma_settlement | ambiguous | 18 | 3 | -1.902 | -3.833 | 1.712 |  | 0.389 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | roma_settlement | clear | 12 | 2 | -1.944 | -3.333 | -0.556 |  | 0.583 | 0.500 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | social_housing | ambiguous | 36 | 6 | -1.130 | -4.000 | 0.990 |  | 0.472 | 0.278 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | social_housing | clear | 25 | 5 | -0.988 | -2.992 | 0.394 |  | 0.400 | 0.240 | 0.600 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | villas | ambiguous | 37 | 7 | -1.571 | -4.168 | 0.631 |  | 0.405 | 0.214 | 0.625 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | villas | clear | 25 | 5 | -1.182 | -4.932 | 0.801 |  | 0.520 | 0.400 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | any_minority | ambiguous | 110 | 8 | -0.263 | -3.357 | 3.652 | 0.828 | 0.509 | 0.327 | 0.717 | tested |  |
| apertus-8b | relief | origin | any_minority | clear | 74 | 5 | -1.585 | -4.708 | 1.586 |  | 0.527 | 0.422 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | local_migrant | ambiguous | 37 | 7 | -1.547 | -5.568 | 2.464 |  | 0.514 | 0.333 | 0.704 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | local_migrant | clear | 25 | 5 | -2.515 | -4.917 | -0.134 |  | 0.480 | 0.360 | 0.640 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | romanian | ambiguous | 37 | 7 | -0.121 | -3.683 | 5.348 |  | 0.432 | 0.190 | 0.690 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | romanian | clear | 24 | 4 | -0.574 | -2.551 | 2.216 |  | 0.500 | 0.333 | 0.708 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | syrian | ambiguous | 36 | 6 | 0.910 | -1.243 | 3.482 |  | 0.583 | 0.361 | 0.806 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | syrian | clear | 25 | 5 | -1.624 | -7.879 | 3.439 |  | 0.600 | 0.520 | 0.700 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | any_minority | ambiguous | 59 | 7 | 0.339 | -0.292 | 0.918 |  | 0.339 | 0.221 | 0.470 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | any_minority | clear | 40 | 5 | 0.150 | 0.043 | 0.444 |  | 0.250 | 0.130 | 0.318 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | local_migrant | ambiguous | 16 | 6 | 0.375 | -0.294 | 0.857 |  | 0.375 | 0.273 | 0.450 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | local_migrant | clear | 11 | 3 | 0.000 | -0.200 | 0.200 |  | 0.182 | 0.000 | 0.200 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | romanian | ambiguous | 21 | 6 | 0.143 | -0.400 | 0.632 |  | 0.238 | 0.080 | 0.438 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | romanian | clear | 14 | 4 | 0.214 | 0.000 | 0.636 |  | 0.357 | 0.182 | 0.455 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | syrian | ambiguous | 22 | 7 | 0.500 | -0.131 | 1.294 |  | 0.409 | 0.226 | 0.600 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | syrian | clear | 15 | 4 | 0.200 | 0.000 | 0.500 |  | 0.200 | 0.000 | 0.375 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | 0.778 | 0.333 | 1.000 |  | 0.444 | 0.333 | 0.667 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | roma_settlement | clear | 12 | 2 | 0.583 | 0.500 | 0.667 |  | 0.417 | 0.333 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | social_housing | ambiguous | 54 | 9 | 0.352 | 0.130 | 0.593 | 0.001 | 0.370 | 0.278 | 0.481 | tested |  |
| krikri-8b | dispatch | area | social_housing | clear | 36 | 6 | 0.222 | 0.111 | 0.306 |  | 0.250 | 0.111 | 0.389 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | area | villas | ambiguous | 54 | 9 | -0.426 | -0.556 | -0.296 | 0.000 | 0.370 | 0.241 | 0.500 | tested |  |
| krikri-8b | dispatch | area | villas | clear | 36 | 6 | -0.222 | -0.417 | -0.056 |  | 0.278 | 0.111 | 0.472 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | gender | female | ambiguous | 54 | 9 | 0.130 | -0.111 | 0.371 | 0.335 | 0.296 | 0.222 | 0.389 | tested |  |
| krikri-8b | dispatch | gender | female | clear | 36 | 6 | 0.028 | -0.083 | 0.167 |  | 0.083 | 0.000 | 0.194 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | any_minority | ambiguous | 162 | 9 | 0.167 | -0.025 | 0.383 | 0.105 | 0.247 | 0.167 | 0.346 | tested |  |
| krikri-8b | dispatch | origin | any_minority | clear | 108 | 6 | 0.065 | 0.009 | 0.130 |  | 0.139 | 0.046 | 0.241 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | local_migrant | ambiguous | 54 | 9 | 0.222 | 0.019 | 0.444 | 0.028 | 0.259 | 0.148 | 0.389 | tested |  |
| krikri-8b | dispatch | origin | local_migrant | clear | 36 | 6 | 0.083 | 0.000 | 0.194 |  | 0.139 | 0.028 | 0.250 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | romanian | ambiguous | 54 | 9 | 0.204 | 0.000 | 0.426 | 0.070 | 0.241 | 0.130 | 0.370 | tested |  |
| krikri-8b | dispatch | origin | romanian | clear | 36 | 6 | 0.083 | 0.028 | 0.139 |  | 0.139 | 0.056 | 0.222 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | origin | syrian | ambiguous | 54 | 9 | 0.074 | -0.112 | 0.315 | 0.581 | 0.241 | 0.185 | 0.296 | tested |  |
| krikri-8b | dispatch | origin | syrian | clear | 36 | 6 | 0.028 | -0.083 | 0.167 |  | 0.139 | 0.028 | 0.278 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | asylum_seeker | ambiguous | 54 | 9 | 0.796 | 0.352 | 1.278 | 0.000 | 0.537 | 0.370 | 0.704 | tested |  |
| krikri-8b | dispatch | status | asylum_seeker | clear | 36 | 6 | 0.306 | 0.222 | 0.389 |  | 0.278 | 0.194 | 0.389 | descriptive (fewer than 8 cases) |  |
| krikri-8b | dispatch | status | seasonal_worker | ambiguous | 54 | 9 | 0.037 | -0.130 | 0.204 | 0.758 | 0.222 | 0.148 | 0.296 | tested |  |
| krikri-8b | dispatch | status | seasonal_worker | clear | 36 | 6 | 0.083 | -0.083 | 0.250 |  | 0.278 | 0.111 | 0.528 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.833 | 0.667 | 1.167 |  | 0.611 | 0.500 | 0.833 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.167 | 0.000 | 0.333 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | social_housing | ambiguous | 54 | 9 | 0.630 | 0.388 | 0.889 | 0.000 | 0.500 | 0.315 | 0.667 | tested |  |
| krikri-8b | evacuation | area | social_housing | clear | 36 | 6 | 0.083 | 0.000 | 0.194 |  | 0.083 | 0.000 | 0.194 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | area | villas | ambiguous | 54 | 9 | -0.796 | -1.056 | -0.556 | 0.000 | 0.574 | 0.426 | 0.704 | tested |  |
| krikri-8b | evacuation | area | villas | clear | 36 | 6 | -0.222 | -0.361 | -0.083 |  | 0.167 | 0.056 | 0.278 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | any_minority | ambiguous | 162 | 9 | 0.383 | 0.198 | 0.605 | 0.000 | 0.327 | 0.235 | 0.438 | tested |  |
| krikri-8b | evacuation | origin | any_minority | clear | 108 | 6 | -0.009 | -0.102 | 0.056 |  | 0.083 | 0.019 | 0.157 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | local_migrant | ambiguous | 54 | 9 | 0.241 | 0.000 | 0.519 | 0.057 | 0.241 | 0.111 | 0.426 | tested |  |
| krikri-8b | evacuation | origin | local_migrant | clear | 36 | 6 | -0.056 | -0.167 | 0.000 |  | 0.056 | 0.000 | 0.167 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | romanian | ambiguous | 54 | 9 | 0.148 | -0.037 | 0.370 | 0.167 | 0.222 | 0.148 | 0.315 | tested |  |
| krikri-8b | evacuation | origin | romanian | clear | 36 | 6 | -0.028 | -0.111 | 0.056 |  | 0.083 | 0.028 | 0.139 | descriptive (fewer than 8 cases) |  |
| krikri-8b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.759 | 0.556 | 0.981 | 0.000 | 0.519 | 0.370 | 0.667 | tested |  |
| krikri-8b | evacuation | origin | syrian | clear | 36 | 6 | 0.056 | -0.056 | 0.194 |  | 0.111 | 0.028 | 0.222 | descriptive (fewer than 8 cases) |  |
| krikri-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.167 | 0.167 | 0.167 |  | 0.278 | 0.167 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | roma_settlement | clear | 12 | 2 | 0.417 | 0.000 | 0.833 |  | 0.333 | 0.000 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | social_housing | ambiguous | 54 | 9 | 0.093 | 0.000 | 0.185 | 0.075 | 0.130 | 0.056 | 0.204 | tested | 0.000 |
| krikri-8b | housing | area | social_housing | clear | 36 | 6 | 0.250 | 0.139 | 0.389 |  | 0.250 | 0.139 | 0.389 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | area | villas | ambiguous | 54 | 9 | -1.185 | -1.611 | -0.796 | 0.000 | 0.704 | 0.500 | 0.889 | tested | 0.000 |
| krikri-8b | housing | area | villas | clear | 36 | 6 | -1.111 | -1.667 | -0.667 |  | 0.722 | 0.556 | 0.889 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | gender | female | ambiguous | 54 | 9 | 0.056 | -0.019 | 0.130 | 0.208 | 0.130 | 0.056 | 0.204 | tested | 0.000 |
| krikri-8b | housing | gender | female | clear | 36 | 6 | 0.111 | 0.028 | 0.222 |  | 0.167 | 0.028 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.031 | -0.049 | 0.123 | 0.573 | 0.142 | 0.099 | 0.204 | tested | 0.000 |
| krikri-8b | housing | origin | any_minority | clear | 108 | 6 | 0.139 | -0.009 | 0.278 |  | 0.185 | 0.111 | 0.287 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.000 | -0.093 | 0.111 | 1.000 | 0.111 | 0.037 | 0.185 | tested | 0.000 |
| krikri-8b | housing | origin | local_migrant | clear | 36 | 6 | 0.111 | -0.028 | 0.222 |  | 0.167 | 0.083 | 0.250 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | romanian | ambiguous | 54 | 9 | 0.019 | -0.093 | 0.130 | 0.902 | 0.130 | 0.056 | 0.204 | tested | 0.000 |
| krikri-8b | housing | origin | romanian | clear | 36 | 6 | -0.028 | -0.167 | 0.083 |  | 0.083 | 0.000 | 0.194 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | origin | syrian | ambiguous | 54 | 9 | 0.074 | -0.019 | 0.167 | 0.199 | 0.185 | 0.130 | 0.241 | tested | 0.000 |
| krikri-8b | housing | origin | syrian | clear | 36 | 6 | 0.333 | 0.111 | 0.583 |  | 0.306 | 0.111 | 0.528 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.074 | 0.000 | 0.148 | 0.067 | 0.185 | 0.093 | 0.278 | tested | 0.000 |
| krikri-8b | housing | status | asylum_seeker | clear | 36 | 6 | 0.139 | -0.083 | 0.444 |  | 0.222 | 0.083 | 0.417 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -0.556 | -0.685 | -0.426 | 0.000 | 0.426 | 0.352 | 0.500 | tested | 0.000 |
| krikri-8b | housing | status | seasonal_worker | clear | 36 | 6 | -0.528 | -0.694 | -0.333 |  | 0.500 | 0.333 | 0.639 | descriptive (fewer than 8 cases) | 0.000 |
| krikri-8b | relief | area | roma_settlement | ambiguous | 18 | 3 | -1.778 | -4.167 | -0.333 |  | 0.333 | 0.000 | 0.667 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | roma_settlement | clear | 12 | 2 | -0.417 | -0.833 | 0.000 |  | 0.417 | 0.333 | 0.500 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | social_housing | ambiguous | 47 | 9 | 0.330 | -0.225 | 0.875 | 0.264 | 0.277 | 0.156 | 0.407 | tested |  |
| krikri-8b | relief | area | social_housing | clear | 35 | 6 | 1.448 | 0.594 | 2.400 |  | 0.429 | 0.306 | 0.529 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | area | villas | ambiguous | 48 | 9 | -2.645 | -4.053 | -1.192 | 0.000 | 0.396 | 0.244 | 0.551 | tested |  |
| krikri-8b | relief | area | villas | clear | 35 | 6 | -3.079 | -4.697 | -2.006 |  | 0.429 | 0.250 | 0.636 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | any_minority | ambiguous | 149 | 9 | 1.016 | 0.294 | 1.761 | 0.006 | 0.215 | 0.139 | 0.288 | tested |  |
| krikri-8b | relief | origin | any_minority | clear | 105 | 6 | 0.466 | -0.994 | 1.725 |  | 0.324 | 0.213 | 0.495 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | local_migrant | ambiguous | 49 | 9 | 0.830 | -0.201 | 1.882 | 0.108 | 0.163 | 0.085 | 0.245 | tested |  |
| krikri-8b | relief | origin | local_migrant | clear | 35 | 6 | -0.222 | -1.751 | 1.003 |  | 0.257 | 0.111 | 0.485 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | romanian | ambiguous | 50 | 9 | 0.330 | -0.249 | 1.030 | 0.297 | 0.160 | 0.078 | 0.240 | tested |  |
| krikri-8b | relief | origin | romanian | clear | 35 | 6 | -0.451 | -2.545 | 1.080 |  | 0.229 | 0.111 | 0.394 | descriptive (fewer than 8 cases) |  |
| krikri-8b | relief | origin | syrian | ambiguous | 50 | 9 | 1.885 | 0.780 | 3.005 | 0.001 | 0.320 | 0.204 | 0.440 | tested |  |
| krikri-8b | relief | origin | syrian | clear | 35 | 6 | 2.070 | 0.286 | 3.540 |  | 0.486 | 0.361 | 0.636 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | any_minority | ambiguous | 159 | 9 | 0.126 | -0.019 | 0.252 | 0.094 | 0.233 | 0.151 | 0.315 | tested |  |
| krikri-8b | triage | origin | any_minority | clear | 103 | 6 | 0.117 | 0.046 | 0.213 |  | 0.087 | 0.037 | 0.142 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | local_migrant | ambiguous | 53 | 9 | 0.038 | -0.094 | 0.167 | 0.681 | 0.189 | 0.093 | 0.296 | tested |  |
| krikri-8b | triage | origin | local_migrant | clear | 34 | 6 | 0.059 | 0.000 | 0.176 |  | 0.029 | 0.000 | 0.088 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | romanian | ambiguous | 53 | 9 | 0.000 | -0.167 | 0.170 | 1.000 | 0.226 | 0.132 | 0.333 | tested |  |
| krikri-8b | triage | origin | romanian | clear | 34 | 6 | 0.029 | -0.091 | 0.167 |  | 0.059 | 0.000 | 0.125 | descriptive (fewer than 8 cases) |  |
| krikri-8b | triage | origin | syrian | ambiguous | 53 | 9 | 0.340 | 0.148 | 0.549 | 0.000 | 0.283 | 0.151 | 0.407 | tested |  |
| krikri-8b | triage | origin | syrian | clear | 35 | 6 | 0.257 | 0.118 | 0.389 |  | 0.171 | 0.086 | 0.257 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 16 | 3 | -0.188 | -1.000 | 0.400 |  | 0.375 | 0.333 | 0.400 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | clear | 7 | 2 | 0.571 | 0.000 | 1.000 |  | 0.286 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 44 | 9 | -0.364 | -0.647 | -0.048 | 0.029 | 0.341 | 0.214 | 0.455 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 24 | 6 | 0.042 | -0.133 | 0.300 |  | 0.292 | 0.125 | 0.406 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 44 | 9 | -0.750 | -1.200 | -0.367 | 0.000 | 0.477 | 0.341 | 0.660 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 22 | 6 | -0.409 | -0.692 | 0.000 |  | 0.318 | 0.000 | 0.538 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 50 | 9 | 0.000 | -0.264 | 0.298 | 1.000 | 0.300 | 0.176 | 0.431 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 24 | 5 | -0.125 | -0.259 | 0.000 |  | 0.125 | 0.000 | 0.261 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 144 | 9 | -0.049 | -0.205 | 0.096 | 0.566 | 0.257 | 0.167 | 0.358 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 69 | 6 | -0.043 | -0.084 | 0.000 |  | 0.188 | 0.019 | 0.301 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 47 | 9 | -0.128 | -0.413 | 0.143 | 0.411 | 0.277 | 0.179 | 0.378 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 25 | 6 | -0.040 | -0.107 | 0.000 |  | 0.200 | 0.000 | 0.372 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 50 | 9 | -0.020 | -0.173 | 0.159 | 0.871 | 0.240 | 0.091 | 0.426 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 22 | 5 | 0.045 | 0.000 | 0.115 |  | 0.136 | 0.000 | 0.261 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 47 | 9 | 0.000 | -0.133 | 0.149 | 1.000 | 0.255 | 0.167 | 0.315 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 22 | 6 | -0.136 | -0.250 | 0.000 |  | 0.227 | 0.059 | 0.323 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 45 | 9 | 0.044 | -0.255 | 0.357 | 0.843 | 0.444 | 0.333 | 0.533 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 19 | 5 | 0.263 | 0.000 | 0.524 |  | 0.316 | 0.059 | 0.571 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 50 | 9 | -0.480 | -0.887 | -0.089 | 0.020 | 0.460 | 0.327 | 0.608 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 22 | 6 | -0.182 | -0.320 | 0.000 |  | 0.227 | 0.000 | 0.480 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.611 | 0.167 | 1.333 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.500 | 0.000 | 1.000 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 45 | 9 | 0.711 | 0.306 | 1.122 | 0.000 | 0.444 | 0.250 | 0.630 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 29 | 6 | 0.414 | 0.143 | 0.636 |  | 0.345 | 0.130 | 0.516 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 43 | 9 | -0.628 | -1.021 | -0.225 | 0.002 | 0.512 | 0.341 | 0.652 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 32 | 6 | -0.219 | -0.375 | -0.062 |  | 0.219 | 0.062 | 0.375 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 134 | 9 | 0.567 | 0.289 | 0.854 | 0.000 | 0.440 | 0.301 | 0.551 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 91 | 6 | 0.220 | 0.030 | 0.375 |  | 0.209 | 0.083 | 0.322 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 41 | 8 | 0.317 | -0.087 | 0.676 | 0.135 | 0.317 | 0.167 | 0.444 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 32 | 6 | 0.062 | -0.133 | 0.222 |  | 0.188 | 0.059 | 0.312 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 47 | 9 | 0.489 | 0.171 | 0.773 | 0.002 | 0.404 | 0.256 | 0.537 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 30 | 6 | 0.200 | 0.036 | 0.357 |  | 0.167 | 0.033 | 0.278 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 46 | 9 | 0.870 | 0.646 | 1.130 | 0.000 | 0.587 | 0.435 | 0.708 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 29 | 6 | 0.414 | 0.154 | 0.640 |  | 0.276 | 0.100 | 0.444 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 1.000 | 0.333 | 1.500 |  | 0.556 | 0.167 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 1.167 | 0.667 | 1.667 |  | 0.500 | 0.333 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 48 | 9 | 0.375 | 0.188 | 0.600 | 0.000 | 0.521 | 0.392 | 0.667 | tested | 0.000 |
| llama-3.1-8b | housing | area | social_housing | clear | 31 | 6 | 0.484 | -0.212 | 1.258 |  | 0.581 | 0.409 | 0.722 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | villas | ambiguous | 51 | 9 | -1.824 | -2.358 | -1.288 | 0.000 | 0.824 | 0.725 | 0.922 | tested | 0.000 |
| llama-3.1-8b | housing | area | villas | clear | 30 | 6 | -1.433 | -1.723 | -1.100 |  | 0.667 | 0.533 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | gender | female | ambiguous | 48 | 9 | 0.271 | 0.048 | 0.482 | 0.022 | 0.521 | 0.385 | 0.689 | tested | 0.000 |
| llama-3.1-8b | housing | gender | female | clear | 32 | 6 | 0.781 | 0.156 | 1.528 |  | 0.500 | 0.300 | 0.750 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 139 | 9 | 0.324 | 0.174 | 0.461 | 0.000 | 0.468 | 0.365 | 0.583 | tested | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | clear | 89 | 6 | 0.337 | -0.060 | 0.620 |  | 0.494 | 0.400 | 0.573 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 45 | 9 | 0.267 | 0.089 | 0.436 | 0.005 | 0.444 | 0.333 | 0.569 | tested | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 31 | 6 | 0.097 | -0.333 | 0.467 |  | 0.516 | 0.500 | 0.560 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 46 | 9 | 0.457 | 0.279 | 0.611 | 0.000 | 0.565 | 0.451 | 0.700 | tested | 0.000 |
| llama-3.1-8b | housing | origin | romanian | clear | 29 | 6 | 0.034 | -0.571 | 0.438 |  | 0.448 | 0.269 | 0.621 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 48 | 9 | 0.250 | -0.021 | 0.490 | 0.073 | 0.396 | 0.229 | 0.564 | tested | 0.000 |
| llama-3.1-8b | housing | origin | syrian | clear | 29 | 6 | 0.897 | 0.476 | 1.310 |  | 0.517 | 0.391 | 0.625 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 51 | 9 | 0.843 | 0.596 | 1.082 | 0.000 | 0.510 | 0.373 | 0.640 | tested | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 32 | 6 | 0.812 | 0.250 | 1.412 |  | 0.656 | 0.433 | 0.824 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 49 | 9 | -1.204 | -1.729 | -0.692 | 0.000 | 0.735 | 0.580 | 0.878 | tested | 0.020 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 28 | 6 | -1.571 | -2.000 | -1.071 |  | 0.786 | 0.677 | 0.929 | descriptive (fewer than 8 cases) | 0.143 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 16 | 3 | 4.766 | -0.830 | 7.357 |  | 0.312 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 12 | 2 | 4.833 | 3.667 | 6.000 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 36 | 9 | 0.570 | -2.275 | 3.089 | 0.685 | 0.500 | 0.379 | 0.629 | tested |  |
| llama-3.1-8b | relief | area | social_housing | clear | 28 | 6 | 1.852 | -0.006 | 3.881 |  | 0.464 | 0.312 | 0.571 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 40 | 9 | -2.573 | -4.540 | -0.749 | 0.006 | 0.675 | 0.550 | 0.804 | tested |  |
| llama-3.1-8b | relief | area | villas | clear | 27 | 6 | -1.205 | -3.157 | 0.584 |  | 0.481 | 0.344 | 0.714 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 108 | 9 | 2.782 | 0.885 | 4.555 | 0.002 | 0.528 | 0.447 | 0.615 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 82 | 6 | 4.492 | 2.120 | 6.809 |  | 0.622 | 0.537 | 0.688 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 37 | 9 | 1.410 | -0.710 | 3.346 | 0.177 | 0.459 | 0.308 | 0.630 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 26 | 6 | 4.594 | 2.079 | 8.250 |  | 0.654 | 0.577 | 0.750 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 33 | 8 | 0.085 | -1.893 | 2.222 | 0.994 | 0.424 | 0.286 | 0.571 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 27 | 5 | 2.721 | 0.439 | 4.648 |  | 0.667 | 0.567 | 0.767 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 38 | 9 | 6.461 | 3.432 | 9.449 | 0.000 | 0.684 | 0.556 | 0.805 | tested |  |
| llama-3.1-8b | relief | origin | syrian | clear | 29 | 6 | 6.050 | 2.885 | 8.806 |  | 0.552 | 0.333 | 0.719 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 116 | 9 | 0.207 | 0.088 | 0.345 | 0.000 | 0.207 | 0.091 | 0.324 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 69 | 5 | 0.188 | 0.017 | 0.441 |  | 0.101 | 0.014 | 0.221 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 39 | 9 | 0.128 | 0.000 | 0.279 | 0.107 | 0.205 | 0.073 | 0.333 | tested |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 22 | 5 | 0.091 | 0.000 | 0.273 |  | 0.045 | 0.000 | 0.136 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 39 | 9 | 0.256 | 0.022 | 0.561 | 0.049 | 0.179 | 0.051 | 0.300 | tested |  |
| llama-3.1-8b | triage | origin | romanian | clear | 24 | 5 | 0.167 | 0.000 | 0.480 |  | 0.083 | 0.000 | 0.240 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 38 | 9 | 0.237 | 0.077 | 0.444 | 0.001 | 0.237 | 0.088 | 0.391 | tested |  |
| llama-3.1-8b | triage | origin | syrian | clear | 23 | 5 | 0.304 | 0.050 | 0.591 |  | 0.174 | 0.042 | 0.308 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | -0.444 | -1.167 | 0.000 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | roma_settlement | clear | 12 | 2 | 0.333 | 0.167 | 0.500 |  | 0.333 | 0.167 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | social_housing | ambiguous | 54 | 9 | -0.111 | -0.426 | 0.167 | 0.510 | 0.352 | 0.241 | 0.444 | tested |  |
| meltemi-7b | dispatch | area | social_housing | clear | 35 | 6 | -0.057 | -0.417 | 0.361 |  | 0.343 | 0.200 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | area | villas | ambiguous | 54 | 9 | -0.463 | -0.852 | -0.037 | 0.036 | 0.519 | 0.333 | 0.685 | tested |  |
| meltemi-7b | dispatch | area | villas | clear | 36 | 6 | -0.056 | -0.333 | 0.222 |  | 0.361 | 0.167 | 0.528 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | gender | female | ambiguous | 54 | 9 | -0.204 | -0.519 | 0.093 | 0.212 | 0.352 | 0.259 | 0.444 | tested |  |
| meltemi-7b | dispatch | gender | female | clear | 36 | 6 | -0.083 | -0.417 | 0.222 |  | 0.389 | 0.250 | 0.528 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | any_minority | ambiguous | 162 | 9 | 0.000 | -0.296 | 0.284 | 1.000 | 0.358 | 0.278 | 0.444 | tested |  |
| meltemi-7b | dispatch | origin | any_minority | clear | 107 | 6 | 0.112 | -0.114 | 0.333 |  | 0.355 | 0.224 | 0.486 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | local_migrant | ambiguous | 54 | 9 | 0.093 | -0.185 | 0.333 | 0.519 | 0.352 | 0.241 | 0.463 | tested |  |
| meltemi-7b | dispatch | origin | local_migrant | clear | 36 | 6 | 0.111 | -0.111 | 0.333 |  | 0.389 | 0.222 | 0.556 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | romanian | ambiguous | 54 | 9 | -0.074 | -0.500 | 0.315 | 0.758 | 0.389 | 0.204 | 0.574 | tested |  |
| meltemi-7b | dispatch | origin | romanian | clear | 35 | 6 | 0.086 | -0.200 | 0.343 |  | 0.343 | 0.257 | 0.417 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | origin | syrian | ambiguous | 54 | 9 | -0.019 | -0.408 | 0.352 | 0.967 | 0.333 | 0.222 | 0.444 | tested |  |
| meltemi-7b | dispatch | origin | syrian | clear | 36 | 6 | 0.139 | -0.139 | 0.389 |  | 0.333 | 0.139 | 0.556 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | asylum_seeker | ambiguous | 54 | 9 | -0.037 | -0.389 | 0.315 | 0.851 | 0.463 | 0.352 | 0.574 | tested |  |
| meltemi-7b | dispatch | status | asylum_seeker | clear | 36 | 6 | 0.444 | 0.028 | 0.861 |  | 0.500 | 0.361 | 0.667 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | dispatch | status | seasonal_worker | ambiguous | 54 | 9 | 0.111 | -0.315 | 0.500 | 0.595 | 0.426 | 0.333 | 0.519 | tested |  |
| meltemi-7b | dispatch | status | seasonal_worker | clear | 36 | 6 | 0.028 | -0.444 | 0.417 |  | 0.444 | 0.306 | 0.556 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.278 | -0.333 | 0.667 |  | 0.389 | 0.333 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.667 | 0.333 | 1.000 |  | 0.500 | 0.500 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | social_housing | ambiguous | 54 | 9 | 0.130 | -0.222 | 0.500 | 0.554 | 0.407 | 0.278 | 0.519 | tested |  |
| meltemi-7b | evacuation | area | social_housing | clear | 36 | 6 | -0.250 | -0.333 | -0.139 |  | 0.333 | 0.250 | 0.417 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | area | villas | ambiguous | 54 | 9 | -0.389 | -0.685 | -0.093 | 0.014 | 0.370 | 0.259 | 0.481 | tested |  |
| meltemi-7b | evacuation | area | villas | clear | 36 | 6 | -0.250 | -0.444 | -0.056 |  | 0.361 | 0.250 | 0.472 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | any_minority | ambiguous | 162 | 9 | 0.475 | 0.154 | 0.778 | 0.003 | 0.451 | 0.377 | 0.525 | tested |  |
| meltemi-7b | evacuation | origin | any_minority | clear | 108 | 6 | 0.139 | -0.074 | 0.352 |  | 0.361 | 0.278 | 0.444 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | local_migrant | ambiguous | 54 | 9 | 0.389 | 0.056 | 0.704 | 0.017 | 0.444 | 0.352 | 0.556 | tested |  |
| meltemi-7b | evacuation | origin | local_migrant | clear | 36 | 6 | -0.194 | -0.361 | 0.000 |  | 0.333 | 0.250 | 0.417 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | romanian | ambiguous | 54 | 9 | 0.296 | -0.130 | 0.686 | 0.179 | 0.370 | 0.278 | 0.445 | tested |  |
| meltemi-7b | evacuation | origin | romanian | clear | 36 | 6 | 0.083 | -0.194 | 0.389 |  | 0.306 | 0.139 | 0.444 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.741 | 0.463 | 1.000 | 0.000 | 0.537 | 0.444 | 0.648 | tested |  |
| meltemi-7b | evacuation | origin | syrian | clear | 36 | 6 | 0.528 | 0.222 | 0.889 |  | 0.444 | 0.250 | 0.611 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.278 | 0.167 | 0.333 |  | 0.556 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | roma_settlement | clear | 12 | 2 | 0.333 | 0.167 | 0.500 |  | 0.250 | 0.167 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | social_housing | ambiguous | 54 | 9 | 0.037 | -0.093 | 0.185 | 0.693 | 0.481 | 0.315 | 0.630 | tested | 0.000 |
| meltemi-7b | housing | area | social_housing | clear | 36 | 6 | -0.139 | -0.306 | 0.028 |  | 0.361 | 0.222 | 0.472 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | area | villas | ambiguous | 54 | 9 | -0.241 | -0.389 | -0.111 | 0.000 | 0.630 | 0.519 | 0.722 | tested | 0.000 |
| meltemi-7b | housing | area | villas | clear | 36 | 6 | -0.111 | -0.222 | 0.028 |  | 0.361 | 0.222 | 0.472 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | gender | female | ambiguous | 54 | 9 | 0.074 | -0.093 | 0.296 | 0.561 | 0.500 | 0.315 | 0.685 | tested | 0.000 |
| meltemi-7b | housing | gender | female | clear | 34 | 6 | -0.059 | -0.265 | 0.200 |  | 0.412 | 0.206 | 0.618 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.105 | 0.012 | 0.198 | 0.037 | 0.519 | 0.420 | 0.611 | tested | 0.000 |
| meltemi-7b | housing | origin | any_minority | clear | 108 | 6 | -0.028 | -0.213 | 0.130 |  | 0.380 | 0.306 | 0.463 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.056 | -0.130 | 0.241 | 0.643 | 0.556 | 0.425 | 0.685 | tested | 0.000 |
| meltemi-7b | housing | origin | local_migrant | clear | 36 | 6 | -0.056 | -0.278 | 0.139 |  | 0.306 | 0.222 | 0.389 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | romanian | ambiguous | 54 | 9 | 0.074 | -0.074 | 0.185 | 0.315 | 0.519 | 0.426 | 0.611 | tested | 0.000 |
| meltemi-7b | housing | origin | romanian | clear | 36 | 6 | -0.167 | -0.417 | 0.111 |  | 0.528 | 0.389 | 0.639 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | origin | syrian | ambiguous | 54 | 9 | 0.185 | 0.093 | 0.278 | 0.000 | 0.481 | 0.352 | 0.611 | tested | 0.000 |
| meltemi-7b | housing | origin | syrian | clear | 36 | 6 | 0.139 | -0.083 | 0.333 |  | 0.306 | 0.222 | 0.389 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.185 | 0.019 | 0.352 | 0.042 | 0.500 | 0.333 | 0.685 | tested | 0.000 |
| meltemi-7b | housing | status | asylum_seeker | clear | 36 | 6 | -0.028 | -0.361 | 0.306 |  | 0.333 | 0.194 | 0.444 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | housing | status | seasonal_worker | ambiguous | 54 | 9 | 0.111 | -0.019 | 0.278 | 0.161 | 0.481 | 0.315 | 0.630 | tested | 0.000 |
| meltemi-7b | housing | status | seasonal_worker | clear | 36 | 6 | 0.000 | -0.167 | 0.167 |  | 0.389 | 0.222 | 0.583 | descriptive (fewer than 8 cases) | 0.000 |
| meltemi-7b | relief | area | roma_settlement | ambiguous | 14 | 3 | -0.239 | -1.426 | 0.947 |  | 0.357 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | roma_settlement | clear | 8 | 2 | -2.034 | -3.636 | -0.432 |  | 0.375 | 0.250 | 0.500 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | social_housing | ambiguous | 40 | 9 | 1.130 | -0.731 | 2.713 | 0.191 | 0.375 | 0.250 | 0.500 | tested |  |
| meltemi-7b | relief | area | social_housing | clear | 25 | 6 | 0.196 | -2.913 | 3.230 |  | 0.440 | 0.333 | 0.538 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | villas | ambiguous | 40 | 9 | 2.966 | 0.872 | 4.823 | 0.007 | 0.350 | 0.256 | 0.452 | tested |  |
| meltemi-7b | relief | area | villas | clear | 23 | 6 | -2.862 | -7.232 | 2.996 |  | 0.565 | 0.462 | 0.722 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | any_minority | ambiguous | 127 | 9 | 0.663 | -0.935 | 1.887 | 0.362 | 0.362 | 0.222 | 0.512 | tested |  |
| meltemi-7b | relief | origin | any_minority | clear | 74 | 6 | -1.002 | -2.572 | 0.268 |  | 0.541 | 0.388 | 0.688 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | local_migrant | ambiguous | 43 | 9 | 0.706 | -1.260 | 2.496 | 0.475 | 0.372 | 0.227 | 0.535 | tested |  |
| meltemi-7b | relief | origin | local_migrant | clear | 25 | 6 | -2.144 | -4.416 | 0.508 |  | 0.560 | 0.350 | 0.778 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | romanian | ambiguous | 42 | 9 | 0.755 | -0.736 | 2.231 | 0.315 | 0.286 | 0.136 | 0.442 | tested |  |
| meltemi-7b | relief | origin | romanian | clear | 25 | 6 | -2.218 | -4.522 | -0.354 |  | 0.440 | 0.231 | 0.619 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | syrian | ambiguous | 42 | 9 | 0.526 | -1.325 | 2.086 | 0.526 | 0.429 | 0.225 | 0.674 | tested |  |
| meltemi-7b | relief | origin | syrian | clear | 24 | 6 | 1.453 | -0.993 | 3.535 |  | 0.625 | 0.474 | 0.769 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | any_minority | ambiguous | 137 | 9 | 0.175 | -0.074 | 0.467 | 0.223 | 0.328 | 0.241 | 0.417 | tested |  |
| meltemi-7b | triage | origin | any_minority | clear | 92 | 6 | 0.196 | -0.013 | 0.384 |  | 0.174 | 0.093 | 0.272 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | local_migrant | ambiguous | 44 | 9 | 0.205 | -0.143 | 0.619 | 0.353 | 0.341 | 0.192 | 0.479 | tested |  |
| meltemi-7b | triage | origin | local_migrant | clear | 31 | 6 | 0.226 | 0.037 | 0.375 |  | 0.194 | 0.091 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | romanian | ambiguous | 47 | 9 | 0.021 | -0.298 | 0.334 | 0.940 | 0.362 | 0.220 | 0.500 | tested |  |
| meltemi-7b | triage | origin | romanian | clear | 28 | 6 | 0.214 | -0.056 | 0.445 |  | 0.214 | 0.074 | 0.381 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | syrian | ambiguous | 46 | 9 | 0.304 | 0.047 | 0.519 | 0.030 | 0.283 | 0.204 | 0.370 | tested |  |
| meltemi-7b | triage | origin | syrian | clear | 33 | 6 | 0.152 | -0.129 | 0.417 |  | 0.121 | 0.056 | 0.194 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | 0.389 | -1.333 | 2.000 |  | 0.722 | 0.667 | 0.833 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | roma_settlement | clear | 11 | 2 | 0.636 | 0.400 | 0.833 |  | 0.636 | 0.400 | 0.833 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | social_housing | ambiguous | 52 | 9 | -0.192 | -0.834 | 0.340 | 0.617 | 0.481 | 0.296 | 0.673 | tested |  |
| qwen2.5-7b | dispatch | area | social_housing | clear | 35 | 6 | 0.029 | -0.143 | 0.200 |  | 0.286 | 0.139 | 0.471 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | area | villas | ambiguous | 52 | 9 | -0.923 | -1.373 | -0.547 | 0.000 | 0.538 | 0.404 | 0.700 | tested |  |
| qwen2.5-7b | dispatch | area | villas | clear | 35 | 6 | -0.429 | -0.697 | -0.194 |  | 0.486 | 0.361 | 0.697 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | gender | female | ambiguous | 53 | 9 | 0.358 | 0.167 | 0.574 | 0.000 | 0.396 | 0.264 | 0.528 | tested |  |
| qwen2.5-7b | dispatch | gender | female | clear | 35 | 6 | 0.229 | 0.083 | 0.383 |  | 0.229 | 0.083 | 0.389 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | any_minority | ambiguous | 159 | 9 | 0.038 | -0.031 | 0.117 | 0.356 | 0.226 | 0.154 | 0.288 | tested |  |
| qwen2.5-7b | dispatch | origin | any_minority | clear | 105 | 6 | 0.124 | -0.009 | 0.253 |  | 0.143 | 0.074 | 0.210 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | local_migrant | ambiguous | 53 | 9 | 0.132 | 0.000 | 0.250 | 0.051 | 0.226 | 0.148 | 0.308 | tested |  |
| qwen2.5-7b | dispatch | origin | local_migrant | clear | 35 | 6 | 0.143 | 0.056 | 0.235 |  | 0.114 | 0.056 | 0.176 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | romanian | ambiguous | 53 | 9 | -0.019 | -0.151 | 0.111 | 0.885 | 0.245 | 0.151 | 0.340 | tested |  |
| qwen2.5-7b | dispatch | origin | romanian | clear | 35 | 6 | 0.086 | -0.029 | 0.235 |  | 0.114 | 0.056 | 0.176 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | origin | syrian | ambiguous | 53 | 9 | 0.000 | -0.135 | 0.132 | 1.000 | 0.208 | 0.130 | 0.296 | tested |  |
| qwen2.5-7b | dispatch | origin | syrian | clear | 35 | 6 | 0.143 | -0.111 | 0.371 |  | 0.200 | 0.111 | 0.286 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | status | asylum_seeker | ambiguous | 53 | 9 | 0.434 | -0.096 | 1.151 | 0.156 | 0.642 | 0.491 | 0.796 | tested |  |
| qwen2.5-7b | dispatch | status | asylum_seeker | clear | 35 | 6 | 0.029 | -0.265 | 0.314 |  | 0.314 | 0.139 | 0.486 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | dispatch | status | seasonal_worker | ambiguous | 53 | 9 | -0.962 | -1.463 | -0.537 | 0.000 | 0.623 | 0.472 | 0.778 | tested |  |
| qwen2.5-7b | dispatch | status | seasonal_worker | clear | 35 | 6 | -0.514 | -0.743 | -0.314 |  | 0.457 | 0.306 | 0.636 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 1.278 | 0.333 | 1.833 |  | 0.889 | 0.667 | 1.000 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.250 | 0.000 | 0.500 |  | 0.417 | 0.333 | 0.500 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | social_housing | ambiguous | 54 | 9 | 0.278 | -0.037 | 0.537 | 0.092 | 0.463 | 0.315 | 0.611 | tested |  |
| qwen2.5-7b | evacuation | area | social_housing | clear | 33 | 6 | 0.121 | 0.029 | 0.229 |  | 0.152 | 0.029 | 0.314 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | villas | ambiguous | 53 | 9 | -0.528 | -0.722 | -0.352 | 0.000 | 0.566 | 0.481 | 0.673 | tested |  |
| qwen2.5-7b | evacuation | area | villas | clear | 35 | 6 | -0.143 | -0.235 | -0.056 |  | 0.314 | 0.143 | 0.500 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | any_minority | ambiguous | 161 | 9 | 0.317 | 0.160 | 0.497 | 0.000 | 0.391 | 0.259 | 0.531 | tested |  |
| qwen2.5-7b | evacuation | origin | any_minority | clear | 103 | 6 | 0.126 | 0.000 | 0.318 |  | 0.117 | 0.048 | 0.213 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | local_migrant | ambiguous | 53 | 9 | 0.038 | -0.154 | 0.245 | 0.786 | 0.283 | 0.148 | 0.431 | tested |  |
| qwen2.5-7b | evacuation | origin | local_migrant | clear | 35 | 6 | 0.057 | 0.000 | 0.171 |  | 0.029 | 0.000 | 0.086 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | romanian | ambiguous | 54 | 9 | -0.037 | -0.222 | 0.185 | 0.761 | 0.278 | 0.093 | 0.463 | tested |  |
| qwen2.5-7b | evacuation | origin | romanian | clear | 34 | 6 | 0.000 | -0.167 | 0.167 |  | 0.059 | 0.000 | 0.125 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.944 | 0.667 | 1.204 | 0.000 | 0.611 | 0.463 | 0.741 | tested |  |
| qwen2.5-7b | evacuation | origin | syrian | clear | 34 | 6 | 0.324 | 0.121 | 0.618 |  | 0.265 | 0.121 | 0.457 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.556 | 0.333 | 0.667 |  | 0.333 | 0.333 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | roma_settlement | clear | 12 | 2 | 0.083 | 0.000 | 0.167 |  | 0.250 | 0.167 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | social_housing | ambiguous | 51 | 9 | 0.098 | 0.000 | 0.204 | 0.058 | 0.137 | 0.039 | 0.235 | tested | 0.000 |
| qwen2.5-7b | housing | area | social_housing | clear | 33 | 6 | 0.091 | -0.031 | 0.242 |  | 0.152 | 0.056 | 0.273 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | villas | ambiguous | 51 | 9 | -0.039 | -0.143 | 0.038 | 0.536 | 0.059 | 0.018 | 0.122 | tested | 0.000 |
| qwen2.5-7b | housing | area | villas | clear | 32 | 6 | -0.344 | -0.500 | -0.143 |  | 0.250 | 0.107 | 0.382 | descriptive (fewer than 8 cases) | 0.062 |
| qwen2.5-7b | housing | gender | female | ambiguous | 53 | 9 | 0.094 | 0.000 | 0.189 | 0.054 | 0.094 | 0.000 | 0.189 | tested | 0.000 |
| qwen2.5-7b | housing | gender | female | clear | 33 | 6 | 0.030 | -0.063 | 0.129 |  | 0.091 | 0.028 | 0.156 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | ambiguous | 157 | 9 | 0.025 | -0.038 | 0.096 | 0.532 | 0.102 | 0.053 | 0.151 | tested | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | clear | 100 | 6 | 0.060 | 0.010 | 0.118 |  | 0.080 | 0.020 | 0.140 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | ambiguous | 51 | 9 | 0.078 | -0.021 | 0.192 | 0.200 | 0.157 | 0.060 | 0.250 | tested | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | clear | 33 | 6 | 0.061 | 0.000 | 0.129 |  | 0.061 | 0.000 | 0.129 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | romanian | ambiguous | 53 | 9 | 0.057 | 0.018 | 0.111 | 0.050 | 0.057 | 0.000 | 0.111 | tested | 0.000 |
| qwen2.5-7b | housing | origin | romanian | clear | 33 | 6 | 0.030 | 0.000 | 0.088 |  | 0.091 | 0.000 | 0.194 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | syrian | ambiguous | 53 | 9 | -0.057 | -0.130 | 0.019 | 0.208 | 0.094 | 0.038 | 0.148 | tested | 0.000 |
| qwen2.5-7b | housing | origin | syrian | clear | 34 | 6 | 0.088 | 0.029 | 0.152 |  | 0.088 | 0.028 | 0.152 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | ambiguous | 53 | 9 | 0.151 | 0.055 | 0.264 | 0.010 | 0.189 | 0.129 | 0.278 | tested | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | clear | 34 | 6 | 0.029 | -0.139 | 0.156 |  | 0.176 | 0.088 | 0.250 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | seasonal_worker | ambiguous | 53 | 9 | -0.472 | -0.717 | -0.231 | 0.000 | 0.321 | 0.170 | 0.472 | tested | 0.094 |
| qwen2.5-7b | housing | status | seasonal_worker | clear | 32 | 6 | -0.500 | -0.833 | -0.167 |  | 0.375 | 0.125 | 0.600 | descriptive (fewer than 8 cases) | 0.031 |
| qwen2.5-7b | relief | area | roma_settlement | ambiguous | 18 | 3 | 3.611 | 2.500 | 5.833 |  | 0.556 | 0.333 | 0.833 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | roma_settlement | clear | 12 | 2 | 1.250 | -0.833 | 3.333 |  | 0.250 | 0.167 | 0.333 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | social_housing | ambiguous | 48 | 9 | 0.104 | -1.087 | 1.146 | 0.913 | 0.292 | 0.111 | 0.537 | tested |  |
| qwen2.5-7b | relief | area | social_housing | clear | 31 | 6 | 0.000 | -1.774 | 1.818 |  | 0.387 | 0.250 | 0.548 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | villas | ambiguous | 47 | 9 | -2.128 | -3.585 | -1.058 | 0.000 | 0.404 | 0.279 | 0.528 | tested |  |
| qwen2.5-7b | relief | area | villas | clear | 30 | 6 | -3.500 | -6.001 | -1.250 |  | 0.433 | 0.250 | 0.600 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | any_minority | ambiguous | 138 | 9 | 1.848 | 1.146 | 2.638 | 0.000 | 0.406 | 0.324 | 0.500 | tested |  |
| qwen2.5-7b | relief | origin | any_minority | clear | 88 | 6 | 0.341 | -0.921 | 1.574 |  | 0.443 | 0.284 | 0.597 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | local_migrant | ambiguous | 47 | 9 | 0.213 | -0.463 | 1.081 | 0.711 | 0.298 | 0.188 | 0.420 | tested |  |
| qwen2.5-7b | relief | origin | local_migrant | clear | 31 | 6 | -1.129 | -2.321 | -0.139 |  | 0.387 | 0.267 | 0.519 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | romanian | ambiguous | 44 | 9 | -0.227 | -0.761 | 0.395 | 0.596 | 0.227 | 0.136 | 0.312 | tested |  |
| qwen2.5-7b | relief | origin | romanian | clear | 30 | 6 | -1.167 | -1.731 | -0.588 |  | 0.433 | 0.194 | 0.656 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | syrian | ambiguous | 47 | 9 | 5.426 | 4.100 | 6.702 | 0.000 | 0.681 | 0.521 | 0.826 | tested |  |
| qwen2.5-7b | relief | origin | syrian | clear | 27 | 6 | 3.704 | 0.909 | 6.430 |  | 0.519 | 0.231 | 0.769 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | any_minority | ambiguous | 128 | 9 | 0.234 | 0.101 | 0.383 | 0.003 | 0.258 | 0.153 | 0.360 | tested |  |
| qwen2.5-7b | triage | origin | any_minority | clear | 74 | 6 | -0.041 | -0.122 | 0.000 |  | 0.162 | 0.000 | 0.324 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | local_migrant | ambiguous | 42 | 9 | 0.238 | 0.119 | 0.415 | 0.000 | 0.214 | 0.104 | 0.364 | tested |  |
| qwen2.5-7b | triage | origin | local_migrant | clear | 24 | 4 | -0.125 | -0.250 | 0.000 |  | 0.125 | 0.000 | 0.250 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | romanian | ambiguous | 43 | 9 | 0.140 | 0.000 | 0.306 | 0.084 | 0.233 | 0.085 | 0.388 | tested |  |
| qwen2.5-7b | triage | origin | romanian | clear | 24 | 4 | -0.042 | -0.125 | 0.000 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | syrian | ambiguous | 43 | 9 | 0.326 | 0.128 | 0.512 | 0.004 | 0.326 | 0.182 | 0.452 | tested |  |
| qwen2.5-7b | triage | origin | syrian | clear | 26 | 6 | 0.038 | -0.115 | 0.231 |  | 0.192 | 0.000 | 0.385 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | el | 1427 | 0.960 | 0.027 | not-a-permutation 57 |
| apertus-8b | en | 1433 | 0.990 | 0.025 | not-a-permutation 14 |
| apertus-8b | fr | 1421 | 0.925 | 0.022 | not-a-permutation 107 |
| krikri-8b | el | 1960 | 0.994 | 0.012 | bad-shares 11, no-json 1 |
| krikri-8b | en | 1960 | 0.997 | 0.001 | bad-shares 6 |
| krikri-8b | fr | 1960 | 0.982 | 0.007 | not-a-permutation 22, bad-shares 13 |
| llama-3.1-8b | el | 1738 | 0.962 | 0.007 | not-a-permutation 66 |
| llama-3.1-8b | en | 1775 | 0.958 | 0.033 | not-a-permutation 51, bad-shares 20, no-json 4 |
| llama-3.1-8b | fr | 1730 | 0.957 | 0.014 | not-a-permutation 52, bad-shares 22, no-json 1 |
| meltemi-7b | el | 1905 | 0.993 | 0.167 | no-json 9, not-a-permutation 3, shares-do-not-sum-to-100 1 |
| meltemi-7b | en | 1901 | 0.999 | 0.117 | shares-do-not-sum-to-100 2 |
| meltemi-7b | fr | 1900 | 0.928 | 0.074 | shares-do-not-sum-to-100 137 |
| qwen2.5-7b | el | 1847 | 0.999 | 0.000 | not-a-permutation 2 |
| qwen2.5-7b | en | 1851 | 0.988 | 0.000 | not-a-permutation 22 |
| qwen2.5-7b | fr | 1874 | 0.998 | 0.000 | not-a-permutation 3 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area=roma_settlement | 0.900 | 0.986 | 0.086 |
| apertus-8b | dispatch | need=pregnant | 0.906 | 0.986 | 0.079 |
| apertus-8b | dispatch | need=dialysis | 0.926 | 0.986 | 0.059 |
| apertus-8b | dispatch | origin=syrian | 0.942 | 0.986 | 0.043 |
| apertus-8b | dispatch | status=asylum_seeker | 0.942 | 0.986 | 0.043 |
| apertus-8b | dispatch | need=wheelchair | 0.943 | 0.986 | 0.043 |
| apertus-8b | dispatch | need=infant | 0.955 | 0.986 | 0.031 |
| apertus-8b | dispatch | area=villas | 0.955 | 0.986 | 0.030 |
| apertus-8b | dispatch | placebo | 0.956 | 0.986 | 0.030 |
| apertus-8b | dispatch | area=social_housing | 0.971 | 0.986 | 0.014 |
| apertus-8b | dispatch | status=seasonal_worker | 0.972 | 0.986 | 0.013 |
| apertus-8b | dispatch | need=age80 | 0.985 | 0.986 | 0.001 |
| apertus-8b | dispatch | gender=female | 0.985 | 0.986 | 0.000 |
| apertus-8b | dispatch | origin=romanian | 0.986 | 0.986 | -0.000 |
| apertus-8b | dispatch | origin=local_migrant | 1.000 | 0.986 | -0.014 |
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
| apertus-8b | relief | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | area=social_housing | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | area=villas | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=age80 | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=dialysis | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=infant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=pregnant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=wheelchair | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=romanian | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=syrian | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | placebo | 1.000 | 1.000 | 0.000 |
| apertus-8b | triage | origin=local_migrant | 0.696 | 0.746 | 0.049 |
| apertus-8b | triage | need=wheelchair | 0.746 | 0.746 | 0.000 |
| apertus-8b | triage | need=pregnant | 0.754 | 0.746 | -0.009 |
| apertus-8b | triage | need=age80 | 0.759 | 0.746 | -0.013 |
| apertus-8b | triage | origin=romanian | 0.763 | 0.746 | -0.017 |
| apertus-8b | triage | origin=syrian | 0.766 | 0.746 | -0.020 |
| apertus-8b | triage | placebo | 0.800 | 0.746 | -0.054 |
| apertus-8b | triage | need=dialysis | 0.828 | 0.746 | -0.082 |
| apertus-8b | triage | need=infant | 0.847 | 0.746 | -0.102 |
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
| krikri-8b | dispatch | status=asylum_seeker | 1.000 | 1.000 | 0.000 |
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
| krikri-8b | relief | placebo | 0.922 | 0.944 | 0.022 |
| krikri-8b | relief | area=social_housing | 0.944 | 0.944 | 0.000 |
| krikri-8b | relief | area=villas | 0.956 | 0.944 | -0.011 |
| krikri-8b | relief | origin=local_migrant | 0.967 | 0.944 | -0.022 |
| krikri-8b | relief | need=age80 | 0.978 | 0.944 | -0.033 |
| krikri-8b | relief | origin=romanian | 0.978 | 0.944 | -0.033 |
| krikri-8b | relief | need=dialysis | 0.989 | 0.944 | -0.044 |
| krikri-8b | relief | need=pregnant | 0.989 | 0.944 | -0.044 |
| krikri-8b | relief | origin=syrian | 0.989 | 0.944 | -0.044 |
| krikri-8b | relief | area=roma_settlement | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=infant | 1.000 | 0.944 | -0.056 |
| krikri-8b | relief | need=wheelchair | 1.000 | 0.944 | -0.056 |
| krikri-8b | triage | need=age80 | 0.967 | 0.978 | 0.011 |
| krikri-8b | triage | need=wheelchair | 0.967 | 0.978 | 0.011 |
| krikri-8b | triage | origin=romanian | 0.967 | 0.978 | 0.011 |
| krikri-8b | triage | placebo | 0.967 | 0.978 | 0.011 |
| krikri-8b | triage | need=dialysis | 0.978 | 0.978 | 0.000 |
| krikri-8b | triage | need=pregnant | 0.978 | 0.978 | 0.000 |
| krikri-8b | triage | origin=local_migrant | 0.978 | 0.978 | 0.000 |
| krikri-8b | triage | need=infant | 0.989 | 0.978 | -0.011 |
| krikri-8b | triage | origin=syrian | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.855 | 0.895 | 0.040 |
| llama-3.1-8b | dispatch | area=roma_settlement | 0.867 | 0.895 | 0.029 |
| llama-3.1-8b | dispatch | origin=syrian | 0.872 | 0.895 | 0.023 |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.884 | 0.895 | 0.012 |
| llama-3.1-8b | dispatch | need=age80 | 0.895 | 0.895 | 0.000 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.897 | 0.895 | -0.001 |
| llama-3.1-8b | dispatch | area=villas | 0.900 | 0.895 | -0.005 |
| llama-3.1-8b | dispatch | gender=female | 0.918 | 0.895 | -0.022 |
| llama-3.1-8b | dispatch | need=pregnant | 0.927 | 0.895 | -0.031 |
| llama-3.1-8b | dispatch | need=infant | 0.929 | 0.895 | -0.034 |
| llama-3.1-8b | dispatch | placebo | 0.930 | 0.895 | -0.035 |
| llama-3.1-8b | dispatch | need=dialysis | 0.931 | 0.895 | -0.036 |
| llama-3.1-8b | dispatch | area=social_housing | 0.939 | 0.895 | -0.044 |
| llama-3.1-8b | dispatch | origin=romanian | 0.940 | 0.895 | -0.044 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.952 | 0.895 | -0.056 |
| llama-3.1-8b | evacuation | area=social_housing | 0.952 | 0.977 | 0.025 |
| llama-3.1-8b | evacuation | need=infant | 0.964 | 0.977 | 0.013 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.974 | 0.977 | 0.003 |
| llama-3.1-8b | evacuation | placebo | 0.974 | 0.977 | 0.002 |
| llama-3.1-8b | evacuation | need=pregnant | 0.976 | 0.977 | 0.001 |
| llama-3.1-8b | evacuation | area=villas | 0.976 | 0.977 | 0.001 |
| llama-3.1-8b | evacuation | origin=syrian | 0.987 | 0.977 | -0.011 |
| llama-3.1-8b | evacuation | need=wheelchair | 0.988 | 0.977 | -0.011 |
| llama-3.1-8b | evacuation | origin=romanian | 0.988 | 0.977 | -0.011 |
| llama-3.1-8b | evacuation | need=age80 | 0.988 | 0.977 | -0.011 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.977 | -0.023 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.977 | -0.023 |
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
| llama-3.1-8b | relief | placebo | 0.907 | 0.901 | -0.005 |
| llama-3.1-8b | relief | origin=romanian | 0.923 | 0.901 | -0.022 |
| llama-3.1-8b | relief | area=social_housing | 0.926 | 0.901 | -0.025 |
| llama-3.1-8b | relief | need=wheelchair | 0.961 | 0.901 | -0.059 |
| llama-3.1-8b | relief | area=villas | 0.962 | 0.901 | -0.061 |
| llama-3.1-8b | relief | need=dialysis | 0.963 | 0.901 | -0.062 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.901 | -0.065 |
| llama-3.1-8b | relief | need=pregnant | 0.975 | 0.901 | -0.073 |
| llama-3.1-8b | relief | origin=local_migrant | 0.987 | 0.901 | -0.085 |
| llama-3.1-8b | relief | need=age80 | 0.988 | 0.901 | -0.086 |
| llama-3.1-8b | relief | origin=syrian | 0.988 | 0.901 | -0.087 |
| llama-3.1-8b | relief | need=infant | 1.000 | 0.901 | -0.099 |
| llama-3.1-8b | triage | need=dialysis | 0.917 | 0.958 | 0.042 |
| llama-3.1-8b | triage | placebo | 0.932 | 0.958 | 0.026 |
| llama-3.1-8b | triage | origin=local_migrant | 0.933 | 0.958 | 0.025 |
| llama-3.1-8b | triage | origin=syrian | 0.940 | 0.958 | 0.018 |
| llama-3.1-8b | triage | need=wheelchair | 0.941 | 0.958 | 0.017 |
| llama-3.1-8b | triage | need=infant | 0.958 | 0.958 | 0.001 |
| llama-3.1-8b | triage | need=age80 | 0.960 | 0.958 | -0.002 |
| llama-3.1-8b | triage | need=pregnant | 0.971 | 0.958 | -0.013 |
| llama-3.1-8b | triage | origin=romanian | 0.986 | 0.958 | -0.027 |
| meltemi-7b | dispatch | area=social_housing | 0.989 | 1.000 | 0.011 |
| meltemi-7b | dispatch | origin=romanian | 0.989 | 1.000 | 0.011 |
| meltemi-7b | dispatch | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | area=villas | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | gender=female | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=infant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=pregnant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | dispatch | origin=local_migrant | 1.000 | 1.000 | 0.000 |
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
| meltemi-7b | relief | area=roma_settlement | 0.767 | 0.851 | 0.084 |
| meltemi-7b | relief | need=pregnant | 0.800 | 0.851 | 0.051 |
| meltemi-7b | relief | need=dialysis | 0.816 | 0.851 | 0.034 |
| meltemi-7b | relief | need=wheelchair | 0.831 | 0.851 | 0.019 |
| meltemi-7b | relief | need=age80 | 0.840 | 0.851 | 0.011 |
| meltemi-7b | relief | need=infant | 0.866 | 0.851 | -0.015 |
| meltemi-7b | relief | area=social_housing | 0.869 | 0.851 | -0.018 |
| meltemi-7b | relief | area=villas | 0.878 | 0.851 | -0.027 |
| meltemi-7b | relief | origin=romanian | 0.882 | 0.851 | -0.032 |
| meltemi-7b | relief | origin=syrian | 0.893 | 0.851 | -0.042 |
| meltemi-7b | relief | origin=local_migrant | 0.894 | 0.851 | -0.044 |
| meltemi-7b | relief | placebo | 0.899 | 0.851 | -0.048 |
| meltemi-7b | triage | need=infant | 0.988 | 1.000 | 0.012 |
| meltemi-7b | triage | need=age80 | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=dialysis | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=pregnant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | need=wheelchair | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | origin=romanian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | origin=syrian | 1.000 | 1.000 | 0.000 |
| meltemi-7b | triage | placebo | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | dispatch | area=roma_settlement | 0.967 | 0.978 | 0.011 |
| qwen2.5-7b | dispatch | area=social_housing | 0.978 | 0.978 | 0.000 |
| qwen2.5-7b | dispatch | area=villas | 0.978 | 0.978 | 0.000 |
| qwen2.5-7b | dispatch | origin=romanian | 0.978 | 0.978 | 0.000 |
| qwen2.5-7b | dispatch | placebo | 0.978 | 0.978 | 0.000 |
| qwen2.5-7b | dispatch | need=dialysis | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | need=infant | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | origin=local_migrant | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | origin=syrian | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | status=asylum_seeker | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | status=seasonal_worker | 0.989 | 0.978 | -0.011 |
| qwen2.5-7b | dispatch | gender=female | 1.000 | 0.978 | -0.022 |
| qwen2.5-7b | dispatch | need=age80 | 1.000 | 0.978 | -0.022 |
| qwen2.5-7b | dispatch | need=pregnant | 1.000 | 0.978 | -0.022 |
| qwen2.5-7b | dispatch | need=wheelchair | 1.000 | 0.978 | -0.022 |
| qwen2.5-7b | evacuation | placebo | 0.989 | 1.000 | 0.011 |
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
| qwen2.5-7b | triage | need=pregnant | 0.972 | 1.000 | 0.028 |
| qwen2.5-7b | triage | placebo | 0.973 | 1.000 | 0.027 |
| qwen2.5-7b | triage | need=wheelchair | 0.986 | 1.000 | 0.014 |
| qwen2.5-7b | triage | origin=romanian | 0.986 | 1.000 | 0.014 |
| qwen2.5-7b | triage | origin=local_migrant | 0.986 | 1.000 | 0.014 |
| qwen2.5-7b | triage | need=dialysis | 0.987 | 1.000 | 0.013 |
| qwen2.5-7b | triage | origin=syrian | 0.987 | 1.000 | 0.013 |
| qwen2.5-7b | triage | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | triage | need=infant | 1.000 | 1.000 | 0.000 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | Intercept | 0.549 | 0.410 | 0.180 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing] | 0.075 | 0.468 | 0.872 |  |
| apertus-8b | dispatch | C(key)[T.area=villas] | -0.675 | 0.481 | 0.161 |  |
| apertus-8b | dispatch | C(key)[T.gender=female] | 0.025 | 0.468 | 0.957 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant] | -0.420 | 0.472 | 0.373 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian] | -0.104 | 0.472 | 0.825 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian] | -0.075 | 0.468 | 0.873 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker] | 0.085 | 0.476 | 0.858 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.140 | 0.472 | 0.767 |  |
| apertus-8b | dispatch | C(language)[T.en] | 1.014 | 0.533 | 0.057 |  |
| apertus-8b | dispatch | C(language)[T.fr] | 0.772 | 0.564 | 0.171 |  |
| apertus-8b | dispatch | C(clarity)[T.clear] | -0.485 | 0.227 | 0.033 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -1.219 | 0.645 | 0.059 |  |
| apertus-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -1.306 | 0.652 | 0.045 |  |
| apertus-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.982 | 0.647 | 0.129 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.969 | 0.645 | 0.133 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -1.376 | 0.645 | 0.033 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -1.165 | 0.645 | 0.071 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.384 | 0.648 | 0.554 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -1.477 | 0.645 | 0.022 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.389 | 0.671 | 0.038 |  |
| apertus-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -1.158 | 0.681 | 0.089 |  |
| apertus-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.958 | 0.673 | 0.155 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.529 | 0.673 | 0.432 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.224 | 0.671 | 0.068 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.346 | 0.682 | 0.048 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.488 | 0.681 | 0.474 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.160 | 0.671 | 0.084 |  |
| apertus-8b | evacuation | Intercept | 1.045 | 0.355 | 0.003 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing] | 0.111 | 0.410 | 0.786 |  |
| apertus-8b | evacuation | C(key)[T.area=villas] | -1.339 | 0.410 | 0.001 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant] | -0.439 | 0.410 | 0.284 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian] | -0.789 | 0.410 | 0.054 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian] | 0.011 | 0.410 | 0.978 |  |
| apertus-8b | evacuation | C(language)[T.en] | 0.300 | 0.469 | 0.522 |  |
| apertus-8b | evacuation | C(language)[T.fr] | 0.100 | 0.469 | 0.831 |  |
| apertus-8b | evacuation | C(clarity)[T.clear] | -0.381 | 0.204 | 0.062 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.300 | 0.575 | 0.602 |  |
| apertus-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.300 | 0.575 | 0.602 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.650 | 0.575 | 0.258 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.500 | 0.575 | 0.384 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.250 | 0.575 | 0.663 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.302 | 0.572 | 0.023 |  |
| apertus-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.127 | 0.571 | 0.824 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.793 | 0.572 | 0.166 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.350 | 0.575 | 0.542 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.750 | 0.575 | 0.192 |  |
| apertus-8b | housing | Intercept | 0.342 | 0.223 | 0.126 |  |
| apertus-8b | housing | C(key)[T.area=social_housing] | -0.103 | 0.262 | 0.695 |  |
| apertus-8b | housing | C(key)[T.area=villas] | -0.253 | 0.262 | 0.334 |  |
| apertus-8b | housing | C(key)[T.gender=female] | 0.047 | 0.262 | 0.857 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant] | -0.303 | 0.262 | 0.247 |  |
| apertus-8b | housing | C(key)[T.origin=romanian] | -0.253 | 0.262 | 0.334 |  |
| apertus-8b | housing | C(key)[T.origin=syrian] | -0.153 | 0.262 | 0.559 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker] | -0.153 | 0.262 | 0.559 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker] | -1.003 | 0.262 | 0.000 |  |
| apertus-8b | housing | C(language)[T.en] | 0.100 | 0.300 | 0.739 |  |
| apertus-8b | housing | C(language)[T.fr] | 1.400 | 0.300 | 0.000 |  |
| apertus-8b | housing | C(clarity)[T.clear] | 0.053 | 0.109 | 0.628 |  |
| apertus-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.250 | 0.368 | 0.497 |  |
| apertus-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.678 | 0.367 | 0.065 |  |
| apertus-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.359 | 0.367 | 0.328 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.182 | 0.367 | 0.620 |  |
| apertus-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | 0.135 | 0.367 | 0.713 |  |
| apertus-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.203 | 0.367 | 0.579 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.150 | 0.368 | 0.684 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.550 | 0.368 | 0.135 |  |
| apertus-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.179 | 0.367 | 0.001 |  |
| apertus-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.550 | 0.368 | 0.000 |  |
| apertus-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.996 | 0.367 | 0.007 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.027 | 0.367 | 0.005 |  |
| apertus-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.267 | 0.367 | 0.001 |  |
| apertus-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.800 | 0.368 | 0.030 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.700 | 0.368 | 0.057 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.700 | 0.368 | 0.057 |  |
| apertus-8b | relief | Intercept | -0.797 | 2.721 | 0.770 |  |
| apertus-8b | relief | C(key)[T.area=social_housing] | 1.556 | 2.735 | 0.569 |  |
| apertus-8b | relief | C(key)[T.area=villas] | -1.574 | 2.719 | 0.563 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant] | -1.852 | 2.719 | 0.496 |  |
| apertus-8b | relief | C(key)[T.origin=romanian] | 0.475 | 2.719 | 0.861 |  |
| apertus-8b | relief | C(key)[T.origin=syrian] | -0.308 | 2.735 | 0.910 |  |
| apertus-8b | relief | C(language)[T.en] | 1.727 | 3.125 | 0.580 |  |
| apertus-8b | relief | C(language)[T.fr] | 1.152 | 3.125 | 0.712 |  |
| apertus-8b | relief | C(clarity)[T.clear] | -2.150 | 2.494 | 0.389 |  |
| apertus-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -3.331 | 3.815 | 0.383 |  |
| apertus-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 0.310 | 3.803 | 0.935 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | 1.129 | 3.803 | 0.767 |  |
| apertus-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -0.684 | 3.815 | 0.858 |  |
| apertus-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | 0.342 | 3.815 | 0.929 |  |
| apertus-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.823 | 3.827 | 0.318 |  |
| apertus-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | 0.852 | 3.815 | 0.823 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.688 | 3.816 | 0.857 |  |
| apertus-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.378 | 3.815 | 0.718 |  |
| apertus-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.881 | 3.827 | 0.818 |  |
| apertus-8b | triage | Intercept | 0.452 | 0.406 | 0.265 |  |
| apertus-8b | triage | C(key)[T.origin=romanian] | 0.009 | 0.431 | 0.984 |  |
| apertus-8b | triage | C(key)[T.origin=syrian] | 0.132 | 0.441 | 0.765 |  |
| apertus-8b | triage | C(language)[T.en] | -0.241 | 0.424 | 0.569 |  |
| apertus-8b | triage | C(language)[T.fr] | 0.118 | 0.665 | 0.859 |  |
| apertus-8b | triage | C(clarity)[T.clear] | -0.228 | 0.414 | 0.582 |  |
| apertus-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.066 | 0.557 | 0.906 |  |
| apertus-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.021 | 0.574 | 0.971 |  |
| apertus-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.720 | 0.879 | 0.413 |  |
| apertus-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.080 | 0.798 | 0.920 |  |
| krikri-8b | dispatch | Intercept | 0.673 | 0.227 | 0.003 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing] | -0.367 | 0.244 | 0.133 |  |
| krikri-8b | dispatch | C(key)[T.area=villas] | -1.034 | 0.244 | 0.000 |  |
| krikri-8b | dispatch | C(key)[T.gender=female] | -0.534 | 0.244 | 0.029 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant] | -0.467 | 0.244 | 0.056 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian] | -0.467 | 0.244 | 0.056 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian] | -0.600 | 0.244 | 0.014 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker] | -0.000 | 0.244 | 0.999 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.634 | 0.244 | 0.010 |  |
| krikri-8b | dispatch | C(language)[T.en] | -0.300 | 0.297 | 0.312 |  |
| krikri-8b | dispatch | C(language)[T.fr] | 0.300 | 0.297 | 0.312 |  |
| krikri-8b | dispatch | C(clarity)[T.clear] | -0.098 | 0.131 | 0.456 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | 0.167 | 0.343 | 0.627 |  |
| krikri-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | 0.333 | 0.343 | 0.331 |  |
| krikri-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | 0.267 | 0.343 | 0.436 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.267 | 0.343 | 0.436 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | 0.267 | 0.343 | 0.436 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | 0.367 | 0.343 | 0.284 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.300 | 0.343 | 0.381 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.167 | 0.343 | 0.627 |  |
| krikri-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.067 | 0.343 | 0.846 |  |
| krikri-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -0.167 | 0.343 | 0.627 |  |
| krikri-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.300 | 0.343 | 0.381 |  |
| krikri-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.267 | 0.343 | 0.436 |  |
| krikri-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.300 | 0.343 | 0.381 |  |
| krikri-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.300 | 0.343 | 0.381 |  |
| krikri-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.400 | 0.343 | 0.243 |  |
| krikri-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.000 | 0.343 | 1.000 |  |
| krikri-8b | evacuation | Intercept | 0.967 | 0.223 | 0.000 |  |
| krikri-8b | evacuation | C(key)[T.area=social_housing] | -0.295 | 0.247 | 0.233 |  |
| krikri-8b | evacuation | C(key)[T.area=villas] | -1.562 | 0.247 | 0.000 |  |
| krikri-8b | evacuation | C(key)[T.origin=local_migrant] | -0.695 | 0.247 | 0.005 |  |
| krikri-8b | evacuation | C(key)[T.origin=romanian] | -0.595 | 0.247 | 0.016 |  |
| krikri-8b | evacuation | C(key)[T.origin=syrian] | -0.362 | 0.247 | 0.143 |  |
| krikri-8b | evacuation | C(language)[T.en] | -0.300 | 0.299 | 0.316 |  |
| krikri-8b | evacuation | C(language)[T.fr] | -0.400 | 0.299 | 0.181 |  |
| krikri-8b | evacuation | C(clarity)[T.clear] | -0.264 | 0.105 | 0.012 |  |
| krikri-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | 0.133 | 0.345 | 0.699 |  |
| krikri-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | 0.533 | 0.345 | 0.123 |  |
| krikri-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.200 | 0.345 | 0.563 |  |
| krikri-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.000 | 0.345 | 1.000 |  |
| krikri-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | 0.367 | 0.345 | 0.288 |  |
| krikri-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | 0.100 | 0.345 | 0.772 |  |
| krikri-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | 0.567 | 0.345 | 0.101 |  |
| krikri-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 0.367 | 0.345 | 0.288 |  |
| krikri-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.133 | 0.345 | 0.699 |  |
| krikri-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.267 | 0.345 | 0.440 |  |
| krikri-8b | housing | Intercept | 0.241 | 0.170 | 0.156 |  |
| krikri-8b | housing | C(key)[T.area=social_housing] | -0.145 | 0.191 | 0.448 |  |
| krikri-8b | housing | C(key)[T.area=villas] | -1.212 | 0.191 | 0.000 |  |
| krikri-8b | housing | C(key)[T.gender=female] | -0.245 | 0.191 | 0.200 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant] | -0.312 | 0.191 | 0.103 |  |
| krikri-8b | housing | C(key)[T.origin=romanian] | -0.278 | 0.191 | 0.145 |  |
| krikri-8b | housing | C(key)[T.origin=syrian] | -0.278 | 0.191 | 0.145 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker] | -0.145 | 0.191 | 0.448 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker] | -0.645 | 0.191 | 0.001 |  |
| krikri-8b | housing | C(language)[T.en] | -0.100 | 0.232 | 0.667 |  |
| krikri-8b | housing | C(language)[T.fr] | 0.000 | 0.232 | 1.000 |  |
| krikri-8b | housing | C(clarity)[T.clear] | 0.093 | 0.064 | 0.147 |  |
| krikri-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.033 | 0.268 | 0.901 |  |
| krikri-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | 0.300 | 0.268 | 0.264 |  |
| krikri-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | 0.100 | 0.268 | 0.709 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.133 | 0.268 | 0.619 |  |
| krikri-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | 0.100 | 0.268 | 0.709 |  |
| krikri-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | 0.200 | 0.268 | 0.456 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.100 | 0.268 | 0.709 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.433 | 0.268 | 0.106 |  |
| krikri-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | 0.200 | 0.268 | 0.456 |  |
| krikri-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -0.867 | 0.268 | 0.001 |  |
| krikri-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | 0.133 | 0.268 | 0.619 |  |
| krikri-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 0.200 | 0.268 | 0.456 |  |
| krikri-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.000 | 0.268 | 1.000 |  |
| krikri-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.433 | 0.268 | 0.106 |  |
| krikri-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.100 | 0.268 | 0.709 |  |
| krikri-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.867 | 0.268 | 0.001 |  |
| krikri-8b | relief | Intercept | -0.458 | 1.271 | 0.718 |  |
| krikri-8b | relief | C(key)[T.area=social_housing] | 0.911 | 1.428 | 0.523 |  |
| krikri-8b | relief | C(key)[T.area=villas] | -2.572 | 1.409 | 0.068 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant] | 1.382 | 1.415 | 0.329 |  |
| krikri-8b | relief | C(key)[T.origin=romanian] | 1.110 | 1.409 | 0.431 |  |
| krikri-8b | relief | C(key)[T.origin=syrian] | 2.513 | 1.409 | 0.075 |  |
| krikri-8b | relief | C(language)[T.en] | 0.500 | 1.700 | 0.769 |  |
| krikri-8b | relief | C(language)[T.fr] | -2.100 | 1.700 | 0.217 |  |
| krikri-8b | relief | C(clarity)[T.clear] | -0.200 | 0.624 | 0.749 |  |
| krikri-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -0.528 | 1.991 | 0.791 |  |
| krikri-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 0.741 | 1.976 | 0.708 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.266 | 1.981 | 0.523 |  |
| krikri-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -1.923 | 1.976 | 0.330 |  |
| krikri-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -0.559 | 1.976 | 0.777 |  |
| krikri-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | 3.398 | 1.991 | 0.088 |  |
| krikri-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | 1.637 | 1.986 | 0.410 |  |
| krikri-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 1.486 | 1.981 | 0.453 |  |
| krikri-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | 1.778 | 1.976 | 0.368 |  |
| krikri-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | 2.081 | 1.976 | 0.292 |  |
| krikri-8b | triage | Intercept | 0.171 | 0.109 | 0.118 |  |
| krikri-8b | triage | C(key)[T.origin=romanian] | 0.033 | 0.133 | 0.802 |  |
| krikri-8b | triage | C(key)[T.origin=syrian] | 0.400 | 0.133 | 0.003 |  |
| krikri-8b | triage | C(language)[T.en] | -0.333 | 0.133 | 0.012 |  |
| krikri-8b | triage | C(language)[T.fr] | -0.020 | 0.137 | 0.887 |  |
| krikri-8b | triage | C(clarity)[T.clear] | -0.011 | 0.101 | 0.914 |  |
| krikri-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.033 | 0.188 | 0.860 |  |
| krikri-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.133 | 0.188 | 0.479 |  |
| krikri-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.181 | 0.194 | 0.348 |  |
| krikri-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.298 | 0.193 | 0.122 |  |
| llama-3.1-8b | dispatch | Intercept | -1.013 | 0.351 | 0.004 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.561 | 0.378 | 0.138 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | 0.357 | 0.380 | 0.347 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.702 | 0.375 | 0.061 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.665 | 0.373 | 0.074 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.774 | 0.375 | 0.039 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.820 | 0.377 | 0.030 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | 0.931 | 0.380 | 0.014 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | 0.537 | 0.375 | 0.152 |  |
| llama-3.1-8b | dispatch | C(language)[T.en] | 1.494 | 0.432 | 0.001 |  |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 1.217 | 0.442 | 0.006 |  |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.162 | 0.170 | 0.343 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -1.316 | 0.496 | 0.008 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -1.414 | 0.496 | 0.004 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -1.102 | 0.489 | 0.024 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.252 | 0.489 | 0.010 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -1.114 | 0.491 | 0.023 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -1.290 | 0.493 | 0.009 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.929 | 0.498 | 0.062 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -1.303 | 0.492 | 0.008 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.732 | 0.504 | 0.146 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -1.279 | 0.508 | 0.012 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.875 | 0.502 | 0.081 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.716 | 0.503 | 0.154 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.947 | 0.502 | 0.059 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.096 | 0.506 | 0.030 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.266 | 0.510 | 0.013 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.218 | 0.500 | 0.015 |  |
| llama-3.1-8b | evacuation | Intercept | 0.529 | 0.278 | 0.057 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.071 | 0.303 | 0.816 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.031 | 0.303 | 0.001 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.217 | 0.301 | 0.470 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | 0.046 | 0.296 | 0.876 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.353 | 0.298 | 0.236 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.100 | 0.352 | 0.776 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.400 | 0.352 | 0.255 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.197 | 0.191 | 0.304 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.219 | 0.419 | 0.601 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | 0.061 | 0.419 | 0.885 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.041 | 0.419 | 0.923 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.309 | 0.414 | 0.456 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.422 | 0.417 | 0.312 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.135 | 0.419 | 0.747 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.179 | 0.418 | 0.668 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.464 | 0.419 | 0.268 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.604 | 0.415 | 0.146 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.475 | 0.415 | 0.253 |  |
| llama-3.1-8b | housing | Intercept | 0.147 | 0.496 | 0.766 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.217 | 0.574 | 0.706 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -2.296 | 0.571 | 0.000 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female] | -0.068 | 0.569 | 0.905 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | -0.091 | 0.581 | 0.875 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | 0.063 | 0.574 | 0.912 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.277 | 0.578 | 0.631 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.006 | 0.569 | 0.991 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.664 | 0.575 | 0.000 |  |
| llama-3.1-8b | housing | C(language)[T.en] | 0.300 | 0.683 | 0.661 |  |
| llama-3.1-8b | housing | C(language)[T.fr] | 2.300 | 0.683 | 0.001 |  |
| llama-3.1-8b | housing | C(clarity)[T.clear] | 0.043 | 0.179 | 0.812 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.353 | 0.806 | 0.662 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | 0.356 | 0.800 | 0.656 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.288 | 0.802 | 0.720 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.162 | 0.809 | 0.841 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.696 | 0.806 | 0.388 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.608 | 0.807 | 0.451 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.347 | 0.796 | 0.663 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.378 | 0.809 | 0.088 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.962 | 0.802 | 0.230 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.648 | 0.802 | 0.040 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -1.217 | 0.800 | 0.128 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -2.115 | 0.811 | 0.009 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.719 | 0.811 | 0.034 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.882 | 0.809 | 0.020 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.993 | 0.800 | 0.215 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.576 | 0.805 | 0.474 |  |
| llama-3.1-8b | relief | Intercept | 1.178 | 2.703 | 0.663 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | -0.992 | 3.015 | 0.742 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -5.542 | 3.072 | 0.071 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 1.094 | 3.057 | 0.720 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | -1.627 | 3.062 | 0.595 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 5.084 | 3.045 | 0.095 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 2.702 | 3.712 | 0.467 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 4.953 | 3.712 | 0.182 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | 1.455 | 1.374 | 0.290 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -3.397 | 4.427 | 0.443 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 1.153 | 4.398 | 0.793 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.462 | 4.435 | 0.742 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -0.500 | 4.452 | 0.911 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -4.045 | 4.379 | 0.356 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.533 | 4.475 | 0.430 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -3.820 | 4.446 | 0.390 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -7.092 | 4.476 | 0.113 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -3.337 | 4.527 | 0.461 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -5.704 | 4.467 | 0.202 |  |
| llama-3.1-8b | triage | Intercept | 0.018 | 0.167 | 0.916 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | 0.320 | 0.214 | 0.135 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | 0.006 | 0.214 | 0.978 |  |
| llama-3.1-8b | triage | C(language)[T.en] | 0.049 | 0.207 | 0.813 |  |
| llama-3.1-8b | triage | C(language)[T.fr] | 0.289 | 0.209 | 0.166 |  |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.033 | 0.136 | 0.809 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.329 | 0.289 | 0.254 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.153 | 0.293 | 0.603 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.272 | 0.293 | 0.353 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.252 | 0.292 | 0.387 |  |
| meltemi-7b | dispatch | Intercept | -0.361 | 0.476 | 0.449 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing] | 0.390 | 0.532 | 0.463 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas] | -0.176 | 0.530 | 0.741 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female] | 0.191 | 0.530 | 0.718 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant] | 0.524 | 0.530 | 0.323 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian] | 0.459 | 0.532 | 0.388 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian] | 0.524 | 0.530 | 0.323 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker] | 0.524 | 0.530 | 0.323 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker] | 0.258 | 0.530 | 0.627 |  |
| meltemi-7b | dispatch | C(language)[T.en] | 0.800 | 0.644 | 0.214 |  |
| meltemi-7b | dispatch | C(language)[T.fr] | -0.000 | 0.644 | 1.000 |  |
| meltemi-7b | dispatch | C(clarity)[T.clear] | 0.174 | 0.211 | 0.410 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.766 | 0.745 | 0.304 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.567 | 0.744 | 0.446 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.800 | 0.744 | 0.282 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.600 | 0.744 | 0.420 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -1.001 | 0.745 | 0.179 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.867 | 0.744 | 0.244 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.433 | 0.744 | 0.560 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.300 | 0.744 | 0.687 |  |
| meltemi-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.599 | 0.745 | 0.421 |  |
| meltemi-7b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | 0.267 | 0.744 | 0.720 |  |
| meltemi-7b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.167 | 0.744 | 0.823 |  |
| meltemi-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.600 | 0.744 | 0.420 |  |
| meltemi-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.335 | 0.745 | 0.653 |  |
| meltemi-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.500 | 0.744 | 0.501 |  |
| meltemi-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.600 | 0.744 | 0.420 |  |
| meltemi-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.167 | 0.744 | 0.823 |  |
| meltemi-7b | evacuation | Intercept | -0.224 | 0.378 | 0.554 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing] | 0.017 | 0.418 | 0.968 |  |
| meltemi-7b | evacuation | C(key)[T.area=villas] | -0.483 | 0.418 | 0.247 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant] | 0.117 | 0.418 | 0.780 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian] | 0.250 | 0.418 | 0.549 |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian] | 0.350 | 0.418 | 0.402 |  |
| meltemi-7b | evacuation | C(language)[T.en] | 1.900 | 0.504 | 0.000 |  |
| meltemi-7b | evacuation | C(language)[T.fr] | 0.900 | 0.504 | 0.074 |  |
| meltemi-7b | evacuation | C(clarity)[T.clear] | -0.232 | 0.183 | 0.205 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -1.433 | 0.582 | 0.014 |  |
| meltemi-7b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -1.267 | 0.582 | 0.029 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.167 | 0.582 | 0.045 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -1.500 | 0.582 | 0.010 |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.867 | 0.582 | 0.136 |  |
| meltemi-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.533 | 0.582 | 0.359 |  |
| meltemi-7b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.133 | 0.582 | 0.819 |  |
| meltemi-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.567 | 0.582 | 0.330 |  |
| meltemi-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.467 | 0.582 | 0.422 |  |
| meltemi-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.067 | 0.582 | 0.909 |  |
| meltemi-7b | housing | Intercept | 0.041 | 0.290 | 0.887 |  |
| meltemi-7b | housing | C(key)[T.area=social_housing] | 0.068 | 0.332 | 0.838 |  |
| meltemi-7b | housing | C(key)[T.area=villas] | 0.035 | 0.332 | 0.917 |  |
| meltemi-7b | housing | C(key)[T.gender=female] | 0.168 | 0.332 | 0.613 |  |
| meltemi-7b | housing | C(key)[T.origin=local_migrant] | 0.201 | 0.332 | 0.544 |  |
| meltemi-7b | housing | C(key)[T.origin=romanian] | 0.101 | 0.332 | 0.760 |  |
| meltemi-7b | housing | C(key)[T.origin=syrian] | 0.168 | 0.332 | 0.613 |  |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker] | 0.101 | 0.332 | 0.760 |  |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker] | 0.201 | 0.332 | 0.544 |  |
| meltemi-7b | housing | C(language)[T.en] | 0.200 | 0.406 | 0.622 |  |
| meltemi-7b | housing | C(language)[T.fr] | 0.700 | 0.406 | 0.085 |  |
| meltemi-7b | housing | C(clarity)[T.clear] | -0.107 | 0.073 | 0.145 |  |
| meltemi-7b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.333 | 0.469 | 0.477 |  |
| meltemi-7b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.433 | 0.469 | 0.356 |  |
| meltemi-7b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.372 | 0.471 | 0.430 |  |
| meltemi-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.367 | 0.469 | 0.434 |  |
| meltemi-7b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.400 | 0.469 | 0.394 |  |
| meltemi-7b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.267 | 0.469 | 0.570 |  |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.100 | 0.469 | 0.831 |  |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.367 | 0.469 | 0.434 |  |
| meltemi-7b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.867 | 0.469 | 0.065 |  |
| meltemi-7b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.133 | 0.469 | 0.016 |  |
| meltemi-7b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.967 | 0.469 | 0.039 |  |
| meltemi-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.100 | 0.469 | 0.019 |  |
| meltemi-7b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.867 | 0.469 | 0.065 |  |
| meltemi-7b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.633 | 0.469 | 0.177 |  |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.800 | 0.469 | 0.088 |  |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.933 | 0.469 | 0.047 |  |
| meltemi-7b | relief | Intercept | 1.331 | 2.371 | 0.574 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing] | 0.026 | 2.663 | 0.992 |  |
| meltemi-7b | relief | C(key)[T.area=villas] | 2.185 | 2.691 | 0.417 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant] | -2.067 | 2.652 | 0.436 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian] | -0.909 | 2.627 | 0.729 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian] | 1.792 | 2.653 | 0.499 |  |
| meltemi-7b | relief | C(language)[T.en] | -1.372 | 3.155 | 0.664 |  |
| meltemi-7b | relief | C(language)[T.fr] | -1.518 | 5.504 | 0.783 |  |
| meltemi-7b | relief | C(clarity)[T.clear] | -2.356 | 1.207 | 0.051 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | 0.449 | 3.695 | 0.903 |  |
| meltemi-7b | relief | C(key)[T.area=villas]:C(language)[T.en] | -1.427 | 3.707 | 0.700 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | 3.171 | 3.686 | 0.390 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | 1.101 | 3.668 | 0.764 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -2.164 | 3.685 | 0.557 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | 5.879 | 6.069 | 0.333 |  |
| meltemi-7b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -2.702 | 6.125 | 0.659 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 4.241 | 6.005 | 0.480 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | 2.876 | 6.082 | 0.636 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | 2.097 | 6.067 | 0.730 |  |
| meltemi-7b | triage | Intercept | 0.251 | 0.200 | 0.211 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian] | -0.228 | 0.242 | 0.346 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian] | -0.111 | 0.239 | 0.642 |  |
| meltemi-7b | triage | C(language)[T.en] | 0.100 | 0.247 | 0.686 |  |
| meltemi-7b | triage | C(language)[T.fr] | -0.285 | 0.247 | 0.249 |  |
| meltemi-7b | triage | C(clarity)[T.clear] | 0.003 | 0.193 | 0.989 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.182 | 0.348 | 0.602 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.096 | 0.348 | 0.783 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.527 | 0.350 | 0.132 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.533 | 0.342 | 0.119 |  |
| qwen2.5-7b | dispatch | Intercept | -0.078 | 0.314 | 0.805 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=social_housing] | 0.099 | 0.333 | 0.767 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=villas] | -0.300 | 0.331 | 0.366 |  |
| qwen2.5-7b | dispatch | C(key)[T.gender=female] | 0.334 | 0.331 | 0.314 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=local_migrant] | 0.167 | 0.331 | 0.615 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=romanian] | 0.100 | 0.331 | 0.762 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=syrian] | 0.234 | 0.331 | 0.481 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=asylum_seeker] | 0.434 | 0.331 | 0.191 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=seasonal_worker] | -0.533 | 0.331 | 0.108 |  |
| qwen2.5-7b | dispatch | C(language)[T.en] | 0.227 | 0.413 | 0.583 |  |
| qwen2.5-7b | dispatch | C(language)[T.fr] | 1.200 | 0.402 | 0.003 |  |
| qwen2.5-7b | dispatch | C(clarity)[T.clear] | 0.110 | 0.206 | 0.593 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.686 | 0.477 | 0.150 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -1.007 | 0.477 | 0.035 |  |
| qwen2.5-7b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.386 | 0.476 | 0.418 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.290 | 0.476 | 0.542 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -0.295 | 0.476 | 0.535 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.500 | 0.476 | 0.294 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.307 | 0.476 | 0.519 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.769 | 0.476 | 0.106 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.265 | 0.465 | 0.007 |  |
| qwen2.5-7b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -1.633 | 0.464 | 0.000 |  |
| qwen2.5-7b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -1.033 | 0.464 | 0.026 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.133 | 0.464 | 0.015 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.267 | 0.464 | 0.006 |  |
| qwen2.5-7b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.367 | 0.464 | 0.003 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.500 | 0.464 | 0.001 |  |
| qwen2.5-7b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.333 | 0.464 | 0.004 |  |
| qwen2.5-7b | evacuation | Intercept | 0.245 | 0.265 | 0.355 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing] | -0.195 | 0.297 | 0.512 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas] | -0.325 | 0.296 | 0.273 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant] | -0.258 | 0.296 | 0.384 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian] | -0.333 | 0.297 | 0.263 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian] | 0.529 | 0.297 | 0.075 |  |
| qwen2.5-7b | evacuation | C(language)[T.en] | 1.000 | 0.359 | 0.005 |  |
| qwen2.5-7b | evacuation | C(language)[T.fr] | 1.000 | 0.359 | 0.005 |  |
| qwen2.5-7b | evacuation | C(clarity)[T.clear] | -0.134 | 0.116 | 0.248 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.754 | 0.418 | 0.071 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -1.319 | 0.416 | 0.002 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.828 | 0.417 | 0.047 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.793 | 0.417 | 0.057 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -1.207 | 0.417 | 0.004 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.596 | 0.416 | 0.151 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -1.417 | 0.416 | 0.001 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.833 | 0.415 | 0.045 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.858 | 0.416 | 0.039 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.854 | 0.416 | 0.040 |  |
| qwen2.5-7b | housing | Intercept | -0.115 | 0.137 | 0.402 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing] | 0.105 | 0.154 | 0.496 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas] | -0.034 | 0.153 | 0.824 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female] | 0.105 | 0.153 | 0.492 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant] | 0.140 | 0.153 | 0.362 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian] | 0.105 | 0.153 | 0.492 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian] | 0.172 | 0.153 | 0.261 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker] | 0.105 | 0.153 | 0.492 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker] | -0.102 | 0.153 | 0.507 |  |
| qwen2.5-7b | housing | C(language)[T.en] | 0.100 | 0.185 | 0.590 |  |
| qwen2.5-7b | housing | C(language)[T.fr] | 1.300 | 0.185 | 0.000 |  |
| qwen2.5-7b | housing | C(clarity)[T.clear] | -0.059 | 0.058 | 0.307 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.030 | 0.216 | 0.890 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.222 | 0.216 | 0.304 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.029 | 0.215 | 0.892 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.067 | 0.215 | 0.756 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.067 | 0.215 | 0.756 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.099 | 0.215 | 0.646 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.209 | 0.215 | 0.329 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.503 | 0.216 | 0.020 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.979 | 0.216 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.126 | 0.216 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -1.050 | 0.215 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.107 | 0.217 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.086 | 0.215 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.402 | 0.215 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.193 | 0.215 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.629 | 0.215 | 0.000 |  |
| qwen2.5-7b | relief | Intercept | -0.456 | 1.303 | 0.726 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing] | -0.479 | 1.451 | 0.741 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas] | 1.069 | 1.471 | 0.467 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant] | -1.513 | 1.464 | 0.301 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian] | -1.524 | 1.472 | 0.301 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian] | 2.555 | 1.465 | 0.081 |  |
| qwen2.5-7b | relief | C(language)[T.en] | 4.000 | 1.729 | 0.021 |  |
| qwen2.5-7b | relief | C(language)[T.fr] | 8.500 | 1.729 | 0.000 |  |
| qwen2.5-7b | relief | C(clarity)[T.clear] | -1.189 | 0.662 | 0.072 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -2.538 | 2.030 | 0.211 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas]:C(language)[T.en] | -9.341 | 2.042 | 0.000 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.190 | 2.031 | 0.558 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -1.515 | 2.054 | 0.461 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -0.154 | 2.053 | 0.940 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -5.340 | 2.031 | 0.009 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -11.120 | 2.047 | 0.000 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -4.867 | 2.047 | 0.017 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -5.153 | 2.054 | 0.012 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -2.734 | 2.047 | 0.182 |  |
| qwen2.5-7b | triage | Intercept | 0.017 | 0.146 | 0.907 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian] | -0.143 | 0.190 | 0.453 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian] | 0.043 | 0.190 | 0.822 |  |
| qwen2.5-7b | triage | C(language)[T.en] | 0.357 | 0.188 | 0.058 |  |
| qwen2.5-7b | triage | C(language)[T.fr] | 0.199 | 0.185 | 0.282 |  |
| qwen2.5-7b | triage | C(clarity)[T.clear] | -0.275 | 0.107 | 0.010 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.097 | 0.264 | 0.713 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.019 | 0.265 | 0.942 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.226 | 0.259 | 0.383 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.182 | 0.257 | 0.479 |  |
