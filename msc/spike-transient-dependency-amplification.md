# Spike: Transient Dependency Amplification and the Logogenic Lipschitz Constant

**Status.** Exploratory research spike; candidate bridge between TST (Temporal Software Theory) and logogenic diagnostics.
**Date.** 2026-04-25.
**Pressure Point.** In `#result-coupled-diagnostic-framework` (Logogenic Agents), the diagnostic error of a Class 2 LLM agent is bounded by $2 L_A \lVert\Delta M_{\text{bias}}\rVert$. The parameter $L_A$ is the Lipschitz constant of the attainability function $A_O(M_t)$, which measures how wildly the set of achievable outcomes swings when the agent's internal representation $M_t$ is slightly hallucinated or biased. The core framework explicitly leaves its characterization domain-dependent. 

This spike attempts to derive exactly what controls $L_A$ for software engineering tasks, connecting it to the non-normal transient growth of the codebase's dependency operator, and proving the mathematical necessity of intermediate tools (tests/compilers) to collapse error propagation.

## 1. The Effective Dependency Operator

When an agent plans a strategy $\Sigma_t$ for a specific feature $F$, it does not interact with the entire codebase simultaneously. It interacts with the *effective dependency subgraph* relevant to the task.

Let $J_F$ be the effective dependency/propagation operator for feature $F$. This operator encodes the functional, semantic, and structural coupling between the components, assumptions, interfaces, and reasoning steps that are load-bearing for the feature.

Mathematically, a small epistemic hallucination or representation error at step $k$ ($\Delta M_k$) perturbs the agent's estimate of the next step. By the chain rule, this error propagates forward through the dependencies:
$$ \Delta M_{k+1} = J_{F, k} \Delta M_k $$

Over a plan of sequential depth $d$, the total propagated error is bounded by the transient gain of the operator sequence:
$$ \lVert \Delta M_d \rVert \le \lVert J_{F, d} \dots J_{F, 1} \rVert \cdot \lVert \Delta M_0 \rVert $$

For a stationary effective operator $J_F$, this becomes $\lVert J_F^d \rVert$. 

The worst-case sensitivity of the final attainability value $\Delta A_O$ is therefore tightly bounded by this transient gain:
$$ \sup_{\lVert\Delta M\rVert=1} \lVert \Delta A_O \rVert \le C_A \lVert J_F^d \rVert $$
This identifies $L_A \propto \lVert J_F^d \rVert$.

## 2. Non-Normal Transient Growth

Because the strategy propagation is directional (a DAG), the operator $J_F$ is strictly upper-triangular under a topological sort. Therefore, $J_F$ is nilpotent ($J_F^D = 0$ where $D$ is the maximum path length), and all of its asymptotic eigenvalues are exactly zero: $\lambda_i(J_F) = 0$.

However, $J_F$ is highly **non-normal** ($J_F^T J_F \neq J_F J_F^T$). For non-normal operators, eigenvalues do not govern short-term behavior. Even though the asymptotic growth is zero, the operator norm $\lVert J_F^d \rVert$ (its largest singular value) can experience massive *transient* growth before nilpotence eventually terminates propagation.

**Risk statement:** If the feature's effective dependency subgraph $J_F$ has high fan-out/fan-in, strong non-normality, or repeated dependency composition, then $\lVert J_F^d \rVert$ may grow rapidly over relevant depths. 

This means that for deep, entangled reasoning tasks, the agent's sensitivity $L_A$ explodes. A single hallucinated premise ($\Delta M_0$) can catastrophically corrupt the entire downstream plan.

## 3. The Engineering Remedy: Projection Operators ($P_k$)

If $L_A$ grows too large, the error bound $2 L_A \lVert\Delta M_{\text{bias}}\rVert$ makes autonomous survival impossible. The agent must restructure the propagation.

In software engineering, compilers, type checkers, test runners, and intermediate execution outputs are not magical oracles. Mathematically, they act as **error-resetting / projection / contraction operators ($P_k$)** inserted into the reasoning chain.

When an agent executes an intermediate step and observes a compiler error or test result, it collapses its uncertainty about the state. The error propagation becomes:
$$ \Delta M_{k+1} = P_k J_{F, k} \Delta M_k $$

The relevant gain for the entire task is no longer the uncontrolled transient growth $\lVert J_F^d \rVert$. Instead, it becomes the interleaved product:
$$ L_A \propto \lVert P_d J_{F, d} \dots P_1 J_{F, 1} \rVert $$

If the tools $P_k$ provide high-fidelity causal feedback (Regime A, `#scope-edge-update-causal-validity`), they act as strong contractions ($\lVert P_k \rVert \ll 1$). By interleaving a strong contraction after every expansion step, the agent prevents the non-normal transient growth from compounding, bounding $L_A$ to a safe, constant magnitude regardless of the total task depth $d$.

## 4. Conclusion and Theoretical Impact

This derivation provides the exact mathematical bridge between TST (Temporal Software Theory) and Logogenic Agents:

1. **Refining the Cognitive Load Hypothesis:** It grounds `#hyp-exponential-cognitive-load`. Increasing the size of the effective coupled subgraph without improving localization, instrumentation, or decomposition *can* increase the worst-case sensitivity exponentially via non-normal transient amplification. "More context" is not automatically bad; "more *entangled* context" is what drives the explosion.
2. **The Physics of Tool Use:** It mathematically derives why deep software tasks fail for LLMs: not merely because "LLMs hallucinate," but because small representation errors are amplified by the dependency structure of the task *unless* the agent actively inserts observation/correction checkpoints ($P_k$) to contract the error envelope.

## 5. Recommended Moves

- Promote this core concept to a working note in `03-logogenic-agents/src/result-coupled-diagnostic-framework.md` to explain what controls $L_A$.
- Retain this spike as a candidate for a future derived segment in TST (`02-tst-core/src/der-transient-dependency-amplification.md`) that officially refines `#hyp-exponential-cognitive-load`.

*(End of spike.)*