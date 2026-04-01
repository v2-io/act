---
label: T-05
type: Theorem
subtype: Derived
name: Dual Optimization Principle
dependencies:
  - "[[t01-time-optimality.md|T-01]]"
  - "[[t03-evolving-systems-scope.md|T-03]]"
  - "[[d03-comprehension-time.md|D-03]]"
  - "[[d04-implementation-time.md|D-04]]"
older-tag: FP-007
revision: 0.2
---

# T-05 Theorem (Derived): Dual Optimization

**Statement:** A principled decision minimizes both time-to-comprehension and time-of-implementation for future features.

$$
\begin{aligned}
&\text{For implementation } C \text{ of current feature:} \\
&\text{principled}(C) \rightarrow \text{minimizes}\left(\text{time}_{\text{comprehension}}(F_i \mid C) + \text{time}_{\text{implementation}}(F_i \mid C)\right)
\end{aligned}
$$
**Justification:**

- **Empirical:** Comprehension time often dominates total feature time (especially with team changes)
- **Compound Effect:** Poor comprehensibility compounds worse than implementation difficulty
- **Team Dynamics:** Comprehension time multiplied by team size, implementation often parallelizable

## Discussion: The Hidden Cost of Incomprehension

Time-to-comprehension is often invisible in metrics but dominates real development time:

- Reading existing code to understand where to make changes
- Understanding why something was done a certain way
- Discovering hidden dependencies and side effects
- Mental model construction and validation

**Team Turnover Multiplier:** With turnover rate $r$ and team size $s$:

$$
\text{total\_comprehension\_cost} = \text{time}_{\text{comprehension}} \times (1 + r) \times s
$$

High-comprehension-cost code becomes exponentially more expensive with team growth or turnover.

**The Comprehension/Implementation Tradeoff:** Sometimes these conflict:

- Abstraction can improve implementation time but hurt comprehension
- Explicit code can improve comprehension but increase implementation sites

The resolution often depends on n_future and team stability.