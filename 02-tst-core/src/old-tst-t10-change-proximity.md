---
label: T-10
type: Theorem
subtype: Derived
name: Change Proximity Principle
dependencies:
  - "[[t09-change-set-size.md|T-09]]"
  - "[[d02-atomic-change-set.md|D-02]]"
  - "[[d05-change-distance.md|D-05]]"
older-tag: FP-009
revision: 0.2
---

# T-10 Theorem (Derived): Change Proximity Principle

**Statement:** Given two implementations producing identical change-sets, the one with changes closer together was likely implemented faster and will enable faster future changes.

$$
\text{proximity}(\text{changeset}) = \frac{1}{\sum_{i,j} \text{distance}(\text{change}_i, \text{change}_j)}
$$

$$
\text{time}_{\text{implementation}} \propto \frac{1}{\text{proximity}(\text{changeset})}
$$
Where distance is as defined in D-05

**Justification:**

- **Cognitive Load:** Mental context switching decreases with proximity
- **Cache Efficiency:** Both human memory and CPU cache benefit from locality
- **Error Reduction:** Related changes in proximity are less likely to be forgotten
- **Review Efficiency:** Code reviews are faster when changes are co-located

**Boundary Conditions:**

- **Language Differences:** Some languages enforce more separation than others
- **Tool Support:** Advanced IDEs can partially compensate for poor proximity
- **Team Boundaries:** Human proximity (same team) can matter more than code proximity

## Discussion: Measuring Distance

Distance between changes can be measured at multiple levels:

1. **Lexical:** Lines/characters apart in same file
2. **Structural:** Function/class/module boundaries crossed
3. **File System:** Directory traversals required
4. **Architectural:** Service/database/network boundaries crossed

Each level adds roughly an order of magnitude to cognitive load.

**The Navigation Tax:** Every jump between distant code locations incurs a "navigation tax"—time spent finding, opening, understanding context, and returning. This tax compounds with each jump, making scattered changes exponentially more expensive than clustered ones.