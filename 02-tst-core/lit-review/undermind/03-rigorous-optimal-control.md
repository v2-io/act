# Rigorous optimal control formulations for software maintenance and refactoring: HJB, PMP, DP

## Overview

Directly relevant, fully rigorous optimal-control formulations for software-internal maintenance/refactoring with discounted infinite-horizon HJB/PMP and calibrated software-metric state dynamics were not found in this set; the closest rigorous results are in adjacent security-maintenance models with threshold/full-effort structure [5] and discounted patching optimization [9,10], while software enhancement/market-share models employ continuous-time control without the technical-debt state focus or formal HJB/PMP treatment in the provided materials [1,3,6,8].

### What matches the goal, and how closely

- Closest methodological match (adjacent domain: IT security maintenance)
  - Piecewise-deterministic deterioration with shocks and maintenance effort leading to a proven steady-state target and “full effort below target” policy; strong structural characterization akin to bang-bang/threshold control [5].
  - Discounted-cost patching models with ODE dynamics and explicit ∫ e^{−δt} cost, focusing on optimal patching frequencies; solved numerically without explicit HJB/PMP in the excerpt [9,10].

- Somewhat related software “enhancement/maintenance” control (not code-internal technical debt)
  - Early and lifecycle work framing enhancement effort as a control over software value/quality states; details in the excerpts do not show HJB/PMP derivations, budget-state modeling, or discounted infinite-horizon structure [1,2,3,4,7].
  - Digital product maintenance where “quality effort” controls market share via diffusion dynamics; analytical characterizations of optimal effort paths, but no technical-debt/complexity ODEs, discounted infinite horizon, or HJB/PMP statements in the excerpts [6,8].

- Not observed in this set
  - Explicit HJB equations or viscosity-solution results for technical-debt/complexity states driven by refactoring effort u(t), nor PMP with costate/switching functions for such models [1,2,3,4,5,6,7,8,9,10].
  - Repository-calibrated ODE/SDE models of code-level metrics with computed, validated optimal refactoring policies [1,2,3,4,5,6,7,8,9,10].

### Evidence on analytic machinery (HJB, PMP, DP)

- HJB and viscosity
  - No paper in this set explicitly states the stationary discounted HJB ρV(x) = min_u{L + ∇V·f} for software-internal metrics, nor viscosity arguments for existence/uniqueness, in the provided text [1,2,3,4,5,6,7,8,9,10].
  - Security patching work uses discounted integrals but reports simulation-based policy computation rather than HJB solution methods [9,10].

- PMP and costate dynamics
  - The IDS maintenance paper provides a structural “full-effort-until-steady-state” result strongly suggestive of PMP with an affine-in-control Hamiltonian and a switching function, but the excerpt does not present explicit costate equations or transversality conditions [5].
  - Enhancement/market models show analytic controls but do not display PMP systems or costate evolution in the excerpts [6,8].

- Discrete-time Bellman/DP
  - No explicit sprint/release Bellman recursions with resource states appear in the excerpts; patching work compares policy classes rather than solving DP recursions [9,10].

### Concrete structural insights that may transfer

- Threshold/full effort regimes
  - Below a target “discrimination ability,” optimal policy is to exert full maintenance effort until the steady-state is reached, then maintain it—an archetypal threshold/bang-bang structure [5]. This supports expecting similar structure when L is affine in u and f is monotone in software-quality states.

- Life-cycle decline in quality effort
  - In market-share-coupled models, optimal quality effort declines over the product’s life cycle, echoing empirical intuition; while external to internal code metrics, it highlights turnpike-like behavior in lifecycle settings [6].

- Discounted objective relevance
  - Discounting is explicit in patching [9], aligning with the desired infinite-horizon discounted cost framing and suggesting feasibility of stationary HJB formulations in IT operations problems.

### Gaps relative to the target formulation

- Missing elements in surveyed software-maintenance literature
  - Software-internal ODE state models x(t) built from measurable technical debt/complexity/defect metrics, with bounded refactoring control and:
    - Stationary discounted HJB and viscosity results [not found in 1-10].
    - PMP with explicit costate dynamics and switching functions, budget constraints as isoperimetric constraints or budget state ḃ = −u, and analysis of bang-bang/singular arcs [not shown in 1-10].
    - Discrete-time Bellman recursions for sprint/release decisions with resource states [not shown in 1-10].
  - Empirical calibration from repositories (commits, complexity, CI/test duration, defect logs) and validation against developer heuristics (e.g., fixed-percent refactoring) [not reported in 1-10].

### What each cluster contributes

- Security maintenance/patching
  - Rigorous structural policy with shocks and drift (steady-state target; full effort below) [5].
  - Discounted-cost optimization and policy comparisons under ODE dynamics; calibrated parameter vectors from practitioner input, albeit solved via simulation [9,10].

- Enhancement/market/customer models
  - Lifecycle optimal control framing with analytical effort trajectories; connects to product diffusion and profit, not to internal technical debt ODEs [6,8].
  - Early lifecycle/maintenance timing and policy-comparison foundations signaling benefits of flexible, state-dependent policies [1,2,3,4,7].

### Implications and recommendations for advancing the target agenda

- Leverage adjacent rigor to design the software-internal model
  - Adopt the discounted stationary HJB frame used implicitly in [9] and the threshold structures shown in [5]; specify x(t) as low-dimensional, measurable code metrics (e.g., technical-debt stock, complexity, test coverage, defect backlog) with Lipschitz dynamics and control bounds.

- Pursue PMP-based structure and budgets explicitly
  - Formulate H(x,u,λ) = L + λ·f with either an isoperimetric budget ∫ u ≤ B (constant multiplier in H) or a budget state ḃ = −u; derive switching conditions and assess bang-bang vs singular arcs, following the structure observed in [5].

- Provide discrete DP versions for sprint planning
  - Develop V(x,b) recursions with discount β = e^{−ρΔt} and effort/resource constraints, enabling mixed discrete/continuous decisions absent in [1,2,3,4,5,6,7,8,9,10].

- Emphasize empirical calibration and validation
  - Calibrate f and L to repository histories and compare computed policies against baseline heuristics (fixed-percent refactoring, debt thresholds), a gap across all surveyed works [1,2,3,4,5,6,7,8,9,10].

### Bottom line

- The surveyed literature confirms that rigorous optimal-control thinking is established around software operations (especially security maintenance with clear threshold policies [5] and discounted patching [9,10]) and around enhancement/market dynamics [6,8], but it does not yet deliver the desired HJB/PMP-grounded, discounted infinite-horizon control of software-internal technical-debt/complexity with empirical validation. This leaves a clear, tractable opening for a mathematically rigorous, metric-calibrated refactoring control framework, drawing structure from [5] and discounted formulations from [9,10], while grounding states and objectives in code-level metrics.

## Categories

### Scope and alignment overview

- Overall, among the retrieved papers, rigorously formulated optimal control models exist in adjacent software operations contexts (security degradation/patching) and in revenue/market-share models for digital products, but there is little direct evidence in these sources of mathematically rigorous optimal control for software-internal quality/technical-debt states with infinite-horizon discounted HJB/PMP analyses as specified in the search goal.
- Most concretely aligned with the desired structure are:
  - A continuous-time optimal maintenance model with both drift and jump deterioration in information security discrimination ability, which proves a steady-state target and prescribes full effort when below that level, i.e., threshold/bang-bang-type prescriptions; the paper presents analytical structure and comparative analyses [5].
  - Discounted-cost patch management models with ODE dynamics and policy optimization over patching frequency decisions, though these are solved numerically without explicit HJB/PMP derivations in the provided excerpts [9,10].
- Software enhancement/maintenance models from the Sethi/Ji line likely use optimal control tools (titles and cross-citations suggest this), but the provided records lack abstracts and methodological details; therefore, only cautious, minimal comparisons are made for [1,2,3,4].
- Digital product maintenance/enhancement models optimize quality effort to influence market share and profit with continuous-time dynamics and analytical characterizations, but they do not present the technical-debt/complexity state-space, HJB/PMP with viscosity verification, or repository-calibrated validations required by the stated goal in the excerpts provided [6,8].

### Comparative table: Core formulation and analytic machinery

| Aspect | [1] | [2] | [3] | [4] | [5] | [6] | [8] | [9] | [10] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Domain focus | software enhancement/lifetime (title) | sizing/timing of maintenance projects (title) | optimal software development (title) | enhancement effort (title) | IDS maintenance/security degradation | digital product quality/market share | software enhancement and customer growth | security patch management trade-offs | optimal policies for patch management |
| State x(t) type | not specified in excerpt | not specified in excerpt | not specified in excerpt | not specified in excerpt | discrimination ability with drift + shocks (explicit) | market share dynamics (“rumor-spreading”) | feature/customer growth states | confidentiality/availability dynamics | patching policy impacts on security states |
| Control u(t) | enhancement/maintenance effort (title-implied) | maintenance project sizing/timing (title-implied) | development/enhancement effort (title-implied) | enhancement effort (title) | maintenance effort on IDS (explicit) | effort devoted to software quality (explicit) | enhancement control (explicit) | patching frequency/policy (explicit) | patching policy (explicit) |
| Deterministic ODE base | unclear | unclear | unclear | unclear | yes (with compound Poisson shocks; piecewise-deterministic) | yes (deterministic ODEs for market share) | yes (deterministic ODEs for growth) | yes (ODEs for C/A); stochastic environment | yes (builds on [9]) |
| Stochastic variant | not stated | not stated | not stated | not stated | yes (abrupt shocks; random arrivals/sizes) | not stated | not stated | yes (stochastic threat; simulation) | likely, per [9] |
| Objective | not stated | not stated | not stated | not stated | minimize long-run cost; steady-state target stated | maximize profit/revenue stream | maximize total profit over lifetime | discounted cost integral explicitly stated | computational policies for patching |
| Infinite-horizon discounted form | not stated | not stated | not stated | not stated | steady-state analysis; discounting not explicit in excerpt | not stated as discounted; life-cycle focus | lifetime period; not stated discounted | yes: ∫ e^{-δt}… dt | unclear from excerpt |
| HJB derived | not stated | not stated | not stated | not stated | structural optimal policy characterized; HJB not explicitly quoted | no HJB quoted | no HJB quoted | not presented in excerpt | not presented in excerpt |
| PMP/costate analysis | not stated | not stated | not stated | not stated | switching/full-effort characterization; costate not quoted | analytical characterizations; PMP not claimed in excerpt | closed-form optimal control; PMP basis suggested but not stated | none in excerpt | none in excerpt |
| Discrete-time Bellman/DP | no info | no info | no info | no info | no | no | no | no (simulation-based) | no (computational study) |
| Budget constraint ∫u ≤ B or ḃ = −u | not stated | not stated | not stated | not stated | not stated | not stated | cost/expenditure terms; no hard budget in excerpt | budget penalty term (soft) | not stated |
| Structural policy result | not available | not available | not available | not available | steady-state target; full effort below target (threshold/bang-bang-like) | optimal quality focus declines over product life cycle | closed-form optimal enhancement policy over lifetime | optimal patching frequency regimes via simulation | policies for patching (details not provided) |

Notes:
- The steady-state target with “full effort must be exerted to reach it” in [5] indicates a threshold structure characteristic of affine-in-control Hamiltonians and bang-bang behavior; the excerpt does not provide explicit HJB/PMP equations, so we report only the stated structural result [5].
- The discounted integral objective is explicitly stated in [9]; however, the solution is simulation-based, and HJB/PMP derivations are not reported in the excerpt [9].
- [6] and [8] give continuous-time optimal control formulations tied to market/customer dynamics and provide analytical characterizations/closed forms, but there is no evidence in the excerpts of HJB/PMP derivations with software-internal technical-debt states [6,8].

### Comparative table: Validation, calibration, and mapping to software-internal metrics

| Aspect | [1] | [2] | [3] | [4] | [5] | [6] | [8] | [9] | [10] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mapping of state to software-internal quality/technical-debt metrics | not available | not available | not available | not available | maps to IDS discrimination ability (security operational metric) | maps to market share (external metric); quality effort as lever | customer/feature growth; not code-level metrics | confidentiality/availability; security operational metrics | security patching; operational security |
| Calibration from repositories (commits, defects, CI, complexity) | not stated | not stated | not stated | not stated | parameter estimation error assessed; not repository-specific in excerpt | not stated | sensitivity analysis; no repository calibration stated | parameters from practitioner interactions; not repository logs in excerpt | not stated |
| Comparison to heuristic practices (e.g., fixed-percent refactoring) | not stated | not stated | not stated | not stated | compares model to alternative settings; shows full vs partial effort implications | shows declining optimal quality effort vs life cycle, akin to known heuristics | sensitivity insights; heuristic comparisons not stated | compares regular vs irregular patching frequencies | evaluates patching policies |
| Numerical method | not stated | not stated | not stated | not stated | analytical steady-state; policy characterization; comparative statics | analytical characterizations; numerical illustrations | closed-form solution + numerical example | simulation-based search over policies | computational experiments |
| Tool/implementation producing optimal policies | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated |

### Synthesis of top findings most relevant to the target goal

- Threshold/full-effort maintenance to reach and maintain a steady-state quality level:
  - For IDS discrimination ability subject to both continuous degradation and abrupt shocks, there exists a steady-state target; when the system is below it, the prescribed optimal action is full maintenance effort until the target is reached [5]. This yields a clear threshold-bang-bang structure in a software-operations context.
- Discounted-cost optimal patch management under dynamic security trade-offs:
  - A discounted integral objective is explicitly optimized over patching strategies with ODE dynamics for confidentiality/availability; optimal patching frequencies are computed numerically for different organizational contexts, though without HJB/PMP derivations in the excerpt [9], with [10] extending policy computation.
- Optimal quality effort trajectories in digital products:
  - When quality effort influences market share via a spreading-dynamics model, analytical results show that optimal quality focus declines over the product life cycle; numerical examples illustrate trajectories under different market conditions [6].
  - A related enhancement-and-customer growth model provides closed-form optimal controls over a product lifetime with sensitivity analyses, though not tied to internal technical-debt metrics in the excerpt [8].

### Gaps relative to the desired formulations

- Missing HJB/PMP derivations for software-internal quality/technical-debt ODEs:
  - None of the excerpts provide explicit HJB equations, viscosity-solution results, or PMP costate dynamics for models where x(t) are measurable code quality/technical-debt/complexity metrics and u(t) is refactoring effort with budget constraints [1,2,3,4,5,6,7,8,9,10]. The strongest structural result (threshold/full effort) appears in security maintenance [5].
- Discounted infinite-horizon with stationary HJB in software-internal metrics:
  - Apart from the discounted objective in patching [9], an infinite-horizon, discounted, stationary HJB formulation tied to software-internal metrics is not evidenced in the provided summaries.
- Empirical calibration from repositories and validation against developer heuristics:
  - No paper in the set reports repository-history calibration of technical-debt/complexity dynamics or explicit comparisons of computed optimal refactoring policies to common heuristics (e.g., fixed-percent refactoring) in the provided excerpts [1,2,3,4,5,6,7,8,9,10].

### What each paper uniquely adds within this set

- [5] Introduces a maintenance model with both continuous degradation and abrupt shocks in an operational software-security context and proves a steady-state target with a full-effort policy below it, giving a clear structural policy prescription.
- [9] Puts forward a discounted-cost integral for patching with ODE state evolution and computes optimal patching frequencies under different environments, explicitly acknowledging stochastic shocks and path dependence.
- [6] Connects optimal control of “quality effort” to market-share dynamics, showing analytically declining optimal quality focus over a product’s life cycle, linking to observed product evolution patterns.
- [8] Provides closed-form optimal enhancement policies in a joint feature/customer growth model over a lifetime horizon, offering analytical tractability.
- [1,2,3,4] Signal a research stream on optimal enhancement/maintenance in software via control-theoretic analysis; however, specific mathematical structures (HJB/PMP, constraints, validation) are not extractable from the provided information.

Where to go next:
- To meet the precise goal, seek works that explicitly model technical debt/complexity/backlog as ODE/SDE states with refactoring effort as the bounded control, derive stationary HJB or PMP with costate dynamics (and possibly show threshold/bang-bang rules), and calibrate on repository metrics. The security maintenance and digital product models provide methodological stepping stones but fall short of the required software-internal state focus in the available excerpts [5,6,8,9,10].

## Timeline

### Timeline of Ideas and Milestones

- 2004–2007: Control-theoretic foundations for software enhancement and maintenance
  - Ji and Sethi initiate a program on optimal control for software development/enhancement, modeling effort as a control and software quality/feature-level as state variables, and deriving analytic characterizations of effort trajectories [3]. Follow-on work applies dynamic optimization to enhancement effort decisions [4].
  - In parallel, Tan and Mookerjee compare uniform versus flexible maintenance/replacement policies, indicating the benefit of adaptive (state-dependent) policies over fixed allocations in software contexts [7].
  - Feng and Sethi analyze sizing and timing of maintenance projects, connecting project-level timing/sizing to dynamic optimization formulations (bridge between static planning and continuous control) [2].
- 2010: Lifecycle perspective and optimal enhancement vs. lifetime trade-offs
  - Ji et al. formalize optimal enhancement and lifetime of software systems in a production/operations context, consolidating the control-theoretic treatment into lifecycle decision-making and citing the early thread [1]. This marks a maturation from single-policy comparisons toward lifecycle-optimal trajectories.
- 2012–2015: Security maintenance and patching policies with discounted costs
  - Ioannidis et al. formulate discounted-cost patching policy optimization with ODEs for security attributes, focusing on path-dependent dynamics and numerically computing policies; this brings explicit discounting into cyber/IT maintenance but largely via simulation rather than HJB/PMP [9].
  - Dey et al. extend patch management optimization, building on [9] and operationalizing managerial policy analyses for different environments [10].
- 2014: Market-coupled software maintenance as optimal quality effort
  - Fan and Griffin pose a single-vendor maintenance/quality-effort control linked to market share via rumor-spreading dynamics, showing analytical decline of optimal quality focus over a life cycle; the objective blends profits with effort costs and uses optimal control techniques, though not centered on technical-debt states or HJB/PMP derivations in the provided excerpts [6].
- 2020: Rigorous stochastic control for security maintenance with shocks
  - Bensoussan et al. study IDS maintenance with continuous degradation and jump shocks, proving existence of a steady-state target and characterizing a full-effort policy until reaching steady state—indicative of bang-bang/threshold structure under a stochastic control framework. This represents a clear step toward mathematically rigorous (possibly viscosity/PMP-inspired) results in IT maintenance [5].
- 2023: Revival of enhancement/customer growth models in optimal control
  - Pradhan et al. formulate feature growth and customer adoption as a coupled control problem to maximize lifetime profit, reporting closed-form solutions and theoretical characterizations, continuing the enhancement/customer-growth branch rather than technical-debt control per se [8].


### Methodological Evolution and Trends

- From deterministic dynamic optimization to lifecycle models
  - Early work emphasized deterministic ODE models with effort as control and quality/enhancement as states, providing analytic characterizations of effort paths over a product’s life [3,4,7]. The 2010 lifecycle analysis consolidated these ideas in an operations setting [1].
- Discounting and infinite-horizon framing appear mainly in security
  - Explicit discounted integral objectives appear prominently in patching/security maintenance [9,10] and in IDS maintenance with drift and shocks [5]. In contrast, enhancement/customer-growth models typically frame finite lifecycles or profit horizons [1,6,8].
- Increasing rigor in stochastic control for IT security
  - The security thread progressed from simulation-based policy search with discounted costs [9,10] to structural results (steady state, full-effort regions) under stochastic degradation and shocks [5], suggesting use of HJB/PMP-style arguments even if not fully detailed in the excerpts.
- Limited explicit HJB/PMP derivations in software maintenance/refactoring
  - Within the software enhancement/maintenance literature surveyed, explicit HJB equations, viscosity-solution results, and PMP costate dynamics with switching functions are largely absent or not visible in the provided summaries, with the strongest structural control-theory results emerging in the IDS maintenance paper [5].
- Shift from code-centric “maintenance” to market/security externalities
  - Several models emphasize market share and customer adoption (quality as a lever) rather than technical debt dynamics [6,8], and others emphasize security posture and patching [5,9,10], indicating a field tilt toward external performance and risk metrics over internal codebase debt/complexity ODEs.


### Clusters of Contributors and Their Impact

- Sethi/Ji/Kumar cluster on enhancement and lifecycle optimization
  - Core contributions: introduced and developed optimal control formulations for software enhancement and lifecycle decisions, demonstrating how dynamic effort policies outperform static heuristics and connecting to operations/IS decision contexts [1,3,4]. This line influenced subsequent lifecycle framing and is cited by later work [1,5,6,8].
  - Significance: established that software effort allocation can be fruitfully posed as an optimal control/lifecycle problem, paving the way for more formal analyses.
- Security maintenance/patching cluster
  - Ioannidis and Williams (and later Dey and Zhang) built discounted-cost, ODE-based patching optimization frameworks—policy-comparison and calibration oriented, yet primarily numerically solved [9,10].
  - Bensoussan et al. advanced the theory with stochastic degradation and jump shocks, proving steady-state targets and full-effort regimes [5], a methodological high-water mark in rigor within the surveyed set.
- Market/quality-effort cluster
  - Fan and Griffin connected maintenance/quality effort to diffusion/market share through optimal control, deriving analytic life-cycle patterns [6]. Pradhan et al. expanded enhancement/customer growth models with closed-form optimal controls [8].
  - Significance: shows receptivity to modeling software maintenance as a control on value creation (market/customer) rather than purely cost/quality internals.


### Patterns, Gaps, and Their Significance

- What matured
  - Lifecycle thinking and dynamic optimization for software effort allocation are well-established in the enhancement and market/security contexts [1,3,5,6,8,9,10].
  - Discounted objectives and steady-state/policy structure (threshold/full-effort regions) are clearly articulated in the security domain [5,9,10].
- What remains scarce relative to the target goal
  - Explicit technical-debt/complexity state variables with ODE dynamics, bounded refactoring controls u(t) with budget constraints, and rigorous derivation of HJB equations or PMP costate/switching characterizations with verification/viscosity results are not prevalent in the software-maintenance/refactoring sense in this set. The strongest structural control results are in IDS maintenance [5], not code refactoring.
  - Empirical calibration to repository metrics and tool implementations computing optimal refactoring policies are not reported in these papers; parameterization typically leverages managerial inputs or generic diffusion/security parameters [6,9,10].
- Methodological drift
  - Many studies use dynamic optimization flavor but stop short of full HJB/PMP analysis or viscosity-solution theory; several lean on numerical simulation and sensitivity analysis rather than closed-loop policy synthesis [9,10].
  - Where Hamiltonian/PMP structure likely applies (e.g., [5]), results emphasize qualitative policy structure (steady-state targets, full-effort when below) rather than comprehensive characterization under budget paths and state constraints.


### Implications for Future Work Aligned to the Goal

- Translate the rigor from security maintenance [5] to software refactoring
  - Model technical debt/complexity/defects as a low-dimensional ODE state with bounded refactoring effort and either discounted infinite horizon or sprint-level DP; derive HJB ρV = min_u{L + ∇V·f} and PMP with switching functions to obtain threshold/bang-bang structures analogous to “full effort until steady state” [5].
- Incorporate explicit budget constraints
  - Use isoperimetric constraints with Lagrange multipliers or augment with a budget state ḃ = −u and analyze via PMP/HJB; this remains underdeveloped in the surveyed software-maintenance literature.
- Provide empirical grounding from repositories
  - Calibrate f and L using commit histories, complexity metrics, build/test times, and defect logs, aiming for identifiability via observed refactoring bursts and throughput variation—this would fill a notable gap not addressed in [1,2,3,4,5,6,7,8,9,10].
- Bridge to discrete DP for sprint/release decisions
  - For mixed discrete-continuous maintenance choices, formalize Bellman recursions with resource states, moving beyond heuristic scheduling toward verifiable optimal policies—an angle mostly untouched in the current set.


### Summary Assessment of the Field’s Trajectory

- Early 2000s work established that software enhancement and maintenance can be fruitfully modeled as optimal control problems with dynamic effort allocation [3,4,7], culminating in lifecycle formulations [1].
- The last decade broadened to security and market-coupled models, adding discounting and, in security, more rigorous stochastic control with structural policies [5,6,9,10].
- Relative to the stated goal—rigorous optimal control of refactoring/technical debt with HJB/PMP and budget constraints—the literature here provides conceptual scaffolding and adjacent rigor (notably [5]) but leaves a clear opportunity for a mathematically grounded, empirically calibrated, software-metric-based control framework.

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [7] | 0.66 | 20% | Comparing uniform and flexible policies for software maintenance and replacement | Yong Tan and V. Mookerjee | IEEE Transactions on Software Engineering | 2005 | 56 | [1, 2, 5] |
| [2] | 0.55 | 91% | Optimal policies for the sizing and timing of software maintenance projects | Q. Feng, ..., and S. Sethi | Eur. J. Oper. Res. | 2006 | 20 | [1, 5, 16] |
| [16] | 0.53 | 7% | Optimal Allocation of Effort to Software Maintenance: A Queuing Theory Approach | V. Kulkarni, ..., and S. Sethi | Production and Operations Management | 2008 | 29 | [1, 2, 5] |
| [139] | 0.48 | 0% | A Field Study of Scale Economies in Software Maintenance | R. Banker and S. Slaughter | Management Science | 1997 | 192 | [1, 2, 7] |
| [263] | 0.47 | 0% | An Economic Model to Estimate Software Rewriting and Replacement Times | Taizan Chan, ..., and Teck-Hua Ho | IEEE Trans. Software Eng. | 1996 | 65 | [1, 2, 7] |
| [32] | 0.46 | 3% | A Dynamic Coordination Policy for Software System Construction | V. Mookerjee and I. R. Chiang | IEEE Trans. Software Eng. | 2002 | 41 | [1, 3, 8] |
| [448] | 0.46 | 0% | Pricing Software Upgrades: The Role of Product Improvement and User Costs | R. Bala and Scott Carr | Production and Operations Management | 2009 | 75 | [1] |
| [63] | 0.46 | 1% | A Fault Threshold Policy to Manage Software Development Projects | I. Robert Chiang and V. Mookerjee | Inf. Syst. Res. | 2004 | 33 | [1, 3, 11] |
| [3] | 0.45 | 85% | Optimal Software Development: A Control Theoretic Approach | Yonghua Ji, ..., and S. Sethi | N/A | 2004 | 46 | [1, 4, 5, 6, 8] |
| [343] | 0.45 | 0% | Optimal Control Theory: Applications to Management Science and Economics | S. Sethi and G. Thompson | N/A | 2000 | 828 | [1, 3, 4] |
| [83] | 0.44 | 1% | Optimal Release Times for Software Systems with Scheduled Delivery Time Based on the HGDM | R. Hou, ..., and Yi-Ping Chang | IEEE Trans. Computers | 1997 | 45 | [1, 3, 4] |
| [212] | 0.44 | 0% | Optimal software release scheduling based on artificial neural networks | T. Dohi, ..., and S. Osaki | Annals of Software Engineering | 1999 | 70 | [1, 3, 11] |
| [404] | 0.44 | 0% | A Comparison of Pair Versus Solo Programming Under Different Objectives: An Analytical Approach | Milind Dawande, ..., and V. Mookerjee | Inf. Syst. Res. | 2008 | 40 | [1] |
| [1] | 0.43 | 92% | Optimal Enhancement and Lifetime of Software Systems: A Control Theoretic Analysis | Yonghua Ji, ..., and Denny Yeh | Production and Operations Management | 2010 | 35 | [5, 6, 8, 16, 19] |
| [234] | 0.43 | 0% | The Machine Maintenance and Sale Age Model of Kamien and Schwartz Revisited | A. Bensoussan and S. Sethi | Manag. Sci. | 2007 | 25 | [1] |
| [410] | 0.31 | 0% | Economic and Policy Implications of Restricted Patch Distribution | Karthik N. Kannan, ..., and Mohit Tawarmalani | Manag. Sci. | 2016 | 29 | [5] |
| [381] | 0.27 | 0% | Software complexity and maintenance costs | R. Banker, ..., and Dani Zweig | Commun. ACM | 1993 | 384 | [1, 7, 8] |
| [113] | 0.26 | 0% | Software Development Practices, Software Complexity, and Software Maintenance Performance: a Field Study | R. Banker, ..., and S. Slaughter | Management Science | 1998 | 304 | [2, 7, 16] |
| [369] | 0.25 | 0% | Value creation and capture: a model of the software development process | Todd A. Little | IEEE Software | 2004 | 36 | [1, 8] |
| [171] | 0.25 | 0% | The State of Software Maintenance | N. Schneidewind | IEEE Transactions on Software Engineering | 1987 | 253 | [2, 7, 16] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref.  | Adjacency score | Topic Match | Title                                                                                                                   | Authors                                          | Journal                                                                 | Year | Total Citations | References These Foundational Papers |
| ----- | --------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------- | ---- | --------------- | ------------------------------------ |
| [16]  | 1.64            | 7%          | Optimal Allocation of Effort to Software Maintenance: A Queuing Theory Approach                                         | V. Kulkarni, ..., and S. Sethi                   | Production and Operations Management                                    | 2008 | 29              | [1, 2, 3, 7, 113, 139, 263]          |
| [377] | 1.20            | 0%          | Research in Operations Management and Information Systems Interface                                                     | Subodha Kumar, ..., and A. Shubham               | Production and Operations Management                                    | 2018 | 142             | [1, 2, 3, 16]                        |
| [5]   | 0.92            | 29%         | Managing Information System Security Under Continuous and Abrupt Deterioration                                          | A. Bensoussan, ..., and W. Yue                   | Production and Operations Management                                    | 2020 | 13              | [1, 2, 3, 7]                         |
| [42]  | 0.91            | 2%          | Managing the security of information systems with partially observable vulnerability                                    | Radha V. Mookerjee and J. Samuel                 | Production and Operations Management                                    | 2023 | 9               | [1, 2, 16]                           |
| [394] | 0.79            | 0%          | Determinants of Software Vulnerability Disclosure Timing                                                                | Ravi Sen, ..., and Subodha Kumar                 | Production and Operations Management                                    | 2019 | 19              | [1, 3, 16]                           |
| [421] | 0.78            | 0%          | A Hierarchical Framework for Organizing a Software Development Process                                                  | Foad Iravani, ..., and R. Ahmadi                 | IO: Empirical Studies of Firms & Markets eJournal                       | 2011 | 1               | [2, 3, 16]                           |
| [529] | 0.73            | 0%          | Product Design Enhancement for Fashion Retailing                                                                        | Yiwei Wang, ..., and Shuya Yin                   | ERN: Statistical Decision Theory; Operations Research (Topic)           | 2019 | 5               | [1, 3]                               |
| [475] | 0.73            | 0%          | Design of Consumer Review Systems and Product Pricing                                                                   | Yabing Jiang and Hong Guo                        | 2013 46th Hawaii International Conference on System Sciences            | 2013 | 82              | [1, 3]                               |
| [459] | 0.73            | 0%          | A Control-theoretic Approach to Realize Self-adaptive Software Systems with Guarantees                                  | S. Shevtsov                                      | N/A                                                                     | 2019 | 0               | [1, 3]                               |
| [434] | 0.73            | 0%          | A Control-based Approach for Self-adaptive Software Systems with Formal Guarantees                                      | S. Shevtsov                                      | N/A                                                                     | 2017 | 0               | [1, 3]                               |
| [371] | 0.73            | 0%          | Title The Influence of Software Process Maturity and Customer Error Reporting on Software Release and Pricing Permalink | T. August and M. F. Niculescu                    | Journal Not Provided                                                    | 2016 | 0               | [1, 3]                               |
| [348] | 0.73            | 0%          | The Influence of Software Process Maturity and Customer Error Reporting on Software Release and Pricing                 | T. August and M. F. Niculescu                    | Manag. Sci.                                                             | 2013 | 25              | [1, 3]                               |
| [209] | 0.73            | 0%          | Optimal Coordination in Distributed Software Development                                                                | Hao Xia, ..., and V. Mookerjee                   | Production and Operations Management                                    | 2016 | 16              | [1, 3]                               |
| [78]  | 0.72            | 1%          | Control-Theoretical Software Adaptation: A Systematic Literature Review                                                 | S. Shevtsov, ..., and M. Maggio                  | IEEE Transactions on Software Engineering                               | 2017 | 78              | [1, 3]                               |
| [8]   | 0.69            | 19%         | An optimal software enhancement and customer growth model: a control-theoretic approach                                 | S. K. Pradhan, ..., and Vijay Kumar              | International Journal of Quality &amp; Reliability Management           | 2023 | 1               | [1, 3]                               |
| [19]  | 0.69            | 6%          | Optimal Control Model of Software Quality for Digital Vendors                                                           | James Fan and Christopher Griffin                | arXiv: General Finance                                                  | 2014 | 0               | [1, 3]                               |
| [300] | 0.65            | 0%          | Technical Debt and the Reliability of Enterprise Software Systems: A Competing Risks Analysis                           | Narayan Ramasubbu and C. Kemerer                 | Information Systems & Economics eJournal                                | 2015 | 47              | [1, 113, 139]                        |
| [274] | 0.64            | 0%          | On the Benefits of Planning and Grouping Software Maintenance Requests                                                  | Gladston Aparecido Junio, ..., and M. T. Valente | 2011 15th European Conference on Software Maintenance and Reengineering | 2011 | 30              | [2, 7, 139]                          |
| [215] | 0.64            | 0%          | A quantitative approach for evaluating software maintenance services                                                    | H. T. Marques-Neto, ..., and M. T. Valente       | N/A                                                                     | 2013 | 10              | [2, 7, 139]                          |
| [58]  | 0.58            | 1%          | The Impact of Release Management on Open-Source Software Co-Creation                                                    | Wei Chen, ..., and Kevin Zhu                     | Sources of Innovation eJournal                                          | 2018 | 0               | [3, 113, 139]                        |