# TST: Temporal Software Theory

Software development as an agentic domain — grounded in ACT's formal machinery, restored to its original status as a consequential body of research in its own right.

**Working draft.** TST re-grounds the original Temporal Software Theory in ACT's mathematical framework — adding causal mathematics, adaptive dynamics, and the persistence condition that explain *why* time-optimal development practices work, not just *that* they do. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.

See [`../FORMAT.md`](../FORMAT.md) for segment file conventions. See [`../NOTATION.md`](../NOTATION.md) for symbols.

**Relationship to ACT:** TST segments reference ACT concepts by slug (e.g., `#temporal-optimality`, `#persistence-condition`). The temporal optimality postulate now has full backing: tempo advantage, persistence conditions, and gain dynamics explain WHY time-optimal development practices work. The dependency is one-directional: TST depends on ACT, not the reverse.


---

## Software as Agentic Domain

*Domain instantiation: software development viewed through ACT. The developer (or AI agent) is an actuated adaptive agent whose environment is a codebase, whose observations are mediated by tools (compiler, tests, IDE), and whose actions are code changes. Software's unique epistemic properties — full observability in principle, genuine interventions via tests, counterfactual replay via version control — make it the richest operationalization domain for ACT.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| S | Scope | | [#software-scope](src/software-scope.md) | Systems with $P(\text{change}) \gt \varepsilon$ | draft |
| S | Observation | | [#software-epistemic-properties](src/software-epistemic-properties.md) | Software's 6 unique properties | missing |
| S | Definition | | [#feature-definition](src/feature-definition.md) | Unit of coherent change | draft |
| S | Result | | [#specification-bound](src/specification-bound.md) | Can't implement unspecified; includes communication bottleneck corollary | draft |
| S | Derived | | [#change-expectation-baseline](src/change-expectation-baseline.md) | Median future ≈ observed past; includes investment scale form | draft |
| S | Definition | | [#developer-as-act-agent](src/developer-as-act-agent.md) | Developer as $(M_t, O_t, \Sigma_t)$ | missing |
| S | Definition | | [#comprehension-time](src/comprehension-time.md) | Cost of constructing local $M_t$ | draft |
| S | Definition | | [#implementation-time](src/implementation-time.md) | Cost from first change to done | draft |
| S | Derived | | [#dual-optimization](src/dual-optimization.md) | Min comprehension + impl time | draft |
| S | Derived | | [#change-investment](src/change-investment.md) | When extra time now pays off | draft |
| S | Discussion + Hypothesis | | [#code-quality-as-observation-infrastructure](src/code-quality-as-observation-infrastructure.md) | Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$ | missing |
| | --GAP-- | | | Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$ | |
| S | Hypothesis | | [#conceptual-alignment](src/conceptual-alignment.md) | Code-domain alignment; includes realignment corollary | draft |
| S | Definition | | [#atomic-changeset](src/atomic-changeset.md) | The diff that is the feature | draft |
| S | Empirical | | [#changeset-size-principle](src/changeset-size-principle.md) | Time ∝ changeset size; includes comprehension corollary | draft |
| S | Definition | | [#change-distance](src/change-distance.md) | Lexical < file < module < svc | draft |
| S | Derived + Hypothesis | | [#change-proximity-principle](src/change-proximity-principle.md) | Closer changes → less time | draft |
| S | Hypothesis | | [#exponential-cognitive-load](src/exponential-cognitive-load.md) | Context-switch cost compounds? | draft |
| S | Definition | | [#system-coupling](src/system-coupling.md) | $P(\text{change } j \mid \text{change } i)$ | draft |
| S | Definition | | [#system-coherence](src/system-coherence.md) | $E[\text{proximity within module}]$ | draft |
| S | Measurement | | [#coherence-coupling-measurement](src/coherence-coupling-measurement.md) | Coherence/coupling from git | draft |
| S | Derived | | [#principled-decision-integration](src/principled-decision-integration.md) | Optimal $C$ minimizes $E[T \vert C]$ | draft |
| S | Definition | | [#system-availability](src/system-availability.md) | $\text{MTTF}/(\text{MTTF}+\text{MTTR})$ | draft |
| S | Scope | | [#continuous-operation](src/continuous-operation.md) | Include $P(\text{fail}) \times T_{\text{recovery}}$ | draft |
| S | Hypothesis | | [#causal-discovery-from-git](src/causal-discovery-from-git.md) | Git as interventional data | missing |
| | --GAP-- | | | Software persistence: the unmaintainability threshold formalized | |
