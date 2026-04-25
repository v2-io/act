---
slug: result-per-dimension-persistence
type: result
status: conditional
depends:
  - result-persistence-condition
  - def-adaptive-tempo
  - deriv-sector-condition
stage: draft
---

# Result: Per-Dimension Persistence

The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension, with the form depending on whether the disturbance is deterministic (Model D) or stochastic (Model S).

## Formal Expression

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance:

### Model D: Deterministic Per-Dimension Threshold

Under bounded disturbance $\lvert w_k(t)\rvert \leq \rho_k$ (GA-2, per dimension), the per-dimension steady-state mismatch is:

$$\lvert\delta_k\rvert_{ss} = \frac{\rho_k}{\alpha_k}$$

**Persistence requires** $\alpha_k \gt \rho_k / R_k$ **for each dimension**, or in linear operational form:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

This is the deterministic worst-case bound — exact under bounded disturbance by the same Lyapunov argument as Prop A.1, applied per dimension.

### Model S: Stochastic Per-Dimension Steady State

Under stochastic disturbance $w_{k,t} \sim N(0, \rho_k^2)$ (GA-2S, per dimension), the discrete AR(1) process $\delta_{k,t+1} = (1 - \eta_k)\delta_{k,t} + w_{k,t}$ has stationary distribution:

$$\delta_k \sim N\!\left(0,\; \frac{\rho_k^2}{2\eta_k - \eta_k^2}\right)$$

The stationary distribution supplies three task-adequacy criteria, each with its own threshold. The choice of criterion is an engineering decision; the three are related by exact constants for Gaussian $\delta_k$.

**(a) RMS bound** (mean-square, matches the scalar form in #result-persistence-condition):

$$\sqrt{E[\delta_k^2]} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}}$$

Requiring $\sqrt{E[\delta_k^2]} \lt \delta_{\text{critical},k}$ and using the small-$\eta_k$ approximation $2\eta_k - \eta_k^2 \approx 2\eta_k$:

$$\boxed{\;\eta_k \gt \frac{\rho_k^2}{2\,\delta_{\text{critical},k}^2}\;} \quad \text{(RMS criterion)}$$

This is the scalar Model S threshold in #result-persistence-condition ($\alpha \gt n\sigma_w^2/(2R^2)$) applied per dimension.

**(b) MAE bound** (mean absolute error; bounds the expected deviation rather than its square):

$$E\!\left[\lvert\delta_k\rvert\right] = \sqrt{E[\delta_k^2]} \cdot \sqrt{\frac{2}{\pi}} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

Requiring $E\!\left[\lvert\delta_k\rvert\right] \lt \delta_{\text{critical},k}$:

$$\eta_k \gt \frac{\rho_k^2}{\pi\,\delta_{\text{critical},k}^2} \quad \text{(MAE criterion)}$$

MAE is smaller than RMS by the factor $\sqrt{2/\pi} \approx 0.798$, so the MAE threshold is $2/\pi \approx 0.637$ times the RMS threshold. The criteria differ by a constant but bound different quantities; applying the same numerical $\delta_{\text{critical},k}$ under both does not mean the same thing.

**(c) Probability bound** (tail-risk criterion, for applications where occasional excursions matter):

$$P\!\left(\lvert\delta_k\rvert \gt \delta_{\text{critical},k}\right) \lt \epsilon \;\Longleftrightarrow\; \eta_k \gt \frac{\rho_k^2 \cdot z_{1-\epsilon/2}^2}{2\,\delta_{\text{critical},k}^2}$$

where $z_{1-\epsilon/2}$ is the two-sided Gaussian quantile. The probability bound at $\epsilon = 0.05$ (two-sided $z \approx 1.96$) is about $1.96^2 \approx 3.84$ times the RMS threshold — stricter because it bounds tail excursions rather than typical magnitudes.

**Recommended primary form.** The RMS criterion (a) is the canonical form for Model S persistence, matching the scalar treatment in #result-persistence-condition and the Lyapunov-based derivation in #deriv-sector-condition (Prop A.1S). The MAE and probability-bound variants are provided for applications where those are the natural task-adequacy measures. All three thresholds are quadratic in $\rho_k/\delta_{\text{critical},k}$ (not linear as in Model D), reflecting the $1/\sqrt{\alpha}$ scaling of the Model S stationary variance.

### Common Structure

The aggregate $L_2$ mismatch $\lVert\delta\rVert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio (Model S) or $\rho_k / \alpha_k$ ratio (Model D). The qualitative conclusion — the weak dimension is the bottleneck — holds for both models.

## Epistemic Status

*Exact conditional on disturbance model.* Both per-dimension forms are now derived from their respective disturbance models:

1. **Model D threshold** ($\mathcal T_k \gt \rho_k/\delta_{\text{critical},k}$) follows from Prop A.1 applied per dimension — the same Lyapunov argument with bounded disturbance, restricted to each coordinate. This is exact under GA-2 + GA-3.

2. **Model S steady state** follows from the AR(1) stationary distribution under Gaussian disturbance (GA-2S): $\delta_k \sim N(0, \rho_k^2/(2\eta_k - \eta_k^2))$. The RMS, MAE, and probability-bound thresholds are all exact under this distribution, differing by the constants $1$, $\sqrt{2/\pi}$, and $z_{1-\epsilon/2}$ respectively. The RMS form $\eta_k \gt \rho_k^2/(2\delta_{\text{critical},k}^2)$ matches the scalar Model S treatment in #result-persistence-condition applied per dimension. The 4-significant-figure simulation match validates Model S, not Model D.

The previously noted "regime mixing" is resolved: the two threshold forms belong to different disturbance models. The Model D threshold is linear in $\rho_k$; the Model S threshold is quadratic. The 72% scalar overestimate and weak-dimension bottleneck are structural properties that hold under both models.

## Discussion

**Scalar tempo overestimates.** In a 3D system with gains $\eta = (0.15, 0.03, 0.03)$ and disturbances $\rho = (0.20, 0.20, 0.02)$:

| Dimension | $\eta_k$ | $\rho_k$ | $\rho_k / \eta_k$ | $E[\Vert\delta_k\Vert]$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 (well-tracked) | 0.15 | 0.20 | 1.33 | 0.303 |
| 2 (weak) | 0.03 | 0.20 | 6.67 | 0.656 |
| 3 (unimportant) | 0.03 | 0.02 | 0.67 | 0.066 |

Scalar prediction: $\rho / \mathcal{T} = 0.284 / 0.21 = 1.35$. Actual $\Vert\delta\Vert_{L_2} = 0.785$. Overestimate: 72%. Dimension 2 alone accounts for 84% of the $L_2$ mismatch.

**Isotropic allocation dominates.** Equalizing the same total gain budget ($\eta = 0.07$ per dimension) reduces $\Vert\delta\Vert_{L_2}$ from 0.785 to 0.685 — a 13% improvement — because it reduces the bottleneck effect on the weak dimension.

**Adversarial exploitation.** An adversary who identifies the target's weak dimension can concentrate disturbance there. Targeted attack (80% on the weak dimension) amplifies the mismatch ratio by 17% (from 2.70 to 3.15). The real danger is structural: if the weak dimension's mismatch exceeds its critical threshold ($R_{\text{max}}$), correction fails on that dimension while the aggregate $\Vert\delta\Vert_{L_2}$ may still look manageable. Per-dimension monitoring is essential.

**Implications for the persistence condition.** Like the scalar result, per-dimension persistence addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the correction machinery on each dimension can outpace that dimension's disturbance rate. An agent can be structurally persistent on every dimension while still being operationally fragile on one (near its per-dimension $R_k$ boundary). The scalar persistence condition ( #result-persistence-condition) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition has two forms: Model D ($\mathcal T_k \gt \rho_k/\delta_{\text{critical},k}$, exact under bounded disturbance) and Model S ($\eta_k \gt \rho_k^2/(\pi \cdot \delta_{\text{critical},k}^2)$, exact under Gaussian disturbance). Both predict per-dimension failure correctly; the choice depends on the disturbance character in the domain.

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

## Working Notes
- The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question — it likely does qualitatively (the weakest dimension still dominates) but the quantitative overestimate may shrink.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) would replace the scalar $\mathcal{T}$ with a diagonal matrix $\mathcal{T} = \text{diag}(\mathcal T_1, \ldots, \mathcal T_d)$. The persistence condition becomes $\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$ for each $k$. This is mentioned in #def-adaptive-tempo's Discussion but not yet formalized.
- Simulation code: `../../msc/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
