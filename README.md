# ACT: Agentic Cycle Theory

A first-principles mathematical theory of adaptive, purposeful agents under uncertainty.

## What ACT Is

ACT unifies three aspects of agency that existing theories treat separately:

1. **Adaptive feedback dynamics** — how agents build and maintain models of reality under environmental change. Originally developed as Temporal Feedback Theory (TFT, now subsumed): mismatch signals, update gain via the uncertainty ratio, adaptive tempo, persistence conditions, adversarial dynamics.

2. **Actuated (purposeful or goal-driven) agency** — how agents hold, pursue, and revise goals. Objectives ($O_t$) and strategy ($\Sigma_t$) are distinct formal objects. Strategy is formalized as a probabilistic causal DAG encoding the agent's theory of how its actions produce goal-achievement.

3. **Composition and shared intent** — how agents compose into larger agents and communicate purpose under uncertainty. Intent compression via the information bottleneck (the Auftragstaktik insight). Composition consistency as a requirement, not a feature.

Beneath all three is a single recurring pattern: **an agent persists when its internal correction outpaces external challenge.** For an individual, this means adaptive tempo must exceed the rate of environmental disturbance — the persistence condition. For a composite (a team, an organization, a swarm), it means internal coordination must equilibrate faster than the external dynamics change — the composition threshold. Both are measurable. Both are comfortably satisfied by most competent agents. The interesting theory lives near the boundary where they aren't.

The theory progresses from general adaptive systems through actuated agency and multi-agent composition to domain instantiations — particularly software development and AI agents operating on code.


## Where to Start

**[`CURRENT-FULL-THEORY.md`](CURRENT-FULL-THEORY.md)** — the canonical outline. The full argument claim by claim, with the current linearization, types, and development stage for each segment.

**[`WORKBENCH.md`](WORKBENCH.md)** — development state: what's written, what's open, known fragilities, spike status, prior-work migration map.

**[`FORMAT.md`](FORMAT.md)** — segment file conventions: frontmatter, document cadence, math formatting, cross-references, epistemic labeling.

**[`notation.md`](notation.md)** — all symbols used in ACT, serving as single authoritative reference.


## Structure

**The theory lives in [`src/`](src/).** Each file is one claim — an axiom, definition, theorem, or hypothesis — named by slug (`src/{slug}.md`). Claims build incrementally, like a proof. One move per file: given what came before, this one thing follows, or is defined, or restricts scope.

Five sections scope progressively:

1. **Adaptive Systems Under Uncertainty** — the general case (from TFT)
2. **Actuated Adaptive Systems** — adding objectives and strategy
3. **Composition and Coordination** — multiple agents, composite agents
4. **Evolving Software Systems** — TST regrounded in ACT's formal machinery
5. **Software-Grounded Agentic Systems** — AI agents, the recursive completion

Canonical ordering lives in `CURRENT-FULL-THEORY.md`, not in filenames. Slugs are the stable identities; the linearization will change as the theory develops.


## Key Results

### Section I — Adaptive Systems (nearing completion)

The formal backbone is the Lyapunov/sector-condition analysis — general, nonlinear, robust. The linear ODE is pedagogical, correct in its regime, not the general case.

- **Uncertainty ratio principle**: $\eta^* = U_M / (U_M + U_o)$ — validated empirically (52% mismatch reduction with Riccati-optimal gain)
- **Persistence condition**: $\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$ — robust across all correction functions tested
- **Adversarial tempo advantage**: superlinear in coupling-dominant regimes (exponent = 2 deterministic, 3/2 stochastic, ~1 non-coupling-dominant)
- **Observation quality gates tempo advantage**: $U_o$ collapses adversarial exponent from ~1.0 to ~0.2 — formally grounding Boyd's emphasis on Orient quality over raw OODA speed
- **Structural adaptation necessity** — catastrophic breakdown observed at predicted threshold

### Section II — Actuated Adaptive Systems (derivation mature, segments in progress)

The derivation chain is in `scratch/spike-v3-purposeful-agent.md`. Porting to segment files is the remaining work.

- **Strategy as probabilistic causal DAG** with AND/OR nodes and single-parameter edges — converged across three independent formalism attempts
- **Orient cascade**: observation → $M_t$ update → $\Sigma_t$ edge revision → feasibility check → possible $O_t$ revision
- **Satisfaction gap / control regret split**: separates "infeasible goal" from "bad strategy"
- **DAG acyclicity derived** from temporal ordering over finite planning horizons
- **Directed separation**: $M_t$ update function is $G_t$-independent (conditional on realized action and event)

### Section IV — Evolving Software (in active conversion from TST)

TST's claims are being systematically integrated with ACT's formal machinery — not just relabeled, but rederived where possible and honestly tagged where not.

- **Median prediction, not expectation**: TST's $\hat{n}_{\text{future}} = n_{\text{past}}$ is a median under Jeffrey's prior on Pareto($\alpha = 1$), whose mean diverges. This affects all downstream quantitative claims.
- **Dual optimization with turnover multiplier**: comprehension cost compounds per-reader; implementation cost does not. Under 100% AI context turnover, comprehension dominates overwhelmingly.


## Current Status

~99 claims mapped across five sections. 85 segments at draft, 14 remaining. Sections I (28) and II (20) are complete. Section III (11/13) has its backbone and simulation results written — two segments remain (Appendix F extraction). Section IV (20/24) is in active conversion from TST. Section V (3/6) and appendices (3/8) have source material identified.

See [`WORKBENCH.md`](WORKBENCH.md) for detailed development state, open questions, known fragilities, and prior-work migration progress.


## Repository Layout

```
act/
├── CURRENT-FULL-THEORY.md   Canonical outline — start here
├── FORMAT.md                 Segment file conventions
├── WORKBENCH.md              Development state and working notes
├── notation.md               Symbol reference
├── CLAUDE.md                 Context for AI agents
│
├── src/                      The theory — claim segments by slug
│   ├── {slug}.md             ACT segments
│   ├── old-tf-*.md           TFT source material (being absorbed)
│   └── old-tst-*.md          TST source material (being converted)
│
├── scratch/                  Working documents and spikes
│   ├── spike-v3-purposeful-agent.md    Definitive Section II derivation
│   ├── spike-agent-composition.md      Composition/holon theory
│   ├── spike-graph-uniqueness.md       DAG structure uniqueness argument
│   ├── 04-intent-dag-consolidated.md   Canonical intent DAG reference
│   ├── track-a-intent-dag/             DAG formalism variants (historical)
│   └── track-b-nonlinear-sims/         Simulation code and results
│
├── _archive/                 Superseded documents
├── refs/                     Reference papers (Hafez 2026, IBM 2025)
└── priors/                   Git submodules (historical only —
    ├── tft/                    all content copied to src/old-tf-*)
    └── tst/                    all content copied to src/old-tst-*)
```


## Prior Art and Positioning

- **BDI** (Rao & Georgeff): Named the parts but has no dynamics. ACT provides the physiology.
- **Active Inference** (Friston): Unifies perception and action under free energy. ACT uses causal feedback dynamics — more transparent and measurable. Expected free energy ≈ ACT's value + $\lambda$ CIY (structural isomorphism, different foundations).
- **Hafez et al. 2026**: Bi-predictability metric ($P$). Complementary — $P$ diagnoses architecture, mismatch diagnoses performance.
- **IBM "Agentic AI Needs a Systems Theory" 2025**: Articulates the void ACT fills. Their open challenges (subgoal emergence, residual control rights) are directly addressed by ACT.
- **TST**: Software domain theory. Gets full treatment in Section IV, regrounded in ACT's formal machinery. TST's claims are honestly scoped and carefully stated; ACT adds the causal mathematics and adaptive dynamics, not rigor — TST already had that.
