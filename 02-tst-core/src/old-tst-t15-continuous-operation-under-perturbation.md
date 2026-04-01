---
label: T-15
type: Theorem
subtype: Scope
name: Continuous Operation Under Perturbation
dependencies:
  - "[[t04-change-expectation-baseline.md|T-04]]"
  - "[[d08-system-availability.md|D-08]]"
revision: 0.2
---

# T-15 Theorem (Scope): Continuous Operation Under Perturbation

**Statement:** For systems that must continue operating while evolving, time optimization includes recovery time from failures and external shocks.

For systems $S$ where:
- $E[\text{changes}_{\text{future}}] > 0$ (evolving systems per T-04)
- $P(\text{external\_shock}) > 0$ (subject to impulses/stress)  
- $\text{required\_availability} > \text{threshold}$ (must stay operational)

$$
\text{Effective time: } T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}
$$
**Discussion:** This theorem narrows the scope from all software to the class of systems that must remain operational while changing—which encompasses most production systems. It preserves time as the sole optimization target while acknowledging that recovery time is part of total time for continuously operating systems.

**Justification:** A crashed system has infinite implementation time from the user's perspective. Therefore, minimizing recovery time is equivalent to minimizing total time. This explains why practices like supervision trees, circuit breakers, and "let it crash" philosophy are optimal—they minimize $T_{\text{recovery}}$.

**Implications:**

- **Defensive Programming:** High $T_{\text{implementation}}$, aims for low $P(\text{failure})$
- **Let It Crash:** Low $T_{\text{implementation}}$, accepts $P(\text{failure})$ but minimizes $T_{\text{recovery}}$
- **Optimal Strategy:** When $T_{\text{recovery}} \ll T_{\text{defensive\_code}}$, accepting failures is time-optimal

**External Shocks:**

- **Impulse:** Sudden shock (traffic spike, deployment)
- **Stress:** Sustained force (slow dependency, memory leak)
- **Strain:** Deformation that propagates through coupled components

Systems optimized per T-15 handle shocks by minimizing propagation (low coupling) and recovery time (fast restart) rather than trying to prevent all failures.