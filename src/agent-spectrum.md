---
slug: agent-spectrum
type: definition
status: first-principled
depends:
  - agent-environment
  - agent-model
---

# The Agent Spectrum

Two independent dimensions — whether the agent maintains a reality model and whether it pursues an objective — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

## Formal Expression

*[Definition (agent-spectrum)]*

Two binary dimensions define four quadrants:

| | No objective ($O_t$ absent) | Has objective ($O_t$ present) |
|---|---|---|
| **No model ($M_t$ absent)** | *Reactive system*: fixed feedback rule (thermostat, reflex arc) | *Blind pursuer*: pursues goal without modeling reality (PID controller, gradient follower) |
| **Has model ($M_t$ present)** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, passive Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The quadrants differ in which state objects the agent maintains:
- Reactive: neither $M_t$ nor $O_t$
- Adaptive tracker: $M_t$ only — Section I's machinery fully describes these agents
- Blind pursuer: $O_t$ only — has a target but no model of how to reach it
- Actuated agent: $(M_t, O_t)$ and possibly $\Sigma_t$ — the full scope of ACT

## Epistemic Status

This is *definitional* — it names regions of a continuum for analytical convenience. The quadrants are not ontological categories; agents migrate between them. A PID controller with auto-tuning is moving from blind pursuer toward actuated agent. An RL agent in pure exploration is temporarily an adaptive tracker.

## Discussion

**The continuum.** The boundaries are analytical distinctions. The "has model / no model" axis is really a spectrum of model richness (from no retained state, through error-integral-derivative, through full world models). The "has objective / no objective" axis is similarly graded (from no preference, through implicit optimization criteria, through explicit multi-objective strategies).

**Section I covers the left column.** Adaptive trackers are the primary subject of Section I — agents that build and maintain $M_t$ without explicit purpose. The mismatch signal ( #mismatch-signal), gain ( #update-gain), tempo ( #adaptive-tempo), and persistence condition ( #persistence-condition) fully characterize their adaptive dynamics. TFT was developed primarily for this quadrant.

**Section II adds the right column.** Actuated agents need everything from Section I plus objectives, strategy, and the orient cascade that connects them. The directed separation ( #directed-separation) ensures that Section I's results carry over unchanged — the adaptive machinery operates on $M_t$ independently of whether the agent has purpose.

**"Actuated" terminology.** The top-right quadrant is labeled "actuated agent" rather than "purposeful agent" to maintain a mechanical, formal register. "Purposeful" and "goal-oriented" are fine in natural language; "actuated" is the formal term. "Self-actuated" is reserved for agents that set their own objectives, as distinct from agents with externally supplied objectives.
