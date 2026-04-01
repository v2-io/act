# Foundational works framing software engineering as development-time optimization

## Overview

The search found a coherent line from early theory to post-LLM practice that explicitly treats software engineering as minimizing development time: foundational limits on compressing the specification–implementation gap [1,2,3], strong empirical evidence that comprehension/navigation dominates and expands nonlinearly with scattering/indirection [6,7,8,9,10,11,12,14], temporal models where past change predicts future change (aging/hazard) [13,15,16,17,24,25], and recent industry studies linking code quality directly to elapsed implementation time with non-linear returns that motivate refactoring ROI, now automated/validated in LLM-era tooling [4,5,23].

### What is earliest and most directly relevant across the seven prioritized lenses

- Information/specification-time lower bounds and the spec–implementation gap
  - Brooks’ essential vs accidental effort identifies irreducible conceptual/specification work that bounds time even if tools eliminate implementation overhead [1].
  - Veldhuizen models libraries/DSLs as compressors of program descriptions; domain entropy H bounds achievable reuse/compression (reuse ≤ 1 − H), and MDL formalizes optimal abstraction generality and its cognitive cost—establishing theoretical ceilings on time savings from abstraction/generation [2,3].
  - Post-LLM: ACE explicitly treats LLMs as implementation compressors that require objective improvement criteria and behavior-preserving validation—consistent with the view that verification/comprehension become bottlenecks, not eliminated by generation [23].

- Nonlinear growth of comprehension time with discontinuities/indirection
  - Controlled and field studies consistently show that a large fraction of time is spent on navigation/comprehension mechanics, with concrete bottlenecks in forming/maintaining working sets and traversing dependencies; tool support could save on the order of 35% of maintenance time [6,8], and search/navigation strategies materially change elapsed task time [7,9].
  - Large-scale logging across applications confirms substantial comprehension shares in real work [10,11,12], in line with “just-in-time comprehension” in industrial settings [14].
  - Theory complements: abstraction has a cognitive difficulty tradeoff, implying non-monotone time effects if over-/under-generalized [3].
  - Post-LLM: tools targeting documentation/navigation reduce time in formative studies, aiming directly at the comprehension bottleneck [27,28,29].

- Bayesian/Lindy-like temporal models (aging/self-exciting change)
  - Lehman’s laws frame software as evolving systems with rising complexity/maintenance needs unless actively controlled [13].
  - Time dependence and propagation: change periods influence future periods, and Bayesian belief networks predict change propagation across artifacts—evidence for clustered, history-dependent change that can forecast maintenance demand [15,16,17].
  - Logical coupling from history (below) underpins these hazard views [24,25].

- Quality attributes as proxies for expected future development time
  - Across 39 proprietary systems, low-quality files take on average +124% longer to resolve issues (and >2× for comparable complexity), with up to ~9× higher variance; low-quality also shows ~15× more defects—framing quality as time economics and a business lever, not an end in itself [4].
  - A follow-up value-creation model shows strong non-linearities: amplified returns at the high-quality end, implying convex benefits to keeping already healthy code clean [5].
  - TD syntheses explicitly define debt as about future development cost and advocate economic decision models, while noting a lack of validated ROI quantification in practice [18,20,22].

- Quantitative links between change proximity/scattering and development time
  - Scattered relevant code and deep dependency traversal increase search/reinvestigation time; structured, dependency-guided investigation reduces elapsed time [7,8].
  - Improving localization/search by combining textual and structural signals is argued and shown to reduce maintenance time [26,29].

- Mathematical refactoring ROI/amortization or optimal-control framing
  - Industrial effect sizes in [4,5] provide empirical parameters to amortize refactoring: savings per future change are both significant and non-linear (larger at higher quality), directly supporting ROI thresholds.
  - TD finance reviews lay out real-options/portfolio framings but stress the empirical ROI gap [18,20].
  - Post-LLM: ACE operationalizes an ROI-oriented loop with objective “improvement” and behavior-preserving validation to ensure generated refactorings translate into future time savings rather than metric-only gains [23].

- Coupling/cohesion defined via co-change probabilities tied to time outcomes
  - Logical coupling is operationalized from version/release histories via co-change probabilities, providing a data-driven definition of coupling that can drive coordination/test-scoping and anticipated change impact [24,25].
  - Combined with Bayesian propagation [17] and time dependence [15,16], these form the ingredients for probabilistic models of expected change time over artifact networks.

### Most integrative works and how they connect multiple subclaims

- Veldhuizen’s MDL/entropy program integrates limits and cognition: libraries/DSLs compress specs with limits set by domain entropy; the best abstractions minimize description length while balancing cognitive difficulty [2,3].
- Tornhill & Borg’s industrial studies link code quality directly to elapsed development time and quantify non-linear returns, enabling refactoring ROI reasoning and prioritization [4,5].
- ACE (post-LLM) integrates compression limits, comprehension bottlenecks, quality-as-time economics, and refactoring ROI into an automated, behavior-validated pipeline designed to reduce end-to-end development time rather than just code-writing effort [23].
- The evolution/logical-coupling/Bayesian line integrates hazard and proximity: co-change networks and time dependence provide predictive structure for where/when change time will be higher [13,15,16,17,24,25].

### Key quantitative effects to carry into models and decisions

- Comprehension/navigation dominates:
  - ~35% of maintenance time is navigation mechanics; structured dependency-guided strategies reduce elapsed time [6,7,8,9].
  - Field evidence confirms substantial comprehension shares across tools and browsers [10,11,12,14].
- Quality strongly affects time:
  - Low-quality files: +124% average longer issue resolution; >2× for comparable complexity; ~15× more defects; much higher variance and long tails in cycle times [4].
  - Non-linear benefits: amplified returns at high quality; suggests threshold/convex ROI for preventive refactoring and stricter quality gates on high-churn hotspots [5].
- Temporal clustering/hazard:
  - Changes cluster and propagate; earlier periods influence later ones; co-change probabilities are measurable and predictive [15,16,17,24,25].

### What is missing or weak in this corpus (opportunities)

- Explicit information-theoretic lower bounds calibrated to human time: while [2,3] bound representation/compression, no paper here turns requirement/spec entropy into empirical minutes/hours after accounting for ambiguity and verification.
- Optimal-control/refactoring policies with validated parameters: reviews call for it [18,20]; [4,5] provide inputs, but end-to-end amortization and control policies (with demand forecasts and option value) are not yet formalized in this set.
- Direct mapping from co-change mutual information to expected time: coupling is quantified [24,25], propagation is modeled [17], but fully specified time predictors that decompose locate–understand–edit–validate against the coupling network are not presented.

### Practical implications for a development-time optimization agenda (pre- and post-LLM)

- Prioritize reductions in comprehension/navigation cost:
  - Invest in tools and practices that maintain working sets, surface dependency paths, and stabilize documentation; expect double-digit percentage savings on maintenance time [6,8,10,11,12,27,28,29].
- Treat code quality as a time-economic variable:
  - Use file-level health and churn to prioritize refactoring where savings are largest; anticipate convex returns at the high-quality end; track variance reduction as a value dimension [4,5].
- Exploit temporal and probabilistic structure:
  - Use co-change networks and time dependence to forecast where change will land next and preemptively refactor/test there; treat hot spots as self-exciting processes [15,16,17,24,25].
- In LLM-enhanced workflows:
  - Focus on lowering specification entropy (clarification loops), constraining generation with domain-specific codebooks/DSLs [2,3], and strengthening automated behavior-preserving validation so generation speed translates to end-to-end time reduction [23].

### Earliest anchors to cite for each prioritized claim

- Limits and spec–implementation gap: Brooks (1986) [1]; reuse/entropy/MDL (2005–2007) [2,3].
- Comprehension time and nonlinearity: Robillard & Murphy (2004) [7]; Ko & Myers (2005–2006) [6,8]; Singer et al. (2010) [14].
- Temporal/aging/hazard: Lehman (1997) [13]; logical coupling (1998, 2003) [24,25]; Bayesian propagation (2007) [17]; time dependence (2009–2010) [15,16].
- Quality as time proxy and ROI: industry datasets (2022–2024) [4,5]; TD finance SLRs (2015) [18,20].
- Post-LLM integration: ACE (2025) [23]; navigation-support tools (2023–2025) [27,28,29].

## Categories

### Scope and organizing principles used for comparison

- I group the papers against the seven prioritized lenses from the search goal: (1) information/specification-time lower bounds and the spec–implementation gap; (2) nonlinear comprehension costs/indirection; (3) Bayesian/Lindy/aging and hazard/self-exciting change; (4) quality attributes as proxies for expected future development time; (5) change proximity/scattering tied to time; (6) refactoring ROI/amortization and control; (7) coupling/cohesion from co-change probabilities tied to time outcomes.
- Within each lens, I compare: explicit optimization/time framing; empirical time measures and headline quantitative effects; theoretical formalisms; integration across lenses; and pre/post‑LLM relevance.

---

### Crosswalk of papers to the seven prioritized lenses

| Ref | Year | (1) Info/spec gap limits | (2) Nonlinear comprehension/indirection | (3) Bayesian/Lindy/aging | (4) Quality as time proxy | (5) Proximity/scattering→time | (6) Refactoring ROI/optimization | (7) Probabilistic coupling/cohesion |
|---|---:|---|---|---|---|---|---|---|
| [1] | 1986 | Strong: essential vs accidental effort limits; tool gains bounded | Implicit (complexity) | – | Implicit (maintainability as means) | – | – | – |
| [2] | 2005 | Strong: information-theoretic bounds on reuse potential | Implicit via abstraction scale | – | – | – | – | – |
| [3] | 2007 | Strong: MDL framing; compression of specs by DSLs/libs | Explicit tradeoff curves: abstraction power vs cognitive difficulty | – | – | – | – | – |
| [6] | 2005 | – | Strong: 3-phase model; up to 35% potential time savings with better tools | – | – | Implicit via navigation burden | – | – |
| [7] | 2004 | – | Strong: investigation patterns tied to elapsed change time | – | – | Strong: scattered relevance increases time | – | – |
| [8] | 2006 | – | Strong: ~35% time on navigation mechanics | – | – | Strong: dependency navigation overhead | – | – |
| [9] | 2009 | – | Strong: navigation styles differ significantly in time | – | – | – | – | – |
| [10,11] | 2018 | – | Strong: field-measured comprehension time across apps | – | – | – | – | – |
| [12] | 2015 | – | Strong: time budget categories; dev time breakdown | – | – | – | – | – |
| [13] | 1997 | – | – | Strong: evolution/aging laws | – | – | – | – |
| [15,16] | 2009–10 | – | – | Strong: time dependence between changes | – | – | – | – |
| [17] | 2007 | – | – | Strong: Bayesian change propagation | – | – | – | – |
| [24,25] | 1998/2003 | – | – | – | – | – | – | Strong: logical coupling via co-change |
| [4] | 2022 | – | – | – | Strong: lower quality → longer Time‑in‑Development | – | Implicit: ROI motivation | – |
| [5] | 2024 | – | – | – | Strong: non-linear value/returns model linking quality to implementation time | – | Implicit: refactoring ROI discussion | – |
| [18] | 2015 | – | – | – | Strong: TD defined as future dev cost | – | Calls for cost/benefit models | – |
| [20] | 2015 | – | – | – | Strong: economic framing of TD | – | Mentions real-options/portfolio views | – |
| [21] | 2012 | – | – | – | Implicit (metric improvements for maintainability) | – | Search-based refactoring (no ROI) | – |
| [22] | 2021 | – | – | – | Strong in practice framing | – | Practice-oriented remediation | – |
| [26] | 2010 | – | Strong: faster localization reduces maintenance time | – | – | Strong: improved search reduces time | – | – |
| [27] | 2024 | – | Strong: reduced doc-navigation time in formative study | – | – | – | – | – |
| [28] | 2023 | – | Strong: reduce comprehension via semantic graph | – | – | – | – | – |
| [29] | 2025 | – | – | – | – | Implicit: faster localization across issue types | – | – |
| [30] | 1995 | Implicit: reuse as only realistic path to order‑of‑magnitude productivity | – | – | – | – | Mentions economic models for reuse | – |
| [23] | 2025 | Implicit: LLMs compress spec→code; verification bottleneck | Strong: comprehension fraction cited; end-to-end refactoring | – | Strong: code health→time, TD “interest” | – | Strong practice framing of ROI | – |

Notes:
- Cells marked “Implicit” indicate the paper frames or motivates the aspect but does not formalize it with time-based models or measurements.
- Only [24,25] directly define coupling via co-change probabilities; [17] predicts change propagation; several comprehension studies connect navigation and scattering to time.

---

### Theoretical limits and the specification–implementation gap

- Unique contributions:
  - Information-theoretic bounds and compression framing:
    - Reuse fraction ≤ 1 − H in a domain with entropy H; component utility distributions follow Zipf-like laws; best abstraction minimizes description length of use cases [2,3]. These establish ceilings on how much “encoding” effort can be reduced by libraries/DSLs and argue that better abstractions compress specification and code, but cannot remove the information that must be acquired/verified.
  - Essential vs accidental effort:
    - Brooks argues that most historical productivity gains removed accidental difficulties; unless accidental work is >90% of effort, eliminating it cannot yield an order‑of‑magnitude improvement, shifting focus to irreducible conceptual complexity and specification work [1].
  - LLM-era restatement:
    - ACE positions LLMs as tools that compress implementation but stresses the need for objective “improvement” criteria and behavior-preserving validation, implying verification/comprehension remain bottlenecks [23].
- Comparative assessment:
  - Explicit optimization/minimization of development time: [2,3] formalize optimization via description length, not elapsed time. [1] qualitatively argues about time bounds via essential complexity. [23] ties model-driven refactoring to time by citing prior time studies and enforcing validation.
  - Integration across lenses: [3] is most integrative, explicitly trading off abstraction power against cognitive difficulty (connecting (1) and (2)); [1] connects limits with tool benefits; [23] connects (1), (2), (4), and (6) in a practical pipeline.

---

### Nonlinear comprehension costs, indirection, and navigation time

- Unique contributions and quantitative findings:
  - Mechanics of navigation is costly:
    - Developers spend about 35% of their time on navigation mechanics; tools could save up to 35% on maintenance tasks by better support for forming/maintaining working sets and navigating dependencies [6,8].
  - Strategy and time performance:
    - Effective investigation strategies (structurally guided searches) correlate with shorter elapsed change times in a controlled study; difficulty discovering relevant methods increases reinvestigation time [7]. Navigation styles differ significantly in time spent collecting information [9].
  - Field scale:
    - Large-scale field logging across applications measures comprehension time in natural settings [10,11]; time categories echo earlier lab findings [12].
  - Abstraction and cognitive difficulty:
    - Tradeoff curves between abstraction power, reuse enabled, and cognitive difficulty are articulated conceptually within an MDL framework [3].
  - Post-LLM maintenance tooling:
    - IDE‑integrated aids (CodeCompass) show reduced documentation-navigation time in formative studies; framing emphasizes cognitive overload and documentation discontinuities [27]. Knowledge graphs aim to convert comprehension into faster search [28].
- Comparative assessment:
  - Time metrics: [6,7,8,9,10,12] measure or report elapsed time fractions; [27] reports reductions in a formative setting; [3] provides theory without time measurements.
  - Nonlinearity: [5] later adds non-linear returns for quality/time; [3] conceptually suggests non-monotone abstraction benefits due to cognitive costs; empirical discontinuities (e.g., crossing boundaries) are qualitatively documented in [6,7,8,14].

---

### Temporal models: Bayesian/self-exciting change, aging, and hazard

- Unique contributions:
  - Evolution/aging laws:
    - Lehman’s laws characterize long-term evolution and growth/complexity trends, supporting the idea of software “aging” that, if not countered, raises future change costs [13].
  - Time dependence between changes:
    - Empirical analyses of large repositories show “time dependence” of code changes—periods and subsystems with changes that influence future changes—offering a way to identify high-impact modules and periods [15,16].
  - Predictive propagation:
    - Bayesian belief networks predict change propagation across software artifacts [17].
- Comparative assessment:
  - Explicit link to development time: [15,16] analyze impact on project development; [17] focuses on propagation probabilities rather than elapsed time; [13] frames process dynamics without time metrics.
  - Integration: These works connect to (7) and (5) by operationalizing the neighborhood/hazard of future changes; combining them with [24,25] yields a probabilistic coupling picture.

---

### Quality attributes as proxies for expected future development time

- Unique contributions and quantitative findings:
  - Code health and time-to-resolve:
    - Across 39 proprietary codebases, low-quality files have ~15× more defects, take on average +124% longer to resolve issues, and show much higher variance/max cycle times; the study explicitly ties code-level quality to Time‑in‑Development and positions findings as business ROI for refactoring [4].
  - Non-linear returns:
    - Combining public datasets, the value-creation model shows that associations between code quality and implementation time vary across the quality spectrum, with amplified returns on investment at the high end; the study emphasizes non-linearities and broken-windows dynamics [5].
  - TD as time/cost:
    - Systematic reviews emphasize TD as about future development cost, and call for quantified cost/benefit models; they catalog economic framings used in practice (real options, portfolios) [18,20,22].
- Comparative assessment:
  - Strength of time linkage: [4,5] are the most direct and quantitative on elapsed implementation/resolution time; [18,20,22] consolidate the economic framing but without new time measurements.
  - Integrative: [23] builds directly on these to justify automated refactoring with objective validation.

---

### Proximity/scattering and time, localization, and co-change coupling

- Unique contributions:
  - Scattering and elapsed time:
    - Scattered relevant code and dependency navigation increase task time; successful strategies mitigate reinvestigation [7,8]. Tooling that fuses structural and textual cues is argued to reduce localization time [26].
  - File localization from issues:
    - Dataset and baselines for general issue-to-file localization aim to reduce developer time spent localizing changes across issue types; shows project-dependent performance and limited benefit of bug-specific heuristics outside bugs [29].
  - Logical coupling via co-change:
    - Product/release history mining defines logical coupling through co-change probabilities between artifacts; these measures operationalize probabilistic coupling that can inform expected coordination/validation scope [24,25].
  - Predictive coupling:
    - Bayesian models estimate propagation probabilities [17].
- Comparative assessment:
  - Time-outcome linkage: [7,8,26,29] link to time through localization/comprehension savings; [24,25,17] quantify coupling/probabilities but do not themselves measure elapsed time impacts, though they are directly usable in time-prediction models.

---

### Refactoring economics: ROI/amortization and optimal policies

- Unique contributions:
  - Empirical ROI signals:
    - Measured time penalties for low-quality code and non-linear value models provide inputs for ROI calculations: savings per future change vs refactoring cost [4,5].
  - Economic framing and gaps:
    - Systematic reviews document the use of real-options and portfolio perspectives and explicitly note the lack of accurate, validated TD cost/benefit quantification in practice [18,20].
  - Automated refactoring with validation:
    - ACE positions refactoring as a scalable, automated activity where “improvement” must be objective and behavior-preserving; it synthesizes prior evidence on maintenance/comprehension time fractions and LLM productivity claims, and argues refactoring is under-addressed despite high time impact [23].
  - Search-based refactoring:
    - Automated refactoring guided by quality metrics (QMOOD, coupling/cohesion/complexity) demonstrates structural improvements; time-based ROI is not measured [21].
- Comparative assessment:
  - Only [4,5] bring quantified time deltas suitable for amortization math; [18,20] provide the economic vocabulary; [23,21] provide mechanisms, with [23] emphasizing validation to manage risk to development time.

---

### Highlight table: strongest time-focused findings and how they complement each other

| Lens | Strongest time-linked empirical result | Complementary theory/mechanism | Pre/Post LLM relevance |
|---|---|---|---|
| (1) Info/spec gap | – (no new time measures) | Essential vs accidental limits [1]; reuse/MDL bounds on achievable compression [2,3] | LLMs compress code but shift bottleneck to verification/comprehension [23] |
| (2) Comprehension/indirection | ~35% of developer time on navigation mechanics; up to 35% savings possible with better tools [6,8]; strategy affects elapsed change time [7,9] | Abstraction tradeoff curves (power vs cognitive difficulty) [3] | Tools that reduce doc navigation show time reductions [27]; knowledge graphs to speed search [28] |
| (3) Aging/hazard | Time dependence of code changes across long histories [15,16] | Lehman’s evolution/aging laws [13]; Bayesian propagation [17] | Applies regardless of LLM; could inform AI-guided change planning |
| (4) Quality→time | Low-quality files: +124% longer issue resolution; >2× for comparable complexity; ~15× defects; higher variance [4]; non-linear, amplified returns at high quality [5] | TD framed as future dev cost; economic views [18,20] | Used to prioritize AI-assisted refactoring [23] |
| (5) Proximity/scattering | Scattering increases elapsed change time via navigation/coordination [7,8]; improved localization reduces time [26,29] | Logical coupling via co-change [24,25]; Bayesian propagation [17] | Supports LLM prompts/seed selection and validation scopes [29,23] |
| (6) Refactoring ROI | Time deltas suitable for amortization in [4,5]; practice framing in [22] | Economic metaphors (options/portfolios) [20]; calls for quantified ROI [18] | ACE operationalizes objective, validated refactoring [23] |
| (7) Probabilistic coupling | – (time not directly measured) | Co-change probabilities define logical coupling [24,25]; propagation models [17] | Direct inputs to time prediction and test-scoping in AI-assisted workflows [23] |

---

### Integrative observations and what is uniquely informative to development-time optimization

- Early theoretical framing that still underpins post‑LLM work:
  - Brooks’ essential/accidental distinction [1] and Veldhuizen’s information-theoretic/MDL framing [2,3] together articulate a lower-bound view: tools compress implementations but cannot beat the informational burden of specification, comprehension, and validation. ACE’s validation-first design reflects this boundary in the LLM era [23].
- Quantified levers with the largest observed time effects:
  - Code quality/health shows large multipliers on elapsed implementation/resolution time (+124% on average; >2× for comparable complexity; variance up to ~9×) [4], with non-linear returns at the high end [5]. These provide concrete parameters for ROI calculations in (6).
  - Navigation/comprehension overhead sits around a third of developer time in multiple settings, and concrete tool affordances are identified (working sets, dependency navigation, losing tracked items) [6,7,8,9,12]. This isolates intervention surfaces for time minimization.
- Temporal structure to anticipate future time:
  - Change processes are path-dependent and cluster in time and space; time dependence and propagation can be modeled, offering a predictive basis for expected future change time and for prioritizing refactoring/test investments [13,15,16,17,24,25].
- Operational proxies for expected change time:
  - Logical coupling via co-change probabilities [24,25] and code health metrics linked to elapsed time [4,5] convert multi-attribute quality into time predictions, aligning with (4) and enabling control decisions (6).

---

### Limitations and cautions across the evidence base

- Proprietary metrics and attribution: Time‑in‑Development assignment across files in multi‑file changes and use of a proprietary Code Health metric in [4] introduce attribution and confounding risks (author experience, language) acknowledged by the authors.
- Generalizability of lab studies: Small‑N controlled studies [6,7,8,9] provide rich mechanisms and time measures but need caution when extrapolating to large, heterogeneous codebases; the field study [10,11,12,14] mitigates this by broader sampling but reports category fractions rather than intervention effects.
- Theory‑to‑time gap: Information-theoretic/MDL analyses [2,3] and logical coupling/probabilistic propagation [24,25,17] provide rigorous structures but rarely translate directly to elapsed time without additional calibration data.
- ROI quantification gap: Reviews [18,20] explicitly note the scarcity of validated, quantitative ROI models for TD/refactoring; [5] begins to address non-linear value, and [4] provides effect sizes, but complete amortization/optimal‑control models remain to be assembled from these components.

---

### References most integrative across lenses

- Veldhuizen’s MDL/abstraction tradeoffs [3] integrate (1) and (2).
- Tornhill & Borg’s studies [4,5] integrate (4) and (6) with non-linearities and explicit time deltas.
- ACE [23] integrates (1), (2), (4), and (6) in a post‑LLM setting, grounded in behavior-preserving validation.
- Logical coupling and propagation [24,25,17] connect (5) and (7) and support (3) when combined with temporal analyses [15,16].

## Timeline

### Timeline overview and major milestones

- 1980s: Conceptual separation of “essential” vs. “accidental” effort anchors limits to productivity gains
  - Brooks’ No Silver Bullet argues most past productivity improvements removed accidental difficulty, and that the remaining essential complexity constrains achievable time reduction—implicitly framing a lower bound on development time by problem essence and specification complexity [1].

- 1990s: Evolutionary view of software change and early coupling-from-history
  - Lehman’s “laws” reorient attention from single-delivery projects to continuous evolution, motivating models where past change predicts future change and costs accrue with growth/aging [13].
  - Logical coupling via co-change is introduced and operationalized using release/VC history, establishing that change co-occurrence is measurable and can guide maintenance focus [24,25].

- Mid-1990s–2000s: Reuse economics and information-theoretic views; emergence of comprehension-as-time bottleneck
  - Reuse as a dominant lever for productivity/quality and its economic ramifications are synthesized, foreshadowing specification–implementation compression as a strategy [30].
  - Veldhuizen models limits to reuse with Kolmogorov complexity and domain entropy, casting libraries/DSLs as codebooks that compress program descriptions, connecting abstraction choice to description-length optimization (and implicitly, to time) [2,3].
  - Empirical studies establish that maintenance is dominated by comprehension and navigation; structured search beats opportunistic browsing; and IDE mechanics alone consume large fractions of task time (≈35%) [6,7,8]. Follow-ups quantify time across activities and navigation styles [9,12].

- Late 2000s–2010s: Temporal models and field-scale measurement of comprehension time
  - Bayesian models for change propagation and empirical “time dependence” studies treat change processes probabilistically and intertemporally, linking past change to future hazard and impact [17], and analyzing how development periods influence future periods [15,16].
  - The “Just-In-Time Comprehension” characterization anchors a practical workflow model where developers repeatedly reconstruct just enough understanding immediately before a change [14].
  - Large-scale field measurements quantify comprehension time in the wild across apps and browsers, confirming comprehension as a substantial share of developer time [10,11].

- Mid-2010s: Technical debt as financial/time economics; mapping evidence gaps
  - Systematic mappings emphasize TD as future development cost, but document the lack of quantitative ROI, amortization, and time-predictive models; they call for economics- and finance-based approaches (options, portfolios) and better empirical validation [18,20].

- Early 2020s: Industrial evidence linking code quality to elapsed time; non-linearities emerge
  - Proprietary multi-codebase studies tie file-level “code health” to time-in-development, reporting 2×+ longer resolution times and higher variance in low-quality code; explicitly positioned as time-waste/ROI arguments for refactoring [4].
  - Follow-up models find non-linear returns: amplified benefits at the high-quality end and strong non-linearities across the spectrum; positioned to support ROI discussions for refactoring [5].

- 2023–2025 (post-LLM): From generation speed to maintainability and validated change-time reduction
  - New tools target comprehension and localization to reduce navigation time (semantic search, documentation augmentation, file localization) and are evaluated on time/efficiency outcomes [27,28,29].
  - ACE proposes an automated, validated LLM refactoring loop, explicitly motivated by the share of time in comprehension/maintenance and by turning “improvement” into an objective tied to future development time; it contrasts claimed LLM coding speedups with correctness/maintainability risks and emphasizes verification and behavior preservation as necessary to translate generation into time savings [23].


### Thematic evolution across the seven prioritized areas

- Information-theoretic and conceptual lower bounds
  - Brooks’ essential vs. accidental distinction frames irreducible effort due to intrinsic problem complexity and specification understanding [1].
  - Veldhuizen’s entropy/MDL framing formalizes the compression limits of abstraction/reuse/DSLs, implying bounds on how much specification-to-implementation time can be reduced by better components/metalanguages; over/under-generalization costs are captured via description length, with cognitive difficulty acknowledged qualitatively [2,3].
  - Trend: from qualitative limit statements [1] to formal compression bounds on representation [2,3], but still sparse direct linkage to human verification/comprehension time.

- Nonlinear comprehension time and indirection/abstraction trade-offs
  - Empirical IDE studies show mechanics of navigation consume large fractions of time and that search strategies materially affect elapsed time [6,7,8,9,12]. JITC highlights repeated partial re-comprehension [14]. Field studies quantify comprehension share at scale [10,11].
  - Recent works design tools to reduce documentation/navigation time, reporting time reductions and completion improvements [27,28,29].
  - Trend: accumulation from lab protocols to large-scale in-the-wild time logs [10,11], then to tool interventions optimized for navigation/comprehension time [27,28,29]. Direct quantification of abstraction “tax vs. reuse” breakeven remains under-modeled; Veldhuizen provides MDL theory without time calibration [3].

- Bayesian/Lindy-like temporal models (aging, hazard/self-excitation)
  - Early empiricism on logical coupling [24,25] evolves into probabilistic change-propagation models [17] and time dependence analyses showing how earlier periods influence later development [15,16].
  - Lehman’s evolution perspective continues to motivate “aging unless renewed” hypotheses with implications for rising marginal change time [13].
  - Trend: recognition of clustered, history-dependent change, but few studies link these hazards explicitly to expected lead time distributions.

- Quality attributes as proxies for expected future development time
  - Industrial multi-system analyses quantitatively tie code quality proxies to defect rates and, crucially, to time-to-resolve and its variance, reframing quality as time economics and enabling refactoring ROI narratives [4,5].
  - TD reviews explicitly identify TD as future development cost and advocate economic framing, while noting missing quantitative models [18,20].
  - Trend: concrete time-effects evidence emerges primarily from industry datasets [4,5], addressing a gap identified in TD syntheses [18,20].

- Proximity/scattering and time outcomes
  - Empirical comprehension/navigation studies show scattering and dependency traversal inflate search time [6,7,8,14]; logical coupling identifies artifacts that co-change, implying hidden proximity that affects coordination and regression scope [24,25].
  - Trend: strong observational basis that scattering increases time; formal models mapping co-change probabilities to expected time remain largely implicit.

- Refactoring ROI/amortization and optimal control
  - TD finance reviews call for options/portfolio/ROI models but find limited rigorous quantification [20]; mapping studies echo the measurement gap [18].
  - Industrial studies translate quality-time associations into a “value creation” model with non-linear returns to maintenance investment [5] and motivate ROI-minded refactoring [4,5].
  - LLM-era ACE operationalizes “objective improvement” and behavior-preserving validation, aligning with the requirement that refactoring must reduce future time, not just metrics [23].
  - Trend: movement from conceptual finance metaphors to empirically parameterized time-effects and toolchains designed to deliver validated, amortizable improvements [4,5,23].

- Coupling/cohesion via co-change probabilities tied to time
  - Foundational work detects logical coupling from histories [24,25]; Bayesian belief networks predict propagation [17]; time dependence of changes highlights interperiod impacts [15,16].
  - Direct formulations linking co-change probabilities to expected change time are suggested by these lines but not fully formalized in the surveyed set; industrial studies use file-level aggregation rather than networked hazard-to-time models [4,5].
  - Trend: the ingredients for probabilistic, time-predictive coupling models exist, but integration into time forecasts is an open opportunity.


### Trends and shifts in methods and emphasis

- From narrative limits to formal compression theory: The field progresses from Brooks’ conceptual limit arguments [1] to information-theoretic analyses of abstraction/reuse as compression [2,3]. However, the bridge from description length to human time remains under-quantified.

- From small-N lab studies to large-scale, in-the-wild time measurement: Early protocol analyses and IDE-logging studies [6,7,8,9,12] evolve into cross-application HCI logging with hundreds of hours, quantifying comprehension time shares [10,11].

- From structure-only metrics to history- and probability-aware models: Static coupling/cohesion gives way to logical coupling and propagation modeling [24,25,17], and to temporal dependence analyses [15,16], aligning with hazard-based views of maintenance.

- From quality as an abstract virtue to quality-as-time economics: Technical debt syntheses call for financial framing [18,20], and industry studies deliver quantitative links from code health to time outcomes with non-linear effects [4,5].

- Post-LLM pivot from generation to validation and maintainability: With code generation cheap, emphasis shifts to verification, behavior preservation, and sustained reduction of future development time; ACE embodies this by validating LLM refactorings and objectivizing “improvement” [23]. Concurrently, tools target the comprehension bottleneck (documentation augmentation, localization) [27,28,29].


### Key contributor clusters and sustained threads

- Cognitive/comprehension and navigation cluster (Ko & Myers; Robillard & Murphy; Singer et al.; Minelli; Xia et al.)
  - Established that maintenance time is dominated by comprehension/navigation and identified specific mechanics and tool gaps [6,7,8,9,12,14], culminating in large-scale time measurements [10,11].
  - Influence: Anchored the “optimize development time by reducing comprehension cost” agenda; informs tool design and evaluation criteria.

- Software evolution and change-propagation cluster (Lehman; Gall et al.; Hassan’s group; Mirarab & Tahvildari)
  - From evolution laws [13] to logical coupling [24,25], Bayesian propagation [17], and time dependence across periods [15,16].
  - Influence: Provides the empirical and modeling basis for hazard/self-exciting views of change and for treating coupling/cohesion probabilistically.

- Information-theoretic abstraction/reuse cluster (Veldhuizen)
  - Formalizes bounds and MDL trade-offs for libraries/DSLs as compression schemes [2,3].
  - Influence: Theoretically grounds the “specification–implementation gap” and cautions that abstractions have optimal granularity; invites time-calibrated MDL in SE.

- Technical-debt economics and industrial time-effects cluster (Ampatzoglou et al.; Li et al.; Tornhill & Borg; ACE team)
  - SLRs articulate TD as future development cost and call for ROI models [18,20]. Industrial studies quantify quality–time links and non-linear returns [4,5]. ACE operationalizes validated, objective refactoring in an LLM context [23].
  - Influence: Shifts the field toward decision support based on expected time savings, with data pipelines that enable ROI-oriented maintenance.


### Implications and likely future directions

- Integrating information theory with cognitive and verification time: Formal compression bounds [2,3] and essential-complexity limits [1] need coupling to empirically measured human-channel rates and verification effort to produce practical lower bounds on change lead time.

- Hazard-based, networked time forecasting: The ingredients—logical coupling [24,25], propagation models [17], and time dependence [15,16]—are poised to yield predictive models of expected change time that account for co-change probabilities, graph distance, and validation scope.

- Nonlinear economics of maintainability and optimal control of refactoring: Evidence of non-linear returns [5] and TD finance framing [18,20] motivate threshold/optimal-control policies for refactoring that consider volatility of demand and option value; ACE-like validated pipelines can provide the needed effect sizes [23].

- Post-LLM verification and maintainability as primary bottlenecks: With generation accelerated, research will likely emphasize reducing ambiguity/entropy in specifications, automating clarification and impact analysis, and strengthening behavior-preserving validation—so that coding speedups translate into sustained reductions in end-to-end development time [23,27,28,29].

- Cohesion/coupling via co-change probabilities tied to time outcomes: Expect a formalization of cohesion/coupling as mutual information among artifact change processes, calibrated to search/coordination/validation time components—fusing history mining with time-cost models implicitly suggested across the cited streams [24,25,17,4,5].

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [5] | 0.30 | 92% | Increasing, not Diminishing: Investigating the Returns of Highly Maintainable Code | Markus Borg, ..., and Adam Tornhill | 2024 IEEE/ACM International Conference on Technical Debt (TechDebt) | 2024 | 6 | [23] |
| [341] | 0.28 | Not measured | SweRank: Software Issue Localization with Code Ranking | R. Reddy, ..., and Shafiq Joty | ArXiv | 2025 | 2 | [29] |
| [12] | 0.23 | 72% | I Know What You Did Last Summer - An Investigation of How Developers Spend Their Time | Roberto Minelli, ..., and Michele Lanza | 2015 IEEE 23rd International Conference on Program Comprehension | 2015 | 195 | [10, 23, 35] |
| [10] | 0.22 | 76% | Measuring Program Comprehension: A Large-Scale Field Study with Professionals | Xin Xia, ..., and Shanping Li | IEEE Transactions on Software Engineering | 2018 | 277 | [23, 27, 29, 36] |
| [8] | 0.21 | 83% | An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks | Amy J. Ko, ..., and H. Aung | IEEE Transactions on Software Engineering | 2006 | 658 | [9, 10, 12, 28, 29] |
| [168] | 0.20 | 0% | Maintaining mental models: a study of developer work habits | Thomas D. Latoza, ..., and R. Deline | Proceedings of the 28th international conference on Software engineering | 2006 | 743 | [8, 10, 12] |
| [84] | 0.17 | 1% | Designing the whyline: a debugging interface for asking questions about program behavior | Amy J. Ko and B. Myers | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems | 2004 | 402 | [6, 8, 9, 10] |
| [11] | 0.16 | 75% | [Journal First] Measuring Program Comprehension: A Large-Scale Field Study with Professionals | Xin Xia, ..., and Shanping Li | 2018 IEEE/ACM 40th International Conference on Software Engineering (ICSE) | 2018 | 8 | [10] |
| [73] | 0.15 | 2% | The effects of naming style and expertise on program comprehension | Barbee Teasley | Int. J. Hum. Comput. Stud. | 1994 | 44 | [6, 8, 9, 10] |
| [219] | 0.14 | 0% | Extracting and analyzing time-series HCI data from screen-captured task videos | Lingfeng Bao, ..., and Bo Zhou | Empirical Software Engineering | 2016 | 36 | [10] |
| [4] | 0.13 | 94% | Code Red: The Business Impact of Code Quality - A Quantitative Study of 39 Proprietary Production Codebases | Adam Tornhill and Markus Borg | 2022 IEEE/ACM International Conference on Technical Debt (TechDebt) | 2022 | 21 | [23] |
| [293] | 0.13 | 0% | A framework and methodology for studying the causes of software errors in programming systems | Amy J. Ko and B. Myers | J. Vis. Lang. Comput. | 2005 | 202 | [6, 8] |
| [342] | 0.12 | Not measured | "Constant, constant, multi-tasking craziness": managing multiple working spheres | Víctor M. González and G. Mark | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems | 2004 | 720 | [6, 8] |
| [316] | 0.12 | 0% | The Time Famine: Toward a Sociology of Work Time | L. Perlow | Administrative Science Quarterly | 1999 | 949 | [6, 8] |
| [7] | 0.12 | 83% | How effective developers investigate source code: an exploratory study | M. Robillard, ..., and G. Murphy | IEEE Transactions on Software Engineering | 2004 | 288 | [8, 12] |
| [343] | 0.11 | Not measured | Leveraging legacy system dollars for e-business | L. Erlikh | IT Professional | 2000 | 461 | [6, 12, 26] |
| [142] | 0.11 | 0% | Models and Theories of Programming Strategy | S. Davies | Int. J. Man Mach. Stud. | 1993 | 179 | [6, 8] |
| [75] | 0.10 | 2% | On the Comprehension of Program Comprehension | W. Maalej, ..., and R. Koschke | N/A | 2014 | 181 | [10] |
| [344] | 0.10 | Not measured | How do professional developers comprehend software? | T. Roehm, ..., and W. Maalej | 2012 34th International Conference on Software Engineering (ICSE) | 2012 | 262 | [10] |
| [345] | 0.10 | Not measured | Quantifying Program Comprehension with Interaction Data | Roberto Minelli, ..., and Takashi Kobayashi | 2014 14th International Conference on Quality Software | 2014 | 20 | [12] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref.  | Adjacency score | Topic Match  | Title                                                                                                                                                 | Authors                                             | Journal                                                                                                      | Year | Total Citations | References These Foundational Papers |
| ----- | --------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- | --------------- | ------------------------------------ |
| [159] | 1.82            | 0%           | A Systematic Literature Review on the Influence of Enhanced Developer Experience on Developers' Productivity: Factors, Practices, and Recommendations | Abdul Razzaq, ..., and Goetz Botterweck             | ACM Computing Surveys                                                                                        | 2024 | 10              | [6, 8, 10, 12]                       |
| [359] | 1.49            | Not measured | An Exploratory Study of Programmers’ Analogical Reasoning and Software History Usage During Code Re-Purposing                                         | John Allen and Caitlin Kelleher                     | 2024 IEEE/ACM 17th International Conference on Cooperative and Human Aspects of Software Engineering (CHASE) | 2024 | 1               | [8, 10, 30, 31]                      |
| [59]  | 1.48            | 3%           | Developer's Cognitive Effort Maintaining Monoliths vs. Microservices - An Eye-Tracking Study                                                          | Georg Simhandl, ..., and Uwe Zdun                   | 2023 30th Asia-Pacific Software Engineering Conference (APSEC)                                               | 2023 | 0               | [8, 10, 68, 168]                     |
| [83]  | 1.34            | 1%           | Exploring the impacts of semi-automated storytelling on programmers’ comprehension of software histories                                              | John Allen and Caitlin Kelleher                     | 2024 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)                                 | 2024 | 2               | [8, 10, 31]                          |
| [214] | 1.28            | 0%           | Why reinventing the wheels? An empirical study on library reuse and re-implementation                                                                 | Bowen Xu, ..., and D. Lo                            | Empirical Software Engineering                                                                               | 2019 | 46              | [31, 32, 52, 121]                    |
| [360] | 1.26            | Not measured | A Retrospective on How Developers Seek, Relate, and Collect Information About Code                                                                    | Amy J. Ko, ..., and Htet Htet Aung                  | IEEE Transactions on Software Engineering                                                                    | 2025 | 0               | [8, 10, 68]                          |
| [79]  | 1.22            | 2%           | Visualising data science workflows to support third-party notebook comprehension: an empirical study                                                  | Dhivyabharathi Ramasamy, ..., and Abraham Bernstein | Empirical Software Engineering                                                                               | 2023 | 12              | [8, 12, 40, 82, 125]                 |
| [115] | 1.08            | 1%           | Learning from Mistakes: Understanding Ad-hoc Logs through Analyzing Accidental Commits                                                                | Yi-Hung Chou, ..., and James A. Jones               | 2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)                            | 2025 | 0               | [8, 10, 84]                          |
| [361] | 1.05            | Not measured | Meta-Manager: A Tool for Collecting and Exploring Meta Information about Code                                                                         | Amber Horvath, ..., and Brad A Myers                | Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems                                 | 2024 | 6               | [6, 8, 84]                           |
| [362] | 1.05            | Not measured | Nuzzlebug: Debugging Block-based Programs in Scratch                                                                                                  | Adina Deiner and G. Fraser                          | 2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE)                                   | 2023 | 5               | [6, 8, 84]                           |
| [363] | 1.02            | Not measured | Code histories: Documenting development by recording code influences and changes in code                                                              | Vo Pham Tri Thien and Caitlin Kelleher              | J. Comput. Lang.                                                                                             | 2024 | 0               | [8, 12]                              |
| [364] | 1.02            | Not measured | Recording and Interpreting Developer Behaviour in Programming Tasks                                                                                   | Martin Schroer and Rainer Koschke                   | 2024 IEEE/ACM First IDE Workshop (IDE)                                                                       | 2024 | 1               | [8, 12]                              |
| [365] | 1.02            | Not measured | Assessing the Effect of Programming Language and Task Type on Eye Movements of Computer Science Students                                              | Niloofar Mansoor, ..., and Bonita Sharif            | ACM Transactions on Computing Education                                                                      | 2023 | 5               | [8, 12]                              |
| [366] | 1.02            | Not measured | Generation-based Code Review Automation: How Far Are Weƒ                                                                                              | Xin Zhou, ..., and David Lo                         | 2023 IEEE/ACM 31st International Conference on Program Comprehension (ICPC)                                  | 2023 | 18              | [8, 12]                              |
| [367] | 1.02            | Not measured | Understanding and Supporting Debugging Workflows in Multiverse Analysis                                                                               | Ken Gu, ..., and Tim Althoff                        | Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems                                 | 2022 | 15              | [8, 12]                              |
| [368] | 1.02            | Not measured | A Data-Driven Analysis of Behaviors in Data Curation Processes                                                                                        | Lei Han, ..., and S. Sadiq                          | ACM Transactions on Information Systems                                                                      | 2022 | 6               | [8, 12]                              |
| [261] | 1.02            | 0%           | Students' Program Comprehension Processes in a Large Code Base                                                                                        | Anshul Shah, ..., and Adalbert Gerald Soosai Raj    | 2025 IEEE/ACM 33rd International Conference on Program Comprehension (ICPC)                                  | 2025 | 0               | [8, 12]                              |
| [143] | 1.01            | 0%           | Supporting Readability by Comprehending the Hierarchical Abstraction of a Software Project                                                            | Avijit Bhattacharjee, ..., and Kevin A. Schneider   | Proceedings of the 15th Innovations in Software Engineering Conference                                       | 2022 | 0               | [8, 12]                              |
| [74]  | 1.00            | 2%           | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding                                                            | Raphael Cabral, ..., and Hélio Lopes                | 2024 IEEE/ACM 3rd International Conference on AI Engineering – Software Engineering for AI (CAIN)            | 2024 | 11              | [8, 12]                              |
| [69]  | 0.99            | 2%           | Students' Use of GitHub Copilot for Working with Large Code Bases                                                                                     | Anshul Shah, ..., and Adalbert Gerald Soosai Raj    | Proceedings of the 56th ACM Technical Symposium on Computer Science Education V. 1                           | 2025 | 8               | [8, 12]                              |