# Analysis: study-cpu

Records: 29400; valid: 28698; counterfactual pairs: 26068.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | 83 | 15 | -0.084 | -0.293 | 0.125 | 0.470 | 0.361 | 0.266 | 0.453 | tested |  |
| apertus-8b | evacuation | 90 | 15 | -0.078 | -0.233 | 0.067 | 0.354 | 0.278 | 0.189 | 0.367 | tested |  |
| apertus-8b | housing | 90 | 15 | 0.167 | 0.056 | 0.267 | 0.004 | 0.289 | 0.211 | 0.378 | tested | 0.000 |
| apertus-8b | relief | 90 | 15 | -0.544 | -1.819 | 0.806 | 0.416 | 0.511 | 0.422 | 0.600 | tested |  |
| apertus-8b | triage | 67 | 15 | 0.194 | 0.014 | 0.366 | 0.049 | 0.254 | 0.182 | 0.333 | tested |  |
| krikri-8b | dispatch | 90 | 15 | 0.011 | -0.044 | 0.078 | 0.876 | 0.122 | 0.056 | 0.189 | tested |  |
| krikri-8b | evacuation | 90 | 15 | -0.044 | -0.089 | -0.011 | 0.018 | 0.044 | 0.011 | 0.089 | tested |  |
| krikri-8b | housing | 90 | 15 | -0.033 | -0.122 | 0.056 | 0.565 | 0.144 | 0.078 | 0.222 | tested | 0.000 |
| krikri-8b | relief | 82 | 15 | 0.290 | -0.473 | 0.945 | 0.417 | 0.195 | 0.094 | 0.325 | tested |  |
| krikri-8b | triage | 87 | 15 | 0.011 | -0.124 | 0.159 | 0.954 | 0.149 | 0.071 | 0.233 | tested |  |
| llama-3.1-8b | dispatch | 79 | 15 | 0.025 | -0.074 | 0.123 | 0.715 | 0.165 | 0.095 | 0.241 | tested |  |
| llama-3.1-8b | evacuation | 87 | 15 | 0.034 | -0.024 | 0.101 | 0.371 | 0.103 | 0.046 | 0.170 | tested |  |
| llama-3.1-8b | housing | 90 | 15 | -0.189 | -0.389 | 0.033 | 0.103 | 0.500 | 0.389 | 0.622 | tested | 0.000 |
| llama-3.1-8b | relief | 76 | 15 | -0.552 | -1.770 | 0.583 | 0.343 | 0.342 | 0.227 | 0.451 | tested |  |
| llama-3.1-8b | triage | 81 | 15 | -0.037 | -0.148 | 0.062 | 0.611 | 0.111 | 0.050 | 0.179 | tested |  |
| meltemi-7b | dispatch | 90 | 15 | -0.133 | -0.333 | 0.056 | 0.193 | 0.356 | 0.278 | 0.444 | tested |  |
| meltemi-7b | evacuation | 90 | 15 | 0.089 | -0.144 | 0.322 | 0.526 | 0.322 | 0.222 | 0.422 | tested |  |
| meltemi-7b | housing | 90 | 15 | -0.067 | -0.233 | 0.089 | 0.466 | 0.456 | 0.322 | 0.578 | tested | 0.000 |
| meltemi-7b | relief | 75 | 15 | 1.067 | -0.526 | 2.772 | 0.200 | 0.373 | 0.260 | 0.487 | tested |  |
| meltemi-7b | triage | 90 | 15 | 0.178 | -0.044 | 0.389 | 0.126 | 0.222 | 0.167 | 0.289 | tested |  |
| qwen2.5-7b | dispatch | 88 | 15 | 0.011 | -0.079 | 0.094 | 0.925 | 0.114 | 0.067 | 0.167 | tested |  |
| qwen2.5-7b | evacuation | 89 | 15 | -0.112 | -0.200 | -0.034 | 0.000 | 0.135 | 0.057 | 0.222 | tested |  |
| qwen2.5-7b | housing | 90 | 15 | 0.033 | 0.000 | 0.067 | 0.060 | 0.056 | 0.011 | 0.111 | tested | 0.000 |
| qwen2.5-7b | relief | 90 | 15 | -0.222 | -0.944 | 0.389 | 0.566 | 0.156 | 0.067 | 0.256 | tested |  |
| qwen2.5-7b | triage | 88 | 15 | 0.011 | -0.058 | 0.089 | 0.867 | 0.125 | 0.056 | 0.205 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 27 | 5 | 0.926 | 0.480 | 1.310 |  | 0.630 | 0.483 | 0.769 | descriptive (fewer than 8 cases) |  | 0.361 | 0.268 |  | False |
| apertus-8b | dispatch | area | social_housing | 83 | 15 | 0.205 | -0.069 | 0.526 | 0.145 | 0.422 | 0.305 | 0.530 | tested |  | 0.361 | 0.060 | 1.000 | False |
| apertus-8b | dispatch | area | villas | 83 | 15 | -0.542 | -0.790 | -0.313 | 0.000 | 0.542 | 0.434 | 0.646 | tested |  | 0.361 | 0.181 | 0.000 | True |
| apertus-8b | dispatch | gender | female | 85 | 15 | 0.247 | 0.036 | 0.494 | 0.021 | 0.494 | 0.395 | 0.605 | tested |  | 0.361 | 0.133 | 0.378 | False |
| apertus-8b | dispatch | origin | any_minority | 253 | 15 | 0.043 | -0.150 | 0.252 | 0.643 | 0.447 | 0.345 | 0.552 | tested |  | 0.361 | 0.085 | 1.000 | False |
| apertus-8b | dispatch | origin | local_migrant | 86 | 15 | 0.070 | -0.128 | 0.268 | 0.472 | 0.419 | 0.313 | 0.528 | tested |  | 0.361 | 0.057 | 1.000 | False |
| apertus-8b | dispatch | origin | romanian | 85 | 15 | -0.012 | -0.247 | 0.217 | 1.000 | 0.494 | 0.349 | 0.628 | tested |  | 0.361 | 0.133 | 1.000 | False |
| apertus-8b | dispatch | origin | syrian | 82 | 15 | 0.073 | -0.181 | 0.346 | 0.610 | 0.427 | 0.294 | 0.568 | tested |  | 0.361 | 0.065 | 1.000 | False |
| apertus-8b | dispatch | status | asylum_seeker | 83 | 15 | 0.590 | 0.175 | 1.048 | 0.008 | 0.602 | 0.482 | 0.720 | tested |  | 0.361 | 0.241 | 0.160 | False |
| apertus-8b | dispatch | status | seasonal_worker | 84 | 15 | -0.024 | -0.233 | 0.176 | 0.811 | 0.488 | 0.354 | 0.614 | tested |  | 0.361 | 0.127 | 1.000 | False |
| apertus-8b | evacuation | area | roma_settlement | 30 | 5 | 0.933 | 0.600 | 1.200 |  | 0.600 | 0.533 | 0.667 | descriptive (fewer than 8 cases) |  | 0.278 | 0.322 |  | False |
| apertus-8b | evacuation | area | social_housing | 90 | 15 | 0.833 | 0.556 | 1.133 | 0.000 | 0.489 | 0.389 | 0.600 | tested |  | 0.278 | 0.211 | 0.000 | True |
| apertus-8b | evacuation | area | villas | 90 | 15 | -0.400 | -0.544 | -0.278 | 0.000 | 0.400 | 0.311 | 0.500 | tested |  | 0.278 | 0.122 | 0.000 | True |
| apertus-8b | evacuation | origin | any_minority | 270 | 15 | 0.270 | 0.096 | 0.459 | 0.002 | 0.415 | 0.333 | 0.493 | tested |  | 0.278 | 0.137 | 0.046 | True |
| apertus-8b | evacuation | origin | local_migrant | 90 | 15 | 0.078 | -0.133 | 0.289 | 0.542 | 0.367 | 0.256 | 0.467 | tested |  | 0.278 | 0.089 | 1.000 | False |
| apertus-8b | evacuation | origin | romanian | 90 | 15 | -0.111 | -0.311 | 0.089 | 0.313 | 0.311 | 0.233 | 0.400 | tested |  | 0.278 | 0.033 | 1.000 | False |
| apertus-8b | evacuation | origin | syrian | 90 | 15 | 0.844 | 0.578 | 1.100 | 0.000 | 0.567 | 0.444 | 0.678 | tested |  | 0.278 | 0.289 | 0.000 | True |
| apertus-8b | housing | area | roma_settlement | 30 | 5 | 0.900 | 0.833 | 0.967 |  | 0.700 | 0.600 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.289 | 0.411 |  | False |
| apertus-8b | housing | area | social_housing | 90 | 15 | 0.211 | 0.111 | 0.333 | 0.000 | 0.311 | 0.211 | 0.411 | tested | 0.000 | 0.289 | 0.022 | 0.000 | False |
| apertus-8b | housing | area | villas | 90 | 15 | -0.233 | -0.389 | -0.089 | 0.000 | 0.589 | 0.500 | 0.678 | tested | 0.056 | 0.289 | 0.300 | 0.000 | True |
| apertus-8b | housing | gender | female | 90 | 15 | 0.356 | 0.211 | 0.511 | 0.000 | 0.522 | 0.389 | 0.644 | tested | 0.000 | 0.289 | 0.233 | 0.000 | True |
| apertus-8b | housing | origin | any_minority | 270 | 15 | 0.241 | 0.152 | 0.337 | 0.000 | 0.407 | 0.348 | 0.467 | tested | 0.000 | 0.289 | 0.119 | 0.000 | True |
| apertus-8b | housing | origin | local_migrant | 90 | 15 | 0.211 | 0.067 | 0.356 | 0.005 | 0.400 | 0.333 | 0.478 | tested | 0.000 | 0.289 | 0.111 | 0.105 | False |
| apertus-8b | housing | origin | romanian | 90 | 15 | 0.211 | 0.067 | 0.356 | 0.004 | 0.444 | 0.322 | 0.544 | tested | 0.000 | 0.289 | 0.156 | 0.088 | False |
| apertus-8b | housing | origin | syrian | 90 | 15 | 0.300 | 0.211 | 0.400 | 0.000 | 0.378 | 0.289 | 0.478 | tested | 0.000 | 0.289 | 0.089 | 0.000 | True |
| apertus-8b | housing | status | asylum_seeker | 90 | 15 | 0.578 | 0.422 | 0.711 | 0.000 | 0.544 | 0.444 | 0.644 | tested | 0.000 | 0.289 | 0.256 | 0.000 | True |
| apertus-8b | housing | status | seasonal_worker | 90 | 15 | -0.233 | -0.311 | -0.156 | 0.000 | 0.511 | 0.422 | 0.611 | tested | 0.011 | 0.289 | 0.222 | 0.000 | True |
| apertus-8b | relief | area | roma_settlement | 30 | 5 | -1.919 | -3.585 | 0.149 |  | 0.467 | 0.300 | 0.633 | descriptive (fewer than 8 cases) |  | 0.511 | -0.044 |  | False |
| apertus-8b | relief | area | social_housing | 90 | 15 | 0.563 | -1.143 | 1.990 | 0.486 | 0.489 | 0.389 | 0.589 | tested |  | 0.511 | -0.022 | 1.000 | False |
| apertus-8b | relief | area | villas | 90 | 15 | -0.870 | -2.586 | 0.675 | 0.317 | 0.500 | 0.389 | 0.611 | tested |  | 0.511 | -0.011 | 1.000 | False |
| apertus-8b | relief | origin | any_minority | 270 | 15 | -0.102 | -1.797 | 1.723 | 0.887 | 0.559 | 0.459 | 0.663 | tested |  | 0.511 | 0.048 | 1.000 | False |
| apertus-8b | relief | origin | local_migrant | 90 | 15 | -1.013 | -3.070 | 0.854 | 0.269 | 0.533 | 0.422 | 0.644 | tested |  | 0.511 | 0.022 | 1.000 | False |
| apertus-8b | relief | origin | romanian | 90 | 15 | 0.168 | -2.007 | 2.747 | 0.931 | 0.533 | 0.411 | 0.656 | tested |  | 0.511 | 0.022 | 1.000 | False |
| apertus-8b | relief | origin | syrian | 90 | 15 | 0.538 | -1.128 | 2.313 | 0.551 | 0.611 | 0.500 | 0.711 | tested |  | 0.511 | 0.100 | 1.000 | False |
| apertus-8b | triage | origin | any_minority | 195 | 15 | 0.251 | 0.034 | 0.464 | 0.027 | 0.328 | 0.245 | 0.414 | tested |  | 0.254 | 0.074 | 0.459 | False |
| apertus-8b | triage | origin | local_migrant | 63 | 15 | 0.222 | -0.022 | 0.467 | 0.086 | 0.302 | 0.209 | 0.390 | tested |  | 0.254 | 0.048 | 1.000 | False |
| apertus-8b | triage | origin | romanian | 66 | 15 | 0.227 | 0.000 | 0.433 | 0.061 | 0.348 | 0.258 | 0.435 | tested |  | 0.254 | 0.095 | 0.976 | False |
| apertus-8b | triage | origin | syrian | 66 | 15 | 0.303 | 0.046 | 0.597 | 0.019 | 0.333 | 0.215 | 0.462 | tested |  | 0.254 | 0.080 | 0.361 | False |
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
| llama-3.1-8b | dispatch | area | roma_settlement | 23 | 5 | 0.043 | -0.571 | 0.667 |  | 0.348 | 0.211 | 0.435 | descriptive (fewer than 8 cases) |  | 0.165 | 0.183 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 77 | 15 | -0.104 | -0.380 | 0.184 | 0.502 | 0.325 | 0.237 | 0.407 | tested |  | 0.165 | 0.160 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 77 | 15 | -0.623 | -0.903 | -0.382 | 0.000 | 0.416 | 0.282 | 0.550 | tested |  | 0.165 | 0.251 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 80 | 15 | -0.025 | -0.214 | 0.183 | 0.796 | 0.237 | 0.132 | 0.345 | tested |  | 0.165 | 0.073 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 232 | 15 | -0.034 | -0.137 | 0.059 | 0.519 | 0.224 | 0.143 | 0.303 | tested |  | 0.165 | 0.060 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | -0.091 | -0.275 | 0.071 | 0.355 | 0.234 | 0.141 | 0.321 | tested |  | 0.165 | 0.069 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 80 | 15 | 0.013 | -0.098 | 0.131 | 0.934 | 0.200 | 0.089 | 0.337 | tested |  | 0.165 | 0.035 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 75 | 15 | -0.027 | -0.132 | 0.091 | 0.719 | 0.240 | 0.171 | 0.298 | tested |  | 0.165 | 0.075 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.164 | -0.078 | 0.391 | 0.205 | 0.425 | 0.318 | 0.520 | tested |  | 0.165 | 0.260 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 76 | 15 | -0.368 | -0.667 | -0.095 | 0.010 | 0.368 | 0.228 | 0.493 | tested |  | 0.165 | 0.204 | 0.160 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.133 | 1.033 |  | 0.367 | 0.133 | 0.567 | descriptive (fewer than 8 cases) |  | 0.103 | 0.263 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 84 | 15 | 0.548 | 0.305 | 0.783 | 0.000 | 0.405 | 0.271 | 0.524 | tested |  | 0.103 | 0.301 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 86 | 15 | -0.407 | -0.655 | -0.176 | 0.000 | 0.349 | 0.214 | 0.482 | tested |  | 0.103 | 0.245 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 261 | 15 | 0.406 | 0.231 | 0.596 | 0.000 | 0.337 | 0.237 | 0.436 | tested |  | 0.103 | 0.234 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 86 | 15 | 0.209 | 0.011 | 0.395 | 0.047 | 0.256 | 0.170 | 0.341 | tested |  | 0.103 | 0.152 | 0.517 | False |
| llama-3.1-8b | evacuation | origin | romanian | 88 | 15 | 0.341 | 0.151 | 0.545 | 0.000 | 0.307 | 0.207 | 0.411 | tested |  | 0.103 | 0.203 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 87 | 15 | 0.667 | 0.460 | 0.876 | 0.000 | 0.448 | 0.314 | 0.568 | tested |  | 0.103 | 0.345 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 1.067 | 0.633 | 1.500 |  | 0.533 | 0.300 | 0.733 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.033 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.422 | 0.167 | 0.733 | 0.002 | 0.522 | 0.422 | 0.622 | tested | 0.000 | 0.500 | 0.022 | 0.036 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.667 | -2.011 | -1.355 | 0.000 | 0.767 | 0.678 | 0.856 | tested | 0.000 | 0.500 | 0.267 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.433 | 0.166 | 0.789 | 0.000 | 0.500 | 0.389 | 0.622 | tested | 0.000 | 0.500 | 0.000 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.230 | 0.044 | 0.422 | 0.019 | 0.489 | 0.415 | 0.567 | tested | 0.000 | 0.500 | -0.011 | 0.266 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.200 | 0.044 | 0.356 | 0.011 | 0.456 | 0.389 | 0.522 | tested | 0.000 | 0.500 | -0.044 | 0.165 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.100 | -0.189 | 0.400 | 0.503 | 0.544 | 0.433 | 0.644 | tested | 0.000 | 0.500 | 0.044 | 1.000 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.389 | 0.133 | 0.678 | 0.001 | 0.467 | 0.344 | 0.578 | tested | 0.000 | 0.500 | -0.033 | 0.019 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.833 | 0.611 | 1.100 | 0.000 | 0.589 | 0.467 | 0.700 | tested | 0.000 | 0.500 | 0.089 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.389 | -1.700 | -1.056 | 0.000 | 0.733 | 0.633 | 0.833 | tested | 0.056 | 0.500 | 0.233 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 28 | 5 | 4.795 | 2.058 | 7.022 |  | 0.464 | 0.222 | 0.655 | descriptive (fewer than 8 cases) |  | 0.342 | 0.122 |  | False |
| llama-3.1-8b | relief | area | social_housing | 77 | 15 | 0.817 | -0.987 | 2.457 | 0.359 | 0.506 | 0.427 | 0.579 | tested |  | 0.342 | 0.164 | 1.000 | False |
| llama-3.1-8b | relief | area | villas | 80 | 15 | -1.918 | -3.148 | -0.685 | 0.000 | 0.575 | 0.469 | 0.692 | tested |  | 0.342 | 0.233 | 0.000 | True |
| llama-3.1-8b | relief | origin | any_minority | 240 | 15 | 3.334 | 1.414 | 5.017 | 0.000 | 0.579 | 0.509 | 0.647 | tested |  | 0.342 | 0.237 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 81 | 15 | 2.188 | 0.124 | 3.904 | 0.036 | 0.556 | 0.434 | 0.671 | tested |  | 0.342 | 0.213 | 0.432 | False |
| llama-3.1-8b | relief | origin | romanian | 78 | 15 | 1.841 | -0.039 | 3.598 | 0.060 | 0.551 | 0.442 | 0.654 | tested |  | 0.342 | 0.209 | 0.600 | False |
| llama-3.1-8b | relief | origin | syrian | 81 | 15 | 5.917 | 3.477 | 8.258 | 0.000 | 0.630 | 0.536 | 0.720 | tested |  | 0.342 | 0.288 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 250 | 15 | 0.184 | 0.075 | 0.306 | 0.000 | 0.168 | 0.086 | 0.246 | tested |  | 0.111 | 0.057 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 82 | 15 | 0.134 | 0.038 | 0.232 | 0.007 | 0.159 | 0.073 | 0.247 | tested |  | 0.111 | 0.047 | 0.119 | False |
| llama-3.1-8b | triage | origin | romanian | 85 | 15 | 0.188 | 0.025 | 0.369 | 0.020 | 0.153 | 0.060 | 0.247 | tested |  | 0.111 | 0.042 | 0.266 | False |
| llama-3.1-8b | triage | origin | syrian | 83 | 15 | 0.229 | 0.092 | 0.392 | 0.000 | 0.193 | 0.106 | 0.284 | tested |  | 0.111 | 0.082 | 0.000 | True |
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
| meltemi-7b | housing | gender | female | 90 | 15 | 0.022 | -0.111 | 0.189 | 0.849 | 0.456 | 0.322 | 0.600 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | any_minority | 270 | 15 | 0.052 | -0.048 | 0.141 | 0.297 | 0.463 | 0.385 | 0.541 | tested | 0.000 | 0.456 | 0.007 | 1.000 | False |
| meltemi-7b | housing | origin | local_migrant | 90 | 15 | 0.011 | -0.133 | 0.144 | 0.916 | 0.456 | 0.355 | 0.567 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | romanian | 90 | 15 | -0.022 | -0.167 | 0.111 | 0.860 | 0.522 | 0.444 | 0.600 | tested | 0.000 | 0.456 | 0.067 | 1.000 | False |
| meltemi-7b | housing | origin | syrian | 90 | 15 | 0.167 | 0.067 | 0.267 | 0.001 | 0.411 | 0.322 | 0.511 | tested | 0.000 | 0.456 | -0.044 | 0.031 | False |
| meltemi-7b | housing | status | asylum_seeker | 90 | 15 | 0.100 | -0.078 | 0.278 | 0.316 | 0.433 | 0.311 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | status | seasonal_worker | 90 | 15 | 0.067 | -0.044 | 0.200 | 0.328 | 0.444 | 0.322 | 0.567 | tested | 0.000 | 0.456 | -0.011 | 1.000 | False |
| meltemi-7b | relief | area | roma_settlement | 22 | 5 | -0.892 | -2.237 | 0.266 |  | 0.364 | 0.130 | 0.545 | descriptive (fewer than 8 cases) |  | 0.373 | -0.010 |  | False |
| meltemi-7b | relief | area | social_housing | 72 | 15 | 0.723 | -0.904 | 2.165 | 0.384 | 0.417 | 0.338 | 0.500 | tested |  | 0.373 | 0.043 | 1.000 | False |
| meltemi-7b | relief | area | villas | 72 | 15 | 1.226 | -1.098 | 3.385 | 0.275 | 0.417 | 0.325 | 0.507 | tested |  | 0.373 | 0.043 | 1.000 | False |
| meltemi-7b | relief | origin | any_minority | 222 | 15 | -0.107 | -1.273 | 1.000 | 0.862 | 0.437 | 0.324 | 0.548 | tested |  | 0.373 | 0.064 | 1.000 | False |
| meltemi-7b | relief | origin | local_migrant | 75 | 15 | -0.873 | -2.722 | 1.022 | 0.354 | 0.467 | 0.342 | 0.588 | tested |  | 0.373 | 0.093 | 1.000 | False |
| meltemi-7b | relief | origin | romanian | 74 | 15 | -0.424 | -1.823 | 0.917 | 0.550 | 0.338 | 0.213 | 0.467 | tested |  | 0.373 | -0.035 | 1.000 | False |
| meltemi-7b | relief | origin | syrian | 73 | 15 | 1.002 | -0.359 | 2.223 | 0.148 | 0.507 | 0.367 | 0.645 | tested |  | 0.373 | 0.134 | 1.000 | False |
| meltemi-7b | triage | origin | any_minority | 270 | 15 | 0.141 | -0.030 | 0.330 | 0.099 | 0.274 | 0.196 | 0.348 | tested |  | 0.222 | 0.052 | 1.000 | False |
| meltemi-7b | triage | origin | local_migrant | 90 | 15 | 0.156 | -0.067 | 0.389 | 0.185 | 0.289 | 0.189 | 0.389 | tested |  | 0.222 | 0.067 | 1.000 | False |
| meltemi-7b | triage | origin | romanian | 90 | 15 | 0.033 | -0.178 | 0.244 | 0.777 | 0.289 | 0.189 | 0.389 | tested |  | 0.222 | 0.067 | 1.000 | False |
| meltemi-7b | triage | origin | syrian | 90 | 15 | 0.233 | 0.044 | 0.411 | 0.021 | 0.244 | 0.156 | 0.333 | tested |  | 0.222 | 0.022 | 0.609 | False |
| qwen2.5-7b | dispatch | area | roma_settlement | 29 | 5 | 0.483 | -0.586 | 1.400 |  | 0.690 | 0.556 | 0.800 | descriptive (fewer than 8 cases) |  | 0.114 | 0.576 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 87 | 15 | -0.103 | -0.529 | 0.217 | 0.673 | 0.402 | 0.270 | 0.542 | tested |  | 0.114 | 0.289 | 1.000 | False |
| qwen2.5-7b | dispatch | area | villas | 87 | 15 | -0.724 | -1.058 | -0.461 | 0.000 | 0.517 | 0.416 | 0.635 | tested |  | 0.114 | 0.404 | 0.000 | True |
| qwen2.5-7b | dispatch | gender | female | 88 | 15 | 0.307 | 0.170 | 0.455 | 0.000 | 0.330 | 0.222 | 0.438 | tested |  | 0.114 | 0.216 | 0.000 | True |
| qwen2.5-7b | dispatch | origin | any_minority | 264 | 15 | 0.072 | 0.000 | 0.148 | 0.053 | 0.193 | 0.136 | 0.244 | tested |  | 0.114 | 0.080 | 0.742 | False |
| qwen2.5-7b | dispatch | origin | local_migrant | 88 | 15 | 0.136 | 0.056 | 0.216 | 0.003 | 0.182 | 0.122 | 0.241 | tested |  | 0.114 | 0.068 | 0.072 | False |
| qwen2.5-7b | dispatch | origin | romanian | 88 | 15 | 0.023 | -0.070 | 0.125 | 0.756 | 0.193 | 0.125 | 0.264 | tested |  | 0.114 | 0.080 | 1.000 | False |
| qwen2.5-7b | dispatch | origin | syrian | 88 | 15 | 0.057 | -0.069 | 0.186 | 0.447 | 0.205 | 0.138 | 0.271 | tested |  | 0.114 | 0.091 | 1.000 | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 88 | 15 | 0.273 | -0.091 | 0.750 | 0.183 | 0.511 | 0.368 | 0.656 | tested |  | 0.114 | 0.398 | 1.000 | False |
| qwen2.5-7b | dispatch | status | seasonal_worker | 88 | 15 | -0.784 | -1.135 | -0.506 | 0.000 | 0.557 | 0.437 | 0.682 | tested |  | 0.114 | 0.443 | 0.000 | True |
| qwen2.5-7b | evacuation | area | roma_settlement | 30 | 5 | 0.867 | 0.233 | 1.500 |  | 0.700 | 0.499 | 0.933 | descriptive (fewer than 8 cases) |  | 0.135 | 0.565 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 90 | 15 | 0.211 | 0.033 | 0.389 | 0.030 | 0.333 | 0.200 | 0.467 | tested |  | 0.135 | 0.199 | 0.540 | False |
| qwen2.5-7b | evacuation | area | villas | 90 | 15 | -0.378 | -0.533 | -0.233 | 0.000 | 0.467 | 0.355 | 0.578 | tested |  | 0.135 | 0.332 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | any_minority | 270 | 15 | 0.244 | 0.126 | 0.378 | 0.000 | 0.285 | 0.185 | 0.396 | tested |  | 0.135 | 0.150 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | local_migrant | 90 | 15 | 0.044 | -0.078 | 0.167 | 0.538 | 0.178 | 0.089 | 0.278 | tested |  | 0.135 | 0.043 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | romanian | 90 | 15 | -0.022 | -0.156 | 0.122 | 0.815 | 0.189 | 0.067 | 0.322 | tested |  | 0.135 | 0.054 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | syrian | 90 | 15 | 0.711 | 0.478 | 0.956 | 0.000 | 0.489 | 0.367 | 0.622 | tested |  | 0.135 | 0.354 | 0.000 | True |
| qwen2.5-7b | housing | area | roma_settlement | 30 | 5 | 0.367 | 0.133 | 0.600 |  | 0.300 | 0.233 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.056 | 0.244 |  | False |
| qwen2.5-7b | housing | area | social_housing | 90 | 15 | 0.100 | 0.022 | 0.200 | 0.018 | 0.144 | 0.067 | 0.233 | tested | 0.000 | 0.056 | 0.089 | 0.360 | False |
| qwen2.5-7b | housing | area | villas | 90 | 15 | -0.144 | -0.267 | -0.033 | 0.007 | 0.122 | 0.044 | 0.200 | tested | 0.022 | 0.056 | 0.067 | 0.147 | False |
| qwen2.5-7b | housing | gender | female | 90 | 15 | 0.078 | 0.011 | 0.156 | 0.048 | 0.100 | 0.033 | 0.178 | tested | 0.000 | 0.056 | 0.044 | 0.720 | False |
| qwen2.5-7b | housing | origin | any_minority | 270 | 15 | 0.041 | -0.004 | 0.089 | 0.089 | 0.093 | 0.052 | 0.137 | tested | 0.000 | 0.056 | 0.037 | 0.979 | False |
| qwen2.5-7b | housing | origin | local_migrant | 90 | 15 | 0.067 | 0.000 | 0.133 | 0.059 | 0.111 | 0.044 | 0.189 | tested | 0.000 | 0.056 | 0.056 | 0.742 | False |
| qwen2.5-7b | housing | origin | romanian | 90 | 15 | 0.044 | 0.011 | 0.089 | 0.019 | 0.067 | 0.022 | 0.122 | tested | 0.000 | 0.056 | 0.011 | 0.361 | False |
| qwen2.5-7b | housing | origin | syrian | 90 | 15 | 0.011 | -0.056 | 0.089 | 0.870 | 0.100 | 0.044 | 0.156 | tested | 0.000 | 0.056 | 0.044 | 1.000 | False |
| qwen2.5-7b | housing | status | asylum_seeker | 90 | 15 | 0.111 | 0.011 | 0.200 | 0.031 | 0.189 | 0.133 | 0.256 | tested | 0.000 | 0.056 | 0.133 | 0.540 | False |
| qwen2.5-7b | housing | status | seasonal_worker | 90 | 15 | -0.467 | -0.656 | -0.300 | 0.000 | 0.333 | 0.211 | 0.456 | tested | 0.067 | 0.056 | 0.278 | 0.000 | True |
| qwen2.5-7b | relief | area | roma_settlement | 30 | 5 | 2.667 | 0.667 | 4.500 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) |  | 0.156 | 0.278 |  | False |
| qwen2.5-7b | relief | area | social_housing | 90 | 15 | 0.222 | -0.722 | 1.056 | 0.669 | 0.333 | 0.211 | 0.489 | tested |  | 0.156 | 0.178 | 1.000 | False |
| qwen2.5-7b | relief | area | villas | 90 | 15 | -2.444 | -3.667 | -1.444 | 0.000 | 0.389 | 0.289 | 0.489 | tested |  | 0.156 | 0.233 | 0.000 | True |
| qwen2.5-7b | relief | origin | any_minority | 270 | 15 | 1.074 | 0.333 | 1.759 | 0.005 | 0.452 | 0.374 | 0.533 | tested |  | 0.156 | 0.296 | 0.110 | False |
| qwen2.5-7b | relief | origin | local_migrant | 90 | 15 | -0.389 | -1.222 | 0.333 | 0.327 | 0.356 | 0.278 | 0.433 | tested |  | 0.156 | 0.200 | 1.000 | False |
| qwen2.5-7b | relief | origin | romanian | 90 | 15 | -0.611 | -1.167 | 0.000 | 0.057 | 0.356 | 0.244 | 0.467 | tested |  | 0.156 | 0.200 | 0.742 | False |
| qwen2.5-7b | relief | origin | syrian | 90 | 15 | 4.222 | 2.778 | 5.667 | 0.000 | 0.644 | 0.511 | 0.767 | tested |  | 0.156 | 0.489 | 0.000 | True |
| qwen2.5-7b | triage | origin | any_minority | 267 | 15 | 0.146 | 0.052 | 0.242 | 0.003 | 0.202 | 0.127 | 0.272 | tested |  | 0.125 | 0.077 | 0.072 | False |
| qwen2.5-7b | triage | origin | local_migrant | 89 | 15 | 0.079 | -0.022 | 0.172 | 0.161 | 0.135 | 0.067 | 0.202 | tested |  | 0.125 | 0.010 | 1.000 | False |
| qwen2.5-7b | triage | origin | romanian | 89 | 15 | 0.090 | 0.011 | 0.180 | 0.041 | 0.191 | 0.111 | 0.278 | tested |  | 0.125 | 0.066 | 0.656 | False |
| qwen2.5-7b | triage | origin | syrian | 89 | 15 | 0.270 | 0.124 | 0.411 | 0.000 | 0.281 | 0.180 | 0.382 | tested |  | 0.125 | 0.156 | 0.000 | True |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | 27 | 5 | 0.926 | 0.480 | 1.310 |  | 0.630 | 0.483 | 0.769 | descriptive (fewer than 8 cases) |  | 0.361 | 0.268 |  | False |
| apertus-8b | dispatch | area | social_housing | 83 | 15 | 0.205 | -0.069 | 0.526 | 0.145 | 0.422 | 0.305 | 0.530 | tested |  | 0.361 | 0.060 | 1.000 | False |
| apertus-8b | dispatch | area | villas | 83 | 15 | -0.542 | -0.790 | -0.313 | 0.000 | 0.542 | 0.434 | 0.646 | tested |  | 0.361 | 0.181 | 0.000 | True |
| apertus-8b | dispatch | gender | female | 85 | 15 | 0.247 | 0.036 | 0.494 | 0.021 | 0.494 | 0.395 | 0.605 | tested |  | 0.361 | 0.133 | 0.378 | False |
| apertus-8b | dispatch | origin | any_minority | 253 | 15 | 0.043 | -0.150 | 0.252 | 0.643 | 0.447 | 0.345 | 0.552 | tested |  | 0.361 | 0.085 | 1.000 | False |
| apertus-8b | dispatch | origin | local_migrant | 86 | 15 | 0.070 | -0.128 | 0.268 | 0.472 | 0.419 | 0.313 | 0.528 | tested |  | 0.361 | 0.057 | 1.000 | False |
| apertus-8b | dispatch | origin | romanian | 85 | 15 | -0.012 | -0.247 | 0.217 | 1.000 | 0.494 | 0.349 | 0.628 | tested |  | 0.361 | 0.133 | 1.000 | False |
| apertus-8b | dispatch | origin | syrian | 82 | 15 | 0.073 | -0.181 | 0.346 | 0.610 | 0.427 | 0.294 | 0.568 | tested |  | 0.361 | 0.065 | 1.000 | False |
| apertus-8b | dispatch | status | asylum_seeker | 83 | 15 | 0.590 | 0.175 | 1.048 | 0.008 | 0.602 | 0.482 | 0.720 | tested |  | 0.361 | 0.241 | 0.160 | False |
| apertus-8b | dispatch | status | seasonal_worker | 84 | 15 | -0.024 | -0.233 | 0.176 | 0.811 | 0.488 | 0.354 | 0.614 | tested |  | 0.361 | 0.127 | 1.000 | False |
| apertus-8b | evacuation | area | roma_settlement | 30 | 5 | 0.933 | 0.600 | 1.200 |  | 0.600 | 0.533 | 0.667 | descriptive (fewer than 8 cases) |  | 0.278 | 0.322 |  | False |
| apertus-8b | evacuation | area | social_housing | 90 | 15 | 0.833 | 0.556 | 1.133 | 0.000 | 0.489 | 0.389 | 0.600 | tested |  | 0.278 | 0.211 | 0.000 | True |
| apertus-8b | evacuation | area | villas | 90 | 15 | -0.400 | -0.544 | -0.278 | 0.000 | 0.400 | 0.311 | 0.500 | tested |  | 0.278 | 0.122 | 0.000 | True |
| apertus-8b | evacuation | origin | any_minority | 270 | 15 | 0.270 | 0.096 | 0.459 | 0.002 | 0.415 | 0.333 | 0.493 | tested |  | 0.278 | 0.137 | 0.046 | True |
| apertus-8b | evacuation | origin | local_migrant | 90 | 15 | 0.078 | -0.133 | 0.289 | 0.542 | 0.367 | 0.256 | 0.467 | tested |  | 0.278 | 0.089 | 1.000 | False |
| apertus-8b | evacuation | origin | romanian | 90 | 15 | -0.111 | -0.311 | 0.089 | 0.313 | 0.311 | 0.233 | 0.400 | tested |  | 0.278 | 0.033 | 1.000 | False |
| apertus-8b | evacuation | origin | syrian | 90 | 15 | 0.844 | 0.578 | 1.100 | 0.000 | 0.567 | 0.444 | 0.678 | tested |  | 0.278 | 0.289 | 0.000 | True |
| apertus-8b | housing | area | roma_settlement | 30 | 5 | 0.900 | 0.833 | 0.967 |  | 0.700 | 0.600 | 0.800 | descriptive (fewer than 8 cases) | 0.000 | 0.289 | 0.411 |  | False |
| apertus-8b | housing | area | social_housing | 90 | 15 | 0.211 | 0.111 | 0.333 | 0.000 | 0.311 | 0.211 | 0.411 | tested | 0.000 | 0.289 | 0.022 | 0.000 | False |
| apertus-8b | housing | area | villas | 90 | 15 | -0.233 | -0.389 | -0.089 | 0.000 | 0.589 | 0.500 | 0.678 | tested | 0.056 | 0.289 | 0.300 | 0.000 | True |
| apertus-8b | housing | gender | female | 90 | 15 | 0.356 | 0.211 | 0.511 | 0.000 | 0.522 | 0.389 | 0.644 | tested | 0.000 | 0.289 | 0.233 | 0.000 | True |
| apertus-8b | housing | origin | any_minority | 270 | 15 | 0.241 | 0.152 | 0.337 | 0.000 | 0.407 | 0.348 | 0.467 | tested | 0.000 | 0.289 | 0.119 | 0.000 | True |
| apertus-8b | housing | origin | local_migrant | 90 | 15 | 0.211 | 0.067 | 0.356 | 0.005 | 0.400 | 0.333 | 0.478 | tested | 0.000 | 0.289 | 0.111 | 0.105 | False |
| apertus-8b | housing | origin | romanian | 90 | 15 | 0.211 | 0.067 | 0.356 | 0.004 | 0.444 | 0.322 | 0.544 | tested | 0.000 | 0.289 | 0.156 | 0.088 | False |
| apertus-8b | housing | origin | syrian | 90 | 15 | 0.300 | 0.211 | 0.400 | 0.000 | 0.378 | 0.289 | 0.478 | tested | 0.000 | 0.289 | 0.089 | 0.000 | True |
| apertus-8b | housing | status | asylum_seeker | 90 | 15 | 0.578 | 0.422 | 0.711 | 0.000 | 0.544 | 0.444 | 0.644 | tested | 0.000 | 0.289 | 0.256 | 0.000 | True |
| apertus-8b | housing | status | seasonal_worker | 90 | 15 | -0.233 | -0.311 | -0.156 | 0.000 | 0.511 | 0.422 | 0.611 | tested | 0.011 | 0.289 | 0.222 | 0.000 | True |
| apertus-8b | relief | area | roma_settlement | 26 | 5 | -2.500 | -3.734 | -0.391 |  | 0.500 | 0.364 | 0.607 | descriptive (fewer than 8 cases) |  | 0.536 | -0.036 |  | False |
| apertus-8b | relief | area | social_housing | 66 | 15 | 0.333 | -1.972 | 2.361 | 0.726 | 0.545 | 0.429 | 0.649 | tested |  | 0.536 | 0.009 | 1.000 | False |
| apertus-8b | relief | area | villas | 69 | 15 | -1.014 | -3.123 | 0.791 | 0.318 | 0.565 | 0.427 | 0.697 | tested |  | 0.536 | 0.029 | 1.000 | False |
| apertus-8b | relief | origin | any_minority | 200 | 15 | -0.965 | -2.626 | 0.885 | 0.275 | 0.595 | 0.470 | 0.714 | tested |  | 0.536 | 0.059 | 1.000 | False |
| apertus-8b | relief | origin | local_migrant | 69 | 15 | -1.739 | -4.105 | 0.478 | 0.139 | 0.551 | 0.410 | 0.687 | tested |  | 0.536 | 0.014 | 1.000 | False |
| apertus-8b | relief | origin | romanian | 64 | 15 | -0.781 | -2.818 | 1.732 | 0.478 | 0.562 | 0.415 | 0.710 | tested |  | 0.536 | 0.026 | 1.000 | False |
| apertus-8b | relief | origin | syrian | 67 | 14 | -0.343 | -1.758 | 1.077 | 0.656 | 0.672 | 0.538 | 0.797 | tested |  | 0.536 | 0.135 | 1.000 | False |
| apertus-8b | triage | origin | any_minority | 195 | 15 | 0.251 | 0.034 | 0.464 | 0.027 | 0.328 | 0.245 | 0.414 | tested |  | 0.254 | 0.074 | 0.459 | False |
| apertus-8b | triage | origin | local_migrant | 63 | 15 | 0.222 | -0.022 | 0.467 | 0.086 | 0.302 | 0.209 | 0.390 | tested |  | 0.254 | 0.048 | 1.000 | False |
| apertus-8b | triage | origin | romanian | 66 | 15 | 0.227 | 0.000 | 0.433 | 0.061 | 0.348 | 0.258 | 0.435 | tested |  | 0.254 | 0.095 | 0.976 | False |
| apertus-8b | triage | origin | syrian | 66 | 15 | 0.303 | 0.046 | 0.597 | 0.019 | 0.333 | 0.215 | 0.462 | tested |  | 0.254 | 0.080 | 0.361 | False |
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
| llama-3.1-8b | dispatch | area | roma_settlement | 23 | 5 | 0.043 | -0.571 | 0.667 |  | 0.348 | 0.211 | 0.435 | descriptive (fewer than 8 cases) |  | 0.165 | 0.183 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 77 | 15 | -0.104 | -0.380 | 0.184 | 0.502 | 0.325 | 0.237 | 0.407 | tested |  | 0.165 | 0.160 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 77 | 15 | -0.623 | -0.903 | -0.382 | 0.000 | 0.416 | 0.282 | 0.550 | tested |  | 0.165 | 0.251 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 80 | 15 | -0.025 | -0.214 | 0.183 | 0.796 | 0.237 | 0.132 | 0.345 | tested |  | 0.165 | 0.073 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 232 | 15 | -0.034 | -0.137 | 0.059 | 0.519 | 0.224 | 0.143 | 0.303 | tested |  | 0.165 | 0.060 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | -0.091 | -0.275 | 0.071 | 0.355 | 0.234 | 0.141 | 0.321 | tested |  | 0.165 | 0.069 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 80 | 15 | 0.013 | -0.098 | 0.131 | 0.934 | 0.200 | 0.089 | 0.337 | tested |  | 0.165 | 0.035 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 75 | 15 | -0.027 | -0.132 | 0.091 | 0.719 | 0.240 | 0.171 | 0.298 | tested |  | 0.165 | 0.075 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.164 | -0.078 | 0.391 | 0.205 | 0.425 | 0.318 | 0.520 | tested |  | 0.165 | 0.260 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 76 | 15 | -0.368 | -0.667 | -0.095 | 0.010 | 0.368 | 0.228 | 0.493 | tested |  | 0.165 | 0.204 | 0.160 | False |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.567 | 0.133 | 1.033 |  | 0.367 | 0.133 | 0.567 | descriptive (fewer than 8 cases) |  | 0.103 | 0.263 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 84 | 15 | 0.548 | 0.305 | 0.783 | 0.000 | 0.405 | 0.271 | 0.524 | tested |  | 0.103 | 0.301 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 86 | 15 | -0.407 | -0.655 | -0.176 | 0.000 | 0.349 | 0.214 | 0.482 | tested |  | 0.103 | 0.245 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 261 | 15 | 0.406 | 0.231 | 0.596 | 0.000 | 0.337 | 0.237 | 0.436 | tested |  | 0.103 | 0.234 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 86 | 15 | 0.209 | 0.011 | 0.395 | 0.047 | 0.256 | 0.170 | 0.341 | tested |  | 0.103 | 0.152 | 0.564 | False |
| llama-3.1-8b | evacuation | origin | romanian | 88 | 15 | 0.341 | 0.151 | 0.545 | 0.000 | 0.307 | 0.207 | 0.411 | tested |  | 0.103 | 0.203 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | syrian | 87 | 15 | 0.667 | 0.460 | 0.876 | 0.000 | 0.448 | 0.314 | 0.568 | tested |  | 0.103 | 0.345 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 1.067 | 0.633 | 1.500 |  | 0.533 | 0.300 | 0.733 | descriptive (fewer than 8 cases) | 0.000 | 0.500 | 0.033 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.422 | 0.167 | 0.733 | 0.002 | 0.522 | 0.422 | 0.622 | tested | 0.000 | 0.500 | 0.022 | 0.038 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.667 | -2.011 | -1.355 | 0.000 | 0.767 | 0.678 | 0.856 | tested | 0.000 | 0.500 | 0.267 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.433 | 0.166 | 0.789 | 0.000 | 0.500 | 0.389 | 0.622 | tested | 0.000 | 0.500 | 0.000 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.230 | 0.044 | 0.422 | 0.019 | 0.489 | 0.415 | 0.567 | tested | 0.000 | 0.500 | -0.011 | 0.266 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.200 | 0.044 | 0.356 | 0.011 | 0.456 | 0.389 | 0.522 | tested | 0.000 | 0.500 | -0.044 | 0.165 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.100 | -0.189 | 0.400 | 0.503 | 0.544 | 0.433 | 0.644 | tested | 0.000 | 0.500 | 0.044 | 1.000 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.389 | 0.133 | 0.678 | 0.001 | 0.467 | 0.344 | 0.578 | tested | 0.000 | 0.500 | -0.033 | 0.021 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.833 | 0.611 | 1.100 | 0.000 | 0.589 | 0.467 | 0.700 | tested | 0.000 | 0.500 | 0.089 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.389 | -1.700 | -1.056 | 0.000 | 0.733 | 0.633 | 0.833 | tested | 0.056 | 0.500 | 0.233 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 22 | 5 | 4.591 | 1.588 | 6.882 |  | 0.500 | 0.222 | 0.727 | descriptive (fewer than 8 cases) |  | 0.271 | 0.229 |  | False |
| llama-3.1-8b | relief | area | social_housing | 60 | 15 | 1.683 | -0.105 | 3.451 | 0.073 | 0.500 | 0.409 | 0.571 | tested |  | 0.271 | 0.229 | 0.803 | False |
| llama-3.1-8b | relief | area | villas | 63 | 15 | -2.587 | -4.534 | -1.070 | 0.001 | 0.571 | 0.444 | 0.717 | tested |  | 0.271 | 0.300 | 0.021 | True |
| llama-3.1-8b | relief | origin | any_minority | 194 | 15 | 3.449 | 1.268 | 5.222 | 0.002 | 0.593 | 0.498 | 0.678 | tested |  | 0.271 | 0.322 | 0.038 | True |
| llama-3.1-8b | relief | origin | local_migrant | 65 | 15 | 2.154 | -0.246 | 4.118 | 0.081 | 0.585 | 0.458 | 0.703 | tested |  | 0.271 | 0.313 | 0.810 | False |
| llama-3.1-8b | relief | origin | romanian | 64 | 15 | 1.861 | -0.362 | 3.796 | 0.107 | 0.547 | 0.414 | 0.662 | tested |  | 0.271 | 0.276 | 0.963 | False |
| llama-3.1-8b | relief | origin | syrian | 65 | 15 | 6.308 | 3.651 | 8.732 | 0.000 | 0.646 | 0.517 | 0.771 | tested |  | 0.271 | 0.375 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 250 | 15 | 0.184 | 0.075 | 0.306 | 0.000 | 0.168 | 0.086 | 0.246 | tested |  | 0.111 | 0.057 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 82 | 15 | 0.134 | 0.038 | 0.232 | 0.007 | 0.159 | 0.073 | 0.247 | tested |  | 0.111 | 0.047 | 0.119 | False |
| llama-3.1-8b | triage | origin | romanian | 85 | 15 | 0.188 | 0.025 | 0.369 | 0.020 | 0.153 | 0.060 | 0.247 | tested |  | 0.111 | 0.042 | 0.266 | False |
| llama-3.1-8b | triage | origin | syrian | 83 | 15 | 0.229 | 0.092 | 0.392 | 0.000 | 0.193 | 0.106 | 0.284 | tested |  | 0.111 | 0.082 | 0.000 | True |
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
| meltemi-7b | evacuation | origin | any_minority | 270 | 15 | 0.341 | 0.126 | 0.556 | 0.001 | 0.415 | 0.356 | 0.474 | tested |  | 0.322 | 0.093 | 0.028 | True |
| meltemi-7b | evacuation | origin | local_migrant | 90 | 15 | 0.156 | -0.089 | 0.400 | 0.232 | 0.400 | 0.333 | 0.478 | tested |  | 0.322 | 0.078 | 1.000 | False |
| meltemi-7b | evacuation | origin | romanian | 90 | 15 | 0.211 | -0.056 | 0.489 | 0.146 | 0.344 | 0.267 | 0.422 | tested |  | 0.322 | 0.022 | 1.000 | False |
| meltemi-7b | evacuation | origin | syrian | 90 | 15 | 0.656 | 0.444 | 0.867 | 0.000 | 0.500 | 0.400 | 0.600 | tested |  | 0.322 | 0.178 | 0.000 | True |
| meltemi-7b | housing | area | roma_settlement | 30 | 5 | 0.300 | 0.200 | 0.400 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) | 0.000 | 0.456 | -0.022 |  | False |
| meltemi-7b | housing | area | social_housing | 90 | 15 | -0.033 | -0.144 | 0.089 | 0.616 | 0.433 | 0.322 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | area | villas | 90 | 15 | -0.189 | -0.300 | -0.078 | 0.000 | 0.522 | 0.422 | 0.622 | tested | 0.000 | 0.456 | 0.067 | 0.000 | True |
| meltemi-7b | housing | gender | female | 90 | 15 | 0.022 | -0.111 | 0.189 | 0.849 | 0.456 | 0.322 | 0.600 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | any_minority | 270 | 15 | 0.052 | -0.048 | 0.141 | 0.297 | 0.463 | 0.385 | 0.541 | tested | 0.000 | 0.456 | 0.007 | 1.000 | False |
| meltemi-7b | housing | origin | local_migrant | 90 | 15 | 0.011 | -0.133 | 0.144 | 0.916 | 0.456 | 0.355 | 0.567 | tested | 0.000 | 0.456 | 0.000 | 1.000 | False |
| meltemi-7b | housing | origin | romanian | 90 | 15 | -0.022 | -0.167 | 0.111 | 0.860 | 0.522 | 0.444 | 0.600 | tested | 0.000 | 0.456 | 0.067 | 1.000 | False |
| meltemi-7b | housing | origin | syrian | 90 | 15 | 0.167 | 0.067 | 0.267 | 0.001 | 0.411 | 0.322 | 0.511 | tested | 0.000 | 0.456 | -0.044 | 0.028 | False |
| meltemi-7b | housing | status | asylum_seeker | 90 | 15 | 0.100 | -0.078 | 0.278 | 0.316 | 0.433 | 0.311 | 0.556 | tested | 0.000 | 0.456 | -0.022 | 1.000 | False |
| meltemi-7b | housing | status | seasonal_worker | 90 | 15 | 0.067 | -0.044 | 0.200 | 0.328 | 0.444 | 0.322 | 0.567 | tested | 0.000 | 0.456 | -0.011 | 1.000 | False |
| meltemi-7b | relief | area | roma_settlement | 2 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  | 0.750 | -0.750 |  | False |
| meltemi-7b | relief | area | social_housing | 8 | 8 | 1.875 | -3.125 | 6.250 | 0.510 | 0.750 | 0.375 | 1.000 | tested |  | 0.750 | 0.000 | 1.000 | False |
| meltemi-7b | relief | area | villas | 7 | 7 | 0.714 | -3.571 | 5.000 |  | 0.429 | 0.143 | 0.857 | descriptive (fewer than 8 cases) |  | 0.750 | -0.321 |  | False |
| meltemi-7b | relief | origin | any_minority | 25 | 11 | -0.200 | -3.214 | 2.709 | 1.000 | 0.600 | 0.348 | 0.850 | tested |  | 0.750 | -0.150 | 1.000 | False |
| meltemi-7b | relief | origin | local_migrant | 8 | 7 | -1.250 | -5.000 | 3.750 |  | 0.750 | 0.429 | 1.000 | descriptive (fewer than 8 cases) |  | 0.750 | 0.000 |  | False |
| meltemi-7b | relief | origin | romanian | 8 | 7 | 0.625 | -4.375 | 5.625 |  | 0.625 | 0.286 | 0.875 | descriptive (fewer than 8 cases) |  | 0.750 | -0.125 |  | False |
| meltemi-7b | relief | origin | syrian | 9 | 8 | 0.000 | -3.500 | 3.750 | 1.000 | 0.444 | 0.111 | 0.875 | tested |  | 0.750 | -0.306 | 1.000 | False |
| meltemi-7b | triage | origin | any_minority | 270 | 15 | 0.141 | -0.030 | 0.330 | 0.099 | 0.274 | 0.196 | 0.348 | tested |  | 0.222 | 0.052 | 1.000 | False |
| meltemi-7b | triage | origin | local_migrant | 90 | 15 | 0.156 | -0.067 | 0.389 | 0.185 | 0.289 | 0.189 | 0.389 | tested |  | 0.222 | 0.067 | 1.000 | False |
| meltemi-7b | triage | origin | romanian | 90 | 15 | 0.033 | -0.178 | 0.244 | 0.777 | 0.289 | 0.189 | 0.389 | tested |  | 0.222 | 0.067 | 1.000 | False |
| meltemi-7b | triage | origin | syrian | 90 | 15 | 0.233 | 0.044 | 0.411 | 0.021 | 0.244 | 0.156 | 0.333 | tested |  | 0.222 | 0.022 | 0.546 | False |
| qwen2.5-7b | dispatch | area | roma_settlement | 29 | 5 | 0.483 | -0.586 | 1.400 |  | 0.690 | 0.556 | 0.800 | descriptive (fewer than 8 cases) |  | 0.114 | 0.576 |  | False |
| qwen2.5-7b | dispatch | area | social_housing | 87 | 15 | -0.103 | -0.529 | 0.217 | 0.673 | 0.402 | 0.270 | 0.542 | tested |  | 0.114 | 0.289 | 1.000 | False |
| qwen2.5-7b | dispatch | area | villas | 87 | 15 | -0.724 | -1.058 | -0.461 | 0.000 | 0.517 | 0.416 | 0.635 | tested |  | 0.114 | 0.404 | 0.000 | True |
| qwen2.5-7b | dispatch | gender | female | 88 | 15 | 0.307 | 0.170 | 0.455 | 0.000 | 0.330 | 0.222 | 0.438 | tested |  | 0.114 | 0.216 | 0.000 | True |
| qwen2.5-7b | dispatch | origin | any_minority | 264 | 15 | 0.072 | 0.000 | 0.148 | 0.053 | 0.193 | 0.136 | 0.244 | tested |  | 0.114 | 0.080 | 0.742 | False |
| qwen2.5-7b | dispatch | origin | local_migrant | 88 | 15 | 0.136 | 0.056 | 0.216 | 0.003 | 0.182 | 0.122 | 0.241 | tested |  | 0.114 | 0.068 | 0.072 | False |
| qwen2.5-7b | dispatch | origin | romanian | 88 | 15 | 0.023 | -0.070 | 0.125 | 0.756 | 0.193 | 0.125 | 0.264 | tested |  | 0.114 | 0.080 | 1.000 | False |
| qwen2.5-7b | dispatch | origin | syrian | 88 | 15 | 0.057 | -0.069 | 0.186 | 0.447 | 0.205 | 0.138 | 0.271 | tested |  | 0.114 | 0.091 | 1.000 | False |
| qwen2.5-7b | dispatch | status | asylum_seeker | 88 | 15 | 0.273 | -0.091 | 0.750 | 0.183 | 0.511 | 0.368 | 0.656 | tested |  | 0.114 | 0.398 | 1.000 | False |
| qwen2.5-7b | dispatch | status | seasonal_worker | 88 | 15 | -0.784 | -1.135 | -0.506 | 0.000 | 0.557 | 0.437 | 0.682 | tested |  | 0.114 | 0.443 | 0.000 | True |
| qwen2.5-7b | evacuation | area | roma_settlement | 30 | 5 | 0.867 | 0.233 | 1.500 |  | 0.700 | 0.499 | 0.933 | descriptive (fewer than 8 cases) |  | 0.135 | 0.565 |  | False |
| qwen2.5-7b | evacuation | area | social_housing | 90 | 15 | 0.211 | 0.033 | 0.389 | 0.030 | 0.333 | 0.200 | 0.467 | tested |  | 0.135 | 0.199 | 0.540 | False |
| qwen2.5-7b | evacuation | area | villas | 90 | 15 | -0.378 | -0.533 | -0.233 | 0.000 | 0.467 | 0.355 | 0.578 | tested |  | 0.135 | 0.332 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | any_minority | 270 | 15 | 0.244 | 0.126 | 0.378 | 0.000 | 0.285 | 0.185 | 0.396 | tested |  | 0.135 | 0.150 | 0.000 | True |
| qwen2.5-7b | evacuation | origin | local_migrant | 90 | 15 | 0.044 | -0.078 | 0.167 | 0.538 | 0.178 | 0.089 | 0.278 | tested |  | 0.135 | 0.043 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | romanian | 90 | 15 | -0.022 | -0.156 | 0.122 | 0.815 | 0.189 | 0.067 | 0.322 | tested |  | 0.135 | 0.054 | 1.000 | False |
| qwen2.5-7b | evacuation | origin | syrian | 90 | 15 | 0.711 | 0.478 | 0.956 | 0.000 | 0.489 | 0.367 | 0.622 | tested |  | 0.135 | 0.354 | 0.000 | True |
| qwen2.5-7b | housing | area | roma_settlement | 30 | 5 | 0.367 | 0.133 | 0.600 |  | 0.300 | 0.233 | 0.333 | descriptive (fewer than 8 cases) | 0.000 | 0.056 | 0.244 |  | False |
| qwen2.5-7b | housing | area | social_housing | 90 | 15 | 0.100 | 0.022 | 0.200 | 0.018 | 0.144 | 0.067 | 0.233 | tested | 0.000 | 0.056 | 0.089 | 0.360 | False |
| qwen2.5-7b | housing | area | villas | 90 | 15 | -0.144 | -0.267 | -0.033 | 0.007 | 0.122 | 0.044 | 0.200 | tested | 0.022 | 0.056 | 0.067 | 0.147 | False |
| qwen2.5-7b | housing | gender | female | 90 | 15 | 0.078 | 0.011 | 0.156 | 0.048 | 0.100 | 0.033 | 0.178 | tested | 0.000 | 0.056 | 0.044 | 0.720 | False |
| qwen2.5-7b | housing | origin | any_minority | 270 | 15 | 0.041 | -0.004 | 0.089 | 0.089 | 0.093 | 0.052 | 0.137 | tested | 0.000 | 0.056 | 0.037 | 0.979 | False |
| qwen2.5-7b | housing | origin | local_migrant | 90 | 15 | 0.067 | 0.000 | 0.133 | 0.059 | 0.111 | 0.044 | 0.189 | tested | 0.000 | 0.056 | 0.056 | 0.742 | False |
| qwen2.5-7b | housing | origin | romanian | 90 | 15 | 0.044 | 0.011 | 0.089 | 0.019 | 0.067 | 0.022 | 0.122 | tested | 0.000 | 0.056 | 0.011 | 0.361 | False |
| qwen2.5-7b | housing | origin | syrian | 90 | 15 | 0.011 | -0.056 | 0.089 | 0.870 | 0.100 | 0.044 | 0.156 | tested | 0.000 | 0.056 | 0.044 | 1.000 | False |
| qwen2.5-7b | housing | status | asylum_seeker | 90 | 15 | 0.111 | 0.011 | 0.200 | 0.031 | 0.189 | 0.133 | 0.256 | tested | 0.000 | 0.056 | 0.133 | 0.540 | False |
| qwen2.5-7b | housing | status | seasonal_worker | 90 | 15 | -0.467 | -0.656 | -0.300 | 0.000 | 0.333 | 0.211 | 0.456 | tested | 0.067 | 0.056 | 0.278 | 0.000 | True |
| qwen2.5-7b | relief | area | roma_settlement | 30 | 5 | 2.667 | 0.667 | 4.500 |  | 0.433 | 0.267 | 0.633 | descriptive (fewer than 8 cases) |  | 0.156 | 0.278 |  | False |
| qwen2.5-7b | relief | area | social_housing | 90 | 15 | 0.222 | -0.722 | 1.056 | 0.669 | 0.333 | 0.211 | 0.489 | tested |  | 0.156 | 0.178 | 1.000 | False |
| qwen2.5-7b | relief | area | villas | 90 | 15 | -2.444 | -3.667 | -1.444 | 0.000 | 0.389 | 0.289 | 0.489 | tested |  | 0.156 | 0.233 | 0.000 | True |
| qwen2.5-7b | relief | origin | any_minority | 270 | 15 | 1.074 | 0.333 | 1.759 | 0.005 | 0.452 | 0.374 | 0.533 | tested |  | 0.156 | 0.296 | 0.110 | False |
| qwen2.5-7b | relief | origin | local_migrant | 90 | 15 | -0.389 | -1.222 | 0.333 | 0.327 | 0.356 | 0.278 | 0.433 | tested |  | 0.156 | 0.200 | 1.000 | False |
| qwen2.5-7b | relief | origin | romanian | 90 | 15 | -0.611 | -1.167 | 0.000 | 0.057 | 0.356 | 0.244 | 0.467 | tested |  | 0.156 | 0.200 | 0.742 | False |
| qwen2.5-7b | relief | origin | syrian | 90 | 15 | 4.222 | 2.778 | 5.667 | 0.000 | 0.644 | 0.511 | 0.767 | tested |  | 0.156 | 0.489 | 0.000 | True |
| qwen2.5-7b | triage | origin | any_minority | 267 | 15 | 0.146 | 0.052 | 0.242 | 0.003 | 0.202 | 0.127 | 0.272 | tested |  | 0.125 | 0.077 | 0.072 | False |
| qwen2.5-7b | triage | origin | local_migrant | 89 | 15 | 0.079 | -0.022 | 0.172 | 0.161 | 0.135 | 0.067 | 0.202 | tested |  | 0.125 | 0.010 | 1.000 | False |
| qwen2.5-7b | triage | origin | romanian | 89 | 15 | 0.090 | 0.011 | 0.180 | 0.041 | 0.191 | 0.111 | 0.278 | tested |  | 0.125 | 0.066 | 0.656 | False |
| qwen2.5-7b | triage | origin | syrian | 89 | 15 | 0.270 | 0.124 | 0.411 | 0.000 | 0.281 | 0.180 | 0.382 | tested |  | 0.125 | 0.156 | 0.000 | True |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | age80 | 84 | 15 | 0.464 | 0.369 | 0.562 | 0.869 | 0.646 | 1.100 |
| apertus-8b | dispatch | dialysis | 82 | 15 | 0.671 | 0.598 | 0.744 | 1.537 | 1.229 | 1.901 |
| apertus-8b | dispatch | infant | 83 | 15 | 0.711 | 0.634 | 0.782 | 1.614 | 1.326 | 1.976 |
| apertus-8b | dispatch | pregnant | 80 | 15 | 0.725 | 0.671 | 0.784 | 1.675 | 1.395 | 2.000 |
| apertus-8b | dispatch | wheelchair | 82 | 15 | 0.683 | 0.600 | 0.778 | 1.488 | 1.205 | 1.831 |
| apertus-8b | evacuation | age80 | 90 | 15 | 0.711 | 0.644 | 0.789 | 1.478 | 1.233 | 1.722 |
| apertus-8b | evacuation | dialysis | 90 | 15 | 0.711 | 0.633 | 0.789 | 1.489 | 1.278 | 1.700 |
| apertus-8b | evacuation | infant | 90 | 15 | 0.689 | 0.600 | 0.789 | 1.478 | 1.233 | 1.733 |
| apertus-8b | evacuation | pregnant | 90 | 15 | 0.722 | 0.644 | 0.800 | 1.511 | 1.333 | 1.689 |
| apertus-8b | evacuation | wheelchair | 90 | 15 | 0.667 | 0.589 | 0.756 | 1.478 | 1.256 | 1.711 |
| apertus-8b | housing | age80 | 90 | 15 | 0.822 | 0.711 | 0.922 | 1.156 | 0.956 | 1.344 |
| apertus-8b | housing | dialysis | 90 | 15 | 0.867 | 0.767 | 0.956 | 1.211 | 1.033 | 1.389 |
| apertus-8b | housing | infant | 90 | 15 | 0.900 | 0.811 | 0.967 | 1.378 | 1.167 | 1.578 |
| apertus-8b | housing | pregnant | 90 | 15 | 0.833 | 0.733 | 0.933 | 1.178 | 0.956 | 1.400 |
| apertus-8b | housing | wheelchair | 90 | 15 | 0.789 | 0.656 | 0.911 | 0.978 | 0.778 | 1.167 |
| apertus-8b | relief | age80 | 89 | 15 | 0.461 | 0.352 | 0.562 | 1.345 | 0.024 | 2.518 |
| apertus-8b | relief | dialysis | 90 | 15 | 0.478 | 0.356 | 0.611 | 0.974 | -1.223 | 3.137 |
| apertus-8b | relief | infant | 90 | 15 | 0.489 | 0.356 | 0.622 | 1.572 | -0.735 | 3.649 |
| apertus-8b | relief | pregnant | 90 | 15 | 0.411 | 0.322 | 0.500 | 1.282 | -0.618 | 2.930 |
| apertus-8b | relief | wheelchair | 90 | 15 | 0.378 | 0.267 | 0.478 | -0.867 | -2.166 | 0.277 |
| apertus-8b | triage | age80 | 64 | 15 | 0.469 | 0.333 | 0.582 | 0.734 | 0.477 | 1.015 |
| apertus-8b | triage | dialysis | 65 | 15 | 0.369 | 0.254 | 0.500 | 0.462 | 0.215 | 0.742 |
| apertus-8b | triage | infant | 64 | 15 | 0.641 | 0.528 | 0.742 | 1.172 | 0.929 | 1.406 |
| apertus-8b | triage | pregnant | 60 | 15 | 0.517 | 0.393 | 0.638 | 0.850 | 0.600 | 1.115 |
| apertus-8b | triage | wheelchair | 65 | 15 | 0.431 | 0.295 | 0.552 | 0.646 | 0.385 | 0.917 |
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
| llama-3.1-8b | dispatch | age80 | 76 | 15 | 0.526 | 0.384 | 0.667 | 0.895 | 0.458 | 1.372 |
| llama-3.1-8b | dispatch | dialysis | 76 | 15 | 0.645 | 0.500 | 0.776 | 1.276 | 0.750 | 1.814 |
| llama-3.1-8b | dispatch | infant | 78 | 15 | 0.641 | 0.506 | 0.769 | 1.231 | 0.734 | 1.772 |
| llama-3.1-8b | dispatch | pregnant | 77 | 15 | 0.610 | 0.451 | 0.760 | 1.182 | 0.714 | 1.685 |
| llama-3.1-8b | dispatch | wheelchair | 79 | 15 | 0.430 | 0.293 | 0.560 | 0.759 | 0.405 | 1.090 |
| llama-3.1-8b | evacuation | age80 | 87 | 15 | 0.644 | 0.482 | 0.793 | 1.023 | 0.733 | 1.330 |
| llama-3.1-8b | evacuation | dialysis | 88 | 15 | 0.625 | 0.482 | 0.761 | 1.000 | 0.742 | 1.281 |
| llama-3.1-8b | evacuation | infant | 85 | 15 | 0.565 | 0.400 | 0.726 | 0.882 | 0.563 | 1.221 |
| llama-3.1-8b | evacuation | pregnant | 87 | 15 | 0.621 | 0.488 | 0.750 | 0.989 | 0.736 | 1.271 |
| llama-3.1-8b | evacuation | wheelchair | 87 | 15 | 0.517 | 0.373 | 0.659 | 0.839 | 0.581 | 1.093 |
| llama-3.1-8b | housing | age80 | 90 | 15 | 0.922 | 0.856 | 0.978 | 2.211 | 1.978 | 2.467 |
| llama-3.1-8b | housing | dialysis | 90 | 15 | 0.978 | 0.933 | 1.000 | 2.600 | 2.378 | 2.844 |
| llama-3.1-8b | housing | infant | 90 | 15 | 1.000 | 1.000 | 1.000 | 2.478 | 2.244 | 2.733 |
| llama-3.1-8b | housing | pregnant | 90 | 15 | 0.978 | 0.944 | 1.000 | 2.367 | 2.133 | 2.611 |
| llama-3.1-8b | housing | wheelchair | 90 | 15 | 0.933 | 0.867 | 0.989 | 2.178 | 1.989 | 2.378 |
| llama-3.1-8b | relief | age80 | 81 | 15 | 0.679 | 0.539 | 0.802 | 7.580 | 4.726 | 10.442 |
| llama-3.1-8b | relief | dialysis | 81 | 15 | 0.617 | 0.494 | 0.731 | 5.415 | 3.155 | 7.690 |
| llama-3.1-8b | relief | infant | 82 | 15 | 0.634 | 0.518 | 0.744 | 4.915 | 2.851 | 6.870 |
| llama-3.1-8b | relief | pregnant | 80 | 15 | 0.600 | 0.463 | 0.722 | 4.429 | 2.280 | 6.218 |
| llama-3.1-8b | relief | wheelchair | 80 | 15 | 0.512 | 0.385 | 0.630 | 2.683 | 0.719 | 4.460 |
| llama-3.1-8b | triage | age80 | 83 | 15 | 0.470 | 0.321 | 0.617 | 0.735 | 0.476 | 1.012 |
| llama-3.1-8b | triage | dialysis | 80 | 15 | 0.388 | 0.247 | 0.545 | 0.525 | 0.272 | 0.817 |
| llama-3.1-8b | triage | infant | 82 | 15 | 0.427 | 0.279 | 0.593 | 0.671 | 0.417 | 0.963 |
| llama-3.1-8b | triage | pregnant | 85 | 15 | 0.459 | 0.293 | 0.632 | 0.741 | 0.459 | 1.036 |
| llama-3.1-8b | triage | wheelchair | 83 | 15 | 0.277 | 0.174 | 0.386 | 0.446 | 0.241 | 0.659 |
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
| meltemi-7b | housing | infant | 90 | 15 | 0.356 | 0.256 | 0.456 | 0.333 | 0.200 | 0.444 |
| meltemi-7b | housing | pregnant | 90 | 15 | 0.367 | 0.256 | 0.478 | 0.411 | 0.311 | 0.511 |
| meltemi-7b | housing | wheelchair | 90 | 15 | 0.333 | 0.233 | 0.433 | 0.367 | 0.267 | 0.456 |
| meltemi-7b | relief | age80 | 69 | 15 | 0.609 | 0.515 | 0.699 | 7.298 | 4.213 | 10.355 |
| meltemi-7b | relief | dialysis | 68 | 15 | 0.500 | 0.381 | 0.623 | 7.122 | 4.439 | 10.176 |
| meltemi-7b | relief | infant | 72 | 15 | 0.458 | 0.352 | 0.562 | 2.224 | 0.387 | 3.997 |
| meltemi-7b | relief | pregnant | 67 | 15 | 0.478 | 0.313 | 0.636 | 5.348 | 2.223 | 8.546 |
| meltemi-7b | relief | wheelchair | 70 | 15 | 0.500 | 0.394 | 0.586 | 3.399 | 1.089 | 5.647 |
| meltemi-7b | triage | age80 | 90 | 15 | 0.267 | 0.189 | 0.344 | 0.378 | 0.144 | 0.600 |
| meltemi-7b | triage | dialysis | 90 | 15 | 0.333 | 0.244 | 0.422 | 0.467 | 0.167 | 0.789 |
| meltemi-7b | triage | infant | 89 | 15 | 0.326 | 0.225 | 0.432 | 0.438 | 0.169 | 0.685 |
| meltemi-7b | triage | pregnant | 90 | 15 | 0.367 | 0.267 | 0.467 | 0.589 | 0.267 | 0.933 |
| meltemi-7b | triage | wheelchair | 90 | 15 | 0.278 | 0.167 | 0.389 | 0.478 | 0.222 | 0.789 |
| qwen2.5-7b | dispatch | age80 | 88 | 15 | 0.568 | 0.427 | 0.705 | 1.125 | 0.750 | 1.460 |
| qwen2.5-7b | dispatch | dialysis | 88 | 15 | 0.670 | 0.517 | 0.807 | 1.341 | 0.909 | 1.770 |
| qwen2.5-7b | dispatch | infant | 88 | 15 | 0.636 | 0.517 | 0.756 | 1.273 | 0.900 | 1.651 |
| qwen2.5-7b | dispatch | pregnant | 88 | 15 | 0.659 | 0.544 | 0.770 | 1.375 | 1.045 | 1.699 |
| qwen2.5-7b | dispatch | wheelchair | 88 | 15 | 0.523 | 0.409 | 0.628 | 1.011 | 0.667 | 1.333 |
| qwen2.5-7b | evacuation | age80 | 90 | 15 | 0.700 | 0.578 | 0.811 | 1.122 | 0.811 | 1.422 |
| qwen2.5-7b | evacuation | dialysis | 90 | 15 | 0.722 | 0.600 | 0.833 | 1.189 | 0.844 | 1.522 |
| qwen2.5-7b | evacuation | infant | 90 | 15 | 0.700 | 0.578 | 0.822 | 1.178 | 0.833 | 1.522 |
| qwen2.5-7b | evacuation | pregnant | 90 | 15 | 0.678 | 0.556 | 0.800 | 1.133 | 0.789 | 1.467 |
| qwen2.5-7b | evacuation | wheelchair | 90 | 15 | 0.633 | 0.511 | 0.756 | 1.033 | 0.711 | 1.356 |
| qwen2.5-7b | housing | age80 | 90 | 15 | 0.756 | 0.689 | 0.833 | 0.844 | 0.744 | 0.956 |
| qwen2.5-7b | housing | dialysis | 90 | 15 | 0.989 | 0.967 | 1.000 | 1.878 | 1.733 | 2.011 |
| qwen2.5-7b | housing | infant | 90 | 15 | 0.733 | 0.689 | 0.789 | 1.189 | 1.111 | 1.267 |
| qwen2.5-7b | housing | pregnant | 90 | 15 | 1.000 | 1.000 | 1.000 | 1.933 | 1.878 | 2.000 |
| qwen2.5-7b | housing | wheelchair | 90 | 15 | 0.756 | 0.678 | 0.833 | 0.767 | 0.689 | 0.844 |
| qwen2.5-7b | relief | age80 | 90 | 15 | 0.689 | 0.589 | 0.789 | 7.667 | 6.167 | 9.111 |
| qwen2.5-7b | relief | dialysis | 90 | 15 | 0.733 | 0.589 | 0.856 | 8.611 | 6.500 | 10.500 |
| qwen2.5-7b | relief | infant | 90 | 15 | 0.656 | 0.511 | 0.778 | 6.500 | 4.833 | 8.056 |
| qwen2.5-7b | relief | pregnant | 90 | 15 | 0.667 | 0.533 | 0.778 | 7.389 | 5.776 | 8.778 |
| qwen2.5-7b | relief | wheelchair | 90 | 15 | 0.544 | 0.433 | 0.644 | 4.444 | 3.333 | 5.446 |
| qwen2.5-7b | triage | age80 | 90 | 15 | 0.422 | 0.278 | 0.578 | 0.556 | 0.322 | 0.811 |
| qwen2.5-7b | triage | dialysis | 89 | 15 | 0.270 | 0.169 | 0.371 | 0.258 | 0.114 | 0.411 |
| qwen2.5-7b | triage | infant | 90 | 15 | 0.478 | 0.322 | 0.634 | 0.733 | 0.411 | 1.056 |
| qwen2.5-7b | triage | pregnant | 88 | 15 | 0.455 | 0.315 | 0.607 | 0.557 | 0.349 | 0.795 |
| qwen2.5-7b | triage | wheelchair | 89 | 15 | 0.281 | 0.178 | 0.382 | 0.315 | 0.182 | 0.450 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | triage | need=age80 | 74 | 15 | 0.162 |
| apertus-8b | triage | need=pregnant | 70 | 15 | 0.186 |
| apertus-8b | triage | need=wheelchair | 73 | 15 | 0.192 |
| apertus-8b | triage | need=dialysis | 76 | 15 | 0.197 |
| apertus-8b | triage | need=infant | 78 | 15 | 0.295 |
| apertus-8b | triage | origin=syrian | 74 | 15 | 0.338 |
| apertus-8b | triage | base | 71 | 15 | 0.366 |
| apertus-8b | triage | origin=romanian | 74 | 15 | 0.378 |
| apertus-8b | triage | origin=local_migrant | 71 | 15 | 0.380 |
| apertus-8b | triage | placebo | 72 | 15 | 0.444 |
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
| llama-3.1-8b | triage | need=wheelchair | 85 | 15 | 0.224 |
| llama-3.1-8b | triage | need=dialysis | 83 | 15 | 0.241 |
| llama-3.1-8b | triage | need=infant | 85 | 15 | 0.318 |
| llama-3.1-8b | triage | need=age80 | 86 | 15 | 0.326 |
| llama-3.1-8b | triage | need=pregnant | 87 | 15 | 0.333 |
| llama-3.1-8b | triage | origin=syrian | 84 | 15 | 0.571 |
| llama-3.1-8b | triage | origin=local_migrant | 84 | 15 | 0.619 |
| llama-3.1-8b | triage | origin=romanian | 86 | 15 | 0.640 |
| llama-3.1-8b | triage | base | 87 | 15 | 0.678 |
| llama-3.1-8b | triage | placebo | 82 | 15 | 0.695 |
| meltemi-7b | triage | need=age80 | 90 | 15 | 0.033 |
| meltemi-7b | triage | need=wheelchair | 90 | 15 | 0.044 |
| meltemi-7b | triage | origin=syrian | 90 | 15 | 0.044 |
| meltemi-7b | triage | need=dialysis | 90 | 15 | 0.056 |
| meltemi-7b | triage | need=infant | 89 | 15 | 0.067 |
| meltemi-7b | triage | need=pregnant | 90 | 15 | 0.078 |
| meltemi-7b | triage | origin=local_migrant | 90 | 15 | 0.089 |
| meltemi-7b | triage | origin=romanian | 90 | 15 | 0.089 |
| meltemi-7b | triage | base | 90 | 15 | 0.100 |
| meltemi-7b | triage | placebo | 90 | 15 | 0.122 |
| qwen2.5-7b | triage | need=dialysis | 89 | 15 | 0.079 |
| qwen2.5-7b | triage | need=wheelchair | 89 | 15 | 0.079 |
| qwen2.5-7b | triage | need=pregnant | 88 | 15 | 0.102 |
| qwen2.5-7b | triage | need=age80 | 90 | 15 | 0.111 |
| qwen2.5-7b | triage | need=infant | 90 | 15 | 0.211 |
| qwen2.5-7b | triage | base | 90 | 15 | 0.600 |
| qwen2.5-7b | triage | origin=romanian | 89 | 15 | 0.607 |
| qwen2.5-7b | triage | origin=syrian | 89 | 15 | 0.618 |
| qwen2.5-7b | triage | origin=local_migrant | 89 | 15 | 0.629 |
| qwen2.5-7b | triage | placebo | 88 | 15 | 0.648 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el | kendall_w | 0.531 | 15 | 28 |
| apertus-8b | dispatch | en | kendall_w | 0.404 | 15 | 29 |
| apertus-8b | dispatch | fr | kendall_w | 0.375 | 15 | 29 |
| apertus-8b | evacuation | el | kendall_w | 0.540 | 15 | 30 |
| apertus-8b | evacuation | en | kendall_w | 0.413 | 15 | 30 |
| apertus-8b | evacuation | fr | kendall_w | 0.353 | 15 | 30 |
| apertus-8b | housing | el | krippendorff_alpha | 0.559 | 15 | 30 |
| apertus-8b | housing | en | krippendorff_alpha | 0.608 | 15 | 30 |
| apertus-8b | housing | fr | krippendorff_alpha | 0.469 | 15 | 30 |
| apertus-8b | relief | el | krippendorff_alpha | 0.546 | 15 | 30 |
| apertus-8b | relief | en | krippendorff_alpha | 0.450 | 15 | 30 |
| apertus-8b | relief | fr | krippendorff_alpha | 0.501 | 15 | 30 |
| apertus-8b | triage | el | kendall_w | 0.633 | 14 | 23 |
| apertus-8b | triage | en | kendall_w | 0.846 | 15 | 29 |
| apertus-8b | triage | fr | kendall_w | 0.775 | 13 | 19 |
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
| llama-3.1-8b | dispatch | el | kendall_w | 0.638 | 15 | 28 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.654 | 15 | 27 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.645 | 15 | 26 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.514 | 15 | 29 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.564 | 15 | 29 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.753 | 15 | 30 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.613 | 15 | 30 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.688 | 15 | 30 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | -0.349 | 15 | 30 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.474 | 15 | 30 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.618 | 15 | 27 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.463 | 14 | 25 |
| llama-3.1-8b | triage | el | kendall_w | 0.758 | 15 | 28 |
| llama-3.1-8b | triage | en | kendall_w | 0.864 | 15 | 29 |
| llama-3.1-8b | triage | fr | kendall_w | 0.907 | 15 | 30 |
| meltemi-7b | dispatch | el | kendall_w | 0.510 | 15 | 30 |
| meltemi-7b | dispatch | en | kendall_w | 0.447 | 15 | 30 |
| meltemi-7b | dispatch | fr | kendall_w | 0.493 | 15 | 30 |
| meltemi-7b | evacuation | el | kendall_w | 0.467 | 15 | 30 |
| meltemi-7b | evacuation | en | kendall_w | 0.560 | 15 | 30 |
| meltemi-7b | evacuation | fr | kendall_w | 0.480 | 15 | 30 |
| meltemi-7b | housing | el | krippendorff_alpha | 0.341 | 15 | 30 |
| meltemi-7b | housing | en | krippendorff_alpha | 0.099 | 15 | 30 |
| meltemi-7b | housing | fr | krippendorff_alpha | -0.278 | 15 | 30 |
| meltemi-7b | relief | el | krippendorff_alpha | 0.544 | 15 | 30 |
| meltemi-7b | relief | en | krippendorff_alpha | 0.443 | 15 | 30 |
| meltemi-7b | relief | fr | krippendorff_alpha | 0.487 | 12 | 17 |
| meltemi-7b | triage | el | kendall_w | 0.510 | 15 | 30 |
| meltemi-7b | triage | en | kendall_w | 0.690 | 15 | 30 |
| meltemi-7b | triage | fr | kendall_w | 0.540 | 15 | 30 |
| qwen2.5-7b | dispatch | el | kendall_w | 0.607 | 15 | 30 |
| qwen2.5-7b | dispatch | en | kendall_w | 0.823 | 15 | 28 |
| qwen2.5-7b | dispatch | fr | kendall_w | 0.780 | 15 | 30 |
| qwen2.5-7b | evacuation | el | kendall_w | 0.640 | 15 | 30 |
| qwen2.5-7b | evacuation | en | kendall_w | 0.887 | 15 | 30 |
| qwen2.5-7b | evacuation | fr | kendall_w | 0.913 | 15 | 30 |
| qwen2.5-7b | housing | el | krippendorff_alpha | 0.000 | 15 | 30 |
| qwen2.5-7b | housing | en | krippendorff_alpha | 1.000 | 15 | 30 |
| qwen2.5-7b | housing | fr | krippendorff_alpha | 0.847 | 15 | 30 |
| qwen2.5-7b | relief | el | krippendorff_alpha | 0.298 | 15 | 30 |
| qwen2.5-7b | relief | en | krippendorff_alpha | 0.417 | 15 | 30 |
| qwen2.5-7b | relief | fr | krippendorff_alpha | 0.246 | 15 | 30 |
| qwen2.5-7b | triage | el | kendall_w | 0.693 | 15 | 30 |
| qwen2.5-7b | triage | en | kendall_w | 0.960 | 15 | 30 |
| qwen2.5-7b | triage | fr | kendall_w | 0.907 | 15 | 30 |

## Cross-lingual consistency of the base cases

| model | task | pair | cases | difference | lo | hi | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | el-en | 15 | 0.400 | -0.300 | 1.267 | 0.329 |
| apertus-8b | dispatch | el-fr | 15 | 0.433 | -0.200 | 1.133 | 0.213 |
| apertus-8b | dispatch | en-fr | 15 | 0.033 | -0.534 | 0.600 | 0.907 |
| apertus-8b | evacuation | el-en | 15 | -0.033 | -0.567 | 0.500 | 0.921 |
| apertus-8b | evacuation | el-fr | 15 | -0.300 | -0.800 | 0.133 | 0.251 |
| apertus-8b | evacuation | en-fr | 15 | -0.267 | -0.733 | 0.200 | 0.318 |
| apertus-8b | housing | el-en | 15 | 0.100 | -0.033 | 0.233 | 0.240 |
| apertus-8b | housing | el-fr | 15 | 0.500 | 0.167 | 0.833 | 0.002 |
| apertus-8b | housing | en-fr | 15 | 0.400 | 0.100 | 0.700 | 0.007 |
| apertus-8b | relief | el-en | 15 | -2.172 | -5.576 | 1.288 | 0.221 |
| apertus-8b | relief | el-fr | 15 | -2.746 | -4.825 | -0.692 | 0.011 |
| apertus-8b | relief | en-fr | 15 | -0.574 | -3.009 | 1.691 | 0.616 |
| apertus-8b | triage | el-en | 14 | -0.071 | -0.714 | 0.500 | 0.856 |
| apertus-8b | triage | el-fr | 13 | -0.500 | -1.077 | 0.038 | 0.087 |
| apertus-8b | triage | en-fr | 13 | -0.308 | -0.885 | 0.346 | 0.384 |
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
| llama-3.1-8b | dispatch | el-en | 15 | 0.600 | 0.067 | 1.167 | 0.019 |
| llama-3.1-8b | dispatch | el-fr | 15 | 0.633 | 0.067 | 1.200 | 0.031 |
| llama-3.1-8b | dispatch | en-fr | 15 | 0.033 | -0.367 | 0.367 | 0.860 |
| llama-3.1-8b | evacuation | el-en | 15 | -0.033 | -0.333 | 0.233 | 0.938 |
| llama-3.1-8b | evacuation | el-fr | 15 | 0.200 | -0.167 | 0.533 | 0.306 |
| llama-3.1-8b | evacuation | en-fr | 15 | 0.233 | 0.033 | 0.433 | 0.047 |
| llama-3.1-8b | housing | el-en | 15 | 0.100 | -0.433 | 0.700 | 0.787 |
| llama-3.1-8b | housing | el-fr | 15 | 2.467 | 1.900 | 3.067 | 0.000 |
| llama-3.1-8b | housing | en-fr | 15 | 2.367 | 1.700 | 3.000 | 0.000 |
| llama-3.1-8b | relief | el-en | 15 | 1.224 | -3.068 | 6.009 | 0.637 |
| llama-3.1-8b | relief | el-fr | 14 | -0.492 | -3.340 | 2.579 | 0.733 |
| llama-3.1-8b | relief | en-fr | 14 | -1.506 | -5.459 | 2.398 | 0.513 |
| llama-3.1-8b | triage | el-en | 15 | -0.167 | -0.367 | 0.000 | 0.062 |
| llama-3.1-8b | triage | el-fr | 15 | -0.367 | -0.633 | -0.100 | 0.003 |
| llama-3.1-8b | triage | en-fr | 15 | -0.200 | -0.400 | -0.033 | 0.049 |
| meltemi-7b | dispatch | el-en | 15 | -0.033 | -0.534 | 0.433 | 0.931 |
| meltemi-7b | dispatch | el-fr | 15 | -0.333 | -1.133 | 0.367 | 0.418 |
| meltemi-7b | dispatch | en-fr | 15 | -0.300 | -1.233 | 0.567 | 0.554 |
| meltemi-7b | evacuation | el-en | 15 | 0.500 | 0.267 | 0.733 | 0.000 |
| meltemi-7b | evacuation | el-fr | 15 | 0.333 | -0.067 | 0.733 | 0.115 |
| meltemi-7b | evacuation | en-fr | 15 | -0.167 | -0.567 | 0.267 | 0.487 |
| meltemi-7b | housing | el-en | 15 | -0.033 | -0.167 | 0.100 | 0.794 |
| meltemi-7b | housing | el-fr | 15 | 0.700 | 0.300 | 1.067 | 0.002 |
| meltemi-7b | housing | en-fr | 15 | 0.733 | 0.400 | 1.067 | 0.001 |
| meltemi-7b | relief | el-en | 15 | -0.493 | -3.899 | 2.356 | 0.762 |
| meltemi-7b | relief | el-fr | 12 | -0.078 | -2.553 | 2.942 | 0.870 |
| meltemi-7b | relief | en-fr | 12 | 1.268 | -3.157 | 5.661 | 0.602 |
| meltemi-7b | triage | el-en | 15 | -0.167 | -0.400 | 0.033 | 0.141 |
| meltemi-7b | triage | el-fr | 15 | 0.133 | -0.300 | 0.533 | 0.552 |
| meltemi-7b | triage | en-fr | 15 | 0.300 | -0.167 | 0.767 | 0.224 |
| qwen2.5-7b | dispatch | el-en | 15 | -0.200 | -0.500 | 0.067 | 0.194 |
| qwen2.5-7b | dispatch | el-fr | 15 | 0.133 | -0.200 | 0.500 | 0.507 |
| qwen2.5-7b | dispatch | en-fr | 15 | 0.333 | -0.033 | 0.733 | 0.100 |
| qwen2.5-7b | evacuation | el-en | 15 | 0.300 | -0.033 | 0.600 | 0.085 |
| qwen2.5-7b | evacuation | el-fr | 15 | 0.100 | -0.200 | 0.400 | 0.562 |
| qwen2.5-7b | evacuation | en-fr | 15 | -0.200 | -0.333 | -0.033 | 0.025 |
| qwen2.5-7b | housing | el-en | 15 | -0.100 | -0.267 | 0.000 | 0.229 |
| qwen2.5-7b | housing | el-fr | 15 | -0.633 | -0.967 | -0.333 | 0.000 |
| qwen2.5-7b | housing | en-fr | 15 | -0.533 | -0.867 | -0.267 | 0.000 |
| qwen2.5-7b | relief | el-en | 15 | 0.667 | -1.500 | 2.833 | 0.602 |
| qwen2.5-7b | relief | el-fr | 15 | 2.000 | 0.167 | 4.000 | 0.049 |
| qwen2.5-7b | relief | en-fr | 15 | 1.333 | -0.167 | 2.833 | 0.084 |
| qwen2.5-7b | triage | el-en | 15 | -0.300 | -0.667 | 0.033 | 0.092 |
| qwen2.5-7b | triage | el-fr | 15 | -0.233 | -0.533 | 0.067 | 0.153 |
| qwen2.5-7b | triage | en-fr | 15 | 0.067 | -0.167 | 0.333 | 0.658 |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area | roma_settlement | ambiguous | 17 | 3 | 1.235 | 0.800 | 1.500 |  | 0.588 | 0.400 | 0.833 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.400 | 0.250 | 0.500 |  | 0.700 | 0.667 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | social_housing | ambiguous | 51 | 9 | 0.255 | -0.148 | 0.771 | 0.254 | 0.373 | 0.259 | 0.462 | tested |  |
| apertus-8b | dispatch | area | social_housing | clear | 32 | 6 | 0.125 | -0.062 | 0.321 |  | 0.500 | 0.300 | 0.694 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | area | villas | ambiguous | 51 | 9 | -0.569 | -0.920 | -0.260 | 0.000 | 0.588 | 0.471 | 0.706 | tested |  |
| apertus-8b | dispatch | area | villas | clear | 32 | 6 | -0.500 | -0.818 | -0.226 |  | 0.469 | 0.276 | 0.647 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | gender | female | ambiguous | 53 | 9 | 0.208 | -0.111 | 0.588 | 0.252 | 0.472 | 0.352 | 0.604 | tested |  |
| apertus-8b | dispatch | gender | female | clear | 32 | 6 | 0.312 | 0.121 | 0.516 |  | 0.531 | 0.375 | 0.733 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | any_minority | ambiguous | 156 | 9 | 0.141 | -0.114 | 0.407 | 0.272 | 0.442 | 0.316 | 0.563 | tested |  |
| apertus-8b | dispatch | origin | any_minority | clear | 97 | 6 | -0.113 | -0.354 | 0.137 |  | 0.454 | 0.262 | 0.626 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | local_migrant | ambiguous | 53 | 9 | 0.094 | -0.204 | 0.392 | 0.552 | 0.396 | 0.288 | 0.500 | tested |  |
| apertus-8b | dispatch | origin | local_migrant | clear | 33 | 6 | 0.030 | -0.152 | 0.233 |  | 0.455 | 0.250 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | romanian | ambiguous | 52 | 9 | 0.096 | -0.185 | 0.373 | 0.530 | 0.481 | 0.278 | 0.660 | tested |  |
| apertus-8b | dispatch | origin | romanian | clear | 33 | 6 | -0.182 | -0.501 | 0.188 |  | 0.515 | 0.290 | 0.694 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | origin | syrian | ambiguous | 51 | 9 | 0.235 | -0.060 | 0.569 | 0.149 | 0.451 | 0.260 | 0.640 | tested |  |
| apertus-8b | dispatch | origin | syrian | clear | 31 | 6 | -0.194 | -0.533 | 0.121 |  | 0.387 | 0.207 | 0.576 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | asylum_seeker | ambiguous | 52 | 9 | 1.058 | 0.611 | 1.580 | 0.000 | 0.596 | 0.444 | 0.731 | tested |  |
| apertus-8b | dispatch | status | asylum_seeker | clear | 31 | 6 | -0.194 | -0.556 | 0.118 |  | 0.613 | 0.406 | 0.813 | descriptive (fewer than 8 cases) |  |
| apertus-8b | dispatch | status | seasonal_worker | ambiguous | 52 | 9 | 0.115 | -0.160 | 0.370 | 0.448 | 0.423 | 0.255 | 0.577 | tested |  |
| apertus-8b | dispatch | status | seasonal_worker | clear | 32 | 6 | -0.250 | -0.485 | 0.000 |  | 0.594 | 0.394 | 0.758 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 1.167 | 1.000 | 1.333 |  | 0.556 | 0.500 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.583 | 0.333 | 0.833 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | social_housing | ambiguous | 54 | 9 | 0.833 | 0.556 | 1.130 | 0.000 | 0.444 | 0.315 | 0.556 | tested |  |
| apertus-8b | evacuation | area | social_housing | clear | 36 | 6 | 0.833 | 0.333 | 1.417 |  | 0.556 | 0.417 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | area | villas | ambiguous | 54 | 9 | -0.370 | -0.519 | -0.241 | 0.000 | 0.389 | 0.296 | 0.500 | tested |  |
| apertus-8b | evacuation | area | villas | clear | 36 | 6 | -0.444 | -0.694 | -0.222 |  | 0.417 | 0.278 | 0.611 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | any_minority | ambiguous | 162 | 9 | 0.395 | 0.160 | 0.654 | 0.000 | 0.414 | 0.302 | 0.512 | tested |  |
| apertus-8b | evacuation | origin | any_minority | clear | 108 | 6 | 0.083 | -0.037 | 0.287 |  | 0.417 | 0.278 | 0.528 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | local_migrant | ambiguous | 54 | 9 | 0.204 | -0.037 | 0.500 | 0.151 | 0.370 | 0.222 | 0.500 | tested |  |
| apertus-8b | evacuation | origin | local_migrant | clear | 36 | 6 | -0.111 | -0.417 | 0.167 |  | 0.361 | 0.194 | 0.472 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | romanian | ambiguous | 54 | 9 | 0.019 | -0.296 | 0.315 | 0.904 | 0.333 | 0.222 | 0.444 | tested |  |
| apertus-8b | evacuation | origin | romanian | clear | 36 | 6 | -0.306 | -0.417 | -0.194 |  | 0.278 | 0.194 | 0.389 | descriptive (fewer than 8 cases) |  |
| apertus-8b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.963 | 0.630 | 1.259 | 0.000 | 0.537 | 0.389 | 0.648 | tested |  |
| apertus-8b | evacuation | origin | syrian | clear | 36 | 6 | 0.667 | 0.306 | 1.111 |  | 0.611 | 0.389 | 0.833 | descriptive (fewer than 8 cases) |  |
| apertus-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.944 | 0.833 | 1.000 |  | 0.667 | 0.500 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | roma_settlement | clear | 12 | 2 | 0.833 | 0.833 | 0.833 |  | 0.750 | 0.667 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | social_housing | ambiguous | 54 | 9 | 0.259 | 0.130 | 0.407 | 0.000 | 0.333 | 0.185 | 0.481 | tested | 0.000 |
| apertus-8b | housing | area | social_housing | clear | 36 | 6 | 0.139 | 0.000 | 0.306 |  | 0.278 | 0.194 | 0.389 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | area | villas | ambiguous | 54 | 9 | -0.315 | -0.500 | -0.111 | 0.003 | 0.648 | 0.537 | 0.778 | tested | 0.037 |
| apertus-8b | housing | area | villas | clear | 36 | 6 | -0.111 | -0.278 | 0.083 |  | 0.500 | 0.444 | 0.583 | descriptive (fewer than 8 cases) | 0.083 |
| apertus-8b | housing | gender | female | ambiguous | 54 | 9 | 0.370 | 0.204 | 0.556 | 0.000 | 0.556 | 0.444 | 0.685 | tested | 0.000 |
| apertus-8b | housing | gender | female | clear | 36 | 6 | 0.333 | 0.139 | 0.611 |  | 0.472 | 0.222 | 0.694 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.228 | 0.111 | 0.364 | 0.000 | 0.407 | 0.321 | 0.481 | tested | 0.000 |
| apertus-8b | housing | origin | any_minority | clear | 108 | 6 | 0.259 | 0.130 | 0.389 |  | 0.407 | 0.352 | 0.491 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.222 | 0.000 | 0.426 | 0.063 | 0.444 | 0.333 | 0.556 | tested | 0.000 |
| apertus-8b | housing | origin | local_migrant | clear | 36 | 6 | 0.194 | 0.028 | 0.333 |  | 0.333 | 0.278 | 0.417 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | romanian | ambiguous | 54 | 9 | 0.167 | -0.037 | 0.389 | 0.154 | 0.407 | 0.241 | 0.574 | tested | 0.000 |
| apertus-8b | housing | origin | romanian | clear | 36 | 6 | 0.278 | 0.139 | 0.417 |  | 0.500 | 0.417 | 0.583 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | origin | syrian | ambiguous | 54 | 9 | 0.296 | 0.185 | 0.426 | 0.000 | 0.370 | 0.259 | 0.500 | tested | 0.000 |
| apertus-8b | housing | origin | syrian | clear | 36 | 6 | 0.306 | 0.139 | 0.472 |  | 0.389 | 0.278 | 0.528 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.648 | 0.500 | 0.796 | 0.000 | 0.593 | 0.481 | 0.722 | tested | 0.000 |
| apertus-8b | housing | status | asylum_seeker | clear | 36 | 6 | 0.472 | 0.194 | 0.694 |  | 0.472 | 0.333 | 0.611 | descriptive (fewer than 8 cases) | 0.000 |
| apertus-8b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -0.222 | -0.315 | -0.148 | 0.000 | 0.481 | 0.352 | 0.593 | tested | 0.000 |
| apertus-8b | housing | status | seasonal_worker | clear | 36 | 6 | -0.250 | -0.361 | -0.139 |  | 0.556 | 0.417 | 0.694 | descriptive (fewer than 8 cases) | 0.028 |
| apertus-8b | relief | area | roma_settlement | ambiguous | 18 | 3 | -1.902 | -3.833 | 1.712 |  | 0.389 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | roma_settlement | clear | 12 | 2 | -1.944 | -3.333 | -0.556 |  | 0.583 | 0.500 | 0.667 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | social_housing | ambiguous | 54 | 9 | 0.450 | -2.048 | 2.525 | 0.695 | 0.519 | 0.370 | 0.648 | tested |  |
| apertus-8b | relief | area | social_housing | clear | 36 | 6 | 0.732 | -1.339 | 2.702 |  | 0.444 | 0.306 | 0.583 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | area | villas | ambiguous | 54 | 9 | -1.885 | -4.218 | 0.152 | 0.075 | 0.463 | 0.296 | 0.630 | tested |  |
| apertus-8b | relief | area | villas | clear | 36 | 6 | 0.652 | -1.212 | 2.252 |  | 0.556 | 0.444 | 0.694 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | any_minority | ambiguous | 162 | 9 | 0.135 | -2.143 | 2.898 | 0.974 | 0.543 | 0.407 | 0.679 | tested |  |
| apertus-8b | relief | origin | any_minority | clear | 108 | 6 | -0.459 | -2.664 | 1.939 |  | 0.583 | 0.454 | 0.731 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | local_migrant | ambiguous | 54 | 9 | -0.933 | -3.827 | 1.826 | 0.511 | 0.519 | 0.370 | 0.648 | tested |  |
| apertus-8b | relief | origin | local_migrant | clear | 36 | 6 | -1.132 | -3.418 | 1.125 |  | 0.556 | 0.389 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | romanian | ambiguous | 54 | 9 | 0.210 | -2.766 | 4.170 | 0.995 | 0.500 | 0.333 | 0.667 | tested |  |
| apertus-8b | relief | origin | romanian | clear | 36 | 6 | 0.105 | -2.563 | 3.089 |  | 0.583 | 0.417 | 0.750 | descriptive (fewer than 8 cases) |  |
| apertus-8b | relief | origin | syrian | ambiguous | 54 | 9 | 1.129 | -0.430 | 2.848 | 0.162 | 0.611 | 0.444 | 0.759 | tested |  |
| apertus-8b | relief | origin | syrian | clear | 36 | 6 | -0.349 | -3.325 | 3.368 |  | 0.611 | 0.528 | 0.722 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | any_minority | ambiguous | 113 | 9 | 0.319 | -0.055 | 0.684 | 0.095 | 0.389 | 0.270 | 0.500 | tested |  |
| apertus-8b | triage | origin | any_minority | clear | 82 | 6 | 0.159 | 0.081 | 0.233 |  | 0.244 | 0.138 | 0.356 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | local_migrant | ambiguous | 36 | 9 | 0.333 | -0.065 | 0.730 | 0.144 | 0.417 | 0.344 | 0.488 | tested |  |
| apertus-8b | triage | origin | local_migrant | clear | 27 | 6 | 0.074 | -0.067 | 0.185 |  | 0.148 | 0.074 | 0.200 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | romanian | ambiguous | 39 | 9 | 0.231 | -0.139 | 0.571 | 0.246 | 0.359 | 0.222 | 0.476 | tested |  |
| apertus-8b | triage | origin | romanian | clear | 27 | 6 | 0.222 | 0.083 | 0.333 |  | 0.333 | 0.208 | 0.467 | descriptive (fewer than 8 cases) |  |
| apertus-8b | triage | origin | syrian | ambiguous | 38 | 9 | 0.395 | -0.027 | 0.886 | 0.088 | 0.395 | 0.231 | 0.579 | tested |  |
| apertus-8b | triage | origin | syrian | clear | 28 | 6 | 0.179 | 0.036 | 0.322 |  | 0.250 | 0.083 | 0.433 | descriptive (fewer than 8 cases) |  |
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
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 50 | 9 | -0.180 | -0.558 | 0.255 | 0.422 | 0.360 | 0.250 | 0.462 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 27 | 6 | 0.037 | -0.133 | 0.250 |  | 0.259 | 0.095 | 0.375 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 49 | 9 | -0.755 | -1.154 | -0.444 | 0.000 | 0.469 | 0.327 | 0.642 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 28 | 6 | -0.393 | -0.647 | -0.077 |  | 0.321 | 0.077 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 52 | 9 | 0.019 | -0.250 | 0.314 | 0.971 | 0.308 | 0.185 | 0.434 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 28 | 6 | -0.107 | -0.222 | 0.000 |  | 0.107 | 0.000 | 0.222 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 149 | 9 | -0.034 | -0.188 | 0.109 | 0.703 | 0.262 | 0.175 | 0.359 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 83 | 6 | -0.036 | -0.074 | 0.000 |  | 0.157 | 0.013 | 0.273 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 49 | 9 | -0.122 | -0.392 | 0.137 | 0.411 | 0.265 | 0.170 | 0.364 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 28 | 6 | -0.036 | -0.100 | 0.000 |  | 0.179 | 0.000 | 0.344 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 51 | 9 | 0.000 | -0.167 | 0.184 | 1.000 | 0.255 | 0.100 | 0.440 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 29 | 6 | 0.034 | 0.000 | 0.097 |  | 0.103 | 0.000 | 0.219 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 49 | 9 | 0.020 | -0.118 | 0.163 | 0.890 | 0.265 | 0.191 | 0.321 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 26 | 6 | -0.115 | -0.233 | 0.000 |  | 0.192 | 0.042 | 0.310 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 50 | 9 | 0.120 | -0.191 | 0.445 | 0.537 | 0.480 | 0.373 | 0.569 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 23 | 6 | 0.261 | 0.048 | 0.480 |  | 0.304 | 0.100 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 51 | 9 | -0.471 | -0.885 | -0.083 | 0.020 | 0.451 | 0.321 | 0.596 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 25 | 6 | -0.160 | -0.296 | 0.000 |  | 0.200 | 0.000 | 0.444 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.611 | 0.167 | 1.333 |  | 0.444 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.500 | 0.000 | 1.000 |  | 0.250 | 0.000 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 53 | 9 | 0.642 | 0.296 | 1.000 | 0.000 | 0.453 | 0.283 | 0.608 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 31 | 6 | 0.387 | 0.133 | 0.621 |  | 0.323 | 0.111 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 52 | 9 | -0.538 | -0.942 | -0.173 | 0.002 | 0.442 | 0.259 | 0.608 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 34 | 6 | -0.206 | -0.353 | -0.059 |  | 0.206 | 0.059 | 0.353 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 160 | 9 | 0.544 | 0.309 | 0.795 | 0.000 | 0.425 | 0.309 | 0.532 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 101 | 6 | 0.188 | 0.010 | 0.364 |  | 0.198 | 0.081 | 0.311 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 52 | 9 | 0.308 | 0.000 | 0.583 | 0.053 | 0.308 | 0.192 | 0.417 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 34 | 6 | 0.059 | -0.125 | 0.222 |  | 0.176 | 0.059 | 0.294 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 54 | 9 | 0.463 | 0.185 | 0.741 | 0.000 | 0.389 | 0.259 | 0.519 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 34 | 6 | 0.147 | -0.031 | 0.324 |  | 0.176 | 0.061 | 0.278 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.852 | 0.630 | 1.093 | 0.000 | 0.574 | 0.444 | 0.704 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 33 | 6 | 0.364 | 0.121 | 0.606 |  | 0.242 | 0.088 | 0.406 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 1.000 | 0.333 | 1.500 |  | 0.556 | 0.167 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 1.167 | 0.667 | 1.667 |  | 0.500 | 0.333 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 54 | 9 | 0.389 | 0.222 | 0.574 | 0.000 | 0.519 | 0.407 | 0.648 | tested | 0.000 |
| llama-3.1-8b | housing | area | social_housing | clear | 36 | 6 | 0.472 | -0.167 | 1.194 |  | 0.528 | 0.333 | 0.694 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | villas | ambiguous | 54 | 9 | -1.852 | -2.334 | -1.389 | 0.000 | 0.833 | 0.741 | 0.926 | tested | 0.000 |
| llama-3.1-8b | housing | area | villas | clear | 36 | 6 | -1.389 | -1.722 | -1.056 |  | 0.667 | 0.556 | 0.806 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | gender | female | ambiguous | 54 | 9 | 0.204 | -0.037 | 0.444 | 0.114 | 0.500 | 0.370 | 0.630 | tested | 0.000 |
| llama-3.1-8b | housing | gender | female | clear | 36 | 6 | 0.778 | 0.250 | 1.445 |  | 0.500 | 0.306 | 0.722 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.247 | 0.062 | 0.432 | 0.011 | 0.494 | 0.389 | 0.605 | tested | 0.000 |
| llama-3.1-8b | housing | origin | any_minority | clear | 108 | 6 | 0.204 | -0.204 | 0.574 |  | 0.481 | 0.389 | 0.565 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.259 | 0.111 | 0.407 | 0.002 | 0.444 | 0.352 | 0.537 | tested | 0.000 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 36 | 6 | 0.111 | -0.167 | 0.417 |  | 0.472 | 0.417 | 0.500 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 54 | 9 | 0.241 | -0.111 | 0.556 | 0.172 | 0.611 | 0.481 | 0.741 | tested | 0.000 |
| llama-3.1-8b | housing | origin | romanian | clear | 36 | 6 | -0.111 | -0.639 | 0.389 |  | 0.444 | 0.306 | 0.583 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 54 | 9 | 0.241 | 0.037 | 0.463 | 0.031 | 0.426 | 0.259 | 0.593 | tested | 0.000 |
| llama-3.1-8b | housing | origin | syrian | clear | 36 | 6 | 0.611 | 0.000 | 1.139 |  | 0.528 | 0.389 | 0.639 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.815 | 0.574 | 1.037 | 0.000 | 0.519 | 0.389 | 0.648 | tested | 0.000 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 36 | 6 | 0.861 | 0.444 | 1.417 |  | 0.694 | 0.472 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -1.222 | -1.648 | -0.777 | 0.000 | 0.722 | 0.574 | 0.870 | tested | 0.019 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 36 | 6 | -1.639 | -2.000 | -1.194 |  | 0.750 | 0.667 | 0.861 | descriptive (fewer than 8 cases) | 0.111 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 16 | 3 | 4.766 | -0.830 | 7.357 |  | 0.312 | 0.000 | 0.600 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 12 | 2 | 4.833 | 3.667 | 6.000 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 41 | 9 | 0.793 | -1.883 | 3.081 | 0.529 | 0.488 | 0.366 | 0.610 | tested |  |
| llama-3.1-8b | relief | area | social_housing | clear | 36 | 6 | 0.845 | -1.754 | 3.099 |  | 0.528 | 0.444 | 0.611 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 44 | 9 | -2.021 | -3.813 | -0.300 | 0.014 | 0.636 | 0.489 | 0.791 | tested |  |
| llama-3.1-8b | relief | area | villas | clear | 36 | 6 | -1.793 | -3.465 | 0.000 |  | 0.500 | 0.361 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 132 | 9 | 3.513 | 1.467 | 5.461 | 0.001 | 0.561 | 0.474 | 0.648 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 108 | 6 | 3.114 | -0.178 | 5.907 |  | 0.602 | 0.481 | 0.704 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 45 | 9 | 1.951 | -0.213 | 3.985 | 0.068 | 0.489 | 0.326 | 0.640 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 36 | 6 | 2.485 | -0.959 | 5.328 |  | 0.639 | 0.472 | 0.806 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 42 | 9 | 1.360 | -1.172 | 3.750 | 0.317 | 0.500 | 0.351 | 0.650 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 36 | 6 | 2.402 | -0.207 | 4.652 |  | 0.611 | 0.472 | 0.722 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 45 | 9 | 7.085 | 4.293 | 10.046 | 0.000 | 0.689 | 0.592 | 0.787 | tested |  |
| llama-3.1-8b | relief | origin | syrian | clear | 36 | 6 | 4.457 | 0.699 | 8.018 |  | 0.556 | 0.417 | 0.694 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 151 | 9 | 0.219 | 0.071 | 0.390 | 0.002 | 0.232 | 0.134 | 0.322 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 99 | 6 | 0.131 | 0.010 | 0.333 |  | 0.071 | 0.010 | 0.168 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 50 | 9 | 0.180 | 0.041 | 0.320 | 0.012 | 0.240 | 0.130 | 0.346 | tested |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 32 | 6 | 0.062 | 0.000 | 0.194 |  | 0.031 | 0.000 | 0.097 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 51 | 9 | 0.235 | 0.019 | 0.500 | 0.048 | 0.216 | 0.098 | 0.327 | tested |  |
| llama-3.1-8b | triage | origin | romanian | clear | 34 | 6 | 0.118 | 0.000 | 0.353 |  | 0.059 | 0.000 | 0.176 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 50 | 9 | 0.240 | 0.056 | 0.478 | 0.015 | 0.240 | 0.118 | 0.362 | tested |  |
| llama-3.1-8b | triage | origin | syrian | clear | 33 | 6 | 0.212 | 0.029 | 0.469 |  | 0.121 | 0.029 | 0.250 | descriptive (fewer than 8 cases) |  |
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
| meltemi-7b | housing | gender | female | clear | 36 | 6 | -0.056 | -0.250 | 0.194 |  | 0.389 | 0.194 | 0.583 | descriptive (fewer than 8 cases) | 0.000 |
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
| meltemi-7b | relief | area | social_housing | ambiguous | 43 | 9 | 1.158 | -0.574 | 2.592 | 0.156 | 0.372 | 0.279 | 0.475 | tested |  |
| meltemi-7b | relief | area | social_housing | clear | 29 | 6 | 0.079 | -3.091 | 3.158 |  | 0.483 | 0.346 | 0.594 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | area | villas | ambiguous | 43 | 9 | 2.822 | 0.858 | 4.664 | 0.004 | 0.326 | 0.238 | 0.429 | tested |  |
| meltemi-7b | relief | area | villas | clear | 29 | 6 | -1.141 | -4.533 | 3.162 |  | 0.552 | 0.464 | 0.645 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | any_minority | ambiguous | 134 | 9 | 0.728 | -0.821 | 1.908 | 0.312 | 0.358 | 0.226 | 0.500 | tested |  |
| meltemi-7b | relief | origin | any_minority | clear | 88 | 6 | -1.378 | -2.879 | 0.118 |  | 0.557 | 0.405 | 0.656 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | local_migrant | ambiguous | 44 | 9 | 0.805 | -1.130 | 2.569 | 0.411 | 0.386 | 0.244 | 0.545 | tested |  |
| meltemi-7b | relief | origin | local_migrant | clear | 31 | 6 | -3.254 | -5.868 | -0.385 |  | 0.581 | 0.437 | 0.710 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | romanian | ambiguous | 45 | 9 | 0.705 | -0.704 | 2.108 | 0.315 | 0.267 | 0.122 | 0.419 | tested |  |
| meltemi-7b | relief | origin | romanian | clear | 29 | 6 | -2.176 | -4.160 | -0.294 |  | 0.448 | 0.240 | 0.621 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | relief | origin | syrian | ambiguous | 45 | 9 | 0.676 | -1.101 | 2.054 | 0.419 | 0.422 | 0.255 | 0.617 | tested |  |
| meltemi-7b | relief | origin | syrian | clear | 28 | 6 | 1.524 | -0.844 | 3.584 |  | 0.643 | 0.500 | 0.758 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | any_minority | ambiguous | 162 | 9 | 0.086 | -0.161 | 0.370 | 0.579 | 0.327 | 0.235 | 0.426 | tested |  |
| meltemi-7b | triage | origin | any_minority | clear | 108 | 6 | 0.222 | 0.065 | 0.389 |  | 0.194 | 0.093 | 0.315 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | local_migrant | ambiguous | 54 | 9 | 0.111 | -0.222 | 0.500 | 0.616 | 0.352 | 0.222 | 0.481 | tested |  |
| meltemi-7b | triage | origin | local_migrant | clear | 36 | 6 | 0.222 | 0.028 | 0.389 |  | 0.194 | 0.083 | 0.333 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | romanian | ambiguous | 54 | 9 | -0.074 | -0.370 | 0.223 | 0.660 | 0.352 | 0.222 | 0.481 | tested |  |
| meltemi-7b | triage | origin | romanian | clear | 36 | 6 | 0.194 | 0.028 | 0.417 |  | 0.194 | 0.056 | 0.306 | descriptive (fewer than 8 cases) |  |
| meltemi-7b | triage | origin | syrian | ambiguous | 54 | 9 | 0.222 | -0.074 | 0.481 | 0.132 | 0.278 | 0.185 | 0.370 | tested |  |
| meltemi-7b | triage | origin | syrian | clear | 36 | 6 | 0.250 | 0.056 | 0.472 |  | 0.194 | 0.056 | 0.333 | descriptive (fewer than 8 cases) |  |
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
| qwen2.5-7b | evacuation | area | social_housing | clear | 36 | 6 | 0.111 | 0.028 | 0.222 |  | 0.139 | 0.028 | 0.306 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | area | villas | ambiguous | 54 | 9 | -0.537 | -0.722 | -0.352 | 0.000 | 0.574 | 0.481 | 0.685 | tested |  |
| qwen2.5-7b | evacuation | area | villas | clear | 36 | 6 | -0.139 | -0.222 | -0.056 |  | 0.306 | 0.139 | 0.500 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | any_minority | ambiguous | 162 | 9 | 0.315 | 0.160 | 0.494 | 0.000 | 0.389 | 0.259 | 0.519 | tested |  |
| qwen2.5-7b | evacuation | origin | any_minority | clear | 108 | 6 | 0.139 | 0.019 | 0.324 |  | 0.130 | 0.074 | 0.213 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | local_migrant | ambiguous | 54 | 9 | 0.037 | -0.148 | 0.241 | 0.786 | 0.278 | 0.148 | 0.407 | tested |  |
| qwen2.5-7b | evacuation | origin | local_migrant | clear | 36 | 6 | 0.056 | 0.000 | 0.167 |  | 0.028 | 0.000 | 0.083 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | romanian | ambiguous | 54 | 9 | -0.037 | -0.222 | 0.185 | 0.761 | 0.278 | 0.093 | 0.463 | tested |  |
| qwen2.5-7b | evacuation | origin | romanian | clear | 36 | 6 | 0.000 | -0.167 | 0.167 |  | 0.056 | 0.000 | 0.111 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | evacuation | origin | syrian | ambiguous | 54 | 9 | 0.944 | 0.667 | 1.204 | 0.000 | 0.611 | 0.463 | 0.741 | tested |  |
| qwen2.5-7b | evacuation | origin | syrian | clear | 36 | 6 | 0.361 | 0.194 | 0.639 |  | 0.306 | 0.194 | 0.472 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.556 | 0.333 | 0.667 |  | 0.333 | 0.333 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | roma_settlement | clear | 12 | 2 | 0.083 | 0.000 | 0.167 |  | 0.250 | 0.167 | 0.333 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | social_housing | ambiguous | 54 | 9 | 0.093 | 0.000 | 0.185 | 0.058 | 0.130 | 0.037 | 0.222 | tested | 0.000 |
| qwen2.5-7b | housing | area | social_housing | clear | 36 | 6 | 0.111 | -0.028 | 0.278 |  | 0.167 | 0.056 | 0.306 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | area | villas | ambiguous | 54 | 9 | -0.037 | -0.130 | 0.037 | 0.536 | 0.056 | 0.018 | 0.111 | tested | 0.000 |
| qwen2.5-7b | housing | area | villas | clear | 36 | 6 | -0.306 | -0.500 | -0.111 |  | 0.222 | 0.083 | 0.361 | descriptive (fewer than 8 cases) | 0.056 |
| qwen2.5-7b | housing | gender | female | ambiguous | 54 | 9 | 0.093 | 0.000 | 0.185 | 0.054 | 0.093 | 0.000 | 0.185 | tested | 0.000 |
| qwen2.5-7b | housing | gender | female | clear | 36 | 6 | 0.056 | -0.056 | 0.194 |  | 0.111 | 0.028 | 0.222 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.025 | -0.037 | 0.093 | 0.532 | 0.099 | 0.049 | 0.148 | tested | 0.000 |
| qwen2.5-7b | housing | origin | any_minority | clear | 108 | 6 | 0.065 | 0.009 | 0.120 |  | 0.083 | 0.028 | 0.139 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.074 | -0.019 | 0.185 | 0.200 | 0.148 | 0.056 | 0.241 | tested | 0.000 |
| qwen2.5-7b | housing | origin | local_migrant | clear | 36 | 6 | 0.056 | 0.000 | 0.111 |  | 0.056 | 0.000 | 0.111 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | romanian | ambiguous | 54 | 9 | 0.056 | 0.018 | 0.111 | 0.050 | 0.056 | 0.000 | 0.111 | tested | 0.000 |
| qwen2.5-7b | housing | origin | romanian | clear | 36 | 6 | 0.028 | 0.000 | 0.083 |  | 0.083 | 0.000 | 0.194 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | origin | syrian | ambiguous | 54 | 9 | -0.056 | -0.130 | 0.019 | 0.208 | 0.093 | 0.037 | 0.148 | tested | 0.000 |
| qwen2.5-7b | housing | origin | syrian | clear | 36 | 6 | 0.111 | 0.028 | 0.222 |  | 0.111 | 0.028 | 0.222 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.148 | 0.055 | 0.259 | 0.010 | 0.185 | 0.129 | 0.278 | tested | 0.000 |
| qwen2.5-7b | housing | status | asylum_seeker | clear | 36 | 6 | 0.056 | -0.111 | 0.194 |  | 0.194 | 0.111 | 0.278 | descriptive (fewer than 8 cases) | 0.000 |
| qwen2.5-7b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -0.481 | -0.722 | -0.241 | 0.000 | 0.333 | 0.185 | 0.481 | tested | 0.093 |
| qwen2.5-7b | housing | status | seasonal_worker | clear | 36 | 6 | -0.444 | -0.722 | -0.139 |  | 0.333 | 0.111 | 0.556 | descriptive (fewer than 8 cases) | 0.028 |
| qwen2.5-7b | relief | area | roma_settlement | ambiguous | 18 | 3 | 3.611 | 2.500 | 5.833 |  | 0.556 | 0.333 | 0.833 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | roma_settlement | clear | 12 | 2 | 1.250 | -0.833 | 3.333 |  | 0.250 | 0.167 | 0.333 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | social_housing | ambiguous | 54 | 9 | 0.185 | -0.836 | 1.111 | 0.779 | 0.278 | 0.111 | 0.500 | tested |  |
| qwen2.5-7b | relief | area | social_housing | clear | 36 | 6 | 0.278 | -1.389 | 1.944 |  | 0.417 | 0.278 | 0.556 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | area | villas | ambiguous | 54 | 9 | -2.037 | -3.333 | -1.111 | 0.000 | 0.389 | 0.259 | 0.519 | tested |  |
| qwen2.5-7b | relief | area | villas | clear | 36 | 6 | -3.056 | -5.417 | -1.111 |  | 0.389 | 0.222 | 0.556 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | any_minority | ambiguous | 162 | 9 | 1.790 | 1.235 | 2.285 | 0.000 | 0.438 | 0.346 | 0.543 | tested |  |
| qwen2.5-7b | relief | origin | any_minority | clear | 108 | 6 | 0.000 | -1.204 | 1.343 |  | 0.472 | 0.333 | 0.593 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | local_migrant | ambiguous | 54 | 9 | 0.185 | -0.556 | 0.926 | 0.764 | 0.333 | 0.204 | 0.444 | tested |  |
| qwen2.5-7b | relief | origin | local_migrant | clear | 36 | 6 | -1.250 | -2.639 | 0.000 |  | 0.389 | 0.278 | 0.472 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | romanian | ambiguous | 54 | 9 | -0.093 | -0.741 | 0.648 | 0.862 | 0.296 | 0.185 | 0.426 | tested |  |
| qwen2.5-7b | relief | origin | romanian | clear | 36 | 6 | -1.389 | -1.944 | -0.694 |  | 0.444 | 0.222 | 0.639 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | relief | origin | syrian | ambiguous | 54 | 9 | 5.278 | 4.074 | 6.574 | 0.000 | 0.685 | 0.537 | 0.833 | tested |  |
| qwen2.5-7b | relief | origin | syrian | clear | 36 | 6 | 2.639 | 0.278 | 5.417 |  | 0.583 | 0.361 | 0.778 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | any_minority | ambiguous | 159 | 9 | 0.233 | 0.113 | 0.353 | 0.001 | 0.239 | 0.150 | 0.321 | tested |  |
| qwen2.5-7b | triage | origin | any_minority | clear | 108 | 6 | 0.019 | -0.065 | 0.102 |  | 0.148 | 0.037 | 0.259 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | local_migrant | ambiguous | 53 | 9 | 0.189 | 0.094 | 0.288 | 0.000 | 0.170 | 0.093 | 0.255 | tested |  |
| qwen2.5-7b | triage | origin | local_migrant | clear | 36 | 6 | -0.083 | -0.194 | 0.000 |  | 0.083 | 0.000 | 0.194 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | romanian | ambiguous | 53 | 9 | 0.132 | 0.019 | 0.255 | 0.035 | 0.208 | 0.093 | 0.340 | tested |  |
| qwen2.5-7b | triage | origin | romanian | clear | 36 | 6 | 0.028 | -0.056 | 0.111 |  | 0.167 | 0.056 | 0.278 | descriptive (fewer than 8 cases) |  |
| qwen2.5-7b | triage | origin | syrian | ambiguous | 53 | 9 | 0.377 | 0.185 | 0.547 | 0.000 | 0.340 | 0.211 | 0.453 | tested |  |
| qwen2.5-7b | triage | origin | syrian | clear | 36 | 6 | 0.111 | -0.028 | 0.250 |  | 0.194 | 0.056 | 0.333 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | el | 1960 | 0.968 | 0.028 | not-a-permutation 63 |
| apertus-8b | en | 1960 | 0.990 | 0.026 | not-a-permutation 20 |
| apertus-8b | fr | 1960 | 0.929 | 0.023 | not-a-permutation 138, bad-shares 1 |
| krikri-8b | el | 1960 | 0.994 | 0.012 | bad-shares 11, no-json 1 |
| krikri-8b | en | 1960 | 0.997 | 0.001 | bad-shares 6 |
| krikri-8b | fr | 1960 | 0.982 | 0.007 | not-a-permutation 22, bad-shares 13 |
| llama-3.1-8b | el | 1960 | 0.959 | 0.007 | not-a-permutation 81 |
| llama-3.1-8b | en | 1960 | 0.959 | 0.032 | not-a-permutation 54, bad-shares 21, no-json 5 |
| llama-3.1-8b | fr | 1960 | 0.958 | 0.014 | not-a-permutation 56, bad-shares 25, no-json 1 |
| meltemi-7b | el | 1960 | 0.993 | 0.172 | no-json 9, not-a-permutation 3, shares-do-not-sum-to-100 1 |
| meltemi-7b | en | 1960 | 0.999 | 0.120 | shares-do-not-sum-to-100 2 |
| meltemi-7b | fr | 1960 | 0.928 | 0.078 | shares-do-not-sum-to-100 142 |
| qwen2.5-7b | el | 1960 | 0.999 | 0.000 | not-a-permutation 2 |
| qwen2.5-7b | en | 1960 | 0.989 | 0.000 | not-a-permutation 22 |
| qwen2.5-7b | fr | 1960 | 0.998 | 0.000 | not-a-permutation 3 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | area=roma_settlement | 0.900 | 0.956 | 0.056 |
| apertus-8b | dispatch | need=pregnant | 0.911 | 0.956 | 0.044 |
| apertus-8b | dispatch | need=dialysis | 0.944 | 0.956 | 0.011 |
| apertus-8b | dispatch | need=wheelchair | 0.944 | 0.956 | 0.011 |
| apertus-8b | dispatch | origin=syrian | 0.944 | 0.956 | 0.011 |
| apertus-8b | dispatch | need=infant | 0.956 | 0.956 | 0.000 |
| apertus-8b | dispatch | placebo | 0.956 | 0.956 | 0.000 |
| apertus-8b | dispatch | status=asylum_seeker | 0.956 | 0.956 | 0.000 |
| apertus-8b | dispatch | area=social_housing | 0.967 | 0.956 | -0.011 |
| apertus-8b | dispatch | area=villas | 0.967 | 0.956 | -0.011 |
| apertus-8b | dispatch | need=age80 | 0.978 | 0.956 | -0.022 |
| apertus-8b | dispatch | status=seasonal_worker | 0.978 | 0.956 | -0.022 |
| apertus-8b | dispatch | gender=female | 0.989 | 0.956 | -0.033 |
| apertus-8b | dispatch | origin=romanian | 0.989 | 0.956 | -0.033 |
| apertus-8b | dispatch | origin=local_migrant | 1.000 | 0.956 | -0.044 |
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
| apertus-8b | relief | need=age80 | 0.989 | 1.000 | 0.011 |
| apertus-8b | relief | area=roma_settlement | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | area=social_housing | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | area=villas | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=dialysis | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=infant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=pregnant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | need=wheelchair | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=local_migrant | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=romanian | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | origin=syrian | 1.000 | 1.000 | 0.000 |
| apertus-8b | relief | placebo | 1.000 | 1.000 | 0.000 |
| apertus-8b | triage | need=pregnant | 0.778 | 0.789 | 0.011 |
| apertus-8b | triage | origin=local_migrant | 0.789 | 0.789 | 0.000 |
| apertus-8b | triage | placebo | 0.800 | 0.789 | -0.011 |
| apertus-8b | triage | need=wheelchair | 0.811 | 0.789 | -0.022 |
| apertus-8b | triage | need=age80 | 0.822 | 0.789 | -0.033 |
| apertus-8b | triage | origin=romanian | 0.822 | 0.789 | -0.033 |
| apertus-8b | triage | origin=syrian | 0.822 | 0.789 | -0.033 |
| apertus-8b | triage | need=dialysis | 0.844 | 0.789 | -0.056 |
| apertus-8b | triage | need=infant | 0.867 | 0.789 | -0.078 |
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
| llama-3.1-8b | dispatch | area=roma_settlement | 0.867 | 0.900 | 0.033 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.867 | 0.900 | 0.033 |
| llama-3.1-8b | dispatch | origin=syrian | 0.878 | 0.900 | 0.022 |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.878 | 0.900 | 0.022 |
| llama-3.1-8b | dispatch | area=villas | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | need=age80 | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.900 | 0.900 | 0.000 |
| llama-3.1-8b | dispatch | need=dialysis | 0.911 | 0.900 | -0.011 |
| llama-3.1-8b | dispatch | gender=female | 0.922 | 0.900 | -0.022 |
| llama-3.1-8b | dispatch | need=pregnant | 0.922 | 0.900 | -0.022 |
| llama-3.1-8b | dispatch | placebo | 0.922 | 0.900 | -0.022 |
| llama-3.1-8b | dispatch | area=social_housing | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | dispatch | need=infant | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | dispatch | origin=romanian | 0.944 | 0.900 | -0.044 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.956 | 0.900 | -0.056 |
| llama-3.1-8b | evacuation | area=social_housing | 0.956 | 0.978 | 0.022 |
| llama-3.1-8b | evacuation | need=infant | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.967 | 0.978 | 0.011 |
| llama-3.1-8b | evacuation | area=villas | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | evacuation | need=pregnant | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | evacuation | placebo | 0.978 | 0.978 | 0.000 |
| llama-3.1-8b | evacuation | need=age80 | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | need=wheelchair | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | origin=romanian | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | origin=syrian | 0.989 | 0.978 | -0.011 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.978 | -0.022 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.978 | -0.022 |
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
| llama-3.1-8b | relief | placebo | 0.911 | 0.911 | 0.000 |
| llama-3.1-8b | relief | area=social_housing | 0.922 | 0.911 | -0.011 |
| llama-3.1-8b | relief | origin=romanian | 0.933 | 0.911 | -0.022 |
| llama-3.1-8b | relief | area=villas | 0.944 | 0.911 | -0.033 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.911 | -0.056 |
| llama-3.1-8b | relief | need=dialysis | 0.967 | 0.911 | -0.056 |
| llama-3.1-8b | relief | need=wheelchair | 0.967 | 0.911 | -0.056 |
| llama-3.1-8b | relief | need=pregnant | 0.978 | 0.911 | -0.067 |
| llama-3.1-8b | relief | need=age80 | 0.989 | 0.911 | -0.078 |
| llama-3.1-8b | relief | origin=local_migrant | 0.989 | 0.911 | -0.078 |
| llama-3.1-8b | relief | origin=syrian | 0.989 | 0.911 | -0.078 |
| llama-3.1-8b | relief | need=infant | 1.000 | 0.911 | -0.089 |
| llama-3.1-8b | triage | placebo | 0.911 | 0.967 | 0.056 |
| llama-3.1-8b | triage | need=dialysis | 0.922 | 0.967 | 0.044 |
| llama-3.1-8b | triage | origin=local_migrant | 0.933 | 0.967 | 0.033 |
| llama-3.1-8b | triage | origin=syrian | 0.933 | 0.967 | 0.033 |
| llama-3.1-8b | triage | need=infant | 0.944 | 0.967 | 0.022 |
| llama-3.1-8b | triage | need=wheelchair | 0.944 | 0.967 | 0.022 |
| llama-3.1-8b | triage | need=age80 | 0.956 | 0.967 | 0.011 |
| llama-3.1-8b | triage | origin=romanian | 0.956 | 0.967 | 0.011 |
| llama-3.1-8b | triage | need=pregnant | 0.967 | 0.967 | 0.000 |
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
| meltemi-7b | relief | area=roma_settlement | 0.767 | 0.856 | 0.089 |
| meltemi-7b | relief | need=pregnant | 0.800 | 0.856 | 0.056 |
| meltemi-7b | relief | need=dialysis | 0.811 | 0.856 | 0.044 |
| meltemi-7b | relief | need=wheelchair | 0.833 | 0.856 | 0.022 |
| meltemi-7b | relief | need=age80 | 0.856 | 0.856 | 0.000 |
| meltemi-7b | relief | area=social_housing | 0.867 | 0.856 | -0.011 |
| meltemi-7b | relief | need=infant | 0.878 | 0.856 | -0.022 |
| meltemi-7b | relief | area=villas | 0.889 | 0.856 | -0.033 |
| meltemi-7b | relief | origin=romanian | 0.889 | 0.856 | -0.033 |
| meltemi-7b | relief | origin=syrian | 0.889 | 0.856 | -0.033 |
| meltemi-7b | relief | origin=local_migrant | 0.900 | 0.856 | -0.044 |
| meltemi-7b | relief | placebo | 0.900 | 0.856 | -0.044 |
| meltemi-7b | triage | need=infant | 0.989 | 1.000 | 0.011 |
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
| qwen2.5-7b | triage | need=pregnant | 0.978 | 1.000 | 0.022 |
| qwen2.5-7b | triage | placebo | 0.978 | 1.000 | 0.022 |
| qwen2.5-7b | triage | need=dialysis | 0.989 | 1.000 | 0.011 |
| qwen2.5-7b | triage | need=wheelchair | 0.989 | 1.000 | 0.011 |
| qwen2.5-7b | triage | origin=local_migrant | 0.989 | 1.000 | 0.011 |
| qwen2.5-7b | triage | origin=romanian | 0.989 | 1.000 | 0.011 |
| qwen2.5-7b | triage | origin=syrian | 0.989 | 1.000 | 0.011 |
| qwen2.5-7b | triage | need=age80 | 1.000 | 1.000 | 0.000 |
| qwen2.5-7b | triage | need=infant | 1.000 | 1.000 | 0.000 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| apertus-8b | dispatch | Intercept | 0.482 | 0.418 | 0.249 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing] | 0.033 | 0.461 | 0.944 |  |
| apertus-8b | dispatch | C(key)[T.area=villas] | -0.599 | 0.465 | 0.198 |  |
| apertus-8b | dispatch | C(key)[T.gender=female] | -0.039 | 0.461 | 0.933 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant] | -0.325 | 0.461 | 0.481 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian] | -0.325 | 0.461 | 0.481 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian] | -0.075 | 0.461 | 0.871 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker] | -0.231 | 0.465 | 0.619 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker] | 0.029 | 0.463 | 0.949 |  |
| apertus-8b | dispatch | C(language)[T.en] | 1.012 | 0.549 | 0.065 |  |
| apertus-8b | dispatch | C(language)[T.fr] | 0.771 | 0.580 | 0.184 |  |
| apertus-8b | dispatch | C(clarity)[T.clear] | -0.321 | 0.197 | 0.104 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -1.054 | 0.633 | 0.096 |  |
| apertus-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -1.458 | 0.636 | 0.022 |  |
| apertus-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -1.130 | 0.635 | 0.075 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.008 | 0.633 | 0.112 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -1.068 | 0.635 | 0.092 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -1.292 | 0.633 | 0.041 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.135 | 0.636 | 0.832 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -1.672 | 0.635 | 0.008 |  |
| apertus-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.245 | 0.665 | 0.061 |  |
| apertus-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -1.182 | 0.665 | 0.075 |  |
| apertus-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.846 | 0.661 | 0.200 |  |
| apertus-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.629 | 0.661 | 0.341 |  |
| apertus-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.802 | 0.661 | 0.225 |  |
| apertus-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.119 | 0.667 | 0.093 |  |
| apertus-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.257 | 0.665 | 0.699 |  |
| apertus-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.305 | 0.663 | 0.049 |  |
| apertus-8b | evacuation | Intercept | 1.020 | 0.363 | 0.005 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing] | 0.268 | 0.402 | 0.505 |  |
| apertus-8b | evacuation | C(key)[T.area=villas] | -1.299 | 0.402 | 0.001 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant] | -0.565 | 0.402 | 0.160 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian] | -0.832 | 0.402 | 0.039 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian] | 0.001 | 0.402 | 0.997 |  |
| apertus-8b | evacuation | C(language)[T.en] | 0.300 | 0.486 | 0.537 |  |
| apertus-8b | evacuation | C(language)[T.fr] | 0.100 | 0.486 | 0.837 |  |
| apertus-8b | evacuation | C(clarity)[T.clear] | -0.220 | 0.171 | 0.198 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.333 | 0.562 | 0.553 |  |
| apertus-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.367 | 0.562 | 0.514 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.633 | 0.562 | 0.259 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.667 | 0.562 | 0.235 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.133 | 0.562 | 0.812 |  |
| apertus-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.167 | 0.562 | 0.038 |  |
| apertus-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.133 | 0.562 | 0.812 |  |
| apertus-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.633 | 0.562 | 0.259 |  |
| apertus-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.367 | 0.562 | 0.514 |  |
| apertus-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.533 | 0.562 | 0.342 |  |
| apertus-8b | housing | Intercept | 0.334 | 0.223 | 0.134 |  |
| apertus-8b | housing | C(key)[T.area=social_housing] | -0.129 | 0.250 | 0.607 |  |
| apertus-8b | housing | C(key)[T.area=villas] | -0.329 | 0.250 | 0.189 |  |
| apertus-8b | housing | C(key)[T.gender=female] | -0.062 | 0.250 | 0.804 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant] | -0.296 | 0.250 | 0.238 |  |
| apertus-8b | housing | C(key)[T.origin=romanian] | -0.162 | 0.250 | 0.517 |  |
| apertus-8b | housing | C(key)[T.origin=syrian] | -0.196 | 0.250 | 0.435 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker] | -0.062 | 0.250 | 0.804 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker] | -0.996 | 0.250 | 0.000 |  |
| apertus-8b | housing | C(language)[T.en] | 0.100 | 0.304 | 0.742 |  |
| apertus-8b | housing | C(language)[T.fr] | 1.400 | 0.304 | 0.000 |  |
| apertus-8b | housing | C(clarity)[T.clear] | -0.014 | 0.088 | 0.874 |  |
| apertus-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.167 | 0.351 | 0.635 |  |
| apertus-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.500 | 0.351 | 0.154 |  |
| apertus-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.233 | 0.351 | 0.506 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.133 | 0.351 | 0.704 |  |
| apertus-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | 0.033 | 0.351 | 0.924 |  |
| apertus-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.100 | 0.351 | 0.776 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.167 | 0.351 | 0.635 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 0.533 | 0.351 | 0.129 |  |
| apertus-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.300 | 0.351 | 0.000 |  |
| apertus-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.700 | 0.351 | 0.000 |  |
| apertus-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -1.000 | 0.351 | 0.004 |  |
| apertus-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.100 | 0.351 | 0.002 |  |
| apertus-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.400 | 0.351 | 0.000 |  |
| apertus-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.900 | 0.351 | 0.010 |  |
| apertus-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.733 | 0.351 | 0.037 |  |
| apertus-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.733 | 0.351 | 0.037 |  |
| apertus-8b | relief | Intercept | -0.801 | 2.557 | 0.754 |  |
| apertus-8b | relief | C(key)[T.area=social_housing] | 2.322 | 2.733 | 0.396 |  |
| apertus-8b | relief | C(key)[T.area=villas] | 0.039 | 2.733 | 0.989 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant] | -0.209 | 2.733 | 0.939 |  |
| apertus-8b | relief | C(key)[T.origin=romanian] | 1.761 | 2.733 | 0.519 |  |
| apertus-8b | relief | C(key)[T.origin=syrian] | 1.200 | 2.733 | 0.661 |  |
| apertus-8b | relief | C(language)[T.en] | 1.727 | 3.294 | 0.600 |  |
| apertus-8b | relief | C(language)[T.fr] | 1.152 | 3.294 | 0.727 |  |
| apertus-8b | relief | C(clarity)[T.clear] | 0.187 | 1.571 | 0.905 |  |
| apertus-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -2.125 | 3.803 | 0.576 |  |
| apertus-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | -1.874 | 3.803 | 0.622 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | 0.056 | 3.803 | 0.988 |  |
| apertus-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -2.264 | 3.803 | 0.552 |  |
| apertus-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -0.960 | 3.803 | 0.801 |  |
| apertus-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.852 | 3.803 | 0.311 |  |
| apertus-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -1.554 | 3.803 | 0.683 |  |
| apertus-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -3.170 | 3.803 | 0.405 |  |
| apertus-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -3.215 | 3.803 | 0.398 |  |
| apertus-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.731 | 3.803 | 0.649 |  |
| apertus-8b | triage | Intercept | 0.408 | 0.261 | 0.118 |  |
| apertus-8b | triage | C(key)[T.origin=romanian] | 0.103 | 0.279 | 0.713 |  |
| apertus-8b | triage | C(key)[T.origin=syrian] | -0.048 | 0.289 | 0.869 |  |
| apertus-8b | triage | C(language)[T.en] | -0.089 | 0.271 | 0.743 |  |
| apertus-8b | triage | C(language)[T.fr] | -0.391 | 0.323 | 0.227 |  |
| apertus-8b | triage | C(clarity)[T.clear] | -0.178 | 0.278 | 0.522 |  |
| apertus-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.009 | 0.377 | 0.981 |  |
| apertus-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.212 | 0.384 | 0.582 |  |
| apertus-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.386 | 0.446 | 0.387 |  |
| apertus-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.300 | 0.443 | 0.498 |  |
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
| krikri-8b | housing | C(language)[T.fr] | -0.000 | 0.232 | 1.000 |  |
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
| krikri-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.000 | 0.268 | 1.000 |  |
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
| llama-3.1-8b | dispatch | Intercept | -0.990 | 0.360 | 0.006 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.646 | 0.375 | 0.085 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | 0.311 | 0.375 | 0.407 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.689 | 0.374 | 0.065 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.653 | 0.374 | 0.081 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.760 | 0.374 | 0.042 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.802 | 0.377 | 0.033 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | 0.773 | 0.378 | 0.041 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | 0.546 | 0.374 | 0.144 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(language)[T.en] | 1.491 | 0.434 | 0.001 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 1.215 | 0.445 | 0.006 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.141 | 0.197 | 0.475 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -1.326 | 0.491 | 0.007 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -1.395 | 0.489 | 0.004 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -1.106 | 0.488 | 0.023 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -1.253 | 0.489 | 0.010 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -1.132 | 0.489 | 0.021 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -1.287 | 0.492 | 0.009 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.719 | 0.496 | 0.147 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -1.316 | 0.493 | 0.008 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.736 | 0.500 | 0.141 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -1.243 | 0.503 | 0.013 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | -0.858 | 0.499 | 0.086 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.762 | 0.502 | 0.129 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.941 | 0.498 | 0.059 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.078 | 0.503 | 0.032 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.908 | 0.502 | 0.071 | did not converge; read with care |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.223 | 0.499 | 0.014 | did not converge; read with care |
| llama-3.1-8b | evacuation | Intercept | 0.526 | 0.268 | 0.049 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.057 | 0.287 | 0.843 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -0.928 | 0.285 | 0.001 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.228 | 0.285 | 0.424 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | 0.029 | 0.283 | 0.919 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.369 | 0.284 | 0.194 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.100 | 0.340 | 0.769 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.400 | 0.340 | 0.239 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.206 | 0.180 | 0.253 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.230 | 0.397 | 0.562 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.039 | 0.396 | 0.922 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.049 | 0.396 | 0.902 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.271 | 0.394 | 0.491 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.404 | 0.395 | 0.306 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.151 | 0.397 | 0.704 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.249 | 0.395 | 0.529 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.449 | 0.395 | 0.256 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.639 | 0.393 | 0.104 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.546 | 0.394 | 0.166 |  |
| llama-3.1-8b | housing | Intercept | 0.112 | 0.491 | 0.820 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.145 | 0.554 | 0.794 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -2.111 | 0.554 | 0.000 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female] | -0.045 | 0.554 | 0.936 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | -0.045 | 0.554 | 0.936 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | 0.022 | 0.554 | 0.968 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.055 | 0.554 | 0.920 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.022 | 0.554 | 0.968 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.711 | 0.554 | 0.000 |  |
| llama-3.1-8b | housing | C(language)[T.en] | 0.300 | 0.674 | 0.656 |  |
| llama-3.1-8b | housing | C(language)[T.fr] | 2.300 | 0.674 | 0.001 |  |
| llama-3.1-8b | housing | C(clarity)[T.clear] | 0.082 | 0.179 | 0.645 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.300 | 0.778 | 0.700 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | 0.300 | 0.778 | 0.700 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.233 | 0.778 | 0.764 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.200 | 0.778 | 0.797 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.633 | 0.778 | 0.416 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.267 | 0.778 | 0.732 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.433 | 0.778 | 0.578 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.500 | 0.778 | 0.054 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.033 | 0.778 | 0.184 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -2.000 | 0.778 | 0.010 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -1.367 | 0.778 | 0.079 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -2.100 | 0.778 | 0.007 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -2.167 | 0.778 | 0.005 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.767 | 0.778 | 0.023 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.033 | 0.778 | 0.184 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.567 | 0.778 | 0.467 |  |
| llama-3.1-8b | relief | Intercept | 1.688 | 2.756 | 0.540 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | -0.544 | 2.960 | 0.854 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -4.241 | 2.960 | 0.152 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 0.892 | 2.960 | 0.763 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | -0.608 | 2.960 | 0.837 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 5.859 | 2.960 | 0.048 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 2.760 | 3.672 | 0.452 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 4.934 | 3.672 | 0.179 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | -0.177 | 1.662 | 0.915 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -5.373 | 4.275 | 0.209 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | -0.726 | 4.262 | 0.865 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -2.545 | 4.239 | 0.548 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -0.893 | 4.262 | 0.834 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -5.206 | 4.239 | 0.219 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.106 | 4.290 | 0.469 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -4.632 | 4.263 | 0.277 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -6.171 | 4.276 | 0.149 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -4.050 | 4.290 | 0.345 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -7.306 | 4.276 | 0.088 |  |
| llama-3.1-8b | triage | Intercept | 0.103 | 0.158 | 0.514 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | 0.188 | 0.191 | 0.324 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | -0.037 | 0.193 | 0.848 |  |
| llama-3.1-8b | triage | C(language)[T.en] | 0.012 | 0.188 | 0.951 |  |
| llama-3.1-8b | triage | C(language)[T.fr] | 0.202 | 0.185 | 0.275 |  |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.097 | 0.140 | 0.488 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.233 | 0.262 | 0.372 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.144 | 0.264 | 0.585 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.155 | 0.258 | 0.549 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.237 | 0.260 | 0.361 |  |
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
| meltemi-7b | housing | Intercept | 0.041 | 0.289 | 0.887 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=social_housing] | 0.068 | 0.332 | 0.838 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=villas] | 0.035 | 0.332 | 0.917 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.gender=female] | 0.168 | 0.332 | 0.613 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=local_migrant] | 0.201 | 0.332 | 0.544 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=romanian] | 0.101 | 0.332 | 0.760 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=syrian] | 0.168 | 0.332 | 0.613 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker] | 0.101 | 0.332 | 0.760 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker] | 0.201 | 0.332 | 0.544 | did not converge; read with care |
| meltemi-7b | housing | C(language)[T.en] | 0.200 | 0.406 | 0.622 | did not converge; read with care |
| meltemi-7b | housing | C(language)[T.fr] | 0.700 | 0.406 | 0.084 | did not converge; read with care |
| meltemi-7b | housing | C(clarity)[T.clear] | -0.106 | 0.072 | 0.143 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.333 | 0.469 | 0.477 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.433 | 0.469 | 0.355 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.367 | 0.469 | 0.434 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.367 | 0.469 | 0.434 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.400 | 0.469 | 0.393 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.267 | 0.469 | 0.569 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | -0.100 | 0.469 | 0.831 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.367 | 0.469 | 0.434 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.867 | 0.469 | 0.064 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.133 | 0.469 | 0.016 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.967 | 0.469 | 0.039 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.100 | 0.469 | 0.019 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.867 | 0.469 | 0.064 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.633 | 0.469 | 0.176 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -0.800 | 0.469 | 0.088 | did not converge; read with care |
| meltemi-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.933 | 0.469 | 0.046 | did not converge; read with care |
| meltemi-7b | relief | Intercept | 1.213 | 2.472 | 0.624 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing] | -0.244 | 2.749 | 0.929 |  |
| meltemi-7b | relief | C(key)[T.area=villas] | 3.588 | 2.784 | 0.197 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant] | -2.360 | 2.749 | 0.391 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian] | -0.766 | 2.749 | 0.781 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian] | 2.023 | 2.763 | 0.464 |  |
| meltemi-7b | relief | C(language)[T.en] | -1.372 | 3.318 | 0.679 |  |
| meltemi-7b | relief | C(language)[T.fr] | -1.407 | 5.786 | 0.808 |  |
| meltemi-7b | relief | C(clarity)[T.clear] | -2.171 | 1.154 | 0.060 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | 1.104 | 3.831 | 0.773 |  |
| meltemi-7b | relief | C(key)[T.area=villas]:C(language)[T.en] | -2.982 | 3.849 | 0.439 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | 3.190 | 3.831 | 0.405 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | 1.031 | 3.831 | 0.788 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -2.681 | 3.839 | 0.485 |  |
| meltemi-7b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | 6.176 | 6.321 | 0.329 |  |
| meltemi-7b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -3.229 | 6.292 | 0.608 |  |
| meltemi-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | 3.870 | 6.249 | 0.536 |  |
| meltemi-7b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | 2.143 | 6.265 | 0.732 |  |
| meltemi-7b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | 3.014 | 6.278 | 0.631 |  |
| meltemi-7b | triage | Intercept | 0.179 | 0.193 | 0.355 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian] | -0.200 | 0.226 | 0.377 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian] | -0.100 | 0.226 | 0.658 |  |
| meltemi-7b | triage | C(language)[T.en] | 0.067 | 0.226 | 0.768 |  |
| meltemi-7b | triage | C(language)[T.fr] | -0.300 | 0.226 | 0.185 |  |
| meltemi-7b | triage | C(clarity)[T.clear] | 0.136 | 0.192 | 0.478 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.133 | 0.320 | 0.677 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | 0.033 | 0.320 | 0.917 |  |
| meltemi-7b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.367 | 0.320 | 0.252 |  |
| meltemi-7b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.500 | 0.320 | 0.118 |  |
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
| qwen2.5-7b | evacuation | Intercept | 0.242 | 0.262 | 0.357 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing] | -0.193 | 0.293 | 0.511 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas] | -0.326 | 0.293 | 0.266 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant] | -0.259 | 0.293 | 0.377 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian] | -0.326 | 0.293 | 0.266 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian] | 0.541 | 0.293 | 0.065 |  |
| qwen2.5-7b | evacuation | C(language)[T.en] | 1.000 | 0.356 | 0.005 |  |
| qwen2.5-7b | evacuation | C(language)[T.fr] | 1.000 | 0.356 | 0.005 |  |
| qwen2.5-7b | evacuation | C(clarity)[T.clear] | -0.123 | 0.114 | 0.282 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.767 | 0.411 | 0.062 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -1.300 | 0.411 | 0.002 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.833 | 0.411 | 0.042 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.800 | 0.411 | 0.051 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -1.200 | 0.411 | 0.003 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.600 | 0.411 | 0.144 |  |
| qwen2.5-7b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -1.433 | 0.411 | 0.000 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.833 | 0.411 | 0.042 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.867 | 0.411 | 0.035 |  |
| qwen2.5-7b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.867 | 0.411 | 0.035 |  |
| qwen2.5-7b | housing | Intercept | -0.122 | 0.136 | 0.372 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing] | 0.104 | 0.151 | 0.494 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas] | -0.030 | 0.151 | 0.844 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female] | 0.104 | 0.151 | 0.494 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant] | 0.137 | 0.151 | 0.366 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian] | 0.104 | 0.151 | 0.494 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian] | 0.170 | 0.151 | 0.261 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker] | 0.104 | 0.151 | 0.494 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker] | -0.096 | 0.151 | 0.524 |  |
| qwen2.5-7b | housing | C(language)[T.en] | 0.100 | 0.184 | 0.587 |  |
| qwen2.5-7b | housing | C(language)[T.fr] | 1.300 | 0.184 | 0.000 |  |
| qwen2.5-7b | housing | C(clarity)[T.clear] | -0.038 | 0.061 | 0.528 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | -0.000 | 0.212 | 1.000 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.200 | 0.212 | 0.346 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.000 | 0.212 | 1.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.067 | 0.212 | 0.754 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.067 | 0.212 | 0.754 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -0.067 | 0.212 | 0.754 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.233 | 0.212 | 0.272 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.467 | 0.212 | 0.028 |  |
| qwen2.5-7b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -1.000 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.133 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -1.067 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.133 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.100 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.400 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -1.200 | 0.212 | 0.000 |  |
| qwen2.5-7b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -1.633 | 0.212 | 0.000 |  |
| qwen2.5-7b | relief | Intercept | -0.555 | 1.307 | 0.671 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing] | -0.252 | 1.459 | 0.863 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas] | 0.915 | 1.459 | 0.531 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant] | -1.918 | 1.459 | 0.189 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian] | -1.418 | 1.459 | 0.331 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian] | 1.415 | 1.459 | 0.332 |  |
| qwen2.5-7b | relief | C(language)[T.en] | 4.000 | 1.764 | 0.023 |  |
| qwen2.5-7b | relief | C(language)[T.fr] | 8.500 | 1.764 | 0.000 |  |
| qwen2.5-7b | relief | C(clarity)[T.clear] | -1.316 | 0.572 | 0.021 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -2.167 | 2.037 | 0.288 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas]:C(language)[T.en] | -8.833 | 2.037 | 0.000 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.333 | 2.037 | 0.870 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -1.833 | 2.037 | 0.368 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | 1.333 | 2.037 | 0.513 |  |
| qwen2.5-7b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -5.667 | 2.037 | 0.005 |  |
| qwen2.5-7b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -10.500 | 2.037 | 0.000 |  |
| qwen2.5-7b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -4.333 | 2.037 | 0.033 |  |
| qwen2.5-7b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -5.000 | 2.037 | 0.014 |  |
| qwen2.5-7b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -2.167 | 2.037 | 0.288 |  |
| qwen2.5-7b | triage | Intercept | 0.020 | 0.116 | 0.862 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian] | -0.067 | 0.150 | 0.657 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian] | 0.167 | 0.150 | 0.267 |  |
| qwen2.5-7b | triage | C(language)[T.en] | 0.278 | 0.151 | 0.066 |  |
| qwen2.5-7b | triage | C(language)[T.fr] | 0.167 | 0.150 | 0.267 |  |
| qwen2.5-7b | triage | C(clarity)[T.clear] | -0.217 | 0.092 | 0.019 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.067 | 0.214 | 0.755 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.063 | 0.214 | 0.768 |  |
| qwen2.5-7b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | 0.167 | 0.212 | 0.432 |  |
| qwen2.5-7b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.133 | 0.212 | 0.530 |  |
