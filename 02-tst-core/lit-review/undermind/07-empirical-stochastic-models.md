# Empirically validated stochastic models of software evolution with risk-aware forecasts

## Overview

The retrieved literature provides solid empirical support only for NHPP/renewal-style defect-arrival models in software reliability, with comparative MLE studies and some Bayesian/nonparametric variants [2,3,4,5,6,8,9,10], but contains no empirically fitted Hawkes/branching cascade models, no queueing analyses for CI/review pipelines, and no birth–death lifecycle modeling aligned with the stated agenda.

### What was found relative to the goal
- Clear coverage:
  - Nonhomogeneous Poisson process (NHPP) and renewal-type software reliability growth models (SRGMs) fit to real defect-arrival data in testing and the field, often with broad multi-dataset comparisons and MLE estimation [2,3,4,5,6,8,9,10].
  - Variants include:
    - Parametric families (Weibull, Gamma, Exponential, Power, etc.) with evidence that Weibull NHPP frequently fits best across many releases [5], and that “infinite‑failure” (type‑II) NHPPs can offer early‑testing predictive advantages over traditional finite‑failure ones [2].
    - Proportional‑intensity NHPPs incorporating time‑dependent process covariates (e.g., test execution time), improving fit/prediction in several real projects [4].
    - Nonparametric NHPP estimation with kernel methods and bootstrap uncertainty [6].
    - Domain‑motivated extensions: imperfect debugging/error generation [10], inflection factor with environment uncertainty [8], “dependent failures” within an NHPP mean-value differential form plus optimal release timing [9].
    - A hierarchical Bayesian renewal approach (Weibull inter‑arrival), with MCMC estimation and structured priors [1].
- Missing (relative to the target agenda):
  - Hawkes/branching-process cascade models: no fitted kernels, branching ratios, spectral radii, or cascade‑size distributions; no time‑rescaling diagnostics for self‑excitation [1,2,3,4,5,6,7,8,9,10].
  - Queueing models for CI/review pipelines: no estimation of arrival/service variability or lead-time distribution validation (M/M/1, G/G/1); no stability checks via ρ=λ/μ [1,2,3,4,5,6,7,8,9,10].
  - Birth–death master‑equation modeling of module/file lifecycles or extinction/population dynamics [1,2,3,4,5,6,7,8,9,10].
  - Statistical‑mechanics analyses (criticality/percolation on dependency graphs, generating functions, diffusion/large deviations, heavy‑tail exponents) [1,2,3,4,5,6,7,8,9,10].
  - Modern calibration diagnostics (time‑rescaling/PIT, QQ/tail checks, prospective rolling-origin coverage) largely absent across the set [1,2,3,4,5,6,7,8,9,10].

### Empirical takeaways within the NHPP/SRGM line
- NHPP adequacy and preferred forms:
  - Across 22 releases from four major systems, Weibull NHPP is the best-fitting parametric form in 16/22 cases; naive cross‑release parameter extrapolations often underperform simply reusing the most recent release’s parameters [5].
  - Infinite‑failure (type‑II) NHPP families—constructed from the same detection-time distributions as classic finite‑failure models—can yield better predictive performance in early testing across 16 datasets [2].
- Extensions that improve fit/prediction in some settings:
  - Covariate-augmented proportional‑intensity SRGMs (time‑varying development metrics in intensity) outperform covariate‑free NHPPs on several real datasets [4].
  - Kernel nonparametric NHPP estimation provides flexible mean‑value functions and bootstrap uncertainty quantification without strong parametric commitments [6].
  - Mechanism‑inspired NHPP variants (imperfect debugging/error generation, dependent failures, inflection points, operating‑environment uncertainty) report improved goodness‑of‑fit or error criteria on benchmark datasets [8,9,10].
- Prospective forecasting experiences:
  - OpenBSD case study shows SRGM parameters can be predicted from pre‑release metrics to forecast post‑release defect rates; out‑of‑sample forecasts were evaluated (Theil statistic), but authors note the lack of confidence bounds [3].

### Estimation and validation practices: strengths and gaps
- Strengths:
  - Maximum likelihood estimation is standard; grouped/time‑interval data likelihoods handled explicitly in some works [2,5].
  - Comparative predictive assessments across multiple datasets and model families are common [2,4,5,8,9].
  - Bayesian MCMC appears for renewal inter‑arrival modeling [1]; bootstrap uncertainty used for nonparametric NHPPs [6].
- Gaps (relative to rigorous point‑process and forecast validation):
  - Time‑rescaling/PIT tests for inter‑arrival calibration and Exp(1) residual QQ are not reported [1,2,3,4,5,6,7,8,9,10].
  - Forecast interval coverage and proper scoring (e.g., log score, CRPS) are not emphasized; evaluation often uses fit/error criteria rather than probabilistic calibration [2,3,4,5,6,8,9,10].
  - No tail/QQ analyses to adjudicate heavy tails vs alternatives [1,2,3,4,5,6,7,8,9,10].
  - Limited prospective rolling‑origin evaluation; where present, it is modest in scope [2,3,5].

### Data and tooling
- Multi‑release datasets and multiple real projects are analyzed (field defects, testing fault counts), offering a useful empirical base for NHPP comparisons [2,3,4,5,6,8,9].
- Reproducible code and open datasets are not highlighted in the provided excerpts; one paper is open access but does not indicate tooling [2].

### How to leverage these findings toward the broader agenda
- Establish strong Poisson/renewal baselines with explicit calibration:
  - Adopt Weibull NHPP and its competitors as baseline arrival models, augmented with proportional‑intensity covariates where available [4,5]; validate with time‑rescaling/PIT and forecast interval coverage—elements missing in current practice [2,3,4,5,6,8,9,10].
  - Use nonparametric NHPP with bootstrap to guard against misspecification and quantify uncertainty [6].
- Expand to cascades, queues, and lifecycles with rigorous diagnostics:
  - Fit Hawkes/multivariate branching models for co‑change/failure cascades; report branching ratios/spectral radii with CIs, perform Exp(1) residual tests, and assess cascade‑size distributions—none of which appears in the current corpus.
  - Infer queueing parameters for CI/review pipelines from arrival/service logs and validate lead‑time distributions and stability (ρ<1) via quantile comparisons and Little’s Law coherence checks.
  - Model module/file birth–death dynamics with explicit master equations and extinction analysis; link to observed population growth/decay patterns.
- Integrate statistical‑mechanics insights and early‑warning metrics:
  - Analyze percolation thresholds on dependency/co‑change graphs via degree moments or largest eigenvalue; monitor proximity to criticality, tail thickening, and recovery‑time slowing as early warnings—absent in these works.
  - Where NHPPs are retained, provide decision‑relevant uncertainty (prediction intervals with coverage) for risk assessment in release planning, echoing the operational focus expressed in [3,5,9].

### Paper‑specific contributions and where they fit
- Broad NHPP comparisons and forecasting lessons on field defects [5]; systematic finite vs infinite‑failure NHPP taxonomy and early‑phase predictive advantages [2].
- Covariate‑augmented proportional‑intensity models showing empirical gains [4].
- Nonparametric NHPP with bootstrap uncertainty [6].
- Mechanism‑inspired NHPP variants: imperfect debugging/error generation [10]; dependent‑failure dynamics with optimal release timing [9]; inflection factor and environment uncertainty [8].
- Bayesian hierarchical renewal modeling with MCMC [1].
- Metrics‑driven parameter prediction and prospective case study (OpenBSD), with noted need for CIs [3].

### Key cautions (near‑miss patterns visible here)
- “Dependent” or “cascading” phrasing does not imply fitted Hawkes/branching processes; in these works, dependence is embedded within NHPP mean‑value dynamics, not via self‑exciting kernels or branching ratios [8,9,10].
- Fit‑centric comparisons without time‑rescaling/PIT and interval coverage can mask calibration issues; prioritize residual diagnostics and out‑of‑sample coverage going forward [2,3,4,5,6,8,9,10].

## Categories

### Scope and positioning of the retrieved literature (relative to the target topic)

- The retrieved set is dominated by software reliability growth models based on NHPP and related renewal-type formulations using failure/defect-arrival data from testing and field operations [2,3,4,5,6,8,9,10], with one Bayesian renewal-style approach [1] and one proportional intensity (covariate-augmented) NHPP line [4]. A classic multi-release field-defect forecasting study is included [5], with a focused OpenBSD case study combining metrics and SRGMs [3].
- None of the papers model self-exciting cascades via Hawkes/branching, multivariate criticality via spectral radius, queueing for CI/review pipelines, birth–death master equations for file/module populations, or percolation/criticality on dependency networks, nor do they report time-rescaling/PIT diagnostics for point processes or tail QQ diagnostics. Thus, they cover only a subset of the target agenda: Poisson/renewal arrival modeling of defects, largely within SRGM practice [1,2,3,4,5,6,8,9,10] and without the statistical-mechanics/criticality aspects emphasized in the goal.

---

### Comparative table: Models, data, estimation, and validation

| Ref | Process model class | Empirical data & scope | Estimation | Predictive validation | Calibration diagnostics | Intervals (CIs/PIs) | Notes on tooling/data |
|---|---|---|---|---|---|---|---|
| [2] | NHPP SRMs; 11 finite-failure and 11 “infinite-failure” variants with explicit mean-value functions | 16 real software fault datasets (time-domain and grouped counts) | MLE; likelihood/log-likelihood incl. grouped data | Goodness-of-fit and predictive performance comparisons across models; claim early testing benefits for type-II | No time-rescaling/PIT or residual tests reported | Not explicitly reported | Open access; code/datasets not indicated |
| [5] | NHPP with parametric rate forms (Exponential, Weibull, Logarithmic, Power, etc.) | 22 releases of 4 systems (OS, middleware, OpenBSD, Tomcat); user-reported field defects | MLE and least squares | Forecasting experiments: parameter reuse vs simple extrapolations; Weibull best in 16/22 fits | No time-rescaling/PIT; no tail diagnostics | Confidence bounds not reported in excerpts | Datasets not indicated |
| [3] | SRGMs (Weibull, Gamma, etc.) combined with metrics-based parameter prediction | 10 OpenBSD releases; field defects from bug tracker | Model fitting for SRGMs; metrics-based models to predict SRGM parameters | Out-of-sample forecasts assessed by Theil statistic; replication of AIC-based post-facto results | Not reported | Authors note lack of confidence bounds | Case study; no tooling indicated |
| [4] | Proportional intensity NHPP (PI-SRM) with covariates; 11 fault-detection time distributions | 4 real development datasets; covariates: test execution time, failure ID work, computer time-failure ID | MLE | Comparative goodness-of-fit and predictive performance vs NHPP without covariates | Not reported | Not reported | No code/data indicated |
| [1] | Hierarchical Bayesian dynamic renewal/NHPP-like (Weibull inter-arrival); priors via Boltzmann-machine construct | Software debugging interval-time data (scope not detailed) | Bayesian MCMC; marginal likelihood/EIC for model/prior selection | Framed as prediction; explicit prospective holdout not shown | No time-rescaling reported | Posterior means discussed; interval calibration not shown | Reproducibility details not indicated |
| [6] | Nonparametric NHPP via kernel estimation; bootstrap | System testing fault-count processes | Nonparametric kernel estimation; bandwidth selection; bootstrap | Predictive reliability evaluated data-driven; specifics of holdout not detailed | Not reported | Bootstrap-based uncertainty described | Methodological; datasets not specified in excerpt |
| [8] | NHPP with “inflection factor” in fault-detection rate; environment-uncertainty consideration | Real failure datasets; compared to several NHPP models | Parameter estimation (implied MLE) | Comparative performance using 10 criteria; “predictability” comparisons | Not reported | Not specified | No tooling noted |
| [9] | NHPP with dependent failures; mean-value differential dm/dt = b(t)[a(t) − m(t)] | 3 cumulative-failure datasets (two OCS, one from Lee et al.) | Parameter estimation (implied MLE); cost model | Benchmark vs 21 SRMs using 11 error criteria; sensitivity analysis | Not reported | Not specified | No tooling noted |
| [10] | NHPP SRGM with imperfect debugging and error generation | Not detailed in excerpt | Not detailed in excerpt | Not detailed in excerpt | Not reported | Not reported | Cited by [8,9] |
| [7] | Incoming problem reports modeling (likely arrival process) | Released products; abstract unavailable | Not specified | Not specified | Not specified | Not specified | Not specified |

Key contrasts:
- Breadth and datasets: [5] is the largest multi-system field-defect study (22 releases across four systems), while [2] systematically spans 22 SRM variants on 16 datasets. [3] is a focused single-project longitudinal case (10 releases).
- Model innovation: [4] (covariates via proportional intensity), [6] (nonparametric NHPP), [8] (inflection factor, environment uncertainty), [9] (dependent failures with cost optimization), and [10] (imperfect debugging/error generation) extend the NHPP family beyond canonical SRGMs.
- Estimation paradigms: Predominantly MLE [2,3,4,5,6,8,9,10]; only [1] is hierarchical Bayesian with MCMC.
- Validation rigor: Several compare in-sample GOF and simple predictive metrics [2,3,4,5,8,9], but none report point-process time-rescaling/PIT diagnostics or formal coverage calibration for forecast intervals in the provided excerpts.

---

### Alignment with the target agenda: coverage and gaps by topic

| Agenda item | Strong coverage | Partial/related | Missing/not supported in these papers |
|---|---|---|---|
| Hawkes/self-exciting cascades; branching-process criticality (n, ρ(G)), cascade-size prediction | — | Conceptual “dependent failures/cascades” motivation only [9] | No Hawkes/branching estimation, no kernel/branching ratio, no spectral-radius criticality, no cascade-size distributions [1,2,3,4,5,6,7,8,9,10] |
| Poisson/renewal defect-arrival models with calibrated forecast intervals and PIT | NHPP/SRGM fitted widely [2,3,4,5,6,8,9,10]; renewal-style Weibull inter-arrivals [1,3,5] | Some predictive assessments [2,3,4,5,8,9]; bootstrap uncertainty [6] | No explicit time-rescaling/PIT or interval calibration; limited prospective rolling-origin evaluation [1,2,3,4,5,6,7,8,9,10] |
| Queueing models for CI/review pipelines (lead time distributions, ρ<1, Kingman) | — | — | No queueing inference or lead-time validation [1,2,3,4,5,6,7,8,9,10] |
| Birth–death processes for module/file lifecycles (master equations, extinction) | — | — | No birth–death formulations or lifecycle population dynamics [1,2,3,4,5,6,7,8,9,10] |
| Statistical-mechanics elements (master equations, generating functions, phase transitions, percolation, heavy-tail exponents) | — | Mean-value differential form in [9] is within NHPP SRGM tradition; imperfect debugging/error generation [10] | No generating functions, critical exponents, percolation/eigenvalue thresholds, or large-deviation/diffusion analyses [1,2,3,4,5,6,7,8,9,10] |
| Estimation frameworks (MLE, Bayesian hierarchical) | MLE standard across SRGMs [2,3,4,5,6,8,9,10] | Hierarchical Bayesian with MCMC [1] | No Bayesian hierarchical pooling across projects with stability/criticality priors |
| Validation suite (retrospective fit + prospective holdouts, PIT/time-rescaling, QQ for heavy tails, coverage) | Retrospective GOF + some prospective forecasts [2,3,4,5,8,9] | Nonparametric bootstrap uncertainty [6] | Time-rescaling/PIT, tail QQ, and calibrated coverage absent in excerpts [1,2,3,4,5,6,7,8,9,10] |
| Practical tooling and datasets (reproducible) | — | Open access article [2] | Code/dataset availability not indicated across the set in the provided text |

---

### Synthesis of empirical findings within the NHPP/SRGM track

- NHPP/SRGM adequacy for defect arrivals:
  - Across diverse systems/releases, NHPP models—particularly Weibull—frequently fit defect-arrival data well in-sample; e.g., Weibull NHPP best in 16/22 releases in [5]; similar findings echoed and expanded across model families in [2], and confirmed as effective baselines in [3,4,8,9].
- Model extensions can improve fit/prediction in certain regimes:
  - Infinite-failure (type-II) NHPPs can outperform finite-failure models, especially early in testing, per multi-dataset comparisons in [2].
  - Covariate-augmented proportional-intensity models (PI-SRM) improve fit and predictions compared to covariate-free NHPPs in several cases [4].
  - Nonparametric NHPP with kernel estimation offers data-driven flexibility and bootstrap uncertainty quantification without prespecifying a detection-time family [6].
  - Domain-inspired dynamics—inflection factors with environment uncertainty [8], dependent failures with cost-optimized release time [9], imperfect debugging/error generation [10]—provide alternative mean-value dynamics that outperform baselines on selected datasets [8,9].
- Forecasting lessons from field data:
  - Parameter transferability across releases is limited; naive extrapolations can underperform reusing the most recent parameters about half the time [5], and metrics-based parameter prediction has mixed success though it can support early forecasting [3].
- Methodological limitations relative to calibration:
  - Despite broad fitting and some predictive comparisons, the set does not report point-process time-rescaling/PIT diagnostics, calibrated forecast intervals with coverage checks, or standardized probabilistic scoring (e.g., log score/CRPS). This constrains rigorous assessment of predictive calibration and sharpness in operational settings [1,2,3,4,5,6,7,8,9,10].

---

### What is uniquely contributed by each paper (within this corpus)

- [2] Systematic finite vs infinite-failure NHPP taxonomy and empirical comparison across 16 datasets; grouped-data likelihoods; evidence for early-testing advantages of type-II NHPPs.
- [5] Large-scale, multi-release field-defect forecasting with head-to-head parametric NHPP families; practical lesson that reusing most recent parameters can beat naive extrapolations; Weibull dominance in many releases.
- [3] Integration of SRGMs with pre-release metrics to predict defect-rate trajectories across 10 OpenBSD releases; out-of-sample evaluation with Theil statistics; explicit acknowledgment of missing confidence bounds.
- [4] Proportional-intensity SRGMs embedding time-dependent covariates; generalized over 11 detection-time distributions; empirical gains over standard NHPPs on multiple industrial datasets.
- [1] Hierarchical Bayesian renewal/NHPP-like modeling with MCMC and a structured prior (Boltzmann-machine inspired); positions Bayesian learning within SRGM practice.
- [6] Nonparametric kernel-based NHPP estimation with bootstrap uncertainty; avoids strict parametric assumptions on detection-time distributions.
- [8] NHPP with an inflection factor and explicit treatment of operating-environment uncertainty; comparative evaluation using multiple criteria on real datasets.
- [9] NHPP with dependent failures formulated via dm/dt = b(t)[a(t) − m(t)], coupled to a cost model for optimal release timing; sensitivity analysis across parameters.
- [10] Imperfect debugging and error generation within NHPP SRGM lineage; forms a baseline for dependent-failure and imperfect-debugging comparisons used in [8,9].
- [7] Addresses incoming problem report arrivals post-release; details unavailable in the excerpt, but thematically aligned with arrival-process modeling.

---

### Implications for the broader research goal and immediate opportunities

- Leverage strengths:
  - Use the NHPP/SRGM evidence base to construct calibrated renewal/Poisson baselines for bug/defect arrivals in modern repositories, extending with covariates [4] and nonparametric intensity estimation [6].
  - Incorporate uncertainty quantification via bootstrap [6] or Bayesian MCMC [1], but add formal PIT/time-rescaling diagnostics and coverage checks to meet the calibration standard of the target agenda.
- Fill key gaps:
  - Introduce Hawkes/multivariate branching models for co-change/failure cascades with explicit branching ratio/spectral-radius estimation and time-rescaling tests—absent here but central to the goal.
  - Develop queueing models for CI/review pipelines with inferred arrival/service variability and validated lead-time distributions—no coverage in this set.
  - Model module/file lifecycles with explicit birth–death master equations and extinction probabilities—unaddressed here.
  - Add statistical-mechanics analyses (percolation thresholds on dependency graphs, critical exponents, large deviations) and early-warning metrics tied to criticality—unavailable in these papers.

These steps would preserve the empirically validated NHPP foundations demonstrated in [2,3,4,5,6,8,9,10] while advancing toward the stochastic-process/statistical-mechanics modeling and validation standards specified in the overall goal.

## Timeline

### Timeline of ideas (2004–2022)

- 2004: Move from descriptive defect counts to NHPP-based reliability projection
  - Broad, cross-product empirical evaluation of parametric NHPP software reliability growth models (SRGMs) across 22 releases; Weibull NHPP often best-fitting; simple parameter reuse strategies for forecasting explored [5].
  - Contemporary work models incoming problem reports for released products in an applied stochastic setting, consistent with NHPP framing though details are sparse [7].

- 2005: Early prospective forecasting with real open-source data
  - Case study on OpenBSD couples SRGMs (Weibull/Gamma) with metrics-based parameter prediction for release-level defect rates; includes some out-of-sample forecasting (Theil statistic) but notes lack of confidence bounds [3].

- 2014: Modeling imperfect debugging and error generation within NHPP
  - Introduction of an NHPP SRGM with imperfect debugging and error generation mechanisms, helping to capture practical debugging dynamics within SRGMs [10], later becoming a baseline comparator in subsequent work [8,9].

- 2019–2022: Diversification within NHPP-style models and estimation strategies
  - New NHPP forms with inflection factors and environmental-uncertainty considerations; multi-dataset comparative evaluations with extensive fit criteria [8].
  - “Dependent-failure” NHPP model incorporating cascading/common-cause intuitions, coupled to an economic optimal-release-time analysis; benchmarked against 21 models on real datasets [9].
  - Nonparametric kernel estimation for NHPP mean value functions to reduce model misspecification risk, including bootstrap-based uncertainty quantification [6].
  - Proportional intensity NHPP models with time-dependent covariates (PI-SRM), estimated by MLE, compared across four real projects and shown to improve fit/prediction in many cases [4].
  - Systematic comparison of “infinite-failure” (type-II) vs traditional “finite-failure” (type-I) NHPP families across 16 real datasets, with likelihood-based fitting and predictive comparisons; type-II found advantageous especially in early testing [2].

- 2020: Bayesian renewal-style modeling enters the reliability toolkit
  - Hierarchical Bayesian dynamic modeling for inter-failure intervals using Weibull renewal formulations and structured priors; positioned relative to NHPP SRGMs but emphasizes Bayesian estimation and model/prior selection criteria [1].


### Methodological trends and shifts

- Predominant NHPP paradigm, increasingly flexible
  - Early work establishes NHPP as the empirical workhorse for defect arrivals in the field and during testing, with Weibull often superior among parametric forms [5]. Subsequent studies keep NHPP but enrich model structure: imperfect debugging/error generation [10], inflection/uncertainty factors [8], and dependent-failure dynamics [9].

- Movement from pure time-only to covariate-informed intensities
  - PI-SRMs generalize NHPP by incorporating time-varying development/process metrics as covariates in the intensity, estimated by MLE and evaluated on multiple real datasets [4].

- From parametric to semi/nonparametric NHPP estimation
  - Kernel-based nonparametric approaches reduce reliance on specific mean-value functional forms and provide bootstrap uncertainty assessments [6].

- Exploration of alternative counting-process families within NHPP framing
  - The “infinite-failure” vs “finite-failure” lens reframes classical families and shows practical forecasting implications in early phases [2].

- Bayesian entry via renewal formulations rather than NHPP likelihoods
  - A hierarchical Bayesian approach models inter-arrival distributions directly (Weibull renewal), offering a distinct inferential route and structured priors, though still aligned with classic reliability processes [1].

- Economic decision coupling
  - Reliability models are linked to optimal release-time decisions using cost models, indicating a turn toward operational decision support [9].


### Validation and evaluation practices over time

- Fit-centric comparisons with limited prospective validation
  - Early and many later works emphasize goodness-of-fit across model families, using information criteria and multiple error metrics [5,8,9]. Prospective or rolling evaluations are present but modest (e.g., OpenBSD case study’s out-of-sample tests [3]; predictive comparisons across held-out datasets in type-II vs type-I NHPP analyses [2]).

- Estimation methods
  - Maximum likelihood estimation is standard across NHPP and PI-SRM studies [2,4,5,8,9]. Bayesian MCMC appears in renewal-based modeling [1]. Nonparametric kernel estimation with bootstrap provides uncertainty quantification without strong parametric assumptions [6].

- Diagnostics
  - The surveyed works focus on aggregate fit/error criteria; the literature here does not emphasize point-process residual/time-rescaling diagnostics, tail/QQ checks, or explicit forecast interval calibration reporting in the way common in modern point-process validation. Several papers note the need for better interval/confidence assessments or broader replication [3].


### Key contributors and collaboration clusters

- H. Okamura and collaborators (including T. Dohi, Siqiao Li)
  - Recurrent contributions on NHPP-based SRGMs: nonparametric kernel NHPP estimation with bootstrap [6], proportional intensity NHPPs with covariates [4], and systematic comparisons of type-II (infinite-failure) vs type-I NHPP models with predictive assessments [2]. This cluster has helped modernize classic SRGMs through flexible estimation, covariates, and careful comparative studies.

- P. Li and collaborators (distinct “Li” authors across periods)
  - Early empirical evaluations and forecasting in field settings: cross-product NHPP comparison and parameter reuse strategies [5], and an OpenBSD prospective case study combining SRGMs with metrics-based parameter prediction [3]. This line highlighted the practical forecasting angle and variability across releases.

- H. Pham and collaborators
  - Introduction of NHPP models with inflection factors and environmental-uncertainty considerations, with broad comparative evaluations [8], continuing the tradition of enriched NHPP families in reliability engineering.

- Additional modeling directions
  - Imperfect debugging/error generation NHPP by Roy et al. [10] that became a comparator for later models [8,9].
  - Bayesian hierarchical renewal modeling by Kaise [1], adding a Bayesian perspective to inter-failure modeling.

These clusters suggest a sustained, incremental evolution of NHPP-centric reliability modeling with active efforts to incorporate covariates, flexible estimation, and practical decision linkages. The Okamura–Dohi–S. Li line, in particular, appears as a contemporary hub for systematic empirical evaluation and methodological variation within the NHPP paradigm [2,4,6].


### Milestones and their significance

- Establishing Weibull NHPP as a strong empirical baseline across diverse systems [5]
  - Provided a practical default and benchmark for subsequent model developments and comparisons.

- Prospective forecasting case study on a major open-source system [3]
  - Early demonstration that SRGMs could be tied to real release planning, while also surfacing the need for uncertainty quantification.

- Incorporating imperfect debugging/error generation into NHPP [10]
  - Brought process-realistic mechanisms into SRGMs, informing later dependent-failure and uncertainty-aware models [8,9].

- Nonparametric NHPP reliability evaluation with bootstrap [6]
  - Reduced model form risk and introduced more explicit uncertainty quantification in SRGM predictions.

- Proportional intensity SRGMs with time-varying covariates [4]
  - Marked a shift toward explanatory, process-aware intensities beyond purely time-based forms.

- Infinite-failure NHPP families and predictive advantage in early testing [2]
  - Reframed classical categories with practical forecasting implications, broadening the toolkit for early-phase reliability planning.

- Economic decision coupling via optimal release time under dependent failures [9]
  - Tightened the connection between stochastic modeling and actionable software release decisions.


### Relation to the stated research agenda: gaps and opportunities highlighted by this corpus

- Point-process cascades and branching/Hawkes models
  - Although some works discuss dependent/cascading failures conceptually [9], none in this set estimate Hawkes or branching-process models, report branching ratios/spectral radii, or perform time-rescaling diagnostics aligned with self-excitation analysis [2,3,4,5,6,7,8,9,1].

- Queueing models for CI/review pipelines
  - No queueing formulations (e.g., M/M/1, G/G/1) are fitted to software pipeline data in this set [2,3,4,5,6,7,8,9,1].

- Birth–death process master-equation approaches to module/file lifecycles
  - The surveyed works stay within reliability growth via NHPP/renewal and do not model lifecycle birth–death dynamics with master equations or extinction analyses [2,3,4,5,6,7,8,9,1].

- Validation depth and calibration
  - While MLE (and in one case Bayesian) estimation are used with comparative fit metrics and some predictive checks, modern diagnostics such as time-rescaled residuals, PIT/coverage for forecast intervals, and tail QQ plots are generally not emphasized here [2,3,4,5,6,7,8,9,1,5,3,6,4].

- Reproducible tooling and datasets
  - Several papers analyze established reliability datasets or multiple real projects, but the excerpts do not emphasize open tooling or fully reproducible pipelines in the contemporary sense [2,3,4,5,6,7,8,9,1,5,3,6,4].

Given these gaps, the next wave of work connecting software evolution to stochastic-process/statistical-mechanics models would likely build on the established NHPP reliability base by:
- Incorporating explicit self-exciting/branching formulations for cascades with criticality metrics and calibrated forecasting,
- Bringing queueing inference to CI/review/ops pipelines for lead-time risk,
- Modeling codebase lifecycles via birth–death master equations, and
- Strengthening validation with time-rescaling, interval calibration, and tail diagnostics—complementing the fit-centric comparative tradition exemplified in this corpus.

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [125] | 0.21 | 2% | Time-Dependent Error-Detection Rate Model for Software Reliability and Other Performance Measures | A. Goel and K. Okumoto | IEEE Transactions on Reliability | 1979 | 1783 | [1, 2, 6, 8, 9, 10, 13, 15] |
| [91] | 0.13 | 2% | Software Reliability: Measurement, Prediction, Application | J. Musa, ..., and K. Okumoto | N/A | 1987 | 1830 | [2, 3, 6, 13, 17, 21] |
| [10] | 0.11 | 14% | AN NHPP SOFTWARE RELIABILITY GROWTH MODEL WITH IMPERFECT DEBUGGING AND ERROR GENERATION | P. Roy, ..., and K. Dey | International Journal of Reliability, Quality and Safety Engineering | 2014 | 33 | [8, 9, 21, 24, 40] |
| [5] | 0.10 | 22% | Empirical evaluation of defect projection models for widely-deployed production software systems | P. Li, ..., and P. Santhanam | N/A | 2004 | 116 | [3, 4, 13, 22] |
| [305] | 0.09 | 1% | Handbook of software reliability engineering | M. Lyu | N/A | 1996 | 1423 | [2, 3, 5, 6, 13] |
| [9] | 0.09 | 16% | A Software Reliability Model with Dependent Failure and Optimal Release Time | Youn Su Kim, ..., and I. Chang | Symmetry | 2022 | 21 | [25, 59, 177, 229] |
| [87] | 0.07 | 3% | Modelling Failures Occurrences of Open Source Software with Reliability Growth | B. Rossi, ..., and G. Succi | N/A | 2010 | 72 | [13, 29, 37, 55, 75] |
| [259] | 0.06 | 1% | Software Reliability Models: Assumptions, Limitations, and Applicability | A. Goel | IEEE Transactions on Software Engineering | 1985 | 948 | [2, 6, 10, 13] |
| [8] | 0.06 | 17% | NHPP Software Reliability Model with Inflection Factor of the Fault Detection Rate Considering the Uncertainty of Software Operating Environments and Predictive Analysis | Kwangyoon Song, ..., and H. Pham | Symmetry | 2019 | 25 | [25, 40, 100, 200] |
| [35] | 0.06 | 5% | A Unified Approach for Developing Software Reliability Growth Models in the Presence of Imperfect Debugging and Error Generation | P. K. Kapur, ..., and Kalpana Yadav | IEEE Transactions on Reliability | 2011 | 181 | [8, 9, 10] |
| [303] | 0.05 | 1% | Predicting Software Reliability | A. Wood | Computer | 1996 | 269 | [2, 5, 10] |
| [263] | 0.05 | 1% | A testing-coverage software reliability model with the uncertainty of operating environments | I. Chang, ..., and Kwangyoon Song | International Journal of Systems Science: Operations & Logistics | 2014 | 51 | [8, 9] |
| [541] | 0.05 | Not measured | A new software reliability model with Vtub-shaped fault-detection rate and the uncertainty of operating environments | H. Pham | Optimization | 2014 | 80 | [8, 9] |
| [459] | 0.04 | 0% | A Multivariate Characterization and Detection of Software Performance Antipatterns | Alberto Avritzer, ..., and Jörg Henß | Proceedings of the ACM/SPEC International Conference on Performance Engineering | 2021 | 11 | [13] |
| [441] | 0.04 | 0% | PPTAMλ: What, Where, and How of Cross-domain Scalability Assessment | Alberto Avritzer, ..., and Catia Trubiani | 2021 IEEE 18th International Conference on Software Architecture Companion (ICSA-C) | 2021 | 9 | [13] |
| [27] | 0.04 | 6% | A general imperfect-software-debugging model with S-shaped fault-detection rate | H. Pham, ..., and Zuemei Zhang | IEEE Transactions on Reliability | 1999 | 287 | [8, 9, 10] |
| [542] | 0.04 | Not measured | Understanding and predicting effort in software projects | A. Mockus, ..., and Ping Zhang | 25th International Conference on Software Engineering, 2003. Proceedings. | 2003 | 117 | [3, 5] |
| [182] | 0.04 | 1% | Finding predictors of field defects for open source software systems in commonly available data sources: a case study of OpenBSD | P. Li, ..., and M. Shaw | 11th IEEE International Software Metrics Symposium (METRICS'05) | 2005 | 54 | [3, 13, 87] |
| [104] | 0.04 | 2% | A logarithmic poisson execution time model for software reliability measurement | J. Musa and K. Okumoto | N/A | 1984 | 607 | [2, 6] |
| [343] | 0.04 | 0% | Use of software triggers to evaluate software process effectiveness and capture customer usage profiles | Kathryn Bassin and P. Santhanam | Proceedings The Eighth International Symposium on Software Reliability Engineering | 1997 | 18 | [5, 13, 87] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref. | Adjacency score | Topic Match | Title | Authors | Journal | Year | Total Citations | References These Foundational Papers |
|---|---|---|---|---|---|---|---|---|
| [13] | 0.30 | 12% | Modeling Performance of Microservices Systems with Growth Theory | Matteo Camilli and Barbara Russo | Empirical Software Engineering | 2022 | 12 | [5, 87, 91, 233, 288, 343, 384, 410] |
| [87] | 0.14 | 3% | Modelling Failures Occurrences of Open Source Software with Reliability Growth | B. Rossi, ..., and G. Succi | N/A | 2010 | 72 | [5, 91, 108, 182, 233, 343] |
| [546] | 0.07 | Not measured | On the adoption of neural networks in modeling software reliability | Kamill Gusmanov | Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering | 2018 | 6 | [87, 91, 233] |
| [201] | 0.05 | 1% | Characterizing defect trends in software support | Tung Thanh Nguyen, ..., and T. Nguyen | Companion Proceedings of the 36th International Conference on Software Engineering | 2014 | 0 | [5, 343] |
| [239] | 0.05 | 1% | Defect Prediction using Combined Product and Project Metrics - A Case Study from the Open Source "Apache" MyFaces Project Family | D. Wahyudin, ..., and S. Biffl | 2008 34th Euromicro Conference Software Engineering and Advanced Applications | 2008 | 36 | [5, 343] |
| [3] | 0.05 | 25% | Forecasting field defect rates using a combined time-based and metrics-based approach: a case study of OpenBSD | P. Li, ..., and M. Shaw | 16th IEEE International Symposium on Software Reliability Engineering (ISSRE'05) | 2005 | 47 | [5, 91, 182, 290, 305] |
| [407] | 0.05 | 0% | Approximating Deployment Metrics to Predict Field Defects and Plan Corrective Maintenance Activities | W. Snipes, ..., and Penelope A. Brooks | 2009 20th International Symposium on Software Reliability Engineering | 2009 | 5 | [5, 91, 182] |
| [55] | 0.05 | 3% | Applicability of Software Reliability Growth Models to Open Source Software | Radoslav Micko, ..., and B. Rossi | 2022 48th Euromicro Conference on Software Engineering and Advanced Applications (SEAA) | 2022 | 2 | [87, 91, 125] |
| [547] | 0.05 | Not measured | Comparing the reliability of software systems: A case study on mobile operating systems | Vladimir Ivanov, ..., and G. Succi | Inf. Sci. | 2018 | 48 | [3, 87, 233] |
| [548] | 0.05 | Not measured | CNN LSTM Network Architecture for Modeling Software Reliability | Kamill Gusmanov | N/A | 2019 | 0 | [87, 233] |
| [549] | 0.05 | Not measured | Comparison of mobile operating systems based on models of growth reliability of the software | G. Succi and V. Ivanov | Computer Research and Modeling | 2018 | 3 | [87, 233] |
| [550] | 0.05 | Not measured | Evolutionary partitioning regression with function stacks | D. Ashlock and J. A. Brown | 2016 IEEE Congress on Evolutionary Computation (CEC) | 2016 | 1 | [87, 233] |
| [5] | 0.05 | 22% | Empirical evaluation of defect projection models for widely-deployed production software systems | P. Li, ..., and P. Santhanam | N/A | 2004 | 116 | [290, 303, 305, 343, 542, 543] |
| [498] | 0.04 | 0% | Staffing Strategies for Maintenance of Critical Software Systems at the Jet Propulsion Laboratory | W. Taber and D. Port | Proceedings of the 10th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement | 2016 | 3 | [5, 384] |
| [551] | 0.04 | Not measured | Optimal Release Time Determination in Intuitionistic Fuzzy Environment Involving Randomized Cost Budget for SDE-Based Software Reliability Growth Model | S. Chatterjee, ..., and C. Bhar | Arabian Journal for Science and Engineering | 2019 | 12 | [87, 91] |
| [552] | 0.04 | Not measured | STRAIT: A Tool for Automated Software Reliability Growth Analysis | Stanislav Chren, ..., and B. Rossi | 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR) | 2019 | 4 | [87, 91] |
| [2] | 0.04 | 28% | Are Infinite-Failure NHPP-Based Software Reliability Models Useful? | Siqiao Li, ..., and H. Okamura | Software | 2022 | 2 | [91, 125, 259, 303, 305] |
| [75] | 0.04 | 3% | Mining Bugzilla datasets with new increasing failure rate software reliability models | N. R. Barraza | 2017 XLIII Latin American Computer Conference (CLEI) | 2017 | 3 | [87, 108] |
| [6] | 0.04 | 20% | Data-driven software reliability evaluation under incomplete knowledge on fault count distribution | T. Dohi, ..., and H. Okamura | Quality Engineering | 2020 | 5 | [91, 125, 259, 305] |
| [200] | 0.04 | 1% | Empowering software reliability: Leveraging efficient fault detection and removal efficiency | Umashankar Samal and Ajay Kumar | Quality Engineering | 2024 | 11 | [8, 10, 91, 125] |