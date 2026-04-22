# TODO — Open Work Items

**Last reconciled:** 2026-04-22 (post-strengthening + post-evening-audits). This file is the living action list. For the 2026-04-21 master audit and the 2026-04-22 morning four-audit batch, see the historical pointers in the Archive section. The 2026-04-22 strengthening cycle (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`) executed strengthen-first repairs for Findings 1, 7, 10, 13 and the AI integration pass. A second triple-audit cycle (Codex / Gemini / Opus) ran *after* the strengthening cycle and surfaced six new findings (F16–F21) plus nine new architectural proposals (O-BP8 through O-BP16); see `msc/pending-findings-2026-04-22.md` "Post-strengthening evening batch" and `msc/architectural-proposals-2026-04-22.md` "Post-strengthening evening additions."

## Highest-priority cleanups — LANDED (Phase 1 of strengthen-first cycle)

All four cleanups landed. F20 strengthened rather than softened; the others were mechanical cross-segment updates. Detail in Archive section below.

- ~~**F18** — `#worked-example-L1` said L1' transfer was "open"~~ — **LANDED.** Updated to cite Prop B.7 (observable-$C$ with five-way gating under facilitator monotonicity) and the Cramér-Rao refutation for unobservable-$C$ single-channel; three repair routes named.
- ~~**F19** — `#section-ii-survival` bias bound in entropy form~~ — **LANDED.** Replaced with MI form from `#observation-ambiguity-modulation`; triple-zero boundary structure made explicit (bias vanishes at $\kappa=0$ OR $\mathcal{A}=0$ OR factually-sharp observation, not just the first).
- ~~**F20** — KL-direction degeneracy in `#strategy-complexity-cost` variational form~~ — **LANDED as strengthening** (not softening). New appendix segment **#strategy-cost-regret-bound** hosts the full derivation: TV bound via bounded value range, Pinsker-KL bound, direction-forcing argument (forward-KL is vacuous under deterministic $\pi^\ast$), admissible-divergence family analysis (TV tight but non-differentiable; reverse-KL canonical-not-unique on gradient-tractability + variational-inference + Fisher-geometry + MDL-coding grounds), and the linear-vs-square-root $\beta_\Sigma$ trade-off (linear preserves IB-shape alignment; square-root would give $\beta_\Sigma \propto V_{\max}$ global naturalization). Segment-level cross-refs updated in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`. `msc/spike-f20-kl-direction-strengthening.md` retained as the reasoning trail only; framework is complete without it.
- ~~**F21** — `#identifiability-floor` frontmatter status conflicts with internal text~~ — **LANDED.** Frontmatter `status:` changed to `discussion-grade`; Epistemic Status rewritten to cleanly separate the meta-pattern (discussion-grade presentational principle) from individual instances (F1's no-go: *exact* for shallow / *robust qualitative* for general; F13's L1' refutation: *exact*).

## Recommendations for next session (from 2026-04-22 close-out review)

What follows is one agent's prioritization, not a binding commitment. Joseph's call which to follow.

### Recommended sequence

**Phase 1 — Cleanups (1–2 hrs total).** Land F18, F19, F20, F21 as a small cleanup commit. These are all known issues from prior work, they don't entangle with any architectural decision, and F20 in particular is a substantive bug in load-bearing recently-landed work. Recommended order within the phase: F21 first (5 min, builds confidence), F18 second (10 min, mechanical), F19 third (20 min, mechanical), F20 last (30–45 min, requires the small theoretical decision on KL direction).

For F20 specifically: prefer Option (a) (reverse KL direction to $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast \mid M_t)$) over Option (b) (Boltzmann-smoothing of $\pi^\ast$). Reason: Option (a) preserves the V-medium move's original spirit (the strategy's distance from the optimum, measured via KL) while fixing the deterministic-$\pi^\ast$ degeneracy with a cleaner mathematical object (negative log-likelihood of the optimal action under the agent's strategy). Option (b) requires introducing a temperature parameter that has no AAD-internal justification. The fix needs to land in `#strategy-complexity-cost`, the companion spike `msc/spike-active-inference-vs-aad.md` §E.6, the `#compression-operations` variational note, and a one-line acknowledgment in `#exploit-explore-deliberate` and `#ciy-unified-objective`. Worth a small `msc/spike-finding-20-kl-direction.md` to document the choice and the reasoning, parallel to how F1 / F7 / F13 strengthening work was documented.

**Phase 2 — Derivation-table convention (O-BP14, 30 min + incremental).** Add the convention to FORMAT.md, then apply to 3–5 high-value derivation-type segments first (`#sector-condition-derivation`, `#strategic-dynamics-derivation` Props B.5–B.7, `#composition-closure`, `#graph-structure-uniqueness`). The remaining segments can be touched as they're next visited. Rationale: this is the highest payoff-to-effort move in the entire portfolio. The derivation-table format itself surfaces what's chosen vs. derived in each segment — which is exactly the kind of clarity that later architectural proposals (O-BP1, O-BP10, C-BP2) need to land cleanly. The tables become scoping artifacts for those moves, not just reader-friendly scaffolding.

**Phase 3 — Coordinated framing pass: O-BP1 + O-BP10 + O-BP8 (1–3 sessions).** Three composable framing moves, all editorial rather than structural:

- **O-BP10** (projection-contraction framing): "an adaptive system is a projection whose contraction rate exceeds its target's drift rate." Goes in OUTLINE.md preamble + `#sector-persistence-template` introductory passage.
- **O-BP1** (template as organizing principle): reframe the OUTLINE around disturbance decomposition at scales. Composes with O-BP10 — O-BP10 is the object-level slogan, O-BP1 is the result-level organizing principle.
- **O-BP8** (explicit scope lattice): name the adaptive → agency → learning-purposeful → exact-Section-II-modular → coupled/logogenic lattice once. Closes Finding 16 and supports both O-BP1 and the eventual C-BP1 three-layer separation.

These three together would constitute a complete elevator-pitch reframing of AAD. They close several of the §H underclaim findings from the morning's AI-positioning spike (especially the persistence-template's broader-validity-than-FEP-flow positioning, which gets sharper under O-BP10's "what AAD actually is" framing). Risk: low — all three are presentational, not structural.

**Phase 4 — Then choose:** Either (a) continue editorial/positioning work with O-BP6 (identity promotion, 1 session), C-BP3 (software calibration laboratory, 45–90 min), C-BP2 (master separability pattern naming, 1–2 sessions); or (b) launch the O-BP11 (observability as master variable) scoping spike as the next substantive structural investigation. Recommendation: do (a) first if the goal is consolidation; do (b) first if the goal is to scope the largest available reorganization while the strengthening cycle's intuitions are fresh.

### What to defer

- **G-BP1, G-BP3, O-BP3** (natural parameters + Fisher geometry + continuous tiering) — large coordinated cluster; defer until project capacity allows multi-session investment. Gemini's Riemannian-manifold reaffirmation strengthened the case but did not change the scoping cost.
- **G-BP2 V-strong** (full reformulation as variational free energy) — paper-writing-time decision per `msc/spike-active-inference-vs-aad.md` §I action 5. Not theoretical-development work.
- **O-BP4, O-BP5, O-BP15, O-BP16** — substantial structural work each. Worth scoping spikes individually when their specific motivation becomes more pressing than the smaller framing moves.
- **O-BP12 (resource budget $B_t$)** — interesting and adjacent to O-BP7, but the framework currently handles bounded rationality piecewise without obvious dysfunction. Defer until the piecewise treatment shows specific friction.
- **O-BP13 (Cox-necessity)** — would elevate `#graph-structure-uniqueness` from sufficiency-only to full Cox-style. Worth a 1–2 session spike but not high-priority unless reviewers raise the necessity question.

### Strategic observation

The pattern emerging from the 2026-04-21 → 2026-04-22 cycle is that AAD benefits more from **concise framing moves** than from major theoretical reorganization. The sector-Lyapunov template factoring, the strengthening cycle, the AI integration positioning, the identifiability-floor meta-segment — all are framing / integration moves with isolated genuinely-new content (F1's no-go theorem, F13's Prop B.7). The Phase 2 + 3 recommendations above continue this pattern. Major structural reorganization (O-BP11, O-BP4, G-BP3) should probably wait until the framing layer has stabilized and the genuine remaining structural friction is more visible.

This is consistent with CLAUDE.md's "convergent depth over generative breadth" principle (3:1 ratio of promoting to creating). The 2026-04-22 cycles were 3:1 in the right direction (one new derivation in F1, one in F13, one new meta-segment, plus extensive framing/integration work). The same ratio should hold in the next cycle: derivation-table convention + O-BP1/10/8 framing pass + cleanups, with at most one substantive spike (probably O-BP11 scoping) thrown in.


## Active — Citations Audit (project-wide)

Surfaced during the reverse-KL uniqueness spike: a specific citation (Amari 2009 for chain-rule uniqueness) was found to be incorrect — the paper proves f∩Bregman intersection uniqueness, not chain-rule uniqueness. The immediate fix is in flight as a background audit agent scoped to the reverse-KL work (`#strategy-cost-regret-bound`, `msc/spike-reverse-kl-uniqueness.md`, and downstream refs).

The broader concern: *every* external-theorem citation across AAD and TST segments should be verified against the actual paper content. Prior strengthening cycles invoked external theorems (Bareinboim et al. 2022 Causal Hierarchy Theorem; Cramér-Rao; Pearl's do-calculus; Tishby-Pereira-Bialek 1999 IB; Khalil Lyapunov results; Friston et al. and Da Costa et al. active-inference references; Aguilera 2022; Bruineberg et al. 2022; etc.) that should have the same level of scrutiny applied.

**Scope.** Every `*[Derived]*`, `*[Proved]*`, and `*[Derived (External theorem)]*` claim that invokes a specific paper. Include both AAD core segments and TST segments. Aim for two per-citation deliverables: (a) outcome of (A correct / B wrong paper / C unverified / D ghost); (b) PDF saved to `ref/` when open-access.

**Pattern to cascade.** The reverse-KL audit is the template for this work — self-contained audit of a single work's citations. For a project-wide audit, pursue in batches by segment cluster (e.g., first Section II derivations, then Section III composition results, then TST operational segments).

**Parking until the reverse-KL audit completes** — that audit's findings will refine the per-citation procedure and surface which other segments need similar scrutiny.


## Active — Strategic Architectural Proposals

Architectural moves remaining from the 2026-04-22 portfolio (`msc/architectural-proposals-2026-04-22.md`). G-BP2 was partially executed in V-medium form during the 2026-04-22 strengthening cycle (variational form of strategy IB; see #strategy-complexity-cost and #compression-operations). The remaining proposals are evaluated on their own merits — beauty, concision, correctness, approachability, fundamentality.

### Smaller / approachable

- **O-BP1 — Sector-persistence template as organizing principle.** Reframe OUTLINE preamble around "AAD decomposes disturbance for bounded-correction dynamics at each scale." Subsumes Finding 9 (Section II preamble). 1–2 sessions, framing touch, low risk. Strengthened by the 2026-04-22 cycle's promotion of the template's load-bearing role across the persistence-flavored results. **Natural next move.**
- **O-BP6 — Identity promotion (`#agent-identity` to formal scope).** AAD applies to agents on singular causal trajectories; grounds why loop Level-2 access is interventional. Partial on Finding 5. One session, localized; no scoping spike needed.
- **C-BP3 — Software as calibration laboratory.** Reframe TST as "privileged high-identifiability calibration domain," other domains as exports under additional assumptions. Subsumes Finding 15; strengthens Findings 7 and 14. The 2026-04-22 F7 strengthening (per-quantity exactness audit + conditional maximality) supplies most of the substance; C-BP3 is the framing layer over it. 45–90 min editorial reframing.
- **C-BP2 — Master separability pattern as explicit organizing principle.** Name the meta-pattern that AAD already runs across L0/L1/L1'/L2, Class 1/2/3, Tier 1/2/3, C1/C2/C3. The 2026-04-22 cycle's #identifiability-floor segment captures one half of this (the no-go side); C-BP2 would name the positive side (separable-core / structured-repair / general-open). Composes with O-BP1. 1–2 sessions.

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
| 5 | Loop framing overstates Level 2 access | **PARTIALLY RESOLVED** by 2026-04-22 AI integration: #loop-interventional-access now distinguishes "data generated under intervention" from "cleanly identified do-estimates" via the three distinctive AAD moves and Bruineberg-blanket positioning. Full closure requires O-BP6 identity promotion |
| 6 | Composition timescale heuristic outruns bridge conditions | Open. 30–45 min scope-narrowing in #composition-consistency |
| 7 | TST overstates git as complete chronica | **RESOLVED** by strengthening (commit b6134c2): per-quantity exactness audit + conditional maximality + $\mathcal{C}_t^{\text{commit}}$ in #software-epistemic-properties |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision |
| 9 | Section II preamble framing understates survival | Open; absorbed if O-BP1 framing pass executed. 30 min standalone |
| 10 | `#information-bottleneck` status mismatches unification role | **RESOLVED** (commit a14682e): status reclassified from discussion-grade to exact (applied external theorem) |
| 11 | Orient cascade step 4c convergence in non-stationary envs | **PARTIALLY RESOLVED** by F1 strengthening: #causal-insufficiency-detection no-go reframes step 4c as the unique broadly-available diagnostic. Step-4c sanity edit in #orient-cascade itself remains optional cleanup |
| 12 | Section II survival slides from statement-level to operational | Open. Subsumed by C-BP1 (three-layer epistemic separation) |
| 13 | `#strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite | **RESOLVED** by strengthening (commit 4d050c8): Prop B.7 derives L1' transfer for observable $C$ with five-way gating; refutes unobservable-$C$ via Cramér-Rao floor; #strategy-dag headline + Correlation Hierarchy table updated |
| 14 | `#developer-as-act-agent` exact-status mismatch (human vs AI regimes) | Open. Option A (15–30 min status downgrade) is straightforward regardless of C-BP4 |
| 15 | Software "richest operationalization domain" headline overclaims | Open; subsumed by C-BP3 reframing |

### Actionable now (independent of remaining portfolio decisions)

- **Finding 4 + 9 coordinated pass** — Section II preamble + scope-narrowing. 60–90 min combined; or absorbed by O-BP1.
- **Finding 6** — composition-consistency scope-narrowing. 30–45 min.
- **Finding 8** — (C-iii) Option A vs Option B decision needed before edit.
- **Finding 14 Option A** — `#developer-as-act-agent` status downgrade. 15–30 min.

### 2026-04-22 evening batch — six new findings

Three independent de novo audits (Codex, Gemini, Opus) ran *after* the strengthening cycle. Three categories of finding emerged: integration gaps from prior cycles, new scope/operational-extractability frictions, and bugs introduced by the strengthening cycle itself.

| # | Finding | Source | Severity | Subsumed by |
|---|---------|--------|----------|-------------|
| 16 | Section II scope lattice underspecified across segments | Codex F1 (evening) | Medium | O-BP8 (scope-lattice naming); partial O-BP1 |
| 17 | `#coupled-diagnostic-framework` operational-computability overclaim | Codex F4 (evening) | Medium-high | C-BP1; partial O-BP9 |
| 18 | `#worked-example-L1` says L1' transfer "open" — STALE after F13 strengthening | Gemini F1 (evening) | Medium | — (cross-segment update) |
| 19 | `#section-ii-survival` bias bound in entropy form, stale after 2026-04-21 Finding B | Gemini F3 (evening) | Medium | — (cross-segment update) |
| 20 | KL-direction degeneracy in `#strategy-complexity-cost` variational form (introduced by V-medium) | Opus F1 (evening) | High | — (theoretical-correction repair) |
| 21 | `#identifiability-floor` frontmatter status conflicts with internal text | Opus F3 (evening) | Low | — (drafting cleanup) |

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
