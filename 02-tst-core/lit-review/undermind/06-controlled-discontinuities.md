# Controlled experiments on code-comprehension scaling with discontinuities: humans vs AI

## Overview

The search found no study that directly measures time-to-correct-answer as a function of explicit discontinuity counts d for both humans and modern AI on identical code tasks, but it surfaced strong component evidence: humans incur substantial navigation and working-memory costs [2,4,5,6], while code LLMs show long-context failures (lost-in-the-middle) and dependency-utilization constraints [3,7,8], implying the field is poised for, but has not yet executed, the desired head-to-head scaling tests and crossover analyses.

### What matches your goal and what does not
- Strong components toward the target:
  - Human navigation overhead and WM limits predictive of superlinear costs:
    - ~35% of developer time is spent on the mechanics of navigation across files and views [2].
    - Working-set/recency predictors plateau near 10 items, consistent with bounded active context during navigation [4].
    - Program-tracing WM capacity around seven variable/value bindings; larger definition–use distances increase load and errors [6].
    - Frequent cross-file “cognitive shifting” associates with poorer student outcomes; intra-file movement does not show this penalty [5].
  - AI long-context limits and dependency utilization:
    - Code “needle-in-a-haystack” shows marked accuracy degradation with longer contexts and a center-position penalty (lost-in-the-middle) [3].
    - Dependency Invocation Rate (DIR) is strongly correlated with pass@1 on repo-level generation; retaining full dependency context helps [7].
    - Agent pipelines change error profiles and retrieval/action patterns; code agents substantially reduce syntax errors [8].
- Missing relative to your precise criteria:
  - No controlled, parity experiments that quantify d (or weighted D) and model T_h vs T_ai scaling on identical tasks [1,2,3,4,5,6,7,8,9,10].
  - No crossover points d*, no hybrid handoff timing/overhead evaluation, and no AI timing inclusive of tool latencies [1,2,3,4,5,6,7,8,9,10].
  - Limited transformer diagnostics tied to task outcomes beyond center-vs-edge placement [3].

### Evidence supporting human scaling mechanisms
- Navigation overhead and discontinuity costs:
  - Developers spend about one-third of time on navigation mechanics, frequently following dependency chains and revisiting code, indicating substantial overhead that plausibly grows with discontinuities [2].
  - Cross-file movements (“cognitive shifting”) correlate with worse performance for novices; within-file movement shows no such effect, isolating cross-boundary penalties [5].
- Working memory constraints and locality:
  - WM capacity during tracing is about seven bindings; increased definition–use distance elevates WM load and errors, directly linking dispersion to performance degradation [6].
  - Navigation strategies exhibit a working set saturation around ~10 items, consistent with bounded attention and reassembly costs [4].
- Mixed effects of structural decomposition:
  - Decomposing single functions into smaller ones did not universally improve comprehension time or accuracy [1].
  - Untangling change sets reduced false positives in code review but did not significantly affect time-to-understand/complete; it prompted more context-seeking along call chains [9].
- Tool-mediated navigation effects:
  - IDE tools shape strategy and time; tools like Stacksplorer led to more revisits in a limited subset of methods and faster completion for some tasks [4].
  - Traceability-enriched navigation improved change quality and altered navigation behavior, suggesting benefits from explicit links across discontinuities [10].

### Evidence supporting AI scaling mechanisms
- Long-context and placement effects in code:
  - Models show degraded accuracy as context length increases and suffer when critical evidence is in the middle of the context (lost-in-the-middle), indicating attention dilution and position effects in code, not just text [3].
- Dependency coverage vs raw length:
  - Higher DIR correlates with higher pass@1; preserving full dependency context outperforms truncated contexts, suggesting that selection/coverage, not just window size, governs success [7].
- Agent/tool mediation:
  - Detailed action logs reveal substantial differences in search/compile activity and that adding a code agent reduces syntax errors dramatically, underscoring the centrality of retrieval/navigation and tool latency in end-to-end pipelines [8].
- Notably absent:
  - Time-to-correct-answer for AI systems (raw LLMs, RAG tools, or agents) under controlled d; no W_eff estimation via distractor-controlled probes tied to task time [3,7,8].

### How discontinuities are (partially) operationalized in the literature
- Human-side proxies:
  - Call-graph distance and forward call depth in navigation sequences [4].
  - Cross-file vs within-file movements as a coarse discontinuity signal [5].
  - Definition–use distance as a locality/dispersion manipulation [6].
- AI-side proxies:
  - Dependency Invocation Rate (DIR) as a measure of cross-file/API dependency utilization [7].
  - Evidence placement (front/middle/back) and total context length in NIAH code stacks [3].
  - Agent retrieval/action counts across files and APIs [8].
- None of these directly count required context-reassembly jumps d along minimal evidence paths or relate them to time-to-correct-answer [1,2,3,4,5,6,7,8,9,10].

### Methodological gaps blocking direct tests of your scaling hypotheses
- No studies jointly:
  - Count d (and weighted D) via precomputed call/dataflow graphs and minimal evidence cut sets.
  - Enforce parity tasks for humans and AIs with identical required discontinuities.
  - Measure time-to-correct-answer with right-censoring and model scaling (exponential vs sublinear/log) with mixed-effects.
  - Include tool-latency and retrieval-selection timing for AI; instrument full navigation overhead N(d) for humans and AIs.
  - Estimate crossover d* and evaluate handoff overhead to validate hybrid protocols [1,2,3,4,5,6,7,8,9,10].

### Cautionary findings that refine experimental design
- “Smaller” or “more modular” is not automatically better for human comprehension [1], and untangling changes benefits review precision more than speed [9]; thus, experiments must manipulate measured d/D rather than crude structural surrogates.
- Tool choice is a first-order factor for both humans [4,10] and AIs [8]; include tool conditions and their latencies in end-to-end timing.

### Implications and concrete recommendations for the next studies
- Task construction and d/D measurement:
  - Precompute call/dataflow graphs to identify minimal evidence paths; count required jumps and assign weights to cross-file/API/dynamic-dispatch boundaries to derive D. Instrument IDEs to log file opens, jumps, searches, scrolling, and dwell times (N(d)) [2,4].
- Human conditions:
  - Stratify students vs professionals; manipulate definition–use distance, nesting depth, and fan-out while holding d fixed vs varied to separate WM from navigation effects [4,6].
  - Use survival/time-to-event modeling with right-censoring; fit multiplicative effects on log-time, expecting positive β1 with d for humans [1,4,6].
- AI conditions:
  - Evaluate frontier LLMs without tools, with retrieval/navigation, and as fine-tuned agents; log full tool latencies and retrieval quality. Include lost-in-the-middle probes and distractor-controlled W_eff estimation [3,7,8].
  - Report time-to-correct-answer inclusive of all think/retrieve/parse/infer steps; relate accuracy and time to DIR and counted d.
- Hybrid protocols and crossover:
  - Measure handoff overhead H (briefing artifacts, summary time, verification loops) and test protocols such as human-navigate/AI-summarize vs AI-navigate/human-validate. Estimate d* where T_h(d*) equals T_ai(d*), and identify regions where T_hybrid < min(T_h, T_ai).
- Species-specific code organization tests:
  - Human-optimized: co-locate dependent code and invariants to reduce D and definition–use distance [2,6].
  - AI-optimized: increase retrievability and salience (docstrings, call-graph keys, summaries) and align chunk boundaries with retrieval units; validate via DIR and lost-in-the-middle mitigations [3,7].

### Bottom line for decision-making
- The human literature provides solid mechanistic support for discontinuity-driven costs via navigation and working-memory constraints [2,4,5,6], while the AI literature documents long-context limitations and the primacy of dependency coverage [3,7,8]; however, the definitive head-to-head timing vs d with crossover/hybrid validation remains an open, tractable experiment that current methods can now credibly execute.

## Categories

### Scope and relevance overview

- This set spans three clusters:
  - Human cognition and navigation in code, with time/strategy/WM evidence but no explicit discontinuity counts d: [2,4,5,6,9,10], and a functional-decomposition trial [1].
  - AI long-context and repository-level utilization without time-to-correct-answer or human–AI parity designs: [3,7,8].
  - None of the papers directly satisfy the “precisely relevant” target (joint human–AI time-to-correct vs measured discontinuities with crossover analysis), but several provide strongly relevant components (navigation overhead and working memory for humans: [2,4,6]; long-context failure modes for LLMs in code: [3]; dependency utilization proxies for code LLMs: [7]; agent retrieval/action instrumentation: [8]).

### Comparative matrix: design, measures, and operationalization

| Ref | Population | Task domain | Primary metrics | Time-to-correct-answer? | Navigation/attention instrumentation | Discontinuity operationalization | Long-context probes | Tool/agent conditions | Key quantitative findings |
|---|---|---|---|---|---|---|---|---|---|
| [2] | Human (developers) | Debugging + enhancement on unfamiliar code | Time allocation, navigation behaviors, success | Partial (70-min sessions; time shares) | IDE telemetry; search/use patterns; overhead estimates | Not explicit d; dependency following noted | None | Eclipse tools used; search and navigation | ~35% of time spent on mechanics of navigation within/between files; frequent failed searches due to limited/misleading cues |
| [4] | Human | Small Java app maintenance; IDE tool variants | Task completion time, navigation sequences, strategy prediction | Yes (task completion time) | Method-level visit/revisit logs; micro-pattern models; working set proxies | Proxies: call-graph distance, forward call depth; no explicit d | None | Multiple navigation tools (Stacksplorer, Blaze, Call Hierarchy, etc.) | Recency/Working-Set model accuracy plateaus for list size >10 (proxy WM bound); Stacksplorer led to more revisits within limited method sets and faster completion than some alternatives |
| [5] | Human (students) | Exam programming across files | Movement within/between files; course performance | Not per-task T_correct; course performance association | Key-level logging of intra/inter-file moves | Proxy: cross-file moves as cognitive shifting; no d | None | Standard IDE use | Frequent cross-file moves associated with worse course performance; intra-file moves showed no such effect |
| [6] | Human | Program tracing | Time-to-completion, accuracy, WM errors | Yes | Restricted-focus viewer to log cursor attention; revisits as WM failures | Proxy: distance between def-use; no d | None | N/A | Participants can hold about seven variable/value pairs; colocating definitions near uses reduces WM load; substantial between-subject variability |
| [9] | Human (pros + grads) | Code review of tangled vs decomposed PRs | Defects found, false positives, time-to-understand/complete | Yes (boxplots; no significant difference) | Qualitative navigation observations | No d; notes chain-of-calls exploration | None | Real PR setting; decomposition manipulation | Decomposition reduced false positives; no significant effect on time or understanding; untangled induced more “context-seeking” across related classes/method chains |
| [10] | Human | Maintenance tasks with/without traceability navigation | Change quality; navigation behavior | Time not emphasized in summary | Same tool with traceability on/off; navigation altered | No d | None | Traceability navigation vs baseline search/tree | Traceability improved change quality and “fundamentally changed” navigation; instant benefit without training |
| [1] | Human | Comprehension of single vs decomposed functions | Reading time, description accuracy, behavior questions | Yes | Reading time recorded; no fine-grained nav | No d; structural manipulation (mono vs multi-function) | None | N/A | Functional decomposition did not universally improve comprehension; inconclusive effect on time/accuracy |
| [3] | AI (11 LLMs) | Needle-in-a-code-haystack bug line retrieval | Retrieval accuracy | No | None beyond prompt placement | No d; manipulates “needle depth” and context length | Yes: 500–16k tokens; center vs edges | No tools; base prompts | Accuracy degrades with longer contexts for many models; “lost-in-the-middle” effect (center placement worse); code NIAH much harder than text baselines |
| [7] | AI (18 CodeLLMs) | Repo-level code generation with tests | Pass@k; Dependency Invocation Rate (DIR) | No | Dependency extraction; execution logs | Proxy: DIR for cross-file/API use; no d | Context-length comparisons; no placement probes | Multi-round debugging; some long-context models | Strong correlation between pass@1 and DIR; instruction-tuned models use dependencies more; retaining full dependency context best; smaller contexts can mislead |
| [8] | AI agents | Reproducing algorithms in repos from papers | Execution accuracy; CodeBLEU; reasoning-graph accuracy; dependency recall; tool-call counts | No | Detailed agent tool-action logs | Proxies: recall of intra-file/cross-file/API deps; no d | None | Dual-agent system; search/compile tooling | Code agent reduces syntax errors from ≈80–83% to ≈24–29%; best execution accuracy ≈0.47; large differences in tool invocation profiles between “reasoning” vs non-reasoning setups |

Notes:
- Where “time-to-correct-answer” is marked “Yes,” the studies measured task completion time under correctness constraints, but none modeled scaling versus explicit, counted discontinuities d or estimated exponential vs sublinear forms [1,4,6,9].
- AI studies [3,7,8] report accuracy and behavior under long context or agent tools but omit time-to-correct-answer.

### Cross-cutting comparisons: what each paper uniquely contributes to the target hypotheses

- Human navigation overhead and working memory constraints
  - Direct overhead estimates: [2] quantifies that about 35% of developer time is spent on navigation mechanics within/between files, highlighting an empirical pathway for increasing T_h with discontinuities even without explicit d counts.
  - Working set/recency bounds: [4] shows navigation strategies align with a working set limit around 10 methods (plateau in recency/working-set predictors), and tool choice shifts strategy and time.
  - Capacity and locality in tracing: [6] directly estimates a WM capacity around seven variable/value bindings and shows increasing def–use distance (reduced locality) increases load and affects time/accuracy.
  - Cross-file movement cost signal: [5] links frequent cross-file shifting with worse overall performance; intra-file moves did not show this penalty.
  - Structure manipulations that don’t simply help: [1] finds decomposing into multiple functions does not universally reduce comprehension time or improve accuracy, cautioning against assuming that more boundaries reduce cognitive load.
  - Review context and decomposition: [9] shows that untangled changes reduce false positives and prompt more cross-entity/chain exploration, but did not significantly alter time-to-understand/complete, suggesting benefits may appear primarily in accuracy rather than speed for review tasks.
  - Traceability navigation benefit: [10] shows improved change quality and altered navigation with traceability; time impacts are not emphasized.

- AI long-context behavior and dependency utilization
  - Lost-in-the-middle in code: [3] demonstrates a pronounced center-placement deficit and accuracy degradation with longer contexts in code-specific NIAH tasks, consistent with long-range attention dilution.
  - Dependency utilization metric: [7] introduces DIR, showing that models that actually invoke cross-file/API dependencies tend to have higher pass@1; full dependency context helps, and smaller contexts can mislead.
  - Agent tool action telemetry and error profiles: [8] provides detailed logs of retrieval/compilation actions and shows substantial reduction in syntax errors when a code agent is present; large variance in tool usage profiles between reasoning vs non-reasoning agent setups.

- Missing elements for the target scaling model
  - No study in this set measures time-to-correct-answer as a function of counted discontinuities d for both humans and AIs on identical tasks [1,2,3,4,5,6,7,8,9,10].
  - No explicit estimation of human exponential scaling parameters α or AI sublinear/log scaling forms, no crossover d*, and no hybrid handoff timing [1,2,3,4,5,6,7,8,9,10].
  - No transformer attention attribution tied to code tasks with time outcomes beyond center-vs-edge probes in [3].

### Methodological comparison aligned to the desired evaluation dimensions

- Time-to-correct-answer as primary outcome
  - Present for humans: [1,4,6,9] (task completion times; [2] gives time shares rather than per-task T_correct).
  - Absent for AI: [3,7,8] (accuracy-only or behavior metrics).

- Discontinuity measurement (d or weighted D)
  - None of the studies count required context-reassembly jumps; several use proxies:
    - Call-graph distance/forward depth and within-file vs cross-file navigation: [4,5].
    - Dependency invocation/utilization (DIR): [7].
    - Needle placement depth and context length: [3].
    - Qualitative chain-of-calls exploration in reviews: [9].

- Navigation/retrieval instrumentation
  - Human IDE telemetry or detailed logs: [2,4]; cursor-based attention tracing via restricted-focus viewer: [6]; qualitative navigation notes: [9]; traceability toggle effect on navigation: [10].
  - AI agent/tool logs with counts and categories: [8]; execution logs and dependency extraction providing DIR: [7].

- Working memory and context switching
  - WM capacity and errors in code tracing: [6].
  - Working set/recency bounds in navigation strategies suggest an upper bound near 10 items: [4].
  - Cross-file cognitive shifting penalty signal: [5].
  - Quantified general navigation overhead (mechanical): [2].
  - None provide programming-specific interruption recovery times or direct 23-minute recovery measurement; treat [2,4,5,6] as relevant but not conclusive on macro-interruptions.

- Long-context transformer behavior and context packing
  - Code-specific long-context degradation and lost-in-the-middle: [3].
  - Context size vs performance and the importance of dependency coverage (not length per se): [7].
  - No direct context packing strategy ablations; no effective window W_eff estimates with distractor controls in this set.

### Convergences and divergences across studies

- Convergences supporting the human-scaling mechanism
  - Multiple lines of evidence indicate that dispersed context and cross-entity traversal impose measurable costs: navigation overhead (~35%) [2], WM capacity around seven bindings [6], working-set saturation near ~10 [4], and performance penalties linked to cross-file shifting [5].
  - These support the plausibility of superlinear or multiplicative time costs with increasing discontinuities, though no paper fits an exponential model.

- Convergences supporting AI limitations in long contexts
  - Lost-in-the-middle and length-related degradation in code retrieval tasks [3].
  - Performance correlates with actually invoking cross-file dependencies rather than raw context length [7].
  - Tool-augmented agents can dramatically change error profiles and retrieval action counts [8], implying that navigation tooling is a dominant factor in AI pipelines.

- Divergences and caveats
  - Structural decomposition does not uniformly help humans [1], and decomposition of changes affects accuracy (false positives) more than time in reviews [9].
  - Some tool choices for humans improve time and shape navigation (e.g., Stacksplorer) [4], while others mainly improve quality [10]; benefits are not uniform across tasks and tools.
  - AI studies currently prioritize accuracy; without time measures, comparative scaling claims versus humans remain unsupported.

### Relevance-to-goal mapping (compliance matrix)

- Strong components for human mechanisms:
  - Navigation overhead and strategy: [2,4]
  - WM capacity and locality: [6]
  - Cross-file shifting signal: [5]

- Strong components for AI mechanisms:
  - Long-context failure modes (code): [3]
  - Dependency utilization proxy: [7]
  - Agent retrieval/action telemetry: [8]

- Weak/negative or contextualized structure results:
  - Functional decomposition not uniformly beneficial: [1]
  - Decomposition in review improves precision, not time: [9]
  - Traceability improves quality; time impact not established here: [10]

- Missing with respect to the target:
  - Joint human–AI identical tasks with counted d and time-to-correct-answer; exponential vs sublinear fits; crossover d*; hybrid handoff timing and protocols [1,2,3,4,5,6,7,8,9,10].

### Implications for designing the next-stage experiments

- For human studies, adopt the instrumentation and WM-sensitive manipulations demonstrated in [2,4,6], and structure tasks to vary explicit evidence-path discontinuity counts (d) rather than generic decomposition as in [1].
- For AI studies, adapt placement/distractor controls from [3] and dependency invocation metrics from [7], while logging full tool latency and action traces as in [8], to estimate T_ai vs d and effective context utilization.
- Ensure parity: same tasks and required evidence paths for human and AI conditions (avoid the mismatch pitfalls highlighted by differences in these literatures).

## Timeline

### Timeline of Key Developments

- 2006 — Navigation overhead and dependency-seeking as dominant costs in maintenance
  - Foundational field/lab study showed developers spend ~35% of time on navigation mechanics, often following dependency chains and revisiting code to reconstruct context; tools both help and hinder navigation strategy [2]. This crystallized “context reassembly” as a central bottleneck and motivated tool-centric interventions.

- 2011 — Early evidence that traceability aids navigation and quality
  - Controlled experiment demonstrated that traceability-enriched navigation alters exploration patterns and improves change-task quality, suggesting structured links can reduce reassembly effort across discontinuities [10].

- 2013 — IDE tools shape navigation strategies and working set size
  - Controlled comparisons of IDE navigation tools revealed distinct exploration patterns, increased revisits in certain tools, and a plateau in “working set” around ~10 items, implying bounded active context during code navigation and differential efficiency by tool design [4].

- 2018 — Change decomposition alters context-seeking behavior in review
  - Untangling changes reduced false positives but not review time; reviewers in decomposed conditions undertook more context-seeking along call chains, reinforcing that dependency traversal is a core cognitive activity even when changes are localized [9].

- 2019 — Cross-file cognitive shifting correlates with poorer student performance
  - Key-logging analyses linked frequent inter-file switching to worse outcomes, while intra-file movement showed no such effect, aligning with the idea that discontinuity jumps incur extra cost for novices [5].

- 2021 — Direct quantification of working memory limits in program tracing
  - Controlled experiments estimated a WM capacity of about seven variable/value bindings, documented characteristic WM errors, and showed that colocating definitions and uses reduces load; provides mechanistic grounding for costs at abstraction boundaries and long-range dependencies [6].

- 2024 — Mixed signals on functional decomposition; repo-level AI dependency use; long-context failure modes for LLMs in code
  - Functional decomposition did not universally improve human comprehension time/accuracy in a tightly controlled setting, cautioning against simplistic “smaller is always better” prescriptions without context-aware structuring [1].
  - RepoExec introduced dependency-aware evaluation for code LLMs, showing that correctly invoking cross-file dependencies correlates with success; instruction tuning and multi-round debugging improve dependency utilization, but timing and head-to-head human comparisons were not assessed [7].
  - BICS established that locating a “needle” bug in large code contexts exhibits strong degradation with longer contexts and a center-position penalty (“lost in the middle”) for LLMs on code, highlighting long-range attention and placement effects; metrics were accuracy-centric rather than time-to-correct-answer [3].

- 2025 — Agentic pipeline instrumentation over end-to-end code reproduction
  - SciReplicate-Bench logged agent/tool actions, cross-file/API dependency recall, and error profiles in reproducing research-code pipelines, demonstrating large tool mediation effects and high syntactic/logic error rates without agent support; again, no timing to correct solution or human parity tasks [8].


### Evolving Methods and Measures

- From qualitative observation to instrumented navigation telemetry
  - Early work emphasized direct observation and interviews augmented by coarse timing [2,10]. Subsequent studies increasingly logged fine-grained navigation sequences, revisits, and model-based predictors of next-step navigation, enabling quantitative characterizations of strategies and bounded working sets [4].

- From global difficulty proxies to dependency- and discontinuity-informed designs
  - Studies shifted from broad “task difficulty” to explicit dependency traversal and context localization: reviewers’ call-chain exploration [9], inter-file switching penalties for novices [5], and WM load manipulations via definition–use distance [6]. However, explicit counting/weighting of “discontinuity” jumps (d) along minimal evidence paths has not been standardized across human studies.

- Emergence of AI evaluations that approximate discontinuities via dependency metrics and context placement
  - Repo-level benchmarks introduced dependency invocation rate (DIR) to approximate cross-file utilization [7]; long-context experiments in code probed position effects (front/middle/back), surfacing “lost in the middle” for code stacks [3]. Agentic evaluations began logging retrieval/navigation tool behaviors as proxies for cross-artifact jumps [8]. Time-to-correct-answer remains largely unmeasured.

- Statistical analysis progression
  - Early analyses used ANOVA and descriptive statistics for navigation measures [4,10]. More recent human studies examined error taxonomies and strategy classification with controlled manipulations [6]. AI studies focused on pass@k and retrieval accuracy [3,7,8], with limited survival/time modeling and no mixed-effects comparisons aligned to discontinuity counts.


### Clusters of Contributors and Influence

- Information seeking and navigation pioneers
  - Ko and collaborators’ 2006 study [2] is heavily cited and catalyzed a methodological lineage around dependency-following, navigational overhead, and the importance of environment/tool design for program comprehension. This thread influenced later tool-centric navigation studies [4,10] and context-seeking observations in review [9].

- IDE/tool-shaping of navigation behaviors
  - Borchers and colleagues’ CHI’13 work [4] provided a comparative framework for how navigation tools alter exploration, revisits, and effective working sets, tying UI affordances to cognitive load—an anchor for later working-memory analyses in code.

- Cognitive mechanism quantification
  - Hanrahan, Crichton, and colleagues’ 2021 CHI paper [6] quantified WM limits in program tracing and strategy differences, establishing a rigorous bridge between cognitive psychology and code comprehension. This provides a mechanistic basis for modeling discontinuity costs through binding limits and definition–use distances.

- Repository-level AI capabilities and context utilization
  - Teams behind RepoExec [7] and BICS [3] mark an AI-centric cluster probing cross-file dependency handling and long-context placement effects in code. The SciReplicate group further instrumented agent tool use and dependency recall at scale [8]. These collectively transition the field toward operationalizing AI navigation and retrieval, though they have not yet aligned with human–AI parity timing under shared discontinuity structures.


### Trends, Patterns, and Their Significance

- Convergence on dependency traversal as the central unit of comprehension
  - Across human studies (navigation logs, review behavior, inter-file switching penalties) and AI studies (DIR, needle placement), the key construct is traversal of dependency chains and the costs of reassembling context across boundaries [2,4,5,7,9]. This aligns closely with the desired operationalization of discontinuities.

- Growing mechanistic grounding for human limits; partial mechanistic views for AI
  - Human working memory limits and definition–use spacing now have direct empirical support in code tasks [6], reinforcing models where costs increase with nested bindings and cross-boundary jumps. AI mechanisms are identified indirectly via placement effects and dependency metrics [3,7], pointing to attention dilution and retrieval selection quality, but without unified measures like effective window W_eff or time-cost decomposition.

- Tool mediation as a first-order factor for both species
  - IDE affordances, traceability, and navigation tools measurably shift human strategies and effectiveness [4,10]; for AI, retrieval/planning agents dramatically change success rates and error profiles [7,8]. This underscores that any scaling study must include tool conditions as experimental factors.

- Mixed and context-dependent effects of decomposition
  - Functional decomposition did not uniformly improve human comprehension [1]; change decomposition reduced false positives but not time [9]. These results caution against equating “more modularization” with “less time,” emphasizing the need to measure actual discontinuity counts (d) and weighted discontinuity (D) rather than structural heuristics.

- Emerging attention to long-context phenomena in code
  - Evidence now documents “lost in the middle” patterns for code contexts [3], mirroring NL findings, and suggests context packing and placement strategies will be pivotal for AI code systems—an essential ingredient for modeling sublinear/logarithmic scaling with d.


### Current Gaps Relative to the Targeted Goal

- Missing head-to-head human vs. AI timing on identical, discontinuity-controlled tasks
  - None of the surveyed works measure time-to-correct-answer as a function of explicitly counted discontinuities (d) for both humans and modern LLMs (with/without tools) on the same tasks [1,2,3,4,5,6,7,8,9,10].

- Limited explicit measurement of discontinuities and navigation overhead
  - Human studies quantify navigation and WM proxy measures but stop short of defining d/D on minimal evidence paths and linking them to time via mixed-effects fits [2,4,5,6,9,10]. AI studies use dependency recall/placement but do not map to d or include end-to-end timing including tool latencies [3,7,8].

- Few transformer-specific diagnostics in code tied to task outcomes
  - Aside from center-vs-edge effects [3], there is little analysis of attention mass, effective window estimation with distractors, or ablation-based marginal utility of retrieved chunks in code tasks with correctness/time endpoints [7,8].


### Implications for the Future Research Trajectory

- Integrate d/D operationalization into instrumented parity experiments
  - Build on navigation telemetry [2,4,10], WM manipulations [6], and dependency metrics [7] to design tasks where minimal evidence paths and discontinuity counts are precomputed. Measure time-to-correct-answer and accuracy jointly for humans (students vs. professionals) and LLMs (raw, with retrieval, agentic), enabling direct tests of exponential vs. sublinear/log scaling.

- Couple human cognitive diagnostics with AI context-utilization probes
  - Combine WM-sensitive designs (definition–use distance, nesting/fan-out) [6] with AI “lost in the middle” and distractor-ablation protocols [3], estimating effective window W_eff and optimal context packing strategies for code.

- Make tool conditions first-class and time-inclusive
  - Reflecting strong tool effects on both humans and AIs [4,7,8,10], include tool latency, retrieval selection quality, and planning loops in end-to-end timing; evaluate hybrid protocols with explicit handoff overheads.

- Reassess modularization guidance through the lens of d
  - Given mixed decomposition outcomes [1,9], prioritize species-specific code organization: reduce D for humans (locality, colocated invariants) vs. increase retrievability and salient summaries for AI [1,7]. Future studies should quantify when these prescriptions diverge.

- Build benchmark suites that log discontinuity traversals and timing
  - Extend repo-level AI benchmarks to record per-jump retrieval/navigate actions, token usage, and ablation-based utility [7,8], and pair with matched human tasks with IDE instrumentation [2,4]; report survival curves, mixed-effects fits, and estimated crossover points d*.


### Summary of Milestones

- Navigation overhead quantified and dependency-following identified as central (2006) [2].
- Traceability and tool affordances shown to reshape navigation and improve quality (2011–2013) [10,4].
- Context-seeking and cross-file shifting linked to performance and review behaviors (2018–2019) [9,5].
- Working memory limits and definition–use distance effects measured in code tracing (2021) [6].
- AI-era benchmarks surface dependency utilization and long-context placement effects in code (2024–2025) [3,7,8].
- Decomposition benefits shown to be context-dependent rather than universal (2024) [1].

Collectively, these steps chart a path from qualitative insights about navigation and dependency traversal in humans toward instrumented, dependency-aware AI evaluations—setting the stage for the next phase: controlled, d-aligned human–AI timing studies that can test and model the proposed scaling laws and hybrid protocols.

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [212] | 0.30 | 0% | Evaluating Large Language Models Trained on Code | Mark Chen, ..., and Wojciech Zaremba | ArXiv | 2021 | 6183 | [3, 7, 8, 15, 16, 17, 19] |
| [48] | 0.17 | 2% | CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | Yangruibo Ding, ..., and Bing Xiang | ArXiv | 2023 | 143 | [7, 15, 16] |
| [101] | 0.15 | 1% | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | Tianyang Liu, ..., and Julian McAuley | ArXiv | 2023 | 187 | [7, 15, 16, 17] |
| [169] | 0.15 | 0% | EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code Repositories | Jia Li, ..., and Zhi Jin | ArXiv | 2024 | 55 | [15, 16, 17, 19] |
| [217] | 0.14 | 0% | Eye Movements in Code Reading: Relaxing the Linear Order | Teresa Busjahn, ..., and S. Tamm | 2015 IEEE 23rd International Conference on Program Comprehension | 2015 | 209 | [5, 6, 22, 29] |
| [83] | 0.14 | 1% | 40 Years of Designing Code Comprehension Experiments: A Systematic Mapping Study | Marvin Wyrich, ..., and S. Wagner | ACM Computing Surveys | 2022 | 24 | [1] |
| [23] | 0.13 | 5% | Tracing software developers' eyes and interactions for change tasks | Katja Kevic, ..., and Thomas Fritz | Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering | 2015 | 104 | [5, 13, 22, 33] |
| [126] | 0.12 | 0% | Measuring Program Comprehension: A Large-Scale Field Study with Professionals | Xin Xia, ..., and Shanping Li | IEEE Transactions on Software Engineering | 2018 | 277 | [1, 22] |
| [120] | 0.12 | 0% | Measuring and modeling programming experience | J. Siegmund, ..., and Stefan Hanenberg | Empirical Software Engineering | 2013 | 143 | [1, 13] |
| [180] | 0.12 | 0% | An eye-tracking study on the role of scan time in finding source code defects | Bonita Sharif, ..., and Jonathan I. Maletic | Proceedings of the Symposium on Eye Tracking Research and Applications | 2012 | 152 | [9, 13, 23, 24] |
| [2] | 0.12 | 36% | An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks | Amy J. Ko, ..., and H. Aung | IEEE Transactions on Software Engineering | 2006 | 662 | [5, 13, 22, 23, 29] |
| [14] | 0.11 | 11% | Analyzing individual performance of source code review using reviewers' eye movement | H. Uwano, ..., and Ken-ichi Matsumoto | Proceedings of the 2006 symposium on Eye tracking research & applications | 2006 | 183 | [9, 11, 13, 23] |
| [358] | 0.10 | 0% | ExecRepoBench: Multi-level Executable Code Completion Evaluation | Jian Yang, ..., and Junyang Lin | ArXiv | 2024 | 11 | [17] |
| [157] | 0.10 | 0% | RULER: What's the Real Context Size of Your Long-Context Language Models? | Cheng-Ping Hsieh, ..., and Boris Ginsburg | ArXiv | 2024 | 361 | [3] |
| [224] | 0.10 | 0% | HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self-invoking Code Generation | Zhaojian Yu, ..., and Xiao-Ping Zhang | ArXiv | 2024 | 12 | [19] |
| [133] | 0.10 | 0% | M2rc-Eval: Massively Multilingual Repository-level Code Completion Evaluation | Jiaheng Liu, ..., and Bo Zheng | ArXiv | 2024 | 9 | [15] |
| [155] | 0.09 | 0% | LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K | Tao Yuan, ..., and Yu Wang | ArXiv | 2024 | 53 | [3] |
| [67] | 0.09 | 1% | Developers' code context models for change tasks | Thomas Fritz, ..., and Christoph Bräunlich | Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering | 2014 | 48 | [13, 22, 23, 33, 44] |
| [39] | 0.09 | 2% | Maintaining mental models: a study of developer work habits | Thomas D. Latoza, ..., and R. Deline | Proceedings of the 28th international conference on Software engineering | 2006 | 743 | [2, 13, 22] |
| [202] | 0.07 | 0% | What Drives the Reading Order of Programmers? An Eye Tracking Study | Norman Peitek, ..., and S. Apel | 2020 IEEE/ACM 28th International Conference on Program Comprehension (ICPC) | 2020 | 37 | [6, 22] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref. | Adjacency score | Topic Match | Title | Authors | Journal | Year | Total Citations | References These Foundational Papers |
|---|---|---|---|---|---|---|---|---|
| [237] | 0.06 | 0% | Eye movements in code review | Andrew Begel and Hana Vrzakova | Proceedings of the Workshop on Eye Movements in Programming | 2018 | 36 | [14, 23, 67, 152, 180, 217, 265, 293] |
| [13] | 0.05 | 12% | Eyes on Code: A Study on Developers’ Code Navigation Strategies | Zohreh Sharafi, ..., and Westley Weimer | IEEE Transactions on Software Engineering | 2022 | 16 | [2, 14, 23, 67, 180, 265] |
| [22] | 0.04 | 6% | Developer's Cognitive Effort Maintaining Monoliths vs. Microservices - An Eye-Tracking Study | Georg Simhandl, ..., and Uwe Zdun | 2023 30th Asia-Pacific Software Engineering Conference (APSEC) | 2023 | 0 | [2, 23, 67, 217] |
| [242] | 0.04 | 0% | Determining Differences in Reading Behavior Between Experts and Novices by Investigating Eye Movement on Source Code Constructs During a Bug Fixing Task | Salwa Aljehane, ..., and Jonathan I. Maletic | ACM Symposium on Eye Tracking Research and Applications | 2021 | 20 | [14, 23, 152, 180, 217, 265] |
| [23] | 0.04 | 5% | Tracing software developers' eyes and interactions for change tasks | Katja Kevic, ..., and Thomas Fritz | Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering | 2015 | 104 | [2, 14, 67, 152, 180, 265, 293] |
| [538] | 0.04 | 0% | A Cookbook for Eye Tracking in Software Engineering | Lisa Grabinger, ..., and J. Mottok | Proceedings of the 6th European Conference on Software Engineering Education | 2025 | 0 | [14, 23, 152, 180, 217] |
| [551] | 0.04 | Not measured | PENGARUH PERALIHAN BAHASA KOMPUTER PADA REPLIKASI EYE TRACKING | Yosep Aditya Wicaksono, ..., and Edy Siswanto | Informatika: Jurnal Teknik Informatika dan Multimedia | 2023 | 0 | [14, 23, 180, 217, 265] |
| [230] | 0.04 | 0% | Studying Developer Eye Movements to Measure Cognitive Workload and Visual Effort for Expertise Assessment | Salwa Aljehane, ..., and Jonathan I. Maletic | Proceedings of the ACM on Human-Computer Interaction | 2023 | 15 | [14, 23, 152, 217, 265] |
| [260] | 0.04 | 0% | Representational Learning Approach for Predicting Developer Expertise Using Eye Movements | Sumeet Maan | Journal Not Provided | 2020 | 2 | [23, 33, 152, 217, 265] |
| [40] | 0.03 | 2% | An eye tracking study assessing the impact of background styling in code editors on novice programmers’ code understanding | Kang-il Park, ..., and Michael Kölling | Proceedings of the 2023 ACM Conference on International Computing Education Research - Volume 1 | 2023 | 8 | [14, 23, 180, 217] |
| [552] | 0.03 | Not measured | Revisión sistemática del enfoque teórico y las variables oculomotoras registradas en estudios de seguimiento ocular en el área de ciencias de la computación e ingeniería en sistemas | L. Villalobos and Á. D. L. Ossa | N/A | 2020 | 0 | [23, 180, 217] |
| [198] | 0.03 | 0% | Assessing the Effect of Programming Language and Task Type on Eye Movements of Computer Science Students | Niloofar Mansoor, ..., and Bonita Sharif | ACM Transactions on Computing Education | 2023 | 5 | [2, 14, 180, 217] |
| [342] | 0.03 | 0% | Through (Tracking) Their Eyes: Abstraction and Complexity in Program Comprehension | Philipp Kather, ..., and J. Vahrenhold | ACM Transactions on Computing Education (TOCE) | 2021 | 20 | [2, 14, 180, 217] |
| [553] | 0.03 | Not measured | Analysis of software developers’ coding behavior: A survey of visualization analysis techniques using eye trackers | D. Davis and F. Zhu | Computers in Human Behavior Reports | 2022 | 12 | [14, 23, 217] |
| [554] | 0.03 | Not measured | A practical guide on conducting eye tracking studies in software engineering | Zohreh Sharafi, ..., and M. Crosby | Empirical Software Engineering | 2020 | 97 | [14, 180, 217, 265] |
| [555] | 0.02 | Not measured | The Expert’s View: Eye Movement Modeling Examples in Software Engineering Education | Florian Hauser, ..., and V. K. Nadimpalli | Proceedings of the 5th European Conference on Software Engineering Education | 2023 | 3 | [14, 180, 217] |
| [497] | 0.02 | 0% | Examples of Unsuccessful Use of Code Comprehension Strategies: A Resource for Developing Code Comprehension Pedagogy | Colleen M. Lewis | Proceedings of the 2023 ACM Conference on International Computing Education Research - Volume 1 | 2023 | 7 | [14, 180, 217] |
| [321] | 0.02 | 0% | Visual Expertise in Code Reviews: Using Holistic Models of Image Perception to Analyze and Interpret Eye Movements | Florian Hauser, ..., and H. Gruber | Proceedings of the 2023 Symposium on Eye Tracking Research and Applications | 2023 | 7 | [14, 180, 217] |
| [270] | 0.02 | 0% | Analyzing and Interpreting Eye Movements in C++: Using Holistic Models of Image Perception | Florian Hauser, ..., and Hans Gruber | Proceedings of the 2024 Symposium on Eye Tracking Research and Applications | 2024 | 3 | [14, 180, 217] |
| [463] | 0.02 | 0% | Characterizing Task-Relevant Information in Natural Language Software Artifacts | Arthur Marques, ..., and G. Murphy | 2020 IEEE International Conference on Software Maintenance and Evolution (ICSME) | 2020 | 5 | [23, 217] |