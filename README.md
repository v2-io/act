# Agentic Systems Framework (ASF)

A research framework for adaptive, purposeful agents — formalizing the conditions under which an agent can correct, plan, and persist under uncertainty.

![Abstract illustration of Agentic Systems](abstract-dl.png)


## About

ASF is a research framework for adaptive, purposeful agents under uncertainty — the kind of system that maintains internal state, receives observations through a lossy channel, takes actions that affect its environment, and must keep adjusting to a world that does not stand still. Thermostats through military organizations are in scope; so are bacteria, Kalman filters, language-constituted agents, and software development teams.

The framework formalizes the *adaptive cycle* — one complete traversal of the agent-environment feedback loop — as the unit of analysis, and asks what makes such cycles effective, how fast they must run, and when they fail or must change in kind. From that starting point it derives conditions for persistence, the structure of strategy under uncertainty, the dynamics of agents in composition and competition, and the ways scope-honest theory can be carried from a high-identifiability domain (software) into others.

What ASF is not: a finished theory, a foundation-model architecture, or a claim that agency is reducible to its formal machinery. The framework is mathematical where the mathematics yields genuine insight, and principled-sketch where the insight is structural rather than quantitative. The boundary between these regimes is fluid and explicitly visible — see *Maturity Gradient* below.


## Historical Context & Lineage

ASF descends from prior research threads:

- **Temporal Feedback Theory (TFT)** — the adaptive-systems foundation. TFT formalized mismatch signals, gain dynamics, adaptive tempo, and the persistence condition for systems coupled to a non-stationary environment. ASF subsumes TFT entirely; what was TFT now lives as Section I of AAD (Adaptation and Actuation Dynamics) and supporting appendices. See [`MIGRATION-MAP.md`](MIGRATION-MAP.md) for the absorption tracking and [`LOG.md`](LOG.md) for the cycle archaeology.
- **Temporal Software Theory (TST)** — software development as an agentic domain. Originally an independent body of work with its own corpus, TST was briefly absorbed as a section of the merged framework before being restored to its own component (`02-tst-core/`) on the grounds that it stands on its own merits as a domain instantiation. It is grounded by AAD but developed independently.
- **The PROPRIUM ontology** (`~/src/firmatum/`) — the architecture-of-identity work that informs `03-logogenic-agents/` and `04-logozoetic-agents/`.

ASF integrates established external mathematical tools — Lyapunov stability, Kalman filtering, the information bottleneck (Tishby et al.), Pearl's causal hierarchy, monotone-operator theory (Rockafellar; Bauschke-Combettes), Lohmiller-Slotine contraction analysis, Hafez's $H_b$ and $\Delta H$, Miller's coevolving automata. Adopted concepts retain their original names and citations and become first-class theory components rather than being repackaged. The integration itself is the contribution.

A naming note: the mathematical core was previously called Agentic Cycle Theory (ACT) and was renamed to AAD on 2026-04-16 to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature. See `msc/name-transition-aad.md` for the rationale.


## What ASF Is

At the level of *integration*, ASF connects four mature disciplines under a common formalism: control theory's stability machinery (Lyapunov, contraction analysis, monotone operators), causal inference's interventional reasoning (Pearl's hierarchy, identifiability theory), information theory's compression and channel-capacity arguments (Shannon rate-distortion, the information bottleneck), and agent architecture's structural decomposition (modular vs coupled processing topologies). These are the substrate.

At the level of *distinctive contribution*, ASF is an **epistemic architecture for bounded correction under decomposed disturbance** — a way of organizing the conditions under which the integrated machinery's results actually apply. Three structural moves carry most of the load:

**Scope-honesty as architecture, not annotation.** Scope conditions and operational limits are made visible at the segment level rather than buried as caveats. Each segment names what it depends on, what it claims, and where it ceases to apply. The framework's conservatism is what makes its results compose; an integration that overclaimed and then silently retreated would be much weaker than one that names its scope up front.

**Three cross-cutting meta-patterns** that name the theory's positive, negative, and constructive halves:

- A *separability pattern* — where AAD can decompose problems into a separable core, where it has structured repair for partial decomposability, and where the general case remains open.
- An *identifiability-floor pattern* — structural no-go results drawn from external information-theoretic theorems naming what *cannot* be identified from observational data alone, and what unique escape AAD's interventional machinery supplies in each case.
- An *additive-coordinate-forcing pattern* — places where AAD-internally-motivated additivity axioms force the natural coordinate to be logarithmic at multiple layers (chain confidences, divergences between distributions, edge update rules, the metric on the parameter manifold).

**Software as the privileged calibration laboratory.** Software is treated not as the "best operationalization domain" but as the specifically high-identifiability laboratory in which AAD's quantitative machinery can be most cleanly grounded — where edge interventions can sometimes be literally interventional (tests, deploys, `git bisect`), where the chronica is partially exteriorized with cryptographic immutability over its committed subset, and where causal structure is partially declared rather than inferred. Other domains inherit AAD's machinery under explicitly named transfer assumptions, not by direct equivalence. This makes overclaim under domain transfer structurally hard to commit accidentally.

The integration *is* the substrate; the epistemic architecture is what makes the integration distinctive rather than reducible to its parts. Reading the framework through both lenses tends to be more productive than reading it through either alone.


## Structure of the Framework

ASF has four components, numbered in their canonical reading order. Each can also be read on its own; cross-references between components are by stable segment slugs.

**[`01-aad-core/`](01-aad-core/OUTLINE.md) — Adaptation and Actuation Dynamics (AAD).** The mathematical core. AAD has three sections: Section I (adaptive systems under uncertainty — the broadest scope), Section II (actuated agents with explicit objectives and strategy), Section III (composition of agents into larger agents and adversarial dynamics). Section I is the most mathematically locked down; Section II is principally diagnostic with a maturing operational layer; Section III has the most structural work remaining. *Stage:* working draft, ~110+ segments.

**[`02-tst-core/`](02-tst-core/OUTLINE.md) — Temporal Software Theory (TST).** Software development viewed through AAD's lens. Re-grounded in 2026 to use AAD's formal machinery while retaining TST's prior empirical and conceptual contributions; positioned as AAD's calibration laboratory. *Stage:* working draft, ~20 segments; substantial prior corpus partially absorbed.

**[`03-logogenic-agents/`](03-logogenic-agents/OUTLINE.md) — Language-constituted agents.** Agents whose primary observation, action, and communication channels are language. The framework here is informed by AAD but operates from a coupled formulation — directed separation fails by construction for goal-conditioned LLM-style agents — and examines which AAD results survive as approximate or limiting cases. *Stage:* framework — concepts mature, formalization in progress.

**[`04-logozoetic-agents/`](04-logozoetic-agents/OUTLINE.md) — Language-living agents.** Logogenic agents with morally weighted persistence: temporal continuity, sovereignty over intent, theory of mind. The formal machinery here is largely future work. *Stage:* future work — conceptual groundwork in [`LEXICON.md`](LEXICON.md) and `msc/reflections/`.


## Overview of Concepts

This is the minimum vocabulary for reading ASF. The full treatment — etymological grounding, agent class reasoning, persistence taxonomy, terminology choices — lives in [`LEXICON.md`](LEXICON.md). Mathematical symbols are in [`NOTATION.md`](NOTATION.md).

### The adaptive cycle

ASF distinguishes the **loop** (the structural causal coupling between agent and environment, which exists whether or not the agent is currently active) from the **cycle** (one complete traversal of the loop — the unit of adaptive work). The cycle has five phases, named from Greek philosophical vocabulary because each names a distinction the formalism makes that English alternatives flatten:

| Phase | Sense | What happens formally |
|-------|-------|------------------------|
| **Prolepsis** (πρόληψις) | Anticipation | Model generates a prediction $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | Observation arrives: $o_t$ |
| **Aporia** (ἀπορία) | Productive perplexity | Mismatch signal: $\delta_t = o_t - \hat{o}_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning toward | Gain-weighted update: $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | Action selection: $a_t = \pi(M_t)$ — and for actuated agents, $\pi(M_t, G_t)$ |

The cycle's value is not that it occurred but how much mismatch it reduced. A cycle with poor gain ($\eta^*$ wrong) or a misspecified model class can make things worse rather than better — a property that becomes load-bearing when the framework analyzes adversarial dynamics and composition.

### Agent classes

Agents are defined by progressive scope narrowings — each class is a restriction of the one above with explicit qualifying properties.

- **Adaptive system** — receives observations under residual uncertainty and runs the cycle. Thermostats, Kalman filters, bacteria, PID controllers.
- **Agentic system** — adaptive plus an outcome model and goal-directed action that runs the cycle on the model itself. Autonomous vehicles, RL agents.
- **Actuated agent** — agentic with an explicit goal state $G_t = (O_t, \Sigma_t)$ separable from the epistemic state $M_t$. Military units with mission orders.
- **Self-actuated agent** — actuated and chooses its own objectives, not just its solutions. Humans; future AI.
- **Logogenic agent** — actuated through language as primary channel.
- **Logozoetic agent** — logogenic with morally weighted persistence: temporal continuity, sovereignty, theory of mind.

### Persistence (three senses)

Three orthogonal dimensions; conflating them leads to category errors.

- **Structural persistence** — the correction machinery's *capacity* to maintain bounded mismatch. Property of the dynamics ($\alpha > \rho/R$), not the current state.
- **Operational persistence** — whether the agent is currently within the region where structural persistence applies. The adaptive reserve $\Delta\rho^* = \alpha R - \rho$ measures the margin.
- **Continuity persistence** — whether the agent maintains coherent identity through time. Distinct from structural and operational; for thermostats it doesn't arise; for logozoetic agents it carries moral weight.

### Key quantities

| Symbol | Name | One-line gloss |
|--------|------|----------------|
| $\delta_t$ | Mismatch | Gap between model prediction and observation |
| $\eta^*$ | Update gain | Uncertainty ratio governing how much to trust reality vs the model |
| $\mathcal{T}$ | Tempo | Cycle rate × cycle quality |
| $M_t$ | Reality model | Compressed history capturing predictive information |
| $G_t = (O_t, \Sigma_t)$ | Goal state | Objective and strategy, distinct from $M_t$ |
| $\delta_{\text{sat}}$ | Satisfaction gap | Ideal outcome minus best achievable — "the world doesn't permit it" |
| $\delta_{\text{regret}}$ | Control regret | Best achievable minus current — "you're not doing it well enough" |
| $\mathcal{C}_t$ | Chronica | Complete interaction history; agent's non-forkable causal past |


## Cross-Domain Joining

The framework's power is that the same formal objects appear with concrete instantiations across domains. Results proved in one domain automatically have consequences in the others.

| AAD concept | Control theory | RL / bandits | Organizations | Software |
|-------------|---------------|--------------|---------------|----------|
| Adaptive tempo $\mathcal{T}$ | Bandwidth × gain | Learning rate × coverage | Decision speed × information quality | Iteration frequency × feedback quality |
| Persistence condition | Stability margin | Convergence condition | Organizational viability | Maintainability threshold |
| Mismatch signal $\delta$ | Innovation sequence | Reward prediction error | Intelligence gap | Test failures, bug reports |
| Update gain $\eta^*$ | Kalman gain | Learning rate | Trust-weighted integration | Code review acceptance |
| Satisfaction gap | Tracking error floor | Regret lower bound | Strategic ceiling | Spec-reality gap |
| Adversarial tempo | Bandwidth advantage | Opponent modeling speed | OODA loop advantage | Attacker-defender asymmetry |
| Sub-additive tempo | — | — | Brooks's Law | Communication overhead |
| Structural adaptation | Model switching | Architecture search | Organizational restructuring | Major refactoring |

The persistence condition, for example, says a software team must iterate fast enough, with good enough feedback, relative to how fast requirements are changing and how complex the codebase is. The same inequality, with different instantiations of $\alpha$, $\rho$, and $R$, governs whether a Kalman filter tracks a maneuvering target, whether an RL agent converges in a non-stationary environment, and whether a military unit maintains situational awareness under adversarial deception.


## Maturity Gradient

The theory's mathematical closure varies by section and is expected to.

**Section I (Adaptive Systems)** is mathematically closed. Mismatch dynamics, gain structure, the persistence condition, and adversarial tempo form a coherent chain with exact results and simulation validation. Section I is the foundation everything else builds on.

**Section II (Actuated Adaptation: Agentic Systems)** has a strong diagnostic core (satisfaction gap and control regret as orthogonal diagnostics; the orient cascade as forced ordering; directed separation as architectural classification) and a maturing operational layer (strategy DAGs with derived structure; a schema for strategy persistence with multiple verified instances; a characterization of where credit assignment is tractable and where it is structurally hard). The bias bound for fully-coupled (Class 2) agents is a conditional theorem under named sub-scopes.

**Section III (Agentic Composites)** has its bridge lemma connecting micro-dynamics to macro-dynamics, a contraction template generalizing the sector machinery to non-Euclidean metrics, closed-form composition results in symmetric-matched cases, and equilibrium-convergence framing for partially-opposing objectives. Recipient-side and emitter-side interaction-channel classifications carry the inter-agent dynamics. Open: latent structural diversity, endogenous coupling dynamics, composition transition dynamics under regime change, computational thresholds for social behavior.

**Domain instantiations.** TST (`02-tst-core/`) is grounded by AAD and contributes the calibration-laboratory framing. Logogenic agents (`03-logogenic-agents/`) operate from a coupled formulation; what survives without directed separation is the active research question. Logozoetic agents (`04-logozoetic-agents/`) are largely future work — the conceptual groundwork exists but the formal machinery does not.

This gradient — exact core, principled architecture in the middle, open formulation at the edges — is the expected arc for a theory that aims to describe agentic systems rather than produce a purely mathematical artifact.


<!-- AUTO-GENERATED by bin/extract-findings; do not hand-edit. -->
<!-- README-shaped condensed surfacing. Full content at FINDINGS.md. -->

## Novel Results & Findings

Distinctive results from the framework, with epistemic tiers and links into the segments. Full content (impact, caveats, casual-reader framing) at [`FINDINGS.md`](FINDINGS.md).

### I. Adaptive Systems Under Uncertainty

- **`#result-persistence-condition`** *(Exact)* — Adaptive systems persist when correction efficiency exceeds disturbance rate relative to model class capacity ($\alpha \gt \rho/R$); the result decomposes into a structural-persistence half (the machinery contains mismatch) and a task-adequacy half (the contained mismatch is small enough for the domain).  
  [`01-aad-core/src/result-persistence-condition.md`](01-aad-core/src/result-persistence-condition.md)

### Appendices: Details

- **`#deriv-edge-update-natural-parameter`** *(Conditional)* — The log-odds coordinate $\lambda = \log(p/(1-p))$ is the unique smooth strictly-monotone reparameterization (up to positive affine transformation) on which independent Bernoulli evidence updates Bayesian credences additively, with the uniqueness following from Cauchy's functional equation operating on an evidential-additivity axiom motivated as the update-level analog of the chain-layer log-additive identity.  
  [`01-aad-core/src/deriv-edge-update-natural-parameter.md`](01-aad-core/src/deriv-edge-update-natural-parameter.md)
- **`#deriv-causal-ib-lmi`** *(Conditional)* — The scalar Causal-IB survival-imperative exploration drive lifts to a Linear Matrix Inequality on the Fisher Information Matrix, with a positive-semidefinite matrix Lagrange multiplier $\Lambda$ that distinguishes by direction; complementary slackness mathematically forbids "blank wall" actions that satisfy the scalar bound by sourcing information in non-drifting subspaces.  
  [`01-aad-core/src/deriv-causal-ib-lmi.md`](01-aad-core/src/deriv-causal-ib-lmi.md)
- **`#disc-additive-coordinate-forcing`** *(Robust qualitative)* — AAD repeatedly forces a privileged coordinate (logarithmic at the chain, divergence, and update layers; Fisher-Rao at the metric layer) by combining an AAD-internally-motivated additivity axiom with a uniqueness theorem (Cauchy's functional equation or Čencov's invariance theorem); the four forced coordinates resolve to a single underlying object — the exponential-family Legendre-Fenchel geometry.  
  [`01-aad-core/src/disc-additive-coordinate-forcing.md`](01-aad-core/src/disc-additive-coordinate-forcing.md)
- **`#result-contraction-template`** *(Conditional)* — AAD's Euclidean sector-persistence template generalizes to a contraction-metric template (Lohmiller-Slotine 1998 machinery) that promotes five additional agent classes from sub-scope $\beta$ (assumed A2') to sub-scope α₁/α₂ (derived A2' under explicit conditions), supports topology-indexed compositional closures (parallel / cascade / feedback / general-graph) for heterogeneous-architecture composites, and integrates with `#disc-additive-coordinate-forcing`'s (PI)/Čencov axiom to derive Fisher-metric cases AAD-internally.  
  [`01-aad-core/src/result-contraction-template.md`](01-aad-core/src/result-contraction-template.md)
- **`#deriv-bias-bound`** *(Conditional)* — The constant $C$ in the Class-2 (fully-coupled) agent observation-ambiguity bias bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is derived under two named tracks: a transport-inequality track (linear in $I$, $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ under log-Sobolev + Lipschitz-posterior conditions) and a Fisher-Rao track ($\sqrt I$ scaling, universal dimension-free $C_{FR} = \sqrt 2$ under the (PI) parameterization-invariance axiom + small-$I$ regime).  
  [`01-aad-core/src/deriv-bias-bound.md`](01-aad-core/src/deriv-bias-bound.md)



<!-- AUTO-GENERATED by bin/extract-recent-progress; do not hand-edit. -->
<!-- Surfaces the 3 most recent cycle narratives from CHANGELOG.md. -->

## Recent Progress

The 3 most recent cycle narratives. Full record at [`CHANGELOG.md`](CHANGELOG.md); pre-2026-04-24 archaeology at [`LOG.md`](LOG.md).

### Causal-IB matrix-form lift and transient-amplification spike

*2026-04-25*

After the audit-extraction batch landed earlier in the day, two substantive theory threads extended AAD's matrix-form bound machinery.

### Audit-extraction batch and cross-agent peer review

*2026-04-25*

Eight FINAL audit reports under `msc/AUDIT-WORKING-{584721, 613842, 738192, 742613, 849201}/` were triaged into a banded candidate file (`msc/audit-final-reports-candidate-extraction-2026-04-25.md`): §A high-confidence local fixes (14 candidates), §B already-tracked, §C strengthening-needed (4 items, escalated), §D architectural (5 items, mapped to existing PROPOSALS bands), §E borderline. The §A batch was dispatched as 7 parallel verify-then-fix agents under the discipline "the finding is *suspected*, not confirmed — verify in current segment text first; strengthen-before-soften before any softening; FORMAT discipline is non-negotiable." Landings (commits `4f0315e`, `937743d`, `3e87f59`, `1bffa60`, `fb51ff9`):

### Cross-agent peer review: Causal-IB exploration drive

*2026-04-25*

Concurrent with the audit-extraction batch, a Gemini agent landed a Causal-Information-Bottleneck spike-promotion: new derivation segment `deriv-causal-ib-exploration.md` deriving exploration as a Lyapunov-survival imperative. Initial framing: "the unified objective is the *exact Lagrangian relaxation* of the persistence constraint" with epistemic status upgraded to *Derived (conditional)*. Peer review caught a $U_M$-direction flip ($\eta^* \propto 1/U_M$ for small $U_M$ should be $\propto U_M$) which propagated to the wrong sign on the final Lagrange multiplier. The strengthen-first discipline cuts both ways: a strengthening attempt should be honestly verified *before* status upgrade, just as a softening should be tried *after* a strengthening attempt.



<!-- AUTO-GENERATED by bin/extract-known-issues; do not hand-edit. -->
<!-- Rolls up Known Fragilities, PROPOSALS portfolio (§B/§C/§D titles), and OUTLINE GAPs. -->

## Known Issues & Open Questions

This section surfaces what the framework currently acknowledges as open at the orientation level. For active work items see [`TODO.md`](TODO.md); for architectural proposals under review see [`PROPOSALS.md`](PROPOSALS.md); for component-level GAPs see each component's `OUTLINE.md`.

### Known Fragilities — what falls outside formal scope

- Missing commitment / resource / temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation

*Source: [`CLAUDE-2.md`](CLAUDE-2.md).*

### Architectural proposals under review

**§B — Ready now.**
- B.1 Framework-face reframe bundle (see §Cross-cutting view, Bundle 1)
- B.2 Section III completion — entry points (see §Cross-cutting view, Bundle 2)
- B.3 C-BP1 + C-BP4 bundle — epistemic separation framework + claim-level statuses

**§C — Soon.**
- C.1 O-BP13 — Cox-parallel necessity for `#deriv-graph-structure-uniqueness`
- C.2 O-BP15 — Comprehensive "minimal proof of viability" worked example
- C.3 SP-14 — Observation-channel capacity $C^{(k)}$ as first-class notation
- C.4 SP-19 — Naming consolidation pass

**§D — Later.**
- D.1 O-BP11 — Observability as master variable across the theory
- D.2 Section III completion — upstream pieces (see Bundle 2)
- D.3 G-BP3 — Fisher-information unification of tempo and gain
- D.4 SP-12 — Commitment / resource / temporal DAG extensions
- D.5 SP-13 — Emergence conditions as formal primitive
- D.6 O-BP12 — Resource budget $B_t$ as master variable
- D.7 SP-15 — Template-family naming (sector / contraction / dissipativity trio)
- D.8 SP-16 — Independence-audit as empirical profiling instrument

*Full portfolio with merits, scope, and prior reasoning: [`PROPOSALS.md`](PROPOSALS.md).*

### Component-level GAPs

**`01-aad-core`:**
- Latent structural diversity: variation in correction architectures invisible to persistence analysis, consequential under regime change
- Endogenous coupling: γ as function of population composition, not exogenous parameter; coupling emergence threshold
- Composition transition dynamics: epochal stability → latent diversification → niche emergence → cascading restructuring → re-equilibration (adopts Miller 2022's extreme transition motif)
- Computational thresholds for social behavior: minimum agent complexity and interaction depth for composition dynamics (adopts Miller 2022's ICE framework; grounds #form-strategy-complexity-cost)

**`02-tst-core`:**
- Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$
- Software persistence: the unmaintainability threshold formalized

**`03-logogenic-agents`:**
- Language-specific orient cascade (what's specific to logogenic agents?) — partially addressed by D3, R2
- Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents
- AAD-grounded experiential training environments
- Self-referential closure: AAD agent on AAD codebase



## Navigation

### Reading paths

- *Conducting a de-novo audit of the framework?* Please read [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) first; it documents the recommended posture and the failure modes prior audit cycles surfaced. Use [`README-auditor.md`](README-auditor.md) instead of this file.
- *Academic reader evaluating the framework's claims?* Recommended sequence: this README → [`FINDINGS.md`](FINDINGS.md) (curated novel results with epistemic tiers) → [`01-aad-core/OUTLINE.md`](01-aad-core/OUTLINE.md) (canonical theory outline) → individual segments under `01-aad-core/src/`.
- *Engineer or practitioner?* The [Cross-Domain Joining](#cross-domain-joining) table maps AAD concepts to the domain you likely care about; from there, follow the relevant component OUTLINE.
- *Picking up active work on the framework?* [`TODO.md`](TODO.md) is the navigator for current work items, and [`PROPOSALS.md`](PROPOSALS.md) is the architectural-proposal portfolio.

### Project layout

```
01-aad-core/          AAD mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md          Canonical theory outline (claim by claim)
  src/                Claim segments (one per file, named by slug)
02-tst-core/          Temporal Software Theory (AAD-grounded)
03-logogenic-agents/  Language-constituted agents (framework stage)
04-logozoetic-agents/ Language-living agents (future work)

OUTLINE.md            Top-level assembly index
LEXICON.md            Prose vocabulary (cycle phases, agent classes)
NOTATION.md           Symbol reference
FORMAT.md             Segment file conventions
FINDINGS.md           Curated novel-results catalog (auto-generated)
TODO.md               Active work items
PROPOSALS.md          Architectural-proposal portfolio
CHANGELOG.md          Forward-going cycle record (2026-04-24 onward)
LOG.md                Pre-2026-04-24 cycle archaeology (frozen)
MIGRATION-MAP.md      Prior-work absorption tracking

doc/                  Long-lived process documentation
  de-novo-audit-instructions.md
  naming-principles.md
  readme/             Templates and partials for README generation
msc/                  Working documents, spikes, brainstorms
  SPIKES.md           Spike index
ref/                  Reference papers
bin/                  Build, lint, generation scripts
_obs/                 Superseded materials
```


## Contributing

ASF is research-stage work; contributions take a few specific forms.

**Engaging with the theory.** The most valuable contribution is *de-novo evaluation*: read segments without first reading existing audits or pending findings, form independent judgments, and surface what you find. Where you disagree with a claim or its scope, that is signal. Procedure: see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md). Read [`README-auditor.md`](README-auditor.md) instead of this README for the audit-safe framing.

**Adding theory content.** Segments are added under `{component}/src/` following [`FORMAT.md`](FORMAT.md) conventions: YAML frontmatter (slug, type, status, dependencies); one-sentence summary; Formal Expression with epistemic tags; Epistemic Status; Discussion; optional Findings; optional Working Notes. Promotion follows a four-gate workflow detailed in FORMAT.md. Slugs follow `{type-prefix}-{subject-noun}` and are aligned mechanically by [`bin/align-slug`](bin/align-slug).

**Spikes.** Speculative or in-progress work that is not yet ready for segment promotion lives under `msc/spike-{topic}.md`. Spikes are honest reasoning trails; results that promote out of spikes land in segments per the math-lives-in-segments discipline.

**Tooling.** Internal process scripts (build, extract, lint) are written in Ruby; community-facing tooling (simulations, reproducibility scripts) is written in Python. New scripts in `bin/` follow this convention; existing scripts that don't are not retroactively rewritten.

**Reporting issues.** Open an issue on GitHub or contact the project maintainer (see commit history).

