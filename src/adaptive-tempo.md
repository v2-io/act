---
slug: adaptive-tempo
type: definition
depends:
  - update-gain
  - event-driven-dynamics
---

# Adaptive Tempo

The effective rate at which an agent acquires useful information from its environment — the product of observation frequency and update quality across all channels.

## Formal Expression

*[Definition (adaptive-tempo)]*

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where:
- $k$ indexes the agent's distinct observation channels
- $\nu^{(k)}$ is the event rate on channel $k$
- $\eta^{(k)*}$ is the optimal update gain on channel $k$ (#update-gain)

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^*$.

## Epistemic Status

This is a *definition*. It names the quantity that characterizes an agent's total corrective capacity, combining loop speed ($\nu$) and epistemic quality ($\eta^*$). The definition itself is not a truth-claim; the substantive claims are in the results that use it (#persistence-condition, #adversarial-tempo-advantage).

## Discussion

**Speed-quality substitutability.** An agent can achieve the same tempo via a fast noisy loop (high $\nu$, low $\eta^*$) or a slower calibrated one (low $\nu$, high $\eta^*$). The product structure means improvements to *both* factors compound multiplicatively.

**Observation noise gating.** Because $\eta^* = U_M / (U_M + U_o)$, high observation noise ($U_o$) depresses gain and collapses tempo regardless of loop speed. You cannot outrun a bad observation channel by iterating faster. This grounds Boyd's emphasis on Orient quality over raw OODA speed.

**Centrality.** Tempo is ACT's core capacity metric. It appears on the left side of the persistence condition (#persistence-condition), determines adversarial advantage (#adversarial-tempo-advantage), and connects to code quality as observation infrastructure (#code-quality-as-observation-infrastructure) in the software domain.