# TODO — Open Work Items

**Last reconciled:** 2026-04-23 (post-critical-mass-composition promotion + 6 brainstorm spikes landed ready-for-review). This file is the living action list.

**Cycle history (most recent first).**
- **2026-04-23 critical-mass composition promotion + brainstorm-spike landing** (commit `0d7b987`). Seven parallel research spikes launched from an external-framework comparison prompt (GAA Baigozin 2025) as a brainstorming exercise. One closed cleanly and promoted: `#critical-mass-composition` derives the composite sector constant in closed form for the symmetric-matched-Tier-1 dyad, subsuming the weakest-link bound, recovering `#team-persistence` and `#adversarial-destabilization` as signed special cases, and formalizing `#symbiogenic-composition` (S-3) as an asymmetric-parameter limit. Cross-segment strengthening to `#composition-closure`, `#team-persistence`, `#symbiogenic-composition`, `#unity-closure-mapping`, `#sector-persistence-template`. Six companion spikes landed in `msc/` ready-for-review (persistence-cost; interaction-channel classification; adaptive-gain dynamics; internal-external decomposition; consolidation dynamics; stability-induced myopia). Segment count: 97 → 98.
- **2026-04-23 SP-2 + citation audit cycle** (three commits: `7456ec3`, `6567914`, `f61e62f`). Executed Tier 1 item 1 (SP-2 meta-segment promotion) + partial Tier 1 item 2 (framing pass — CLAUDE.md §7 + OUTLINE preamble) + full citation audit project-wide. SP-2 landed as `#additive-coordinate-forcing` with the honest 1-anchor-plus-2-theorem characterization after in-flight verification narrowed Opus's 5-instance conjecture. Citation audit ran 4 parallel first-pass batches + 4 follow-up batches + 2 PDF-level Tier 1 verification agents + 1 missing-citation audit; produced 26 verified PDFs in `ref/` and zero confirmed attribution errors project-wide (reverse-KL's 20-25% rate was a local concentration in one spike, not a project-wide pattern). Segment count: 96 → 97.
- **2026-04-23 triple audit** (Codex / Gemini / Opus, post-cycle). 10 consolidated findings (F22–F31) across the three audits plus 7 session-discovered architectural proposals (SP-2 through SP-8, extending SP-1 from the strengthening cycle). ~25% of candidate findings rejected as already-adequately-caveated. See `msc/pending-findings-2026-04-23.md` and `msc/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions."
- **2026-04-22/23 cascading strengthening cycle** (nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`; plus session-close `2fc829b`). Executed Phases 1–5 + 7; landed three Cauchy-functional-equation uniqueness theorems; discovered the three-layer additive-decomposition pattern (SP-1). See Archive for per-commit detail.
- **2026-04-22 strengthening cycle** (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`). Executed strengthen-first repairs for Findings 1, 7, 10, 13 and the AI integration pass.
- **2026-04-22 triple audit (evening)**. Six findings F16–F21 (all resolved by the cascading cycle) plus nine new architectural proposals O-BP8 through O-BP16 (four of which — O-BP14, O-BP6, C-BP3, C-BP2 — landed in the cascading cycle; C-BP3 and C-BP2 were added to the portfolio in the evening batch).

The three audit cycles together mark the transition from finding-driven repair work to consolidation-and-reframing work. See §"Recommendations for next session" below for the post-2026-04-23 recommended ordering.

## Active — Pending-Review Spikes (2026-04-23 brainstorm cycle)

Six spikes landed in `msc/` from the 2026-04-23 brainstorm cycle, marked READY FOR REVIEW. My own per-spike assessment against the written content (not the agents' self-summaries). Promotion priority ranked by structural-gap-fill vs refinement-of-existing.

**One spike (H: ρ-factorization) is in flight** attacking the weakest link in spike E.

### Priority-1 promotions (fill structural gaps)

- **Spike C — Interaction-channel classification** (`msc/spike-interaction-channels.md`). **Strongest case.** Four-regime recipient-side theory (Informative / magnitude-shock / structural-shock / ambient-noise) with boundaries stated entirely in existing AAD quantities (sector-region $R_B$, model-class $\mathcal F(\mathcal M_B)$, rate $U_{o,B} \cdot \nu$). Kalman-over-Kalman derivation works four canonical cases; the II-a vs II-b split has genuinely different repair paths. Decomposition of $\rho_B^{\text{eff}}$ with negative Regime-I term generalizes `#team-persistence`'s cooperative-action term. **Closes the `#adversarial-edge-targeting` Section III gap** by pairing with it as recipient-side classifier + emitter-side optimizer. Target: new Section III segment `#interaction-channel-classification`. Caveat: $\mathcal I_\max(\mathcal M_B)$ normalization is heuristic (alternative: sufficient-statistics-span formulation). **Recommend promote.**

- **Spike F — Consolidation dynamics** (`msc/spike-consolidation-dynamics.md`). Names a regime currently only a parenthetical in `#recursive-update`. Distinguishing axis (clean): *objective* — online = one-step mismatch minimization; consolidation = IB-gap-reduction toward $\phi^\ast$. Other candidate axes (timescale, information source, scope of change) are scope conditions not distinguishing features. Exposes a real gap: AAD has plasticity lower bound $(1-\lambda) > \rho_\Sigma/R_\Sigma$ from `#strategy-persistence-schema` but no stability upper bound — the asymmetry predicts faster forgetting is always better, empirically false. Names the **stability-plasticity feasibility window**. Logogenic implications (§6) are load-bearing — three independent reasons logogenic agents need consolidation as architectural primitive. Target: new Section I segment `#consolidation-dynamics` after `#temporal-nesting`. Caveats: §3.3 structured example is sketch not theorem; stability upper bound flagged as pending derivation; identifiability-floor Instance 3 candidate is speculative. **Recommend promote as formulation-type + flag open derivations.**

- **Spike A — Persistence-cost** (`msc/spike-persistence-cost.md`). Clean bound: $\dot R_{\min} \geq n\alpha/2$ nats/time via Shannon RDF composed with Prop A.1S under Model S + Gaussian-OU. Kalman-Bucy saturates per Mitter-Newton 2005. Math is trivial (two-line composition of classical facts); value-add is AAD-framing. **Opens channel capacity as potentially first-class AAD quantity** with $C_{\text{channel}} \geq \mathcal T/2$ as persistence prerequisite — a new diagnostic lever not currently in theory, particularly binding in bandwidth-constrained settings. Three candidates correctly rejected (gain-magnitude tautological, control-effort filter-specific, Lyapunov-dissipation is conservation-law). Target: new appendix segment `#persistence-cost` OR template-cost subsection in `#sector-persistence-template`. Caveats: scope narrow (Gaussian-OU, high-resolution, steady state); sub-scope $\beta$ transfer under-justified; Landauer-branding oversold. **Recommend promote with honest scope limits.**

### Priority-2 promotions (refine existing machinery)

- **Spike D — Adaptive gain dynamics** (`msc/spike-adaptive-gain-dynamics.md`). (MG-1)–(MG-4) meta-gain decomposition is real content. Sub-scope refinement $\alpha_1$ (fixed-gain, current `#gain-sector-bridge` Prop B.3) / $\alpha_2$ (adaptive-gain under MG-1-MG-4) / $\beta$ (everything else) is a principled extension of the A2' partition. Adaptive Kalman with Mehra Q/R estimator lands in $\alpha_2$ cleanly (rate $\asymp 1/\sqrt{N}$ matching classical asymptotics); AMSGrad framed as "meta-gain repair preserving $\alpha_2$"; MAML outer-loop honestly falls to $\beta$ due to non-convexity. Augmented-state Lyapunov proof sketch in §7 is standard Khalil 4.18. Concerns: leans heavily on existing two-timescale stochastic approximation (Borkar 1997/2008) — AAD value-add is integration with `#sector-persistence-template`, not new mathematics. §4.4 fixed-point closure for RMSProp is qualitative. MAML case is classification, not derivation. Target: new segment `#adaptive-gain-dynamics` + minor edits to `#sector-condition-derivation`, `#gain-sector-bridge`, `#multi-timescale-stability`. **Recommend promote; be honest about imported machinery.**

- **Spike G — Stability-induced myopia** (`msc/spike-stability-induced-myopia.md`). R1 sub-case (within-class drift) clean: $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ follows from `#edge-update-natural-parameter`'s forced log-odds coordinate. **$1/(n+1)$ rate structurally forced through Aczél Cauchy-FE** — agent cannot escape by re-parameterizing. Strongest concrete move: **elevates forgetting prerequisite** in `#strategy-persistence-schema` from "required for asymptotic persistence" to "required for detection-latency bounded independently of operating point." Genuine sharpening. Weaknesses: R2 (model-class inadequacy) case admitted as discussion-grade; R3 basically Instance 1 restated; theorem is about signal latency not decision-theoretic deferral. Target: appendix segment or absorption — land R1 as its own result; distribute R2 and R3 as cross-references to `#credit-assignment-boundary` and `#identifiability-floor`. **Recommend compressed promotion** — keep the compact R1 result + forgetting-prerequisite sharpening; don't over-build R2/R3.

### Priority-3 promotion (blocked on ρ-factorization)

- **Spike E — Internal-external decomposition** (`msc/spike-internal-external-decomposition.md`). *Currently blocked.* Spike H (ρ-factorization) is in flight attacking the weakest link. Log-viability $\mathcal V = \log\lVert\delta_{\text{critical}}\rVert - \log R^\ast$ has a coarse form $\mathcal V = \log\lVert\delta_{\text{critical}}\rVert - \log\rho + \log\alpha$ that is exact (algebraic identity). Fine form $\mathcal V = \mathcal V_E + \mathcal V_I$ with 9 summands is robust-qualitative because the $\rho$-factorization $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is working-hypothesis, not derived. Structurally same shape as Oaxaca-Blinder (1973); log coordinate is adjacent to Cauchy-FE family, not forced. TST rotation-experiment diagnostic (§8.3) has practical teeth. Identifiability-floor Instance 3 claim is speculative pending matched-distribution construction. **If Spike H succeeds:** promote full decomposition as appendix segment with clean derivation. **If Spike H fails:** land only the coarse form as a note in `#persistence-condition` Discussion, develop TST rotation diagnostic separately, keep fine decomposition in `msc/`.

### Composition note

Spike B (critical-mass-composition, already promoted) + Spike A (persistence-cost) + Spike D (adaptive-gain) together constitute a *template-cost/template-contraction triad* under `#sector-persistence-template`. If all three land, the template's cross-instance story broadens substantially: each persistence-flavored segment inherits not just a threshold but also a cost-rate bound (A), a meta-gain contraction condition when the gain itself is adaptive (D), and — when composing — a closed-form critical-mass formula (B). A future meta-segment could name this as "template augmentation" if the pattern firms up.

## Highest-priority cleanups — LANDED (Phase 1 of strengthen-first cycle)

All four cleanups landed. F20 strengthened rather than softened; the others were mechanical cross-segment updates. Detail in Archive section below.

- ~~**F18** — `#worked-example-L1` said L1' transfer was "open"~~ — **LANDED.** Updated to cite Prop B.7 (observable-$C$ with five-way gating under facilitator monotonicity) and the Cramér-Rao refutation for unobservable-$C$ single-channel; three repair routes named.
- ~~**F19** — `#section-ii-survival` bias bound in entropy form~~ — **LANDED.** Replaced with MI form from `#observation-ambiguity-modulation`; triple-zero boundary structure made explicit (bias vanishes at $\kappa=0$ OR $\mathcal{A}=0$ OR factually-sharp observation, not just the first).
- ~~**F20** — KL-direction degeneracy in `#strategy-complexity-cost` variational form~~ — **LANDED as strengthening** (not softening). New appendix segment **#strategy-cost-regret-bound** hosts the full derivation: TV bound via bounded value range, Pinsker-KL bound, direction-forcing argument (forward-KL is vacuous under deterministic $\pi^\ast$), admissible-divergence family analysis (TV tight but non-differentiable; reverse-KL canonical-not-unique on gradient-tractability + variational-inference + Fisher-geometry + MDL-coding grounds), and the linear-vs-square-root $\beta_\Sigma$ trade-off (linear preserves IB-shape alignment; square-root would give $\beta_\Sigma \propto V_{\max}$ global naturalization). Segment-level cross-refs updated in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`. `msc/spike-f20-kl-direction-strengthening.md` retained as the reasoning trail only; framework is complete without it.
- ~~**F21** — `#identifiability-floor` frontmatter status conflicts with internal text~~ — **LANDED.** Frontmatter `status:` changed to `discussion-grade`; Epistemic Status rewritten to cleanly separate the meta-pattern (discussion-grade presentational principle) from individual instances (F1's no-go: *exact* for shallow / *robust qualitative* for general; F13's L1' refutation: *exact*).

## Active — 2026-04-23 triple audit findings and session-discovered proposals

**10 consolidated findings** from three independent de novo audits (Codex 5 + Gemini 4 + Opus 6, with cross-audit overlap on 5 of them). Full detail in `msc/pending-findings-2026-04-23.md`. Summary table:

| # | Finding | Source(s) | Severity | Subsumption |
|---|---------|-----------|----------|-------------|
| 22 | README-level scope framing outruns Section II exact theorem scope | Codex 1 + Gemini 4 partial | High | Partial by O-BP8 + SP-7 |
| 23 | "16/24 exact survival" headline compresses three distinct layer-claims | Codex 2 | High | Partial by C-BP1 |
| 24 | Strategy-edge semantics not harmonized with identifiability machinery; DAG-forced framing overclaims | Codex 3 + Opus F + Gemini 2 | High | msc/spike-edge-semantics-resolution.md "causal efficacy credence" framing is the integration target |
| 25 | `#coupled-diagnostic-framework` slides from defined to runtime-computable | Codex 4 | High | Directly by C-BP1 |
| 26 | Section III composition-closure reads more closed than self-aware status supports; Tier 3 prevalence not characterized | Codex 5 + Gemini 1 + Opus D | Medium-high | SP-6 (composition-closure consolidation) |
| 27 | Scalar tempo overcounting — foundational metric structurally additive | Gemini 3 | (already caveated; retained for visibility) | Partial by O-BP3 |
| 28 | $\rho_\Sigma$ is unmeasurable threshold parameter on which trajectory guarantee depends | Opus A | High (gap); medium (substantive vs. honest-open) | None — genuinely unaddressed |
| 29 | Update-rule heterogeneity integration debt in `#unity-dimensions` | Opus B | High (pure integration debt) | None — mechanical work |
| 30 | Stacked scope narrowings (Class 1 + learning-agent) only Class 1 visible at OUTLINE | Opus C | High | Directly by O-BP8 |
| 31 | Orient cascade 4c's signal-to-noise sensitivity not surfaced where step prescribed | Opus E | Medium | None — 30min editorial fix |

**7 session-discovered architectural proposals** (SP-2 through SP-8) in `msc/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions":

- ~~**SP-2** — Additive-coordinate-forcing meta-pattern, 5-instance (not 3).~~ **LANDED 2026-04-23** as `#additive-coordinate-forcing` meta-segment (`01-aad-core/src/additive-coordinate-forcing.md`, `type: discussion`, `status: discussion-grade`). The 5-instance conjecture was tested and narrowed to a **1-anchor-plus-2-theorem** characterization: chain layer is a mathematical identity (not a Cauchy-FE theorem); divergence and update layers are the two theorems conditional on AAD-internally-motivated axioms. Lyapunov and IB Lagrangian classified as *adjacent family members* with explicit reasoning (Lyapunov coordinate matched not forced; IB adopted from external theorem not re-derived). Cross-refs added in instance and adjacent segments. SP-1 entry in proposals doc was silently truncated; it has been replaced with a promotion pointer.
- **SP-3** — Calibration-laboratory template as prescription. Generalize #software-epistemic-properties' transfer-assumption table to a `domain-instantiation-template.md` for all domains.
- **SP-4** — Agent identity elevation from scope to architectural postulate: "AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations."
- **SP-5** — Two-tier "Reader's Path" presentation. Short load-bearing preamble per segment, preceding the formal apparatus.
- **SP-6** — Composition-closure consolidation pass. Scope bridge lemma explicitly to linear-Gaussian + exponential-family cases; adopt "AAD-shaped reduction" as the honest general claim. Repairs F26.
- **SP-7** — Epistemic architecture as the framework's distinctive contribution. All three audits converge on this reframe: AAD's value is in how it organizes scope, not in which results it integrates. Partially closes F22; composes with SP-3, SP-4, O-BP10, O-BP8 as the framework-reframing cluster.
- **SP-8** — Dual-edged identifiability-floor + separability-pattern reading. Both meta-segments present the positive half (strengthened machinery); foreground the negative half (bounded reach) equally.

**Convergent big-picture reframe** (Codex + Gemini + Opus): move the framework's center of mass from "integration of four disciplines" to "organization-of-scope under a master principle" — Codex's "bounded correction under decomposed disturbance," Gemini's "thermodynamics of purposeful systems with coupling as primary geometric variable," Opus's "epistemic architecture as distinctive contribution." These are not the same proposal but they are on the same axis.

### Actionable from the audit batch

- **F29** (unity-dimensions two-axis integration) — **pure mechanical work**, 45–90 min. Should land first in next session as a confidence-building cleanup.
- **F31** (orient cascade 4c sensitivity note) — 30 min editorial. Small cleanup.
- **F25** (coupled-diagnostic-framework runtime vs. analytical) — 60–90 min editorial *or* wait for C-BP1 landing and handle together.
- **F30** (OUTLINE scope lattice) — 20–40 min editorial; composes naturally with O-BP8 if Phase C framing pass is pursued.

### Requires scoping or substantive work

- **F22 + SP-7** — README + CLAUDE.md + OUTLINE preamble rewrite as a coordinated framing pass. 1–2 sessions. Incorporates the convergent big-picture reframe.
- **F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to segments; soften `#strategy-dag`'s "DAG-forced" language; foreground causal sufficiency as scope condition. 1 session.
- **F26 + SP-6** — Composition-closure consolidation pass. 2–3 sessions + optional scoping spike.
- **F28** ($\rho_\Sigma$) — Strengthen-first spike attempting to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. 1–2 sessions.
- **F23** — "16/24 exact survival" per-layer breakdown. Coordinate with C-BP1 three-layer separation to avoid redoing work. 1 session.

### Supersedes prior planning

~~SP-2 supersedes the three-instance meta-segment promotion (Phase B in the prior recommended sequence).~~ **Phase B is closed.** The meta-segment landed with honest 3-primary + 2-adjacent characterization. Future extensions on this axis live in `#additive-coordinate-forcing` Working Notes (candidate future layers at credit-assignment, composition-closure-defect, shared-intent compression; each would require its own AAD-internal axiom + Cauchy-FE derivation).

SP-7 + SP-3 together partially fulfill Phase C (framing pass), which is now deepened rather than replaced — the OUTLINE/CLAUDE.md rewrite should incorporate the convergent reframe at the same time as it adds the scope lattice (O-BP8) and the template-as-organizing-principle (O-BP1) content.


## Recommendations for next session (updated post-2026-04-23 audit)

What follows is one agent's prioritization after the 2026-04-23 audit. Joseph's call which to follow.

### Session gains (what landed; refresh of session character)

The 2026-04-22/23 cycle ran Phases 1–5 + 7 of the proposed sequence, plus two unplanned in-flight strengthening spikes surfaced during the work. Nine commits delivered:

- **Three new uniqueness theorems**, each forcing a logarithmic coordinate via a Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom: (i) F20 regret-bound derivation (reverse-KL direction forced); (ii) reverse-KL chain-rule uniqueness (Csiszár 1991 / Shore-Johnson 1980 / Hobson 1969, under chain-rule-additivity axiom); (iii) evidential-additivity uniqueness of log-odds (Aczél 1966 Cauchy-functional-equation argument, under evidential-additivity axiom).
- **Discovered structural pattern** — the three theorems share a common shape. Documented as SP-1 during the cycle; **promoted to `#additive-coordinate-forcing` meta-segment 2026-04-23** with honest 1-anchor-plus-2-theorem characterization (chain layer = mathematical identity; divergence, update = theorems conditional on AAD-internal additivity axioms; Lyapunov + IB Lagrangian classified as adjacent family members with explicit reasoning).
- **Scope partitions sharpened.** A2' α/β sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex = α derived; PID/rule-based/human-judgment = β assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).
- **Three new meta-segments or promotions.** `#separability-pattern` (positive-half complement to `#identifiability-floor`, six ladders enumerated); `#agent-identity` promoted to formal scope (type: scope, status: robust-qualitative); `#edge-update-natural-parameter` (uniqueness theorem + scope condition).
- **O-BP14 derivation-table convention** landed in `FORMAT.md` with tables applied to five derivation segments.
- **C-BP3 TST reframing** as calibration laboratory with transfer-assumption table.
- **Citation audit** ran on the reverse-KL uniqueness work: three wrong attributions (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 — none contain the chain-rule uniqueness theorem) corrected to Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975 with PDFs saved to `ref/`. Eguchi 1983 venue corrected. Three-layer-pattern discovery now rests on defensible citations.

Segment count: 93 → 96 (added `#identifiability-floor` before this cycle; `#strategy-cost-regret-bound`, `#separability-pattern`, `#edge-update-natural-parameter` this cycle). Stage distribution: ~13 claims-verified, ~23 deps-verified, ~59 draft.

### Recommended sequence for next session (updated 2026-04-23)

**Phase α — Quick wins first (1 session total).** Confidence-builders and pure integration debts:
- **F29** — `#unity-dimensions` two-axis integration (45–90 min). Pure mechanical work landing `msc/spike-unity-closure-mapping.md`'s Option C into Formal Expression.
- **F31** — `#orient-cascade` step 4c practical-sensitivity note (30 min).
- **F21-follow-up / F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to `#strategy-dag`; soften "DAG-forced" language to match `#graph-structure-uniqueness`'s sufficiency-only content (1 session).

**Phase A — CLOSED 2026-04-23.** Project-wide citation audit completed across 3 commits (`7456ec3`, `6567914`, `f61e62f`). Zero confirmed attribution errors. 26 PDFs in `ref/`. 5 missing-citation gaps hardened. See §"Citations Audit — COMPLETE 2026-04-23" above for detail.

**Phase B — CLOSED 2026-04-23.** The `#additive-coordinate-forcing` meta-segment landed with the honest 1-anchor-plus-2-theorem characterization. Opus's 5-instance conjecture was tested and narrowed: Lyapunov and IB Lagrangian are documented as *adjacent family members* rather than primary instances, with explicit reasoning (Lyapunov's quadratic coordinate is a formulation choice matched to the sector condition, not forced by it; IB is adopted from Tishby-Pereira-Bialek 1999 as applied external theorem rather than re-derived under AAD-internal axioms). Cross-refs added in five home segments; SP-1 entry in proposals doc promoted from truncated-table to promotion-pointer.

**Phase C — Coordinated framing + reframe pass (PARTIAL 2026-04-23; 1-2 sessions remaining).** Part 1 landed in commit `7456ec3`: CLAUDE.md §7 expanded from "Honesty as architectural principle" to "Epistemic architecture as AAD's distinctive contribution" with the convergent Codex/Gemini/Opus reframe and the seven elements of AAD's epistemic architecture explicitly named; `01-aad-core/OUTLINE.md` acquired a new "Reading AAD" paragraph framing the theory at both integration and distinctive levels with the three meta-segments as cross-sectional structure.

**Part 2 (remaining) — segment-level moves:**
- **SP-7** (epistemic architecture foregrounding): README.md public-facing reframe incorporating the convergent audit observation. Partially closes F22.
- **O-BP10** (projection-contraction slogan): "adaptive system = projection whose contraction exceeds target's drift." Promote to segment-level content in `#sector-persistence-template` or a new organizing-principle segment.
- **O-BP1** (template as organizing principle): OUTLINE preambles get refreshed framing around disturbance decomposition at scales. Composes with O-BP10 and the additive-coordinate-forcing meta-segment.
- **O-BP8** (explicit scope lattice): name the adaptive → agency → learning-purposeful → Class-1-modular → coupled/logogenic lattice once as a scope-lattice segment or canonical paragraph in `#scope-condition`. Closes F16 and F30.
- **SP-3** (calibration-laboratory template generalization): write `domain-instantiation-template.md` or FORMAT.md section prescribing the transfer-assumption table format. Composes with O-BP8.
- **SP-4** (agent identity to architectural postulate): elevate `#agent-identity` frontmatter from scope to postulate; rewrite Formal Expression to state the commitment ("AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations").

Estimated 1-2 sessions for Part 2. Tracked as task #8.

**Phase D — Composition-closure consolidation (SP-6; 2–3 sessions).** Repairs F26. Scope the bridge lemma explicitly to linear-Gaussian + exponential-family Tier-1 cases; adopt "composite agents are AAD agents iff effective dynamics admit an AAD-shaped reduction" as the honest general claim. Scoping spike valuable first. Downstream of Phase A (citation audit; especially on `#composition-closure`'s Khalil/Khasminskii citations).

**Phase E — Substantive spikes (choose by priority):**
- **F28 strengthening spike** ($\rho_\Sigma$ operationalization, 1–2 sessions). Attempt to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. Addresses the deepest substantive finding in this audit batch.
- **O-BP11 observability master-variable falsification spike** (deepest structural insight from the earlier cycle; not yet attempted).
- **Phase 2.5 B.5d uniqueness spike** (potential additional instance of SP-2 pattern).
- **Phase 9 C-BP1 + C-BP4 epistemic separation** (three-layer separation + claim-level statuses; partially addresses F23 and F25; composes with O-BP14 tables).

**Phase F — SP-5 "Reader's Path" two-tier presentation (1–4 sessions).** After Phase C framing pass stabilizes. Short load-bearing preamble per segment; incremental application.

**Phase G — SP-8 dual-edged floor/separability reading (1 session).** Framing touch on `#identifiability-floor` + `#separability-pattern`. Composes with SP-7.

### What to defer

- **G-BP3 (Fisher-information unification)** — large multi-session rewrite. Gemini's Riemannian-manifold reaffirmation strengthened the case but did not change the scoping cost. G-BP1 partial execution (Path B uniqueness theorem landed) reduces the remaining G-BP3 scope somewhat.
- **G-BP2 V-strong** (full reformulation as variational free energy) — paper-writing-time decision per `msc/spike-active-inference-vs-aad.md` §I action 5. Not theoretical-development work.
- **O-BP4, O-BP5, O-BP15, O-BP16** — substantial structural work each.
- **O-BP12 (resource budget $B_t$)** — interesting but piecewise treatment currently works.
- **O-BP13 (Cox-necessity)** — worth a 1–2 session spike but not high-priority.
- **Full Props B.1–B.7 restatement in log-odds** — the G-BP1 spike showed this is not required for Finding 2 (Fisher-equivalent in moment parameters). Deferred to a future G-BP3 Fisher-unification session.

### Strategic observation (updated)

The 2026-04-22/23 cycle ran at a different depth than the prior cycle. The prior cycle was 3:1 promoting-to-creating (per CLAUDE.md's "convergent depth over generative breadth" principle). This cycle was closer to 2:1 — six framing/consolidation moves (cleanups, O-BP14 tables, C-BP3 calibration lab, C-BP2 separability pattern, O-BP6 identity promotion, citation audit) plus three genuinely-new derivations (F20 regret bound, reverse-KL chain-rule uniqueness, log-odds evidential-additivity uniqueness). The denser output is acceptable because the three new derivations were not independent — they share the Cauchy-functional-equation structure, and discovering the shared structure was itself a consolidation move.

The recommended next session should rebalance toward consolidation: Phase A (citation audit) is pure consolidation; Phase B (three-layer meta-segment) is naming-the-obvious; Phase C (framing pass) is editorial. Phase D opens to substantive structural work only after the consolidation layer is stable.

The pattern becoming visible: AAD's strengthening cycles alternate between *depth* (new theorems) and *breadth-compression* (consolidation and naming). This cycle was depth-heavy; the next should be breadth-compression-heavy. If this alternation continues, it may itself be a project-level discipline worth naming in CLAUDE.md.


## Citations Audit — COMPLETE 2026-04-23

**Result: zero confirmed attribution errors project-wide.** The reverse-KL audit's 3-wrong-out-of-16 rate was a local concentration in that one spike's citations; the broader corpus is clean. Three commits closed the audit project:

- `7456ec3` — SP-2 landing + framing-pass subset (initial SP-1 truncation fix in proposals doc)
- `6567914` — Tier 1 verification: 3 framing refinements + Morozova-Chentsov completion + ref/ rename hygiene
- `f61e62f` — Missing-citation hardening: Tikhonov / Chechik / Doob-Dynkin / Cox / Cramér added

**What was audited.** Four first-pass Explore batches covered every `*[Derived]*`, `*[Proved]*`, and external-theorem citation across 01-aad-core and 02-tst-core. Four follow-up agents with curl-into-ref/ workflow closed the E-verdict backlog. Two PDF-level Tier 1 verification agents confirmed the highest-risk attributions (Bruineberg's "Pearl-blanket vs Friston-blanket" terminology is VERBATIM, with credit to Martin Biehl in footnote 3; Bareinboim CHT = Theorem 1 p.22 of the 2022 ACM Books chapter; Aguilera's FEP-narrow-validity claim exactly matches AAD's usage).

**26 PDFs in `ref/`.** Canonically named (`{author}-{year}-{short}.pdf`). Load-bearing external theorems covered: Khalil 2002, Khasminskii 2012, Nesterov 2004, Pearl 2009, Lauritzen 1996, Spirtes-Glymour-Scheines 2000, Bareinboim 2022, Cover-Thomas 2006 (textbook), Tishby 1999, Chechik 2005, Csiszár 1991, Shore-Johnson 1980, Hobson 1969, Eguchi 1983, Aczél & Daróczy, Ay et al. 2017, all Friston lineage (2010/2013/2017/2019/2023), Da Costa 2020, Sajid 2021, Parr-Pezzulo 2022, Aguilera 2022, Bruineberg 2022, Sun-Firestone 2020, Clark 2013, Wiener 1948, Hafez 2026, Miller 2022. Amari 2009 and Amari-Cichocki 2010 already retained from the reverse-KL audit.

**Framing refinements landed** (commit `6567914`): (1) Eguchi 1983 attribution is now "the differential-geometric framework in Eguchi 1983" not "Eguchi's theorem" (Theorem 3 is about estimator efficiency; the f-divergence/Fisher-metric result is in §2 contrast-function machinery); (2) Sun & Firestone 2020 direction-of-inference clarified (they diagnose, AAD responds); (3) Friston 2023 labeled as the path-integral methodological extension; Friston 2019 named as the primary NESS source.

**Missing-citation hardening landed** (commit `f61e62f`): Tikhonov 1952 + Khalil 2002 Ch 11 (singular perturbation) to `#temporal-nesting` and `#multi-timescale-stability`; Chechik 2005 full citation to `#compression-operations`; Kallenberg 2002 footnote in `#recursive-update-derivation` (Doob-Dynkin); Cox 1946 + Jaynes 2003 in `#graph-structure-uniqueness` and `#strategy-dag`; Cramér 1946 in `#identifiability-floor` and `#strategic-dynamics-derivation`.

**Spike-to-segment promotion fix** (commit `6567914`): Morozova & Chentsov 1991 citation completed in `#strategy-cost-regret-bound` §6.2 by importing the full form from `msc/spike-reverse-kl-uniqueness.md` ("Markov invariant geometry on state manifolds," *Itogi Nauki i Tekhniki*, translated in *J. Sov. Math.* 56(5):2648-2669).

**Residue (acceptable):** 3 emphasis-vulnerable linter warnings in `#strategic-dynamics-derivation` on dense table-row math (lines 346, 501, 507) — fixing requires math restructuring that exceeds citation-hardening scope. Miller 2022 `Ex_Machina` specific chapter/section/table loci (§3.3, Ch 1, Table 12.2) not independently PDF-verified; book is in `ref/miller-2022-ex-machina.pdf` if a future spot-check is desired.


## Active — Strategic Architectural Proposals

Architectural moves from the 2026-04-22 portfolio (`msc/architectural-proposals-2026-04-22.md`). Six proposals from the portfolio have now landed (O-BP14, O-BP6, C-BP3, C-BP2, G-BP1 partial, G-BP2 V-medium); the three-layer additive-decomposition pattern was discovered as a by-product and is now documented in the proposals doc (§SP-1 "Discovered structural patterns"). Remaining proposals are evaluated on their own merits.

### Landed in the 2026-04-22/23 strengthening cycle

- **O-BP14 — Derivation-audit-table convention.** **LANDED** (commit c1d9fcf). FORMAT.md carries the convention; tables applied to #strategy-cost-regret-bound, #recursive-update-derivation, #sector-condition-derivation, #strategic-dynamics-derivation, #composition-closure. Surfaced A2' α/β ambiguity (→ A2' strengthening spike) and B.5d minimal-scheme claim (→ Phase 2.5 parked).
- **O-BP6 — Identity promotion.** **LANDED** (commit 2980327). #agent-identity promoted to type:scope / status:robust-qualitative; three consequences named; #loop-interventional-access + #model-sufficiency carry cross-refs. Closes Finding 5 end-to-end.
- **C-BP3 — Software as calibration laboratory.** **LANDED** (commit d0373fc). #software-epistemic-properties + 02-tst-core/OUTLINE preamble reframed; transfer-assumption table for five AAD-core quantities. Closes Finding 15.
- **C-BP2 — Master separability pattern.** **LANDED** (commit 72ca532). New meta-segment #separability-pattern (positive-half complement to #identifiability-floor, six ladders enumerated). Three-part characterization of AAD scope: #independence-audit + #approximation-tiering + #separability-pattern. Composes with future O-BP1 + O-BP10.
- **G-BP1 — Logit reparameterization (partial).** **PARTIALLY EXECUTED** (commit a39dfb7). Scoping confirmed narrow scope (only #credit-assignment-boundary required substantive work); Path B strengthening yielded the **evidential-additivity uniqueness theorem** in new appendix segment #edge-update-natural-parameter (log-odds forced via Cauchy functional equation, AAD-internally motivated as the update-level analog of #chain-confidence-decay). Finding 2 resolved by restating default signal in log-odds (domain = ℝ, no mechanical break). Interface notes in #strategy-dag + #edge-update-via-gain. Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent). Full sweep deferred to future G-BP3 Fisher-unification session.
- **G-BP2 V-medium** (prior cycle, commit a14642e). KL-form in #strategy-complexity-cost; this cycle added the **regret-bound derivation of KL direction** (commit 0a772d2, new appendix #strategy-cost-regret-bound) and the **chain-rule uniqueness theorem** (commit f70fb68; citations corrected in commit e777f01). V-strong still an open paper-writing-time decision.

### Not yet landed — smaller / approachable

- **O-BP1 — Sector-persistence template as organizing principle.** Reframe OUTLINE preamble around "AAD decomposes disturbance for bounded-correction dynamics at each scale." Subsumes Finding 9 (Section II preamble). 1–2 sessions, framing touch, low risk. Now sharpened by the three-layer additive-decomposition pattern (§SP-1): O-BP1's "disturbance decomposition at scales" reads cleanly once readers know AAD has a forced-logarithmic-coordinate move at three layers. **Natural next move after Phase B (SP-1 meta-segment).**

### Not yet landed — larger / scoping required

- **G-BP3 — Fisher-information unification of tempo and gain.** The largest single move in the portfolio. Major rewrite; scoping spike essential. The 2026-04-22 AAD-vs-AI positioning spike increased the case for keeping AAD's Lyapunov/sector-condition machinery distinct from the FEP-flow apparatus. G-BP1 partial-execution shrinks the remaining scope somewhat (log-odds coordinate already landed).
- **O-BP3 — Continuous-parameter approximation tiering.** L0/L1/L1'/L2, C1/C2/C3, Tier 1/2/3 as continuous parameter spaces. Partial on Finding 11 (now closed by F1's no-go strengthening).
- **O-BP4 — Continuous-valued strategy DAG.** Dedicated scoping spike recommended.
- **O-BP5 — Orient cascade as recursive adaptive cycle.** Strengthens composition-consistency.
- **O-BP7 — Known structural absences (meta-proposal).** Treat alongside #identifiability-floor §"Adjacent Floors" as parallel research agendas.

### Larger / scoping required

- **G-BP1 — Natural-parameter / logit reparameterization.** Fixes Finding 2 (unbounded gradient). **Partially executed 2026-04-22** (`msc/spike-gbp1-logit-scoping.md`): scoping confirmed narrow scope (only `#credit-assignment-boundary` required substantive work); Path B strengthening yielded the evidential-additivity uniqueness theorem in new appendix segment `#edge-update-natural-parameter` (update-level analog of #chain-confidence-decay, parallel to reverse-KL uniqueness under chain-rule axiom); `#credit-assignment-boundary` default signal restated in log-odds (domain = ℝ, no mechanical break); interface-notes added to `#strategy-dag` and `#edge-update-via-gain`; Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent). Full sweep (restating Props B.1-B.7 in log-odds) still open but motivated by G-BP3 Fisher unification rather than Finding 2.
- **G-BP3 — Fisher-information unification of tempo and gain.** The largest single move in the portfolio. Major rewrite; scoping spike essential. The 2026-04-22 AAD-vs-AI positioning spike (`msc/spike-active-inference-vs-aad.md` §C.1, §H Underclaim 1) increased the case for keeping AAD's Lyapunov/sector-condition machinery distinct from the FEP-flow apparatus — G-BP3 needs to engage that.
- **O-BP3 — Continuous-parameter approximation tiering.** L0/L1/L1'/L2, C1/C2/C3, Tier 1/2/3 as continuous parameter spaces. Subsumed continuous-convention tier-C item. Partial on Finding 11 (now mostly closed by F1's no-go strengthening, since L0→L1 escalation is now derived).
- **O-BP4 — Continuous-valued strategy DAG.** Edges carry expected-progress rates; nodes aggregate progress fields. Dedicated scoping spike recommended.
- **O-BP5 — Orient cascade as recursive adaptive cycle.** Strengthens composition-consistency. No findings directly subsumed.
- **O-BP7 — Known structural absences (meta-proposal).** Tier-switching policy, misspecification cost, cross-hierarchy monotonicity, CIY/EIG. The 2026-04-22 #identifiability-floor segment's §"Adjacent Floors" partially restates these; treat O-BP7 and §"Adjacent Floors" as parallel research agendas.

### Layered with C-BP1 + C-BP4

- **C-BP1 — Three-layer epistemic separation (defined / causally valid / operationally extractable).** Subsumes Finding 12; partial on 9 and 14. Scoping spike worthwhile.
- **C-BP4 — Claim-level epistemic statuses.** Convention extension. Pairs with C-BP1.

### Conceptually executed (but not in segment form)

- **G-BP2 V-medium executed.** The variational form of the strategy IB objective landed in `#strategy-complexity-cost` (KL-divergence replacing Shannon-MI; closes Gemini Finding 2/3) plus a paragraph in `#compression-operations` plus Discussion-level cross-refs in `#exploit-explore-deliberate` and `#ciy-unified-objective`. V-strong (full reformulation as VFE master objective) was deliberately not pursued and remains an open paper-writing-time decision per `msc/spike-active-inference-vs-aad.md` §E.
- **O-BP2 partially executed.** The synthesis-segment route was taken in 2026-04-21 (`#compression-operations` is the result). Full four-segment rewrite remains open; `msc/spike-ib-unification-plan.md` remains the record. The §H Overlap 2 honest credit landed in the 2026-04-22 AI integration commit.

### Proposal clusters (from original portfolio)

- G-BP1 + G-BP3 + O-BP3 (natural parameters + Fisher geometry + continuous tiering)
- G-BP1 + O-BP4 (logit + continuous DAG)
- O-BP1 + O-BP5 + O-BP6 (template + recursion + identity — "recursive persistence on singular trajectories")
- C-BP1 + C-BP4 (three-layer framework + claim-level implementation)
- O-BP1 + C-BP2 (result-level + epistemic-posture organizing principles)

### Post-strengthening evening additions (2026-04-22)

A second triple-audit cycle surfaced nine genuinely new architectural proposals plus several substantive *extensions* to existing proposals. The extensions to existing proposals — Gemini's Riemannian-manifold framing of G-BP1+G-BP3, Codex's "predictive relevance under bounded loss" framing of O-BP2, Gemini's Class 2 dissolution under O-BP2, Gemini's explicit $\lambda, N_r, \mu \in [0,1]$ form of O-BP3, Codex's alternative three-layer phrasing for C-BP1, Opus's six-ladder expansion of C-BP2 and the positive-half complementarity with `#identifiability-floor`, and Opus's O-BP1 + O-BP2 → Section III pull-up path — are documented in `msc/architectural-proposals-2026-04-22.md` "Extensions to existing proposals." When considering whether to scope or execute any of those existing proposals, read the extensions first — they substantially expand the case for several of them. The genuinely new proposals are below.

**Smaller / approachable (high payoff per effort):**

- **O-BP14 — Per-segment "what's derived vs. chosen vs. assumed" table convention.** `#graph-structure-uniqueness` lines 154–165 already carries this and it's the clearest epistemic signal in the repo. FORMAT.md convention extension + incremental per-segment application. **Probably highest-payoff-to-effort move in this batch.** Pairs with C-BP4. 30 min for convention + ~10 min per segment.
- **O-BP8 — Explicit scope lattice as named-once-and-reused object.** Adaptive → agency → learning-purposeful → exact Section II modular → coupled/logogenic. State once, reference everywhere. Subsumes Finding 16. 1-session scoping spike + 30–60 min application.
- **O-BP10 — Projection-contraction framing of sector-persistence template.** "An adaptive system is a projection whose contraction rate exceeds its target's drift rate." Composes with O-BP1 (result-level) and C-BP2 (posture-level) as the three-tier organizing-principle stack. **One of the most concise potential restatements of the entire theory available.** 1–3 sessions for preamble + template touch + comprehensive naming pass.
- **O-BP9 — Typed admissibility for composition** (model-only / goal-bearing / strategy-bearing × Tier). Subsumes Finding 8 cleanly; partial on Finding 17. 1–2 session scoping spike.

**Larger / scoping required:**

- **O-BP11 — Observability as master variable across the theory.** Across L1' refutation, P4, P6, B.2/B.3, observability-dominance, directed-separation κ_processing, loop-interventional-access, shared-intent, TST P6 — observability appears as a recurring master variable currently presented as separate machinery in each instance. **Probably the deepest available structural insight from the audit cycle.** Substantial: scoping spike essential, 4–6 sessions if pursued in segment form. **Largest available reorganization** in the current portfolio.
- **O-BP12 — Resource budget $B_t$ as master variable for bounded rationality.** Currently piecewise (DL of Σ_t, deliberation cost, η* capacity-dependence, context-window limits, β_Σ calibration); a single $B_t$ would let those derive rather than be separately postulated. Adjacent to O-BP7. 1–2 session scoping spike + 2–3 sessions if pursued.
- **O-BP13 — Cox-parallel necessity for `#graph-structure-uniqueness`.** Currently sufficiency-only; necessity direction probably reachable via Lauritzen's characterization of Markov properties on different graph classes. 1–2 session dedicated spike.
- **O-BP15 — Comprehensive "minimal proof of viability" worked example.** Single concrete instantiation hitting every Section I/II result. Should follow O-BP1 + O-BP2 framing stabilization. 3–4 session content effort.
- **O-BP16 — Population-level Lyapunov dynamics** (for Section III). Tracks distribution of correction architectures and endogenous coupling rather than per-agent static bounds. Closes "neutral drift" blindness flagged by `msc/spike-neutral-drift-lyapunov.md`. Adjacent to existing Section III gaps (latent structural diversity, endogenous coupling). Major: scoping spike essential, 4–6 sessions if pursued.

### Updated recommended ordering (post-evening-audit)

Smallest-payoff-to-effort, with the four immediate cleanups above pre-required:

1. **F18 + F19 + F20 + F21 cleanup** (highest-priority cleanups section). 1–2 hrs total.
2. **O-BP14** (derivation-table convention) — 30 min convention + first batch.
3. **O-BP1** (template as organizing principle) — framing touch, low risk.
4. **O-BP10** (projection-contraction framing) — composes with O-BP1; can land in same pass.
5. **O-BP6** (identity promotion) — one session, localized.
6. **O-BP8** (scope lattice naming) — composes with O-BP1; closes F16.
7. **C-BP3** (software calibration laboratory) — 45–90 min editorial.
8. **C-BP2** (master separability pattern) — pairs with O-BP1 + O-BP10.
9. **G-BP1** (logit reparameterization) — fixes Finding 2's residual gradient issue.

The larger reorganizations (O-BP11 observability-master, O-BP12 resource-budget, O-BP13 Cox-necessity, O-BP15 comprehensive-worked-example, O-BP16 population-Lyapunov, G-BP2 V-strong, G-BP3 Fisher-unification, O-BP3 continuous-tiering, O-BP4 continuous-DAG, O-BP5 recursive-AAD, O-BP2 four-compressions full) remain longer-term scoping work. **O-BP11 (observability as master variable) deserves first attention among these** as the deepest available structural insight — even if not pursued, the scoping spike would surface what AAD's observability machinery actually is across the theory.


## Active — Pending Findings

The 2026-04-22 batch had 15 findings; the strengthening cycle resolved 4 directly and resolves several others through subsumption. Updated table below; see `msc/pending-findings-2026-04-22.md` for the original characterizations.

### 2026-04-22 batch — current status

| # | Finding | Status |
|---|---------|--------|
| 1 | L0 residual under on-policy execution | **RESOLVED** by strengthening (commit 14a6095): no-go theorem in #causal-insufficiency-detection |
| 2 | Unbounded gradient in credit-assignment signal | **RESOLVED** by G-BP1 scoping + partial execution (`msc/spike-gbp1-logit-scoping.md`): Path B evidential-additivity uniqueness theorem landed in new appendix segment #edge-update-natural-parameter (parallel to reverse-KL uniqueness under chain-rule axiom); #credit-assignment-boundary default signal function restated in log-odds (domain = ℝ, no mechanical break); #strategy-dag and #edge-update-via-gain carry parallel-presentation notes; #strategic-dynamics-derivation Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent). Full G-BP1 sweep deferred; current scope narrow + strengthened |
| 3 | Degenerate MI in strategy IB objective | **RESOLVED** by V-medium G-BP2 (commit a14682e): KL-form replaces Shannon-MI in #strategy-complexity-cost |
| 4 | Section II silent scope narrowing (agency → learning) | Open. 45–60 min reconciliation. Coordinate with Finding 9 for combined Section II preamble pass (or absorb both into O-BP1 framing pass) |
| 5 | Loop framing overstates Level 2 access | **RESOLVED** by O-BP6 identity promotion (commit 2980327): #agent-identity now a formal scope statement (type: scope, status: robust-qualitative); #loop-interventional-access depends on it and carries an explicit singular-trajectory-ground paragraph. F5 closed end-to-end |
| 6 | Composition timescale heuristic outruns bridge conditions | Open. 30–45 min scope-narrowing in #composition-consistency |
| 7 | TST overstates git as complete chronica | **RESOLVED** by strengthening (commit b6134c2): per-quantity exactness audit + conditional maximality + $\mathcal{C}_t^{\text{commit}}$ in #software-epistemic-properties |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision |
| 9 | Section II preamble framing understates survival | Open; absorbed if O-BP1 framing pass executed. 30 min standalone |
| 10 | `#information-bottleneck` status mismatches unification role | **RESOLVED** (commit a14682e): status reclassified from discussion-grade to exact (applied external theorem) |
| 11 | Orient cascade step 4c convergence in non-stationary envs | **PARTIALLY RESOLVED** by F1 strengthening: #causal-insufficiency-detection no-go reframes step 4c as the unique broadly-available diagnostic. Step-4c sanity edit in #orient-cascade itself remains optional cleanup |
| 12 | Section II survival slides from statement-level to operational | Open. Subsumed by C-BP1 (three-layer epistemic separation) |
| 13 | `#strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite | **RESOLVED** by strengthening (commit 4d050c8): Prop B.7 derives L1' transfer for observable $C$ with five-way gating; refutes unobservable-$C$ via Cramér-Rao floor; #strategy-dag headline + Correlation Hierarchy table updated |
| 14 | `#developer-as-act-agent` exact-status mismatch (human vs AI regimes) | Open. Option A (15–30 min status downgrade) is straightforward regardless of C-BP4 |
| 15 | Software "richest operationalization domain" headline overclaims | **RESOLVED** by C-BP3 calibration-lab reframing (commit d0373fc): #software-epistemic-properties headline rewritten; 02-tst-core/OUTLINE preamble updated; transfer-assumption table makes non-software identification relaxations explicit |

### Actionable now (independent of remaining portfolio decisions)

- **Finding 4 + 9 coordinated pass** — Section II preamble + scope-narrowing. 60–90 min combined; or absorbed by O-BP1.
- **Finding 6** — composition-consistency scope-narrowing. 30–45 min.
- **Finding 8** — (C-iii) Option A vs Option B decision needed before edit.
- **Finding 14 Option A** — `#developer-as-act-agent` status downgrade. 15–30 min.

### 2026-04-22 evening batch — six new findings (all resolved)

Three independent de novo audits (Codex, Gemini, Opus) ran *after* the morning strengthening cycle and surfaced six new findings. The 2026-04-22/23 strengthening cycle resolved all six (F18-F21 in the Phase 1 cleanup commit; F16 partial, F17 partial). Status table:

| # | Finding | Source | Severity | Status |
|---|---------|--------|----------|--------|
| 16 | Section II scope lattice underspecified across segments | Codex F1 (evening) | Medium | Open; subsumed by O-BP8 in future Phase C framing pass |
| 17 | `#coupled-diagnostic-framework` operational-computability overclaim | Codex F4 (evening) | Medium-high | Open; subsumed by C-BP1 three-layer separation (future Phase 9) |
| 18 | `#worked-example-L1` says L1' transfer "open" — STALE after F13 strengthening | Gemini F1 (evening) | Medium | **RESOLVED** (commit 0a772d2): updated with Prop B.7 + Cramér-Rao refutation + three repair routes; facilitator monotonicity surfaced as load-bearing |
| 19 | `#section-ii-survival` bias bound in entropy form, stale after 2026-04-21 Finding B | Gemini F3 (evening) | Medium | **RESOLVED** (commit 0a772d2): MI form + triple-zero boundary structure made explicit |
| 20 | KL-direction degeneracy in `#strategy-complexity-cost` variational form (introduced by V-medium) | Opus F1 (evening) | High | **RESOLVED AS STRENGTHENING** (commits 0a772d2, f70fb68, e777f01): new appendix #strategy-cost-regret-bound with regret-bound derivation (direction forced) + chain-rule uniqueness theorem (specific divergence uniquely forced) + corrected citations |
| 21 | `#identifiability-floor` frontmatter status conflicts with internal text | Opus F3 (evening) | Low | **RESOLVED** (commit 0a772d2): status → discussion-grade; Epistemic Status rewritten cleanly separating meta-pattern from instances |

**Reaffirmed (not new):** Codex F2 evening reaffirms F6 (composition timescale heuristic); Codex F3 evening reaffirms F8 ((C-iii) gap); Opus F2 evening reaffirms F14 (developer-as-act-agent status). Several other candidate findings were *rescinded* by the audits themselves on in-segment counterevidence — see `msc/pending-findings-2026-04-22.md` and the audit transcripts for the transparency tables.

### 2026-04-21 batch — both RESOLVED 2026-04-22 (historical, from earlier in the day)

Finding A (composition-closure temporal coarse-graining) and Finding B (observation-ambiguity-modulation architecture-contamination) — both closed in the morning's audit-trio commits before the strengthening cycle. See `msc/pending-findings-2026-04-21.md` for the closed-out resolution notes.


## Active — Tier-C Deferrals

- **$G_t$ as single object; $(O_t, \Sigma_t)$ as a property** (Opus 2026-04-21 synthesis §7). Touches Section II scaffolding. **Defer until more Class 2 logogenic work lands.** Strengthened by O-BP2 (compressions-as-projections); if O-BP2 is pursued, this item converges with it.
- **Continuous convention hierarchy** $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). Subsumed by O-BP3 (continuous-parameter tiering) — handled there if O-BP3 is pursued.


## Active — Genuinely Open MEDIUM Items

- **Composition scaling with $N$.** Whether closure defect scales polynomially or exponentially with team size. **Scoping spike done** (`msc/spike-composition-scaling-N.md`, 2026-04-22): four readings identified, five candidate first moves, two composing axes ($K_c$ macro-timescale; unity × update-heterogeneity). Question is well-framed but unresolved; execution deferred. Critical for large-team applications.

- **Multi-timescale stability formalization.** `#multi-timescale-stability` is stage `sketch`; `#temporal-nesting` leans on it. Needs formal $N$-timescale singular perturbation treatment. Partially overlaps with the 2026-04-21 Finding A repair path if Option 2 (Tikhonov) is later chosen.

- **Communication-gain adversarial scope.** `#communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation.

- **Exploit/Explore/Deliberate spike findings.** `#exploit-explore-deliberate` was written, but the adversarial spike (`msc/spike-three-way-tradeoff.md`) noted that the two-stage decomposition and $\Delta V_\Sigma$ approximation are hand-waving. Segment may be substantially rewritten. The 2026-04-22 AI integration added an EFE pragmatic/epistemic + sophisticated-inference cross-reference; the rewrite question remains.

- **Adjacent identifiability floors** (`#identifiability-floor` §"Adjacent Floors", added 2026-04-22). Three open extensions: (1) causal-IB for interventional relevance variables (Wieczorek-Roth 2017 and follow-ups); (2) misspecification-cost quantification under finite information budget; (3) tier-switching policy cost. Each is a candidate scoping spike. Overlaps with O-BP7 (known structural absences) — both surface from the same observation that the theory has gaps in its tier-switching/misspecification machinery.

- **V-strong G-BP2 — paper-writing-time decision.** Whether to ever present AAD as a control-theoretic specialization of active inference. The V-medium move keeps both options open. Per `msc/spike-active-inference-vs-aad.md` §I action 5, defer to the right rhetorical moment.


## Active — Missing Segments

### AAD Core (`01-aad-core/`)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| `adversarial-edge-targeting` | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| `intent-dag-development` | A | Aside | Convergence history of AND/OR + single-$p$ (archaeological record) |
| `worked-example-cam` | A | Worked example | Coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as $\varepsilon^\ast = 0$ composition. Planned in `#composition-closure` Discussion. |

### Section III — Composition Dynamics gaps (from Miller + Hafez integration)

- Latent structural diversity
- Endogenous coupling — $\gamma$ as function of population composition
- Composition transition dynamics (Miller 2022 extreme-transition motif)
- Computational thresholds for social behavior (Miller 2022 ICE framework)
- Agent opacity (Hafez et al. 2026 backward predictive uncertainty $H_b$)


## Active — Presentation

- **Three-way presentation split.** All reviewers recommend: (a) core results, (b) conditional architecture, (c) empirical programs. Single highest-leverage presentation change. Not yet executed.

- **AAD-vs-AI introductory positioning.** Per `msc/spike-active-inference-vs-aad.md` §I action 2: when a paper draft is being prepared, surface the §C distinctive-claims and §D refusals at the introductory level (CLAUDE.md, OUTLINE.md preambles). The 2026-04-22 segment-level integration sets the foundation; introductory-level surfacing is the paper-writing-time follow-through. Three underclaim moves named: persistence template's broader validity (Aguilera 2022 contrast); directed-separation as Pearl-blanket conservative form (Bruineberg 2022 contrast); satisfaction-gap as decision-theory content (Sun & Firestone 2020 dark-room contrast).

- **Prior-art positioning synthesis.** Active inference / FEP / POMDP / BDI relationships now in individual segments (substantially expanded 2026-04-22). A synthesis pass that surfaces the pattern across segments may still be valuable.


## Active — Editorial Hygiene

- **Spike-to-segment reverse-check.** Standing Gate 2 check per `FORMAT.md`: "What did the spike establish that the segment does not say?" — added in Session C.5 of 2026-04-21 cycle; verify it's still present and visible.

- **Segment counts in CLAUDE.md "What's Settled" summary** — refreshed 2026-04-22 (post-strengthening): now 93 AAD core segments. Refresh opportunistically.


## Active — Promotion Pipeline

**Current state (2026-04-22, post-strengthening):** 93 AAD core segments. Several segments reset to `draft` for re-review after the strengthening cycle: `#causal-insufficiency-detection` (full rewrite), `#strategy-dag` (Correlation Hierarchy substantially reworked), `#strategic-dynamics-derivation` (new Prop B.7), `#information-bottleneck` (status upgrade + VFE cross-ref), `#directed-separation` (Bruineberg integration), `#satisfaction-gap`/`#control-regret` (EFE-collapse contrast), `#strategy-complexity-cost` (V-medium variational form), `#compression-operations` (variational + hierarchical-generative-model credit), `#sector-persistence-template` (Aguilera contrast), `#loop-interventional-access` (honest-credit + identifiability-floor cross-ref).

The new `#identifiability-floor` segment is at `draft`; it would benefit from a Gate 1 dependency audit on the next promotion pass.

Recommended next promotion candidates remain the ones from the prior round: `#sector-condition-derivation`, `#recursive-update-derivation`, `#mismatch-decomposition`, `#chain-confidence-decay`, `#persistence-condition`, `#gain-sector-bridge`, `#worked-example-kalman`, `#discrete-sector-condition`, `#graph-structure-uniqueness`. (`#satisfaction-gap` and `#control-regret` were on this list pre-strengthening; they are now back at draft after the EFE-contrast addition and need re-promotion.)


## Active — Lower Priority

- **Observability-dominance product formula.** $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ posited, not derived. Label as formulation choice or derive.
- **Strategic calibration aggregation.** $L^2$ norm unjustified. Label as design choice.
- **Scope architecture.** "Within AAD's scope" ambiguous between adaptive and agency scope.
- **`loop-interventional-access` status.** "exact" defensible; opening claim could be softened. (Note: AI integration sharpened the distinctive-AAD-moves framing 2026-04-22.)
- **Between-event dynamics.** $g_M(M_\tau)$ defined but unreferenced. Important for logogenic agents.
- **Fully coupled adversarial dynamics.** Both agents' mismatch co-evolving. Open.
- **`objective-functional` labeling.** "axiomatic" for scalar-comparability is a formulation choice.
- **Heavy-tailed disturbances.** Model S assumes finite second moment.
- **`satisfaction-gap`/`control-regret` convention-dependence.** "exact" but convention-relative diagnostics. Add note to Epistemic Status. (Note: EFE-contrast was added 2026-04-22; convention-dependence note not yet.)
- **External validation design.** Testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Deferred — Project Structure

- Root-level assembly index (when content beyond AAD warrants it)
- `framework/` directory for non-mathematical content
- Multiple index support (paper, preprint, monograph)
- Section IV standalone paper outline (draft at `msc/2026-03-14-section-iv-paper-outline.md`)


## Deferred — Tooling

- `lint-md` directory arguments


## Archive — Work landed

Detailed historical items moved out of the active list. Kept here so that future agents can find what was done.

### 2026-04-22/23 strengthening cycle — COMPLETE (commits `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`)

Nine commits delivering six proposal executions, three Cauchy-functional-equation uniqueness theorems, and one citation-audit cleanup. The cycle's distinctive pattern: three independent strengthenings all forced logarithmic coordinates via Cauchy-functional-equation arguments, which on retrospect comprise a three-layer additive-decomposition pattern (documented as §SP-1 in `msc/architectural-proposals-2026-04-22.md`).

- **Phase 1 cleanups (F18-F21) + F20 regret-bound strengthening** (commit `0a772d2`). F18 (worked-example-L1 stale L1' open claim), F19 (section-ii-survival entropy→MI bias bound), F21 (identifiability-floor frontmatter). F20 strengthened as regret-bound derivation: the π*-first KL direction is forced because forward-KL is vacuous under deterministic π*. New appendix segment `#strategy-cost-regret-bound`.
- **Phase 2: O-BP14 derivation-table convention** (commit `c1d9fcf`). FORMAT.md convention + tables applied to 5 derivation segments. Surfaced A2' α/β ambiguity (→ A2' strengthening spike) and B.5d minimal-scheme claim (parked Phase 2.5).
- **Phase 3: O-BP6 identity promotion** (commit `2980327`). `#agent-identity` promoted to type:scope/status:robust-qualitative with three explicit consequences. Closes F5.
- **Reverse-KL uniqueness theorem** (commit `f70fb68`, citations corrected in `e777f01`). Under the chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975), reverse-KL is uniquely forced within the direction-forced f-divergence family. Axiom AAD-internally motivated as divergence-level analog of #chain-confidence-decay. Concrete χ² counterexample exhibited.
- **A2' strengthening** (commit `80b40d2`). Sub-scope partition α (A2' derived) vs β (A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012). Sub-scope label inherited by sector-persistence-template instances.
- **Phase 4: C-BP3 calibration laboratory** (commit `d0373fc`). TST reframed as "privileged high-identifiability calibration laboratory" with transfer-assumption table for five AAD-core quantities. Closes F15.
- **Phase 7: C-BP2 separability pattern** (commit `72ca532`). New meta-segment `#separability-pattern` (six ladders enumerated; positive-half complement to `#identifiability-floor`). Three-part meta-segment family: #independence-audit + #approximation-tiering + #separability-pattern.
- **Citation audit of reverse-KL work** (commit `e777f01`). Three wrong attributions corrected (Csiszár 1972, Amari 2009 Theorem 1, Amari-Cichocki 2010 Prop 3.2 do not contain the claimed chain-rule uniqueness theorem); Eguchi 1983 venue corrected. Audit trail preserved in-segment. Three PDFs saved to `ref/`.
- **Phase 5: G-BP1 logit scoping — partial execution** (commit `a39dfb7`). Third Cauchy-functional-equation uniqueness theorem: under the evidential-additivity axiom (Bayesian independent-evidence updates add in a fixed coordinate), log-odds is uniquely forced up to positive affine. Axiom AAD-internally motivated as update-level analog of #chain-confidence-decay. New appendix segment `#edge-update-natural-parameter`. Finding 2 (unbounded gradient mechanical break in #credit-assignment-boundary) resolved by restating default signal in log-odds (domain ℝ, no mechanical break). Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent); full restatement deferred to future G-BP3.
- **New meta-pattern discovered** (cascaded observation, commit `a39dfb7` and prior). Three independent uniqueness theorems (chain-confidence-decay, reverse-KL, log-odds) share structural shape: Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom forces logarithmic coordinates. Documented as §SP-1 in `msc/architectural-proposals-2026-04-22.md`; candidate for promotion to explicit meta-segment (`#additive-decomposition-pattern`) in a future session.

### 2026-04-22 strengthening cycle — COMPLETE (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`)

Followed Joseph's strengthen-first-before-soften posture (`feedback_strengthen_before_soften.md`): for each finding with a softening repair on file, attempted the strengthening first; only fell back to softening if strengthening failed. Outcomes:

- **F1 — strengthening succeeded.** No-go theorem: under purely on-policy execution with sequential short-circuit, no detection mechanism can distinguish an L0-insufficient world from an L0-sufficient world matched on regime conditionals. Tier: *exact* for shallow strict-prerequisite cases; *robust qualitative* for general DAG topology. Five boundary routes characterized. The covariance test under joint sibling observability is now the unique broadly-available violation of the no-go's scope — sharpening the load-bearing role of `#loop-interventional-access`. Predecessor softening repair retained as historical fallback.

- **F7 — strengthening succeeded.** Per-quantity exactness audit: ~14 AAD-relevant estimators in three blocks (TST operational, causal-discovery substrate, multi-agent observable structure) are exact functions of $\mathcal{C}_t^{\text{commit}}$. Conditional maximality: under cryptographic immutability, cryptographic authorship, standard universal retrieval, and mainline-bounded scope, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of $\mathcal{C}_t$. Estimator-of-AAD-quantity bias separated as a third Consequence clause. $\mathcal{C}_t^{\text{commit}}$ added to NOTATION.md.

- **F10 — strengthening (status upgrade).** `#information-bottleneck` reclassified from `discussion-grade` to `exact` (applied external theorem: Tishby, Pereira & Bialek 1999), with three-paragraph Epistemic Status rewrite naming the AAD binding ($X = \mathcal{C}_t$, $T = M_t$, $Y =$ future-obs) and the Markov-chain factorization holding by construction.

- **F13 — strengthening succeeded for observable-$C$; refuted for unobservable-$C$.** New Prop B.7 in `#strategic-dynamics-derivation` derives the L1' sector transfer with five-way gating $\alpha_{L1'} = \min(1/(n_C+1), \min_j \theta_C \pi_{j\mid C}/(n_{j\mid C}+1), \min_j (1-\theta_C)\pi_{j\mid \neg C}/(n_{j\mid \neg C}+1))$ under observable common cause and facilitator monotonicity. Reduces correctly to B.6 in the strict-prerequisite limit. The unobservable-$C$ single-channel case is *refuted* by the Cramér-Rao floor (Fisher information matrix is rank 1 with factorization $\mathcal{F} = uu^T/(\mu\bar\mu)$ where $u = (\Delta_j, \theta_C, 1-\theta_C)$). Repair routes: augment $C$-observability, run multi-child joint observation, or fall back to plan-level marginal tracking. `#strategy-dag` Correlation Hierarchy extended to four rows.

- **New meta-segment `#identifiability-floor`.** Names the emerging pattern of structural no-go results in AAD — limits derived from external information-theoretic theorems (Pearl/Bareinboim CHT for F1; Cramér-Rao for F13). Three adjacent open extensions surfaced: causal-IB for interventional relevance, misspecification-cost quantification, tier-switching policy cost.

- **AI integration pass (Phases A–D).** Implemented the AAD-vs-Active-Inference positioning spike's §H Overlap+Underclaim findings:
  - Phase A: G-BP2 V-medium executed — variational form replaces Shannon-MI in `#strategy-complexity-cost` (closes Gemini Finding 2/3); related cross-refs in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`.
  - Phase B: Honest credit to action-perception-loop framing (Friston 2017, Parr & Pezzulo 2022, Wiener 1948, Conant & Ashby 1970) in `#loop-interventional-access` with three distinctive AAD moves named; honest credit to hierarchical-generative-model lineage (Friston 2008/2010, Clark 2013, Hohwy 2013) in `#compression-operations` with three structural additions named.
  - Phase C: Aguilera 2022 FEP-flow narrowing contrast in `#sector-persistence-template`; Bruineberg 2022 Pearl-blanket vs Friston-blanket distinction in `#directed-separation` (AAD as conservative form); Sun & Firestone 2020 dark-room contrast in `#satisfaction-gap`/`#control-regret`.
  - Phase D: VFE accuracy-complexity equivalence in `#information-bottleneck` (Friston 2010/2017, Parr & Pezzulo 2022, Tishby & Zaslavsky 2015).

### 2026-04-22 audit-trio + Codex round-2 cycle — COMPLETE (commits before strengthening)

The morning's audit trio (Gemini, Codex round-1, Opus) and the afternoon Codex round-2 audit produced the 15-finding pending list and 14 architectural proposals (`msc/architectural-proposals-2026-04-22.md`). The strengthening cycle resolved 4 directly + 3 partially + 1 by V-medium G-BP2; remaining are listed in the Pending Findings section above.

### 2026-04-21 audit cycle — COMPLETE (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`)

Session plan derived from `msc/opus-audit-2026-04-21.md`. Summary of what landed:

- **Session A** — `#sector-persistence-template` factored out as shared lemma; six persistence-flavored segments re-expressed as template instances. Four honesty fixes.
- **Session B** — `#graph-structure-uniqueness` reframed as Cox-analog; two new meta-segments: `#independence-audit` and `#approximation-tiering`.
- **Session C** — Scope gates in `#composition-closure`, `#unity-dimensions` lead rewritten, `#software-epistemic-properties` P1 codebase-vs-environment scoping, `section-ii-survival` statement-level-vs-operational distinction, FORMAT.md promotion-workflow reverse-check.
- **Session D** — Scoping spike `msc/spike-ib-unification-plan.md` delivered; execution absorbed into `#compression-operations` segment with three integration edits.
- **Late-cycle Gemini batch** — L1 soft-facilitator gap handled; Finding A and Finding B (composition-closure temporal coarse-graining; observation-ambiguity-modulation architecture-contamination) both closed 2026-04-22.

### 2026-04-02 Codex round-2 findings — COMPLETE

All numbered items from the round-2 review resolved in segments. Full history in `msc/analysis-2026-04-02-round2.md`.

### 2026-03-13 consolidated review — mostly COMPLETE

Top issues (1) directed-separation architectural classification, (2) $\alpha$-vs-$\mathcal{T}$ distinction, (3) composition-closure bridge lemma, (4) graph uniqueness at theorem strength, (6) assorted formal issues — all landed. Remaining: (5) `#causal-discovery-from-git` now written; TST overstatement of causal status of git data is covered within that segment.
