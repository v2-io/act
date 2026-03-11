# CLAUDE.md — Context for AI Agents Working on ACT

## What This Project Is

ACT (Agentic Cycle Theory) is a first-principles mathematical theory of
adaptive, purposeful agents. It supersedes and subsumes Temporal Feedback
Theory (TFT, in priors/tft/), which provides the adaptive-systems
foundation. TFT is prior work now absorbed into ACT, not a separate
co-existing theory.

This is theoretical research, not software engineering. The primary artifacts
are mathematical formalisms and claim segments. Quality means rigor, honesty
about epistemic status, and clarity for future readers — not code coverage.

## Where to Start

**Read `src/000-contents.md` first.** This is the master outline — the whole
argument in plain English. It maps ~75 claims across five sections, shows
what's written, and marks gaps honestly.

**Read `priors/tft/TF-00.md`** for the notation conventions and epistemic
system that ACT adopts.

## Theory Structure

The theory lives in `src/` as claim segments. **Each file is like a
high-level proof step** — one move per file. Given what came before, this
one thing follows, or is defined, or restricts scope. An assumption and
the theorem derived from it are two steps, not one. Corollaries and
alternate formulations can live with their parent claim (they reinforce
its independence), but anything that could be referenced independently
should be its own file.

**TFT's file structure is NOT the model — it's what went wrong.** TFT's
monolithic multi-claim documents are the problem ACT fixes. TST's
one-claim-per-section cadence is the structural model. TFT conventions
are adopted ONLY for epistemic labeling (equation-level tags, tiers).

**File identity and ordering:**
- The **slug** is the file's identity. Everything references by
  `#slug-name`, never by number.
- Numbering is the current best linearization of the dependency DAG —
  it WILL change. Expect files to move between sections, be renumbered,
  and be inserted or removed as the theory refines.
- YAML frontmatter: `slug`, `type`, `depends` (list of prerequisite
  slugs). The type of each dependency (definition import vs logical
  antecedent vs scope assumption) is derivable from the referenced
  file's own `type` field — no typed edges needed.
- Five sections scope progressively: I. Adaptive Systems, II. Actuated
  Adaptive Systems, III. Composition and Coordination, IV. Evolving
  Software, V. Software-Grounded Agentic Systems

**Cadence per file:**
1. YAML frontmatter (slug, type, depends)
2. Title
3. One-sentence summary
4. Formal Expression (with equation-level tags)
5. Epistemic Status paragraph
6. Discussion (interpretation, connections — brief)

Definition/notation and scope-narrowing files may use a simpler format
than full claims.

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to
reality (mismatch signals, gain, tempo, persistence). But it has no
treatment of goals. ACT adds:

- **O_t** (objective — what the agent wants) and **Σ_t** (strategy — how
  it plans to get there) alongside **M_t** (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes,
  edges with confidence weights p, update via the uncertainty ratio)
- The **Orient cascade**: observation → M_t update → Σ_t edge revision →
  feasibility check → possible O_t revision
- **Directed separation**: M_t dynamics independent of O_t/Σ_t; Σ_t
  depends on M_t; action couples all three
- **G_t = (O_t, Σ_t)**: the purposeful substate decomposes into objective
  (evaluation) and strategy (guidance) — a definitional split, not a
  timescale claim

## Epistemic Conventions

Follow TFT's conventions exactly (see priors/tft/TF-00.md):

**Equation-level tags** (inline before equations):
- `*[Definition]*`, `*[Derived]*`, `*[Derived (Conditional on ...)]*`
- `*[Hypothesis]*`, `*[Empirical Claim]*`, `*[Formulation]*`
- `*[Discussion]*`, `*[Assumption]*`

**Document-level Epistemic Status paragraph** at the top of each segment,
explaining what's derived vs hypothesized vs discussion-grade. Example:
"The threshold's *existence* is *robust qualitative*. The quantitative form
is *exact* under assumptions GA-2, GA-3."

**Claim tiers** (from TF-00's Claim Registry):
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are
not TFT terms.

**Every claim must be grounded.** If stated as fact, it needs its own
derivation or is explicitly tagged as hypothesis/empirical/discussion-grade.
Do not let ungrounded assertions transfer from TST uncritically.

## Key Architectural Decisions

1. **ACT supersedes TFT.** Don't modify priors/tft/ documents. Don't treat
   TFT as a separate co-existing theory.

2. **Claim segments, not chapters.** New theory content goes in `src/` as
   individual claim files, not in ACT-01/ACT-03 style chapter documents.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism
   attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **TST gets full treatment in Section IV.** Not just domain table rows.
   T-01 (temporal optimality) is generalized as ACT's first axiom (#010).

## What's Settled vs. Open

### Settled (from convergence testing + spikes)
- Single-parameter edges with AND/OR nodes
- Orient cascade structure (now derived from information dependency)
- Additive log-confidence decay (generalizes p^n)
- Observability as strategy enablement
- Directed separation (with explicit scope condition for goal-conditioned agents)
- G_t = (O_t, Σ_t) split (definitional, not timescale-dependent)
- Satisfaction gap / control regret split (replaces simpler δ_objective)
- DAG acyclicity derived from temporal ordering (former fragility resolved)
- Composition consistency required (not optional) by scope condition's
  level-independence

### Open (see Section II gaps in contents)
- Action-deliberation-exploration tradeoff (three-way with Σ_t)
- Strategy tempo formalization
- Cognitive cost of Σ_t (no β analog yet)
- Edge identifiability conditions (resolved in software, open in general)
- P3→Markov step in graph uniqueness (sketch, needs tightening)
- Composition laws (specific forms are sketches; existence is required)

### Known Fragilities
- Edge semantics claim interventional but update from observational
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) —
  acknowledged as scope restriction, not a bug

## Simulation Findings

The track-b simulations (scratch/track-b-nonlinear-sims/) validated and
refined specific claims:

- Cor. 11.2's exponent = 2 under deterministic drift (confirmed: 1.999)
- Under stochastic disturbances, exponent = 1.5 (not 2.0)
- Observation noise collapses adversarial exponent from ~1.0 to ~0.2
- Per-dimension persistence exact (scalar overestimates by 72%)
- TF-06's gain principle empirically validated (52% reduction)

## File Organization

- `src/` — **The theory.** Claim segment files. Start with
  `000-contents.md` for the map.
- `_archive/` — Superseded root-level docs (ACT-01.md, ACT-03.md).
  Content extracted to src/ segments; preserved for archaeology.
- `priors/tft/` — TFT submodule (read-only reference for epistemic
  conventions and adaptive-systems foundation)
- `priors/tst/` — TST submodule (read-only; content regrounded in src/)
- `refs/` — Reference papers
- `scratch/` — Working documents, spikes, historical artifacts
  - `spike-v3-purposeful-agent.md` — Definitive Section II derivation
  - `spike-agent-composition.md` — Composition/holon theory
  - `spike-graph-uniqueness.md` — DAG structure uniqueness argument
  - `04-intent-dag-consolidated.md` — Canonical intent DAG reference
  - `track-a-intent-dag/` — DAG formalism variants (historical)
  - `track-b-nonlinear-sims/` — Simulation code and results
- `../agentic-tft/` — Prior bridge work: TFT → AI agents. Docs 10-14
  relevant to Section V.
