---
label: T-08
type: Theorem
subtype: Derived
name: Domain Tracking Principle
dependencies:
  - "[[t07-conceptual-alignment.md|T-07]]"
older-tag: FP-006
revision: 0.2
---

# T-08 Theorem (Derived): Domain Tracking

**Statement:** Code must continuously evolve to reflect the current best understanding of the domain, with refactoring priority proportional to semantic drift.

$$
\text{refactor\_priority}(\text{code}) = \text{semantic\_distance}(\text{code\_model}, \text{current\_domain\_model}) \times \text{usage\_frequency}
$$

$$
\text{domain\_model}(t) = \text{domain\_model}(t-1) + \text{market\_learning} + \text{user\_feedback} + \text{pivot\_decisions}
$$

$$
\text{convergence\_score} = \frac{|\text{domain\_terms} \cap \text{code\_terms}|}{|\text{domain\_terms}|}
$$
**Justification:**

- **Comprehension:** Code using current domain language is understood fastest
- **Market Fit:** Clear domain understanding correlates with product-market fit
- **Team Alignment:** Shared vocabulary reduces communication overhead
- **Living Documentation:** Code becomes the authoritative domain model

**Critical Insight:** The most important refactors are vocabulary and concept alignments, not technical improvements. As domain understanding evolves (through market discovery, user feedback, pivots), the code must track these changes.

**Boundary Conditions:**

- **Exploration Phase:** When domain is being discovered, stability is low
- **Mature Domains:** Well-understood domains change slowly
- **Technical Domains:** Some code has no domain vocabulary (kernels, compilers)

## Discussion: Refactoring Priority

1. Fix terminology mismatches in high-traffic code
2. Unify scattered concepts now understood as one
3. Split conflated concepts now understood as distinct
4. Update boundaries to match new domain boundaries
5. Technical improvements (only after domain alignment)

**The Learning Loop:**

$$
\text{Unclear domain} \to \text{Exploratory code} \to \text{User feedback} \to
$$

$$
\text{Clearer domain} \to \text{Refactor to align} \to \text{Better code} \to
$$

$$
\text{Faster iteration} \to \text{More feedback} \to \text{Clearer domain...}
$$
**Strategic Test Timing:** Write tests when refactoring for domain alignment, not before domain understanding stabilizes:

- Tests protect behavior during vocabulary updates
- Tests document current domain understanding
- Premature tests lock in wrong models