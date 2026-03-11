---
slug: update-gain
type: empirical-claim
status: exact (Kalman/conjugate), robust-qualitative (general)
depends:
  - mismatch-signal
  - observation-function
---

# Update Gain

The optimal weight an agent assigns to new observations when updating its model balances model uncertainty against observation noise.

## Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^*$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*
$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch (#mismatch-signal) and $g(\cdot)$ is a correction mapping from observation space to model update space.

## Epistemic Status

*Exact* for linear-Gaussian systems (where $\eta^*$ is the Kalman gain) and conjugate Bayesian systems. For general adaptive systems (RL agents, organizational learning, biological adaptation), it is *robust qualitative* — any optimal adaptation process must approximate this functional dependence, even if the variance ratio is not explicitly computed.

## Discussion

**Limiting behavior.** When $U_M \gg U_o$ (high model uncertainty — e.g., after initialization or structural adaptation), $\eta^* \to 1$: trust the observation. When $U_M \ll U_o$ (confident model, noisy channel), $\eta^* \to 0$: trust the model. The gain determines how strongly the agent corrects toward reality on each update.

**Gain collapse.** When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^* \to 0$ and the agent stops learning. Mismatches are ignored, producing confirmation bias or a decoupled reality model.

**Multi-dimensional generalization.** In vector-valued systems, $U_M$ and $U_o$ are covariance matrices and $\eta^*$ becomes a gain matrix (as in the Kalman filter). The scalar form captures the essential structure.

**Connection to adaptive tempo.** The update gain is one factor in the agent's adaptive tempo (#adaptive-tempo): $\mathcal{T} = \nu \cdot \eta^*$. Updating frequently (high $\nu$) is useless if the updates extract no information (low $\eta^*$). Gain measures the *quality* of the update cycle; event rate measures its *speed*.