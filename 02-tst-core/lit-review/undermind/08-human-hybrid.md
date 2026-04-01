# Empirical/formal models of hybrid human–AI software teams beating solo baselines

## Overview

Across post‑2020 studies we found no direct demonstrations of true complementarity (i.e., T_hybrid < min(T_human, T_AI)); instead, recent RCTs and field deployments show mixed time effects for AI‑assisted coding—speedups in some greenfield contexts [2,3] and slowdowns in mature OSS work [4]—with coordination/verification overheads often dominating outcomes, especially in code‑review workflows [1,6,7,9].

### What is established vs. missing relative to the target goal
- Established
  - AI assistance can reduce individual time on greenfield tasks in controlled enterprise/professional settings (≈21–31% faster) [2,3].
  - In real OSS issue work by experienced contributors, allowing state‑of‑the‑art copilots can increase time to completion (≈+19%) despite higher output volume expectations [4].
  - Code‑review assistance frequently adds measurable coordination overhead (longer PR closure times, per‑suggestion inspection costs) even when suggestions are implemented [1,6,7,9].
  - Interface choices that re‑target or gate AI outputs measurably shift human time burdens (e.g., showing patches to authors instead of reviewers reduced reviewer slowdowns) [1].
- Missing (relative to the brief)
  - No study provides AI‑alone gold‑standard timing or validated proxy sufficient to test T_hybrid < min(T_human, T_AI) on the same tasks [1,2,3,4,5,6,7,8,9,10].
  - No empirically calibrated formal models of comparative advantage, optimal handoff granularity, or explicit T_explain/T_understand/T_verify decomposition; trust‑update dynamics are not quantitatively modeled [1,2,3,4,5,6,7,8,9,10].
  - Sparse stratification across all requested task categories and units of analysis; pair/small‑team hybrid dynamics remain largely untested beyond PR‑level telemetry [6,9].

### Time outcomes by task and setting
- Greenfield feature implementation (individual+AI)
  - Preregistered two‑phase study with ≈95% professionals: −30.7% median completion time with AI in Phase 1; modest, non‑significant speedup when evolving AI‑produced artifacts by new developers [2].
  - Enterprise RCT with 96 Google engineers: ≈−21% developer time with AI features on a complex repo‑realistic task (CI wide) [3].
- Real‑world OSS tasks (individual+AI)
  - Field RCT on 246 real issues from large mature repos: +19% time with modern assistants (Cursor Pro, Claude 3.5/3.7), despite participants forecasting speedups; LoC/hr +47% (p=0.16) but no time savings [4].
- Code review workflows
  - Production agent at scale: initial safety RCT found reviewers took >5% longer when shown AI patches; UX changed to author‑targeting to mitigate reviewer overhead [1].
  - Industrial deployment (GPT‑4 Turbo review agent): longer PR closure times despite ~74% of automated comments being acted on and perceived usefulness [6].
  - Live study (Mozilla/Ubisoft): median 43 s reviewer inspection per AI comment; acceptance ≈7–8% overall, higher for refactoring (≈18%) than functional issues (≈5%) [7].
- Testing and security tasks
  - Unit‑test support: higher coverage and defect detection with interactive LLM assistance, but more false positives; efficiency improved within time‑box [5].
  - Security programming with intentional HiLDe interface: fewer vulnerabilities but slower completion (time–quality trade‑off) [10].

### Coordination and verification overhead: measured components
- Per‑artifact inspection costs: ≈43 s median per generated review comment [7].
- System‑level coordination impacts:
  - PR closure time increased with automated review agents [6].
  - Project‑level Copilot usage associated with ≈8% higher integration coordination time (more code discussions) alongside modest contribution increases (+5.9%) [9].
- Interface‑mediated shifts:
  - Reviewer‑facing AI patches increased reviewer time; author‑targeting reduced the penalty [1].
  - LLM‑as‑a‑judge filtering reduced irrelevant comments but acceptance remained low, suggesting residual mismatch in timing and observability [7].

### Quality and error trade‑offs
- Security: intentional critical‑decision‑point interfaces reduce vulnerabilities at a time cost [10].
- Testing: more defects found and higher coverage, but increased false positives that can inflate verification/rework [5].
- Code review: higher acceptance for refactoring vs functional comments indicates differential observability/verification ease [7]; production agents perceived as useful but sometimes trigger recursive/faulty feedback cycles [6].
- Project‑level quality: no detectable change reported in one Copilot telemetry study (metric unspecified) [9].

### Task‑ and workflow‑specific implications
- Greenfield with strong scaffolds and controlled environments: AI assistance tends to speed individual work [2,3].
- Mature, complex repos with heavy coordination and high developer familiarity: AI can slow end‑to‑end delivery, likely due to handoff/verification overhead and reliability/latency issues [4].
- Code review: without strong oracles, AI‑generated comments often add T_understand/T_verify; use author‑side patching and pre‑submission assistance to shift verification to the party best positioned to act quickly [1,6,7].
- Testing: leverage AI to expand coverage and candidate tests, but budget time for triage of false positives; integrate stronger oracles (property tests/types) to reduce rework [5].

### Alignment (and gaps) with the requested modeling agenda
- Comparative advantage and optimal handoff granularity
  - Empirical signals support the importance of handoff targeting and chunking (e.g., author vs reviewer; refactoring vs functional comments) [1,7], but no studies calibrate formal allocation models or report optimal turn sizes.
- Coordination overhead decomposition
  - Several studies surface components of T_handoff (inspection times, PR closure effects, integration discussions) [1,6,7,9], yet none decompose T_explain/T_understand/T_verify with calibrated parameters.
- Trust calibration dynamics
  - Behavioral evidence of miscalibration: experts and participants overpredicted AI speedups in OSS tasks [4]; reviewer slowdowns when exposed to patches [1]; low acceptance of generated comments despite filtering [7]. No explicit Bayesian/delta‑rule updates or validated interventions with quantitative trust metrics were reported.
- Cognitive load, convergence, error propagation, longitudinal effects
  - No direct cognitive‑load instrumentation (NASA‑TLX/physio) in this set; iterative convergence and downstream defect propagation are only indirectly visible (false positives, recursive reviews) [5,6,7]. Limited longitudinal insights; one study suggests maintainability benefits for habitual AI users [2].

### Units of analysis and populations
- Predominantly individual+AI studies with professional developers [2,3,4,5,8,10]; enterprise engineers [3]; experienced OSS contributors [4].
- Team/project‑level telemetry shows coordination effects and role heterogeneity (core vs peripheral) [9].
- Pair‑programming and small‑team controlled trials with explicit coordination protocols are absent.

### Evidence‑backed workflow guidelines
- Gate and target AI outputs to minimize reviewer verification load (prefer author‑side application of fixes; pre‑submission checks) [1,7].
- Use strong oracles to enable macro‑handoffs; otherwise, tighten loops with smaller chunks and structured prompts to contain rework [5,6,7].
- Monitor and budget for coordination overhead when deploying review agents (expect longer PR closure initially; track inspection time, acceptance, and recursive comment loops) [6,7,9].
- In high‑stakes domains (security), adopt interfaces that increase deliberate reflection even at a time cost [10].
- Expect heterogeneous treatment effects; instrument environments to detect when AI slows work (e.g., mature repos, high familiarity tasks) and adapt policies accordingly [4].

### Critical gaps and priorities for next studies
- Add AI‑alone baselines: measure autonomous or proxy T_AI (e.g., time‑to‑first‑passing test/patch on fixed hardware) alongside T_h and T_hybrid to enable tests of T_hybrid < min(T_h, T_AI) [1,2,3,4,5,6,7,8,9,10].
- Calibrate handoff models: instrument T_explain/T_understand/T_verify and rework loops; report handoff counts and granularity to estimate overhead multipliers [1,6,7,9].
- Trust calibration experiments: implement Bayesian or delta‑rule reliance policies with uncertainty annotations and verification gates; quantify over‑/under‑reliance and intervention effects [1,4,7].
- Stratify by task type and unit: run blocked RCTs across greenfield, bug‑fix, review, tests, refactoring; include pair/small‑team conditions with defined ownership of explanation vs verification [2,3,4,5,6,7,9,10].
- Map crossover points d*: tag task difficulty/observability and estimate T_h(d), T_ai(d), T_hybrid(d) to identify d* and hybrid‑advantage regions [2,3,4,7].
- Economic utility: report time adjusted by downstream defect costs and rework to compare quality–time trade‑offs fairly [5,6,7,10].

## Categories

### Cross-Study Synthesis: Where, When, and Why Human–AI Hybrids Help or Hurt

- Net time effects diverge by task and workflow:
  - Greenfield feature work by individual professionals shows moderate-to-large speedups with AI assistance (≈21–31% faster) in controlled RCTs inside enterprise contexts [2,3]. In contrast, experienced OSS contributors working on real issues in mature repos were ≈19% slower when allowed to use state-of-the-art AI tools [4].
  - Code review with AI frequently increases coordination time (longer PR closure, inspection time), even when suggestions are often acted on, consistent with nontrivial T_understand/T_verify overhead [1,6,7].
  - Security-focused, intentional human-in-the-loop interfaces reduce vulnerabilities at the cost of slower completion, evidencing an explicit efficiency–quality trade-off [10].
  - Unit test generation can raise defect detection and efficiency but introduces false positives, which can increase downstream verification/rework load [5].
- Coordination overhead is consistently material and measurable:
  - Explicit timing of review inspection (median 43 s per generated comment) and low acceptance rates imply significant T_understand with many unproductive paths [7].
  - Organization-scale telemetry reveals longer PR closure with automated review agents, attributed by practitioners to faulty/irrelevant comments and recursive review cycles [6], and an RCT safety trial found >5% longer reviewer time when exposing AI-generated patches to reviewers (leading to a UX redesign to avoid this) [1].
  - At project scale, Copilot usage is associated with increased coordination time for integration (~8%), even with net gains in code contribution volumes [9].
- Quality effects depend on scaffolds and interaction design:
  - Security-oriented human-in-the-loop decoding reduces vulnerabilities via structured choice points [10].
  - LLM-assisted unit test writing increases coverage and defect detection but also false positives [5].
  - Code-review assistance shows low acceptance for functional issues but higher for refactoring (≈18% acceptance), suggesting differential observability and verifiability by comment type [7]; production agents see high “accounted for” rates but still lengthen PR closure times [6].
- Evidence for true complementarity (T_hybrid < min(T_human, T_AI)) is generally not established:
  - None of the studies provide gold-standard AI-alone time baselines; a few provide only proxy measures (e.g., inspection time per AI suggestion) [1,6,7]. As such, most results are about AI-assisted vs human-alone, not hybrid vs both human-alone and AI-alone head-to-head [2,3,4,5,6,7,9,10].

---

### Study Design, Populations, Tasks, and Tools

| Study | Population (experience) | Unit of analysis | Task category | Setting | AI tooling/model named | Interaction modality |
|---|---|---|---|---|---|---|
| [2] | N=151; ~95% professional devs | Individual+AI | Greenfield feature addition; subsequent evolution by new devs | Controlled, preregistered experiment | “AI assistant” (not specified in excerpt) | Interactive assistance during implementation |
| [3] | n=96 full-time Google SWEs | Individual+AI | Complex enterprise task incl. writing, build, test | Enterprise RCT (internal infra) | Three internal AI features | Integrated IDE/infrastructure features |
| [4] | 16 experienced OSS contributors (~5 yrs); 246 tasks | Individual+AI | Real OSS issues on large mature repos | Field RCT (task-level randomization) | Cursor Pro; Claude 3.5/3.7 Sonnet | IDE/chat assistants as chosen |
| [5] | N=30 (experience not specified in excerpt) | Individual+AI | Unit test generation for Java with seeded defects | Time-boxed controlled experiment | ChatGPT, GitHub Copilot (examples) | Interactive test authoring |
| [6] | 238 practitioners; 3 focal projects | Team/project | Code review on PRs | Industry deployment case study | Qodo PR Agent (GPT-4 Turbo) | Automated review bot on PRs |
| [7] | Mozilla and Ubisoft developers | Reviewer+tool | Code review comments | Live user study in two orgs | GPT-4o with RAG, CoT, memory; LLM-as-a-Judge | Generated comments filtered then shown |
| [8] | 29 professional developers | Individual reviewer | Code review | Controlled experiment | Specific model not named in excerpt | Auto-generated reviews |
| [9] | OSS developers (core vs peripheral stratification) | Developer and project | Collaborative development (mixed) | Observational telemetry study | GitHub Copilot (usage logs) | IDE copilot usage inferred |
| [10] | N=18 developers | Individual+AI | Security programming tasks | Within-subjects lab study | HiLDe (human-in-the-loop decoding) | Critical-decision-point exploration |
| [1] | Meta-scale reviewers/authors | Reviewer and author | Code review fixes to comments | Production deployment + RCT safety trial | Meta-tuned Llama (LargeLSFT) vs GPT‑4o offline | Auto-generated patches; UX modified to author-only |

Notes:
- Experience stratification is explicit in [2,3,4,8]; role stratification (core vs peripheral) in [9].
- Task strata cover greenfield [2,3,4], unit testing [5], code review generation/fix [1,6,7,8], and security coding [10].

---

### Primary Outcome Comparisons: Time and Quality

| Study | Time-to-completion effect (direction/size) | Quality/defects outcome | Notable coordination/verification observations |
|---|---|---|---|
| [2] | Phase 1: median −30.7% completion time with AI; posterior mean ≈ −60% for habitual users (speedup); Phase 2 evolution: modest, non-significant speedup | Slightly higher average CodeHealth; significant increase for habitual AI users in Phase 2 | No handoff decomposition reported |
| [3] | ≈ −21% developer time with AI (CI wide) | Not reported in excerpt | RCT; heterogeneity: devs with more coding hours/day gained more |
| [4] | +19% completion time with AI allowed (slower), despite participants predicting speedups | LoC/hr +47% (p=0.16); no defect outcomes in excerpt | Analysis of 20 setting/tool/task properties; high repo familiarity hypothesized to affect results |
| [5] | Improved testing efficiency in interactive condition (time-boxed) | Higher coverage and defect detection; increased false positives | Interactive loop; no detailed time breakdown provided |
| [6] | Longer PR closure times with automated reviews | Practitioners report useful bug detection and quality awareness | ~73.8% automated comments “accounted for”; faulty/irrelevant comments and recursive reviews noted |
| [7] | Median 43 s reviewer time per generated comment | Acceptance: 8.1% (Mozilla), 7.2% (Ubisoft); higher for refactoring (≈18%) than functional (≈5%); similar follow-up revision rates to human comments | LLM-as-a-Judge filters; mismatch with review timing hypothesized |
| [8] | Review time measured; specific direction/size not provided in excerpt | Review quality and reviewer confidence measured | Professional reviewers; detailed metrics not in excerpt |
| [9] | Project contributions +5.9% net; coordination time for integration +8% | No detectable change in code quality (metric unspecified) | Core devs benefit more; coordination overhead rises more for peripheral devs |
| [10] | Slower task completion with HiLDe vs baseline AI | Fewer vulnerabilities; improved catching/correcting vulnerabilities | Intentional reflection increased; explicit efficiency–quality trade-off |
| [1] | RCT safety trial: reviewers took >5% longer when AI patches were shown; led to UX change to show patches to authors instead | Offline exact-match patch rate 68% (LargeLSFT), +9pp over GPT‑4o; better API modernity | Production deployment at scale; reviewer exposure increased T_understand/T_verify; workflow change mitigated |

Caveats:
- Only [2,3,4,10] explicitly report time-to-completion for end-to-end tasks; code-review studies report PR closure time or per-suggestion inspection time [1,6,7], which proxy coordination overhead rather than end-to-end implementation time.
- Quality is multi-faceted; several studies provide mixed signals (e.g., more defects found but more false positives in testing [5]).

---

### Evidence Against/For Hybrid Superiority Over Both Human and AI Alone

- AI-alone baselines:
  - None of the studies report gold-standard autonomous AI completion times on the same tasks; thus, strict tests of T_hybrid < min(T_human, T_AI) are absent [1,2,3,4,5,6,7,8,9,10].
  - Proxy AI-alone signals appear only indirectly (e.g., acceptance rates, time to inspect suggestions, offline patch exact-match rates) [1,6,7], which are insufficient to compute T_AI or T_verify for end-to-end tasks.
- Implication:
  - Claims should be limited to AI-assisted vs human-alone deltas or coordination overhead measurements. Demonstrations of true complementarity vs substitution remain open for the surveyed set.

---

### Handoff and Coordination Overhead: What’s Measured

- Direct timing slices:
  - Per-suggestion inspection time: median 43 s per generated review comment [7].
  - Reviewer time increase when exposed to AI patches: >5% in safety trial (prompted UX shift) [1].
- System-level coordination impacts:
  - Longer PR closure time with review agents despite high “accounted for” rates [6].
  - Integration coordination time +8% associated with Copilot usage at project level [9].
- Acceptance/implementation rates as proxies for productive handoffs:
  - Low acceptance for functional review comments (≈5%), higher for refactoring (≈18%), suggesting observability-dependent handoff success [7].
  - High resolution/accounting of automated comments in PRs (≈73.8%) but net slower PR closure [6], indicating rework/verification loops can dominate.

---

### Trust, Reliance, and Interface Interventions

- Trust calibration dynamics are not explicitly modeled; however, several design/effect patterns are relevant:
  - Surfacing AI patches to reviewers increased time; restricting visibility to authors reduced the review-time penalty [1], suggesting that interface gating can prevent over-reliance burdens on reviewers and align verification effort with authorship.
  - HiLDe deliberately increases user reflection at critical decision points, which lowered vulnerabilities but slowed work [10]; this is a designed “trust-throttling” mechanism suited to high-stakes code.
  - LLM-as-a-Judge filters reduced irrelevant comments before human exposure in RevMate [7]; acceptance remained low, implying residual mismatch with reviewer expectations/timing.
  - At project scale, increased coordination time alongside higher contributions with Copilot [9] indicates potential overproduction and downstream verification load; heterogeneous effects by role (core vs peripheral) hint at differing trust/use patterns.

---

### Task- and Workflow-Specific Patterns

- Greenfield feature implementation (individual+AI):
  - Speedups in enterprise experiments [2,3]; slowdowns in mature OSS with high familiarity and large context [4]. This divergence underscores sensitivity to ecosystem tooling, repo familiarity, and AI reliability/latency [4].
- Bug fixing:
  - Not isolated as primary tasks in these studies; review fix generation at Meta shows strong offline patchability (68% exact match) but reviewer-facing exposure increases time, motivating author-side application [1].
- Code review:
  - Auto-generated comments: low acceptance, nontrivial inspection time; better for refactoring than functional concerns [7].
  - Automated review agents: high acted-on rates yet longer PR closure times and reports of recursive/faulty suggestions [6].
  - Reviewer support experiments measure time/quality but lack detailed decomposition or strong positive time results in provided excerpts [8].
- Test generation:
  - Interactive LLM support increases coverage and defects found with improved efficiency but raises false positives [5].
- Security/refactoring/intentionality:
  - Human-in-the-loop decoding reduces vulnerabilities at the cost of time [10]; refactoring comments more readily accepted than functional ones in live settings [7].

---

### Methodological and Reporting Gaps Relative to the Target Criteria

- Missing AI-alone gold or proxy baselines for end-to-end time in all studies [1,2,3,4,5,6,7,8,9,10].
- No formal, empirically calibrated models for handoff cost decomposition (T_explain, T_understand, T_verify), comparative-advantage allocation, or trust-update dynamics; measurements are mostly aggregate outcomes or coarse proxies [1,2,3,4,5,6,7,8,9,10].
- Limited stratification by experience beyond professional vs student; only [9] stratifies by OSS role; [2] distinguishes habitual AI users ex post. Pair programming and small-team hybrid dynamics are not experimentally isolated.
- Crossover difficulty points (d*) and explicit difficulty/observability tagging are absent; studies vary in domain complexity (enterprise vs OSS) but do not provide calibrated regime maps.
- Cognitive load is not directly measured (no NASA-TLX, physiological proxies) in the provided excerpts.

---

### Practical Workflow Implications Supported by the Evidence

- Gate AI outputs to the party best positioned to verify quickly:
  - Showing code-fix patches to authors rather than reviewers reduced review-time penalties at Meta [1].
- Prefer macro-handoffs where strong oracles exist; tighten loops when observability is low:
  - Unit tests as verification oracles enable efficient iteration in test generation [5]; review comments without strong oracles lead to inspection overhead with low acceptance [7].
- Expect coordination overhead in review workflows; instrument and budget for it:
  - Longer PR closure times with review agents [6] and increased integration coordination time at project scale with Copilot [9] suggest planning for additional verification cycles.
- For high-stakes security tasks, favor interfaces that increase intentional reflection:
  - HiLDe reduced vulnerabilities with a deliberate time cost [10]; consider such designs where defect costs dominate time.

---

### Quick Reference: Which Studies Address Which Aspects

- Direct end-to-end time effects (individual+AI): [2,3,4,10]
- Code review coordination impacts: [1,6,7,8]
- Test generation efficiency/quality trade-offs: [5]
- Project-level telemetry on contribution and coordination: [9]
- Interface/UX interventions with measurable time impact: [1,7,10]
- Evidence of true complementarity (T_hybrid < min(T_human, T_AI)): none established with AI-alone time baselines [1,2,3,4,5,6,7,8,9,10]

## Timeline

### Timeline and key milestones (2024–2025)

- 2024: First wave of field and controlled studies on LLM support for code review and collaborative development
  - Enterprise deployment case study of GPT‑4 Turbo–based automated code reviews finds mixed outcomes: widespread usage and perceived usefulness alongside longer PR closure times and frustration from recursion/faulty comments [6].
  - Large mixed open-/closed-source user study of GPT‑4o for review comments reports low acceptance (≈7–8%), higher acceptance for refactoring than for functional issues, and a measurable reviewer inspection time overhead (median 43 s/comment) [7].
  - Controlled lab study with 29 professionals shows measurable effects on review quality, review time, and reviewer confidence when automatically generated reviews are present (specific LLMs not named in excerpts) [8].
  - Platform-level telemetry study of Copilot across OSS projects detects modest increases in contributions (+5.9%) but also an ≈8% increase in coordination time (more code discussions), with heterogeneous effects by developer role [9].
- 2024 (published 2025): First enterprise RCT on end-to-end development time
  - Randomized controlled trial with 96 Google engineers shows a ≈21% time reduction on a complex, repo-realistic task with internal AI features, but with large uncertainty and no AI‑alone baseline; effects are stronger for engineers spending more hours on code-related work [3].
- 2025: Second wave emphasizes downstream effects, real‑world RCTs in OSS, and productionized hybrid workflows
  - Meta deploys an in‑production system for AI‑assisted fixes to code review comments at massive scale; an initial safety RCT shows that exposing AI patches to reviewers increases their time by >5%, prompting a UX change to show patches to authors instead—an important milestone in managing verification load and trust calibration via interface design [1].
  - Pre-registered two‑phase experiment (N=151, ≈95% professionals) on greenfield feature implementation and subsequent evolution tasks finds a 30.7% median time reduction with AI in Phase 1 and modest maintainability improvements downstream (CodeHealth), especially for habitual AI users [2].
  - RCT with experienced OSS contributors on large, mature repos finds a 19% slowdown with state‑of‑the‑art tools (Cursor Pro, Claude 3.5/3.7), highlighting setting/tool/task contingencies and coordination overheads; participants had forecasted speedups, underscoring trust/miscalibration risks [4].
  - Time‑boxed unit testing experiment shows LLM‑assistance improves coverage and defect detection efficiency but raises false positives—clarifying a quality–efficiency trade‑off in test generation tasks [5].
  - Human‑in‑the‑loop decoding interface (HiLDe) surfaces LLM “critical decision points,” reducing vulnerabilities but slowing completion—an explicit illustration of quality–time trade‑offs mediated by handoff/verification design [10].


### Shifts in focus and evolving methods

- From acceptance/quality proxies to timing and coordination-aware outcomes
  - Early code-review studies established feasibility and usefulness but uncovered coordination costs: longer PR closure times with automated reviews [6], low acceptance rates and measurable reviewer inspection overheads [7], and increased project-level coordination time with Copilot [9].
  - Subsequent work foregrounded time-to-completion as the primary outcome in controlled settings: enterprise RCTs [3], preregistered experiments with professionals [2], and OSS field RCTs [4]. These reveal mixed speed outcomes depending on context and task.
- From student/toy tasks to professional, repo-realistic, and field contexts
  - Professional developers and real repositories dominate the more recent studies: Google engineers [3], experienced OSS contributors on mature repos [4], professional-heavy samples [2], and industrial deployments [1,6,7]. This shift improves external validity for hybrid collaboration claims.
- From generic “AI help” to explicitly specified, modern copilots and agentic workflows
  - Named modern models/tools appear increasingly (GPT‑4 Turbo, GPT‑4o, Claude 3.5/3.7, Cursor Pro), including organization-tuned models (fine‑tuned Llama variants) and production integration with workflow-aware UX changes [1,3,6,7].
  - Emerging interfaces attempt to optimize handoff granularity and verification: reviewer‑targeting vs author‑targeting of AI patches to reduce reviewer time [1]; LLM‑as‑a‑judge filters to reduce low‑value review comments [7]; critical-decision-point highlighting to focus human attention [10].
- From substitution framing to explicit hybrid trade-offs
  - Evidence increasingly highlights the verification and coordination components of T_hybrid: AI support can speed individual coding tasks [2,3] yet lengthen review/closure times [6,7], increase coordination [9], or even slow overall completion in complex OSS tasks [4].
  - Test generation shows tangible detection/coverage gains but also error introduction via false positives, increasing verify/rework time [5].
- Methodological rigor and transparency
  - Growth in preregistration [2], controlled RCTs in enterprise and OSS settings [3,4], and detailed telemetry of actual workflows [6,7,9] marks a methodological maturation.


### What these studies collectively establish (and where gaps remain)

- Established patterns
  - Hybrid efficiency is highly context-dependent. Greenfield, well-scaffolded tasks in controlled enterprise settings show speedups [2,3], while complex, mature OSS contexts with rich coordination demands can see slowdowns [4].
  - Coordination and verification overheads are first-order drivers of outcomes. Multiple field studies document increased PR closure times, reviewer inspection time, and discussion activity when AI is introduced [6,7,9]. A production safety RCT shows that who receives AI patches (author vs reviewer) changes reviewer time by >5% [1].
  - Interface design matters. Filtering, targeting, and highlighting strategies can redistribute cognitive/verification load, improving quality but often trading off speed [1,7,10].
  - Quality effects are mixed and task‑specific. Test generation benefits are clear but carry higher false‑positive rates [5]; code review assistance yields variable acceptance and perceived usefulness [6,7]; vulnerability reduction is possible with intentional interfaces at the cost of time [10].
- Persistent gaps relative to hybrid-complementarity theory
  - Few studies report AI‑alone gold standards or even proxy AI‑alone times (e.g., time‑to‑first‑passing tests), limiting direct tests of T_hybrid < min(T_h, T_ai) [2,3,4,5,6,7,9,10].
  - No study in this set provides empirically calibrated models decomposing T_explain, T_understand, T_verify or formal comparative‑advantage allocation with optimal handoff granularity estimates; most evidence is observational or experimental without calibrated parameters [1,2,3,4,5,6,7,8,9,10].
  - Trust calibration is inferred but rarely modeled. Over‑/under‑reliance patterns appear (e.g., reviewer slowdowns and forecasts vs realized performance) [1,4,7], yet quantitative trust‑update dynamics and validated interventions are not formally evaluated.
  - Limited stratification by task category across the full spectrum (greenfield, bug-fix, code review, test generation, refactoring) and by unit of analysis beyond individual+AI; team‑level effects are mainly via OSS telemetry [9] and PR workflows [6,7].
  - Crossover difficulty points d* and economic utility measures (time adjusted by defect costs) are not reported in this set.


### Research clusters and contributors

- Code review and PR workflow cluster (industry + academia)
  - Meta’s MetaMateCR production system integrates model selection, internal benchmarking, and live safety trials, and demonstrates UX‑mediated control of verification costs [1].
  - Industrial deployment study at Beko with GPT‑4 Turbo (Qodo PR Agent) documents organization‑scale uptake and the trade‑off between usefulness and longer PR closure times [6].
  - Cross‑organization user study with Mozilla and Ubisoft employing GPT‑4o, RAG, and LLM‑as‑a‑judge explores acceptance dynamics and reviewer time costs [7].
  - Controlled experiment with professionals assesses how auto‑generated reviews impact reviewer performance and confidence [8].
  - This cluster suggests a sustained shift toward treating code review as a socio‑technical system where AI must be integrated with care to avoid coordination blowups while preserving value [1,6,7,8].
- Productivity and task execution RCT cluster
  - Enterprise RCT at Google quantifies an average ≈21% time reduction with internal AI features on a complex, realistic task [3].
  - OSS RCT with experienced contributors finds a 19% slowdown with modern assistants, surfacing moderators like repo familiarity, project size, and tool reliability/latency [4].
  - Pre‑registered experiment with professionals finds substantial speedups for greenfield development and modest downstream maintainability benefits [2].
  - Together, these works highlight heterogeneous treatment effects and the importance of environment, scaffolding, and verification mechanisms [2,3,4].
- Testing and secure coding/intentional interfaces
  - LLM‑assisted unit testing improves detection/coverage but raises false positives, clarifying where AI contributes and where verification burdens grow [5].
  - HiLDe’s intentional decoding identifies “critical decision points,” improving security outcomes at the cost of time, illustrating a concrete handoff‑granularity interface design [10].


### Trends that likely shape the next phase

- Integration-first, UX‑aware systems over raw model upgrades
  - Evidence that presentation/targeting of AI outputs changes human time and outcomes (e.g., reviewer vs author targeting) indicates interface and workflow levers can dominate raw model quality in hybrid settings [1,6,7,10].
- Measurement of coordination and verification as primary outcomes
  - PR closure time, reviewer inspection time, discussion volume, and false‑positive rates are becoming standard metrics alongside task completion time—reflecting that T_handoff and verify/rework loops are decisive in practice [5,6,7,9].
- Movement toward field RCTs and preregistration
  - Enterprise and OSS RCTs and preregistered designs are emerging as the gold standard for credible causal estimates in realistic contexts [2,3,4].
- Toward calibrated decision policies (but modeling still missing)
  - Several studies implicitly motivate calibrated acceptance/verification policies (filters, targeting, critical‑point highlighting), yet formal, empirically calibrated models of comparative advantage, handoff decomposition, trust dynamics, and crossover d* remain largely open [1,2,3,4,5,6,7,8,9,10].

## Foundational Work

### Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the **reference rate**, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but provide important context.

| Ref. | Reference Rate | Topic Match | Title | Authors | Journal | Year | Total Citations | Cited By These Relevant Papers |
|---|---|---|---|---|---|---|---|---|
| [11] | 0.55 | 14% | The Impact of AI on Developer Productivity: Evidence from GitHub Copilot | Sida Peng, ..., and Mert Demirer | ArXiv | 2023 | 325 | [1, 3, 4, 9, 10] |
| [3] | 0.47 | 46% | How Much Does AI Impact Development Speed? an Enterprise-Based Randomized Controlled Trial | Elise Paradis, ..., and Satish Chandra | 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 5 | [1, 4] |
| [18] | 0.42 | 6% | Moving Faster and Reducing Risk: Using LLMs in Release Deployment | Rui Abreu, ..., and Nachiappan Nagappan | 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 2 | [1, 3] |
| [15] | 0.38 | 9% | Resolving Code Review Comments with Machine Learning | Alexander Frömmgen, ..., and Maniatis Google | 2024 IEEE/ACM 46th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 22 | [1, 3] |
| [26] | 0.37 | 3% | Multi-line AI-Assisted Code Authoring | Omer Dunay, ..., and Nachiappan Nagappan | Companion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering | 2024 | 20 | [1, 3] |
| [6] | 0.36 | 26% | Automated Code Review in Practice | Umut Cihan, ..., and Eray Tüzün | 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 5 | [1] |
| [124] | 0.34 | 0% | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Carlos E. Jimenez, ..., and Karthik Narasimhan | ArXiv | 2023 | 794 | [1, 4] |
| [86] | 0.29 | 0% | The Impact of Large Language Models on Open-source Innovation: Evidence from GitHub Copilot | Doron Yeverechyahu, ..., and Gal Oestreicher-Singer | ArXiv | 2024 | 13 | [3, 4, 9] |
| [274] | 0.28 | 0% | CommentFinder: a simpler, faster, more accurate code review comments recommendation | Yang Hong, ..., and A. Aleti | Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering | 2022 | 55 | [1, 6, 7] |
| [541] | 0.27 | Not measured | Evaluating Large Language Models Trained on Code | Mark Chen, ..., and Wojciech Zaremba | ArXiv | 2021 | 6183 | [1, 10, 11, 17] |
| [33] | 0.27 | 2% | Significant Productivity Gains through Programming with Large Language Models | Thomas Weber, ..., and Sven Mayer | Proceedings of the ACM on Human-Computer Interaction | 2024 | 23 | [3, 4] |
| [65] | 0.25 | 1% | AI-Assisted SQL Authoring at Industry Scale | Chandra Maddila, ..., and Peter C. Rigby | 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 4 | [1] |
| [542] | 0.23 | Not measured | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code | Naman Jain, ..., and Ion Stoica | ArXiv | 2024 | 567 | [1] |
| [45] | 0.22 | 1% | AI-Assisted Code Authoring at Scale: Fine-Tuning, Deploying, and Mixed Methods Evaluation | V. Murali, ..., and Peter C. Rigby | Proc. ACM Softw. Eng. | 2023 | 19 | [1] |
| [61] | 0.22 | 1% | Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming | Hussein Mozannar, ..., and E. Horvitz | ArXiv | 2022 | 125 | [3, 11, 12, 17] |
| [523] | 0.22 | 0% | Randomized Controlled Trials: Questions, Answers, and Musings | Judith Lumley | Birth-issues in Perinatal Care | 2008 | 200 | [1] |
| [189] | 0.20 | 0% | PaperBench: Evaluating AI's Ability to Replicate AI Research | Giulio Starace, ..., and Tejal Patwardhan | ArXiv | 2025 | 40 | [4] |
| [60] | 0.19 | 1% | Measuring AI Ability to Complete Long Tasks | Thomas Kwa, ..., and Lawrence Chan | ArXiv | 2025 | 30 | [4] |
| [498] | 0.19 | 0% | GATE: An Integrated Assessment Model for AI Automation | Ege Erdil, ..., and Robert Sandler | ArXiv | 2025 | 2 | [4] |
| [122] | 0.19 | 0% | SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? | Samuel Miserendino, ..., and Johannes Heidecke | ArXiv | 2025 | 38 | [4] |

## Adjacent Work

### Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas for useful new research directions.

| Ref. | Adjacency score | Topic Match | Title | Authors | Journal | Year | Total Citations | References These Foundational Papers |
|---|---|---|---|---|---|---|---|---|
| [82] | 0.29 | 0% | Who is using AI to code? Global diffusion and impact of generative AI | Simone Daniotti, ..., and Frank M. H. Neffke | ArXiv | 2025 | 1 | [3, 11, 86, 190] |
| [46] | 0.27 | 1% | The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers * | Kevin Zheyuan Cui, ..., and Salz | Journal Not Provided | N/A | 32 | [11, 86, 168, 190] |
| [4] | 0.27 | 40% | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Joel Becker, ..., and David Rein | ArXiv | 2025 | 5 | [3, 11, 86, 168, 190] |
| [86] | 0.24 | 0% | The Impact of Large Language Models on Open-source Innovation: Evidence from GitHub Copilot | Doron Yeverechyahu, ..., and Gal Oestreicher-Singer | ArXiv | 2024 | 13 | [11, 168, 190] |
| [540] | 0.24 | 0% | AI Recommendations and Non-instrumental Image Concerns | David Almog | ArXiv | 2025 | 0 | [11, 168, 190] |
| [536] | 0.24 | 0% | Approach or Avoidance: How Does Employees’ Generative AI Awareness Shape Their Job Crafting Behavior? A Sensemaking Perspective | Yihang Yan, ..., and Yao Geng | Behavioral Sciences | 2025 | 0 | [11, 168, 190] |
| [474] | 0.24 | 0% | Automation, AI, and the Intergenerational Transmission of Knowledge | Enrique Ide | ArXiv | 2025 | 0 | [11, 168, 190] |
| [465] | 0.24 | 0% | AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials | Tobias Heinrich, ..., and Navida Chun-Han Wang | PLOS One | 2025 | 0 | [11, 168, 190] |
| [462] | 0.24 | 0% | Improving Generative Ad Text on Facebook using Reinforcement Learning | Daniel Jiang, ..., and Zheqing Zhu | ArXiv | 2025 | 0 | [11, 168, 190] |
| [328] | 0.24 | 0% | Working with AI: Measuring the Occupational Implications of Generative AI | Kiran Tomlinson, ..., and Siddharth Suri | ArXiv | 2025 | 0 | [11, 168, 190] |
| [289] | 0.24 | 0% | On the Future of Software Reuse in the Era of AI Native Software Engineering | A. Taivalsaari, ..., and Cesare Pautasso | ArXiv | 2025 | 0 | [11, 168, 190] |
| [70] | 0.22 | 0% | Prompting LLMs for Code Editing: Struggles and Remedies | Daye Nam, ..., and Satish Chandra | ArXiv | 2025 | 1 | [3, 11, 61] |
| [9] | 0.21 | 18% | The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot | Fangchen Song, ..., and Wen Wen | ArXiv | 2024 | 4 | [11, 86, 103, 190] |
| [544] | 0.19 | Not measured | Does generative AI facilitate investor Trading? Early evidence from ChatGPT outages | Qiang Cheng, ..., and Yue Zhao | Journal of Accounting and Economics | 2025 | 2 | [11, 190] |
| [282] | 0.19 | 0% | Making AI Inevitable: Historical Perspective and the Problems of Predicting Long-Term Technological Change | Mark Fisher and John Severini | ArXiv | 2025 | 0 | [11, 190] |
| [168] | 0.19 | 0% | Generative AI at Work | Erik Brynjolfsson, ..., and Lindsey Raymond | SSRN Electronic Journal | 2023 | 531 | [11, 190] |
| [58] | 0.18 | 1% | Human-AI Experience in Integrated Development Environments: A Systematic Literature Review | Agnia Sergeyuk, ..., and Maliheh Izadi | ArXiv | 2025 | 5 | [11, 33, 61, 103] |
| [3] | 0.18 | 46% | How Much Does AI Impact Development Speed? an Enterprise-Based Randomized Controlled Trial | Elise Paradis, ..., and Satish Chandra | 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) | 2024 | 5 | [11, 33, 61, 86, 103, 438] |
| [33] | 0.18 | 2% | Significant Productivity Gains through Programming with Large Language Models | Thomas Weber, ..., and Sven Mayer | Proceedings of the ACM on Human-Computer Interaction | 2024 | 23 | [11, 61, 438] |
| [17] | 0.18 | 7% | Developer Behaviors in Validating and Repairing LLM-Generated Code Using IDE and Eye Tracking | Ningzhi Tang, ..., and T. Li | 2024 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC) | 2024 | 4 | [11, 61, 103] |