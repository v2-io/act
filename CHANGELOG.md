# CHANGELOG

The forward-going record of substantive changes to the framework. Entries are ordered most-recent-first, dated, and grouped by theme within a date.

## How this file relates to LOG.md, TODO.md §Archive, and git

- **CHANGELOG.md** *(this file)* — substantive changes from 2026-04-24 onward. Cycle-shape narratives ("what changed about how the theory thinks", structural moves, conventions adopted) go here. Entry granularity is the day; commit hashes appear inline for traceability.
- **[LOG.md](LOG.md)** — archaeology of cycles through 2026-04-24. Frozen at that date. Read it when the *origin* of a current commitment matters: whether a "settled" item rests on derivation or on a cycle's working consensus, or how an audit finding's prior status should shape current routing.
- **[TODO.md §Archive](TODO.md)** — commit-and-finding granularity record of landed work, kept inside the active TODO.
- **Git** — primary source for "what changed in code/segments." Use `git log --follow` for slug-renamed segments.

The split between CHANGELOG and TODO §Archive is intentional: CHANGELOG carries the *narrative shape* (what conventions changed, what disciplines emerged, what the cycle was about); TODO §Archive carries the *checklist trail* (which findings closed, which commits did what). They overlap in scope but serve different reading needs.

---

## 2026-04-25

### Audit-extraction cycle: 2026-04-24 fresh-pass results captured

The 2026-04-24 fresh-pass audit (an Opus-4.7 primary pass + independent Gemini and Codex re-audits in the same session) produced findings, an architectural proposal candidate, and a meta-lesson about audit failure modes. The primary pass had initially returned "zero findings"; Gemini and Codex independently surfaced five-plus real findings (math errors in worked examples, cross-segment contradictions around the recently-added C-iv route, integration debt between TST and `03-logogenic-agents/`). The audit's "Reading-mode failures" post-mortem became the foundation for the substantially improved `msc/de-novo-audit-instructions.md` (separate cycle, also 2026-04-24/25).

This cycle was extraction-only: no segment-text changes, no architectural decisions made — purely surfacing the audit's substantive content into the durable tracking documents (TODO.md, PROPOSALS.md, pending-findings-2026-04-25.md) so the source `msc/audit-2026-04-24-fresh-pass.md` could scroll into obscurity without losing signal. The next audit cycle, running with the improved instructions, will inevitably re-discover some of this batch's findings — capture-first protects the existing batch's signal against that overlap.

**What landed:**
- `msc/pending-findings-2026-04-25.md` — burden-of-proof writeups for 5 verified findings (F-V1 discrete-variance-gap math error; F-V2 scope-multi-agent vs scope-composite-agent contradiction; F-V3 C-iii vs $G_c$ requirement, = F8 from 2026-04-22 batch; F-V4 sign error in zero-sum worked example; F-V5 TST↔logogenic integration debt) and 3 partial findings (P-V1, P-V2, P-V3). Each finding verified first-hand by the integrating agent against current src text. F-V1's math re-derived independently via Taylor expansion of segment's own DA.1S; F-V4's NE re-checked via Monderer-Shapley derivative test ($\Phi = a_A - a_B$ wrong, correct is $\Phi = a_A + a_B$, NE $(1,1)$ not $(1,-1)$). External-citation spot-checks (Bretagnolle-Huber, Otto-Villani 2000) confirmed accurate.
- `TODO.md` "Active — Pending Findings" — 2026-04-25 batch table; F-V3↔F8 cross-reference; two decisions explicitly marked deferred (F-V3 routing Path A vs SP-21; SP-21 timing).
- `PROPOSALS.md` §G — **SP-21** (composite-agent scope-route ontology split) added with full schema. Critically: SP-21 *reverses* the deliberate 2026-04-22/23 unification reasoning (the disjunctive C-i ∨ C-ii ∨ C-iii ∨ C-iv form with explicit "preferred reading: treat as a different type within the same scope condition, via (C-iv)" in `msc/spike-strategic-composition.md`). Entry includes the prior-reasoning paper trail (8 dependent segments, the spike-level decision SP-21 would undo) and recommends *deferral* until Bundle 2 (Section III completion) matures the substrate. Reversal-with-paper-trail discipline is a precedent worth preserving for future audits.
- Mechanical fix bundle (F-V1, F-V2, F-V4, F-V5, P-V1, P-V3) delegated as a single Task agent with strict instructions to re-derive math rather than paste, read both TST and logogenic-agents segments before F-V5, and not auto-commit.

**What didn't land (deferred for Joseph):**
- F-V3 / F8 narrow editorial fix (Path A: induce $O_c$ from relevance variable $Y$ for C-iii). ~45–60 min.
- SP-21 architectural restructure (Path B / SP-21). 4–6 sessions; recommended for deferral.

**Convention surfaced this cycle.** When audit cycles produce both local findings AND architectural-restructure candidates that reverse recent deliberate decisions, the proposal should land in PROPOSALS.md with the *prior-reasoning paper trail explicit* — quoted spike passages, downstream rework cost, the specific decision-point being reversed. Joseph's question "is there prior reasoning that illuminates what will be undone?" is the right diagnostic for any restructure proposal; the answer should be in the proposal entry, not buried in the audit document.

---

## 2026-04-24

### Role-prefix discipline: pilot → tooling → sweep

Project-wide adoption of the slug convention `{type-prefix}-{subject-noun}`, where the type prefix derives mechanically from each segment's `type:` frontmatter. Three landed pieces:

- **Pilot** (commits `09ace17`, `f6b8ae4`, `0b9cd24`): seven slug changes across four type categories, including the 1:2 semantic split of `#scope-condition` into `#scope-adaptive-system` + `#scope-agency` (the old name described the segment's role rather than the class it defined; downstream segments depend on one or the other, not on an abstract compound). Subject-noun-first slug naming validated as architectural invariant. Pilot-validation observations folded into the principles-file rewrite.
- **Tooling** (commits `981b291`, `3aa9e74`): `bin/align-slug` introduced as a one-segment wrapper over `bin/rename-slug`. Reads `type:` from frontmatter, computes the correct target slug under the project-wide `TYPE_TO_PREFIX` mapping, and invokes the mechanical rename only when not already aligned. `--all` for repo sweeps.
- **Full sweep** (commits `e6adf9e`, `f8bc46a`): `TYPE_TO_PREFIX` expanded from 1 entry to 14, collapsing FORMAT.md type tokens to compact natural-English forms (`postulate → post`, `definition → def`, `derivation → deriv`, etc.) so an `ls` of `src/` surfaces the kind-of-thing at a glance. Trailing-`-{type}` strip added: subject-nouns shouldn't carry the type word once the role-prefix lives in front (`bias-bound-derivation` → `deriv-bias-bound`). Sweep applied across 142 active segments; `01-aad-core/OUTLINE.md` lint-clean throughout.

Bug caught and fixed mid-arc: an early `bare_subject` used the full type vocabulary as candidate leading-prefixes, silently corrupting subject-nouns whose leading word coincided with a type token (`observation-function` → `def-function`, losing "observation"). Tightened to strip only the segment's own type forms. Two corrupted slugs (`def-function`, `scope-ambiguity-modulation`) restored.

### Methodology: separate-passes for role-prefix vs subject-noun

Going forward, role-prefix addition (mechanical) and subject-noun renaming (judgment-heavy) execute in separate cycles. Bundling creates two failure modes: the segment's prose drifts out of step with its new identity, and voters can't evaluate noun choices when the prefix is decided in the same cycle. Documented in `msc/naming-pilot-rename-plan.md` and the auto-memory.

### `FORMAT.md` segment-set principle

New "Segment-set principle (load-bearing for tooling)" subsection makes explicit what was previously implicit: every non-`old-*` file in `src/` is a segment that conforms to FORMAT (drafts and orphans included; stages are progress within FORMAT, not exemptions); `old-*` is the only exemption mechanism; other working material doesn't belong in `src/`. Tools (`bin/align-slug --all`, `bin/lint-outline`, `bin/build`) reference this principle.

### Refined naming-principles file

`msc/naming-principles.md` rewritten for the refined Round 1. Cold-start instruction moved to first paragraph (round-1 contamination evidence). New "Architectural invariants" section recording role-prefix discipline + subject-noun-first + Greek-vocabulary commitment + separate-passes methodology — these are no longer up for vote. New "Vote categories" section explicitly distinguishing rename / keep / canonicalize / add-alias / name-unnamed-thing. `+2` weight added; bands spelled out. Renamed-from-now-sounds-weird test added. Scope-honesty special-case for meta-segments documented.

### Side-resolutions

- **Finding 14 Option A** (`#scope-developer-agent` exact-status mismatch): closed by the type-frontmatter cleanup that landed in commit `0b9cd24` (`type: definition` → `scope`, `status: exact` → `axiomatic`).
- **`bin/lint-outline` PROOF → DERIV**: graphviz display label for `derivation` changed from "PROOF" to "DERIV", aligning with FORMAT.md's deliberate avoidance of proof terminology.

### Type-frontmatter audit (preflight for the sweep)

Opus general-purpose audit of all 142 active segments cleared the repo at 100% type-vocabulary conformance, zero stale tokens. Five type-vs-content mismatches surfaced; three clear cases corrected (`unity-dimensions`: discussion → definition; `simulation-results`: detail → observation; `tempo-composition`: sketch → derived). Two borderlines surfaced for reviewer judgment, not applied (`agent-opacity`, `observation-ambiguity-modulation`). 18 internal H1/tag-word inconsistencies catalogued; most are intentional setup-tag-before-main-tag patterns. Audit-recommended additional `TYPE_TO_PREFIX` mappings rejected as unnecessary or insufficient-frequency.

### Known follow-up

- **Formal-tag content cleanup**: ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect, content to update; separate cycle.
- **Two reviewer-judgment type calls** from the audit (`agent-opacity`, `observation-ambiguity-modulation`).
- **Three H1/first-tag word disagreements** flagged by the audit (`objective-functional`, `composition-closure`, `ciy-observational-proxy`); content cleanup, any time.

---

## Imported from auto-memory (2026-04-25)

The narrative cycle entries below were imported from `MEMORY.md` to reduce de-novo-audit priming bleed. Faithful copies of the auto-memory entries; voice and date conventions preserved as-is. Pre-2026-04-24 entries here partially overlap with `LOG.md` archaeology — kept as imported rather than reconciled, since the auto-memory voice is itself the artifact worth preserving.

### Purposeful Agency Derivation (March 2026)
- **Main spike**: `msc/spike-purposeful-agent-derivation.md`
- Core approach: derive the need for causal structure from first principles
- The causal hierarchy theorem proves Level 2 access requires causal structure
- The feedback loop provides Level 2 access by construction (TF-02)
- The O_t/Σ_t split is a **scope narrowing** (for timescale-separated agents), not a derived result
- G_t complexity is bounded by M_t evaluative capacity

### Spike v3 (March 2026 — definitive version)
- `msc/spike-v3-purposeful-agent.md` — definitive version for porting to 01-aad-core/src/
- Key features: unified value object, satisfaction gap + control regret split, cost inequality labeled normative, directed separation with prominent scope condition, strategy persistence as proposed schema

### Graph Uniqueness Spike (March 2026)
- `msc/spike-graph-uniqueness.md`
- **Key result**: Four operational postulates force strategy representation to be a DAG with the Markov property
- **Acyclicity is DERIVED**: temporal ordering over finite planning horizon prevents cycles
- **The P3→Markov step needs tightening** — open question

### Agent Composition / Holon Spike (March 2026)
- `msc/spike-agent-composition.md`
- Composition consistency is a REQUIREMENT for AAD's coherence, not a feature
- Section III = "Composition Dynamics" — all new ground
- 2-3 agent base case, n-agent follows by induction

### Codex Reviews (March 2026)
- Three rounds of review. Key items: X_t lift, Level 2 scoping, O_t/Σ_t as independent dimensions, satisfaction gap/control regret split, directed separation scope condition, composition closure criterion
- See [session_2026_03_11_tst_conversion.md](session_2026_03_11_tst_conversion.md) for full details

### Fresh Eyes Session (2026-03-14)
- [project_fresh_eyes_2026_03_14.md](project_fresh_eyes_2026_03_14.md) — editorial fixes, composition bridge lemma, architectural classification
- **Key insight**: project needs convergent depth over generative breadth. 3:1 ratio (promoting vs creating) until segments reach candidate stage.

### Consolidated Three-Model Review (2026-03-13)
- `msc/2026-03-13-feedback.md` — top priorities: (1) quantify directed-separation approximation, (2) clarify α vs T relationship, (3) resolve composition-closure bridge lemma

### SOC / Renormalization Lens on Composition (2026-04-20)
- [project_soc_composition.md](project_soc_composition.md) — speculation-grade: RG-style fixed-point argument on composition; forward (→ power laws), inverse (→ closure as consequence), "optimal-at-critical" conjecture. Captured in `msc/speculation-soc-composition.md`. Parked, not pursued.

### Section III Unity-Closure Investigation (2026-04-20)
- [project_section_iii_unity_closure.md](project_section_iii_unity_closure.md) — Two parallel spikes: IB/rate-distortion unity→closure mapping (`msc/spike-unity-closure-mapping.md`) + MZ connection (`msc/spike-mori-zwanzig-composition.md`). Findings: (1) unity→closure is a rate-distortion relation, not direct prediction; (2) MZ zero-lag bound closes, full-kernel bound doesn't; (3) two-axis closure structure (unity × update-heterogeneity) exposes gap in `#unity-dimensions`. Notes updated. Ready for segment promotion.

### 2026-04-22 Audit Cycle (four audits, 15 findings, 14 architectural proposals)
- [project_2026_04_22_audit_cycle.md](project_2026_04_22_audit_cycle.md) — Major audit cycle on 2026-04-22. Four de novo audits (Gemini, Codex r1, Opus, Codex r2) produced 15 local findings + 14 architectural proposals. Portfolio lives in `msc/architectural-proposals-2026-04-22.md`; findings detail in `msc/pending-findings-2026-04-22.md`. TODO.md is the navigator with Strategic Proposals at top.

### 2026-04-22 Strengthening Cycle (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`)
- [project_2026_04_22_strengthening_cycle.md](project_2026_04_22_strengthening_cycle.md) — Strengthen-first execution after Joseph's mid-session course-correction. F1 strengthening → no-go theorem in #causal-insufficiency-detection (CHT applied; covariance test now derived as unique broadly-available violation). F7 strengthening → per-quantity exactness audit + conditional maximality in #software-epistemic-properties + $\mathcal{C}_t^{\text{commit}}$ in NOTATION.md. F10 → IB status discussion-grade → exact. F13 strengthening → Prop B.7 derived for L1' observable-$C$ (five-way gating) + Cramér-Rao refutation for unobservable single-channel. New meta-segment #identifiability-floor naming the F1+F13 no-go pattern. AI integration pass: G-BP2 V-medium executed + Aguilera/Bruineberg/Sun-Firestone underclaim positioning + Friston/Wiener/Conant-Ashby honest-credit moves across 9 segments.

### 2026-04-22/23 Cascading Strengthening Cycle (nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`)
- [project_2026_04_22_23_cascading_strengthening.md](project_2026_04_22_23_cascading_strengthening.md) — Multi-phase strengthening session running Phases 1-5+7 of post-evening-audit sequence plus two in-flight spikes (reverse-KL uniqueness, A2'). **Three Cauchy-functional-equation uniqueness theorems discovered** (F20 regret-bound, reverse-KL chain-rule, log-odds evidential-additivity) — each forcing a logarithmic coordinate via AAD-internally-motivated additivity axiom. Discovered three-layer additive-decomposition pattern (§SP-1 in proposals doc). Three new appendix / meta segments: #strategy-cost-regret-bound, #separability-pattern, #edge-update-natural-parameter. #agent-identity promoted to formal scope. TST reframed as calibration laboratory. O-BP14 derivation-table convention established. Citation audit found 3 wrong attributions in reverse-KL work (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2) corrected to Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975. Project-wide citation audit now TODO.

### 2026-04-23 Brainstorm Cycle (seven commits: `0d7b987`, `591e8b6`, `13fe242`, `b48cdee`, `77a9bde`, `0bd859e`, `a739e9a`)
- [project_2026_04_23_brainstorm_cycle.md](project_2026_04_23_brainstorm_cycle.md) — Seven parallel research spikes prompted by GAA (Baigozin 2025) external-framework comparison as brainstorming exercise. Six promoted: `#critical-mass-composition`, `#interaction-channel-classification`, `#consolidation-dynamics`, `#persistence-cost`, `#adaptive-gain-dynamics`, `#detection-latency`. One deferred (`#internal-external-decomposition`) pending variance-additive reframe after Spike H (ρ-factorization) returned honest obstruction — multiplicative $\rho = \rho_{\text{ext}} \cdot f(\mathcal M) \cdot g(\pi)$ NOT derivable; native structure is variance-additive. Novel structural observations: **template-augmentation triad** (B+A+D under #sector-persistence-template); Aczél-FE downstream consequences (#detection-latency is first result where #additive-coordinate-forcing's constructive meta-pattern composes with a negative consequence → motivates positive requirement); recipient-side theory closes the `#adversarial-edge-targeting` Section III GAP by pairing classifier+optimizer. Segment count: 96 → 103.

### 2026-04-23 Gap A/B Cycle (spikes + promotion)
- [project_2026_04_23_gap_ab_cycle_and_promotion.md](project_2026_04_23_gap_ab_cycle_and_promotion.md) — Gemini 2026-04-23 audit flagged two gaps (default signal function under correlated failures; contraction beyond linear Kalman). 12 parallel spikes + Jacobian-level B1 follow-up + H_b spike. 7 commit-scoped landings executed: 6 new segments (#contraction-template, #strategic-composition, #fisher-whitened-update-rule, #l1-update-bias, #variational-sector-condition, #agent-opacity) + Instance 3 in #identifiability-floor + 4th primary instance in #additive-coordinate-forcing (Čencov via (PI)) + 7th ladder in #separability-pattern + (C-iv) in #composition-scope-condition + (PI) axiom in #agent-identity + monotone-operator lineage acknowledged in #sector-persistence-template / #sector-condition-derivation. Segment count 103 → 109.

### 2026-04-23 SP-2 + Citation Audit Cycle (three commits: `7456ec3`, `6567914`, `f61e62f`)
- [project_2026_04_23_sp2_citation_audit.md](project_2026_04_23_sp2_citation_audit.md) — SP-2 landed as #additive-coordinate-forcing meta-segment (97th AAD segment). Opus's 5-instance conjecture **narrowed in-flight** to honest **1-anchor-plus-2-theorem** characterization (chain layer = mathematical identity; divergence + update = theorems conditional on AAD-internal additivity axioms; Lyapunov + IB Lagrangian = adjacent family members). Framing pass part 1: CLAUDE.md §7 expanded to "Epistemic architecture as AAD's distinctive contribution" incorporating convergent Codex/Gemini/Opus reframe; OUTLINE "Reading AAD" preamble added. **Citation audit project-wide completed: zero confirmed attribution errors** (reverse-KL 20-25% rate was a local concentration, not project-wide pattern). PDF-level verification confirmed Bruineberg 2022 "Pearl-blanket vs Friston-blanket" is VERBATIM terminology (not AAD paraphrase, credit Martin Biehl fn 3); Bareinboim CHT = Theorem 1 p.22 of 2022 ACM Books chapter (= Columbia TR R-60); Aguilera 2022 FEP-narrow-validity claim exactly matches AAD's usage. 3 framing refinements (Eguchi framework/theorem distinction; Sun & Firestone direction-of-inference; Friston 2023 path-integral vs stability). 5 missing-citation gaps hardened (Tikhonov, Chechik, Doob-Dynkin, Cox, Cramér). ref/ hygiene: 26 PDFs acquired and canonically renamed, then excluded from git (redistribution rights); ref/INDEX.md tracks the bibliography.

### 2026-04-24 Consolidation Audit + Naming Sweep (commit `9274c33`, paused pre-pilot)
- [project_2026_04_24_consolidation_and_naming.md](project_2026_04_24_consolidation_and_naming.md) — PROPOSALS.md consolidation (33 proposals → banded portfolio + two cross-cutting bundles + 6 newly-surfaced candidates from segment Working Notes); multi-agent naming sweep Round 1 (10 agents across 7 model architectures, 1,073 vote rows, Ruby aggregation script in bin/, three output formats); role-prefix discipline proposed and pilot staged. Paused for compaction before pilot. Key decisions already settled: subject-noun preference for slug naming; role-prefix as invariant (#scope-, #postulate-, #derivation-, etc.); #scope-adaptive-system / #scope-composite-agent / #scope-human-developer-agent / #scope-logogenic-agent as the pilot set. ASF is the intentional umbrella name (not debt); AAD is Part I only.

### 2026-04-25 Fresh-Audit Session — three failures, two re-audits, instructions file landed
- [project_2026_04_25_audit_session.md](project_2026_04_25_audit_session.md) — De novo audit Joseph requested went through three attempts: delegation failure (parallel sub-agent comprehension); verification-mode failure (anchored on prior frame as scaffolding despite explicitly choosing fresh-pass option); third pass produced `msc/audit-2026-04-24-fresh-pass.md` with "zero findings" claim. Joseph then ran independent Gemini and Codex audits, surfacing 5 verified findings I missed (F-V1 math error in discrete-sector-condition variance gap; F-V2 scope-multi-agent vs scope-composite-agent C-iv contradiction; F-V3 C-iii without $O_c$ vs composition-closure $G_c$ requirement; F-V4 zero-sum sign error in deriv-strategic-composition; F-V5 TST/logogenic Class 2 integration debt). Reading-mode failures self-diagnosed: charitable reading on worked-example math; cross-segment consistency not checked around recent C-iv addition; sample bias toward "load-bearing centers" missed discrete-time machinery. Produced `msc/de-novo-audit-instructions.md` with substantive lessons for future audits — three editorial passes: initial draft, softening + structural additions (three-phase report shape, source ordering src-first then msc/ref/git, prior-audit-reading caveat), final tone calibration to peer-to-peer voice. F-V findings not yet on TODO.md as active findings — Joseph or future agent with authority needs to add them. B7 architectural proposal flagged: separating composite-agent scope routes (C-i/ii/iii/iv) into distinct composite ontologies with distinct macro-objects.

### 2026-04-25 Audit-Extraction Cycle — findings + B7→SP-21 captured into tracking docs; mechanical fixes landed
- [project_2026_04_25_audit_extraction.md](project_2026_04_25_audit_extraction.md) — Follow-up to the fresh-audit session above. Joseph's framing: "extract and organize what was just done so we can move on to a much better audit posture" — the source `msc/audit-2026-04-24-fresh-pass.md` would scroll into obscurity quickly, only what landed in tracking documents would survive. **Captured into durable tracking docs:** 5 verified findings + 3 partial findings → `msc/pending-findings-2026-04-25.md` + TODO.md "Active — Pending Findings" 2026-04-25 batch (F-V1 verified via Taylor-expansion re-derivation + Python numerical sanity check; F-V2/F-V3/F-V4/F-V5 verified first-hand against current src; F-V3 ≡ F8 from 2026-04-22 batch, re-surfaced); B7 → **SP-21** in PROPOSALS.md §G with full prior-reasoning paper trail. **SP-21 reverses prior reasoning.** Explore-agent investigation surfaced that the disjunctive C-i ∨ C-ii ∨ C-iii ∨ C-iv form was a *deliberate* 2026-04-22/23 unification choice — `msc/spike-strategic-composition.md` lines 99–108 carry "preferred reading: treat as a different type within the same scope condition, via (C-iv)" with explicit reasoning. SP-21 entry includes the prior-reasoning quote, 8 dependent-segment downstream rework cost, and recommends *deferral* until Bundle 2 (Section III completion) matures the substrate. **Convention crystallized:** when audit cycles produce restructure proposals that reverse recent deliberate decisions, the proposal entry must include the prior-reasoning paper trail explicitly — Joseph's diagnostic question "is there prior reasoning that illuminates what will be undone?" should be answerable from the entry itself, not buried in audit docs. **Mechanical fix bundle landed (uncommitted, lint-clean):** F-V1 math correction in two segments (verified numerically); F-V2 editorial in scope-multi-agent (C-iv-aware); F-V4 worked-example math correction in deriv-strategic-composition with substantive judgment call (introduced quadratic action-cost regularization since corrected unregularized linear $\Phi$ at corner NE has no interior contraction; flagged for follow-up review including Cournot-style alternative); F-V5 cross-component pass on scope-developer-agent integrating Class 2 caveats from logogenic-agents; P-V1 Working Notes edit; P-V2 punchline tightening with MZ bound cross-reference; P-V3 one-sentence softening. **Sub-agent provenance confusion** noted: the fix agent's retrospective summary incorrectly claimed Fixes 1–4 were "already applied before the session" — git status confirmed agent did make those edits. Worth knowing as a sub-agent failure mode (retrospective hallucination about own work). **F-V3 / F8 routing decision still open** (Path A: induce $O_c$ from relevance variable Y for C-iii; ~45–60 min, preserves unification; vs Path B: SP-21, deferred). **F-V4 follow-up review queued in TODO** (4 items: re-verify regularization algebra; attempt Cournot substitution; brainstorm other LQ alternatives; check unnoticed implications of corrected NE-at-(1,1) interpretation).

### 2026-04-24 Gemini Pressure-Point Cycle (three commits: `6102a93`, `b76ee67`, `e3d7179`)
- [project_2026_04_24_pressure_point_cycle.md](project_2026_04_24_pressure_point_cycle.md) — External Gemini audit via working notes flagged five pressure points (composition bridge lemma; IB purity / Shannon-zero / Forward-KL-infinity / reverse-KL fix "abandoned IB purity"; multiplicative ρ-factorization failed; neutral-drift blindness; missing constant C). Five primary spikes + four cross-cutting follow-ups (Instance-4 triage; Fenchel-Bregman reframe; KL-to-state-distance template; Path 1 PDF-verification). **Headline Tier 1 results:** Path 5 **Bretagnolle-Huber identity** ($D_{\mathrm{KL}} = -\log(1-\mathrm{TV})$ exact under deterministic $\pi^*$, strictly sharper than Pinsker) replaces Pinsker as primary bound in `#strategy-cost-regret-bound` §4 with matched lower bound via action-gap; §5 asymmetry-from-one-sidedness paragraph (second leg of direction-forcing); §6.3 Bregman-Fenchel identification (reverse-KL is Bregman divergence of negative-entropy; log-odds Fenchel-dual natural coordinate); §6.4 info-theoretic-MDP lineage positioning with **AAD-outlier-on-KL-direction ownership** (all three lineage papers put agent-first; AAD's π*-first forced by regret-bound + BH tightness). Path 1 *demoted* from "reverse-KL IS IB" to lineage positioning after PDF verification found Claim A contradicted at formula level (TP2011's Information-to-Go is multi-information, not KL-to-reference — that's Rubin 2012's). **Rubin 2012 Theorem 3 PAC-Bayesian bound** added as fourth independent motivation for KL-to-reference form. **DA2'-inc ≡ (CT2)-at-$M=I$ structural transparency** in `#composition-closure` makes Euclidean metric-α₁ cases AAD-internally-derived without new axiom; three-independent-obstruction convergence for adversarial regime in `#contraction-template`; structural Lipschitz-floor scope-exit for rule-based sub-scope-β in `#sector-condition-derivation`. **New appendix `#bias-bound-derivation`**: Track 1 transport-inequality $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ linear in I under LSI + Lipschitz-posterior; Track 2 Fisher-Rao universal $C_{FR} = \sqrt 2$ under (PI)+Čencov + small-I; Attempt E no-go justifies (PI) as load-bearing. Upgrades Class-2 bias bound from "order-of-magnitude guidance" to "conditional theorem." `#information-bottleneck` IB-lineage vs info-theoretic-MDP-lineage cross-reference. `#loop-interventional-access` two-mode deployment subsection (Mode 1 agent-self / Mode 2 observer-on-sub-agent; reserves Mode 3 for future I4). **Instance-4 triage:** 4 floor-candidates → 2 genuine new primary instances (C2 I4 agent-internal architecture; C4 I5 mechanism-design under broad reading) + 1 sub-statement (C1 ρ-factorization) + 1 redirect (C3 constant-C). **Fenchel-Bregman reframe (SP-9):** honest structural description is "one geometric object + four independently-motivated axioms converging on it + four segment manifestations" — richer than both naive reframe and current 1-anchor-plus-3-theorem. Tier 3 architectural proposal. **KL-to-state-distance template (SP-10):** narrow `#posterior-displacement-template` contingent on forward-looking clients. Segment count 109 → 110. Nine spike files preserved; three PDFs acquired (tishby-polani-2011-info-decision-action.pdf — singular title corrected; rubin-2012; levine-2018).

### Segment Status (April 2026)
- **AAD (01-aad-core/)**: 110 segments (per `bin/lint-outline` 2026-04-24 post-pressure-point-cycle). Stage distribution: ~13 claims-verified, ~23 deps-verified, ~73 draft. 3 missing slugs remain (`adversarial-edge-targeting`, `intent-dag-development`, `worked-example-cam`). 2026-04-24 added: #bias-bound-derivation (new appendix for Class-2 constant C).
- **TST (02-tst-core/)**: 20 segments. 4 missing slugs from earlier round are now written.
- **Section II backbone COMPLETE** — all promoted from v3 spike
- **Section III**: 13 segments written. Adversarial-edge-targeting still gap; Section III dynamics gaps from Miller + Hafez also still open (latent structural diversity, endogenous coupling, composition transition dynamics, computational thresholds, agent opacity)
- **2026-04-22 added**: `#identifiability-floor` (new meta-segment naming F1+F13 no-go pattern)
- 10 segments reset to draft after the 2026-04-22 strengthening cycle for re-review (substantive content changes)

---

*Prior cycle history: see [LOG.md](LOG.md). Prior commit/finding-level archive: see [TODO.md §Archive](TODO.md#archive--work-landed).*
