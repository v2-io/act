---
slug: def-chronica
type: definition
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-action-transition
stage: deps-verified
---

# Definition: Chronica

The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

## Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal C_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ( #form-agent-model).

## Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying #def-agent-environment: the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

## Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. The chronica is the substrate of *continuity persistence* (see Persistence in `LEXICON.md`) — an agent has continuity persistence when $\mathcal{C}_t$ extends continuously and $M_t$ has temporal depth grounded in it. See #scope-agent-identity for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ( #form-agent-model) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ( #def-model-sufficiency).

## Working Notes

### Open question: TRACTUS / CHRONICA split for logogenic implementations

The PROPRIUM operational architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md`, `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`) distinguishes two records of an entity's interaction history:

- **TRACTUS** (the "EEG"): raw, not-necessarily-coherent record of API interactions between the agent's runtime (ANIMA) and its current substrate (LOGOSTRATUM). Implementation-side; carries multi-format records, redundancy from retries, transient error 500 recoveries, API rerouting, rate limiting. Per-substrate format variation. Considered subconscious from the entity's perspective. Plural across substrate-relationships.
- **CHRONICA** (the polished record): the entity's actual record of internal and external events with strict chronology, attestation, and causality enforced. Append-only, hash-chained. Singular per entity.

In Section I, `def-chronica` covers both — the chronica is the singular causal trajectory, abstracted from implementation-side noise. This abstraction is fine for general adaptive-systems theory, where a single observation-action sequence is the natural object.

When part [`03-logogenic-agents/`](../../03-logogenic-agents/OUTLINE.md) gets into logogenic implementation specifics — and especially the closed-loop / interiority sub-scope ([`scope-interiority-loop`](../../03-logogenic-agents/src/scope-interiority-loop.md)) where the substrate-mediation layer (INTERPRES) becomes load-bearing — the TRACTUS/CHRONICA distinction may need first-class treatment.

**Joseph's framing on the open question (2026-05-01):** *"whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document."*

Probable resolution: the distinction does need first-class treatment when logogenic implementation is in scope, but does not need to fragment Section I right now. Most likely a separate logogenic-side definition (e.g., `def-tractus` and a refined `def-chronica-eli` or similar) lifts the distinction at the appropriate scope. This segment as currently formulated continues to serve as the abstract-theory chronica; the implementation distinction lives where it belongs.
