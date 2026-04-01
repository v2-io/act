# Empirical time-based ROI models for software maintenance, debt, and options

## Overview

The search did not find any single work that delivers the fully integrated, hours-first, capital-budgeting and options/portfolio framework you seek; instead, complementary pieces exist—compound-interest/breaking-point models and hours-based stocks/flows [1,2,4,10], strong before/after operational evidence for refactoring benefits in person-hours [5], portfolio selection for TD (database normalization) with covariance [6,8], and empirical value–maintainability relations showing nonlinear returns [7]—while queueing-theoretic CFt construction, calibrated real-options valuation, and ex-ante/ex-post capital-budgeting validation remain notably absent [1,2,3,4,5,6,7,8,9,10].

### What aligns most strongly with your criteria
- Compound interest and “breaking point” for technical debt
  - FITTED formalizes continuous/compound TD interest, evolving principal, and a “breaking point” where cumulative interest equals principal; principal is estimated from code-level artifacts and converted with an hourly rate [1]. Prior foundational work on “breaking point” and financial framing underpins FITTED [4,10].
- Hours as the unit of account in system-level dynamics
  - A system‑dynamics model explicitly represents TD principal in man‑hours, interest as extra maintenance hours, and team capacity; compounding effects arise via feedback (maintainability → productivity → backlog → further TD) [2].
- Empirical, time-based outcomes of paying down architecture debt
  - A longitudinal industrial case quantifies refactoring effort (563.8 person‑hours) and reports sizable improvements in time-to-close issues, bug-fix duration (−30%), and throughput (more change requests completed), with statistical support [5].
- Portfolio theory applied to technical debt items
  - Normalization debts are prioritized using Markowitz mean–variance with correlations among items [6]; later extended with multi-attribute ranking (TOPSIS) and an industrial case [8]. These provide an optimization scaffold (risk/return, covariance), albeit not yet in hours-first throughput terms.

### Where the results fall short of the target (critical gaps)
- Hours-first capital budgeting with CoD in CFt and r from opportunity cost
  - No paper computes NPV/IRR/payback in hours while keeping cost-of-delay only in CFt and deriving r from the opportunity cost of developer time [1,2,3,4,5,6,7,8,9,10].
- Queueing-theoretic linkage from TD to CFt
  - None connect TD-induced service-time inflation to Kingman-based delay growth and then to time-denominated cashflows [1,2,3,4,5,6,7,8,9,10].
- Empirical interest rates in hours/month, amortization, and ceiling effects
  - While compounding and breaking points are modeled [1,4,10] and SD feedbacks suggest compounding [2], we found no calibrated monthly “interest rate” (e.g., 5–15%/month) expressed as hours/month per hour of principal, no amortization schedules, and no explicit debt-ceiling/ρ→1 analysis [1,2,3,4,5,6,7,8,9,10].
- Real options with calibrated parameters (closed-form/binomial/Monte Carlo)
  - Options are proposed for cloud TD decisions [9], but the surveyed texts do not map S0, K, σ, q to hours or calibrate volatility from delivery/CoD variability, nor do they backtest [9].
- Ex-ante versus ex-post validation and sensitivity
  - Except for before/after operational improvements [5], the literature here lacks ex-ante locked predictions with ex-post evaluation and sensitivity/robustness analyses for NPV/IRR/PI/option values [1,2,3,4,5,6,7,8,9,10].

### What you can reuse immediately from the found works
- Calibrating compounding models and “breaking points”
  - Use FITTED’s constructs and measurement pipeline (code metrics → principal and interest) to initialize compound-interest models and estimate when cumulative interest equals principal; retrofit to hours-first by keeping all flows in hours before converting to currency [1,4,10].
- Deriving realized payback and PI from empirical refactor data
  - From [5], compute realized payback_h: compare 563.8 hours against monthly hours saved via reduced bug-fix duration and increased throughput; this enables an ex-post check of capital-budgeting measures (payback_h, PI_h) even though the paper did not compute them explicitly [5].
- Portfolio scaffolding with correlations
  - The Markowitz framework applied to database normalization can be adapted: define per-item “return” as expected hours saved (or throughput gain) and risk as variance of delivery time/throughput; retain covariance structure to compute an efficient frontier under capacity constraints [6,8].
- Nonlinear benefit curves
  - The value-creation model showing amplified returns at high maintainability supports concave/convex benefit functions μ_i(x_i) in portfolio optimization and informs option payoff convexity for architectural flexibility [7].

### Practical synthesis plan to close the gaps (evidence-based, using these sources)
- Hours-first capital budgeting
  - Adopt [2]’s hours-based stocks/flows and [1]’s measurement of principal/interest; compute NPV_h/IRR_h with cost-of-delay embedded in CFt (via hours of delay × shadow price of developer time) and r set to the organization’s opportunity cost. Validate ex-post using datasets like [5].
- Queueing-theoretic CFt construction
  - Pair measured service-time changes from interventions (e.g., bug-fix duration drop in [5]) with a Kingman-based M/G/1 approximation to translate TD-driven service-time inflation into queueing delays and then into CFt_h; this adds the missing operational link.
- Technical-debt interest rates and amortization
  - From operational data (extra rework hours, service-time inflation) and estimated principal (à la [1,2]), compute i_m = interest hours per month per hour of principal; track under remediation schedules to estimate amortization and detect ceiling effects as utilization approaches thresholds.
- Calibrated real options for architectural flexibility
  - Use variability in CFt_h/time-saved from longitudinal data [5] and dispersion from broader datasets [7] to estimate σ; define S0_h as PV_h of expected hours saved; K_h as remediation hours; derive q to reflect decay/leakage of opportunity. Evaluate via binomial or Monte Carlo; compare to static NPV_h.
- Portfolio optimization under realistic constraints
  - Extend the MPT framing from [6,8] by:
    - Defining returns in hours saved/throughput units; risks as variance of delivery time; covariances estimated from historical co-variation (e.g., shared bottlenecks).
    - Adding constraints on headcount by skill and minimum batch sizes.
    - Incorporating nonlinear benefit curves informed by [7].
- Ex-ante/ex-post validation and sensitivity
  - For upcoming refactors, lock parameters at t0 (P_h, i_m, λ, E[S], c_s^2, σ, π, r), forecast NPV_h/IRR_h/option value/portfolio allocation, then evaluate realized outcomes ex-post (as in [5]) and conduct sensitivity/robustness analyses around key parameters.

### Paper-by-paper takeaways (what each contributes)
- FITTED and antecedents: explicit compound interest, evolving principal, and breaking point; tool-supported estimation from code metrics, with conversion via hourly rates; lacks capital budgeting, queueing, or options/portfolio [1,4,10].
- System dynamics for maintenance allocation: hours-based principal/interest and compounding via feedback; no NPV/IRR, queueing, or options; good foundation for policy simulation [2].
- Architecture-debt longitudinal study: concrete hours for refactoring and statistically significant time-based outcome improvements; ideal for reconstructing realized payback/PI and calibrating σ and CFt_h [5].
- Portfolio prioritization for normalization debt: mean–variance with covariance [6], extended to multi-attribute ranking with an industrial case [8]; needs hours-first throughput returns and operational risk calibration.
- Maintainability and value: regression-based, nonlinear returns linking code quality to implementation time and defects; informs convexity in benefit functions and options value but not framed in capital-budgeting terms [7].
- Real options in TD: early proposal in cloud service selection, without the parameter mapping/calibration details needed for your framework [9].

### Bottom line for your program
- The literature you have provides solid building blocks—compound interest/breaking points [1,4,10], hours-based dynamic modeling [2], empirical time savings after refactoring [5], portfolio machinery [6,8], and nonlinear benefit evidence [7]—but you will need to integrate them and supply the missing economic glue: hours-first capital budgeting with explicit CoD in CFt, queueing-based CFt derivation, calibrated options valuation, and ex-ante/ex-post validation with sensitivity analysis [1,2,3,4,5,6,7,8,9,10].

## Categories

### Scope-and-Criteria Comparison Against the Targeted Economic Modeling Goals

Legend: ✓ = explicitly addressed; △ = partially/indirectly addressed; ✗ = not addressed in provided material.

| Paper | Hours as unit of account (cashflows in hours, hours→$ mapping) | Capital budgeting (NPV/IRR/Payback with r from opportunity cost; CoD only in CFt) | Technical-debt compounding interest (monthly rate, amortization, ceiling) | Queueing link (service-time inflation → Kingman/CFt) | Real options (closed-form/binomial/Monte Carlo; calibrated) | Portfolio optimization (frontier; constraints; covariance) | Depreciation/value decay tied to ops metrics | Empirical measurement/validation (rates; ex-ante vs ex-post) | Sensitivity/robustness analysis |
|---|---|---|---|---|---|---|---|---|---|
| [1] FITTED (2018) | △ Converts interest to USD via developer hourly rate; principal in time per fix; not consistently hours-first for all CFt [1] | ✗ No NPV/IRR/payback/discount-rate treatment seen [1] | ✓ Continuous/compound interest; “breaking point” where cumulative interest equals principal; principal evolves with growth [1] | ✗ No queueing linkage [1] | ✗ | ✗ | ✗ | △ Industrial validation with a tool and two engineers; no ex-ante/ex-post forecast validation; no monthly % interest rates reported in provided text [1] | ✗ |
| [2] System dynamics for maintenance allocation (2016) | ✓ Principal quantified in man-hours; interest as extra maintenance hours; team capacity in hours [2] | ✗ | △ Interest modeled as ongoing extra hours; compounding via feedback loops on maintainability/productivity; no explicit monthly rate or amortization schedule [2] | ✗ | ✗ | ✗ | △ Implicit decay of maintainability/productivity over time; tied to “technical debt” stock but not calibrated to operational defect/lead-time metrics in excerpts [2] | △ Simulation calibrated from literature/secondary data; no ex-ante vs ex-post field validation [2] | ✗ |
| [3] Empirical model of TD and interest (2011) | — Not enough detail in provided text | — | — | — | — | — | — | — | — |
| [4] Breaking point estimation (2015) | — | — | △ “Breaking point” concept referenced; details not in provided text [4] | — | — | — | — | — | — |
| [5] Longitudinal architecture-debt paydown (2018) | △ Reports refactoring effort in person-hours and time-based outcomes (lead time, bug-fix duration); no hours-first CF modeling [5] | ✗ | ✗ | ✗ | ✗ | ✗ | △ Shows operational improvements (issue counts, lead time); not framed as decay parameters [5] | ✓ Before/after empirical results with statistical tests; not an ex-ante forecast validation [5] | ✗ |
| [6] Portfolio for DB normalization (2018) | ✗ No hours-first treatment; “return” mixes I/O cost and data-quality terms [6] | ✗ | △ Mentions table growth/“interest accumulation” as risk driver; not in hours/month per hour of principal [6] | ✗ | ✗ | ✓ Markowitz portfolio with covariance; weight constraints; objective on return–risk [6] | ✗ | ✗ | ✗ |
| [7] Returns of highly maintainable code (2024) | △ Models effects on defect count and implementation time; can inform hours-based value but no explicit hours-first CF model [7] | ✗ | △ Non-linear value–quality relationship suggests increasing returns; not framed as debt interest rate [7] | ✗ | ✗ | ✗ | ✗ | ✓ Empirical associations from combined datasets; not intervention validation [7] | ✗ |
| [8] Managing TD in DB normalization (2022) | △ Considers effort/cost; not systematically hours-first across CFt [8] | ✗ | ✗ | ✗ | ✗ | ✓ Portfolio + TOPSIS multi-attribute ranking; industrial case [8] | ✗ | △ Industrial case application; no ex-ante vs ex-post predictive validation [8] | ✗ |
| [9] Real options for cloud TD (2013) | — | — | — | — | △ Uses real options to manage TD in cloud service selection per title; calibration/closed-form details not provided [9] | — | — | — | — |
| [10] Financial approach to TD interest (2015) | — | — | △ “Financial approach” to TD interest; details not in provided text [10] | — | — | — | — | — | — |

Notes:
- “—” indicates insufficient information in the provided excerpts to assess.
- None of the provided papers explicitly separate CoD into CFt while deriving r from opportunity cost for NPV/IRR in an hours-first capital-budgeting framework.
- No paper connects debt-induced service-time inflation to CFt using Kingman’s formula or related queueing approximations in the provided material.


### Modeling Constructs: Principal, Interest, Compounding, and Measurement

| Aspect | [1] FITTED | [2] System dynamics | [4] Breaking point | [5] Arch-debt case | [6,8] DB normalization portfolios | [7] Maintainability returns | [9] Real options | [10] Financial approach |
|---|---|---|---|---|---|---|---|---|
| Principal definition | Source-code TD principal estimated as number of “must-fix” problems × time per fix × cost per fix; sourced from SonarQube metrics [1] | Stock “TechnicalDebt” measured as remediation man-hours [2] | Not specified (breaking point concept referenced) [4] | Refactoring workload measured as 563.8 person-hours across 106 CRs [5] | Not expressed as hours of principal; framed as tables to normalize, with effort/cost as criteria [6,8] | Not applicable (no explicit principal) [7] | Not specified [9] | Not specified [10] |
| Interest definition | Fitness-distance-based interest via maintainability metrics, mapped to USD using LoC addition rates and hourly rates; continuous/compound growth modeled; “breaking point” when cumulative interest equals principal [1] | Continuing extra maintenance hours stemming from lower maintainability/productivity; feedback-driven compounding over time [2] | “Breaking point” estimation (details not present) [4] | Not modeled as “interest”; observed reductions in time-to-close and bug-fix duration post-refactor [5] | References “interest accumulation” via table growth affecting performance risk, not in hours-per-hour terms [6,8] | Non-linear associations between code quality and implementation time/defects; can imply marginal “returns” but not labeled as interest [7] | Not specified [9] | “Financial” framing of interest (details not present) [10] |
| Compounding specification | Explicit continuous/compound modeling and evolving principal; visualized via cumulative curves; tool support [1] | Compounding via system feedback (maintainability→productivity→backlog growth); no explicit monthly rate or amortization schedule [2] | Conceptual breaking point [4] | — | Not explicit [6,8] | Implied increasing returns at high quality [7] | — | — |
| Time base and rates | References versions/LoC growth; no explicit monthly percentage interest rate reported in excerpt [1] | Time in years; parameters like “NewBusinessDemands = 0.07 1/year” [2] | — | Empirical windows of ~5 months pre/post [5] | — | Empirical intervals; not framed as rates [7] | — | — |


### Evidence and Validation Designs

- Industrial/tool validation:
  - FITTED was validated with practitioners via a Breaking Point Calculator tool; analysis involved two engineers; no ex-ante vs ex-post predictive validation is shown in the provided text [1].
  - Database-normalization prioritization with Portfolio/TOPSIS includes an industrial case, demonstrating applicability but not predictive validation or realized ROI tracking [8].

- Longitudinal empirical effects of debt paydown:
  - The architecture-debt study reports concrete effort (563.8 hours) and statistically significant improvements in time-based operational metrics (e.g., 30% reduction in average bug-fix duration; throughput increases) across comparable five-month windows [5]. This is among the strongest empirical before/after datasets in the set.

- Simulation-based analysis:
  - The system-dynamics model explores policy counterfactuals (preventive vs perfective maintenance) with stocks/flows in hours, showing long-term consequences of resource allocation; calibration relies on literature/secondary data rather than on-site measurements; no ex-post validation [2].

- Statistical associations:
  - The maintainability-returns paper provides regression-based evidence linking code quality to implementation time and defects, with non-linearities and “amplified returns” at the high-quality end; not tied to explicit TD principal/interest constructs [7].

- Option/financial framing:
  - Real options for cloud TD is only evidenced by the title/venue here; details on parameterization, calibration, or empirical backtesting are not available in the provided text [9].
  - The “financial approach” to TD interest [10] and “breaking point” [4] appear to be conceptual/methodological antecedents to FITTED [1], but the provided excerpts do not include empirical validation details.


### Portfolio and Prioritization Approaches

- Modern Portfolio Theory (MPT) for TD items:
  - Database normalization TD is treated as a portfolio of “assets,” with expected return and variance, and portfolio covariance/weight constraints to trade off performance gains and data-quality risks [6]. This matches the efficient-frontier framing structurally, but:
    - Returns are not expressed in developer hours/time-saved.
    - No headcount/skills/budget constraints in hours are modeled as resource constraints in the portfolio optimization in the provided text [6].
  - The extended framework with TOPSIS provides multi-criteria ranking incorporating maintainability, performance, data quality, and cost, validated via an industrial case [8]. Efficient-frontier visualization and risk-adjusted throughput are not reported.

- Empirical covariance:
  - [6] accounts for inter-table correlations in variance/covariance; estimation details for covariance from data (vs assumptions) are not included in the provided material.

- Contrast with other works:
  - No other paper in the set constructs a quantitative efficient frontier of features vs maintenance with return as throughput/time saved and risk as variance of delivery time/throughput under explicit resource constraints.


### Gaps Relative to the Targeted Economic Requirements

- Missing hours-first capital budgeting and CoD handling:
  - None of the papers compute NPV/IRR/payback in hours with r derived from the opportunity cost of developer time while keeping CoD explicitly in CFt [1,2,3,4,5,6,7,8,9,10].

- Queueing-theoretic linkage:
  - No work connects TD to CFt via λ, E[S], c_s^2, and Kingman’s approximation to quantify delay growth and cost-of-delay in hours [1,2,3,4,5,6,7,8,9,10].

- Real options with calibrated parameters:
  - Apart from the real-options positioning in cloud TD selection [9], there is no closed-form/binomial/Monte Carlo valuation with parameters mapped and calibrated to delivery-time or CoD volatility [1,2,3,4,5,6,7,8,9,10].

- Empirical TD “interest rates”:
  - No study reports monthly percentage interest rates (e.g., 5–15%/month) in hours-per-hour terms, with amortization schedules or debt ceiling (utilization) effects [1,2,3,4,5,6,7,8,9,10]. FITTED models compounding and breaking points but does not, in the provided excerpt, present calibrated monthly rates or amortization schedules [1].

- Ex-ante vs ex-post validation and sensitivity:
  - Ex-ante economic predictions locked at t0 and ex-post outcome comparisons, plus sensitivity/robustness analyses (elasticities, Monte Carlo), are absent in the provided materials [1,2,3,4,5,6,7,8,9,10].


### Unique Contributions and How They Can Be Leveraged

- Compounding and “breaking point” formalization:
  - FITTED’s continuous/compound interest with a breaking-point calculator and evolving principal sourced from maintainability metrics is the most explicit compound-interest treatment and tool-supported approach here [1]. It can seed calibration of compounding models if augmented with time-bucketed, hours-based data.

- Hours-based system dynamics of maintenance allocation:
  - The stock-and-flow model in [2] already uses man-hours for principal/interest and team capacity, enabling conversion to hours-first cashflows; adding explicit discounting and CoD-in-CFt would move it closer to the targeted framework.

- Strong before-after operational evidence for architecture refactoring:
  - The longitudinal study [5] provides measurable time savings and throughput changes tied to a quantified refactoring effort (hours). These outcomes can be retrofitted to compute realized payback time in hours and validate ex-ante forecasts in future studies.

- Portfolio framing with covariance for TD items:
  - The MPT-based normalization prioritization [6] and the multi-criteria extension with an industrial case [8] provide a starting point for building efficient frontiers; replacing return/risk with hours-first throughput/time-saved and delivery-time variance, and adding resource constraints by skill in hours, would align with the target portfolio model.

- Non-linear value–quality relationships:
  - The empirical non-linear returns to maintainability [7] support modeling diminishing or increasing returns in maintenance/refactoring benefit functions μ_i(x_i) within portfolio optimization and for scenario design in real-options valuation.

- Real options in TD context:
  - [9] establishes precedent for options-theoretic treatment of TD decisions; a concrete next step is parameter mapping (S0_h, K_h, σ, q) in hours, with calibration from delivery variability and CoD dispersion.


### Comparative Takeaways for Expert Discussion

- Best current alignment with “hours as currency” and compound-interest constructs: [1] and [2].
- Best empirical operational outcomes for refactoring benefits: [5].
- Best structural portfolio machinery (risk/return and covariance): [6], with broader multi-criteria industrial application in [8].
- Evidence for non-linear maintenance returns useful for modeling benefit curves and interest compounding: [7].
- Only explicit real-options angle within the set: [9], though details are not available in the provided text.

Collectively, these works cover important pieces—compounding/breaking points [1,4,10], hours-based stocks/flows [2], empirical time-based outcomes [5,7], and portfolio structuring [6,8]—but none deliver the integrated, empirically validated, hours-first capital-budgeting, queueing-linked, options- and portfolio-based economic framework specified in the search goal.

## Timeline

### Timeline and Evolution of Ideas

- 2011 — Early empirical modeling of TD “interest”:
  - Nugroho et al. present one of the earliest empirical attempts to quantify technical debt and its “interest,” catalyzing later work that treats TD as accruing costs over time [3].

- 2013 — Introduction of real options framing to TD:
  - Alzaghoul and Bahsoon propose using real options to manage TD in cloud-service selection, marking an early application of options thinking to software debt/flexibility decisions, though details on parameter calibration and hours-based mapping are not evident in the excerpt [9].

- 2015 — Financialization and “breaking point” concept:
  - Chatzigeorgiou et al. introduce the “breaking point,” where accumulated interest equals principal, making compounding effects and timing explicit and helping to motivate pre-emptive remediation decisions [4].
  - Ampatzoglou et al. propose a financial approach for managing TD interest, solidifying the vocabulary of principal/interest and bridging code metrics to economic constructs, setting up subsequent frameworks [10].

- 2016 — System-dynamics modeling of maintenance trade-offs:
  - Franco et al. model resource allocation between perfective and preventive maintenance via system dynamics, explicitly representing principal in man-hours and feedback loops from maintainability to productivity and backlog growth [2].

- 2018 — Consolidation and industrial validation; portfolio thinking enters database normalization:
  - Ampatzoglou et al. (FITTED) formalize compound interest, evolving principal, and a “breaking point” calculator, with industrial validation and a pipeline from code metrics (e.g., SonarQube) to economic quantities; they convert to currency using developer hourly rates [1].
  - Nayebi et al. provide a longitudinal empirical study quantifying the impact of paying down architecture debt on throughput, defect-related delays, and rework, offering detailed before/after metrics tied to refactoring hours [5].
  - Al-Barak and Bahsoon apply Modern Portfolio Theory to prioritize database normalization debts, defining per-item “return” and risk with covariance-aware selection, foreshadowing multi-criteria portfolio methods in debt management [6].

- 2022 — Maturation of multi-attribute debt management in databases:
  - Albarak et al. extend the portfolio framing with TOPSIS and multiple attributes (data quality, performance, maintainability, cost), and demonstrate an industrial case, maturing the practical selection toolkit for normalization debt [8].

- 2024 — Nonlinear value-creation and returns to maintainability:
  - Borg and Tornhill empirically derive a value-creation model linking code quality to defect counts and implementation time, showing strong nonlinearities and amplified returns at high quality levels, supporting strategic refactoring where it yields disproportionate payoff [7].


### Thematic Trajectories and Trends

- From qualitative metaphors to quantitative constructs (principal/interest/breaking point):
  - The field transitions from metaphorical TD discourse to explicit economic constructs, with principal defined in remediation hours and interest modeled as compounding accumulation leading to a measurable breaking point [3,4,10], consolidated and tool-supported in FITTED [1].

- Increasing empirical grounding and operational metrics:
  - Case-based, operationally rich studies quantify impacts of refactoring on throughput, defect-related delay, and churn [5]. The 2024 study extends empirical modeling, revealing nonlinear return patterns tied to code quality [7]. These datasets supply the ingredients to calibrate time-based cashflows and validate ROI claims, though explicit capital-budgeting formalisms remain rare.

- Portfolio approaches to debt selection:
  - Beginning in database normalization, the literature adopts portfolio theory (means, variances, covariances) to prioritize remediation under constraints, evolving from single-criterion to multi-attribute, practice-oriented frameworks with industrial cases [6,8]. This indicates a shift toward decision-support tools that can balance competing remediation candidates at scale.

- Options thinking for architectural/technology flexibility:
  - Real options are introduced early for cloud TD [9], signaling recognition of deferral/abandonment flexibility. However, subsequent works in the provided set focus more on portfolio/ranking than on calibrated options valuation, suggesting this line is underdeveloped in terms of parameter mapping and empirical validation.

- System feedbacks and compounding dynamics:
  - System-dynamics models capture feedback from TD to maintainability, productivity, and backlog growth, emphasizing the long-run consequences of allocation policies [2]. This complements compounding-interest and breaking-point notions, with both streams pointing to nonlinearity and thresholds.

- Measurement pipelines from code metrics to economic quantities:
  - Tool-supported extraction of principal and interest from maintainability metrics (e.g., SonarQube-derived) become prominent, including automation (Breaking Point Calculator) and structural similarity/optimal metric baselines for estimation [1,4]. This reflects a practical turn toward repeatable, model-driven measurement.


### Influential Clusters and Contributors

- Ampatzoglou–Chatzigeorgiou–Avgeriou cluster:
  - Contributions: formalization of financial constructs for TD (principal, compound interest), “breaking point,” and FITTED framework with industrial validation and tooling [1,4,10].
  - Impact: Provided the conceptual and computational underpinnings for compound-interest modeling and introduced accessible tools, shaping subsequent empirical/engineering practice.

- Bahsoon and collaborators (Al‑Barak/Albarak):
  - Contributions: early real-options application to TD in cloud service selection [9]; portfolio-theoretic prioritization for normalization debt, evolving into multi-attribute decision frameworks with industry evaluation [6,8].
  - Impact: Seeded flexibility valuation and advanced practical portfolio decision-making for specific TD domains (databases), including consideration of correlations and multi-criteria trade-offs.

- Empirical architecture-debt impact (Nayebi et al.):
  - Contributions: longitudinal, quantified impacts of architectural debt remediation on throughput and defect-related outcomes, with precise effort accounting [5].
  - Impact: Reinforced the business case for architecture-level remediation with field evidence, bridging code analysis tools (DV8/Titan) to operational outcomes.

- Maintainability–value link (Borg, Tornhill):
  - Contributions: regression-based value-creation model showing nonlinear returns to high maintainability, integrating public datasets to relate code quality to delivery time and defects [7].
  - Impact: Strengthens the argument for targeted refactoring and preventive practices in high-churn/high-importance areas, and motivates models accommodating convex payoff regions.


### Methodological Evolution

- Measurement and modeling of TD interest:
  - Early empirical models establish the feasibility of quantifying interest [3].
  - Breaking-point analyses and FITTED introduce compounding and evolving principal with tool support and maintainability metrics-to-time conversions [1,4].
  - System dynamics incorporate feedback loops among maintainability, productivity, and backlog, enabling policy simulations over long horizons [2].

- Decision analytics:
  - Portfolio models emerge for specific domains (database normalization) with risk–return trade-offs, correlations, and later multi-attribute ranking (TOPSIS) augmented by industrial evaluations [6,8].
  - Real-options framing appears for cloud TD decisions, but subsequent calibration and hours-based parameterization are not prominent in the provided set [9].

- Empirical impact studies:
  - Architecture debt remediation studies quantify refactoring hours and downstream effects on issue throughput and defect-related durations, helping translate technical choices into time-based outcomes [5].
  - Recent value-creation regressions quantify nonlinear payoff structures, guiding where refactoring may yield outsized benefits [7].


### Significance, Patterns, and What They Suggest

- Convergence on time-based quantities, but incomplete capital budgeting:
  - Several works express costs and benefits in developer effort/time and connect code metrics to remediation hours [1,2,5,6,8], yet explicit capital-budgeting analyses (NPV/IRR/PI in hours with discount rates rooted in opportunity cost) are largely absent in these references.

- Recognition of compounding and thresholds:
  - The breaking-point concept and SD feedbacks emphasize nonlinear risk growth and threshold effects [2,4], consistent with operational realities where delay and maintainability degradation accelerate beyond certain utilization/quality levels.

- Portfolio selection is gaining traction; options remain nascent:
  - Practical portfolio methods exist for targeted domains with some empirical grounding [6,8], whereas real options, introduced early [9], have not yet become a calibrated, mainstream tool in the surveyed set.

- Empirical grounding is improving:
  - Longitudinal case evidence and cross-dataset regressions increase empirical rigor and external validity [5,7]. This trend supports future calibration of economic models (e.g., volatility for options, distributions for portfolio risk).

- Toward nonlinearity-aware planning:
  - Evidence of convex payoffs at high maintainability [7] and compounding costs [1,4] suggests that models should account for nonlinear benefits and risks rather than assume linear ROI.


### Implications and Likely Future Directions

- Capital-budgeting formalization in hours:
  - Given widespread use of time/effort as the measurement basis, the field is poised to incorporate NPV/IRR/payback/profitability index in hours with explicit opportunity-cost discounting and cost-of-delay in cashflows, filling a current gap not addressed directly in these works [1,2,5,6,7,8,10].

- Calibrated real options for architectural flexibility:
  - With emerging empirical variability in delivery times and throughput [5,7], there is an opportunity to parameterize options (volatility, dividend yield/decay) for migrations/refactors using observed dispersion, extending early options work [9] to calibrated decision support.

- Portfolio optimization under realistic constraints:
  - Existing portfolio framings can evolve into organization-wide efficient-frontier planning that incorporates headcount by skill, covariance of throughput/time-saved, and diminishing returns, extending beyond domain-specific normalization cases [6,8].

- Integration with operational queuing models:
  - While compounding and backlog dynamics are modeled [1,2,4], explicit queueing-theoretic links (e.g., Kingman-based delay growth from service-time inflation) are not evident here; connecting maintainability-induced service-time changes to delivery delays would strengthen CFt estimation and prioritization.

- Empirical validation standards:
  - The move toward longitudinal and dataset-based studies [5,7] sets the stage for ex-ante vs ex-post validation of predicted ROI/option values/portfolio choices, improving credibility and generalizability across domains and team contexts.

Overall, the field has advanced from metaphor to measurement and from singular remediation choices to risk-aware portfolio prioritization, with growing empirical evidence. The next milestones will likely formalize capital budgeting in hours, calibrate real options for architecture and platform flexibility, and connect TD-induced service-time inflation to delivery delays via queueing, all validated with ex-ante predictions and ex-post outcomes.

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [380] | 0.38 | 0% | The WyCash portfolio management system | Ward Cunningham | N/A | 1992 | 991 | [1, 2, 3, 4, 5, 6, 9, 10, 11] |
| [23] | 0.36 | 5% | A systematic mapping study on technical debt and its management | Zengyang Li, ..., and Peng Liang | J. Syst. Softw. | 2015 | 627 | [1, 2, 4, 6, 10] |
| [146] | 0.35 | 1% | Prioritizing design debt investment opportunities | N. Zazworka, ..., and F. Shull | N/A | 2011 | 90 | [1, 6, 10, 13, 16] |
| [11] | 0.34 | 14% | A portfolio approach to technical debt management | Yuepu Guo and C. Seaman | N/A | 2011 | 144 | [1, 6, 9, 10] |
| [24] | 0.30 | 5% | Estimating the size, cost, and types of Technical Debt | B. Curtis, ..., and Alexandra Szynkarski | 2012 Third International Workshop on Managing Technical Debt (MTD) | 2012 | 104 | [1, 4, 16, 17, 20] |
| [70] | 0.24 | 1% | Using technical debt data in decision making: Potential decision approaches | C. Seaman, ..., and A. Vetrò | 2012 Third International Workshop on Managing Technical Debt (MTD) | 2012 | 154 | [6, 9, 10, 12, 13] |
| [3] | 0.24 | 31% | An empirical model of technical debt and interest | Ariadi Nugroho, ..., and T. Kuipers | N/A | 2011 | 170 | [2, 10, 19, 23] |
| [482] | 0.24 | 0% | A threshold based approach to technical debt | R. Eisenberg | ACM SIGSOFT Softw. Eng. Notes | 2012 | 56 | [1, 10, 13, 20, 23] |
| [227] | 0.22 | 0% | In Search of a Metric for Managing Architectural Technical Debt | R. Nord, ..., and Marco Gonzalez-Rojas | 2012 Joint Working IEEE/IFIP Conference on Software Architecture and European Conference on Software Architecture | 2012 | 167 | [5, 10, 12, 13, 23] |
| [4] | 0.21 | 27% | Estimating the breaking point for technical debt | A. Chatzigeorgiou, ..., and Theodoros Amanatidis | 2015 IEEE 7th International Workshop on Managing Technical Debt (MTD) | 2015 | 42 | [1, 10] |
| [284] | 0.20 | 0% | A Case Study in Locating the Architectural Roots of Technical Debt | R. Kazman, ..., and Andriy Shapochka | 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering | 2015 | 128 | [5, 25, 26] |
| [20] | 0.17 | 7% | The financial aspect of managing technical debt: A systematic literature review | Areti Ampatzoglou, ..., and P. Avgeriou | Inf. Softw. Technol. | 2015 | 184 | [1, 4, 10] |
| [1] | 0.16 | 43% | A Framework for Managing Interest in Technical Debt: An Industrial Validation | Areti Ampatzoglou, ..., and P. Avgeriou | 2018 IEEE/ACM International Conference on Technical Debt (TechDebt) | 2018 | 35 | [33, 34, 37, 60, 62, 84, 87, 101] |
| [10] | 0.16 | 15% | A Financial Approach for Managing Interest in Technical Debt | Areti Ampatzoglou, ..., and A. Chatzigeorgiou | N/A | 2015 | 27 | [1, 6] |
| [396] | 0.15 | 0% | Tracking technical debt — An exploratory case study | Yuepu Guo, ..., and C. Siebra | 2011 27th IEEE International Conference on Software Maintenance (ICSM) | 2011 | 100 | [1, 10, 23] |
| [39] | 0.15 | 2% | Managing Technical Debt in Enterprise Software Packages | Narayan Ramasubbu and C. Kemerer | IEEE Transactions on Software Engineering | 2014 | 39 | [1, 4] |
| [434] | 0.15 | 0% | Technical Debt: From Metaphor to Theory and Practice | Philippe B Kruchten, ..., and Ipek Ozkaya | IEEE Software | 2012 | 619 | [2, 4, 6, 23] |
| [72] | 0.14 | 1% | A systematic literature review on Technical Debt prioritization: Strategies, processes, factors, and tools | Valentina Lenarduzzi, ..., and F. Fontana | J. Syst. Softw. | 2021 | 101 | [7] |
| [458] | 0.14 | 0% | Defining the decision factors for managing defects: A technical debt perspective | W. Snipes, ..., and C. Seaman | 2012 Third International Workshop on Managing Technical Debt (MTD) | 2012 | 56 | [1, 10, 23] |
| [111] | 0.11 | 1% | Estimating the Principal of an Application's Technical Debt | B. Curtis, ..., and Alexandra Szynkarski | IEEE Software | 2012 | 112 | [2, 5, 23] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref. | Adjacency score | Topic Match | Title | Authors | Journal | Year | Total Citations | References These Foundational Papers |
|---|---|---|---|---|---|---|---|---|
| [87] | 0.38 | 1% | Quantifying Technical Debt: A Systematic Mapping Study and a Conceptual Model | Judith Perera, ..., and Kelly Blincoe | ArXiv | 2023 | 3 | [3, 11] |
| [23] | 0.18 | 5% | A systematic mapping study on technical debt and its management | Zengyang Li, ..., and Peng Liang | J. Syst. Softw. | 2015 | 627 | [3, 11, 24, 69, 146, 227, 396, 482] |
| [74] | 0.17 | 1% | Value- and debt-aware selection and composition in cloud-based service-oriented architectures using real options | Esra Alzaghoul | N/A | 2015 | 1 | [3, 11, 24, 69, 227, 284, 482] |
| [33] | 0.15 | 3% | A Systematic Mapping Study Exploring Quantification Approaches to Code, Design, and Architecture Technical Debt | Judith Perera, ..., and Kelly Blincoe | ACM Transactions on Software Engineering and Methodology | 2024 | 5 | [1, 3, 11, 24, 69, 146, 227, 284, 380, 482] |
| [138] | 0.14 | 1% | Methods and Tools for TD Estimation and Forecasting: A State-of-the-art Survey | D. Tsoukalas, ..., and D. Tzovaras | 2018 International Conference on Intelligent Systems (IS) | 2018 | 18 | [1, 3, 9, 11, 24, 69, 146, 227] |
| [283] | 0.12 | 0% | Identification and analysis of the elements required to manage technical debt by means of a systematic mapping study | Carlos Fernández-Sánchez, ..., and Jennifer Pérez | J. Syst. Softw. | 2017 | 55 | [3, 9, 11, 69, 70, 146, 227, 284] |
| [10] | 0.12 | 15% | A Financial Approach for Managing Interest in Technical Debt | Areti Ampatzoglou, ..., and A. Chatzigeorgiou | N/A | 2015 | 27 | [3, 11, 146, 227, 380, 396, 482] |
| [90] | 0.11 | 1% | Measuring the Principal of Defect Debt | S. Akbarinasaji, ..., and Atakan Erdem | 2016 IEEE/ACM 5th International Workshop on Realizing Artificial Intelligence Synergies in Software Engineering (RAISE) | 2016 | 14 | [3, 11, 24, 70, 146, 227, 482] |
| [354] | 0.11 | 0% | Design Rule Spaces: A New Model for Representing and Analyzing Software Architecture | Yuanfang Cai, ..., and Qiong Feng | IEEE Transactions on Software Engineering | 2019 | 35 | [3, 11, 24, 69, 70, 227, 284] |
| [268] | 0.10 | 0% | Technical debt management in the context of agile methods in software development | G. Tonin | N/A | 2018 | 5 | [3, 11, 24, 70, 227, 482] |
| [253] | 0.09 | 0% | Design Debt Prioritization: A Design Best Practice-Based Approach | Reinhold Plösch, ..., and Christian Körner | 2018 IEEE/ACM International Conference on Technical Debt (TechDebt) | 2018 | 14 | [3, 11, 24, 69, 146] |
| [199] | 0.09 | 0% | Modelling the Quantification of Technical Debt | Judith Perera | Companion Proceedings of the 2022 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity | 2022 | 3 | [3, 69, 70, 146, 227, 284] |
| [491] | 0.09 | 0% | The role of technical debt in software development | Jesse Yli-Huumo | N/A | 2017 | 5 | [11, 24, 70, 146, 227, 482] |
| [356] | 0.09 | 0% | Database Normalization Debt: A Debt-Aware Approach to Reason about Normalization Decisions in Database Design | Mashel Al-Barak, ..., and Rami Bahsoon | ArXiv | 2017 | 0 | [9, 11, 23, 146, 380, 423, 434] |
| [330] | 0.09 | 0% | Modelling Propagation of Technical Debt | Johannes Holvitie, ..., and Ville Leppänen | 2016 42th Euromicro Conference on Software Engineering and Advanced Applications (SEAA) | 2016 | 4 | [3, 11, 70, 146, 482] |
| [135] | 0.09 | 1% | Technical debt forecasting: An empirical study on open-source repositories | D. Tsoukalas, ..., and A. Chatzigeorgiou | J. Syst. Softw. | 2020 | 35 | [1, 3, 4, 24, 69, 146] |
| [203] | 0.08 | 0% | Identification and measurement of Requirements Technical Debt in software development: A systematic literature review | A. Melo, ..., and W. Santos | J. Syst. Softw. | 2022 | 27 | [1, 3, 11, 24, 70] |
| [84] | 0.08 | 1% | Identification and Measurement of Technical Debt Requirements in Software Development: a Systematic Literature Review | A. Melo, ..., and Will Santos | ArXiv | 2021 | 2 | [1, 3, 11, 24, 70] |
| [102] | 0.08 | 1% | On the interest of architectural technical debt: Uncovering the contagious debt phenomenon | A. Martini and J. Bosch | Journal of Software: Evolution and Process | 2017 | 37 | [3, 11, 70, 227, 284] |
| [542] | 0.08 | Not measured | Exploring the Relation between Technical Debt Principal and Interest: An Empirical Approach | Areti Ampatzoglou, ..., and L. Angelis | Inf. Softw. Technol. | 2020 | 14 | [1, 3, 4, 69, 284, 482] |