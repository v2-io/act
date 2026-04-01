# Synthesis Report: Stochastic Processes in Software Evolution (Research Topic 6)

## Executive Summary

The systematic investigation of stochastic process applications to software evolution reveals a **profound but explicable gap** between theoretical potential and empirical reality[^1]. While the literature provides extensive work on Non-Homogeneous Poisson Process (NHPP) models—specifically for **software reliability and fault arrival during testing**[^2]—the critical components needed for broader software evolution and the Temporal Software Theory remain **entirely absent** from empirical research. This gap exists not from oversight but from disciplinary boundaries: software engineering researchers rarely possess deep stochastic process training, while stochastic process experts rarely engage with software data.

## Part I: What Was Found vs. What Was Sought

### Dominant Finding: NHPP Reliability Models (Narrow Focus)

The corpus overwhelmingly consists of NHPP-based Software Reliability Growth Models (SRGMs), but these are **narrowly focused on fault/bug arrival during testing phases**, not general software evolution[^3]:

**Empirical Coverage (Testing Context)**:
- **Weibull NHPP**: Dominates across 16-22 datasets of testing faults, often providing best fit[^4]
- **Infinite-failure variants**: Outperform finite-failure models in early testing phases[^5]
- **Environmental uncertainty models**: Inflection factors and Rayleigh rates for test environments[^6]
- **Covariate-augmented models**: Time-dependent testing effort as proportional intensity[^7]

**Mathematical Formulations (Cumulative Fault Models)**:
$$m(t) = a(1 - e^{-bt^c})$$ (Weibull NHPP - cumulative faults detected)
$$\frac{dm}{dt} = b(t)[a(t) - m(t)]$$ (Dependent-failure NHPP - fault detection rate)

### Critical Absences: The Missing Pillars

**1. Hawkes/Branching Cascades**: **ZERO EMPIRICAL STUDIES**
- No branching ratio $\eta$ or spectral radius $\rho(G)$ estimation on software data
- No cascade-size distributions $P(\text{cascade} = k)$
- No criticality assessment ($\eta \approx 1$ or $\rho \approx 1$)
- No self-exciting kernels $\phi(t)$ fitted to fix/change cascades

**2. Queueing Theory for CI/CD Pipelines**: **NOT FOUND**
- No M/M/1, G/G/1, or processor sharing models for review queues
- No arrival rate $\lambda$ and service rate $\mu$ inference from pipeline logs
- No lead-time distribution validation
- No Little's Law verification: $L = \lambda W$

**3. Birth-Death Master Equations**: **COMPLETELY ABSENT**
- No $\frac{dP_n}{dt} = \lambda_{n-1}P_{n-1} - (\lambda_n + \mu_n)P_n + \mu_{n+1}P_{n+1}$
- No file/module population dynamics
- No extinction probability calculations
- No generating function solutions

## Part II: Methodological Assessment

### Current Practice Limitations

**Validation Gaps**[^8]:
- **No time-rescaling tests**: Residuals should be $\text{Exp}(1)$ if model correct
- **No PIT diagnostics**: Probability integral transform uniformity unchecked
- **Limited holdout testing**: Mostly retrospective fits, not prospective forecasts
- **No tail diagnostics**: QQ plots for heavy-tailed phenomena absent

**Estimation Methods**:
- Dominated by MLE and nonlinear regression[^9]
- Bayesian approaches rare (1 hierarchical model found)[^10]
- Bootstrap uncertainty only in 1 study[^11]

### One Bridging Insight: Microservices Performance

The Russo-Camilli study represents a notable bridge between reliability modeling and operational performance[^12]:
- Models performance violations using NHPP-style growth curves
- **Explicitly recognizes** equivalence to $M_t/D/\infty$ (infinite-server queue)
- Authors demonstrate **awareness** of queueing connection: "S-shaped models can be interpreted as queueing systems where all arrivals are immediately served"
- BUT: No actual queue parameter inference performed ($\lambda$, $\mu$ not estimated)
- Represents **conceptual awareness** that could be extended to full queueing analysis

## Part III: Why This Gap Matters for Temporal Theory

### Direct Mapping to Framework Theorems

The missing stochastic components map precisely to specific theorems in the Temporal Software Theory:

**For T-03 (Lindy Effect/Change Persistence)**:
- Need: Population-level validation with confidence intervals on $E[\text{changes}_\text{future}]$
- Found: Only cumulative fault counts during testing, not ongoing change-pattern distributions
- Gap: No validation of Pareto distributions in change frequencies across system lifetime
- **Impact**: Cannot provide probabilistic bounds on future change expectations

**For T-04 (Investment Principle)**:
- Need: Risk-adjusted ROI under cascade uncertainty for refactoring decisions
- Found: Deterministic cost models only[^13]
- Gap: No option value theory, no cascade risk quantification
- **Impact**: Cannot justify refactoring under uncertainty about cascade effects

**For T-09/T-10 (Proximity and Coupling)**:
- Need: Random walks on dependency graphs, first-passage times for change propagation
- Found: Static coupling metrics without temporal dynamics
- Gap: No diffusion processes or spectral radius conditions
- **Impact**: Cannot predict change propagation patterns or critical thresholds

**For T-14 (Continuous Operation Under Perturbation)**:
- Need: Recovery time distributions, cascade propagation under shocks
- Found: Simple failure rates without propagation dynamics
- Gap: No percolation thresholds or phase transitions
- **Impact**: Cannot identify when systems become fragile or predict cascade boundaries

## Part IV: Statistical Mechanics—The Unfulfilled Promise

### Phase Transitions and Critical Phenomena: **NOT FOUND**

Despite rich theoretical potential:
- No percolation thresholds for bug spread
- No critical coupling measurements
- No universality classes identified
- No scaling laws near criticality

### Entropy and Information: **PRESENT BUT UNAPPLIED**

Information-theoretic concepts appear but remain disconnected from evolution dynamics:
- **Veldhuizen's domain entropy** (2005-2007): Establishes information-theoretic bounds on reuse fraction[^14]
  - Shows $\text{reuse fraction} \leq 1 - H$ where $H$ is domain entropy
  - **Critical insight**: Provides theoretical foundation but never applied to evolution
- **Gap in application**: No code entropy growth models over time
- **Missing connection**: No maximum entropy principles for change prediction
- **Unexplored**: Free energy minimization analogies for architectural evolution

### Network Science: **ABSENT**

Zero studies on:
- Scale-free degree distributions in dependencies
- Small-world properties in software architecture
- Preferential attachment in module growth
- Community detection for optimal boundaries

## Part V: The Positive Foundation

### What Can Be Built Upon

**1. Strong NHPP Baseline**:
- Extensive empirical validation across diverse systems
- Well-established parameter estimation methods
- Can serve as exogenous arrival layer for more complex models

**2. Methodological Sophistication Within Limits**:
- Okamura-Dohi-Li cluster: Advancing nonparametric methods[^15]
- Song-Chang-Pham-Kim thread: Environmental uncertainty modeling[^16]
- Infrastructure exists for extension

**3. Decision-Oriented Extensions**:
- Cost models coupled to reliability trajectories[^17]
- Optimal release timing frameworks
- Ready for risk-based enhancement

## Part VI: Mathematical Opportunities

### Immediate Extensions Possible

**1. Hawkes Process Layer**:
```python
λ(t) = μ + Σ φ(t - t_i)  # Self-excitation
branching_ratio = ∫ φ(t)dt  # Criticality measure
```

Apply to:
- CI failure cascades
- Co-change bursts
- Incident propagation chains

**2. Queueing Theory Application**:
From existing arrival models, infer:
- Service distributions from pipeline logs
- Utilization $\rho = \lambda/\mu$
- Sojourn time validation

**3. Master Equation Formulation**:
For file populations:
$$\frac{dP_n}{dt} = \text{birth}_n - \text{death}_n$$

With solutions via generating functions:
$$G(z,t) = \sum_{n=0}^{\infty} P_n(t)z^n$$

## Part VII: Critical Research Agenda

### Priority 1: Empirical Hawkes/Branching Studies

**Required**:
1. Multivariate Hawkes fitting to software event streams
2. Branching ratio estimation with confidence intervals
3. Criticality assessment: $\eta < 1$ (subcritical) vs $\eta \geq 1$ (critical/supercritical)
4. Cascade-size prediction validation

**Data Sources**:
- CI/CD failure logs with timestamps
- Bug tracker cascades (bug fixes triggering new bugs)
- Dependency update chains

### Priority 2: Queueing Inference for Pipelines

**Required**:
1. Arrival and service distribution fitting
2. Queue length and waiting time validation
3. Little's Law coherence checks
4. Capacity planning models

**Data Sources**:
- GitHub Actions/Jenkins logs
- Code review timing data
- Build queue metrics

### Priority 3: Birth-Death Lifecycle Models

**Required**:
1. Module creation/deletion rate estimation
2. Population equilibrium analysis
3. Extinction probability calculation
4. Diffusion approximations near criticality

**Data Sources**:
- Git history (file births/deaths)
- Module evolution tracking
- Architecture element turnover

## Part VIII: Theoretical Implications

### For Temporal Software Theory

The absence of these stochastic models means:

1. **No uncertainty quantification** for time predictions
2. **No cascade risk assessment** for architectural decisions
3. **No queue-theoretic bounds** on development throughput
4. **No extinction risks** for module sustainability

### For Software Engineering Practice

Without these models, we cannot:
- Predict when cascading failures will occur
- Optimize pipeline capacity
- Assess module viability
- Identify critical thresholds

## Conclusion: Understanding the Gap

The investigation reveals that stochastic process modeling in software engineering remains **embryonic** despite decades of NHPP reliability work. Importantly, this gap has **structural causes**:

1. **Disciplinary boundaries**: Software engineering researchers focus on practical tools; stochastic process experts focus on traditional applications (finance, biology, physics)
2. **Data challenges**: Software event data is messier than classical point process applications—irregular sampling, missing data, non-stationarity
3. **Unclear value proposition**: Before the Temporal Software Theory provided a unifying framework, the connection between these models and practical outcomes wasn't evident

The field has extensively studied **fault arrival during testing** but ignored **evolution dynamics**—cascades, queues, and lifecycles—precisely the phenomena that matter for modern continuous deployment.

This gap represents both a **critical weakness** and an **extraordinary opportunity**. The mathematical machinery exists in other fields[^18]; the software data exists in repositories[^19]; the Temporal Theory now provides the framework connecting them. Only the empirical bridge remains unbuilt.

The Temporal Software Theory's time-based optimization cannot achieve its full potential without probabilistic bounds, confidence intervals, and risk assessments that only stochastic models can provide. Building this bridge is not merely an academic exercise but a practical necessity for software engineering's evolution from craft to science.

---

## References

[^1]: [[6-RESEARCH-GOALS-stochastic-processes.md]] - Original research objectives
[^2]: [[../refs/undermind-6.md]], lines 13-15 - Summary of findings
[^3]: Li, S., Dohi, T., & Okamura, H. (2022). "Are Infinite-Failure NHPP-Based Software Reliability Models Useful?" Software, 2(3)
[^4]: Li, P., et al. (2004). "Empirical evaluation of defect projection models for widely-deployed production software systems." ICSE 2004
[^5]: [[../refs/undermind-6.md]], reference [3] - Infinite vs finite failure comparison
[^6]: Song, K., Chang, I., & Pham, H. (2019). "NHPP Software Reliability Model with Inflection Factor." Symmetry, 11(4)
[^7]: Li, S., et al. (2022). "Comprehensive Analysis of Proportional Intensity-Based Software Reliability Models with Covariates." Electronics
[^8]: [[../refs/undermind-6.md]], lines 73-76 - Validation gaps
[^9]: [[../refs/undermind-6.md]], lines 487-489 - Estimation practices
[^10]: Kaise, T. (2020). "Software Reliability Analysis Based on Hierarchical Dynamic Models and Bayesian Estimations." ISCIE International Symposium
[^11]: Dohi, T., & Okamura, H. (2020). "Data-driven software reliability evaluation under incomplete knowledge." Quality Engineering
[^12]: Camilli, M., & Russo, B. (2022). "Modeling Performance of Microservices Systems with Growth Theory." Empirical Software Engineering, 27(1)
[^13]: [[../refs/undermind-6.md]], lines 492-494 - Decision-oriented outputs
[^14]: Veldhuizen, T.L. (2005, 2007). "Software Libraries and Their Reuse: Entropy, Kolmogorov Complexity, and Zipf's Law." ArXiv
[^15]: [[../refs/undermind-6.md]], lines 651-666 - Okamura-Dohi-Li research cluster
[^16]: [[../refs/undermind-6.md]], lines 667-671 - Song-Chang-Pham-Kim thread
[^17]: Kim, Y.S., Song, K., & Chang, I. (2022). "Software Reliability Model with Dependent Failure and Optimal Release Time." Symmetry
[^18]: Kanazawa, K., & Sornette, D. (2020). "Field master equation theory of the self-excited Hawkes process." Physical Review Research
[^19]: [[../a-mathematical-theory-of-software-evolution--temporal-software-theory.md]] - Framework requiring stochastic extensions