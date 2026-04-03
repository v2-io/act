---
slug: discrete-sector-condition
type: derivation
status: exact
depends:
  - sector-condition-derivation
  - update-gain
  - gain-sector-bridge
  - event-driven-dynamics
stage: draft
---

# Derivation: Discrete-Time Sector Condition

Discrete-time analogs of Props A.1, A.1S, and A.2 via contraction mapping, closing the fluid-limit gap (GA-5) between the event-driven dynamics ( #event-driven-dynamics) and the continuous-time Lyapunov results in #sector-condition-derivation.

## Formal Expression

### Setup

The discrete mismatch dynamics at event step $k$ are:

*[Definition (Discrete Dynamics)]*

$$\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$$

where $\eta^\ast$ is the update gain ( #update-gain), $F_d$ is the discrete correction direction, and $w_k$ is the per-step disturbance. The continuous correction function $F(\mathcal{T}, \delta)$ from #sector-condition-derivation decomposes as $F = \nu \cdot \eta^\ast \cdot F_d$ at event rate $\nu$.

### (DA2') Discrete Sector Condition

*[Assumption DA2' (discrete-sector-condition)]*

There exist constants $c_{\min} > 0$ and $c_{\max} < 2/\eta^\ast$ such that for all $\lVert\delta\rVert \leq R$:

$$c_{\min} \lVert\delta\rVert^2 \leq \delta^T F_d(\delta) \leq c_{\max} \lVert\delta\rVert^2$$

The **lower bound** ($c_{\min}$) is directional fidelity — the correction points inward, identical to the continuous sector condition (A2') from #sector-condition-derivation via #gain-sector-bridge.

The **upper bound** ($c_{\max} < 2/\eta^\ast$) is the **no-overshoot condition**: each correction step must not reverse the mismatch. This is the classical step-size condition $\eta^\ast < 2/L$ for gradient descent (where $L$ is the Lipschitz constant of the gradient). For Bayesian updates, this is satisfied by construction — the posterior lies between prior and data.

### Contraction factor

Under DA2', the per-step Lyapunov function $V_k = \frac{1}{2}\lVert\delta_k\rVert^2$ satisfies:

*[Derived (contraction, from DA2')]*

$$\lVert\delta_{k+1} - 0\rVert^2 \leq \lambda^2 \lVert\delta_k\rVert^2 + 2\lVert\delta_k\rVert \lVert w_k\rVert + \lVert w_k\rVert^2$$

where:

$$\lambda = \max(\lvert 1 - \eta^\ast c_{\min}\rvert,\; \lvert 1 - \eta^\ast c_{\max}\rvert)$$

DA2' ensures $\lvert\lambda\rvert < 1$: the lower bound gives $1 - \eta^\ast c_{\min} < 1$, and the upper bound gives $1 - \eta^\ast c_{\max} > -1$.

### Proposition DA.1: Bounded Mismatch (Deterministic)

**Statement.** Under DA2' with bounded per-step disturbance $\lVert w_k\rVert \leq \rho_{\text{step}}$, the mismatch is ultimately bounded:

*[Derived (DA.1, discrete bounded mismatch)]*

$$R^\ast_D = \frac{\rho_{\text{step}}}{1 - \lvert\lambda\rvert}$$

**Proof.** The contraction mapping yields:

$$\lVert\delta_{k+1}\rVert \leq \lvert\lambda\rvert \lVert\delta_k\rVert + \rho_{\text{step}}$$

This is an affine contraction with $\lvert\lambda\rvert < 1$. By the Banach fixed-point theorem, all trajectories starting in $\mathcal B_R$ converge to the ball of radius $R^\ast_D = \rho_{\text{step}}/(1 - \lvert\lambda\rvert)$, provided $R^\ast_D < R$. $\square$

**Recovery of continuous result.** In the fluid limit ($\eta^\ast \to 0$, $\nu \to \infty$, $\nu \eta^\ast = \mathcal{T}$ fixed), $\lambda \to 1 - \eta^\ast c_{\min}$ and $\rho_{\text{step}} \to \rho/\nu$. Then:

$$R^\ast_D = \frac{\rho/\nu}{\eta^\ast c_{\min}} = \frac{\rho}{\nu \eta^\ast c_{\min}} = \frac{\rho}{\alpha}$$

recovering Prop A.1 exactly. The discrete-to-continuous gap for Model D steady state is **zero**.

### Proposition DA.2: Adaptive Reserve (Discrete)

**Statement.** Under the conditions of DA.1, the agent can absorb an additional per-step disturbance of:

*[Derived (DA.2, discrete adaptive reserve)]*

$$\Delta\rho^\ast_{\text{step}} = (1 - \lvert\lambda\rvert) R - \rho_{\text{step}}$$

**Proof.** Identical to Prop A.2: the new $R^\ast_D = (\rho_{\text{step}} + \Delta\rho)/(1 - \lvert\lambda\rvert)$ must satisfy $R^\ast_D \leq R$. $\square$

The structure is identical to the continuous adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$, with $\alpha$ replaced by the discrete contraction rate $(1 - \lvert\lambda\rvert)/\eta^\ast$ (which equals $\alpha$ in the fluid limit).

### Proposition DA.1S: Stochastic Bounded Mismatch (Discrete)

**Statement.** Under DA2' with i.i.d. zero-mean disturbance $\mathbb{E}[w_k] = 0$, $\mathbb{E}[\lVert w_k\rVert^2] = \sigma^2_{\text{step}}$, the mismatch satisfies:

*[Derived (DA.1S, discrete stochastic bounded mismatch)]*

$$\mathbb{E}[\lVert\delta_k\rVert^2] \leq \lambda^{2k}_{\text{eff}} \lVert\delta_0\rVert^2 + \frac{\sigma^2_{\text{step}}}{1 - \lambda^2_{\text{eff}}}$$

where $\lambda^2_{\text{eff}} = 1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c^2_{\max}$.

**Proof.** Define $V_k = \lVert\delta_k\rVert^2$. Taking expectations of the squared update:

$$\mathbb{E}[V_{k+1} \mid \delta_k] = \lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert^2 + \sigma^2_{\text{step}}$$

The first term satisfies:

$$\lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert^2 = V_k - 2\eta^\ast \delta_k^T F_d(\delta_k) + (\eta^\ast)^2 \lVert F_d(\delta_k)\rVert^2$$

By DA2' (lower bound on $\delta^T F_d$ and upper bound implying $\lVert F_d\rVert^2 \leq c^2_{\max} V_k$):

$$\mathbb{E}[V_{k+1} \mid \delta_k] \leq \lambda^2_{\text{eff}} V_k + \sigma^2_{\text{step}}$$

This is a supermartingale (when $V_k$ is large enough). Iterating:

$$\mathbb{E}[V_k] \leq \lambda^{2k}_{\text{eff}} V_0 + \frac{\sigma^2_{\text{step}}}{1 - \lambda^2_{\text{eff}}}$$

The steady-state mean-square mismatch is $\sigma^2_{\text{step}} / (1 - \lambda^2_{\text{eff}})$. $\square$

**Recovery of continuous result.** In the fluid limit: $\sigma^2_{\text{step}} \to n\sigma^2_w / \nu$, $\lambda^2_{\text{eff}} \to 1 - 2\eta^\ast c_{\min}$, and $(1 - \lambda^2_{\text{eff}}) \to 2\eta^\ast c_{\min}$. The steady-state becomes $n\sigma^2_w / (2\nu \eta^\ast c_{\min}) = n\sigma^2_w / (2\alpha)$, recovering Prop A.1S exactly.

The discrete-to-continuous gap for Model S variance is $O((\eta^\ast)^2 c^2_{\max})$ — the $(\eta^\ast)^2 \lVert F_d\rVert^2$ term that vanishes in the fluid limit. This quantifies the error introduced by GA-5 and confirms it is small whenever $\eta^\ast c_{\max} \ll 1$.

### Fluid Limit Theorem

*[Derived (Conditional on Lipschitz regularity)]*

**Statement.** Let $F_d$ be Lipschitz continuous with constant $L_F$ on $\mathcal B_R$. Let $\delta^{(\nu)}(t)$ denote the piecewise-constant interpolation of the discrete trajectory at event rate $\nu$, and $\delta(t)$ the solution of the continuous ODE $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$ with $F = \nu \eta^\ast F_d$. Then:

$$\sup_{t \in [0,T]} \lVert\delta^{(\nu)}(t) - \delta(t)\rVert \leq C \cdot \frac{\eta^\ast c_{\max}}{\nu^{1/2}}$$

for a constant $C$ depending on $T$, $L_F$, and $R$.

**Sketch.** This follows from the standard ODE-approximation theory for Euler schemes (Kushner & Yin, 2003, Ch. 5). The discrete update $\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$ is a forward Euler step for the ODE with step size $1/\nu$. The Lipschitz condition on $F_d$ ensures the local truncation error is $O(1/\nu^2)$. Summing over $O(\nu T)$ steps and applying the Gronwall inequality gives the $O(1/\nu^{1/2})$ bound.

For Model D (deterministic): the steady-state gap is exactly zero (both discrete and continuous converge to the same fixed point). The fluid-limit error affects only transients.

For Model S (stochastic): the steady-state variance gap is $O((\eta^\ast)^2 c^2_{\max})$, which equals $O(\eta^\ast c_{\max} / \nu)$ when expressed in terms of the event rate.

## Epistemic Status

**DA.1 and DA.2** are *exact* — standard contraction-mapping results. The proofs require only the discrete sector condition DA2', which is itself derived from the gain principle + directional fidelity ( #gain-sector-bridge) for well-designed agents.

**DA.1S** is *exact* under the stated i.i.d. assumption. The supermartingale argument is standard.

**Fluid limit theorem** is *conditional* on Lipschitz regularity of $F_d$ — a standard regularity condition satisfied by all correction functions in the verified instances table ( #gain-sector-bridge). The convergence rate follows from classical ODE approximation theory (Kushner & Yin, 2003); the application to the ACT mismatch dynamics is new but the mathematics is not.

**Max attainable:** exact for DA.1/DA.2/DA.1S; conditional for the fluid limit (Lipschitz cannot be removed).

## Discussion

**GA-5 is closed.** The fluid-limit bridging assumption is no longer required as an ungrounded assumption. For Model D, the discrete and continuous steady states are identical — the gap is zero. For Model S, the gap is $O(\eta^\ast c_{\max})$ in variance, quantitatively bounded and small in the regime where $\eta^\ast c_{\max} \ll 1$. The continuous-time results in #sector-condition-derivation are formally justified as the fluid limit of the discrete results here.

**The upper bound is the classical step-size condition.** The no-overshoot condition $c_{\max} < 2/\eta^\ast$ (equivalently $\eta^\ast < 2/c_{\max}$) is the same constraint as the step-size condition $\eta < 2/L$ for gradient descent, the stability condition for the Kalman gain, and the convergence condition for fixed-point iteration. For Bayesian updates, it is satisfied by construction. The discrete framework reveals this constraint, which is invisible in the continuous limit.

**No downstream results change qualitatively.** The persistence condition, adaptive reserve, and adversarial scaling laws derived in #sector-condition-derivation and #adversarial-destabilization hold as stated. The discrete framework provides sharper constants (replacing $\alpha$ with $(1 - \lvert\lambda\rvert)/\eta^\ast$) and a quantitative transient error bound, but the qualitative structure is unchanged.

**Section I's formal chain is now complete.** The prediction chain:

$$\text{gain principle} + \text{B1} \;\xrightarrow{\text{derived}}\; \text{sector condition} \;\xrightarrow{\text{Lyapunov/contraction}}\; \text{persistence, reserve, scaling}$$

holds in both continuous time (via #sector-condition-derivation) and discrete time (via this segment), with a quantitative bridge between them (the fluid limit theorem).

## Working Notes

- Non-stationary gain: when $\eta^\ast$ varies over time (as in Kalman filtering with growing $P^-$), the contraction factor $\lambda$ changes per step. The ultimate bound still holds if $\sup_k \lvert\lambda_k\rvert < 1$, but the transient analysis requires time-varying contraction arguments.
- Heavy-tailed disturbances: DA.1S assumes finite second moment. Sub-Weibull or heavy-tailed $w_k$ would need truncation arguments or alternative Lyapunov functions. These extreme cases are better modeled as triggers for structural adaptation ( #structural-adaptation-necessity).
- Non-i.i.d. disturbances: correlated $w_k$ (e.g., Markov environment noise) weakens the supermartingale argument. The contraction still holds per-step, but the steady-state bound requires mixing conditions. This connects to the adversarial coupling analysis in #adversarial-destabilization.
