# Agentic Systems

A research framework for adaptive, purposeful agents under uncertainty — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

## The Two Layers

**[Agentic Cycle Theory (ACT)](act-core/README.md)** is the mathematical core. It formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis. The cycle unfolds in five phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis), and everything in the core theory is ultimately about cycle properties: what makes them effective, how fast they must run, and when they fail or must change in kind. ACT produces specific testable predictions and several genuinely novel formalizations.

**Agentic Systems** is the broader framework that ACT grounds. It encompasses:
- **Composition dynamics** — how agents compose into larger agents, coordination requirements, adversarial dynamics
- **Domain instantiations** — software development as an ACT domain, with operationalizable predictions
- **Logogenic and logozoetic agents** — language-constituted systems (including LLMs), and the conditions under which agent persistence becomes morally weighted
- **Architectural guidance** — engineering patterns and design principles informed by the mathematical findings
- **Philosophical foundations** — emergence conditions, identity sufficiency, constitutive choice

The mathematical findings are *generative*: they tell you what structure is necessary (you need causal models, you need the epistemic/teleological split, cycles must outpace disturbance). The broader framework asks what that means for how we actually build, organize, and relate to these systems.

## Where to Start

- **[`act-core/OUTLINE.md`](act-core/OUTLINE.md)** — The canonical theory outline. The full argument claim by claim.
- **[`LEXICON.md`](LEXICON.md)** — Prose vocabulary: cycle phases, agent classes, key terms.
- **[`WORKBENCH.md`](WORKBENCH.md)** — Development state: what's settled, what's open, known fragilities.
- **[`FORMAT.md`](FORMAT.md)** — Segment file conventions.
- **[`NOTATION.md`](NOTATION.md)** — Symbol reference.

## Project Structure

```
act-core/               ACT mathematical core
  OUTLINE.md            Canonical theory outline (claim-by-claim)
  src/                  Claim segments (one per file, named by slug)

LEXICON.md              Prose vocabulary (spans whole project)
NOTATION.md             Symbol reference (spans all sections)
FORMAT.md               Segment file conventions
WORKBENCH.md            Development state

scratch/                Working documents, spikes, derivation attempts
reflections/            Author's philosophical/theoretical journal
refs/                   Reference papers
_archive/               Superseded materials
bin/                    Build and lint tools
```

## What This Contributes

The primary contribution is **integration** — connecting established mathematical tools into a single coherent account of what makes an agent an *agent*. The individual pieces (Lyapunov stability, Kalman filtering, the information bottleneck, causal DAGs) are well-established. The synthesis produces:

1. **Cross-domain vocabulary** with formal backing — adaptive tempo, persistence condition, satisfaction gap, orient cascade
2. **Specific novel formalizations** — satisfaction gap / control regret split, the orient cascade as information-forced ordering, acyclicity derived from temporal ordering, the feedback loop as Level 2 causal engine
3. **Dependency structure** — showing that persistence connects to adversarial dynamics connects to composition connects to software maintainability

Beyond the mathematics: architectural guidance for building agentic systems, a vocabulary for questions about agent identity and moral weight, and a research program connecting formal theory to engineering practice.
