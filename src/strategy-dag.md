---
slug: strategy-dag
type: definition
status: conditional
depends:
  - and-or-scope
  - causal-structure
  - pearl-causal-hierarchy
---

# Strategy DAG

The strategy $\Sigma_t$ is a directed acyclic graph with probabilistic edges and AND/OR combination semantics. Each edge carries the agent's causal credence that completing the parent step advances the child step. The graph encodes the agent's theory of how its actions produce progress toward its objectives.

## Formal Expression

*[Definition (strategy-dag)]*

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t)$$

where:
- $V_t$: set of propositional nodes (conditions that could be true or false)
- $E_t \subseteq V_t \times V_t$: directed causal edges
- $p_t : E_t \to [0,1]$: **causal credence** per edge — the agent's confidence that completing the parent advances the child
- $\gamma_t : V_t \to \{\text{AND}, \text{OR}\}$: combination rule per node ( #and-or-scope)

**Structural constraints:**

1. **Acyclicity.** $\Sigma_t$ is a DAG. This is *derived*, not assumed — see below.
2. **Rootedness.** Every node has a directed path to at least one terminal (objective) node.
3. **Source constraint.** Leaf nodes are actions the agent can take or conditions the agent can observe.

**Edge semantics.** Each edge carries a single causal credence weight:

$$p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed},\, M_t)$$

This is the agent's credence that completing step $i$ causally advances step $j$, given its current model. In **intervention-rich domains** (software, laboratory science — where the agent performs genuine experiments), this credence approximates the interventional probability $P(j \mid do(i), M_t)$. In **confounded domains** (military, organizational — where evidence is delayed, correlated, or strategically distorted), the credence is weaker: it encodes the agent's best causal belief, but that belief may be biased by observational confounding. The strength of the causal interpretation depends on the domain's identifiability conditions ( #causal-information-yield, admissibility regimes).

**Status propagation.** Forward pass in topological order, $O(\lvert V \rvert + \lvert E \rvert)$:

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf (base credence)} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR} \end{cases}$$

**Single-parameter edges.** Each edge carries one number ($p_{ij}$), not two. An earlier formalism attempt used $(p_{ij}, \theta_{ij})$ where $\theta$ was "contribution magnitude." This was dropped because the AND/OR combination rules at nodes absorb $\theta$'s role — the complexity budget goes to one bit per node ($\gamma$) instead of one float per edge.

### Acyclicity is Derived

*[Derived (from causal-structure + finite planning horizon)]*

Each node in $\Sigma_t$ represents a future event or state with temporal position $\tau_i > t$. An edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ ( #causal-structure: causes precede effects). A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

Strategies involving iteration ("try A, if fail try B, if fail try A again") are acyclic when time-indexed: $A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$ Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view.

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory.

**Scope of the acyclicity result.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment, which may include cyclic causal processes (feedback loops in the physical world, market dynamics, ecosystem interactions). The acyclicity is specific to the purposeful substate.

## Epistemic Status

*Conditional* on the #and-or-scope restriction. The DAG structure itself is more strongly motivated — it follows from temporal ordering (acyclicity), probabilistic uncertainty (Cox's theorem forces probability on edges), and a plausible argument that state-local revisability forces the Markov factorization (`scratch/spike-graph-uniqueness.md`). The full argument from operational axioms to DAG structure is a proof sketch, not yet a theorem — the step from local revisability to the Markov condition needs tightening (see #graph-structure-uniqueness in appendices). The acyclicity derivation above IS tight.

The AND/OR parameterization is a parsimony-motivated formulation choice within the forced graphical structure, not a derived necessity ( #and-or-scope). The single-parameter edge convention is similarly a formulation choice motivated by convergence across three independent attempts.

## Discussion

**The graph structure is forced; the parameterization is chosen.** This is analogous to: probability is forced by Cox's axioms, but the specific probability distribution for a given problem is a modeling choice. ACT uses DAG + AND/OR because (a) AND/OR is the most parsimonious complete basis for binary combination, (b) the DAG naturally supports causal reasoning, and (c) the representation converged across three independent formalism attempts. Alternative parameterizations within the graphical structure are legitimate research directions.

**Combination assignment is principled but fallible.** The question "if I remove one parent, can $v$ still be achieved?" is derivable from $M_t$'s causal model — it's a principled assignment, not arbitrary. But the assignment can be wrong (false AND = pessimistic over-investment; false OR = optimistic under-investment), and should be updateable when evidence reveals a different structural relationship.

**Connection to Pearl's framework.** The strategy DAG is a causal Bayesian network where the agent is both the modeler and the intervener. Pearl's do-calculus applies in intervention-rich domains where the agent can experimentally verify edge credences. In confounded domains, the DAG degrades to a "best causal belief" structure — useful for planning but with acknowledged potential for systematic bias.

## Working Notes

- Edge failures are assumed independent in the combination rules. Real systems have correlated failures (shared infrastructure, common-mode risks). The actual confidence is lower than the independent-edge formula suggests. Modeling correlation structure would require augmenting the DAG with hidden common-cause nodes or using a richer parameterization — both increase complexity. Currently acknowledged as a limitation.
- The graph-uniqueness argument (P1-P4 → DAG with Markov property) is the strongest structural justification: temporal ordering + Cox's theorem + local revisability + observable intermediates → directed graphical model with the Markov factorization. If the P3→Markov step can be tightened to a full proof, strategy-dag could be promoted from Definition to Derived. See `scratch/spike-graph-uniqueness.md`.
- Health metrics (groundedness, observability coverage, weighted redundancy, bottleneck scores) are scaffold — engineering quantities for monitoring DAG health, not principled derivations. They may be useful for implementation but should not enter the theory's formal chain.
- **The O_t ↔ terminal-node interface is under-specified.** The rootedness constraint says every node has a directed path to a terminal (objective) node, and #structural-change-as-parametric-limit lists "objective revision" as changing terminal nodes. But #strategy-dimension defines $O_t$ and $\Sigma_t$ as distinct objects. If terminals encode $O_t$, then $\Sigma_t$ contains $O_t$, blurring the split. The intended interpretation: terminal nodes are *defined by* $O_t$ (they represent evaluation criteria derived from $O_t$), but $O_t$ lives outside $\Sigma_t$. When $O_t$ changes, terminal conditions change, which can trigger structural changes in $\Sigma_t$. An explicit terminal-condition map $\phi: O_t \to \mathcal{P}(V_t^{\text{terminal}})$ would formalize this interface. Until then, the split is clean in prose but not in the math.
- **$p_v$ (leaf base credence) is undefined.** The status propagation formula uses $p_v$ for leaf nodes but this is not defined in the formal expression. It should be: the agent's prior credence that the leaf condition is achievable or currently holds. For action nodes, $p_v$ is the agent's confidence it can execute the action; for observable-condition nodes, $p_v$ is the agent's estimate that the condition obtains. This needs to be explicitly added to the definition.
