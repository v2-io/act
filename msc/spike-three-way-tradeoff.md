# Spike: Three-Way Exploit/Explore/Deliberate Tradeoff

**Date:** 2026-04-02
**Status:** Working spike for the Section II gap after #strategy-persistence-schema
**Target segment:** `01-act-core/src/exploit-explore-deliberate.md`


## The Problem

ACT currently has three binary tradeoffs that each capture one face of the resource-allocation problem for actuated agents:

1. **Exploit vs. Explore** (#ciy-unified-objective): $\pi^\ast = \arg\max_a [Q_O(M_t, a) + \lambda \cdot \text{CIY}(a)]$. Allocates action selection between value-maximizing and information-gathering actions. Section I machinery.

2. **Think vs. Act** (#deliberation-cost): Deliberation of duration $\Delta\tau$ is net-beneficial when $\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert > \rho_{\text{delib}} \cdot \Delta\tau$. Section I machinery.

3. **Plan vs. Explore** (#explicit-strategy-condition): $C_{\text{plan}} + C_{\text{maintain}} < C_{\text{explore}} + C_{\text{repair}}$. A normative condition for whether explicit $\Sigma_t$ is worth having at all. Section II machinery.

What's missing: the unified allocation. At each decision point, an actuated agent with explicit $\Sigma_t$ faces a three-way choice:

- **Exploit**: take the currently-best action under $\Sigma_t$ (earn immediate value via $Q_O$)
- **Explore**: take an information-gathering action (earn CIY, improving $M_t$)
- **Deliberate**: pause acting to revise $M_t$ or $\Sigma_t$ internally (earn $\Delta\eta^\ast$ or $\Delta\alpha_\Sigma$)

These three compete for a shared finite resource: the agent's time/capacity budget within each cycle.


## What Existing Machinery Provides

### The exploit/explore balance (Section I)

The CIY-unified objective gives:

$$\pi^\ast(M_t, G_t) = \arg\max_a [Q_O(M_t, a; \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a; M_t)]$$

This handles the action-selection problem *conditional on acting*. The $\lambda$ weight modulates between exploitation and exploration. But it assumes the agent IS acting --- it doesn't consider the option of not acting at all (deliberating instead).

### The think/act threshold (Section I)

The deliberation cost gives a binary threshold:

$$\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert > \rho_{\text{delib}} \cdot \Delta\tau$$

This tells the agent when to pause. But it only considers *epistemic* deliberation (improving $\eta^\ast$ for model updates). For actuated agents, deliberation can also improve the *strategy* --- revising $\Sigma_t$ edges, restructuring the DAG, reassessing $O_t$. The orient cascade (#orient-cascade) describes the ordering of these revisions; what's missing is the *cost-benefit* framework for deciding how much cycle budget to spend on strategic deliberation vs. acting.

### The plan/explore threshold (Section II)

The explicit strategy condition is a one-time design decision: is explicit $\Sigma_t$ worth it? Once the agent has $\Sigma_t$, the question becomes: at this moment, should I exploit $\Sigma_t$, explore to improve $M_t$, or deliberate to improve $\Sigma_t$?


## Structure of the Unified Allocation

### The key insight: deliberation is a third activity, not a modifier of the other two

In the binary exploit/explore framework, the agent always acts --- the only question is what kind of action. Adding deliberation introduces a genuinely different mode: the agent may choose NOT to act externally, instead investing time in internal processing.

This means the tradeoff is not a single optimization over actions but a **two-stage allocation**:

**Stage 1 (act vs. deliberate):** What fraction of the current cycle to spend deliberating vs. acting?

**Stage 2 (exploit vs. explore):** Conditional on acting, which action to take?

Stage 2 is already solved by the CIY-unified objective. The new content is Stage 1, extended to cover strategic deliberation (not just epistemic deliberation).

### Why not a single three-way optimization?

The three activities are not commensurable in a single $\arg\max$ because:

1. Exploit and explore are *actions* (same type: elements of $\mathcal{A}$). They can be compared directly via $Q_O + \lambda \cdot \text{CIY}$.
2. Deliberate is *inaction* (or internal action). Its benefit is measured in improved future action quality, not in immediate value or information.

The benefit of deliberation is *mediated* --- it improves the agent's capacity for future exploitation and exploration. This makes it a different kind of investment: exploit and explore earn returns now; deliberate earns returns later. The comparison requires a temporal discount or amortization.


## The Formal Structure

### Budget constraint

At each decision point, the agent allocates its cycle time $T_{\text{cycle}}$ between deliberation ($\Delta\tau$) and action ($T_{\text{cycle}} - \Delta\tau$):

*[Formulation]*

$$T_{\text{cycle}} = \Delta\tau + T_{\text{act}}$$

where $\Delta\tau \geq 0$ is deliberation duration and $T_{\text{act}} = T_{\text{cycle}} - \Delta\tau$ is the time available for acting.

### Value of acting (conditional on $\Delta\tau$)

After deliberation of duration $\Delta\tau$, the agent acts with improved model $M_t'$ and potentially revised strategy $\Sigma_t'$. The expected value of the action phase is the CIY-unified objective evaluated at the post-deliberation state:

$$V_{\text{act}}(\Delta\tau) = \max_a [Q_O(M_t', a; \pi_{\text{cont}}, N_h) + \lambda(M_t', O_t, N_h) \cdot \text{CIY}(a; M_t')]$$

where $M_t' = M_t(\Delta\tau)$ reflects any internal model improvement from deliberation.

### Cost of deliberation

Deliberation incurs two costs:

1. **Temporal cost**: mismatch accumulates at rate $\rho_{\text{delib}}$ during the pause. Total: $\rho_{\text{delib}} \cdot \Delta\tau$.
2. **Opportunity cost**: the agent foregoes $T_{\text{act}}$ worth of acting. At the current expected value rate, this is approximately $V_{\text{act}}(0) \cdot (1 - T_{\text{act}}/T_{\text{cycle}})$.

### Benefit of deliberation

Deliberation can improve the agent's state along two dimensions:

1. **Epistemic improvement**: $\Delta\eta^\ast(\Delta\tau)$ --- improved model update gain (already in #deliberation-cost).
2. **Strategic improvement**: $\Delta\alpha_\Sigma(\Delta\tau)$ --- improved strategy quality. This could mean:
   - Better edge credences (internal simulation reveals inconsistencies)
   - Better DAG structure (nodes added/pruned)
   - Better $O_t$ (objective revision triggered by satisfaction-gap analysis)

The strategic benefit is mediated through the orient cascade: deliberation time is spent traversing steps 2-5 of the cascade (evaluate $\delta_{\text{sat}}$, evaluate $\delta_{\text{regret}}$, evaluate $\delta_{\text{strategic}}$, potentially revise $O_t$).

### The unified objective

Combining, the agent maximizes over deliberation duration $\Delta\tau$:

*[Formulation]*

$$\Delta\tau^\ast = \arg\max_{\Delta\tau \geq 0} \left[V_{\text{act}}(\Delta\tau) - \rho_{\text{delib}} \cdot \Delta\tau \right]$$

where $V_{\text{act}}(\Delta\tau)$ incorporates both the improved action quality and the reduced action time.

This is structurally the same as the deliberation-cost threshold but with:
- $V_{\text{act}}$ now includes the CIY term (exploration value)
- $V_{\text{act}}$ benefits from both epistemic ($\Delta\eta^\ast$) and strategic ($\Delta\alpha_\Sigma$) improvements

The first-order condition is:

$$\frac{\partial V_{\text{act}}}{\partial \Delta\tau} = \rho_{\text{delib}}$$

Stop deliberating when the marginal improvement rate drops below the mismatch drift rate.


## When Each Activity Dominates

The three-way allocation has natural dominance regimes. These follow from the structure of the objective, not from additional assumptions.

### Exploit dominates when:
- $\rho$ is high (environment changes fast --- can't afford to pause)
- $\delta_{\text{regret}} \approx 0$ (strategy is near-optimal)
- $\lambda \approx 0$ (model uncertainty is low)
- $\lVert\delta_{\text{epistemic}}\rVert$ is small (model is adequate)
- $\lVert\delta_{\text{strategic}}\rVert$ is small (strategy is calibrated)

In this regime: the agent knows what to do and the situation demands immediate action. This is Boyd's implicit guidance and control (Orient $\to$ Act, bypassing Decide). In adaptive cycle terms: prolepsis is accurate, so praxis follows fluently.

### Explore dominates when:
- $U_M$ is high (model uncertainty is large)
- $\lambda$ is large (long horizon, information compounds)
- $\delta_{\text{epistemic}}$ is large but $\rho_{\text{delib}}$ is also large (can't afford to think, must probe)
- $\Sigma_t$ has many unobservable edges (#observability-dominance --- exploration is required to make strategy edges assessable)
- CIY of available actions is high (distinguishable outcomes exist)

In this regime: the agent doesn't know enough to act effectively, and probing is cheaper than thinking. The mismatch is large and the model needs correction via external evidence, not internal computation.

### Deliberate dominates when:
- $\rho_{\text{delib}}$ is low (environment is stable during pauses)
- $\delta_{\text{regret}} \gg 0$ OR $\delta_{\text{strategic}} \gg 0$ (strategy needs revision)
- Strategy DAG has many stale edges (high $\rho_\Sigma$, low $\mathcal{T}_\Sigma$)
- $\Delta\eta^\ast$ or $\Delta\alpha_\Sigma$ have high marginal return (early in the diminishing-returns curve)
- The action space is dangerous (high cost of error: $C_{\text{repair}}$ large)

In this regime: acting without planning is too expensive, and the environment permits the agent to pause. This is the domain of strategic planning, architectural review, System 2 reasoning. In adaptive cycle terms: the agent lingers in epistrophe, investing in a deeper orient cascade traversal before praxis.


## What's Derivable vs. What's Formulation

### Derived from existing machinery:
1. **The two-stage structure** (act-vs-deliberate, then exploit-vs-explore) follows from the type distinction: exploit and explore are actions; deliberate is inaction. This is a structural consequence, not a design choice.
2. **The dominance regimes** follow from the first-order conditions of the respective binary tradeoffs. High $\rho_{\text{delib}}$ kills deliberation value (from #deliberation-cost). High $U_M$ amplifies exploration value (from #ciy-unified-objective). Low $\delta_{\text{regret}}$ kills deliberation motivation (from #control-regret).
3. **The budget constraint** is a conservation law: time spent deliberating is time not spent acting.

### Formulation choices:
1. **The specific functional form** of $V_{\text{act}}(\Delta\tau)$ is domain-dependent. The theory provides the structure (value of acting post-deliberation minus drift cost) but not the function.
2. **The decomposition of deliberation benefit** into epistemic ($\Delta\eta^\ast$) and strategic ($\Delta\alpha_\Sigma$) is a modeling choice that parallels the $M_t$/$\Sigma_t$ factorization. Under directed separation (#directed-separation), the two benefits are independently evaluable. For Class 2 agents, they're coupled.
3. **Whether $\Delta\tau$ is continuous or discrete** is a scope choice. The continuous treatment (first-order condition) is cleaner; real agents typically face discrete choice points.

### Hypotheses / open:
1. **Whether the marginal returns curve for strategic deliberation has the same concave shape as epistemic deliberation.** Plausible (early revisions are most valuable) but not demonstrated.
2. **Whether internal simulation can generate genuine CIY** (deliberation-as-exploration). If so, the boundary between "explore" and "deliberate" is fuzzy --- internal simulation that surfaces model inconsistencies functions as exploration without external action. This connects to #deliberation-cost's Open Question 3.


## Connection to the Adaptive Cycle Phases

The three-way allocation maps onto the adaptive cycle phases:

| Activity | Primary cycle phase | What improves |
|----------|-------------------|--------------|
| Exploit | Praxis | Immediate value ($Q_O$) |
| Explore | Praxis $\to$ Aisthesis | Future $M_t$ quality ($\text{CIY} \to \Delta\eta^\ast$) |
| Deliberate | Extended Epistrophe | Future action quality ($\Delta\eta^\ast$, $\Delta\alpha_\Sigma$) |

Exploitation is praxis with the current model. Exploration is praxis chosen to improve the *next* aisthesis. Deliberation is extended epistrophe --- the agent stays in the corrective phase longer, running the orient cascade more deeply before proceeding to praxis.

The temporal-optimality postulate (#temporal-optimality) provides normative grounding: among strategies achieving equivalent outcomes, the one requiring least time is preferred. This means:
- The agent should not deliberate beyond the point where marginal improvement drops below marginal cost
- The agent should not explore when exploitation yields the same long-run outcome
- The agent should not exploit when exploration or deliberation would produce a strictly better outcome faster


## Decision for the Segment

**Type:** `formulation` --- the three-way allocation structure is a modeling framework that extends the existing binary tradeoffs. The dominance regimes are derived; the specific objective function form is a formulation choice.

**Status:** `conditional` --- conditional on the deliberation-drift assumption (GA-4, from #deliberation-cost) and on directed separation (#directed-separation) for the clean decomposition of deliberation benefit into epistemic and strategic components.

**Dependencies:**
- `ciy-unified-objective` --- the binary exploit/explore objective being extended
- `deliberation-cost` --- the binary think/act threshold being incorporated
- `explicit-strategy-condition` --- the normative condition that $\Sigma_t$ is worth having
- `strategy-persistence-schema` --- the strategic correction rate $\alpha_\Sigma$ that deliberation improves
- `orient-cascade` --- the internal structure of the deliberation phase
- `control-regret` --- the signal that triggers deliberation ($\delta_{\text{regret}} \gg 0$)
- `temporal-optimality` --- normative grounding

**Key formal result:** The extended first-order condition:

$$\frac{\partial}{\partial \Delta\tau}\left[\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert + \Delta V_\Sigma(\Delta\tau)\right] = \rho_{\text{delib}}$$

where $\Delta V_\Sigma(\Delta\tau)$ is the value improvement from strategy revision during deliberation. Stop deliberating when the marginal joint (epistemic + strategic) improvement rate drops below the drift rate.

This reduces to #deliberation-cost when $\Delta V_\Sigma = 0$ (no strategy revision) and to pure exploitation when $\Delta\tau = 0$ (no deliberation).
