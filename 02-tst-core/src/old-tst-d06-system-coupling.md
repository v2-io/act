---
label: D-06
type: Definition
name: System Coupling
dependencies: []
revision: 0.2
---

# D-06 Definition: System Coupling

The probability that a change to one module will require a change to another:

$$
\text{coupling}(\text{module}_i, \text{module}_j) = P(\text{change}(\text{module}_j) \mid \text{change}(\text{module}_i))
$$