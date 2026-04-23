# LOG.md — Cycle History

This file records cycle-by-cycle narrative for completed audit/strengthening/brainstorm cycles. **It is archaeology, not load-bearing for current work.** Fresh agents should read `CLAUDE.md` (architectural state) and `TODO.md` (active work) first; come here only when the *origin* of a current commitment matters — for instance, when judging whether a "settled" item rests on derivation or on a cycle's working consensus, or when an audit finding's prior status helps decide a current routing call.

`TODO.md §Archive` records work landed at the commit/finding granularity; this file records the *theoretical* contributions and structural moves that shaped the framework's current shape. The two are complementary: TODO.md says *what shipped*, LOG.md says *what changed about how the theory thinks*.

Entries are ordered most-recent-first.

---

## 2026-04-23 — Gemini Gap A/B Cycle

Twelve parallel research spikes against two gaps surfaced in Gemini's audit: (A) default signal function validation under correlated failures (L1'/L2); (B) contraction assumptions verified only for linear Kalman-type, needing extension to broader agent classes. A follow-up spike (Jacobian-level B1 strengthening) tested whether B1's metric-α₂ derivations could be made AAD-internal rather than theorem-imported; its mixed-lift three-layer result became load-bearing for the landing epistemic labeling. An H_b agent-opacity spike (from Hafez 2026) closed the long-flagged `#adversarial-edge-targeting` Section III gap.

**Six new segments landed:**
- `#contraction-template` — Lohmiller-Slotine metric generalization of `#sector-persistence-template` with 5 α promotions, topology-indexed closures, heterogeneous (CM2-M)
- `#strategic-composition` — equilibrium-convergence framing for partially-opposing $O_t^{(i)}$ under Monderer-Shapley / Rosen
- `#fisher-whitened-update-rule`
- `#l1-update-bias`
- `#variational-sector-condition`
- `#agent-opacity` — $H_b^{A\mid B}$ with sign-flip derived via signed coupling, emitter-side four-regime classification, 16-cell composition closing adversarial-edge-targeting

**Four structural additions to existing meta-architecture:**
- Instance 3 in `#identifiability-floor` (composition-layer no-go via Liberzon 2003 common-Lyapunov nonexistence)
- Fourth primary instance in `#additive-coordinate-forcing` (Čencov-invariance at metric layer under the new (PI) axiom in `#agent-identity`; 1-anchor-plus-2-theorem → 1-anchor-plus-3-theorem)
- Seventh ladder in `#separability-pattern` (A2'-scope metric-α₁/α₂/β)
- (C-iv) scope route in `#composition-scope-condition`

**Two new commitments:**
- **(PI) parameterization-invariance axiom** adopted as natural extension of `#agent-identity`'s singular-trajectory commitment: AAD's predictions should not depend on arbitrary choice of coordinates on $M_t$.
- **Monotone-operator-theory lineage** (Rockafellar 1970 / Bauschke-Combettes 2017) explicitly acknowledged in `#sector-persistence-template` and `#sector-condition-derivation` — AAD is a specialization (one-point anchoring; Model D/S decomposition; identifiability-floor composition; composition-consistency; α/β epistemic labeling are AAD-distinctive).

Segment count: 103 → 109. Thirteen spike files retained in `msc/` as reasoning trails.

**Cross-segment reverse-check** (Gate-3-sidebar per `FORMAT.md`) on the six newly-promoted segments is flagged in TODO as future-session work — the spike-to-segment compression should be verified against the original spike content to confirm no over-aggressive compression. Each spike is preserved in `msc/spike-*.md` per `feedback_math_lives_in_segments`.

---

## 2026-04-23 — Brainstorm Cycle

Seven commits: `0d7b987`, `591e8b6`, `13fe242`, `b48cdee`, `77a9bde`, `0bd859e`, `a739e9a`. Seven parallel research spikes prompted by an external-framework comparison (GAA Baigozin 2025) as a brainstorming exercise. Six of the seven promoted to new segments; one (internal-external decomposition) was deferred after the $\rho$-factorization spike returned an honest obstruction. Segment count: 96 → 103.

**Substantive theoretical contributions:**

1. **`#critical-mass-composition`** — closed-form composite sector constant $(\alpha-C)R \gt \rho + \gamma\mathcal T$ for the symmetric-matched-Tier-1 dyad via joint quadratic Lyapunov. Sign-sensitive refinement of the weakest-link bound; recovers `#team-persistence` (cooperative $\gamma \lt 0$) and `#adversarial-destabilization` (adversarial $\gamma \gt 0$) as signed special cases; formalizes `#symbiogenic-composition` (S-3) autonomy-reduction as asymmetric-parameter weighted-Lyapunov limit. Closes long-standing Section III bridge-lemma opening.

2. **`#interaction-channel-classification`** — four-regime recipient-side theory (Informative / magnitude-shock / structural-shock / ambient-noise) with boundaries in existing AAD quantities. Regime-typed $\rho_B^{\text{eff}}$ decomposition with negative Regime-I term generalizes cooperative-action coupling. Pairs with the `#adversarial-edge-targeting` Section III GAP as recipient-classifier + emitter-optimizer. Surfaces the Regime-I-with-adversarial-content informational attack that the emitter-side scalar cannot express.

3. **`#consolidation-dynamics`** — offline regime of `#recursive-update`'s between-event dynamics with IB-gap-reduction objective. Names the **stability-plasticity feasibility window** that closes an asymmetry in `#strategy-persistence-schema` (plasticity lower bound only, no stability upper bound). Required as architectural primitive in `03-logogenic-agents/` under context-turnover.

4. **`#persistence-cost`** — sustained information rate $\dot R \geq n\alpha/2$ nats/time under Model S + Gaussian-OU (Shannon RDF + Prop A.1S; Kalman-Bucy saturates per Mitter-Newton 2005). Channel-capacity prerequisite $C \geq \mathcal T/2$ opens as first-class persistence diagnostic.

5. **`#adaptive-gain-dynamics`** — A2' sub-scope partition refined from $\alpha$/$\beta$ to $\alpha_1$/$\alpha_2$/$\beta$ via augmented-state Lyapunov composition under meta-gain conditions (MG-1)–(MG-4). Adaptive Kalman, AMSGrad, IMM, MAML classified.

6. **`#detection-latency`** — within-class regime-change detection latency $\Omega((n_{\min}+1)/\varepsilon)$ **structurally forced** by composition of `#edge-update-natural-parameter`'s Aczél-Cauchy-FE log-odds with Beta-Bernoulli $\eta_{\text{edge}} = 1/(n+1)$. Sharpens the forgetting prerequisite to "also required for bounded detection latency."

7. **Spike H ($\rho$-factorization, in flight)** returned honest outcome (C) obstruction: multiplicative $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable; native structure is variance-additive $\rho^2 = \rho_{\text{irr}}^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$. Internal-external decomposition (Spike E) deferred pending variance-additive reframe.

---

## 2026-04-22/23 — Cascading Strengthening Cycle

Nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`. Executed Phases 1–5 and 7 of the post-evening-audit proposed sequence plus two in-flight strengthening spikes.

**Substantive theoretical contributions:**

1. **Three Cauchy-functional-equation uniqueness theorems**, each forcing a logarithmic coordinate via an AAD-internally-motivated additivity axiom: (a) F20 regret-bound derivation → reverse-KL direction forced under deterministic $\pi^\ast$; (b) reverse-KL chain-rule uniqueness under chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975); (c) log-odds evidential-additivity uniqueness (Aczél 1966 Cauchy-functional-equation argument). Landed in new appendix segments `#strategy-cost-regret-bound` and `#edge-update-natural-parameter`.

2. **Discovered structural pattern** (§SP-1 in `msc/architectural-proposals-2026-04-22.md`): the three theorems share a common shape — products of independent factors become additive sums on log-scale coordinates, with each coordinate uniquely forced by an AAD-internally-motivated additivity axiom. Promoted 2026-04-23 to `#additive-coordinate-forcing` meta-segment with the honest **1-anchor-plus-2-theorem** characterization (chain layer = mathematical identity; divergence + update = theorems; Lyapunov + IB Lagrangian documented as adjacent family members). Composes with `#identifiability-floor` + `#separability-pattern` as AAD's three-part meta-architecture.

3. **A2' scope partition**: α sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex — A2' derived under #gain-sector-bridge directional fidelity) vs β sub-scope (PID/rule-based/human-judgment — A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).

4. **New meta-segment `#separability-pattern`**: positive-half complement to `#identifiability-floor`, six ladders enumerated (L0/L1/L1'/L2, C1/C2/C3, Class 1/3/2, Tier 1/2/3, Regime A/B/C, Adaptive/Agency/Composite) under separable-core / structured-repair / general-open shape.

5. **Citation audit** (completed 2026-04-23 in commits `7456ec3`, `6567914`, `f61e62f`): three wrong attributions in the reverse-KL work were corrected (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 → Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975). Project-wide audit subsequently ran across all AAD and TST segments — **zero confirmed attribution errors found elsewhere**; reverse-KL's 20-25% rate was a local concentration, not representative. PDF-level verification confirmed Bruineberg 2022's "Pearl-blanket vs Friston-blanket" is verbatim terminology (not AAD paraphrase), Bareinboim CHT = Theorem 1 p.22 of 2022 ACM Books chapter, Aguilera 2022's FEP-narrow-validity claim exactly matches AAD's usage. 5 missing-citation gaps hardened (Tikhonov, Chechik full, Doob-Dynkin, Cox, Cramér). 26 PDFs acquired and canonically named in `ref/`, then **excluded from git** (redistribution rights); `ref/INDEX.md` is the tracked bibliography.

6. **Additional framing moves**: `#agent-identity` promoted to formal scope statement (Section II scope commitment grounds `#loop-interventional-access`); TST reframed as "privileged high-identifiability calibration laboratory" (not "richest operationalization domain"); O-BP14 derivation-table convention landed with applications to five derivation segments.

---

## 2026-04-22 — Strengthening Cycle (Findings 1, 7, 10, 13 + AI integration)

Five commits: `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`. Executed strengthen-first repairs for Findings 1, 7, 10, 13 from the audit-trio batch plus the AI integration pass.

**Landmark contributions:**
- A no-go theorem for on-policy L0-insufficiency detection (Pearl/Bareinboim CHT applied) — `#causal-insufficiency-detection`.
- A derived L1' sector transfer for soft-facilitators under observable common cause (Prop B.7 with facilitator monotonicity) plus Cramér-Rao refutation for the unobservable case — `#strategic-dynamics-derivation`.
- Per-quantity exactness audit for git-derived TST estimators with conditional maximality — `#software-epistemic-properties` + $\mathcal{C}_t^{\text{commit}}$ in NOTATION.md.
- The `#identifiability-floor` meta-segment naming the structural-no-go pattern.

---

## 2026-04-22 — Audit-Trio + Codex Round-2

Morning audit trio (Gemini, Codex round-1, Opus) and afternoon Codex round-2 audit produced the 15-finding pending list and 14 architectural proposals (`msc/architectural-proposals-2026-04-22.md`). The strengthening cycle that followed resolved 4 findings directly, 3 partially, and 1 by V-medium G-BP2.

This was the cycle that established the three-document pattern (findings doc + proposals doc + TODO navigator) per `feedback_architectural_proposals_vs_findings`.

---

## Earlier History (pointer-only)

- **2026-04-21 audit cycle** (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`) — IB unification + sector-Lyapunov template factoring landed; six AAD persistence-flavored results re-expressed as instances of `#sector-persistence-template`. See `TODO.md §Archive` for commit-level detail.

- **2026-04-20** — SOC/renormalization speculation (parked in `msc/speculation-soc-composition.md`); Section III unity-closure investigation (`msc/spike-unity-closure-mapping.md`, `msc/spike-mori-zwanzig-composition.md`) finding two-axis closure structure exposing gap in `#unity-dimensions`.

- **2026-04-16** — ACT → AAD rename to resolve collision with "AI Consciousness Test" (Schneider & Turner). See `msc/name-transition-aad.md`.

- **2026-04-02** — edge semantics resolved as regime-indexed interpretation (causal efficacy estimate with A/B/C regime classification); `_obs/old-tf-*` files preserved.

- **2026-03-14** — α/T relationship resolved (α proportional to T verified across all correction function classes).

- **2026-03-13** — Three-model consolidated review (Claude Opus, OpenAI Codex, Google Gemini) framed the theory's structural priorities. See `msc/2026-03-13-feedback.md`. Of those: directed-separation scope decision (resolved as architectural classification), α/T relationship (resolved 2026-03-14), composition-closure bridge lemma (tier-specific contraction structure promoted; remaining moves landed in 2026-04-21 cycle).

- **2026-03-11** — TST conversion. The original monolithic TFT documents split into segment files; `02-tst-core/` reorganized with slug filenames and an explicit OUTLINE.md.

- **March 2026** — Spike-driven foundation: `msc/spike-purposeful-agent-derivation.md`, `msc/spike-v3-purposeful-agent.md` (definitive), `msc/spike-graph-uniqueness.md` (DAG with Markov property forced from four operational postulates; acyclicity derived from temporal ordering), `msc/spike-agent-composition.md` (Section III "Composition Dynamics" framed). Codex three-round review established the X_t lift, Level 2 scoping, satisfaction gap / control regret split, directed separation scope condition.

- **March 2026 — terminology rename**: axiom→postulate, theorem→result, proof→derivation; `first-principled` status label → `axiomatic`. See `feedback_terminology_rename.md` in agent memory; the rationale ("avoid physics-envy framing") and the migration applied across all then-existing segments.

- **February 2026** — `msc/agentic-tft-*.md` bridge work absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, review response. Source material for `03-logogenic-agents/` and `04-logozoetic-agents/`.
