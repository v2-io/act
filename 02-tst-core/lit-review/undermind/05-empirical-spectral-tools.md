# Empirical spectral tools for predicting software dependency cascades

## Overview

The retrieved literature contains no empirical studies or tools that compute spectra (e.g., spectral radius, directed/normalized Laplacians, resolvents) on real, directed, weighted software dependency graphs and validate cascade thresholds or sizes against observed propagation; instead, works largely use centrality features for fault/change prediction and one undirected spectral-clustering application, on small-to-medium OSS systems [1,2,3,4,5,6,7,9].

### What the corpus actually delivers

- Centrality-based prediction on dependency graphs
  - Class/file/function-level directed dependency graphs are built and centralities (eigenvector, PageRank, HITS, betweenness, closeness) are used to predict fault-proneness or rank “key” components; some graphs are weighted by dependency counts [2,3,4,5,6,7,9].
  - Examples:
    - Bug/fault-proneness prediction with centralities on class-level directed graphs (Tomcat, Ant) [4]; similar validation across multiple OSS projects combining centralities with OO metrics [3].
    - Weighted dependency networks with h-index–style key-class measures correlated to VCS revision counts (Tomcat, Ant, JUNG) [7].
    - PageRank-derived FunctionRank on invocation-weighted dynamic call graphs to identify influential functions [5].
    - Multi-relation networks integrating dependencies, co-change, and developer ties with eigenvector-like measures for defect prediction [9].
- Spectral clustering (undirected/unnormalized) for decomposition
  - Microservice identification via Laplacian eigenmaps + k-means on an undirected, unnormalized Laplacian derived from class dependencies; evaluated by cohesion/coupling metrics, not by propagation or stability [1].
- Structural use of SCCs
  - Dependence clusters defined as SCCs in function-level SDGs; larger clusters linked to higher fault-proneness; various centralities assessed within SCC subgraphs [2].

### Gaps relative to the target goals (a–h in the query)

- Spectral-radius thresholds and resolvent/cascade validation
  - No computation of ρ(A) on directed, weighted A; no explicit x_{t+1} = βA x_t cascade models; no resolvent (I − βA)^{-1} or exp(A) features; no testing of βρ(A) = 1 thresholds against observed change/bug cascades [1,2,3,4,5,6,7,9].
- Directed/normalized Laplacians and bottlenecks
  - No use of directed or normalized Laplacians, Fiedler values, or Cheeger-type analyses; [1] uses an unnormalized, undirected Laplacian only [1].
- Eigenvector centrality for critical components
  - Eigenvector/PageRank are used, but as correlational predictors rather than within a calibrated cascade or stability framework, and sometimes after symmetrization [2,3,4,5,6,7,9].
- Spectral clustering for module detection
  - Present only in [1], without directed/π-weighted formulations or robustness checks via eigengaps; evaluation is structural MQ, not evolution/propagation [1].
- Perturbation analyses/non-normality
  - No eigenvalue sensitivity (left/right Perron vectors), pseudospectral analysis, or low-rank resolvent updates reported [1,2,3,4,5,6,7,9].
- Matrix-function propagation
  - No empirical computation of Katz/resolvent or exp(A) on real software dependency graphs beyond generic PageRank usage [2,3,4,5,6,7,9].
- Random-graph baselines
  - No ER/configuration-model or scale-free baselines to quantify non-random structure or spectral deviations [1,2,3,4,5,6,7,9].
- Phase transitions and critical phenomena
  - No reports of phase transitions at ρ(A) = 1, cascade size distributions, or universality-class discussion on software graphs [1,2,3,4,5,6,7,9].

### Partial signals you can leverage

- Weighted, directed dependency construction exists
  - Several works construct A with edge weights from dependency counts or dynamic invocation frequencies at class/function granularity [5,7,9], and SDGs with directed data- and control-dependence edges [2].
- Temporal/validation hooks
  - VCS revision counts (change frequency) and issue-tracker-based bug labels are available and have been aligned to graph nodes in multiple studies, providing ground truth for future cascade validation [3,4,7,9].
- SCC awareness
  - SCC decomposition is used as an indicator of risky cyclic structure [2], which aligns with the block-structure perspective needed for directed spectral analysis.

### Dataset scale and representativeness

- Predominantly small-to-medium OSS systems
  - Case studies include Tomcat, Ant, JUNG, cflow, several academic datasets, and a few Java web programs; typical analyses operate at class/function granularity with thousands of nodes at most [1,3,4,5,6,7].
- No large industrial mono-repos or ecosystem-scale graphs
  - No evidence of Maven/npm/PyPI/Linux-scale dependency spectra, nor industrial pipelines with confidence intervals or thresholds [1,2,3,4,5,6,7,9].

### Tooling status

- Extraction tools and general-purpose platforms appear
  - Static dependency extraction via commercial tools (Understand) and reverse-engineering pipelines are used to produce graphs [4,6,9].
- Missing spectral-analysis tooling
  - No tools exposed for computing ρ(A), directed/normalized Laplacians, resolvents, exp(A), or for perturbation/pseudospectra and configuration-model baselines with uncertainty reporting [1,2,3,4,5,6,7,9].

### Methodological pitfalls visible in the corpus

- Direction/normalization often discarded
  - Symmetrization or undirected projections are common when computing “spectral” features (e.g., [1], parts of [3,6]), undermining directed cascade interpretability [1,3,6].
- Centrality ≠ cascade predictiveness
  - Centrality correlations with faults/changes are reported, but without models tying them to transmissibility β and resolvent-based susceptibility, so actionable βρ(A) thresholds are absent [3,4,7,9].
- No baselines or uncertainty
  - Without degree-preserving nulls and CIs, reported improvements may conflate structure with size/activity effects [1,2,3,4,5,6,7,9].

### Implications for your program of work

- Feasibility
  - The community already extracts directed, weighted A and links to VCS/issue trackers [3,4,5,7,9], so adding spectral-radius, directed/normalized Laplacians, and resolvent/exp(A) computations is technically feasible.
- Opportunity
  - There is a clear gap for a pipeline that:
    - Computes ρ(A) on SCCs and tests βρ(A) thresholds by estimating β from observed spillovers, with (I − βA)^{-1}-based susceptibility features and out-of-sample validation.
    - Uses directed/π-weighted normalized Laplacians to quantify bottlenecks and modularity, and evaluates spectral clustering stability via eigengaps.
    - Benchmarks spectral metrics against configuration-model nulls and reports uncertainty.
    - Quantifies perturbation leverage dρ/da_ij via Perron vector pairs to prioritize architectural hardening.
- Validation design
  - Use time-resolved A(t) from consecutive releases; align co-change and bug-spillover events with appropriate lags (as in [7,9] data handling), and evaluate calibration curves vs βρ(A) bins with bootstrapped CIs.

### Paper-by-paper positioning (most to least proximate)

- Closest methodological building blocks
  - Weighted directed dependency graphs with VCS validation: [7].
  - Dynamic weighted invocation graphs and influence scoring: [5].
  - Multi-relation integration including dependencies and co-change: [9].
  - SCCs as dependence clusters tied to risk: [2].
  - Spectral clustering (unnormalized, undirected) for decomposition: [1].
- Earlier centrality-focused works
  - Centrality-based bug prediction and developer-validated importance rankings: [3,4,6].
- Insufficient detail
  - Early mentions of “error propagation” and “cascading failure” lack accessible methods/results here [8,10].

## Categories

### Scope and Coverage Comparison Across Papers

- Overall, the retrieved set concentrates on centrality-based prediction and one microservice decomposition via spectral clustering; none provide empirical cascade modeling with βρ(A) thresholds, resolvent-based predictions, or directed/normalized Laplacian analyses on real software dependency graphs as specified in the goal [1,2,3,4,5,6,7,8,9,10].
- The most common spectral elements are eigenvector-derived centralities (often via PageRank) applied to directed or symmetrized graphs; there is no evidence in the provided excerpts of computing spectral radius ρ(A), matrix-function resolvents (I−βA)−1, exp(A), directed Cheeger/Fiedler analyses, perturbation derivatives of eigenvalues, or random-graph degree-preserving null baselines [1,2,3,4,5,6,7,9].
- Validation focuses on fault-proneness or change frequency correlations, not on observed cascade propagation aligned to βρ(A) thresholds; only [7] explicitly correlates centrality with VCS revision counts, and [4,9] use bug labels, but without cascade-size prediction or threshold testing [4,7,9].

### Comparison Matrix: Alignment with Target Spectral Topics

| Paper | ρ(A) / thresholds βρ(A)=1 | Resolvent / exp(A) | Laplacian (normalized/directed) & Cheeger | Eigenvector centrality (left/right), Katz/PageRank | Spectral clustering | Perturbation/eigenvalue sensitivity | Matrix-function propagation | Random-graph/configuration baselines | Cascade validation vs VCS/issue tracker |
|---|---|---|---|---|---|---|---|---|---|
| [1] | No evidence | No | Unnormalized Laplacian only (undirected) | Not the focus | Yes (unnormalized graph Laplacian) | No | No | No | No |
| [2] | No | No | No | Yes (eigenvector, PageRank among many) | No | No | No | No | Fault-proneness models only |
| [3] | No | No | No | Yes (eigenvector variants; sometimes symmetrized) | No | No | No | No | Fault-proneness/count prediction |
| [4] | No | No | No | Yes (eigenvector, PageRank, HITS) | No | No | No | No | Bug proneness/severity prediction |
| [5] | No | No | No | Yes (PageRank-derived FunctionRank) | No | No | No | No | Influence identification; no cascade validation |
| [6] | No | No | No | Yes (PageRank, Markov centrality, etc.) | No | No | No | No | Developer-judged importance; no VCS cascade |
| [7] | No | No | No | Yes (h-index variants vs common centralities) | No | No | No | No | Correlates with VCS revision counts |
| [8] | Insufficient info | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient |
| [9] | No | No | No | Yes (Bonacich power, eigenvector-based closeness, etc.) | No | No | No | No | Bug prediction (post-release) |
| [10] | Insufficient info | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient | Insufficient |

Notes:
- “No evidence” means the provided excerpts do not indicate the method was used; it does not preclude presence in full text.
- Where eigenvector centrality/PageRank is used, it is for node ranking/prediction, not for cascade-threshold analysis or resolvent computation [2,3,4,5,6,7,9].

### Dependency Graph Construction and Weighting

| Paper | Node granularity | Edge type(s) | Directed | Weighted (by counts) | Notes/Extraction tooling |
|---|---|---|---|---|---|
| [1] | Classes (Java) | Static structure; Wc from Wm and structure Lp | Likely undirected in Laplacian step | Not clearly weighted in spectral step | Combines static and dynamic analysis |
| [2] | Functions | Call + data dependencies (SDG) | Yes | Not specified | SCCs define “dependence clusters” |
| [3] | Classes | Static dependencies | Yes (sometimes symmetrized) | Not specified | Combines with OO metrics |
| [4] | Classes | 5 dependency types (inheritance, field, method, return, parameter) | Yes | Not specified | Reverse engineering to XML |
| [5] | Functions/modules | Invocation dependencies from execution traces | Yes | Yes (invocation counts) | Multiple versions of cflow |
| [6] | Classes/interfaces | Various dependency relations; best subset found | Both considered | Weighted via capacities in flow model | ConQAT mentioned |
| [7] | Classes | 5 dependency types; weight = number of dependencies | Yes | Yes (counts) | Tomcat, Ant, JUNG |
| [8] | — | — | — | — | — |
| [9] | Files + developers | Functional calls (Understand) + co-change; plus dev-file, dev-dev | Mixed | Weights normalized; combined | Tri-Relation Network |
| [10] | — | — | — | — | — |

Observations:
- Only [5,7,9] clearly use weighted directed edges by counts; others either do not specify or use unweighted/undirected surrogates for spectral steps [1,2,3,4,5,6,7,9].
- Use of proper SCC handling is explicit in [2]; important for interpreting eigenvectors and reducibility.

### Validation Signals and Outcomes

- Fault-proneness (classification/regression):
  - [2] metrics vs fault-proneness with effort-aware evaluation [2].
  - [3] centralities + OO metrics for fault-proneness, fault counts, and severity, with cross-version/system validation [3].
  - [4] centralities predict bug proneness and severity on Tomcat/Ant [4].
  - [9] TRN centralities improve post-release bug prediction over baselines [9].
- Change frequency:
  - [7] centrality variants correlated with VCS revision counts (e.g., R^2 ≈ 0.864 in one case) [7].
- Developer-labeled importance:
  - [6] recommends “central” classes; validated by developer judgment, not defects or cascades [6].
- Microservice decomposition quality:
  - [1] spectral clustering evaluated by MQ cohesion/coupling metric and comparisons to baselines; not defect/cascade-oriented [1].
- Cascade validation against observed propagation:
  - None of the excerpts report constructing x_{t+1}=βA x_t models, estimating β, computing (I−βA)−1, or validating predicted cascade sizes against co-change/bug-spillover events with temporal alignment [1,2,3,4,5,6,7,9].

### Methods Compared: Centralities and Spectral Tools

| Paper | Centralities used | Spectral clustering | Laplacians | Other spectral tools |
|---|---|---|---|---|
| [1] | — | Yes (unnormalized graph Laplacian; k-eigenvectors + k-means) | Unnormalized (undirected) | — |
| [2] | Eigenvector, PageRank, betweenness, closeness, etc. | No | No | — |
| [3] | Eigenvector variants, DMNC, closeness; degree excluded | No | No | — |
| [4] | Eigenvector, PageRank, HITS, betweenness, closeness, degree | No | No | — |
| [5] | FunctionRank (PageRank-like) | No | No | — |
| [6] | PageRank, Markov centrality, flow model | No | No | — |
| [7] | h-index style variants vs common centralities | No | No | — |
| [9] | Bonacich power, eigenvector of geodesic closeness, betweenness | No | No | — |

Key distinctions:
- Only [1] performs an explicit spectral clustering pipeline, but on an unnormalized Laplacian and without directed/π-weighted formulations; evaluation is structural (MQ), not propagation-based [1].
- Several papers use PageRank/eigenvector centrality but not for thresholds or cascade modeling, and sometimes on symmetrized graphs [2,3,4,5,6,7,9].

### Dataset Scale and Industrial Emphasis

- Small-to-medium OSS systems dominate:
  - [1] three Java Web programs from GitHub (e.g., JPet…), class-level [1].
  - [4] Tomcat and Ant [4].
  - [6] four Java OSS projects (~160k LOC average) [6].
  - [7] Tomcat, Ant, JUNG [7].
  - [5] multiple versions of cflow [5].
  - [3] several versions of five OSS systems from Jureczko/Spinellis [3].
- Package-ecosystem scale (e.g., npm, PyPI) and large industrial mono-repos are not present in the excerpts [1,2,3,4,5,6,7,9].
- No study reports industrial-scale validation with issue trackers and VCS aligned to cascade events, nor calibration of actionable thresholds (e.g., βρ cutoffs with CIs) [1,2,3,4,5,6,7,9].

### Methodological Gaps Relative to the Goal

- Missing spectral-radius and threshold analyses:
  - No computation of ρ(A) or βρ(A) thresholds; row-stochastic normalization and associated β interpretation absent [1,2,3,4,5,6,7,9].
- Missing directed/normalized Laplacians:
  - No use of Chung’s directed Laplacian, π-weighted symmetrizations, or Cheeger-type analyses for bottlenecks; where Laplacians appear, they are unnormalized and undirected [1].
- Absent cascade/resolvent modeling and validation:
  - No resolvent (I−βA)−1, no exp(A), no matrix-function propagation on real software graphs; no empirical cascade size prediction or threshold localization [1,2,3,4,5,6,7,9].
- Limited perturbation/non-normality analysis:
  - No eigenvalue sensitivity (u,v) or pseudospectra; no low-rank resolvent updates [1,2,3,4,5,6,7,9].
- Baselines:
  - No ER/configuration-model or degree-preserving nulls to contextualize spectral structure [1,2,3,4,5,6,7,9].
- Tooling:
  - Tools that compute advanced spectral analyses (ρ(A), directed Laplacians, resolvents) and provide uncertainty/thresholds are not reported; ConQAT is mentioned for general analysis in [6], Understand for static extraction in [9] [6,9].

### Takeaways for an Expert Researcher

- Closest spectral method usage is [1]’s spectral clustering for microservice identification, but it is not normalized/directed and is evaluated on cohesion/coupling—not on propagation or stability [1].
- Most studies rely on centrality features to predict faults or changes; they do not bridge to cascade theory or spectral thresholds and thus cannot provide actionable βρ(A) guidance or susceptibility bounds [2,3,4,5,6,7,9].
- If the aim is to compute spectra of real, directed, weighted dependency graphs and test cascade predictions with βρ(A) thresholds and resolvent/exp(A) features against observed propagation, none of the listed works fulfill that brief; they collectively motivate data pipelines (graph extraction, weighting, VCS/bug linkage) but leave core spectral-cascade validation open [1,2,3,4,5,6,7,9].

## Timeline

### Timeline and evolution of ideas

- 2012–2013: Dependency networks and centrality for software analytics
  - Recommendation of “central” classes from class-level dependency graphs, using PageRank, Markov centrality, and flow models, with developer validation; both directed and undirected variants explored, edge-type selection emphasized; tooling mentions (ConQAT) but no cascade or spectral-radius analysis [6].
  - Bug prediction from dependency networks using centralities (degree, betweenness, eigenvector, PageRank, HITS) on class-level directed graphs; validation via fixed-bug data; again, no spectral radius, Laplacians, or cascade thresholds [4].
  - A contemporaneous thread on “error propagation analysis” in software networks appears, but details are not available in the provided material [10].
  - A “cascading failure analysis” concept is present in 2014, hinting at dynamics, but with no accessible abstract to gauge methods/validation [8].

- 2016: From basic centralities to structural units and weighted key-class measures
  - Dependence clusters operationalized as strongly connected components (SCCs) in function-level directed system dependence graphs; larger clusters linked to higher fault-proneness; network metrics evaluated within SCC subgraphs for predictive modeling; this is one of the first explicit uses of SCC structure at scale in this corpus [2].
  - Identification of key classes in weighted dependency networks, introducing h-index–style measures and validating against version-control change frequency; edges carry counts of dependency relations, moving beyond unweighted graphs, though still without spectral-radius or Laplacian analyses [7].

- 2018–2019: Weighted, PageRank-style influence and multi-relation integration
  - FunctionRank extends PageRank to invocation-weighted directed graphs using counts from dynamic traces; reports influential functions across versions; emphasizes weighted edges and dynamic data, but stops short of spectral or resolvent-based cascade models [5].
  - Tri-Relation Networks integrate developer–file contributions, file–file dependencies, and developer–developer collaboration; centralities on the combined network improve fault-proneness prediction over single-relation baselines; static dependencies extracted with industrial tools (Understand); no spectral-radius thresholds, Laplacians, or random-graph nulls [9].

- 2023: Spectral clustering enters microservice decomposition; centralities paired with OO metrics
  - Spectral clustering (Laplacian eigenvectors + k-means) applied to class-level graphs for microservice identification in legacy Java systems; focuses on decomposition quality rather than dynamics; uses unnormalized Laplacian on a constructed adjacency; no directed/normalized Laplacians or Cheeger-style analyses reported [1].
  - Empirical validation that combining object-oriented metrics with centralities (including eigenvector variants) improves fault-proneness prediction across versions/systems; direction sometimes removed/symmetrized for measures; remains within centrality–prediction paradigm, without cascade thresholds or spectral functions [3].


### Methodological trends and patterns

- Persistent reliance on centrality-based correlates of faults and importance
  - Across 2012–2023, the most common spectral-related tools are eigenvector-derived centralities (PageRank, eigenvector centrality, Markov centrality) applied to static dependency graphs to rank classes/files by “importance” or fault risk [6,4,7,5,3,9]. These works generally do not compute spectral radii, resolvents, or matrix functions tied to cascade sizes.

- Gradual enrichment of graph construction and weighting
  - Early works mixed dependency types and experimented with directed vs undirected representations [6,4]. Later papers incorporate weights from multiple static dependency counts [7], dynamic invocation frequencies [5], and multi-relational integration including co-change and developer relations [9].

- Structural decomposition advances precede directed spectral theory use
  - SCCs are used to define “dependence clusters” linked to faults [2], indicating awareness of reducibility and cycles. However, directed normalized Laplacians, Cheeger-type inequalities, and Hermitian surrogates for community detection are absent; spectral clustering is applied in an undirected/unnormalized fashion for microservice decomposition [1].

- Validation evolves but remains prediction-centric
  - Many studies validate via developer judgment [6], defect labels [4,3,9], or change frequency from VCS [7]. None in this set validate linear cascade models x_{t+1}=βA x_t against observed propagation events, nor test βρ(A)=1 thresholds, nor estimate resolvent-based susceptibility bounds.

- Limited scale and absence of random-graph baselines
  - Case studies span small-to-medium OSS projects (e.g., Tomcat, Ant, JUNG, cflow, several academic datasets) [4,7,5,3,6], with no industrial-scale ecosystems like Maven/npm/PyPI or the Linux kernel in this corpus. Comparisons to Erdős–Rényi or degree-preserving configuration models are not reported.

- Emergent use of “spectral” in tooling for decomposition rather than dynamics
  - The first explicit “spectral” method is for clustering in microservice identification [1], not for stability or cascade thresholds. Directed/normalized Laplacians and Fiedler/Cheeger analyses are not yet reflected in these empirical pipelines.


### Notable contributor clusters and their threads

- He and collaborators: centrality for bug prediction and weighted key-class identification
  - 2013 bug prediction from dependency-network centralities [4] and the 2016 weighted key-class measures correlated with VCS change frequency [7] form a coherent thread emphasizing practical network metrics and validation against defects/changes. This line foregrounds weighted directed graphs but does not engage with spectral radii, Laplacians, or cascade thresholds.

- Jürgens/Steidl and coauthors: centrality and flow for developer-informed class importance
  - The 2012 work blends PageRank/Markov centrality with a flow model for recommending central classes, evaluated by developers across multiple Java projects [6]. It establishes early practice in graph-based importance assessment but avoids spectral stability/dynamics.

- Xu/Baowen group and coauthors: dependence clusters (SCCs) and fault-proneness
  - The 2016 ASE paper advances the use of SCCs as dependence clusters and ties cluster size/membership to fault-proneness, incorporating a wide range of network metrics within SCC subgraphs [2]. This is a structural milestone that recognizes the role of cycles but still omits spectral thresholds or directed Laplacian theory.

- Wotawa and collaborators: multi-relational networks for fault prediction
  - The 2019 TRN integrates dependencies with developer interactions and contributions, yielding improved prediction performance [9]. This broadens the relational scope but further distances the line from pure dependency-graph spectral dynamics.

- Other threads
  - Function-level influence via PageRank variants on dynamic traces [5] suggests an interest in dynamic data, yet remains within centrality paradigms rather than resolvent/exp(A) propagation.


### Significance and implications for the field

- What has matured
  - Building directed, weighted dependency graphs and computing centralities to support prediction and prioritization is established practice across multiple groups and datasets [6,4,7,5,3,9].
  - Structural signals like SCCs/dependence clusters correlate with fault-proneness, suggesting cycles matter for risk [2].

- What remains largely unexplored relative to spectral cascade theory
  - Empirical computation and use of spectral radius ρ(A) on real directed, weighted dependency graphs; explicit cascade models x_{t+1}=βA x_t and resolvent-based susceptibility; validation of βρ(A)=1 thresholds against observed propagation events; and reporting of actionable stability thresholds with uncertainty are absent in these works.
  - Directed/normalized Laplacian analyses (Fiedler values, Cheeger-type bounds) for modularity/bottlenecks; spectral clustering with directed Laplacians or Hermitian surrogates; eigenvalue perturbation and pseudospectral robustness analyses; and matrix-function propagation (e.g., exp(A)) have not been adopted in the surveyed empirical studies.
  - Comparisons to degree-preserving nulls or scale-free baselines to quantify non-random structure are missing across the corpus.

- Likely near-term directions
  - Given the adoption of spectral clustering for microservice decomposition [1] and the widespread use of PageRank-like methods, a natural step is to incorporate:
    - Perron–Frobenius spectral-radius metrics and resolvent-based risk scoring into existing dependency-analysis pipelines.
    - Directed, normalized Laplacian toolchains for community detection and bottleneck diagnosis, aligned with SCC condensation practices already in use [2].
    - Temporal analyses linking spectral metrics to observed co-change or defect propagation in VCS/issue trackers, with calibration of transmissibility β and confidence intervals.
    - Degree-preserving configuration-model nulls for rigorous baselining of spectral features.
  - Collaboration opportunities exist by bridging groups focused on centrality/weighted dependencies [4,7,5,3] and those emphasizing structural SCC-based risk [2] with modern network-science toolkits for directed spectra and cascades.

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [37] | 0.52 | 1% | Predicting defects using network analysis on dependency graphs | Thomas Zimmermann and Nachiappan Nagappan | 2008 ACM/IEEE 30th International Conference on Software Engineering | 2008 | 579 | [2, 3, 4, 7, 9, 12, 13] |
| [281] | 0.33 | 0% | Can developer-module networks predict failures? | M. Pinzger, ..., and Brendan Murphy | N/A | 2008 | 274 | [2, 4, 7, 9, 11] |
| [247] | 0.22 | 0% | Graph-based analysis and prediction for software evolution | P. Bhattacharya, ..., and M. Faloutsos | 2012 34th International Conference on Software Engineering (ICSE) | 2012 | 223 | [4, 5, 7] |
| [169] | 0.22 | 0% | Network Versus Code Metrics to Predict Defects: A Replication Study | Rahul Premraj and Kim Herzig | 2011 International Symposium on Empirical Software Engineering and Measurement | 2011 | 82 | [3, 4, 13] |
| [96] | 0.20 | 0% | Empirical Analysis of Object-Oriented Metrics and Centrality Measures for Predicting Fault-Prone Classes in Object-Oriented Software | Alexandre Ouellet and M. Badri | N/A | 2019 | 3 | [3] |
| [541] | 0.20 | Not measured | A study on software fault prediction techniques | S. Rathore and Sandeep Kumar | Artificial Intelligence Review | 2019 | 149 | [3] |
| [32] | 0.19 | 2% | Studying the impact of dependency network measures on software quality | Thanh H. D. Nguyen, ..., and A. Hassan | 2010 IEEE International Conference on Software Maintenance | 2010 | 79 | [3, 9, 13, 18, 19] |
| [361] | 0.17 | 0% | Power-Laws in a Large Object-Oriented Software System | G. Concas, ..., and N. Serra | IEEE Transactions on Software Engineering | 2007 | 240 | [3, 4] |
| [6] | 0.15 | 20% | Using Network Analysis for Recommendation of Central Software Classes | Daniela Steidl, ..., and Elmar Jürgens | 2012 19th Working Conference on Reverse Engineering | 2012 | 42 | [4, 7] |
| [542] | 0.15 | Not measured | Use of relative code churn measures to predict system defect density | Nachiappan Nagappan and T. Ball | Proceedings. 27th International Conference on Software Engineering, 2005. ICSE 2005. | 2005 | 879 | [2, 9] |
| [209] | 0.15 | 0% | Empirical analysis of network measures for predicting high severity software faults | Lin Chen, ..., and Baowen Xu | Science China Information Sciences | 2016 | 18 | [3, 22] |
| [543] | 0.15 | Not measured | "Better Data" is Better than "Better Data Miners" (Benefits of Tuning SMOTE for Defect Prediction) | Amritanshu Agrawal and T. Menzies | ArXiv | 2017 | 96 | [3] |
| [55] | 0.14 | 1% | An Empirical Study on the Relation between Dependency Neighborhoods and Failures | Thomas Zimmermann, ..., and L. Williams | 2011 Fourth IEEE International Conference on Software Testing, Verification and Validation | 2011 | 33 | [4, 7] |
| [87] | 0.14 | 0% | Predicting failures with developer networks and social network analysis | Andrew Meneely, ..., and J. Osborne | N/A | 2008 | 260 | [4, 7, 9] |
| [544] | 0.14 | Not measured | Core and Periphery in Free/Libre and Open Source Software Team Communications | Kevin Crowston, ..., and J. Howison | Proceedings of the 39th Annual Hawaii International Conference on System Sciences (HICSS'06) | 2006 | 213 | [4, 7] |
| [153] | 0.12 | 0% | Validation of network measures as indicators of defective modules in software systems | Ayse Tosun Misirli, ..., and A. Bener | Proceedings of the 5th International Conference on Predictor Models in Software Engineering | 2009 | 93 | [3, 9, 13] |
| [31] | 0.11 | 2% | An empirical study on software defect prediction with a simplified metric set | Peng He, ..., and Yutao Ma | ArXiv | 2014 | 280 | [3] |
| [545] | 0.10 | Not measured | A Systematic Literature Review on Fault Prediction Performance in Software Engineering | T. Hall, ..., and S. Counsell | IEEE Transactions on Software Engineering | 2012 | 1045 | [3] |
| [4] | 0.10 | 26% | Using Software Dependency to Bug Prediction | Peng He, ..., and Lulu He | Mathematical Problems in Engineering | 2013 | 10 | [7, 18, 31] |
| [546] | 0.09 | Not measured | Towards identifying software project clusters with regard to defect prediction | Marian Jureczko and L. Madeyski | Proceedings of the 6th International Conference on Predictive Models in Software Engineering | 2010 | 537 | [3] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref. | Adjacency score | Topic Match | Title | Authors | Journal | Year | Total Citations | References These Foundational Papers |
|---|---|---|---|---|---|---|---|---|
| [126] | 0.01 | 0% | Using K-core Decomposition on Class Dependency Networks to Improve Bug Prediction Model's Practical Performance | YunHuan Qu, ..., and Ting Liu | IEEE Transactions on Software Engineering | 2021 | 42 | [32, 37, 153, 169, 209, 281] |
| [308] | 0.01 | 0% | Evaluating network embedding techniques’ performances in software bug prediction | Yu Qu and Heng Yin | Empirical Software Engineering | 2021 | 17 | [32, 37, 153, 169, 209, 281] |
| [331] | 0.01 | 0% | Network Embedding Techniques for Predicting Software Defects: A Review | Sweta Mehta, ..., and K. Patnaik | International Journal of Scientific Research and Management (IJSRM) | 2025 | 0 | [32, 37, 153, 169, 209, 281] |
| [247] | 0.01 | 0% | Graph-based analysis and prediction for software evolution | P. Bhattacharya, ..., and M. Faloutsos | 2012 34th International Conference on Software Engineering (ICSE) | 2012 | 223 | [37, 153, 169, 281] |
| [205] | 0.01 | 0% | Revisiting the Impact of Dependency Network Metrics on Software Defect Prediction | Lina Gong, ..., and S. Jiang | IEEE Transactions on Software Engineering | 2022 | 17 | [32, 37, 153, 169] |
| [186] | 0.01 | 0% | Empirical analysis of network measures for effort-aware fault-proneness prediction | Wanwangying Ma, ..., and Baowen Xu | Inf. Softw. Technol. | 2016 | 56 | [32, 37, 153, 169] |
| [209] | 0.01 | 0% | Empirical analysis of network measures for predicting high severity software faults | Lin Chen, ..., and Baowen Xu | Science China Information Sciences | 2016 | 18 | [32, 37, 153, 169] |
| [13] | 0.01 | 8% | Predicting Aging-Related Bugs Using Network Analysis on Aging-Related Dependency Networks | Fangyun Qin, ..., and Zhiping Shi | IEEE Transactions on Emerging Topics in Computing | 2023 | 6 | [32, 37, 153, 169] |
| [3] | 0.01 | 29% | Combining object‐oriented metrics and centrality measures to predict faults in object‐oriented software: An empirical validation | Alexandre Ouellet and M. Badri | Journal of Software: Evolution and Process | 2023 | 11 | [32, 37, 153, 169, 209] |
| [9] | 0.01 | 13% | Using Tri-Relation Networks for Effective Software Fault-Proneness Prediction | Yihao Li, ..., and F. Wotawa | IEEE Access | 2019 | 13 | [32, 37, 153, 281] |
| [4] | 0.01 | 26% | Using Software Dependency to Bug Prediction | Peng He, ..., and Lulu He | Mathematical Problems in Engineering | 2013 | 10 | [37, 169, 281] |
| [538] | 0.01 | 0% | HEDF: A Method for Early Forecasting Software Defects Based on Human Error Mechanisms | Fuqun Huang and L. Strigini | IEEE Access | 2021 | 13 | [37, 281] |
| [553] | 0.01 | Not measured | Continuous Software Bug Prediction | Song Wang, ..., and Nachiappan Nagappan | Proceedings of the 15th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM) | 2021 | 14 | [37, 281] |
| [554] | 0.01 | Not measured | Graph-based machine learning improves just-in-time defect prediction | Jonathan Bryan and P. Moriano | PLOS ONE | 2021 | 7 | [37, 281] |
| [439] | 0.01 | 0% | Adapting bug prediction models to predict reverted commits at Wayfair | Alexander Suh | Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering | 2020 | 2 | [37, 281] |
| [555] | 0.00 | Not measured | Survey of software defect prediction features | Shaoming Qiu, ..., and Liangyu Liu | Neural Comput. Appl. | 2024 | 1 | [37, 209] |
| [7] | 0.00 | 17% | An Improved Approach to Identifying Key Classes in Weighted Software Network | Yi Ding, ..., and Peng He | Mathematical Problems in Engineering | 2016 | 15 | [37, 281] |
| [383] | 0.00 | 0% | Progress on approaches to software defect prediction | Zhiqiang Li, ..., and Xiaoke Zhu | IET Softw. | 2018 | 203 | [209, 281] |
| [32] | 0.00 | 2% | Studying the impact of dependency network measures on software quality | Thanh H. D. Nguyen, ..., and A. Hassan | 2010 IEEE International Conference on Software Maintenance | 2010 | 79 | [37, 153] |
| [142] | 0.00 | 0% | Measuring Cohesion of Software Systems Using Weighted Directed Complex Networks | Jie Zhang, ..., and Fanghua Ye | 2018 IEEE International Symposium on Circuits and Systems (ISCAS) | 2018 | 4 | [32, 281] |