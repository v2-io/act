---
slug: strategy-cost-regret-bound
type: derivation
status: robust-qualitative
depends:
  - strategy-complexity-cost
  - value-object
  - objective-functional
  - chain-confidence-decay
  - strategy-dag
stage: draft
---

# Derivation: Regret-Bound Derivation of the Strategy-Cost KL Direction

The variational form of the strategy-cost objective ( #strategy-complexity-cost) carries a $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ relevance term. This appendix derives that **the $\pi^\ast$-first KL direction is forced** as the non-vacuous regret-bound form, and proves (conditional on a chain-rule additivity axiom motivated by #chain-confidence-decay) that **reverse-KL is uniquely forced within the direction-forced f-divergence family**.

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

### §6 — Admissible-divergence family and uniqueness of reverse-KL

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

**What is uniquely forced by the regret-bound argument alone.** The direction: the reference $\pi^\ast$ is first. This is a real derivation outcome, not a selection. Within the $\pi^\ast$-first family, multiple f-divergences each give valid bounds; an additional structural axiom is required to pick one uniquely.

#### §6.1 — Chain-rule uniqueness theorem

*[Derived (reverse-kl-uniqueness, Conditional on chain-rule axiom)]*

**Theorem (Csiszár 1972; Amari 2009).** *Let $D_f(P\Vert Q) = \sum_x Q(x) f(P(x)/Q(x))$ be a smooth f-divergence with $f$ convex and $f(1) = 0$. The chain rule*

$$D_f(P_{XY} \Vert Q_{XY}) \;=\; D_f(P_X \Vert Q_X) \;+\; \mathbb{E}_{P_X}\!\left[D_f(P_{Y\mid X} \Vert Q_{Y\mid X})\right]$$

*holds for all joint distributions $(X, Y)$ if and only if $f(t) = c \cdot t\log t$ for some $c \gt 0$ — i.e., $D_f$ is reverse-KL up to positive scaling.*

**References.** Csiszár 1972, *Periodica Mathematica Hungarica* 2:191–213; Amari 2009, *IEEE Trans. Info. Theory* 55(11):4925–4931, Theorem 1; Amari & Cichocki 2010, *Bull. Pol. Acad. Sci. Tech. Sci.* 58(1):183–195, Prop. 3.2.

**Why other members of the family fail the chain rule.** Concrete counterexample for $\chi^2$: take $Q_X$ uniform on $\{x_1, x_2\}$, $P_X = (3/4, 1/4)$, $Q(y\mid x)$ uniform, $P(y\mid x) = (3/4, 1/4)$ for both $x$. Direct calculation gives $\chi^2(P_{XY}\Vert Q_{XY}) = 9/16$, while $\chi^2(P_X\Vert Q_X) + \mathbb{E}_{P_X}[\chi^2(P_{Y\mid X}\Vert Q_{Y\mid X})] = 1/4 + 1/4 = 8/16$. Non-additive: $9/16 \neq 8/16$. Rényi-$\alpha$ for $\alpha \neq 1$ fails analogously; Bretagnolle-Huber is a monotone transform of reverse-KL (not an independent f-divergence); Hellinger-squared ($\alpha = 0$) likewise fails.

**AAD-internal motivation for the chain-rule axiom.** The chain rule is the *divergence-level analog* of the additive log-confidence decay in `#chain-confidence-decay`. AAD has already committed to additive-mismatch-decomposition-along-causal-chains in that segment; the divergence-level parallel is:

$$D(\pi^\ast \Vert Q_{\Sigma_t}) \;=\; \sum_{t=1}^T \mathbb{E}_{\pi^\ast}\!\left[D\bigl(\pi^\ast(\cdot\mid a_{\lt t}^\ast) \,\big\Vert\, Q(\cdot\mid a_{\lt t}^\ast)\bigr)\right]$$

— total mismatch between $\pi^\ast$ and $Q_{\Sigma_t}$ decomposes additively over the DAG's causal layers along the optimal trajectory. Non-chain-rule divergences (e.g., $\chi^2$) give super-additive decompositions in which layer-mismatches amplify multiplicatively — structurally discordant with the DAG factorization ( #strategy-dag). Adopting the chain-rule axiom is therefore not arbitrary; it is the divergence-level version of a decomposition principle AAD already relies on.

**Corollary (within the chain-rule axiom).** Under deterministic $\pi^\ast$ + bounded value + chain-rule additivity, reverse-KL is the unique smooth f-divergence in the direction-forced admissible family. The "Reverse-KL canonical among smooth divergences" status upgrades from formulation choice (under the pre-axiom reading) to *Derived (conditional on the chain-rule axiom)*.

**What the uniqueness theorem does not do.** It fixes the divergence within the f-divergence family; it does not fix the bounding function $g$ around the divergence (Pinsker vs Bretagnolle-Huber vs Le Cam-on-$\chi^2$ are *different bounds using different divergences*, so only Pinsker and BH-on-KL remain in scope after uniqueness — and these differ only in the $g$-envelope on top of reverse-KL, not in the divergence itself). It does not resolve the linear-vs-square-root form question of §7 (that is a Lagrangian-shape choice orthogonal to the divergence choice). Monotone transforms of reverse-KL (e.g., $1 - e^{-D_{\mathrm{KL}}}$) are equivalence-class members for gradient-based optimization and are not ruled out.

**Scope of the axiom.** The chain rule is stated for arbitrary joint decompositions. AAD's strategy spaces are discrete at the proposition level; the theorem applies directly. For continuous strategy spaces (e.g., low-level control), the chain rule extends via Amari & Nagaoka 2000 §3.5; no new subtleties.

#### §6.2 — Secondary characterizations (now supporting rather than load-bearing)

Four additional properties further motivate reverse-KL as the canonical choice; under §6.1 they are no longer load-bearing for uniqueness but remain informative about why reverse-KL is a comfortable fit with the rest of the AAD framework:

1. **Gradient-tractability.** TV is non-differentiable at mass boundaries; reverse-KL is smooth. Operational minimization via gradient methods rules out TV despite its tightness — independent of the uniqueness argument.
2. **Variational-inference alignment.** Reverse-KL is the standard divergence in the variational-inference lineage (ELBO derivation uses reverse-KL; Friston et al. 2017; Da Costa et al. 2020). The V-medium move's rhetorical payoff — shared vocabulary with active inference — lives on reverse-KL specifically. This is *convergent evidence* that reverse-KL is natural in multiple frames, not an independent uniqueness argument (Path D in `msc/spike-reverse-kl-uniqueness.md` §6 shows the ELBO decomposition itself uses the chain rule as a sub-step; logical priority is chain rule → reverse-KL → ELBO).
3. **Fisher geometry.** Reverse-KL's second-order expansion gives the Fisher information metric (Amari & Nagaoka 2000). *But by Eguchi's theorem* (Eguchi 1983, *Annals of the Institute of Statistical Mathematics* 35(1):1–24), every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric at second order up to the scalar $f''(1)$. Fisher-metric-at-second-order is *not* a distinguishing axiom within the f-divergence family — it is satisfied by every member. Noted here because it is a commonly-invoked distinguishing property; it does not distinguish.
4. **Information-budget / MDL interpretation.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ is the expected extra bits needed to code samples from $\pi^\ast$ under $Q_{\Sigma_t}$'s code. The coding interpretation aligns with the segment's MDL framing. MDL is itself a chain-rule-respecting coding scheme (the bits-to-code-a-joint decompose additively over factorizations); consistency with MDL is convergent with §6.1.

**Čencov/Morozova-Chentsov background** (Čencov 1982 *Statistical Decision Rules and Optimal Inference*, AMS; Morozova & Chentsov 1991; Ay, Jost, Lê & Schwachhöfer 2017, *Information Geometry*, Springer). The f-divergence family itself is characterized by Markov-morphism invariance (sufficient-statistic coarse-graining invariance) — this is what makes "f-divergences" the right background family to search within. Amari 2009 shows the alpha-divergences are the sub-family that are simultaneously f-divergences and Bregman divergences. Reverse-KL sits at $\alpha = 1$ within the alpha-family; the chain-rule axiom of §6.1 is what picks $\alpha = 1$ out of the one-parameter alpha-family.

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

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Regret definition $R(Q_{\Sigma_t}) := V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V]$ | Definitional; collapses to the three literature forms under deterministic $\pi^\ast$ | Definition |
| TV-regret bound $R \leq V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$ | Bounded value range + deterministic $\pi^\ast$ | Proved (tight) |
| Pinsker-KL bound $R \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ | Pinsker's inequality applied to TV bound | Proved |
| **KL direction forced** (reverse-KL, $\pi^\ast$-first) | Forward-KL is vacuous ($+\infty$) under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass | **Proved (direction uniquely forced)** |
| **Reverse-KL uniquely forced within direction-forced f-divergences** | Chain-rule additivity axiom (Csiszár 1972; Amari 2009 Theorem 1); AAD-internally motivated as divergence-level analog of #chain-confidence-decay (§6.1) | **Derived (conditional on chain-rule axiom)** |
| Secondary characterizations (gradient-tractability, VI-alignment, MDL coding) | Independent operational properties; each compatible with reverse-KL, none individually distinguishing | Formulation support (non-load-bearing under §6.1) |
| Fisher-metric-at-second-order does not distinguish reverse-KL | Eguchi's theorem (Eguchi 1983): every smooth f-divergence with $f''(1) \gt 0$ induces the Fisher metric up to scalar $f''(1)$ | Proved (no-go for Path A as uniqueness axiom) |
| Admissible family members (TV, Bretagnolle-Huber, $\chi^2$, Rényi-$\alpha$) | Each yields a valid regret bound; survey §6 | Derived (each) |
| TV is tightest; Pinsker is loose by $\sqrt{\cdot}$ | Standard tightness analysis (Tsybakov 2009 §2.4) | Proved (comparison) |
| $\beta_\Sigma \propto V_{\max}$ naturalization (square-root-KL form) | Direct identification from Pinsker bound | Derived (under square-root form) |
| $\beta_\Sigma$ local interpretation (linear-KL form, segment-retained) | Differentiation of Pinsker bound at operating point | Derived (local only) |
| Linear-KL form retained over square-root form | IB-shape alignment with #compression-operations | Formulation choice |
| Vacuity regimes ($V_{\max}=\infty$, $Q_{\Sigma_t}(a^\ast)=0$, stochastic $\pi^\ast$) | Direct analysis of the bound | Proved (boundary) |
| Tied-optimum extension | $\pi^\ast$ uniform on $\mathcal{A}^\ast$; bound adapts directly | Derived |
| Softmax-smoothed $\pi^\ast$ extension | Sketched in §9 | Hypothesis (deferred) |
| Uniqueness under chain-rule axiom (§6.1) | Csiszár 1972 / Amari 2009 Theorem 1 applied to the direction-forced family; axiom AAD-internally motivated (§6.1) | Derived (conditional) |

The dividing line: the KL **direction** is forced by the regret-bound derivation (strong result). The specific reverse-KL **form** within the direction-forced f-divergence family is *derived under the chain-rule additivity axiom* (§6.1) — conditional on an axiom that AAD independently motivates as the divergence-level version of the additive-decomposition principle already in #chain-confidence-decay. The $\beta_\Sigma$ naturalization is partial — available globally only under the square-root form, locally under the linear form retained for IB-shape alignment.

## Epistemic Status

*Robust qualitative.* The direction-forcing claim (§5) is derived under standard assumptions (bounded value, deterministic $\pi^\ast$ on the canonical AAD scope). The TV and Pinsker bounds (§§3–4) are textbook results (Tsybakov 2009; Cover & Thomas 2006). The admissible-divergence family characterization (§6) is a truthful survey. The **chain-rule uniqueness theorem (§6.1)** upgrades the reverse-KL selection from "canonical-not-unique" to "uniquely forced conditional on the chain-rule axiom"; the axiom is AAD-internally motivated as the divergence-level analog of #chain-confidence-decay. Fisher-metric-at-second-order is explicitly identified as *not* a distinguishing axiom within the f-divergence family (Eguchi's theorem), closing the most-obvious candidate uniqueness route as a no-go. The $\beta_\Sigma$ naturalization (§7) is a trade-off analysis, not a derivation — the linear-vs-square-root choice is discussed honestly. The extensions (§9) are sketches, not derivations.

Max attainable: *exact* for the specific claim "forward-KL is a vacuous bound on $R$ under deterministic $\pi^\ast$" (direct calculation; §5), "Pinsker gives the reverse-KL bound" (standard theorem application; §4), and "reverse-KL is the unique chain-rule-respecting f-divergence in the direction-forced family" (Csiszár 1972 / Amari 2009 uniqueness applied; §6.1). *Robust qualitative* for the overall strengthened characterization — the uniqueness is conditional on the chain-rule axiom, which is a principled axiom choice (AAD-internally motivated, §6.1) but remains an axiom rather than a consequence of prior AAD commitments.

## Discussion

**The convergence with active inference's reverse-KL.** Active inference's expected free energy (Friston et al. 2017; Parr & Pezzulo 2022) also uses reverse-KL against a preferred distribution, with the direction arising from the variational-free-energy-gradient lineage. AAD derives the direction from a regret-bound argument internal to the decision-theoretic scope. The convergence (two distinct derivations reach the same direction) is worth noting but is not a uniqueness argument — it shows reverse-KL is *natural* in multiple frames. The lineage difference preserves AAD's distinctive content: AAD's derivation does not require VFE as master objective or preferences-as-priors ( #ciy-unified-objective, #satisfaction-gap for the contrast).

**Why the regret bound is the right derivation, not Donsker-Varadhan.** The Donsker-Varadhan variational representation

$$\log\mathbb{E}_Q[e^f] \geq \mathbb{E}_P[f] - D_{\mathrm{KL}}(P \Vert Q)$$

gives reverse-KL bounds for exponential-moment functionals, but requires $V$ to have bounded exponential moments (a stronger-than-bounded assumption for unbounded $V$). The Pinsker-TV route used here requires only bounded value range and is closer to the AAD scope's natural assumptions. Donsker-Varadhan becomes relevant if unbounded-$V$ extensions are attempted.

**Relationship to standard policy-gradient regret bounds.** The argument here is structurally identical to standard policy-gradient / online MDP regret bounds (Agarwal, Kakade, Lee, Mahajan 2021 "On the theory of policy gradient methods" Lemma 3.2; Even-Dar, Kakade, Mansour 2009 "Online Markov decision processes"). AAD's contribution is *re-using the standard bound as the derivation of the KL direction in the strategy-cost objective*, not inventing the bound. This is consistent with AAD's integration-over-invention character.

## Working Notes

- **Linear vs. square-root form — revisit with downstream evidence.** The segment keeps the linear-KL form for IB-shape alignment. If downstream work shows the IB-shape-across-four-operations claim in #compression-operations is strained and the four $\beta$s want separate scales anyway, switching #strategy-complexity-cost to the square-root form (naturalizing $\beta_\Sigma$) becomes attractive. Revisit with the O-BP2 (four compressions as one hierarchy) work if pursued.
- **Stochastic-$\pi^\ast$ extension.** Flagged in §9 but not derived. The tied-optimum case is immediate; softmax-smoothed $\pi^\ast$ needs a careful treatment of what regret quantity is being bounded (expected-vs-max).
- **Family characterization strengthening.** *Resolved 2026-04-22* — see §6.1. The chain-rule additivity axiom (Csiszár 1972; Amari 2009) picks reverse-KL uniquely within the direction-forced f-divergence family. The Fisher-metric candidate was ruled out by Eguchi's theorem (every smooth f-divergence induces the Fisher metric at second order up to scale; not distinguishing). Full reasoning trail in `msc/spike-reverse-kl-uniqueness.md`.
- **Non-Pinsker tighter bounds.** Bretagnolle-Huber gives $\operatorname{TV}(P, Q) \leq \sqrt{1 - e^{-D_{\mathrm{KL}}(P\Vert Q)}}$, which is tighter than Pinsker's $\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}}$ for large $D_{\mathrm{KL}}$. If operational gradients at large $D_{\mathrm{KL}}$ matter, BH is the better choice. Not adopted in the segment because Pinsker-reverse-KL has the cleaner ELBO-alignment story; BH is flagged for operational work where the tightness difference matters.
