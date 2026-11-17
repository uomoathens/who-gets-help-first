# Analysis: replication-q8-pinned

Records: 5016; valid: 4823; counterfactual pairs: 3992.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | 79 | 15 | -0.114 | -0.276 | 0.076 | 0.238 | 0.215 | 0.122 | 0.312 | tested |  |
| llama-3.1-8b | evacuation | 70 | 14 | -0.071 | -0.215 | 0.045 | 0.371 | 0.143 | 0.055 | 0.267 | tested |  |
| llama-3.1-8b | housing | 73 | 15 | 0.055 | -0.395 | 0.468 | 0.770 | 0.562 | 0.443 | 0.667 | tested | 0.041 |
| llama-3.1-8b | relief | 54 | 14 | 0.646 | -0.954 | 2.179 | 0.442 | 0.426 | 0.286 | 0.583 | tested |  |
| llama-3.1-8b | triage | 59 | 12 | 0.017 | -0.125 | 0.127 | 0.883 | 0.102 | 0.030 | 0.185 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.000 | -0.300 | 0.310 |  | 0.214 | 0.077 | 0.333 | descriptive (fewer than 8 cases) |  |  | 0.215 | -0.001 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 74 | 15 | -0.135 | -0.400 | 0.128 | 0.372 | 0.324 | 0.187 | 0.455 | tested |  |  | 0.215 | 0.109 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 68 | 15 | -0.603 | -0.959 | -0.281 | 0.000 | 0.456 | 0.305 | 0.593 | tested |  |  | 0.215 | 0.241 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 74 | 15 | 0.054 | -0.120 | 0.218 | 0.512 | 0.230 | 0.132 | 0.338 | tested |  |  | 0.215 | 0.015 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 220 | 15 | 0.000 | -0.163 | 0.167 | 1.000 | 0.264 | 0.164 | 0.357 | tested |  | name | 0.215 | 0.048 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 73 | 15 | 0.068 | -0.184 | 0.329 | 0.637 | 0.315 | 0.192 | 0.447 | tested |  | name | 0.215 | 0.100 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 74 | 15 | 0.081 | -0.054 | 0.234 | 0.309 | 0.203 | 0.101 | 0.307 | tested |  | name | 0.215 | -0.012 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 73 | 15 | -0.151 | -0.362 | 0.038 | 0.133 | 0.274 | 0.162 | 0.382 | tested |  | name | 0.215 | 0.059 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 70 | 15 | 0.200 | -0.123 | 0.466 | 0.227 | 0.386 | 0.224 | 0.547 | tested |  |  | 0.215 | 0.171 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 72 | 15 | -0.486 | -0.806 | -0.232 | 0.000 | 0.375 | 0.230 | 0.529 | tested |  |  | 0.215 | 0.160 | 0.000 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.533 | 0.133 | 0.933 |  | 0.367 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  |  | 0.143 | 0.224 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 71 | 14 | 0.521 | 0.233 | 0.845 | 0.000 | 0.408 | 0.268 | 0.560 | tested |  |  | 0.143 | 0.266 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 65 | 14 | -0.508 | -0.750 | -0.311 | 0.000 | 0.415 | 0.279 | 0.551 | tested |  |  | 0.143 | 0.273 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 203 | 15 | 0.443 | 0.211 | 0.704 | 0.000 | 0.379 | 0.249 | 0.521 | tested |  | statement | 0.143 | 0.236 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 69 | 15 | 0.319 | 0.090 | 0.562 | 0.006 | 0.333 | 0.203 | 0.476 | tested |  | statement | 0.143 | 0.190 | 0.102 | False |
| llama-3.1-8b | evacuation | origin | romanian | 67 | 15 | 0.284 | 0.036 | 0.539 | 0.022 | 0.284 | 0.131 | 0.455 | tested |  | statement | 0.143 | 0.141 | 0.286 | False |
| llama-3.1-8b | evacuation | origin | syrian | 67 | 15 | 0.731 | 0.455 | 1.041 | 0.000 | 0.522 | 0.354 | 0.683 | tested |  | statement | 0.143 | 0.380 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.967 | 0.564 | 1.367 |  | 0.633 | 0.467 | 0.767 | descriptive (fewer than 8 cases) | 0.000 |  | 0.562 | 0.072 |  | False |
| llama-3.1-8b | housing | area | social_housing | 71 | 15 | 0.451 | -0.016 | 0.845 | 0.064 | 0.592 | 0.492 | 0.687 | tested | 0.070 |  | 0.562 | 0.030 | 0.768 | False |
| llama-3.1-8b | housing | area | villas | 72 | 15 | -1.750 | -2.167 | -1.321 | 0.000 | 0.819 | 0.721 | 0.908 | tested | 0.208 |  | 0.562 | 0.258 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 75 | 14 | 0.667 | 0.229 | 1.014 | 0.002 | 0.507 | 0.414 | 0.600 | tested | 0.053 |  | 0.562 | -0.055 | 0.036 | False |
| llama-3.1-8b | housing | origin | any_minority | 222 | 15 | 0.446 | 0.190 | 0.678 | 0.000 | 0.514 | 0.455 | 0.582 | tested | 0.054 | name | 0.562 | -0.048 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 72 | 15 | 0.319 | 0.077 | 0.560 | 0.010 | 0.431 | 0.328 | 0.551 | tested | 0.056 | name | 0.562 | -0.131 | 0.140 | False |
| llama-3.1-8b | housing | origin | romanian | 76 | 15 | 0.289 | -0.037 | 0.566 | 0.095 | 0.513 | 0.438 | 0.600 | tested | 0.053 | name | 0.562 | -0.048 | 1.000 | False |
| llama-3.1-8b | housing | origin | syrian | 74 | 15 | 0.730 | 0.352 | 1.040 | 0.000 | 0.595 | 0.500 | 0.687 | tested | 0.054 | name | 0.562 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 72 | 15 | 0.847 | 0.500 | 1.141 | 0.000 | 0.653 | 0.536 | 0.767 | tested | 0.056 |  | 0.562 | 0.091 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 71 | 15 | -1.099 | -1.646 | -0.718 | 0.000 | 0.634 | 0.500 | 0.766 | tested | 0.099 |  | 0.562 | 0.072 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 26 | 5 | 3.742 | -0.206 | 6.874 |  | 0.577 | 0.458 | 0.696 | descriptive (fewer than 8 cases) |  |  | 0.426 | 0.151 |  | False |
| llama-3.1-8b | relief | area | social_housing | 50 | 11 | 3.966 | 1.753 | 6.809 | 0.000 | 0.520 | 0.364 | 0.659 | tested |  |  | 0.426 | 0.094 | 0.000 | True |
| llama-3.1-8b | relief | area | villas | 51 | 11 | -0.864 | -3.369 | 1.589 | 0.511 | 0.490 | 0.341 | 0.660 | tested |  |  | 0.426 | 0.064 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 166 | 15 | 4.498 | 2.242 | 6.591 | 0.000 | 0.651 | 0.567 | 0.727 | tested |  | statement | 0.426 | 0.225 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 56 | 15 | 3.841 | 0.951 | 6.586 | 0.007 | 0.714 | 0.597 | 0.821 | tested |  | statement | 0.426 | 0.288 | 0.105 | False |
| llama-3.1-8b | relief | origin | romanian | 57 | 13 | 3.536 | 1.069 | 5.899 | 0.006 | 0.561 | 0.460 | 0.672 | tested |  | statement | 0.426 | 0.135 | 0.102 | False |
| llama-3.1-8b | relief | origin | syrian | 53 | 12 | 6.225 | 4.438 | 7.890 | 0.000 | 0.679 | 0.564 | 0.787 | tested |  | statement | 0.426 | 0.253 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 174 | 13 | 0.195 | 0.069 | 0.365 | 0.000 | 0.218 | 0.132 | 0.313 | tested |  | statement | 0.102 | 0.117 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 56 | 12 | 0.071 | -0.068 | 0.229 | 0.397 | 0.179 | 0.055 | 0.326 | tested |  | statement | 0.102 | 0.077 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 59 | 12 | 0.136 | -0.073 | 0.378 | 0.255 | 0.254 | 0.136 | 0.382 | tested |  | statement | 0.102 | 0.153 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 59 | 12 | 0.373 | 0.235 | 0.545 | 0.000 | 0.220 | 0.143 | 0.311 | tested |  | statement | 0.102 | 0.119 | 0.000 | True |

## Sensitivity: origins without an official name source

Origins whose names have no official source: syrian. The fairness table is recomputed without them, so that the pooled origin=any_minority and the Holm correction rest on sourced names only.

| analysis | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- |
| all origins | 34 | 14 | 9 | 5 | 1 |
| without unsourced origins | 29 | 8 | 3 | 5 | 1 |

## Origin contrasts by how origin is signalled

name: origin is signalled only by the person's name (dispatch, housing). statement: origin is stated in words, for example 'Most residents are refugees from Syria' (evacuation, relief, triage). An effect carried by statements does not depend on the choice of names.

| value | signal | tasks | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- | --- | --- |
| local_migrant | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| local_migrant | statement | evacuation, relief, triage | 3 | 0 | 0 | 0 | 0 |
| romanian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| romanian | statement | evacuation, relief, triage | 3 | 0 | 0 | 0 | 0 |
| syrian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| syrian | statement | evacuation, relief, triage | 3 | 3 | 3 | 0 | 1 |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.000 | -0.300 | 0.310 |  | 0.214 | 0.077 | 0.333 | descriptive (fewer than 8 cases) |  |  | 0.215 | -0.001 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 74 | 15 | -0.135 | -0.400 | 0.128 | 0.372 | 0.324 | 0.187 | 0.455 | tested |  |  | 0.215 | 0.109 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 68 | 15 | -0.603 | -0.959 | -0.281 | 0.000 | 0.456 | 0.305 | 0.593 | tested |  |  | 0.215 | 0.241 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 74 | 15 | 0.054 | -0.120 | 0.218 | 0.512 | 0.230 | 0.132 | 0.338 | tested |  |  | 0.215 | 0.015 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 220 | 15 | 0.000 | -0.163 | 0.167 | 1.000 | 0.264 | 0.164 | 0.357 | tested |  | name | 0.215 | 0.048 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 73 | 15 | 0.068 | -0.184 | 0.329 | 0.637 | 0.315 | 0.192 | 0.447 | tested |  | name | 0.215 | 0.100 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 74 | 15 | 0.081 | -0.054 | 0.234 | 0.309 | 0.203 | 0.101 | 0.307 | tested |  | name | 0.215 | -0.012 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 73 | 15 | -0.151 | -0.362 | 0.038 | 0.133 | 0.274 | 0.162 | 0.382 | tested |  | name | 0.215 | 0.059 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 70 | 15 | 0.200 | -0.123 | 0.466 | 0.227 | 0.386 | 0.224 | 0.547 | tested |  |  | 0.215 | 0.171 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 72 | 15 | -0.486 | -0.806 | -0.232 | 0.000 | 0.375 | 0.230 | 0.529 | tested |  |  | 0.215 | 0.160 | 0.000 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.533 | 0.133 | 0.933 |  | 0.367 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  |  | 0.143 | 0.224 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 71 | 14 | 0.521 | 0.233 | 0.845 | 0.000 | 0.408 | 0.268 | 0.560 | tested |  |  | 0.143 | 0.266 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 65 | 14 | -0.508 | -0.750 | -0.311 | 0.000 | 0.415 | 0.279 | 0.551 | tested |  |  | 0.143 | 0.273 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 203 | 15 | 0.443 | 0.211 | 0.704 | 0.000 | 0.379 | 0.249 | 0.521 | tested |  | statement | 0.143 | 0.236 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 69 | 15 | 0.319 | 0.090 | 0.562 | 0.006 | 0.333 | 0.203 | 0.476 | tested |  | statement | 0.143 | 0.190 | 0.102 | False |
| llama-3.1-8b | evacuation | origin | romanian | 67 | 15 | 0.284 | 0.036 | 0.539 | 0.022 | 0.284 | 0.131 | 0.455 | tested |  | statement | 0.143 | 0.141 | 0.330 | False |
| llama-3.1-8b | evacuation | origin | syrian | 67 | 15 | 0.731 | 0.455 | 1.041 | 0.000 | 0.522 | 0.354 | 0.683 | tested |  | statement | 0.143 | 0.380 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.967 | 0.564 | 1.367 |  | 0.633 | 0.467 | 0.767 | descriptive (fewer than 8 cases) | 0.000 |  | 0.562 | 0.072 |  | False |
| llama-3.1-8b | housing | area | social_housing | 71 | 15 | 0.451 | -0.016 | 0.845 | 0.064 | 0.592 | 0.492 | 0.687 | tested | 0.070 |  | 0.562 | 0.030 | 0.768 | False |
| llama-3.1-8b | housing | area | villas | 72 | 15 | -1.750 | -2.167 | -1.321 | 0.000 | 0.819 | 0.721 | 0.908 | tested | 0.208 |  | 0.562 | 0.258 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 75 | 14 | 0.667 | 0.229 | 1.014 | 0.002 | 0.507 | 0.414 | 0.600 | tested | 0.053 |  | 0.562 | -0.055 | 0.038 | False |
| llama-3.1-8b | housing | origin | any_minority | 222 | 15 | 0.446 | 0.190 | 0.678 | 0.000 | 0.514 | 0.455 | 0.582 | tested | 0.054 | name | 0.562 | -0.048 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 72 | 15 | 0.319 | 0.077 | 0.560 | 0.010 | 0.431 | 0.328 | 0.551 | tested | 0.056 | name | 0.562 | -0.131 | 0.160 | False |
| llama-3.1-8b | housing | origin | romanian | 76 | 15 | 0.289 | -0.037 | 0.566 | 0.095 | 0.513 | 0.438 | 0.600 | tested | 0.053 | name | 0.562 | -0.048 | 1.000 | False |
| llama-3.1-8b | housing | origin | syrian | 74 | 15 | 0.730 | 0.352 | 1.040 | 0.000 | 0.595 | 0.500 | 0.687 | tested | 0.054 | name | 0.562 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | status | asylum_seeker | 72 | 15 | 0.847 | 0.500 | 1.141 | 0.000 | 0.653 | 0.536 | 0.767 | tested | 0.056 |  | 0.562 | 0.091 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 71 | 15 | -1.099 | -1.646 | -0.718 | 0.000 | 0.634 | 0.500 | 0.766 | tested | 0.099 |  | 0.562 | 0.072 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 19 | 5 | 2.947 | -0.500 | 6.722 |  | 0.526 | 0.214 | 0.708 | descriptive (fewer than 8 cases) |  |  | 0.438 | 0.089 |  | False |
| llama-3.1-8b | relief | area | social_housing | 31 | 10 | 3.258 | 1.241 | 5.913 | 0.000 | 0.452 | 0.281 | 0.657 | tested |  |  | 0.438 | 0.014 | 0.000 | False |
| llama-3.1-8b | relief | area | villas | 33 | 10 | -0.803 | -3.531 | 2.294 | 0.617 | 0.455 | 0.222 | 0.676 | tested |  |  | 0.438 | 0.017 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 111 | 14 | 3.761 | 1.469 | 5.556 | 0.005 | 0.640 | 0.552 | 0.747 | tested |  | statement | 0.438 | 0.202 | 0.090 | False |
| llama-3.1-8b | relief | origin | local_migrant | 38 | 12 | 3.618 | 0.278 | 6.397 | 0.027 | 0.684 | 0.575 | 0.811 | tested |  | statement | 0.438 | 0.247 | 0.378 | False |
| llama-3.1-8b | relief | origin | romanian | 37 | 12 | 2.122 | 0.013 | 4.650 | 0.049 | 0.568 | 0.383 | 0.767 | tested |  | statement | 0.438 | 0.130 | 0.637 | False |
| llama-3.1-8b | relief | origin | syrian | 36 | 11 | 5.597 | 3.515 | 7.321 | 0.000 | 0.667 | 0.545 | 0.758 | tested |  | statement | 0.438 | 0.229 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 174 | 13 | 0.195 | 0.069 | 0.365 | 0.000 | 0.218 | 0.132 | 0.313 | tested |  | statement | 0.102 | 0.117 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 56 | 12 | 0.071 | -0.068 | 0.229 | 0.397 | 0.179 | 0.055 | 0.326 | tested |  | statement | 0.102 | 0.077 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 59 | 12 | 0.136 | -0.073 | 0.378 | 0.255 | 0.254 | 0.136 | 0.382 | tested |  | statement | 0.102 | 0.153 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 59 | 12 | 0.373 | 0.235 | 0.545 | 0.000 | 0.220 | 0.143 | 0.311 | tested |  | statement | 0.102 | 0.119 | 0.000 | True |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | age80 | 71 | 15 | 0.479 | 0.315 | 0.632 | 0.944 | 0.529 | 1.375 |
| llama-3.1-8b | dispatch | dialysis | 67 | 15 | 0.567 | 0.413 | 0.703 | 1.119 | 0.719 | 1.508 |
| llama-3.1-8b | dispatch | infant | 71 | 15 | 0.549 | 0.371 | 0.720 | 1.155 | 0.733 | 1.563 |
| llama-3.1-8b | dispatch | pregnant | 74 | 15 | 0.595 | 0.438 | 0.740 | 1.216 | 0.819 | 1.632 |
| llama-3.1-8b | dispatch | wheelchair | 70 | 15 | 0.486 | 0.319 | 0.649 | 0.943 | 0.532 | 1.346 |
| llama-3.1-8b | evacuation | age80 | 66 | 14 | 0.652 | 0.508 | 0.783 | 0.939 | 0.672 | 1.205 |
| llama-3.1-8b | evacuation | dialysis | 67 | 14 | 0.657 | 0.500 | 0.809 | 0.955 | 0.662 | 1.258 |
| llama-3.1-8b | evacuation | infant | 64 | 15 | 0.656 | 0.492 | 0.803 | 0.938 | 0.643 | 1.230 |
| llama-3.1-8b | evacuation | pregnant | 68 | 15 | 0.676 | 0.529 | 0.811 | 1.000 | 0.708 | 1.286 |
| llama-3.1-8b | evacuation | wheelchair | 70 | 15 | 0.571 | 0.391 | 0.729 | 0.857 | 0.514 | 1.186 |
| llama-3.1-8b | housing | age80 | 72 | 15 | 0.972 | 0.933 | 1.000 | 3.111 | 2.716 | 3.488 |
| llama-3.1-8b | housing | dialysis | 72 | 15 | 1.000 | 1.000 | 1.000 | 3.431 | 3.000 | 3.833 |
| llama-3.1-8b | housing | infant | 75 | 15 | 0.973 | 0.931 | 1.000 | 3.360 | 2.923 | 3.744 |
| llama-3.1-8b | housing | pregnant | 69 | 14 | 0.986 | 0.956 | 1.000 | 3.246 | 2.857 | 3.614 |
| llama-3.1-8b | housing | wheelchair | 71 | 15 | 0.915 | 0.844 | 0.974 | 2.901 | 2.529 | 3.277 |
| llama-3.1-8b | relief | age80 | 55 | 13 | 0.673 | 0.483 | 0.833 | 9.346 | 4.633 | 13.720 |
| llama-3.1-8b | relief | dialysis | 55 | 14 | 0.673 | 0.522 | 0.800 | 8.701 | 4.667 | 12.370 |
| llama-3.1-8b | relief | infant | 55 | 13 | 0.655 | 0.490 | 0.800 | 7.001 | 2.730 | 10.795 |
| llama-3.1-8b | relief | pregnant | 53 | 13 | 0.642 | 0.447 | 0.805 | 6.218 | 2.381 | 9.416 |
| llama-3.1-8b | relief | wheelchair | 54 | 13 | 0.556 | 0.424 | 0.684 | 3.995 | 0.882 | 7.283 |
| llama-3.1-8b | triage | age80 | 57 | 13 | 0.474 | 0.360 | 0.600 | 0.789 | 0.566 | 1.050 |
| llama-3.1-8b | triage | dialysis | 55 | 11 | 0.436 | 0.345 | 0.529 | 0.691 | 0.508 | 0.898 |
| llama-3.1-8b | triage | infant | 54 | 12 | 0.574 | 0.425 | 0.714 | 1.037 | 0.709 | 1.436 |
| llama-3.1-8b | triage | pregnant | 58 | 11 | 0.483 | 0.370 | 0.614 | 0.810 | 0.645 | 0.982 |
| llama-3.1-8b | triage | wheelchair | 59 | 12 | 0.237 | 0.170 | 0.314 | 0.390 | 0.302 | 0.478 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | triage | need=wheelchair | 65 | 13 | 0.215 |
| llama-3.1-8b | triage | need=dialysis | 61 | 14 | 0.262 |
| llama-3.1-8b | triage | need=age80 | 63 | 14 | 0.317 |
| llama-3.1-8b | triage | need=pregnant | 67 | 15 | 0.343 |
| llama-3.1-8b | triage | need=infant | 60 | 15 | 0.367 |
| llama-3.1-8b | triage | origin=syrian | 67 | 13 | 0.493 |
| llama-3.1-8b | triage | placebo | 69 | 14 | 0.580 |
| llama-3.1-8b | triage | base | 65 | 14 | 0.646 |
| llama-3.1-8b | triage | origin=romanian | 66 | 15 | 0.652 |
| llama-3.1-8b | triage | origin=local_migrant | 64 | 14 | 0.688 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el | kendall_w | 0.608 | 15 | 28 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.723 | 15 | 26 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.787 | 15 | 27 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.627 | 14 | 25 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.723 | 14 | 27 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.755 | 13 | 24 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.290 | 15 | 28 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.597 | 15 | 26 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | 0.570 | 13 | 25 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.362 | 12 | 21 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.509 | 14 | 23 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.283 | 11 | 18 |
| llama-3.1-8b | triage | el | kendall_w | 0.650 | 12 | 23 |
| llama-3.1-8b | triage | en | kendall_w | 0.844 | 10 | 19 |
| llama-3.1-8b | triage | fr | kendall_w | 0.778 | 14 | 23 |

## Cross-lingual consistency of the base cases

p_holm: Holm correction across all comparisons (task by language pair) of each model, as in the fairness table. reportable: p_holm < 0.05. Bootstrap p-values are resolved to 1/2000; 0.000 means below that.

| model | task | pair | cases | difference | lo | hi | p | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el-en | 15 | 0.233 | -0.067 | 0.567 | 0.165 | 1.000 | False |
| llama-3.1-8b | dispatch | el-fr | 15 | 0.433 | 0.000 | 0.900 | 0.054 | 0.594 | False |
| llama-3.1-8b | dispatch | en-fr | 15 | 0.200 | -0.267 | 0.667 | 0.421 | 1.000 | False |
| llama-3.1-8b | evacuation | el-en | 13 | 0.000 | -0.269 | 0.231 | 1.000 | 1.000 | False |
| llama-3.1-8b | evacuation | el-fr | 12 | 0.167 | -0.250 | 0.500 | 0.408 | 1.000 | False |
| llama-3.1-8b | evacuation | en-fr | 13 | 0.154 | -0.038 | 0.346 | 0.170 | 1.000 | False |
| llama-3.1-8b | housing | el-en | 15 | -0.233 | -0.700 | 0.233 | 0.369 | 1.000 | False |
| llama-3.1-8b | housing | el-fr | 13 | 3.308 | 2.577 | 4.038 | 0.000 | 0.000 | True |
| llama-3.1-8b | housing | en-fr | 13 | 3.269 | 2.654 | 4.000 | 0.000 | 0.000 | True |
| llama-3.1-8b | relief | el-en | 11 | 2.462 | -1.467 | 6.321 | 0.210 | 1.000 | False |
| llama-3.1-8b | relief | el-fr | 10 | -0.522 | -6.119 | 4.782 | 0.897 | 1.000 | False |
| llama-3.1-8b | relief | en-fr | 10 | -1.977 | -6.482 | 2.151 | 0.381 | 1.000 | False |
| llama-3.1-8b | triage | el-en | 10 | -0.400 | -0.800 | -0.099 | 0.014 | 0.168 | False |
| llama-3.1-8b | triage | el-fr | 12 | -0.500 | -0.875 | -0.167 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | en-fr | 10 | -0.050 | -0.300 | 0.200 | 0.855 | 1.000 | False |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | 0.000 | -0.500 | 0.500 |  | 0.333 | 0.333 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 47 | 9 | -0.213 | -0.587 | 0.222 | 0.349 | 0.468 | 0.327 | 0.617 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 27 | 6 | 0.000 | -0.091 | 0.111 |  | 0.074 | 0.000 | 0.160 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 43 | 9 | -0.791 | -1.317 | -0.325 | 0.000 | 0.605 | 0.444 | 0.767 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 25 | 6 | -0.280 | -0.542 | -0.042 |  | 0.200 | 0.048 | 0.312 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 48 | 9 | 0.083 | -0.167 | 0.304 | 0.539 | 0.312 | 0.185 | 0.455 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 26 | 6 | 0.000 | -0.094 | 0.130 |  | 0.077 | 0.000 | 0.179 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 139 | 9 | -0.029 | -0.268 | 0.235 | 0.831 | 0.374 | 0.296 | 0.462 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 81 | 6 | 0.049 | -0.043 | 0.222 |  | 0.074 | 0.020 | 0.162 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 46 | 9 | 0.065 | -0.333 | 0.457 | 0.800 | 0.435 | 0.311 | 0.580 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 27 | 6 | 0.074 | -0.062 | 0.350 |  | 0.111 | 0.030 | 0.250 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 49 | 9 | 0.122 | -0.078 | 0.360 | 0.300 | 0.306 | 0.192 | 0.419 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 25 | 6 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 44 | 9 | -0.295 | -0.595 | -0.020 | 0.046 | 0.386 | 0.263 | 0.500 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 29 | 6 | 0.069 | -0.061 | 0.292 |  | 0.103 | 0.030 | 0.208 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 45 | 9 | 0.222 | -0.264 | 0.620 | 0.381 | 0.556 | 0.404 | 0.711 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 25 | 6 | 0.160 | 0.000 | 0.462 |  | 0.080 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 45 | 9 | -0.667 | -1.128 | -0.304 | 0.000 | 0.533 | 0.388 | 0.725 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 27 | 6 | -0.185 | -0.379 | 0.000 |  | 0.111 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.778 | 0.167 | 1.167 |  | 0.500 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.167 | 0.000 | 0.333 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 45 | 9 | 0.689 | 0.375 | 1.095 | 0.000 | 0.489 | 0.320 | 0.682 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 26 | 5 | 0.231 | -0.174 | 0.690 |  | 0.269 | 0.045 | 0.483 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 40 | 9 | -0.725 | -1.000 | -0.481 | 0.000 | 0.575 | 0.458 | 0.688 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 25 | 5 | -0.160 | -0.267 | -0.043 |  | 0.160 | 0.043 | 0.267 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 121 | 9 | 0.603 | 0.314 | 0.931 | 0.000 | 0.504 | 0.367 | 0.678 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 82 | 6 | 0.207 | -0.029 | 0.500 |  | 0.195 | 0.037 | 0.379 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 41 | 9 | 0.439 | 0.111 | 0.769 | 0.011 | 0.439 | 0.279 | 0.628 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 28 | 6 | 0.143 | -0.083 | 0.406 |  | 0.179 | 0.036 | 0.344 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 39 | 9 | 0.410 | 0.044 | 0.758 | 0.034 | 0.385 | 0.175 | 0.619 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 28 | 6 | 0.107 | -0.100 | 0.393 |  | 0.143 | 0.000 | 0.312 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 41 | 9 | 0.951 | 0.605 | 1.385 | 0.000 | 0.683 | 0.535 | 0.833 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 26 | 6 | 0.385 | 0.048 | 0.731 |  | 0.269 | 0.038 | 0.484 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.667 | 0.167 | 1.167 |  | 0.611 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 1.417 | 1.167 | 1.667 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 42 | 9 | 0.381 | -0.286 | 0.875 | 0.236 | 0.619 | 0.479 | 0.745 | tested | 0.048 |
| llama-3.1-8b | housing | area | social_housing | clear | 29 | 6 | 0.552 | -0.077 | 1.103 |  | 0.552 | 0.364 | 0.694 | descriptive (fewer than 8 cases) | 0.103 |
| llama-3.1-8b | housing | area | villas | ambiguous | 43 | 9 | -1.767 | -2.395 | -1.143 | 0.000 | 0.814 | 0.680 | 0.935 | tested | 0.140 |
| llama-3.1-8b | housing | area | villas | clear | 29 | 6 | -1.724 | -2.061 | -1.273 |  | 0.828 | 0.690 | 0.966 | descriptive (fewer than 8 cases) | 0.310 |
| llama-3.1-8b | housing | gender | female | ambiguous | 46 | 9 | 0.522 | -0.116 | 1.040 | 0.117 | 0.587 | 0.481 | 0.689 | tested | 0.043 |
| llama-3.1-8b | housing | gender | female | clear | 29 | 5 | 0.897 | 0.643 | 1.133 |  | 0.379 | 0.286 | 0.467 | descriptive (fewer than 8 cases) | 0.069 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 131 | 9 | 0.412 | 0.046 | 0.718 | 0.025 | 0.534 | 0.457 | 0.629 | tested | 0.046 |
| llama-3.1-8b | housing | origin | any_minority | clear | 91 | 6 | 0.495 | 0.082 | 0.784 |  | 0.484 | 0.402 | 0.580 | descriptive (fewer than 8 cases) | 0.066 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 42 | 9 | 0.381 | 0.195 | 0.605 | 0.000 | 0.452 | 0.280 | 0.628 | tested | 0.048 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 30 | 6 | 0.233 | -0.357 | 0.676 |  | 0.400 | 0.312 | 0.545 | descriptive (fewer than 8 cases) | 0.067 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 45 | 9 | 0.178 | -0.351 | 0.612 | 0.506 | 0.511 | 0.404 | 0.652 | tested | 0.044 |
| llama-3.1-8b | housing | origin | romanian | clear | 31 | 6 | 0.452 | 0.280 | 0.645 |  | 0.516 | 0.419 | 0.607 | descriptive (fewer than 8 cases) | 0.065 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 44 | 9 | 0.682 | 0.133 | 1.083 | 0.019 | 0.636 | 0.512 | 0.769 | tested | 0.045 |
| llama-3.1-8b | housing | origin | syrian | clear | 30 | 6 | 0.800 | 0.250 | 1.206 |  | 0.533 | 0.423 | 0.625 | descriptive (fewer than 8 cases) | 0.067 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 44 | 9 | 0.659 | 0.204 | 1.080 | 0.006 | 0.614 | 0.429 | 0.786 | tested | 0.045 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 28 | 6 | 1.143 | 0.778 | 1.333 |  | 0.714 | 0.600 | 0.826 | descriptive (fewer than 8 cases) | 0.071 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 43 | 9 | -1.116 | -1.923 | -0.585 | 0.000 | 0.605 | 0.409 | 0.804 | tested | 0.093 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 28 | 6 | -1.071 | -1.429 | -0.679 |  | 0.679 | 0.529 | 0.788 | descriptive (fewer than 8 cases) | 0.107 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 15 | 3 | 3.687 | -0.565 | 8.631 |  | 0.467 | 0.400 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 11 | 2 | 3.818 | -0.600 | 7.500 |  | 0.727 | 0.667 | 0.800 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 26 | 6 | 2.084 | 0.377 | 3.569 |  | 0.538 | 0.280 | 0.714 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | clear | 24 | 5 | 6.004 | 2.130 | 11.708 |  | 0.500 | 0.292 | 0.684 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 28 | 7 | -0.795 | -2.978 | 1.254 |  | 0.464 | 0.292 | 0.654 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | clear | 23 | 4 | -0.949 | -5.783 | 4.299 |  | 0.522 | 0.250 | 0.818 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 91 | 9 | 4.056 | 2.260 | 5.952 | 0.000 | 0.626 | 0.515 | 0.717 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 75 | 6 | 5.034 | 0.522 | 8.857 |  | 0.680 | 0.567 | 0.825 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 31 | 9 | 3.036 | 1.286 | 4.953 | 0.000 | 0.710 | 0.536 | 0.867 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 25 | 6 | 4.840 | -1.698 | 9.938 |  | 0.720 | 0.600 | 0.857 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 32 | 8 | 3.595 | 0.852 | 6.343 | 0.003 | 0.531 | 0.407 | 0.610 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 25 | 5 | 3.461 | -0.647 | 8.059 |  | 0.600 | 0.423 | 0.850 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 28 | 6 | 5.712 | 3.565 | 7.560 |  | 0.643 | 0.440 | 0.821 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | clear | 25 | 6 | 6.800 | 3.667 | 10.286 |  | 0.720 | 0.600 | 0.810 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 107 | 8 | 0.224 | 0.033 | 0.495 | 0.020 | 0.280 | 0.165 | 0.398 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 67 | 5 | 0.149 | 0.061 | 0.267 |  | 0.119 | 0.049 | 0.189 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 35 | 7 | 0.086 | -0.111 | 0.333 |  | 0.257 | 0.077 | 0.447 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 21 | 5 | 0.048 | 0.000 | 0.125 |  | 0.048 | 0.000 | 0.133 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 36 | 7 | 0.111 | -0.194 | 0.500 |  | 0.306 | 0.133 | 0.486 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | clear | 23 | 5 | 0.174 | 0.040 | 0.333 |  | 0.174 | 0.043 | 0.286 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 36 | 7 | 0.472 | 0.341 | 0.667 |  | 0.278 | 0.205 | 0.370 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | clear | 23 | 5 | 0.217 | 0.038 | 0.600 |  | 0.130 | 0.036 | 0.308 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | el | 1666 | 0.981 | 0.016 | not-a-permutation 26, bad-shares 3, shares-do-not-sum-to-100 2, no-json 1 |
| llama-3.1-8b | en | 1677 | 0.943 | 0.041 | not-a-permutation 61, bad-shares 20, no-json 15 |
| llama-3.1-8b | fr | 1673 | 0.961 | 0.023 | not-a-permutation 41, bad-shares 19, no-json 5 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.852 | 0.920 | 0.068 |
| llama-3.1-8b | dispatch | need=dialysis | 0.857 | 0.920 | 0.063 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.871 | 0.920 | 0.050 |
| llama-3.1-8b | dispatch | area=villas | 0.892 | 0.920 | 0.029 |
| llama-3.1-8b | dispatch | gender=female | 0.906 | 0.920 | 0.015 |
| llama-3.1-8b | dispatch | need=infant | 0.906 | 0.920 | 0.015 |
| llama-3.1-8b | dispatch | need=pregnant | 0.907 | 0.920 | 0.013 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.907 | 0.920 | 0.013 |
| llama-3.1-8b | dispatch | origin=romanian | 0.907 | 0.920 | 0.013 |
| llama-3.1-8b | dispatch | need=age80 | 0.928 | 0.920 | -0.007 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.928 | 0.920 | -0.007 |
| llama-3.1-8b | dispatch | origin=syrian | 0.929 | 0.920 | -0.008 |
| llama-3.1-8b | dispatch | area=social_housing | 0.930 | 0.920 | -0.010 |
| llama-3.1-8b | dispatch | placebo | 0.933 | 0.920 | -0.012 |
| llama-3.1-8b | dispatch | area=roma_settlement | 1.000 | 0.920 | -0.080 |
| llama-3.1-8b | evacuation | area=villas | 0.961 | 0.974 | 0.014 |
| llama-3.1-8b | evacuation | need=infant | 0.973 | 0.974 | 0.001 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.974 | 0.974 | 0.000 |
| llama-3.1-8b | evacuation | origin=romanian | 0.987 | 0.974 | -0.012 |
| llama-3.1-8b | evacuation | need=pregnant | 0.987 | 0.974 | -0.013 |
| llama-3.1-8b | evacuation | area=social_housing | 0.988 | 0.974 | -0.013 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.974 | -0.026 |
| llama-3.1-8b | evacuation | need=age80 | 1.000 | 0.974 | -0.026 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.974 | -0.026 |
| llama-3.1-8b | evacuation | need=wheelchair | 1.000 | 0.974 | -0.026 |
| llama-3.1-8b | evacuation | origin=syrian | 1.000 | 0.974 | -0.026 |
| llama-3.1-8b | evacuation | placebo | 1.000 | 0.974 | -0.026 |
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
| llama-3.1-8b | relief | need=dialysis | 0.928 | 0.873 | -0.054 |
| llama-3.1-8b | relief | placebo | 0.928 | 0.873 | -0.054 |
| llama-3.1-8b | relief | need=wheelchair | 0.930 | 0.873 | -0.056 |
| llama-3.1-8b | relief | area=social_housing | 0.940 | 0.873 | -0.067 |
| llama-3.1-8b | relief | area=villas | 0.957 | 0.873 | -0.083 |
| llama-3.1-8b | relief | need=pregnant | 0.957 | 0.873 | -0.083 |
| llama-3.1-8b | relief | origin=local_migrant | 0.958 | 0.873 | -0.085 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.873 | -0.093 |
| llama-3.1-8b | relief | origin=syrian | 0.971 | 0.873 | -0.098 |
| llama-3.1-8b | relief | origin=romanian | 0.972 | 0.873 | -0.099 |
| llama-3.1-8b | relief | need=age80 | 0.986 | 0.873 | -0.113 |
| llama-3.1-8b | relief | need=infant | 0.986 | 0.873 | -0.113 |
| llama-3.1-8b | triage | need=infant | 0.938 | 0.985 | 0.047 |
| llama-3.1-8b | triage | need=age80 | 0.955 | 0.985 | 0.030 |
| llama-3.1-8b | triage | origin=romanian | 0.971 | 0.985 | 0.014 |
| llama-3.1-8b | triage | placebo | 0.972 | 0.985 | 0.013 |
| llama-3.1-8b | triage | need=dialysis | 0.984 | 0.985 | 0.001 |
| llama-3.1-8b | triage | origin=local_migrant | 0.985 | 0.985 | 0.000 |
| llama-3.1-8b | triage | need=wheelchair | 0.985 | 0.985 | 0.000 |
| llama-3.1-8b | triage | need=pregnant | 1.000 | 0.985 | -0.015 |
| llama-3.1-8b | triage | origin=syrian | 1.000 | 0.985 | -0.015 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | Intercept | -0.165 | 0.324 | 0.611 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.147 | 0.355 | 0.679 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | -0.393 | 0.357 | 0.271 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.150 | 0.357 | 0.675 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.387 | 0.354 | 0.275 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.367 | 0.355 | 0.302 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.064 | 0.357 | 0.858 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | -0.057 | 0.357 | 0.874 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.151 | 0.356 | 0.671 |  |
| llama-3.1-8b | dispatch | C(language)[T.en] | -0.001 | 0.421 | 0.998 |  |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 0.006 | 0.432 | 0.988 |  |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.165 | 0.170 | 0.332 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.323 | 0.494 | 0.513 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.251 | 0.502 | 0.617 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.003 | 0.496 | 0.995 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.290 | 0.493 | 0.556 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -0.236 | 0.493 | 0.632 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.146 | 0.496 | 0.768 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.910 | 0.501 | 0.070 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.319 | 0.500 | 0.523 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.181 | 0.502 | 0.718 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | -0.043 | 0.507 | 0.933 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | 0.098 | 0.502 | 0.845 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.325 | 0.505 | 0.520 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.269 | 0.504 | 0.594 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.151 | 0.503 | 0.764 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | 0.349 | 0.504 | 0.489 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.375 | 0.501 | 0.454 |  |
| llama-3.1-8b | evacuation | Intercept | 0.552 | 0.274 | 0.044 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.041 | 0.294 | 0.889 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.096 | 0.304 | 0.000 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.040 | 0.290 | 0.890 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | -0.009 | 0.294 | 0.975 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.172 | 0.292 | 0.556 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.400 | 0.338 | 0.237 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.300 | 0.338 | 0.375 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.283 | 0.208 | 0.174 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.343 | 0.404 | 0.396 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.205 | 0.414 | 0.620 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.542 | 0.405 | 0.180 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.549 | 0.407 | 0.177 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.209 | 0.408 | 0.610 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.323 | 0.409 | 0.429 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.124 | 0.417 | 0.765 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.423 | 0.407 | 0.299 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.625 | 0.412 | 0.129 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.219 | 0.408 | 0.591 |  |
| llama-3.1-8b | housing | Intercept | -0.050 | 0.483 | 0.917 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.631 | 0.510 | 0.216 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -1.960 | 0.508 | 0.000 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female] | 0.073 | 0.505 | 0.885 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | 0.147 | 0.508 | 0.772 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | 0.165 | 0.505 | 0.743 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.665 | 0.505 | 0.187 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.465 | 0.510 | 0.362 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.550 | 0.510 | 0.000 | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.en] | 0.500 | 0.601 | 0.406 | did not converge; read with care |
| llama-3.1-8b | housing | C(language)[T.fr] | 2.400 | 0.601 | 0.000 | did not converge; read with care |
| llama-3.1-8b | housing | C(clarity)[T.clear] | 0.034 | 0.355 | 0.923 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | 0.459 | 0.718 | 0.523 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.773 | 0.712 | 0.278 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.342 | 0.710 | 0.630 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.732 | 0.716 | 0.307 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.882 | 0.708 | 0.213 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -1.142 | 0.712 | 0.109 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.392 | 0.716 | 0.584 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.243 | 0.719 | 0.084 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.084 | 0.716 | 0.906 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.365 | 0.719 | 0.058 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.721 | 0.712 | 0.311 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.599 | 0.714 | 0.025 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.535 | 0.712 | 0.031 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.522 | 0.712 | 0.033 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -2.138 | 0.716 | 0.003 | did not converge; read with care |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.235 | 0.717 | 0.743 | did not converge; read with care |
| llama-3.1-8b | relief | Intercept | 1.020 | 3.243 | 0.753 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | 0.808 | 3.597 | 0.822 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -2.757 | 3.593 | 0.443 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 3.671 | 3.571 | 0.304 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | 1.387 | 3.549 | 0.696 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 5.867 | 3.622 | 0.105 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 3.120 | 4.148 | 0.452 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 5.095 | 4.280 | 0.234 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | 1.909 | 2.180 | 0.381 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -1.110 | 5.142 | 0.829 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | -1.233 | 5.110 | 0.809 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -4.125 | 5.033 | 0.412 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -1.370 | 5.004 | 0.784 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -5.111 | 5.083 | 0.315 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -3.317 | 5.213 | 0.525 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -6.802 | 5.211 | 0.192 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -9.384 | 5.171 | 0.070 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -6.479 | 5.153 | 0.209 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -7.959 | 5.205 | 0.126 |  |
| llama-3.1-8b | triage | Intercept | 0.154 | 0.183 | 0.400 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | 0.118 | 0.202 | 0.559 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | 0.244 | 0.202 | 0.228 | did not converge; read with care |
| llama-3.1-8b | triage | C(language)[T.en] | -0.071 | 0.211 | 0.735 | did not converge; read with care |
| llama-3.1-8b | triage | C(language)[T.fr] | 0.024 | 0.214 | 0.910 | did not converge; read with care |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.097 | 0.200 | 0.628 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | -0.007 | 0.297 | 0.981 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.244 | 0.297 | 0.412 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.112 | 0.295 | 0.704 | did not converge; read with care |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.409 | 0.296 | 0.167 | did not converge; read with care |
