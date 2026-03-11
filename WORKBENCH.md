# WORKBENCH — ACT Theory Development

Working notes for theory development. This is a thinking tool, not a
reference document. For the canonical theory structure, see
`CURRENT-FULL-THEORY.md`.


## Segment Status

### Written
| Slug | Type | Notes |
|------|------|-------|
| [temporal-optimality](src/temporal-optimality.md) | Axiom | Needs review |
| [agent-environment](src/agent-environment.md) | Definition | Needs review |
| [observation-function](src/observation-function.md) | Definition | Needs review |
| [action-transition](src/action-transition.md) | Definition | Needs review |
| [scope-condition](src/scope-condition.md) | Scope | Needs review |
| [agent-model](src/agent-model.md) | Formulation | Needs review |
| [information-bottleneck](src/information-bottleneck.md) | Formulation | Needs review |
| [model-sufficiency](src/model-sufficiency.md) | Definition | Needs review |
| [model-class-fitness](src/model-class-fitness.md) | Definition | Needs review |
| [recursive-update](src/recursive-update.md) | Derived | Needs review |
| [update-gain](src/update-gain.md) | Empirical | Needs review |
| [adaptive-tempo](src/adaptive-tempo.md) | Definition | Needs review |
| [persistence-condition](src/persistence-condition.md) | Theorem | Needs review |
| [sector-condition-stability](src/sector-condition-stability.md) | Theorem | Needs review |
| [agent-spectrum](src/agent-spectrum.md) | Definition | Needs review |
| [specification-bound](src/specification-bound.md) | Theorem | Needs review |

### Not Yet Written — Section I
| Slug | Type | Source material |
|------|------|-----------------|
| composition-consistency | Axiom | `scratch/spike-agent-composition.md` |
| causal-structure | Axiom | TF-02 |
| pearl-causal-hierarchy | Definition | TF-02 |
| chronica | Definition | TF-02 |
| event-driven-dynamics | Formulation | TF-04 |
| mismatch-signal | Definition | TF-05 |
| mismatch-decomposition | Theorem | TF-05, Prop 5.1 |
| structural-adaptation-necessity | Theorem | TF-10, Prop 10.1 |

### Not Yet Written — Section II
| Slug | Type | Source material |
|------|------|-----------------|
| complete-agent-state | Formulation | v3 spike §1 |
| objective-functional | Definition | v3 spike §2 |
| value-object | Definition | v3 spike §2.2 |
| strategy-dimension | Definition | v3 spike §3 |
| causal-hierarchy-requirement | Derived + Scope | v3 spike §4 |
| loop-interventional-access | Derived | v3 spike §4.3 |
| explicit-strategy-condition | Normative | v3 spike §5 |
| chain-confidence-decay | Derived | v3 spike §6.1 |
| and-or-scope | Scope | v3 spike §6.2 |
| strategy-dag | Definition | intent-dag-consolidated + graph uniqueness spike |
| directed-separation | Derived + Scope | v3 spike §8 |
| satisfaction-gap | Definition | v3 spike §7.3 |
| control-regret | Definition | v3 spike §7.4 |
| strategic-calibration | Definition | v3 spike §7.5 |
| orient-cascade | Derived | v3 spike §7.6 |
| observability-dominance | Derived | intent-dag-consolidated |
| edge-update-via-gain | Hypothesis | intent-dag-consolidated |
| structural-change-as-parametric-limit | Formulation | intent-dag-consolidated |
| strategy-persistence-schema | Proposed schema | v3 spike §9 |

### Not Yet Written — Sections III–V
All claims. Source material in TFT (TF-11, Appendix F, track-b sims),
composition spike, TST, and agentic-tft docs 10-14.


## Key Spikes

| Spike | Location | Status |
|-------|----------|--------|
| Purposeful agent derivation (v3) | `scratch/spike-v3-purposeful-agent.md` | **Definitive** for Section II porting |
| Agent composition / holon | `scratch/spike-agent-composition.md` | Core insight strong; composition laws are sketches |
| Graph structure uniqueness | `scratch/spike-graph-uniqueness.md` | Acyclicity derived; P3→Markov needs tightening |
| Intent DAG consolidated | `scratch/04-intent-dag-consolidated.md` | Canonical DAG reference; converged |
| Prior art assessment | `scratch/02-prior-art-assessment.md` | Hafez/IBM/BDI/active-inference positioning |
| LLM causal access note | `scratch/llm-causal-access-note.md` | Pearl reconciliation; potential intro/paper/blog |
| Track-b simulations | `scratch/track-b-nonlinear-sims/` | 6 variants, all validated |


## What's Settled

*From convergence testing, spikes, and simulation:*

- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with explicit scope condition for goal-conditioned
  agents)
- $G_t = (O_t, \Sigma_t)$ split (definitional, not timescale-dependent)
- Satisfaction gap / control regret split (replaces simpler
  $\delta_{\text{objective}}$)
- DAG acyclicity derived from temporal ordering (former fragility resolved)
- Composition consistency required (not optional) by scope condition's
  level-independence


## What's Open

- Action-deliberation-exploration tradeoff (three-way with $\Sigma_t$)
- Strategy tempo formalization
- Cognitive cost of $\Sigma_t$ (no $\beta$ analog yet)
- Edge identifiability conditions (resolved in software, open in general)
- P3→Markov step in graph uniqueness (sketch, needs tightening)
- Composition laws (specific forms are sketches; existence is required)


## Known Fragilities

- Edge semantics claim interventional but update from observational
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) —
  acknowledged as scope restriction, not a bug


## Codex Review Issues (from memory — fixes needed)

1. **State completeness**: Must lift to $X_t = (M_t, G_t)$. $M_t$ becomes
   epistemic substate, not complete state. Foundational.
2. **Level 2 too strong**: Pre-compiled controllers are purposeful at
   Level 1. Scope to agents that must *learn* action consequences during
   operation.
3. **Objective/strategy are independent dimensions**: Don't conflate in a
   single hierarchy. $O_t$ richness and $\Sigma_t$ richness vary
   independently. Split early.
4. **$O_t$ parametrizes TF-08's "value" term**: Cleaner insertion point.
5. **Objective as trajectory functional**: $J$: trajectories $\to \mathbb{R}$
   is genuinely more general than point targets.
6. **Cost inequality for $\Sigma_t$**: Derive need for explicit planning
   from $\text{cost}(\text{plan}) < \text{cost}(\text{explore})$, making
   #temporal-optimality load-bearing.
7. **$p^n$ is the special case**: Robust result is additive log-confidence
   growth.
8. **Strategy persistence is a theorem schema**: Need strategic error state,
   correction operator, disturbance class.
9. **Directed separation is conditional**: $f_M$ is $G_t$-independent, but
   closed-loop $M$ transition depends on $G_t$ through action. Precise claim
   is about update function, not trajectory.
10. **$\delta_{\text{objective}}$ must split into TWO quantities**:
    satisfaction gap + control regret. Without this split, the $O_t$ revision
    cascade doesn't work.

Items 1–10 are addressed in v3 spike. Porting to src/ segments is the
remaining work.


## Ordering Questions

*The current linearization in CURRENT-FULL-THEORY.md may need revision:*

- Should #temporal-optimality move from Section I to Section II? It's about
  specific objectives — arguably an actuated-agent concept, not a general
  adaptive-systems concept. Counter-argument: it applies to Section I agents
  too (a Kalman filter that converges faster is better).

- Should #composition-consistency move earlier or later? Currently at the end
  of Section I foundations, before the dynamics claims. Could go right after
  #scope-condition (it's a direct consequence of scope's level-independence).
  The composition spike argues for early placement.

- Section II ordering: the v3 spike proposes a specific 16-segment
  linearization (§11). Is that still the best ordering after the codex
  review corrections?


## Simulation Findings (Summary)

The track-b simulations (`scratch/track-b-nonlinear-sims/`) validated and
refined specific claims:

- Cor. 11.2's exponent = 2 under deterministic drift (confirmed: 1.999)
- Under stochastic disturbances, exponent = 1.5 (not 2.0)
- Observation noise collapses adversarial exponent from ~1.0 to ~0.2
- Per-dimension persistence exact (scalar overestimates by 72%)
- TF-06's gain principle empirically validated (52% reduction)


## Prior Art Positioning

*Detailed cross-mapping in `scratch/02-prior-art-assessment.md`:*

- **Hafez** (bi-predictability $P$): complementary diagnostic, no
  goals/dynamics. $H_b$ has no ACT analog yet — matters for
  legibility/coordination.
- **IBM 2025** (systems theory manifesto): calls for what ACT provides. Their
  open challenges (subgoal emergence, residual control rights) directly
  addressed by ACT.
- **BDI**: named the parts, no dynamics.
- **Active inference**: closest competitor, different foundation.
- **Paper strategy**: lead with Section I (proved) + Section II (v3 spike),
  cite IBM as articulating the need, Hafez as complementary diagnostic.
