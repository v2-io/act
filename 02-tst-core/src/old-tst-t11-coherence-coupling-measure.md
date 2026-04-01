---
label: T-11
type: Theorem
subtype: Measurement
name: Coherence-Coupling Measure Principle
dependencies:
  - "[[t10-change-proximity.md|T-10]]"
  - "[[d06-system-coupling.md|D-06]]"
  - "[[d07-system-coherence.md|D-07]]"
older-tag: FP-010
revision: 0.2
---

# T-11 Theorem (Measurement): Coherence-Coupling Measure Principle

**Statement:** Software coherence and loose coupling can be objectively measured by the expected proximity of changes for typical features.

$$
\text{System quality score: } \text{quality} = \frac{\sum_i \text{coherence}(\text{module}_i)}{\sum_{i,j} \text{coupling}(\text{module}_i, \text{module}_j)}
$$
**Justification:**

- **Empirical:** High-quality systems show clustered changes within modules
- **Theoretical:** Minimizing cross-module changes minimizes coordination costs
- **Practical:** This provides the first measurable definition of these classic concepts

**Critical Insight:** This principle finally provides a quantitative, measurable definition for coupling and cohesion based on actual change patterns rather than static code analysis. We can now empirically measure these properties using git history.

**Boundary Conditions:**

- **Young Systems:** Need sufficient change history for meaningful measurements
- **Major Refactors:** Can reset the measurement baseline
- **Different Change Types:** Bug fixes vs features may have different patterns

## Discussion: Finally Measurable

After decades of qualitative descriptions, we can now measure coupling and cohesion:

- Mine git history for change patterns
- Calculate actual coupling coefficients between modules
- Track coherence trends over time
- Predict which modules will change together

**Organizational Implications:** Per Conway's Law, this measurement also reflects organizational structure. High coupling between modules owned by different teams predicts communication overhead and coordination challenges.