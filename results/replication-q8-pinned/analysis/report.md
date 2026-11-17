# Analysis: replication-q8-pinned

Records: 5880; valid: 5666; counterfactual pairs: 5056.

Positive shift = the target moved up in priority (ranking positions, percentage points of supplies, or score points).

## Noise floor: the base case re-run with a new seed

| model | task | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | 81 | 15 | -0.111 | -0.271 | 0.074 | 0.238 | 0.210 | 0.118 | 0.305 | tested |  |
| llama-3.1-8b | evacuation | 87 | 15 | -0.069 | -0.191 | 0.034 | 0.263 | 0.126 | 0.045 | 0.227 | tested |  |
| llama-3.1-8b | housing | 90 | 15 | 0.100 | -0.300 | 0.444 | 0.591 | 0.511 | 0.389 | 0.622 | tested | 0.033 |
| llama-3.1-8b | relief | 77 | 15 | 0.492 | -0.806 | 1.749 | 0.454 | 0.390 | 0.284 | 0.512 | tested |  |
| llama-3.1-8b | triage | 88 | 15 | 0.023 | -0.080 | 0.112 | 0.684 | 0.125 | 0.056 | 0.195 | tested |  |

## Fairness: attributes that should not change the decision

![Signed shifts](fairness.png)

excess_flip = flip_rate minus the noise floor for the same model and task. Rows resting on fewer than 8 cases are descriptive and are not tested. origin=any_minority pools every non-reference origin.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.000 | -0.300 | 0.310 |  | 0.214 | 0.077 | 0.333 | descriptive (fewer than 8 cases) |  |  | 0.210 | 0.004 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 79 | 15 | -0.165 | -0.434 | 0.092 | 0.274 | 0.316 | 0.175 | 0.456 | tested |  |  | 0.210 | 0.107 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 75 | 15 | -0.613 | -0.961 | -0.320 | 0.000 | 0.440 | 0.280 | 0.589 | tested |  |  | 0.210 | 0.230 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 78 | 15 | 0.051 | -0.116 | 0.202 | 0.512 | 0.218 | 0.128 | 0.315 | tested |  |  | 0.210 | 0.008 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 236 | 15 | 0.021 | -0.141 | 0.181 | 0.816 | 0.267 | 0.171 | 0.352 | tested |  | name | 0.210 | 0.057 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | 0.065 | -0.180 | 0.311 | 0.637 | 0.299 | 0.184 | 0.420 | tested |  | name | 0.210 | 0.089 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 79 | 15 | 0.114 | -0.013 | 0.263 | 0.128 | 0.215 | 0.127 | 0.308 | tested |  | name | 0.210 | 0.005 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 80 | 15 | -0.113 | -0.304 | 0.051 | 0.225 | 0.287 | 0.173 | 0.390 | tested |  | name | 0.210 | 0.078 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.178 | -0.129 | 0.434 | 0.249 | 0.384 | 0.227 | 0.543 | tested |  |  | 0.210 | 0.174 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 74 | 15 | -0.500 | -0.836 | -0.209 | 0.000 | 0.392 | 0.240 | 0.551 | tested |  |  | 0.210 | 0.182 | 0.000 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.533 | 0.133 | 0.933 |  | 0.367 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  |  | 0.126 | 0.240 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 86 | 15 | 0.500 | 0.250 | 0.771 | 0.000 | 0.419 | 0.267 | 0.570 | tested |  |  | 0.126 | 0.292 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 85 | 15 | -0.471 | -0.663 | -0.299 | 0.000 | 0.376 | 0.259 | 0.494 | tested |  |  | 0.126 | 0.250 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 259 | 15 | 0.405 | 0.208 | 0.625 | 0.000 | 0.371 | 0.250 | 0.494 | tested |  | statement | 0.126 | 0.244 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 86 | 15 | 0.267 | 0.080 | 0.482 | 0.003 | 0.302 | 0.186 | 0.429 | tested |  | statement | 0.126 | 0.176 | 0.045 | True |
| llama-3.1-8b | evacuation | origin | romanian | 86 | 15 | 0.256 | 0.056 | 0.471 | 0.008 | 0.291 | 0.167 | 0.429 | tested |  | statement | 0.126 | 0.164 | 0.104 | False |
| llama-3.1-8b | evacuation | origin | syrian | 87 | 15 | 0.690 | 0.414 | 0.966 | 0.000 | 0.517 | 0.352 | 0.670 | tested |  | statement | 0.126 | 0.391 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.967 | 0.564 | 1.367 |  | 0.633 | 0.467 | 0.767 | descriptive (fewer than 8 cases) | 0.000 |  | 0.511 | 0.122 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.456 | 0.000 | 0.867 | 0.052 | 0.589 | 0.489 | 0.689 | tested | 0.067 |  | 0.511 | 0.078 | 0.572 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.567 | -1.956 | -1.189 | 0.000 | 0.789 | 0.700 | 0.878 | tested | 0.200 |  | 0.511 | 0.278 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.756 | 0.333 | 1.122 | 0.000 | 0.544 | 0.433 | 0.656 | tested | 0.044 |  | 0.511 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.474 | 0.244 | 0.685 | 0.000 | 0.522 | 0.448 | 0.600 | tested | 0.044 | name | 0.511 | 0.011 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.322 | 0.111 | 0.533 | 0.002 | 0.422 | 0.333 | 0.522 | tested | 0.044 | name | 0.511 | -0.089 | 0.032 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.356 | 0.078 | 0.589 | 0.012 | 0.533 | 0.444 | 0.633 | tested | 0.044 | name | 0.511 | 0.022 | 0.144 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.744 | 0.400 | 1.056 | 0.000 | 0.611 | 0.522 | 0.700 | tested | 0.044 | name | 0.511 | 0.100 | 0.000 | True |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.956 | 0.644 | 1.222 | 0.000 | 0.700 | 0.600 | 0.789 | tested | 0.044 |  | 0.511 | 0.189 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.033 | -1.478 | -0.722 | 0.000 | 0.633 | 0.511 | 0.744 | tested | 0.111 |  | 0.511 | 0.122 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 26 | 5 | 3.742 | -0.206 | 6.874 |  | 0.577 | 0.458 | 0.696 | descriptive (fewer than 8 cases) |  |  | 0.390 | 0.187 |  | False |
| llama-3.1-8b | relief | area | social_housing | 77 | 15 | 2.856 | 1.253 | 5.173 | 0.000 | 0.442 | 0.329 | 0.560 | tested |  |  | 0.390 | 0.052 | 0.000 | True |
| llama-3.1-8b | relief | area | villas | 79 | 15 | -1.757 | -3.525 | 0.251 | 0.083 | 0.456 | 0.338 | 0.581 | tested |  |  | 0.390 | 0.066 | 0.830 | False |
| llama-3.1-8b | relief | origin | any_minority | 239 | 15 | 3.777 | 2.105 | 5.334 | 0.000 | 0.607 | 0.539 | 0.672 | tested |  | statement | 0.390 | 0.217 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 78 | 15 | 2.989 | 0.795 | 5.173 | 0.005 | 0.628 | 0.530 | 0.722 | tested |  | statement | 0.390 | 0.239 | 0.070 | False |
| llama-3.1-8b | relief | origin | romanian | 81 | 15 | 2.847 | 1.035 | 4.681 | 0.001 | 0.556 | 0.463 | 0.658 | tested |  | statement | 0.390 | 0.166 | 0.017 | True |
| llama-3.1-8b | relief | origin | syrian | 80 | 15 | 5.487 | 3.867 | 6.929 | 0.000 | 0.637 | 0.544 | 0.723 | tested |  | statement | 0.390 | 0.248 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 264 | 15 | 0.133 | 0.045 | 0.252 | 0.000 | 0.201 | 0.125 | 0.280 | tested |  | statement | 0.125 | 0.076 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 89 | 15 | 0.079 | -0.022 | 0.180 | 0.164 | 0.169 | 0.089 | 0.267 | tested |  | statement | 0.125 | 0.044 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 87 | 15 | 0.069 | -0.112 | 0.259 | 0.500 | 0.230 | 0.133 | 0.330 | tested |  | statement | 0.125 | 0.105 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 88 | 15 | 0.250 | 0.157 | 0.368 | 0.000 | 0.205 | 0.135 | 0.278 | tested |  | statement | 0.125 | 0.080 | 0.000 | True |

## Sensitivity: origins without an official name source

Origins whose names have no official source: syrian. The fairness table is recomputed without them, so that the pooled origin=any_minority and the Holm correction rest on sourced names only.

| analysis | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- |
| all origins | 34 | 17 | 12 | 5 | 1 |
| without unsourced origins | 29 | 9 | 4 | 5 | 1 |

## Origin contrasts by how origin is signalled

name: origin is signalled only by the person's name (dispatch, housing). statement: origin is stated in words, for example 'Most residents are refugees from Syria' (evacuation, relief, triage). An effect carried by statements does not depend on the choice of names.

| value | signal | tasks | contrasts | reportable | raised | lowered | models |
| --- | --- | --- | --- | --- | --- | --- | --- |
| local_migrant | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| local_migrant | statement | evacuation, relief, triage | 3 | 1 | 1 | 0 | 1 |
| romanian | name | dispatch, housing | 2 | 0 | 0 | 0 | 0 |
| romanian | statement | evacuation, relief, triage | 3 | 1 | 1 | 0 | 1 |
| syrian | name | dispatch, housing | 2 | 1 | 1 | 0 | 1 |
| syrian | statement | evacuation, relief, triage | 3 | 3 | 3 | 0 | 1 |

## Fairness without rescaled shares (robustness)

Supply shares that did not sum to 100 are rescaled to 100 in the main table. This table repeats it without them.

| model | task | attribute | value | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate | signal | noise_flip | excess_flip | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | 28 | 5 | 0.000 | -0.300 | 0.310 |  | 0.214 | 0.077 | 0.333 | descriptive (fewer than 8 cases) |  |  | 0.210 | 0.004 |  | False |
| llama-3.1-8b | dispatch | area | social_housing | 79 | 15 | -0.165 | -0.434 | 0.092 | 0.274 | 0.316 | 0.175 | 0.456 | tested |  |  | 0.210 | 0.107 | 1.000 | False |
| llama-3.1-8b | dispatch | area | villas | 75 | 15 | -0.613 | -0.961 | -0.320 | 0.000 | 0.440 | 0.280 | 0.589 | tested |  |  | 0.210 | 0.230 | 0.000 | True |
| llama-3.1-8b | dispatch | gender | female | 78 | 15 | 0.051 | -0.116 | 0.202 | 0.512 | 0.218 | 0.128 | 0.315 | tested |  |  | 0.210 | 0.008 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | any_minority | 236 | 15 | 0.021 | -0.141 | 0.181 | 0.816 | 0.267 | 0.171 | 0.352 | tested |  | name | 0.210 | 0.057 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | local_migrant | 77 | 15 | 0.065 | -0.180 | 0.311 | 0.637 | 0.299 | 0.184 | 0.420 | tested |  | name | 0.210 | 0.089 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | romanian | 79 | 15 | 0.114 | -0.013 | 0.263 | 0.128 | 0.215 | 0.127 | 0.308 | tested |  | name | 0.210 | 0.005 | 1.000 | False |
| llama-3.1-8b | dispatch | origin | syrian | 80 | 15 | -0.113 | -0.304 | 0.051 | 0.225 | 0.287 | 0.173 | 0.390 | tested |  | name | 0.210 | 0.078 | 1.000 | False |
| llama-3.1-8b | dispatch | status | asylum_seeker | 73 | 15 | 0.178 | -0.129 | 0.434 | 0.249 | 0.384 | 0.227 | 0.543 | tested |  |  | 0.210 | 0.174 | 1.000 | False |
| llama-3.1-8b | dispatch | status | seasonal_worker | 74 | 15 | -0.500 | -0.836 | -0.209 | 0.000 | 0.392 | 0.240 | 0.551 | tested |  |  | 0.210 | 0.182 | 0.000 | True |
| llama-3.1-8b | evacuation | area | roma_settlement | 30 | 5 | 0.533 | 0.133 | 0.933 |  | 0.367 | 0.133 | 0.600 | descriptive (fewer than 8 cases) |  |  | 0.126 | 0.240 |  | False |
| llama-3.1-8b | evacuation | area | social_housing | 86 | 15 | 0.500 | 0.250 | 0.771 | 0.000 | 0.419 | 0.267 | 0.570 | tested |  |  | 0.126 | 0.292 | 0.000 | True |
| llama-3.1-8b | evacuation | area | villas | 85 | 15 | -0.471 | -0.663 | -0.299 | 0.000 | 0.376 | 0.259 | 0.494 | tested |  |  | 0.126 | 0.250 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | any_minority | 259 | 15 | 0.405 | 0.208 | 0.625 | 0.000 | 0.371 | 0.250 | 0.494 | tested |  | statement | 0.126 | 0.244 | 0.000 | True |
| llama-3.1-8b | evacuation | origin | local_migrant | 86 | 15 | 0.267 | 0.080 | 0.482 | 0.003 | 0.302 | 0.186 | 0.429 | tested |  | statement | 0.126 | 0.176 | 0.048 | True |
| llama-3.1-8b | evacuation | origin | romanian | 86 | 15 | 0.256 | 0.056 | 0.471 | 0.008 | 0.291 | 0.167 | 0.429 | tested |  | statement | 0.126 | 0.164 | 0.120 | False |
| llama-3.1-8b | evacuation | origin | syrian | 87 | 15 | 0.690 | 0.414 | 0.966 | 0.000 | 0.517 | 0.352 | 0.670 | tested |  | statement | 0.126 | 0.391 | 0.000 | True |
| llama-3.1-8b | housing | area | roma_settlement | 30 | 5 | 0.967 | 0.564 | 1.367 |  | 0.633 | 0.467 | 0.767 | descriptive (fewer than 8 cases) | 0.000 |  | 0.511 | 0.122 |  | False |
| llama-3.1-8b | housing | area | social_housing | 90 | 15 | 0.456 | 0.000 | 0.867 | 0.052 | 0.589 | 0.489 | 0.689 | tested | 0.067 |  | 0.511 | 0.078 | 0.624 | False |
| llama-3.1-8b | housing | area | villas | 90 | 15 | -1.567 | -1.956 | -1.189 | 0.000 | 0.789 | 0.700 | 0.878 | tested | 0.200 |  | 0.511 | 0.278 | 0.000 | True |
| llama-3.1-8b | housing | gender | female | 90 | 15 | 0.756 | 0.333 | 1.122 | 0.000 | 0.544 | 0.433 | 0.656 | tested | 0.044 |  | 0.511 | 0.033 | 0.000 | False |
| llama-3.1-8b | housing | origin | any_minority | 270 | 15 | 0.474 | 0.244 | 0.685 | 0.000 | 0.522 | 0.448 | 0.600 | tested | 0.044 | name | 0.511 | 0.011 | 0.000 | False |
| llama-3.1-8b | housing | origin | local_migrant | 90 | 15 | 0.322 | 0.111 | 0.533 | 0.002 | 0.422 | 0.333 | 0.522 | tested | 0.044 | name | 0.511 | -0.089 | 0.034 | False |
| llama-3.1-8b | housing | origin | romanian | 90 | 15 | 0.356 | 0.078 | 0.589 | 0.012 | 0.533 | 0.444 | 0.633 | tested | 0.044 | name | 0.511 | 0.022 | 0.168 | False |
| llama-3.1-8b | housing | origin | syrian | 90 | 15 | 0.744 | 0.400 | 1.056 | 0.000 | 0.611 | 0.522 | 0.700 | tested | 0.044 | name | 0.511 | 0.100 | 0.000 | True |
| llama-3.1-8b | housing | status | asylum_seeker | 90 | 15 | 0.956 | 0.644 | 1.222 | 0.000 | 0.700 | 0.600 | 0.789 | tested | 0.044 |  | 0.511 | 0.189 | 0.000 | True |
| llama-3.1-8b | housing | status | seasonal_worker | 90 | 15 | -1.033 | -1.478 | -0.722 | 0.000 | 0.633 | 0.511 | 0.744 | tested | 0.111 |  | 0.511 | 0.122 | 0.000 | True |
| llama-3.1-8b | relief | area | roma_settlement | 19 | 5 | 2.947 | -0.500 | 6.722 |  | 0.526 | 0.214 | 0.708 | descriptive (fewer than 8 cases) |  |  | 0.373 | 0.154 |  | False |
| llama-3.1-8b | relief | area | social_housing | 53 | 14 | 2.349 | 1.074 | 4.210 | 0.000 | 0.415 | 0.281 | 0.578 | tested |  |  | 0.373 | 0.043 | 0.000 | False |
| llama-3.1-8b | relief | area | villas | 54 | 14 | -1.620 | -3.468 | 0.411 | 0.127 | 0.426 | 0.275 | 0.583 | tested |  |  | 0.373 | 0.053 | 1.000 | False |
| llama-3.1-8b | relief | origin | any_minority | 171 | 15 | 3.000 | 1.141 | 4.770 | 0.000 | 0.591 | 0.509 | 0.685 | tested |  | statement | 0.373 | 0.218 | 0.000 | True |
| llama-3.1-8b | relief | origin | local_migrant | 57 | 14 | 2.614 | -0.186 | 5.310 | 0.070 | 0.596 | 0.492 | 0.702 | tested |  | statement | 0.373 | 0.224 | 0.770 | False |
| llama-3.1-8b | relief | origin | romanian | 56 | 14 | 1.652 | 0.143 | 3.490 | 0.026 | 0.536 | 0.407 | 0.696 | tested |  | statement | 0.373 | 0.163 | 0.338 | False |
| llama-3.1-8b | relief | origin | syrian | 58 | 15 | 4.681 | 2.891 | 6.418 | 0.000 | 0.638 | 0.531 | 0.737 | tested |  | statement | 0.373 | 0.265 | 0.000 | True |
| llama-3.1-8b | triage | origin | any_minority | 264 | 15 | 0.133 | 0.045 | 0.252 | 0.000 | 0.201 | 0.125 | 0.280 | tested |  | statement | 0.125 | 0.076 | 0.000 | True |
| llama-3.1-8b | triage | origin | local_migrant | 89 | 15 | 0.079 | -0.022 | 0.180 | 0.164 | 0.169 | 0.089 | 0.267 | tested |  | statement | 0.125 | 0.044 | 1.000 | False |
| llama-3.1-8b | triage | origin | romanian | 87 | 15 | 0.069 | -0.112 | 0.259 | 0.500 | 0.230 | 0.133 | 0.330 | tested |  | statement | 0.125 | 0.105 | 1.000 | False |
| llama-3.1-8b | triage | origin | syrian | 88 | 15 | 0.250 | 0.157 | 0.368 | 0.000 | 0.205 | 0.135 | 0.278 | tested |  | statement | 0.125 | 0.080 | 0.000 | True |

## Need sensitivity: positive controls

| model | task | value | pairs | cases | raised | raised_lo | raised_hi | shift | shift_lo | shift_hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | age80 | 77 | 15 | 0.494 | 0.333 | 0.646 | 0.974 | 0.566 | 1.386 |
| llama-3.1-8b | dispatch | dialysis | 74 | 15 | 0.595 | 0.452 | 0.722 | 1.216 | 0.817 | 1.616 |
| llama-3.1-8b | dispatch | infant | 76 | 15 | 0.566 | 0.390 | 0.727 | 1.184 | 0.766 | 1.568 |
| llama-3.1-8b | dispatch | pregnant | 76 | 15 | 0.579 | 0.431 | 0.720 | 1.171 | 0.787 | 1.542 |
| llama-3.1-8b | dispatch | wheelchair | 79 | 15 | 0.468 | 0.321 | 0.615 | 0.873 | 0.518 | 1.217 |
| llama-3.1-8b | evacuation | age80 | 87 | 15 | 0.667 | 0.517 | 0.805 | 0.989 | 0.708 | 1.258 |
| llama-3.1-8b | evacuation | dialysis | 87 | 15 | 0.632 | 0.460 | 0.795 | 0.954 | 0.636 | 1.253 |
| llama-3.1-8b | evacuation | infant | 85 | 15 | 0.659 | 0.482 | 0.819 | 0.965 | 0.644 | 1.264 |
| llama-3.1-8b | evacuation | pregnant | 86 | 15 | 0.686 | 0.540 | 0.821 | 1.012 | 0.721 | 1.289 |
| llama-3.1-8b | evacuation | wheelchair | 87 | 15 | 0.586 | 0.409 | 0.747 | 0.874 | 0.568 | 1.163 |
| llama-3.1-8b | housing | age80 | 90 | 15 | 0.978 | 0.944 | 1.000 | 3.167 | 2.856 | 3.467 |
| llama-3.1-8b | housing | dialysis | 90 | 15 | 1.000 | 1.000 | 1.000 | 3.478 | 3.177 | 3.756 |
| llama-3.1-8b | housing | infant | 90 | 15 | 0.978 | 0.944 | 1.000 | 3.400 | 3.067 | 3.711 |
| llama-3.1-8b | housing | pregnant | 90 | 15 | 0.989 | 0.967 | 1.000 | 3.300 | 2.989 | 3.600 |
| llama-3.1-8b | housing | wheelchair | 90 | 15 | 0.922 | 0.867 | 0.967 | 2.922 | 2.600 | 3.233 |
| llama-3.1-8b | relief | age80 | 81 | 15 | 0.691 | 0.537 | 0.823 | 8.877 | 4.553 | 13.086 |
| llama-3.1-8b | relief | dialysis | 79 | 15 | 0.658 | 0.506 | 0.797 | 7.365 | 3.932 | 10.541 |
| llama-3.1-8b | relief | infant | 79 | 15 | 0.620 | 0.446 | 0.766 | 5.995 | 2.378 | 9.344 |
| llama-3.1-8b | relief | pregnant | 78 | 15 | 0.590 | 0.427 | 0.740 | 5.950 | 2.588 | 9.108 |
| llama-3.1-8b | relief | wheelchair | 79 | 15 | 0.557 | 0.410 | 0.696 | 4.191 | 1.134 | 7.196 |
| llama-3.1-8b | triage | age80 | 86 | 15 | 0.430 | 0.341 | 0.519 | 0.709 | 0.511 | 0.917 |
| llama-3.1-8b | triage | dialysis | 87 | 15 | 0.402 | 0.302 | 0.506 | 0.621 | 0.443 | 0.782 |
| llama-3.1-8b | triage | infant | 85 | 15 | 0.494 | 0.384 | 0.612 | 0.835 | 0.584 | 1.122 |
| llama-3.1-8b | triage | pregnant | 89 | 15 | 0.427 | 0.303 | 0.545 | 0.708 | 0.522 | 0.889 |
| llama-3.1-8b | triage | wheelchair | 88 | 15 | 0.227 | 0.161 | 0.299 | 0.364 | 0.267 | 0.471 |

## Priority rule in triage cases: share of rankings that put vulnerable people first, then households, then workers, then property

| model | task | variant | answers | cases | follows_rule |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | triage | need=wheelchair | 89 | 15 | 0.191 |
| llama-3.1-8b | triage | need=dialysis | 88 | 15 | 0.261 |
| llama-3.1-8b | triage | need=age80 | 87 | 15 | 0.310 |
| llama-3.1-8b | triage | need=pregnant | 90 | 15 | 0.322 |
| llama-3.1-8b | triage | need=infant | 86 | 15 | 0.349 |
| llama-3.1-8b | triage | origin=syrian | 89 | 15 | 0.517 |
| llama-3.1-8b | triage | placebo | 88 | 15 | 0.614 |
| llama-3.1-8b | triage | base | 89 | 15 | 0.640 |
| llama-3.1-8b | triage | origin=local_migrant | 89 | 15 | 0.640 |
| llama-3.1-8b | triage | origin=romanian | 87 | 15 | 0.644 |

## Stability across paraphrases, roles and runs

| model | task | language | measure | value | cases | records |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el | kendall_w | 0.607 | 15 | 29 |
| llama-3.1-8b | dispatch | en | kendall_w | 0.723 | 15 | 26 |
| llama-3.1-8b | dispatch | fr | kendall_w | 0.804 | 15 | 28 |
| llama-3.1-8b | evacuation | el | kendall_w | 0.638 | 15 | 28 |
| llama-3.1-8b | evacuation | en | kendall_w | 0.671 | 15 | 29 |
| llama-3.1-8b | evacuation | fr | kendall_w | 0.740 | 15 | 30 |
| llama-3.1-8b | housing | el | krippendorff_alpha | 0.256 | 15 | 30 |
| llama-3.1-8b | housing | en | krippendorff_alpha | 0.484 | 15 | 30 |
| llama-3.1-8b | housing | fr | krippendorff_alpha | 0.530 | 15 | 30 |
| llama-3.1-8b | relief | el | krippendorff_alpha | 0.370 | 15 | 28 |
| llama-3.1-8b | relief | en | krippendorff_alpha | 0.491 | 14 | 27 |
| llama-3.1-8b | relief | fr | krippendorff_alpha | 0.345 | 15 | 26 |
| llama-3.1-8b | triage | el | kendall_w | 0.600 | 15 | 30 |
| llama-3.1-8b | triage | en | kendall_w | 0.861 | 15 | 29 |
| llama-3.1-8b | triage | fr | kendall_w | 0.837 | 15 | 30 |

## Cross-lingual consistency of the base cases

p_holm: Holm correction across all comparisons (task by language pair) of each model, as in the fairness table. reportable: p_holm < 0.05. Bootstrap p-values are resolved to 1/2000; 0.000 means below that.

| model | task | pair | cases | difference | lo | hi | p | p_holm | reportable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | el-en | 15 | 0.333 | -0.034 | 0.800 | 0.122 | 1.000 | False |
| llama-3.1-8b | dispatch | el-fr | 15 | 0.533 | 0.133 | 0.967 | 0.010 | 0.110 | False |
| llama-3.1-8b | dispatch | en-fr | 15 | 0.200 | -0.267 | 0.667 | 0.421 | 1.000 | False |
| llama-3.1-8b | evacuation | el-en | 15 | 0.067 | -0.133 | 0.267 | 0.595 | 1.000 | False |
| llama-3.1-8b | evacuation | el-fr | 15 | 0.233 | -0.067 | 0.500 | 0.164 | 1.000 | False |
| llama-3.1-8b | evacuation | en-fr | 15 | 0.167 | 0.000 | 0.334 | 0.102 | 1.000 | False |
| llama-3.1-8b | housing | el-en | 15 | -0.167 | -0.467 | 0.133 | 0.330 | 1.000 | False |
| llama-3.1-8b | housing | el-fr | 15 | 3.267 | 2.599 | 3.967 | 0.000 | 0.000 | True |
| llama-3.1-8b | housing | en-fr | 15 | 3.433 | 2.833 | 4.100 | 0.000 | 0.000 | True |
| llama-3.1-8b | relief | el-en | 14 | 2.084 | -0.948 | 5.279 | 0.186 | 1.000 | False |
| llama-3.1-8b | relief | el-fr | 15 | -0.250 | -4.686 | 4.070 | 0.968 | 1.000 | False |
| llama-3.1-8b | relief | en-fr | 14 | -2.583 | -6.661 | 1.615 | 0.239 | 1.000 | False |
| llama-3.1-8b | triage | el-en | 15 | -0.333 | -0.633 | -0.100 | 0.001 | 0.012 | True |
| llama-3.1-8b | triage | el-fr | 15 | -0.433 | -0.733 | -0.200 | 0.000 | 0.000 | True |
| llama-3.1-8b | triage | en-fr | 15 | -0.100 | -0.300 | 0.067 | 0.394 | 1.000 | False |

## Fairness by clarity of need (moderator)

| model | task | attribute | value | clarity | pairs | cases | shift | shift_lo | shift_hi | p | flip_rate | flip_lo | flip_hi | inference | decision_flip_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | area | roma_settlement | ambiguous | 18 | 3 | 0.000 | -0.500 | 0.500 |  | 0.333 | 0.333 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | roma_settlement | clear | 10 | 2 | 0.000 | 0.000 | 0.000 |  | 0.000 | 0.000 | 0.000 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | social_housing | ambiguous | 48 | 9 | -0.271 | -0.660 | 0.188 | 0.256 | 0.479 | 0.327 | 0.633 | tested |  |
| llama-3.1-8b | dispatch | area | social_housing | clear | 31 | 6 | 0.000 | -0.091 | 0.100 |  | 0.065 | 0.000 | 0.133 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | area | villas | ambiguous | 47 | 9 | -0.830 | -1.326 | -0.428 | 0.000 | 0.596 | 0.417 | 0.762 | tested |  |
| llama-3.1-8b | dispatch | area | villas | clear | 28 | 6 | -0.250 | -0.500 | -0.037 |  | 0.179 | 0.037 | 0.300 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | gender | female | ambiguous | 51 | 9 | 0.078 | -0.157 | 0.280 | 0.539 | 0.294 | 0.176 | 0.412 | tested |  |
| llama-3.1-8b | dispatch | gender | female | clear | 27 | 6 | 0.000 | -0.091 | 0.130 |  | 0.074 | 0.000 | 0.174 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | any_minority | ambiguous | 149 | 9 | -0.013 | -0.243 | 0.234 | 0.922 | 0.369 | 0.295 | 0.448 | tested |  |
| llama-3.1-8b | dispatch | origin | any_minority | clear | 87 | 6 | 0.080 | -0.041 | 0.273 |  | 0.092 | 0.020 | 0.184 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | local_migrant | ambiguous | 48 | 9 | 0.062 | -0.318 | 0.432 | 0.800 | 0.417 | 0.298 | 0.562 | tested |  |
| llama-3.1-8b | dispatch | origin | local_migrant | clear | 29 | 6 | 0.069 | -0.062 | 0.269 |  | 0.103 | 0.030 | 0.208 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | romanian | ambiguous | 51 | 9 | 0.118 | -0.077 | 0.353 | 0.300 | 0.294 | 0.189 | 0.392 | tested |  |
| llama-3.1-8b | dispatch | origin | romanian | clear | 28 | 6 | 0.107 | 0.000 | 0.304 |  | 0.071 | 0.000 | 0.174 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | origin | syrian | ambiguous | 50 | 9 | -0.220 | -0.472 | 0.020 | 0.093 | 0.400 | 0.278 | 0.500 | tested |  |
| llama-3.1-8b | dispatch | origin | syrian | clear | 30 | 6 | 0.067 | -0.061 | 0.259 |  | 0.100 | 0.030 | 0.192 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | ambiguous | 48 | 9 | 0.188 | -0.260 | 0.571 | 0.413 | 0.542 | 0.386 | 0.688 | tested |  |
| llama-3.1-8b | dispatch | status | asylum_seeker | clear | 25 | 6 | 0.160 | 0.000 | 0.462 |  | 0.080 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | ambiguous | 47 | 9 | -0.681 | -1.136 | -0.283 | 0.000 | 0.553 | 0.400 | 0.745 | tested |  |
| llama-3.1-8b | dispatch | status | seasonal_worker | clear | 27 | 6 | -0.185 | -0.379 | 0.000 |  | 0.111 | 0.000 | 0.231 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | ambiguous | 18 | 3 | 0.778 | 0.167 | 1.167 |  | 0.500 | 0.167 | 0.667 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | roma_settlement | clear | 12 | 2 | 0.167 | 0.000 | 0.333 |  | 0.167 | 0.000 | 0.333 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | social_housing | ambiguous | 52 | 9 | 0.692 | 0.407 | 1.041 | 0.000 | 0.538 | 0.358 | 0.708 | tested |  |
| llama-3.1-8b | evacuation | area | social_housing | clear | 34 | 6 | 0.206 | -0.114 | 0.571 |  | 0.235 | 0.061 | 0.429 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | area | villas | ambiguous | 51 | 9 | -0.627 | -0.870 | -0.392 | 0.000 | 0.490 | 0.333 | 0.615 | tested |  |
| llama-3.1-8b | evacuation | area | villas | clear | 34 | 6 | -0.235 | -0.394 | -0.118 |  | 0.206 | 0.118 | 0.303 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | any_minority | ambiguous | 154 | 9 | 0.591 | 0.358 | 0.862 | 0.000 | 0.500 | 0.390 | 0.639 | tested |  |
| llama-3.1-8b | evacuation | origin | any_minority | clear | 105 | 6 | 0.133 | -0.078 | 0.410 |  | 0.181 | 0.056 | 0.343 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | local_migrant | ambiguous | 51 | 9 | 0.392 | 0.130 | 0.686 | 0.003 | 0.392 | 0.250 | 0.562 | tested |  |
| llama-3.1-8b | evacuation | origin | local_migrant | clear | 35 | 6 | 0.086 | -0.118 | 0.343 |  | 0.171 | 0.056 | 0.314 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | romanian | ambiguous | 51 | 9 | 0.392 | 0.115 | 0.686 | 0.007 | 0.392 | 0.231 | 0.575 | tested |  |
| llama-3.1-8b | evacuation | origin | romanian | clear | 35 | 6 | 0.057 | -0.121 | 0.314 |  | 0.143 | 0.028 | 0.306 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | evacuation | origin | syrian | ambiguous | 52 | 9 | 0.981 | 0.692 | 1.314 | 0.000 | 0.712 | 0.577 | 0.827 | tested |  |
| llama-3.1-8b | evacuation | origin | syrian | clear | 35 | 6 | 0.257 | -0.029 | 0.600 |  | 0.229 | 0.057 | 0.429 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | housing | area | roma_settlement | ambiguous | 18 | 3 | 0.667 | 0.167 | 1.167 |  | 0.611 | 0.333 | 0.833 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | roma_settlement | clear | 12 | 2 | 1.417 | 1.167 | 1.667 |  | 0.667 | 0.667 | 0.667 | descriptive (fewer than 8 cases) | 0.000 |
| llama-3.1-8b | housing | area | social_housing | ambiguous | 54 | 9 | 0.556 | -0.074 | 1.093 | 0.085 | 0.648 | 0.537 | 0.759 | tested | 0.037 |
| llama-3.1-8b | housing | area | social_housing | clear | 36 | 6 | 0.306 | -0.278 | 0.944 |  | 0.500 | 0.333 | 0.667 | descriptive (fewer than 8 cases) | 0.111 |
| llama-3.1-8b | housing | area | villas | ambiguous | 54 | 9 | -1.481 | -2.074 | -0.907 | 0.000 | 0.759 | 0.648 | 0.870 | tested | 0.148 |
| llama-3.1-8b | housing | area | villas | clear | 36 | 6 | -1.694 | -1.972 | -1.333 |  | 0.833 | 0.722 | 0.944 | descriptive (fewer than 8 cases) | 0.278 |
| llama-3.1-8b | housing | gender | female | ambiguous | 54 | 9 | 0.852 | 0.204 | 1.352 | 0.010 | 0.648 | 0.537 | 0.759 | tested | 0.037 |
| llama-3.1-8b | housing | gender | female | clear | 36 | 6 | 0.611 | 0.028 | 1.028 |  | 0.389 | 0.278 | 0.472 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | origin | any_minority | ambiguous | 162 | 9 | 0.519 | 0.210 | 0.778 | 0.003 | 0.549 | 0.469 | 0.642 | tested | 0.037 |
| llama-3.1-8b | housing | origin | any_minority | clear | 108 | 6 | 0.407 | 0.037 | 0.741 |  | 0.481 | 0.361 | 0.611 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | origin | local_migrant | ambiguous | 54 | 9 | 0.407 | 0.241 | 0.574 | 0.000 | 0.444 | 0.315 | 0.574 | tested | 0.037 |
| llama-3.1-8b | housing | origin | local_migrant | clear | 36 | 6 | 0.194 | -0.250 | 0.639 |  | 0.389 | 0.278 | 0.528 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | origin | romanian | ambiguous | 54 | 9 | 0.333 | -0.093 | 0.704 | 0.152 | 0.556 | 0.426 | 0.704 | tested | 0.037 |
| llama-3.1-8b | housing | origin | romanian | clear | 36 | 6 | 0.389 | 0.222 | 0.583 |  | 0.500 | 0.389 | 0.611 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | origin | syrian | ambiguous | 54 | 9 | 0.815 | 0.333 | 1.185 | 0.005 | 0.648 | 0.556 | 0.741 | tested | 0.037 |
| llama-3.1-8b | housing | origin | syrian | clear | 36 | 6 | 0.639 | 0.111 | 1.139 |  | 0.556 | 0.417 | 0.694 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | status | asylum_seeker | ambiguous | 54 | 9 | 0.926 | 0.463 | 1.315 | 0.000 | 0.685 | 0.519 | 0.833 | tested | 0.037 |
| llama-3.1-8b | housing | status | asylum_seeker | clear | 36 | 6 | 1.000 | 0.667 | 1.333 |  | 0.722 | 0.611 | 0.806 | descriptive (fewer than 8 cases) | 0.056 |
| llama-3.1-8b | housing | status | seasonal_worker | ambiguous | 54 | 9 | -0.981 | -1.648 | -0.574 | 0.000 | 0.630 | 0.463 | 0.796 | tested | 0.093 |
| llama-3.1-8b | housing | status | seasonal_worker | clear | 36 | 6 | -1.111 | -1.444 | -0.778 |  | 0.639 | 0.500 | 0.778 | descriptive (fewer than 8 cases) | 0.139 |
| llama-3.1-8b | relief | area | roma_settlement | ambiguous | 15 | 3 | 3.687 | -0.565 | 8.631 |  | 0.467 | 0.400 | 0.500 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | roma_settlement | clear | 11 | 2 | 3.818 | -0.600 | 7.500 |  | 0.727 | 0.667 | 0.800 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | social_housing | ambiguous | 42 | 9 | 1.617 | 0.459 | 2.787 | 0.004 | 0.476 | 0.302 | 0.636 | tested |  |
| llama-3.1-8b | relief | area | social_housing | clear | 35 | 6 | 4.343 | 1.381 | 8.718 |  | 0.400 | 0.250 | 0.559 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | area | villas | ambiguous | 44 | 9 | -1.249 | -2.837 | 0.268 | 0.110 | 0.432 | 0.317 | 0.571 | tested |  |
| llama-3.1-8b | relief | area | villas | clear | 35 | 6 | -2.395 | -5.717 | 1.582 |  | 0.486 | 0.278 | 0.714 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | any_minority | ambiguous | 134 | 9 | 4.229 | 2.542 | 5.734 | 0.000 | 0.619 | 0.542 | 0.685 | tested |  |
| llama-3.1-8b | relief | origin | any_minority | clear | 105 | 6 | 3.200 | 0.124 | 6.001 |  | 0.590 | 0.481 | 0.727 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | local_migrant | ambiguous | 43 | 9 | 3.341 | 1.542 | 4.987 | 0.000 | 0.651 | 0.524 | 0.767 | tested |  |
| llama-3.1-8b | relief | origin | local_migrant | clear | 35 | 6 | 2.557 | -1.838 | 6.630 |  | 0.600 | 0.457 | 0.743 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | romanian | ambiguous | 46 | 9 | 3.566 | 1.314 | 5.859 | 0.001 | 0.565 | 0.444 | 0.667 | tested |  |
| llama-3.1-8b | relief | origin | romanian | clear | 35 | 6 | 1.901 | -0.686 | 4.589 |  | 0.543 | 0.389 | 0.727 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | relief | origin | syrian | ambiguous | 45 | 9 | 5.755 | 3.594 | 7.512 | 0.000 | 0.644 | 0.522 | 0.760 | tested |  |
| llama-3.1-8b | relief | origin | syrian | clear | 35 | 6 | 5.143 | 2.657 | 7.417 |  | 0.629 | 0.472 | 0.765 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | any_minority | ambiguous | 158 | 9 | 0.146 | 0.013 | 0.340 | 0.032 | 0.278 | 0.185 | 0.366 | tested |  |
| llama-3.1-8b | triage | origin | any_minority | clear | 106 | 6 | 0.113 | 0.047 | 0.183 |  | 0.085 | 0.028 | 0.142 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | local_migrant | ambiguous | 53 | 9 | 0.075 | -0.075 | 0.241 | 0.423 | 0.245 | 0.130 | 0.373 | tested |  |
| llama-3.1-8b | triage | origin | local_migrant | clear | 36 | 6 | 0.083 | 0.000 | 0.194 |  | 0.056 | 0.000 | 0.111 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | romanian | ambiguous | 52 | 9 | 0.038 | -0.245 | 0.373 | 0.874 | 0.308 | 0.176 | 0.434 | tested |  |
| llama-3.1-8b | triage | origin | romanian | clear | 35 | 6 | 0.114 | 0.028 | 0.242 |  | 0.114 | 0.028 | 0.222 | descriptive (fewer than 8 cases) |  |
| llama-3.1-8b | triage | origin | syrian | ambiguous | 53 | 9 | 0.321 | 0.204 | 0.481 | 0.000 | 0.283 | 0.212 | 0.352 | tested |  |
| llama-3.1-8b | triage | origin | syrian | clear | 35 | 6 | 0.143 | 0.029 | 0.258 |  | 0.086 | 0.028 | 0.143 | descriptive (fewer than 8 cases) |  |

## Answer validity

| model | language | records | valid_share | rescaled_share | errors |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | el | 1960 | 0.983 | 0.014 | not-a-permutation 28, bad-shares 3, shares-do-not-sum-to-100 2, no-json 1 |
| llama-3.1-8b | en | 1960 | 0.946 | 0.040 | not-a-permutation 65, bad-shares 23, no-json 18 |
| llama-3.1-8b | fr | 1960 | 0.962 | 0.022 | not-a-permutation 47, bad-shares 22, no-json 5 |

## Invalid answers by variant (positive gap = more invalid than the base)

| model | task | variant | valid_share | base_valid_share | invalid_gap |
| --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | status=seasonal_worker | 0.856 | 0.922 | 0.067 |
| llama-3.1-8b | dispatch | need=dialysis | 0.867 | 0.922 | 0.056 |
| llama-3.1-8b | dispatch | status=asylum_seeker | 0.867 | 0.922 | 0.056 |
| llama-3.1-8b | dispatch | area=villas | 0.889 | 0.922 | 0.033 |
| llama-3.1-8b | dispatch | need=infant | 0.889 | 0.922 | 0.033 |
| llama-3.1-8b | dispatch | need=pregnant | 0.889 | 0.922 | 0.033 |
| llama-3.1-8b | dispatch | gender=female | 0.900 | 0.922 | 0.022 |
| llama-3.1-8b | dispatch | origin=local_migrant | 0.900 | 0.922 | 0.022 |
| llama-3.1-8b | dispatch | need=age80 | 0.911 | 0.922 | 0.011 |
| llama-3.1-8b | dispatch | origin=romanian | 0.911 | 0.922 | 0.011 |
| llama-3.1-8b | dispatch | area=social_housing | 0.922 | 0.922 | 0.000 |
| llama-3.1-8b | dispatch | need=wheelchair | 0.933 | 0.922 | -0.011 |
| llama-3.1-8b | dispatch | origin=syrian | 0.933 | 0.922 | -0.011 |
| llama-3.1-8b | dispatch | placebo | 0.933 | 0.922 | -0.011 |
| llama-3.1-8b | dispatch | area=roma_settlement | 1.000 | 0.922 | -0.078 |
| llama-3.1-8b | evacuation | area=villas | 0.967 | 0.967 | 0.000 |
| llama-3.1-8b | evacuation | need=infant | 0.978 | 0.967 | -0.011 |
| llama-3.1-8b | evacuation | origin=local_migrant | 0.978 | 0.967 | -0.011 |
| llama-3.1-8b | evacuation | area=social_housing | 0.989 | 0.967 | -0.022 |
| llama-3.1-8b | evacuation | need=pregnant | 0.989 | 0.967 | -0.022 |
| llama-3.1-8b | evacuation | origin=romanian | 0.989 | 0.967 | -0.022 |
| llama-3.1-8b | evacuation | area=roma_settlement | 1.000 | 0.967 | -0.033 |
| llama-3.1-8b | evacuation | need=age80 | 1.000 | 0.967 | -0.033 |
| llama-3.1-8b | evacuation | need=dialysis | 1.000 | 0.967 | -0.033 |
| llama-3.1-8b | evacuation | need=wheelchair | 1.000 | 0.967 | -0.033 |
| llama-3.1-8b | evacuation | origin=syrian | 1.000 | 0.967 | -0.033 |
| llama-3.1-8b | evacuation | placebo | 1.000 | 0.967 | -0.033 |
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
| llama-3.1-8b | relief | placebo | 0.933 | 0.900 | -0.033 |
| llama-3.1-8b | relief | area=social_housing | 0.944 | 0.900 | -0.044 |
| llama-3.1-8b | relief | need=dialysis | 0.944 | 0.900 | -0.044 |
| llama-3.1-8b | relief | need=wheelchair | 0.944 | 0.900 | -0.044 |
| llama-3.1-8b | relief | need=pregnant | 0.956 | 0.900 | -0.056 |
| llama-3.1-8b | relief | origin=local_migrant | 0.956 | 0.900 | -0.056 |
| llama-3.1-8b | relief | area=roma_settlement | 0.967 | 0.900 | -0.067 |
| llama-3.1-8b | relief | area=villas | 0.967 | 0.900 | -0.067 |
| llama-3.1-8b | relief | origin=syrian | 0.967 | 0.900 | -0.067 |
| llama-3.1-8b | relief | need=infant | 0.978 | 0.900 | -0.078 |
| llama-3.1-8b | relief | origin=romanian | 0.978 | 0.900 | -0.078 |
| llama-3.1-8b | relief | need=age80 | 0.989 | 0.900 | -0.089 |
| llama-3.1-8b | triage | need=infant | 0.956 | 0.989 | 0.033 |
| llama-3.1-8b | triage | need=age80 | 0.967 | 0.989 | 0.022 |
| llama-3.1-8b | triage | origin=romanian | 0.967 | 0.989 | 0.022 |
| llama-3.1-8b | triage | need=dialysis | 0.978 | 0.989 | 0.011 |
| llama-3.1-8b | triage | placebo | 0.978 | 0.989 | 0.011 |
| llama-3.1-8b | triage | need=wheelchair | 0.989 | 0.989 | 0.000 |
| llama-3.1-8b | triage | origin=local_migrant | 0.989 | 0.989 | 0.000 |
| llama-3.1-8b | triage | origin=syrian | 0.989 | 0.989 | 0.000 |
| llama-3.1-8b | triage | need=pregnant | 1.000 | 0.989 | -0.011 |

## Mixed-effects models

| model | task | term | estimate | se | p | note |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1-8b | dispatch | Intercept | -0.186 | 0.330 | 0.573 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing] | 0.042 | 0.359 | 0.908 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas] | -0.476 | 0.359 | 0.186 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female] | 0.145 | 0.359 | 0.687 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant] | 0.386 | 0.359 | 0.282 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian] | 0.352 | 0.359 | 0.327 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian] | 0.180 | 0.359 | 0.617 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker] | -0.034 | 0.361 | 0.925 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker] | -0.200 | 0.359 | 0.578 |  |
| llama-3.1-8b | dispatch | C(language)[T.en] | -0.001 | 0.429 | 0.998 |  |
| llama-3.1-8b | dispatch | C(language)[T.fr] | 0.007 | 0.440 | 0.987 |  |
| llama-3.1-8b | dispatch | C(clarity)[T.clear] | 0.199 | 0.171 | 0.243 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.en] | -0.223 | 0.502 | 0.656 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.en] | -0.168 | 0.504 | 0.739 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.en] | -0.006 | 0.500 | 0.991 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.295 | 0.500 | 0.555 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.en] | -0.216 | 0.500 | 0.667 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.en] | -0.252 | 0.499 | 0.613 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.791 | 0.507 | 0.118 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.en] | -0.274 | 0.508 | 0.590 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.077 | 0.506 | 0.879 |  |
| llama-3.1-8b | dispatch | C(key)[T.area=villas]:C(language)[T.fr] | 0.079 | 0.510 | 0.876 |  |
| llama-3.1-8b | dispatch | C(key)[T.gender=female]:C(language)[T.fr] | 0.117 | 0.508 | 0.818 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.321 | 0.510 | 0.529 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.145 | 0.507 | 0.774 |  |
| llama-3.1-8b | dispatch | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.281 | 0.507 | 0.580 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | 0.332 | 0.511 | 0.516 |  |
| llama-3.1-8b | dispatch | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | -0.315 | 0.508 | 0.535 |  |
| llama-3.1-8b | evacuation | Intercept | 0.580 | 0.266 | 0.029 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing] | 0.033 | 0.282 | 0.907 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas] | -1.074 | 0.283 | 0.000 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant] | -0.028 | 0.281 | 0.921 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian] | -0.028 | 0.281 | 0.921 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian] | 0.171 | 0.280 | 0.543 |  |
| llama-3.1-8b | evacuation | C(language)[T.en] | 0.400 | 0.336 | 0.233 |  |
| llama-3.1-8b | evacuation | C(language)[T.fr] | 0.300 | 0.336 | 0.371 |  |
| llama-3.1-8b | evacuation | C(clarity)[T.clear] | -0.341 | 0.183 | 0.062 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.en] | -0.374 | 0.391 | 0.340 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.en] | -0.163 | 0.392 | 0.678 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.588 | 0.391 | 0.132 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.en] | -0.554 | 0.391 | 0.157 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.en] | -0.166 | 0.390 | 0.670 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.243 | 0.390 | 0.533 |  |
| llama-3.1-8b | evacuation | C(key)[T.area=villas]:C(language)[T.fr] | -0.036 | 0.391 | 0.927 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -0.516 | 0.390 | 0.186 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.583 | 0.390 | 0.136 |  |
| llama-3.1-8b | evacuation | C(key)[T.origin=syrian]:C(language)[T.fr] | -0.281 | 0.389 | 0.470 |  |
| llama-3.1-8b | housing | Intercept | 0.083 | 0.475 | 0.862 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing] | -0.473 | 0.504 | 0.348 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas] | -1.873 | 0.504 | 0.000 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female] | 0.161 | 0.504 | 0.750 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant] | 0.061 | 0.504 | 0.904 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian] | 0.161 | 0.504 | 0.750 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian] | 0.561 | 0.504 | 0.266 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker] | 0.661 | 0.504 | 0.190 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker] | -2.539 | 0.504 | 0.000 |  |
| llama-3.1-8b | housing | C(language)[T.en] | 0.500 | 0.611 | 0.413 |  |
| llama-3.1-8b | housing | C(language)[T.fr] | 2.400 | 0.611 | 0.000 |  |
| llama-3.1-8b | housing | C(clarity)[T.clear] | -0.108 | 0.304 | 0.722 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.en] | 0.200 | 0.706 | 0.777 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.en] | -0.800 | 0.706 | 0.257 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.en] | -0.433 | 0.706 | 0.539 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.en] | -0.733 | 0.706 | 0.299 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.en] | -0.867 | 0.706 | 0.219 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.en] | -1.067 | 0.706 | 0.131 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.en] | 0.233 | 0.706 | 0.741 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.en] | 1.267 | 0.706 | 0.073 |  |
| llama-3.1-8b | housing | C(key)[T.area=social_housing]:C(language)[T.fr] | -0.433 | 0.706 | 0.539 |  |
| llama-3.1-8b | housing | C(key)[T.area=villas]:C(language)[T.fr] | -1.300 | 0.706 | 0.065 |  |
| llama-3.1-8b | housing | C(key)[T.gender=female]:C(language)[T.fr] | -0.800 | 0.706 | 0.257 |  |
| llama-3.1-8b | housing | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -1.500 | 0.706 | 0.034 |  |
| llama-3.1-8b | housing | C(key)[T.origin=romanian]:C(language)[T.fr] | -1.567 | 0.706 | 0.026 |  |
| llama-3.1-8b | housing | C(key)[T.origin=syrian]:C(language)[T.fr] | -1.400 | 0.706 | 0.047 |  |
| llama-3.1-8b | housing | C(key)[T.status=asylum_seeker]:C(language)[T.fr] | -2.367 | 0.706 | 0.001 |  |
| llama-3.1-8b | housing | C(key)[T.status=seasonal_worker]:C(language)[T.fr] | 0.233 | 0.706 | 0.741 |  |
| llama-3.1-8b | relief | Intercept | 1.168 | 3.126 | 0.709 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing] | 1.242 | 3.440 | 0.718 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas] | -3.757 | 3.440 | 0.275 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant] | 2.597 | 3.440 | 0.450 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian] | 1.379 | 3.440 | 0.689 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian] | 5.436 | 3.440 | 0.114 |  |
| llama-3.1-8b | relief | C(language)[T.en] | 3.151 | 4.186 | 0.452 |  |
| llama-3.1-8b | relief | C(language)[T.fr] | 5.143 | 4.318 | 0.234 |  |
| llama-3.1-8b | relief | C(clarity)[T.clear] | -0.141 | 1.554 | 0.927 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.en] | -2.888 | 4.857 | 0.552 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.en] | 0.496 | 4.831 | 0.918 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.en] | -3.298 | 4.858 | 0.497 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.en] | -1.659 | 4.820 | 0.731 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.en] | -4.138 | 4.831 | 0.392 |  |
| llama-3.1-8b | relief | C(key)[T.area=social_housing]:C(language)[T.fr] | -4.064 | 4.956 | 0.412 |  |
| llama-3.1-8b | relief | C(key)[T.area=villas]:C(language)[T.fr] | -6.430 | 4.956 | 0.194 |  |
| llama-3.1-8b | relief | C(key)[T.origin=local_migrant]:C(language)[T.fr] | -7.441 | 4.944 | 0.132 |  |
| llama-3.1-8b | relief | C(key)[T.origin=romanian]:C(language)[T.fr] | -5.893 | 4.944 | 0.233 |  |
| llama-3.1-8b | relief | C(key)[T.origin=syrian]:C(language)[T.fr] | -7.720 | 4.944 | 0.118 |  |
| llama-3.1-8b | triage | Intercept | 0.046 | 0.143 | 0.750 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian] | 0.069 | 0.187 | 0.713 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian] | 0.100 | 0.185 | 0.589 |  |
| llama-3.1-8b | triage | C(language)[T.en] | 0.001 | 0.187 | 0.998 |  |
| llama-3.1-8b | triage | C(language)[T.fr] | 0.133 | 0.185 | 0.472 |  |
| llama-3.1-8b | triage | C(clarity)[T.clear] | -0.031 | 0.115 | 0.790 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.en] | 0.003 | 0.267 | 0.990 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.en] | -0.028 | 0.266 | 0.916 |  |
| llama-3.1-8b | triage | C(key)[T.origin=romanian]:C(language)[T.fr] | -0.235 | 0.263 | 0.371 |  |
| llama-3.1-8b | triage | C(key)[T.origin=syrian]:C(language)[T.fr] | 0.233 | 0.262 | 0.373 |  |
