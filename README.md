# Agentic Systems

A research framework for adaptive, purposeful agents under uncertainty — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

![Abstract illustration of Agentic Systems](abstract-dl.png)


## What This Is

ACT connects established mathematical tools — Lyapunov stability, Kalman filtering, the information bottleneck, causal DAGs, singular perturbation theory — into a single coherent account of what makes an agent persist, adapt, and compose. The individual pieces are well-established. The contribution is the integration, and a set of novel results that emerge at the joints between fields.

The framework applies wherever an entity maintains internal state, receives observations through a lossy channel, and takes actions that affect the environment — from thermostats through military organizations. Domain-specific instantiations (software development, language-constituted agents) are grounded by ACT's core theory but developed independently.


## Structure

**[Agentic Cycle Theory (ACT)](01-act-core/OUTLINE.md)** is the mathematical core. It formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis. The cycle unfolds in five phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis), and everything in the core theory is ultimately about cycle properties: what makes them effective, how fast they must run, and when they fail or must change in kind.

**[Temporal Software Theory (TST)](02-tst-core/OUTLINE.md)** is software development viewed as an agentic domain — grounded in ACT but independently consequential. TST formalizes why time-optimal development practices work, how code quality affects adaptive capacity, and what makes software systems persist or collapse.

**[Logogenic Agents](03-logogenic-agents/OUTLINE.md)** — Language-constituted agents (including LLMs). Framework stage — informed by ACT's formal machinery but not yet at ACT's level of mathematical formalization.

**[Logozoetic Agents](04-logozoetic-agents/OUTLINE.md)** — Language-living agents whose persistence is morally weighted. Future work.


## Novel Results

These are ACT's genuine mathematical contributions — results that emerge from the integration and can be stated independently.

**Persistence condition.** A single inequality governing adaptive system viability: the correction efficiency must exceed the disturbance rate relative to model class capacity (α > ρ/R). Derived from sector-condition Lyapunov analysis; generalizes across correction function classes. This is the theory's central result — it connects control theory's stability analysis to the question of when any adaptive system (a thermostat, a development team, a learning agent) can maintain coherent function.

**Acyclicity from temporal ordering.** Strategy graphs over finite planning horizons must be acyclic — derived from the irreversibility of time, not assumed as a structural convenience. Any directed graph whose edges represent "X causally precedes Y" over a finite set with real-valued timestamps is forced to be a DAG.

**Satisfaction gap / control regret split.** Decomposes the gap between desired and actual outcomes into two orthogonal diagnostics: "the world doesn't permit it" (satisfaction gap: objective exceeds attainability) versus "you're not doing it well enough" (control regret: current policy underperforms the best available). The 2×2 diagnostic disambiguates four corrective-action regimes.

**Adversarial tempo exponents.** When two coupled agents compete, the faster agent's advantage scales with a regime-dependent exponent: b ≈ 2 (deterministic drift, coupling-dominant), b ≈ 3/2 (stochastic noise, coupling-dominant), b → 1 (non-coupling-dominant). These emerged from simulation forcing a theory revision — the original theory predicted a single exponent.

**Orient cascade as forced ordering.** The resolution order within the adaptive cycle (epistemic update → attainability assessment → regret computation → strategic calibration → objective revision) is not a design recommendation but a mathematical consequence of information dependency: each step's input requires the previous step's output.

**Composition bridge lemma.** Bounded closure defect between individual and composite dynamics implies bounded trajectory error, via the same Lyapunov contraction argument that grounds Section I. This connects the composition story to the persistence machinery.

**Feedback loop as Level 2 causal engine.** Any agent in a feedback loop generates interventional data by construction — the agent's action causally precedes the next observation. This connects control theory's feedback structure to Pearl's causal hierarchy without requiring the agent to explicitly perform experiments.

**Observability dominance.** Unobservable strategy edges freeze at their prior (the gain principle drives update rate to zero). Paths through unobservable nodes become "epistemically dead" — an absorbing state the agent cannot escape without structural change. This connects the information-theoretic gain principle to strategic planning.

**Structural adaptation necessity.** When model class fitness is insufficient, no parametric adaptation can close the mismatch floor — the agent must change its model class, not just its parameters. Derived from the information bottleneck applied to model sufficiency.

**Directed separation as architectural classification.** Whether epistemic updates are goal-blind is determined by processing topology, not by a tunable coupling parameter. Three classes: modular (separation by construction), fully merged (fails by construction), partially modular. This resolved a major open issue — the earlier κ-as-scalar framing was a category error.


## Cross-Domain Joining

The framework's power is that the same formal objects appear with concrete instantiations across domains. Results proved in one domain automatically have consequences in the others:

| ACT concept | Control theory | RL / bandits | Organizations | Software |
|-------------|---------------|--------------|---------------|----------|
| Adaptive tempo T | Bandwidth × gain | Learning rate × coverage | Decision speed × information quality | Iteration frequency × feedback quality |
| Persistence condition | Stability margin | Convergence condition | Organizational viability | Maintainability threshold |
| Mismatch signal δ | Innovation sequence | Reward prediction error | Intelligence gap | Test failures, bug reports |
| Update gain η* | Kalman gain | Learning rate | Trust-weighted integration | Code review acceptance |
| Satisfaction gap | Tracking error floor | Regret lower bound | Strategic ceiling | Spec-reality gap |
| Adversarial tempo | Bandwidth advantage | Opponent modeling speed | OODA loop advantage | Attacker-defender asymmetry |
| Sub-additive tempo | — | — | Brooks's Law | Communication overhead |
| Structural adaptation | Model switching | Architecture search | Organizational restructuring | Major refactoring |

The persistence condition, for example, tells you that a software team must iterate fast enough, with good enough feedback, relative to how fast requirements are changing and how complex the codebase is. The same inequality, with different instantiations of α, ρ, and R, governs whether a Kalman filter tracks a maneuvering target, whether an RL agent converges in a nonstationary environment, and whether a military unit maintains situational awareness under adversarial deception.


## Convergent Choices

A category between "derived from first principles" and "arbitrary framework decision" — representational choices where all investigated alternatives fail or converge to the same structure:

**AND/OR node types for strategy.** Three independent formalism attempts (general CPT, noisy-OR, weighted combination) converged on AND/OR as the only workable basis. Noisy-OR was rejected for non-identifiability; weighted combination for parameter explosion (2^k vs. k). A parsimony theorem (AND/OR as the unique minimal complete basis under the theory's constraints) would promote this to "derived."

**Single-parameter edges.** Alternatives (multi-parameter credences, edge-specific distributions) were tried and abandoned. The convergence suggests this is not arbitrary but forced by the interaction between the uncertainty ratio principle and the chain-confidence identity.

**P3→Markov condition.** The postulate that strategy must be locally revisable, combined with temporal ordering and causal sufficiency, appears to force the Markov property on the strategy DAG. Currently conditional on causal sufficiency (which is guaranteed for agent-constructed strategies). If the conditioning can be removed, this promotes to a derived result — analogous to how acyclicity was once assumed and is now derived.

These sit between "we chose this" and "this is the only option." Tracking them separately from pure framework choices tells the reader: *we didn't just pick this; we tried everything else and it didn't work.*


## Maturity Gradient

The theory's mathematical closure varies by section, and this is by design:

**Section I (Adaptive Systems)** is mathematically closed. The recursive-update derivation, sector-condition Lyapunov proofs, persistence condition, and adversarial dynamics form a coherent chain with exact results, simulation validation, and an end-to-end Kalman worked example. This is the foundation everything else builds on.

**Section II (Purposeful Agents)** has a strong diagnostic core (satisfaction gap, control regret, orient cascade ordering, directed separation) and an incomplete operational layer. The strategy-maintenance loop — how agents actually revise their plans — has the right structure but three unresolved pieces: the signal function for edge updates is undefined, credit assignment for multi-parent nodes is unresolved, and strategy persistence is a schema awaiting instantiation. Section II is best understood as a well-typed diagnostic architecture waiting for a minimal strategic dynamics result.

**Section III (Agentic Composites)** has the bridge lemma connecting closure defect to trajectory error, plus a set of qualitative conceptual contributions (unity dimensions, shared intent, Auftragstaktik principle). It becomes convincing after projection admissibility and strategy dynamics are made concrete. Section III is best understood as a research program scaffold built on Section I's Lyapunov machinery.

This gradient — from exact core through principled architecture to open formulation — is the expected arc for a theory that aims to describe agentic systems rather than produce a purely mathematical artifact.


## Where to Start

- **[`OUTLINE.md`](OUTLINE.md)** — Top-level assembly index across all parts.
- **[`01-act-core/OUTLINE.md`](01-act-core/OUTLINE.md)** — The ACT mathematical core, claim by claim.
- **[`LEXICON.md`](LEXICON.md)** — Prose vocabulary: cycle phases, agent classes, key terms.
- **[`WORKBENCH.md`](WORKBENCH.md)** — Development state: what's settled, what's open, known fragilities.
- **[`FORMAT.md`](FORMAT.md)** — Segment file conventions.
- **[`NOTATION.md`](NOTATION.md)** — Symbol reference.


## Project Layout

```
01-act-core/            ACT mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md            Theory outline (claim-by-claim)
  src/                  Claim segments (one per file, named by slug)

02-tst-core/            Temporal Software Theory (ACT-grounded)
  OUTLINE.md            Software theory outline
  src/                  Software domain segments

03-logogenic-agents/    Language-constituted agents (framework)
  OUTLINE.md            Logogenic framework outline

04-logozoetic-agents/   Language-living agents (future work)
  OUTLINE.md            Logozoetic framework outline

OUTLINE.md              Top-level assembly index
LEXICON.md              Prose vocabulary (spans whole project)
NOTATION.md             Symbol reference (spans all sections)
FORMAT.md               Segment file and general md conventions
WORKBENCH.md            Development state

msc/                    Working documents, spikes, derivation attempts
ref/                    Reference papers
bin/                    Build and lint tools

_obs/                   Superseded materials
```
