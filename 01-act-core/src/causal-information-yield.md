---
slug: causal-information-yield
type: definition
status: discussion-grade
depends:
  - pearl-causal-hierarchy
  - action-selection
  - mismatch-signal
---

# Definition: Causal Information Yield

Actions don't merely select among outcomes — they produce characteristically different outcome distributions depending on the causal structure. Causal information yield (CIY) quantifies the **action-distinguishability** of an action: how different its outcome distribution is from what alternative actions would produce.

## Formal Expression

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

$\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Level 2 from Level 1 epistemic access ( #pearl-causal-hierarchy).

**Observational proxy** (for diagnostic use with observational statistics):

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is **sign-indefinite in general** and requires causal assumptions for interpretation. The canonical CIY (interventional) is the primary quantity; the proxy is auxiliary.

**Safety conditions for proxy use.** The proxy form should NOT be used in policy optimization (e.g., as the CIY term in the unified policy objective) because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction. The proxy is suitable only for diagnostic purposes: detecting whether an action carried causal information (large proxy magnitude) vs. none (proxy near zero). For decision-making, use the canonical CIY (non-negative by construction) or a known-safe surrogate (ensemble disagreement, UCB bonuses). If the canonical CIY is intractable and no safe surrogate is available, the CIY term should be dropped from the policy objective entirely, defaulting to pure exploitation.

### Admissibility regimes

*[Scope Condition (ciy-admissibility)]*

Three regimes determine when CIY can be estimated and how strong the causal identification is:

**Regime A — Randomized interventions.** The agent varies its actions across episodes (RL agents exploring, scientists experimenting, organisms probing). CIY is directly estimable from the agent's execution data and non-negative by construction. This is the standard case for active agents within the adaptive loop ( #loop-interventional-access). Action variation provides the identification needed for clean interventional estimates.

**Regime B — Observational with causal assumptions.** The agent cannot freely vary actions (constrained by coordination, policy, or resource limits). CIY estimation requires additional structure: a known causal DAG, instrumental variables, or functional form assumptions. Results inherit whatever causal assumptions are made. The interventional interpretation of CIY is weaker — it holds under the assumed causal structure but not model-free.

**Regime C — Adversarial or passive observation.** The agent either did not intervene (passive monitoring) or the observation channel includes responses from potentially adversarial sources. In the passive case, CIY is zero by definition (no intervention, no interventional information). In the adversarial case, CIY from the query action itself remains non-negative, but the *content* of the response may be designed to increase model-reality mismatch. The adversary operates through the disturbance term $\rho$, not through the information measure.

The regime is a property of the **domain and the agent's action space**, not a parameter the agent chooses. Software development is typically Regime A (the agent runs tests, deploys to staging, observes results — high action variation). Organizational strategy is typically Regime B (multiple initiatives run concurrently, attribution requires assumptions). Intelligence analysis is typically Regime C (the analyst observes but does not intervene).

## Epistemic Status

The CIY *definition* is well-grounded in causal inference theory. The *structural claim* — that the optimal policy jointly maximizes value and causal information — is *discussion-grade*, supported by convergent results in Bayesian RL, active inference, and information-directed sampling, but not derived from first principles within ACT. The specific form of $\lambda(M_t)$ (the exploration-exploitation balance weight) is not derived. See discussion of the unified policy objective below.

## Discussion

**CIY measures distinguishability, not learning value.** CIY as defined is the expected KL divergence between outcome distributions — how different the outcomes of $a$ are from the outcomes of typical alternatives. This is **action-distinguishability**, not **expected information gain** (EIG). The distinction matters: an action can have high CIY even when the agent already knows the outcome distributions perfectly (the distributions ARE different, but the agent learns nothing new by confirming what it already knows). High CIY is *necessary* for learning (indistinguishable actions can't teach anything) but not *sufficient* (distinguishable actions only teach when the agent is uncertain about the distinction).

The two quantities approximately coincide when $U_M$ is high — when the agent doesn't know the outcome distributions, high-CIY actions also have high EIG because observing a characteristically different outcome updates the agent's beliefs about the causal structure. They diverge when $U_M$ is low — a confident agent gains nothing from taking a distinguishable action it already understands.

The $\lambda(M_t)$ weighting in the unified policy objective (below) partially compensates: when $U_M$ is low, $\lambda \to 0$, suppressing the CIY term regardless of its magnitude. This makes the exploration term behave more like EIG — suppressing exploration when the agent is already certain. The compensation is heuristic (the $\lambda$ form is not derived). For the current theory, CIY serves as a tractable surrogate for EIG, with the $\lambda$ weighting providing the uncertainty-gating that makes the surrogate reasonable.

**Open direction: proper EIG within ACT.** Replacing CIY with a proper expected information gain quantity — $\text{EIG}(a; M) = I(o; \theta \mid do(a), M)$ where $\theta$ parameterizes the model — would be a stronger foundation for the exploration term, particularly in domains where the agent must decide between actions that are all highly distinguishable but differ in what they teach. Under certain scopes (intervention-rich domains with well-parameterized models), the EIG formulation might yield sharper exploration strategies — preferring actions that resolve the *most uncertain* causal links rather than the most distinguishable ones. Whether this yields operationally significant improvements over the $\lambda$-weighted CIY surrogate is an empirical question. The CIY formulation has the advantage of being computable from the agent's current model alone (it doesn't require reasoning about model uncertainty); EIG requires a meta-model of what the agent doesn't know.

**Dependence on the reference distribution $q$.** The quantitative CIY value depends on the choice of $q$, which is a significant degree of freedom. A uniform $q$ treats all alternatives equally; a policy-induced $q$ emphasizes alternatives the agent would consider. ACT adopts the policy-induced $q$ as default: $q(\cdot \mid M) = \pi(\cdot \mid M)$, yielding CIY as "how different is this action's outcome from what I'd typically see?" CIY values are not comparable across different $q$ choices.

**The unified policy objective.** The exploration-exploitation tension suggests:

*[Discussion (unified-policy-objective)]*

$$\pi^*(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is exploration (causal information yield). $\lambda(M_t)$ controls the balance:

- High $U_M$ (uncertain model) → large $\lambda$ — exploration is valuable
- Low $U_M$ (confident model) → small $\lambda$ — exploitation dominates
- Long time horizon → larger $\lambda$ — information compounds
- High $\rho$ (fast-changing environment) → larger $\lambda$ — perpetual uncertainty

$\lambda$ carries units of [value per unit information]. In specific domains it reduces to known quantities:

| Domain | $\lambda$ reduces to | Status |
|--------|---------------------|--------|
| Bayesian bandits | Gittins index | Exactly derived |
| Kalman dual control | Probing cost in quadratic objective | Exactly derived |
| Active inference | Precision on epistemic affordance | Framework-derived |
| Information-directed sampling | $(\text{VoI})^2 / \text{info gain}$ | Exactly derived (Russo & Van Roy) |
| RL with UCB | Confidence-bound scaling | Heuristic (tuned) |

**Query actions: accessing external models.** A qualitatively distinct class of actions: querying another agent's model. When a reliable source exists (expert, database, documentation, well-trained LLM), "ask a well-formed question" can yield information equivalent to thousands of probe-observe cycles. The source's model has already performed the compression work ( #information-bottleneck) — the response transfers the *output* of compression rather than requiring the agent to reconstruct it.

Key properties of query actions:
- **Information density**: Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes
- **Trust-dependent gain**: Update from query depends on the agent's model of the source's reliability and alignment, not on observation channel noise ( #communication-gain)
- **Pre-compressed information**: Responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align
- **Structural adaptation via external models**: Encountering another agent's model can trigger structural change ( #structural-adaptation-necessity) — incorporating external representational structure rather than building it de novo ("grafting")

When high-CIY query channels are available, the unified policy objective favors query actions over direct probes, particularly when $U_M$ is high, a trusted source exists, query cost is low, and the needed information is about *structure* rather than the agent's specific situation.

**The adversarial mirror: deception and model corruption.** The same channel that enables cooperative knowledge transfer can be exploited to degrade the opponent's model. A deceptive response yields positive CIY in the strict information-theoretic sense, but the content drives model-reality mismatch *upward*. The update gain $\eta^\ast$ for the victim depends on trust; successful deception exploits high trust to inject a large, misdirected update. In the Lyapunov framework ( #sector-condition-stability), this is adversarial disturbance injected through the observation channel, with coupling coefficient $\gamma_A$ determined by the victim's trust level and exposure. See #communication-gain for the formal treatment of trust-dependent gain, and #adversarial-destabilization for the Lyapunov formalization. Distributed tempo, topology analysis, and game-theoretic integration are Section III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`).

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #strategy-dag) need observational access ( #observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The Free Energy Principle's "expected free energy" decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking). ACT's formulation is structurally isomorphic: expected value ≈ extrinsic, CIY ≈ epistemic. Whether this convergence is deep or superficial is an open question. ACT grounds exploration in explicitly *causal* information rather than entropy reduction — not all uncertainty reduction is equally valuable; causal information specifically enables better *intervention*.

**Identifiability gate.** Before incorporating CIY into policy objectives: (1) action variation must exist, (2) admissibility regime must be identified, (3) reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

**(Descended from TF-08.)**
