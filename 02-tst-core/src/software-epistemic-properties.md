---
slug: software-epistemic-properties
type: observation
status: discussion-grade
depends:
  - software-scope
  - pearl-causal-hierarchy
  - observation-function
  - adaptive-tempo
stage: draft
---

# Observation: Software's Epistemic Properties

Software development possesses six epistemic properties that collectively make it the richest operationalization domain for AAD — not merely another instantiation, but a domain where AAD's formal machinery can be tested with unusually high fidelity.

## Formal Expression

*[Observation (software-epistemic-properties)]*

Six properties distinguish software development from other adaptive domains. Each is stated with its AAD-theoretic consequence.

**P1. Environment inspectability.** The codebase state $\Omega_t$ is fully observable in principle. The partial observability in software arises from the *agent's* limited attention and comprehension bandwidth, not from the environment hiding state. Formally: the observation function $h$ is lossy because of cognitive limits on the agent side, not because $\Omega_t$ is physically inaccessible.

$$U_o^{\text{(code)}} = f(\text{agent bandwidth}) \quad \text{not} \quad f(\text{environment opacity})$$

*Consequence:* The observation uncertainty $U_o$ for code-reading channels is under the agent's (and previous agents') partial control — unlike most domains where $U_o$ is set by physics. This enables P6 below.

**P2. Executable counterfactuals (scoped Level 3 access).** Version control provides literal Pearl Level 3 counterfactual execution ( #pearl-causal-hierarchy) for a specific and well-defined class of questions: **code-internal counterfactuals with deterministic outcomes.** For questions of the form "what would the test suite report if implementation X had been chosen instead of Y, holding the test suite and environment fixed?", `git checkout` plus re-implementation plus test execution is not a proxy — it is literal counterfactual realization with ground-truth verification. The domain is the codebase itself; the intervention is on code; the outcome is on code behavior; the verification is the test suite.

This literal Level 3 access fails for a complementary class: **counterfactuals crossing the agent-environment boundary** — questions about what feature sequence the team would have produced, how the market would have responded, or how a different developer would have proceeded. These are path-dependent on external events that cannot be replayed. For this second class, `git checkout` is a strong executable proxy, not literal Level 3.

The distinction is sharp because it separates identifiable regimes: code-internal tests are deterministic functions of code (Level 3 literal); agent-coupled questions require the past trajectory of external events (Level 3 proxy at best). No other AAD domain offers literal Level 3 on *any* non-trivial class of questions.

*Consequence:* Model class fitness $\mathcal{F}(\mathcal{M})$ ( #model-class-fitness) becomes empirically measurable *for the code-internal regime*: fork at a past decision point, try an alternative architecture, run the same test suite and benchmarks, and measure whether it achieves higher sufficiency on those deterministic targets. For the agent-coupled regime, measurement requires the proxy interpretation with its path-dependence caveats (see discussion below).

**P3. Genuine interventions (Level 2 access).** Developers perform real interventions: running tests, deploying to staging, making speculative changes. Each is a $do(\cdot)$ operation ( #pearl-causal-hierarchy) whose outcome is observed through well-characterized channels. Software provides a spectrum of Level 2 channels with known $(\nu, U_o)$ profiles:

| Channel | $\nu$ | $U_o$ | Coverage |
|---------|--------|--------|----------|
| Type checker | Instant | Near-zero | Syntactic/type |
| Linter | Instant | Very low | Style + common errors |
| Unit tests | Seconds–minutes | Low | Tested paths |
| Integration tests | Minutes | Low–medium | Cross-module |
| Staging deploy | Minutes–hours | Medium | Near-production |
| Production canary | Hours | Low (real traffic) | Full |

*Consequence:* Causal information yield ( #causal-information-yield) is concretely estimable per channel, enabling principled sequencing: fast narrow channels first, slower broader channels when needed.

**P4. Partially explicit causal structure.** Import graphs, dependency declarations, API contracts, and type systems declare causal structure explicitly. Change propagation follows these paths. This is richer causal identification than most domains offer.

*Consequence:* The causal DAG required for strategy representation ( #strategy-dag) is partially given by the environment, not entirely inferred by the agent.

**P5. Exact exteriorized chronica.** Git provides a complete, immutable record of every exteriorized change: what changed, when, and by whom. For the *exteriorized* content of the chronica $\mathcal{C}_t$ ( #chronica) — the sequence of codebase state transitions, their timing, and their authorship — git records this without information loss. State transitions are preserved exactly; the diff between commits $i$ and $i+1$ is the exact intervention that occurred.

The chronica is, by definition, the record of interactions between agent and environment — not the agent's internal reasoning about those interactions. Git's scope matches the chronica's definition precisely for the codebase domain: the codebase is the environment, commits are the interventions, diffs are the state transitions, and all of these are recorded exactly.

What git does not record is orthogonal to the chronica: the agent's internal model state $M_t$ (which beliefs drove the intervention), the strategy DAG $\Sigma_t$ (which causal hypotheses led to this choice), or the objective $O_t$ (which target the agent was pursuing). These are agent-internal and not part of the chronica by any domain's definition. Commit messages and PR descriptions are partial exteriorizations of $M_t$/$G_t$ intent, but only to the extent the agent chose to verbalize them.

*Consequence:* Empirical estimation of environment-side AAD quantities ($\rho$, coupling, change frequency, state-transition patterns) is possible from the historical record, without the sampling and recall biases that afflict other domains. Estimation of agent-internal quantities ($M_t$ content, $\Sigma_t$ structure, $O_t$ definition) requires separate instrumentation — commit messages, PR descriptions, design documents, or for AI agents, explicit reasoning traces.

**P6. Agent-controlled observation quality.** Code quality IS observation channel quality. Well-written code with clear naming has low $U_o$ for the code-reading channel; obfuscated code has high $U_o$. Agents can improve their own future observation channels by writing better code — a feedback loop within the feedback loop.

*Consequence:* The agent's environment-modifying actions at time $t$ affect the observation function $h$ at time $t+k$, creating a second-order dynamic where current code quality investments compound into future adaptive capacity via $U_o \to \eta^\ast \to \mathcal{T}$. See #code-quality-as-observation-infrastructure.

## Epistemic Status

These six properties are *observations* — empirical features of the software development domain, not derived from AAD. Their AAD-theoretic consequences are *discussion-grade*: structurally motivated mappings from domain features to formal quantities, not derivations. The individual properties are independently verifiable (P1: can you read all the source? P2: can you `git checkout`? P3: can you run tests? etc.) and uncontroversial as descriptions of the domain.

The claim that these properties *collectively* make software the richest AAD testbed is comparative and harder to verify — it requires showing that no other accessible domain offers all six simultaneously. This is plausible (biological systems lack P1, P2, P5; military systems lack P1, P5; financial systems lack P4, P6) but the comparison has not been systematic.

Max attainable: *discussion-grade*. These are domain observations with theoretical interpretation, not derivable claims.

## Discussion

**The inspectability distinction (P1) is load-bearing.** Most AAD domains are POMDPs because the environment hides state. Software is a POMDP because the *agent* cannot attend to all state simultaneously. This means observation quality improvements are possible by restructuring the environment (the codebase) rather than by building better sensors. The observation function $h$ is partially a design choice, not a physical constraint. This fundamentally changes the adaptive dynamics: the agent can invest in improving $h$ itself, not just in improving $M_t$ given a fixed $h$.

**P2 regime boundary.** The literal Level 3 scope is narrower than the full replay problem. Literal counterfactual realization requires: (a) the intervention is expressible as a code state change, (b) the outcome is a deterministic function of code state (test result, type-check, benchmark on fixed inputs), and (c) the environment between code and outcome is reproducible (fixed test suite, fixed dependencies, pinned inputs). When all three hold, `git checkout` + reimplementation + test execution gives literal Level 3 with ground-truth verification; when any fails, the same procedure provides an executable proxy.

Path-dependence breaks (c): if we want to know how the *feature sequence* would have evolved under an alternative architecture, the counterfactual feature requests depend on how users and the team responded to the architecture historically — none of which is replayable. Re-implementation cost breaks nothing formally but introduces *effective* limits: replaying 1000 features under alternative architectures is expensive enough that partial replay (10-50 representative features) is the operational practice. Even partial replay on the code-internal regime provides far more information than model-based speculation — and it is still literal Level 3 for each replayed instance, not a proxy.

**P5 and the instrumentation boundary.** The exact-chronica status of git applies to environment-side content (state transitions, timing, authorship) — matching exactly what the chronica is defined to contain. Agent-internal content (why a particular intervention was chosen; which beliefs or strategies drove it) is not part of the chronica in any domain and therefore not in git's scope. Commit messages and PR descriptions are partial exteriorizations of agent intent; their quality varies enormously by authorial discipline. This is relevant for #causal-discovery-from-git: the interventional record is complete (because it is environment-side), but the confounder record is partial wherever confounders depend on agent-internal state (e.g., developer knowledge state, which is agent-internal and not part of the chronica).

**Multi-agent amplification.** P5 (perfect history) combined with P6 (agent-controlled observation quality) creates a distinctive multi-agent dynamic: agents can externalize parts of $M_t$ into the environment (documentation, clear naming, architecture decisions) where future agents can observe it. This converts ephemeral model state into persistent environmental state — the agent writes its model into $\Omega$ so that future agents can reconstruct $M_t$ through observation. The quality of this externalization determines how much of the previous agent's model survives turnover, and directly affects #comprehension-time for subsequent agents.

## Working Notes

- P1 says the environment is inspectable *in principle*, but for large codebases the cost of full inspection may exceed the agent's available time. There may be a useful formalization of "effective observability" that accounts for the agent's time budget — something like $U_o^{\text{eff}} = U_o^{\text{intrinsic}} + f(\lvert\Omega\rvert / \text{budget})$. This connects to #information-bottleneck: the agent must compress because full observation is too expensive, even though it is in principle available.
- The "feedback loop within the feedback loop" (P6) is the most theoretically interesting property. It creates a self-referential dynamic where the adaptive cycle's own outputs modify its future inputs. AAD's current formulation allows action-dependent observation ($o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$), but the cumulative effect of many past actions on $h$ is a longer-timescale phenomenon. Whether this requires extending AAD or is already captured by the existing formalism (with $h$ treated as slowly varying) is an open question.
- The table in P3 invites a formal treatment: given the $(\nu, U_o)$ profile per channel and the agent's current $U_M$, what is the CIY-optimal sequencing of probes? This would be a concrete worked example for #causal-information-yield applied to software.

*(Source: old-tst-via-tft-readme.md, "What Software Development Uniquely Offers.")*
