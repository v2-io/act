---
slug: strategy-cost-regret-bound
type: derivation
status: robust-qualitative
depends:
  - strategy-complexity-cost
  - value-object
  - objective-functional
stage: draft
---

# Derivation: Regret-Bound Derivation of the Strategy-Cost KL Direction

The variational form of the strategy-cost objective ( #strategy-complexity-cost) carries a $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ relevance term. This appendix derives that **the $\pi^\ast$-first KL direction is forced** as the non-vacuous regret-bound form, and characterizes the admissible family of divergences within which reverse-KL is the canonical (but not uniquely forced) member.

## Formal Expression

### §1 — Setup

Fix $O_t$, $M_t$, continuation policy $\pi_{\mathrm{cont}}$, and horizon $N_h$. The action-value is the objective-functional evaluation at $a$: $V(a) := Q_O(M_t, a; \pi_{\mathrm{cont}}, N_h)$ ( #value-object; $V$ derives from $O_t$ per #objective-functional). The optimal action is $a^\ast := \arg\max_a V(a)$; under AAD's canonical scope ( #value-object), the optimal policy $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast}$ is the point mass on $a^\ast$ (tied-optimum extensions §8). Write $V_{\max} := \max_a V(a) - \min_a V(a)$ for the value range at fixed $M_t$; this is finite whenever $\mathcal{A}$ is a bounded action set under $V$.

$Q_{\Sigma_t}(\cdot \mid M_t)$ is the action distribution induced by the strategy DAG. In general $Q_{\Sigma_t}$ is stochastic — the DAG's edge-credence uncertainty induces policy stochasticity downstream of propagation.

### §2 — Regret against the optimal policy

*[Definition (strategy-induced-regret)]*

The strategy-induced regret of $Q_{\Sigma_t}$ against $\pi^\ast$ is:

$$R(Q_{\Sigma_t}) \;:=\; V(a^\ast) \;-\; \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)] \;=\; \sum_{a} Q_{\Sigma_t}(a) \cdot \bigl[V(a^\ast) - V(a)\bigr]$$

Writing $\Delta(a) := V(a^\ast) - V(a) \in [0, V_{\max}]$ for the per-action regret gap. Three regret forms in the literature:

$$\mathbb{E}_{\pi^\ast}[V] - \mathbb{E}_{Q_{\Sigma_t}}[V], \qquad V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V], \qquad \mathbb{E}_{\pi^\ast}[V - V_{Q_{\Sigma_t}}]$$

coincide identically under deterministic $\pi^\ast$.

### §3 — Total-variation bound (tight)

*[Derived (tv-regret-bound, from bounded $V$ + deterministic $\pi^\ast$)]*

$$R(Q_{\Sigma_t}) \;=\; \sum_a Q_{\Sigma_t}(a)\,\Delta(a) \;\leq\; V_{\max} \cdot \sum_{a \neq a^\ast} Q_{\Sigma_t}(a) \;=\; V_{\max} \cdot (1 - Q_{\Sigma_t}(a^\ast))$$

For deterministic $\pi^\ast = \delta_{a^\ast}$:

$$\operatorname{TV}(\pi^\ast, Q_{\Sigma_t}) \;=\; \tfrac{1}{2}\sum_a \lvert \pi^\ast(a) - Q_{\Sigma_t}(a)\rvert \;=\; 1 - Q_{\Sigma_t}(a^\ast)$$

Therefore:

$$\boxed{\;R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \operatorname{TV}(\pi^\ast, Q_{\Sigma_t})\;} \qquad \text{(tight)}$$

**Tightness.** Equality holds exactly when $\Delta(a) = V_{\max}$ for all $a \neq a^\ast$ (degenerate value landscape: every suboptimal action incurs the full value range). For typical landscapes the bound is loose by a factor $\mathbb{E}_{Q_{\Sigma_t}}[\Delta \mid a \neq a^\ast]/V_{\max} \in (0, 1]$.

### §4 — Pinsker-KL bound (reverse direction)

*[Derived (kl-regret-bound, via Pinsker + tv-regret-bound)]*

Pinsker's inequality (Tsybakov 2009 §2.4; Cover & Thomas 2006 §11.6): $\operatorname{TV}(P, Q) \leq \sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(P \Vert Q)}$. Applied with $P = \pi^\ast$, $Q = Q_{\Sigma_t}$:

$$\boxed{\;R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \sqrt{\tfrac{1}{2}\,D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\;}$$

Under deterministic $\pi^\ast$, $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = \sum_a \pi^\ast(a)\log(\pi^\ast(a)/Q_{\Sigma_t}(a)) = -\log Q_{\Sigma_t}(a^\ast) \in [0, +\infty)$. Finite and graded whenever $Q_{\Sigma_t}(a^\ast) \gt 0$; diverges only in the structural-failure limit where the strategy places zero mass on the optimum.

### §5 — Direction-forcing claim (the load-bearing result)

*[Derived (kl-direction-forced, from deterministic $\pi^\ast$)]*

**Claim.** The KL direction with $\pi^\ast$ *first* is forced as the non-vacuous regret-bound form. Forward-KL $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ is *not* a non-vacuous bound on $R(Q_{\Sigma_t})$ under deterministic $\pi^\ast$.

**Derivation.** Expanding:

$$D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) \;=\; \sum_a Q_{\Sigma_t}(a) \log\!\bigl(Q_{\Sigma_t}(a)/\pi^\ast(a)\bigr)$$

For any $a \neq a^\ast$: $\pi^\ast(a) = 0$ (point mass assumption). The summand $Q_{\Sigma_t}(a)\log(Q_{\Sigma_t}(a)/0) = +\infty$ unless $Q_{\Sigma_t}(a) = 0$. Therefore $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) = +\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$ — for *all but a measure-zero subset* of stochastic strategies. A bound "$R \leq +\infty$" is vacuous.

This is the same shape of degeneracy as the original Shannon-MI form (Gemini Finding 2) that the V-medium move was introduced to escape: same degeneracy-when-$\pi^\ast$-is-deterministic, different value ($0$ vs $+\infty$). Only the *reverse* direction escapes both.

**Alignment with the structural problem.** Forward-KL is natural for *mode-covering* inference (where $Q$ is asked to cover $P$'s full support) and variational inference when $Q$ is learned to match a full distribution. Reverse-KL is natural for *mode-seeking* (concentrate $Q$ on $P$'s mode). The AAD strategy problem is mode-seeking by construction: the strategy should concentrate on $a^\ast$. The direction alignment with the structural problem is not accidental.

### §6 — Admissible-divergence family (Outcome B characterization)

*[Discussion (admissible-regret-divergences)]*

The regret-bound argument forces the *direction* (the reference distribution $\pi^\ast$ appears first) but admits a family of divergences. Each member yields a valid regret bound; they differ in tightness and operational properties:

| Divergence | Bound on $R$ | Tightness | Finite under det. $\pi^\ast$? | Gradient-tractable? |
|---|---|---|---|---|
| $\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$ | $V_{\max}\cdot\operatorname{TV}$ | **Tight** (extremal $V$) | Yes | No (non-differentiable) |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ via Pinsker | $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}}$ | Loose by $\sqrt{\cdot}$ | Yes | Yes |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ via Bretagnolle-Huber | $V_{\max}\sqrt{1 - e^{-D_{\mathrm{KL}}}}$ | Tighter than Pinsker for large $D_{\mathrm{KL}}$ | Yes | Yes |
| $\chi^2(\pi^\ast \Vert Q_{\Sigma_t})$ (Le Cam) | $V_{\max}\cdot\tfrac{1}{2}\sqrt{\chi^2}$ | Typically looser than Pinsker | Yes: $\chi^2 = 1/Q_{\Sigma_t}(a^\ast) - 1$ | Yes |
| $D_\alpha(\pi^\ast \Vert Q_{\Sigma_t})$ (Rényi, $\alpha \geq 1$) | Various | Interpolates KL ($\alpha\to 1$) and $\chi^2$ ($\alpha = 2$) | Yes for $\alpha \geq 1$ | Yes |
| $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ (forward-KL) | $+\infty$ | Vacuous | **No** | — |

**What is uniquely forced.** The direction: the reference $\pi^\ast$ is first. This is a real derivation outcome, not a selection.

**What is a family.** The specific functional form within $\pi^\ast$-first divergences. Reverse-KL via Pinsker is *canonical* (not *unique*) on four grounds — each honestly weaker than a uniqueness theorem:

1. **Gradient-tractability.** TV is non-differentiable at mass boundaries; reverse-KL, $\chi^2$, and Rényi are smooth. Operational minimization via gradient methods rules out TV despite its tightness.
2. **Variational-inference alignment.** Reverse-KL is the standard divergence in the variational-inference lineage (ELBO derivation uses reverse-KL; Friston et al. 2017; Da Costa et al. 2020). The V-medium move's rhetorical payoff — shared vocabulary with active inference — lives on reverse-KL specifically. Bretagnolle-Huber or $\chi^2$ bounds, while also valid, would break the bridge.
3. **Fisher geometry.** Reverse-KL's second-order expansion gives the Fisher information metric (Amari & Nagaoka 2000), the canonical pull-back of policy-manifold geometry. $\chi^2$ gives a different (Euclidean-like) metric.
4. **Information-budget / MDL interpretation.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ is the expected extra bits needed to code samples from $\pi^\ast$ under $Q_{\Sigma_t}$'s code — direct coding interpretation aligned with the segment's MDL framing.

**None of these is a uniqueness argument.** Each says reverse-KL is the canonical instance in the family. A uniqueness theorem would require reverse-KL to be tightest among smooth divergences; the table shows TV is tightest but non-differentiable, and Bretagnolle-Huber sometimes beats Pinsker. The honest claim: reverse-KL is the canonical smooth-divergence member of an admissible family, selected on the four grounds above.

### §7 — $\beta_\Sigma$ interpretation under the regret bound

*[Discussion ($\beta_\Sigma$-local-vs-global)]*

The Pinsker bound gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$. Two scale forms for the segment's trade-off parameter $\beta_\Sigma$ arise:

**(a) Square-root-KL form** (tight regret-bound scale):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot \sqrt{D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}, \qquad \beta_\Sigma = V_{\max}/\sqrt{2}$$

$\beta_\Sigma$ is *globally naturalized* as a constant scale proportional to the value range at fixed $M_t$. Cost: the form departs from the linear-Lagrangian IB shape that #compression-operations uses across the four compression operations.

**(b) Linear-KL form** (IB-shape instance, preserved in the segment):

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$$

Under this form, $\beta_\Sigma$'s regret-bound interpretation is *local*: differentiating the Pinsker bound, $\partial R/\partial D_{\mathrm{KL}} = V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$, so $\beta_\Sigma$ represents the local cost-per-bit at the operating point but varies with $D_{\mathrm{KL}}$. Upside: consistency with the IB linear-Lagrangian shape ( #compression-operations). Downside: no uniform global $\beta_\Sigma$ scale.

**Choice made in #strategy-complexity-cost.** Keep the linear form (IB-shape alignment); note the square-root form in the Epistemic Status as the "source" derivation. The direction-forcing claim is the load-bearing strengthening; the linear-vs-square-root choice is a second-order trade-off that preserves architectural consistency at the cost of a fully naturalized $\beta_\Sigma$.

### §8 — Bound tightness and scope limits

**Vacuity regimes** (where the regret bound fails to be informative):

1. **$V_{\max} = \infty$ (unbounded value).** Then all bounds are $\infty$. AAD's $O_t$ is $\mathbb{R}$-valued ( #objective-functional); boundedness of $V$ over $\mathcal{A}$ at fixed $M_t$ is an additional assumption. Stated here as a scope condition of the derivation.
2. **$Q_{\Sigma_t}(a^\ast) = 0$ (strategy cannot express the optimum).** Then $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = +\infty$. This is structural failure — the strategy's DAG cannot produce the optimal action — and the infinite KL correctly flags it. *Informative degeneracy*, not pathology: operational minimization rejects such $\Sigma_t$.
3. **$\pi^\ast$ not deterministic (outside canonical scope).** For stochastic $\pi^\ast$ with larger support than $Q_{\Sigma_t}$, reverse-KL may still be infinite. §9 addresses tied-optimum extensions; stochastic $\pi^\ast$ under softmax-smoothing is future work.

**Tightness comparison.** TV is the tight bound in the admissible family; Pinsker is loose by $\sqrt{\cdot}$; Bretagnolle-Huber is tighter than Pinsker for large $D_{\mathrm{KL}}$. None of the KL bounds is *tightest* — TV wins — but TV's non-differentiability is an operational strike. Reverse-KL is the tightest bound in the *smooth-divergence* sub-family among standard choices, with Bretagnolle-Huber as a gradient-tractable alternative when bounds in the large-KL regime matter.

### §9 — Extensions

**Tied-optimum case.** If $\pi^\ast$ has support on a tied-optimum set $\mathcal{A}^\ast = \{a : V(a) = V(a^\ast)\}$ with uniform mass, reverse-KL is finite whenever $Q_{\Sigma_t}$ covers $\mathcal{A}^\ast$. The regret-bound argument extends directly: $R(Q_{\Sigma_t}) = \sum_a Q_{\Sigma_t}(a)\Delta(a) \leq V_{\max} \cdot \mathbb{P}_{Q_{\Sigma_t}}(a \notin \mathcal{A}^\ast)$ and Pinsker applies unchanged.

**Softmax-smoothed $\pi^\ast$ (stochastic $\pi^\ast$ for non-degeneracy reasons).** A regret bound of the form

$$\mathbb{E}_{\pi^\ast}[V] - \mathbb{E}_{Q_{\Sigma_t}}[V]$$

with softmax-weighted $\pi^\ast$ also admits the Pinsker-KL step, with reverse-KL again the non-vacuous direction (forward-KL remains vacuous whenever $\pi^\ast$ has wider support than $Q_{\Sigma_t}$, and vice versa). Deferred for explicit treatment.

## Epistemic Status

*Robust qualitative.* The direction-forcing claim (§5) is derived under standard assumptions (bounded value, deterministic $\pi^\ast$ on the canonical AAD scope). The TV and Pinsker bounds (§§3–4) are textbook results (Tsybakov 2009; Cover & Thomas 2006). The admissible-divergence family characterization (§6) is a truthful survey; reverse-KL is identified as canonical-not-unique on four explicitly-stated non-uniqueness-theorem grounds. The $\beta_\Sigma$ naturalization (§7) is a trade-off analysis, not a derivation — the linear-vs-square-root choice is discussed honestly. The extensions (§9) are sketches, not derivations.

Max attainable: *exact* for the specific claim "forward-KL is a vacuous bound on $R$ under deterministic $\pi^\ast$" (direct calculation; §5) and "Pinsker gives the reverse-KL bound" (standard theorem application; §4). *Robust qualitative* for the overall characterization (direction forced, specific form canonical within family) — the admissible family §6 presentation could become *exact* if a uniqueness result were derived from additional structural constraints (e.g., that reverse-KL uniquely minimizes a specific operational cost among smooth divergences), but this is not currently in hand.

## Discussion

**The convergence with active inference's reverse-KL.** Active inference's expected free energy (Friston et al. 2017; Parr & Pezzulo 2022) also uses reverse-KL against a preferred distribution, with the direction arising from the variational-free-energy-gradient lineage. AAD derives the direction from a regret-bound argument internal to the decision-theoretic scope. The convergence (two distinct derivations reach the same direction) is worth noting but is not a uniqueness argument — it shows reverse-KL is *natural* in multiple frames. The lineage difference preserves AAD's distinctive content: AAD's derivation does not require VFE as master objective or preferences-as-priors ( #ciy-unified-objective, #satisfaction-gap for the contrast).

**Why the regret bound is the right derivation, not Donsker-Varadhan.** The Donsker-Varadhan variational representation

$$\log\mathbb{E}_Q[e^f] \geq \mathbb{E}_P[f] - D_{\mathrm{KL}}(P \Vert Q)$$

gives reverse-KL bounds for exponential-moment functionals, but requires $V$ to have bounded exponential moments (a stronger-than-bounded assumption for unbounded $V$). The Pinsker-TV route used here requires only bounded value range and is closer to the AAD scope's natural assumptions. Donsker-Varadhan becomes relevant if unbounded-$V$ extensions are attempted.

**Relationship to standard policy-gradient regret bounds.** The argument here is structurally identical to standard policy-gradient / online MDP regret bounds (Agarwal, Kakade, Lee, Mahajan 2021 "On the theory of policy gradient methods" Lemma 3.2; Even-Dar, Kakade, Mansour 2009 "Online Markov decision processes"). AAD's contribution is *re-using the standard bound as the derivation of the KL direction in the strategy-cost objective*, not inventing the bound. This is consistent with AAD's integration-over-invention character.

## Working Notes

- **Linear vs. square-root form — revisit with downstream evidence.** The segment keeps the linear-KL form for IB-shape alignment. If downstream work shows the IB-shape-across-four-operations claim in #compression-operations is strained and the four $\beta$s want separate scales anyway, switching #strategy-complexity-cost to the square-root form (naturalizing $\beta_\Sigma$) becomes attractive. Revisit with the O-BP2 (four compressions as one hierarchy) work if pursued.
- **Stochastic-$\pi^\ast$ extension.** Flagged in §9 but not derived. The tied-optimum case is immediate; softmax-smoothed $\pi^\ast$ needs a careful treatment of what regret quantity is being bounded (expected-vs-max).
- **Family characterization strengthening.** A uniqueness theorem for reverse-KL within the smooth-divergence family is open. Candidate structural constraints: "the unique smooth divergence whose second-order expansion equals the Fisher information metric on the policy manifold" (Amari-Nagaoka style) — this would be an exact characterization but requires additional geometric scaffolding. Deferred.
- **Non-Pinsker tighter bounds.** Bretagnolle-Huber gives $\operatorname{TV}(P, Q) \leq \sqrt{1 - e^{-D_{\mathrm{KL}}(P\Vert Q)}}$, which is tighter than Pinsker's $\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}}$ for large $D_{\mathrm{KL}}$. If operational gradients at large $D_{\mathrm{KL}}$ matter, BH is the better choice. Not adopted in the segment because Pinsker-reverse-KL has the cleaner ELBO-alignment story; BH is flagged for operational work where the tightness difference matters.
