---
label: T-12
type: Theorem
subtype: Empirical
name: Comprehension-Proximity Correlation Principle
dependencies:
  - "[[t05-dual-optimization.md|T-05]]"
  - "[[t10-change-proximity.md|T-10]]"
older-tag: FP-011
revision: 0.2
---

# T-12 Theorem (Empirical): Comprehension-Proximity Correlation Principle

**Statement:** Time-to-comprehension is inversely proportional to the expected proximity of relevant code for understanding a feature.

$$
\text{time}_{\text{comprehension}}(F) \propto \frac{1}{\text{proximity}(\text{relevant\_code}(F))}
$$
Where relevant_code includes:
- Direct implementation
- Dependencies
- Configuration
- Tests
- Documentation

**Justification:**

- **Cognitive Science:** Working memory limitations mean distant information is harder to integrate
- **Empirical:** Eye-tracking studies show comprehension time increases with navigation
- **Practical:** Developers report understanding clustered code faster

**Boundary Conditions:**

- **Familiarity Bonus:** Well-known code has effectively infinite proximity
- **Documentation Quality:** Good docs can create virtual proximity
- **Tool Assistance:** IDEs with good navigation can improve effective proximity

## Discussion: The Mental Model Challenge

Building a mental model requires holding multiple pieces of information simultaneously. When code is scattered, the mental model must be larger and more complex, increasing comprehension time exponentially rather than linearly.

**Documentation as Proximity:** Well-written documentation can create "virtual proximity" by bringing distant concepts together in one place. This is why architectural decision records and design docs are valuable—they increase the effective proximity of distributed decisions.