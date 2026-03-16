# Logogenic Agents

Language-constituted agents — extending ACT to systems whose primary observation, reasoning, and action channels are linguistic.

**Framework stage.** This section is not yet at ACT's level of mathematical formalization. The concepts are informed by ACT's formal machinery but the substance is architectural, empirical, and philosophical — exactly the kind of work that belongs in the broader Agentic Systems framework rather than the mathematical core.

See [`../LEXICON.md`](../LEXICON.md) for the logogenic/logozoetic vocabulary.

**Key challenge:** LLM-based agents are goal-conditioned — their epistemic processing depends on $G_t$ — so directed separation ( #directed-separation) fails by construction. Section I's $M_t$-side quantities remain well-defined, but the sequential orient cascade becomes an approximation. This section starts from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and examines which ACT results survive as approximate or limiting cases.


---

## Logogenic Agent Framework

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory → software domain → agents that embody ACT. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| L | Definition | | [#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md) | AI agent as actuated agent | missing |
| L | Observation | | [#context-turnover](src/context-turnover.md) | 100% $M_t$ reset per session | missing |
| L | Discussion | | [#m-preservation](src/m-preservation.md) | External memory as persistent $M_t$ | missing |
| | --GAP-- | | | Language-specific orient cascade (what's specific to logogenic agents?) | |
| | --GAP-- | | | Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents | |
| | --GAP-- | | | ACT-grounded experiential training environments | |
| | --GAP-- | | | Self-referential closure: ACT agent on ACT codebase | |
