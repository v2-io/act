---
label: T-07
type: Theorem
subtype: Derived
name: Conceptual Alignment Principle
dependencies:
  - "[[t01-time-optimality.md|T-01]]"
older-tag: FP-005
revision: 0.2
---

# T-07 Theorem (Derived): Conceptual Alignment

**Statement:** Code architecture must align with conceptual architecture, such that the probability of coordination between changes equals the probability of conceptual overlap between features.

$$
P(\text{coordination\_required} \mid \Delta A, \Delta B) = P(\text{conceptual\_overlap} \mid \text{feature}_A, \text{feature}_B)
$$
**Measurement:**

$$
\text{alignment\_score} = 1 - \frac{\text{unnecessary\_conflicts}}{\text{total\_parallel\_changes}}
$$
Where unnecessary_conflicts = conflicts between conceptually independent features

**Justification:**

- **Parallel Development:** Enables truly parallel work without coordination overhead
- **Cognitive Alignment:** Code structure matching mental models reduces comprehension time
- **Natural Boundaries:** Real-world concepts have natural boundaries that minimize overlap
- **Emergent Architecture:** Good structure is discovered from the domain, not imposed

**Critical Insight:** Merge conflicts between "unrelated" features indicate architectural misalignment. Good architecture enables parallel development of independent features without coordination.

**Boundary Conditions:**

- **Domain Fluidity:** Early in product development when domain is unclear
- **Technical Constraints:** Sometimes technical requirements force non-conceptual boundaries
- **Team Structure:** Conway's Law may override conceptual boundaries

## Discussion: Architecture as Discovery

Architecture shouldn't be imposed through technical patterns but discovered through domain understanding. The best structures emerge from identifying natural conceptual boundaries.

**The Merge Conflict Metric:** Unnecessary merge conflicts are architecture smells:

$$
\text{architecture\_quality} = 1 - \frac{\text{conceptually\_independent\_conflicts}}{\text{total\_conflicts}}
$$
**Feature Folders vs Type Folders:** This principle explains why feature-based organization often beats type-based:

- Type folders force every feature to touch multiple locations
- Feature folders contain related changes
- Domain boundaries are more stable than technical boundaries