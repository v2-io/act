# Unnamed-Concept Consolidation Map

Proposed merges of unnamed-concept votes across the naming-cycle vote files (`msc/naming/naming-votes/*.md`). Status: **PROPOSAL** — awaiting human review before any source-file edits for this consolidation step are applied.

The aggregator at `bin/naming-aggregate.rb` collapses cosmetic variation (case, punctuation, slug-prefix) but cannot recognize that two natural-language descriptions of the same unnamed concept are the same concept. This map identifies those clusters by manual reading.

**Total unnamed-concept rows scanned:** 298 (across 16 vote files)
**Proposed clusters:** 39 (high-confidence: 17, medium: 14, low: 8)
**Unclustered singletons (listed at end):** ~120

The agent ID format below uses the file basename (e.g., `opus-4-7-r2`, `gemini-3-1-pro-preview-r2`). Weight is the agent's vote weight; a `[+3]` is a strong preference, `[+1]` weak, `[-1]` rejection.

---

## Cluster 1 — The persistence region in parameter space (where the agent maintains bounded mismatch)

**Confidence:** high

**Constituent rows:**
- `[unnamed: the sector-persistence region in parameter space]` — agent: agent1-original-brainstorm, weight: +1, proposed name: `persistence envelope`
- `[unnamed: the region where the persistence condition holds]` — agent: gemini-1, weight: +3, proposed name: `Persistence envelope`
- `[unnamed: the sector-persistence region in parameter space]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"persistence envelope"`
- `[unnamed: the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely]` — agent: haiku-4-5-r2, weight: +2, proposed name: `"persistence envelope"`
- `[unnamed: the sector-persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch]` — agent: opus-1m, weight: +3, proposed name: `persistence envelope`
- `[unnamed: the region in parameter space where sector-persistence holds]` — agent: opus-4-7-b, weight: +3, proposed name: `persistence envelope`
- `[unnamed: the persistence envelope]` — agent: opus-4-7-b, weight: -1, proposed name: `adaptive basin` (alternative-rejected)
- `[unnamed: the persistence region in $(\alpha, \rho, R)$ parameter space]` — agent: opus-4-7-r2, weight: +3, proposed name: `"persistence envelope"`
- `[unnamed: bounded mismatch region]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `persistence envelope`
- `[unnamed: the region in parameter space where parametric updates remain effective before structural change is forced]` — agent: haiku-4-5-r2, weight: +1, proposed name: `"parametric regime" or "stability envelope"`

**Proposed canonical name:** `persistence envelope`

**Why a cluster:** Eight of nine agents proposing this concept independently arrived at "persistence envelope" — strongest convergence in the entire corpus. The set $\{(\alpha, \rho, R) : \alpha \gt \rho/R\}$ is the precise referent. This is the highest-value, highest-confidence single consolidation in the corpus.

---

## Cluster 2 — Contraction-over-drift / projection-contraction slogan

**Confidence:** high

**Constituent rows:**
- `[unnamed: organizing-principle slogan "an adaptive system is a projection whose contraction rate exceeds its target's drift rate"]` — agent: codex-1, weight: +3, proposed name: `contraction-over-drift principle`
- `[unnamed: projection contraction must beat target drift]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `contraction-over-drift principle`
- `[unnamed: agent as a projection whose contraction rate must exceed its target's drift]` — agent: gemini-1, weight: +1, proposed name: `Contraction imperative`
- `[unnamed: Joseph's mental model "projection whose contraction rate must exceed its target's drift rate"]` — agent: opus-4-7-b, weight: +1, proposed name: `the projection slogan / contraction-over-drift slogan`
- `[unnamed: the projection whose contraction rate must exceed target drift — the Opus organizing-principle slogan]` — agent: sonnet-4-6, weight: +3, proposed name: `contraction-over-drift principle`
- `[unnamed: the contraction-over-drift insight]` — agent: sonnet-4-6, weight: +1, proposed name: `drift-contraction inequality`
- `[unnamed: the organizing-principle slogan — "An adaptive system is a projection whose contraction rate exceeds its target's drift rate"]` — agent: opus-4-7, weight: +1, proposed name: `projection-contraction slogan`

**Proposed canonical name:** `contraction-over-drift principle`

**Why a cluster:** Four agents converged on this exact name; one alternative ("contraction imperative") names the same Opus-attributed slogan. Strong cluster.

---

## Cluster 3 — Strengthen-first posture / attempt the improbable

**Confidence:** high

**Constituent rows:**
- `[unnamed: strengthen-first posture]` — agent: gemini-2, weight: +3, proposed name: `strengthen-first posture`
- `[unnamed: the "strengthen before soften" work posture]` — agent: opus-4-7, weight: +3, proposed name: `strengthen-first posture`
- `[unnamed: the "strengthen-before-soften" posture applied to apparent overclaims]` — agent: sonnet-4-6, weight: +1, proposed name: `epistemic strengthening posture`
- `[unnamed: the "strengthen-first, attempt the improbable" meta-approach to theory development]` — agent: sonnet-4-6, weight: +3, proposed name: `attempt the improbable`

**Proposed canonical name:** `strengthen-first posture` (with `attempt the improbable` as the spirit-form alias)

**Why a cluster:** All four reference CLAUDE.md's working-conventions section. Sonnet's "attempt the improbable" is a register-shift, not a different concept.

---

## Cluster 4 — The five-phase cycle as a single named whole

**Confidence:** high

**Constituent rows:**
- `[unnamed: cycle-phase sequence as whole]` — agent: agent1-original-brainstorm, weight: +1, proposed name: `the pentad / five-phase cycle`
- `[unnamed: cycle-phase sequence as a whole]` — agent: gemini-1, weight: +1, proposed name: `The adaptive pentad`
- `[unnamed: cycle-phase sequence as a whole]` — agent: opus-1m, weight: +1, proposed name: `the pentad`
- `[unnamed: The cycle-as-a-whole]` — agent: gemini-2, weight: +1, proposed name: `adaptive traversal`
- `[unnamed: the cycle-as-a-whole]` — agent: opus-4-7-b, weight: +1, proposed name: `the adaptive pentad`
- `[unnamed: the cycle-as-a-whole]` — agent: opus-4-7-b, weight: -1, proposed name: `the five-turn` (alternative-rejected)

**Proposed canonical name:** `the adaptive pentad` (or `the pentad`)

**Why a cluster:** All six refer to Prolepsis-Aisthesis-Aporia-Epistrophe-Praxis as a unit. "Pentad" and "adaptive pentad" dominate.

---

## Cluster 5 — Calibration laboratory framing

**Confidence:** high

**Constituent rows:**
- `[unnamed: calibration-laboratory framing as reusable meta-move]` — agent: agent1-original-brainstorm, weight: +1, proposed name: `calibration domain / calibration lab`
- `[unnamed: software as AAD's privileged high-identifiability calibration laboratory]` — agent: codex-2, weight: +3, proposed name: `calibration laboratory`
- `[unnamed: "calibration laboratory" framing for software/TST]` — agent: opus-4-7, weight: +3, proposed name: `calibration laboratory`
- `[unnamed: software's role as calibration laboratory, named-in-prose-but-not-in-slug]` — agent: opus-4-7-r2, weight: +2, proposed name: `"software-as-calibration-laboratory"`
- `[unnamed: the calibration-laboratory concept applied outside TST]` — agent: opus-4-7-b, weight: +1, proposed name: `calibration domain`
- `[unnamed: the move where AAD treats software not as instantiation but as TST's epistemically privileged measurement substrate]` — agent: opus-4-7-r2, weight: +2, proposed name: `"calibration-laboratory move"`

**Proposed canonical name:** `calibration laboratory`

**Why a cluster:** Already canonical in CLAUDE.md/TST OUTLINE per several agents' notes; this round is essentially a canonicalize-not-rename signal. `calibration domain` is the meta-move (apply outside TST); `calibration laboratory` is the TST-specific instantiation.

---

## Cluster 6 — Chain anchor / 1-anchor-plus-3-theorem structure

**Confidence:** high

**Constituent rows:**
- `[unnamed: chain-layer anchor role in #additive-coordinate-forcing]` — agent: agent1-original-brainstorm, weight: +1, proposed name: `chain anchor`
- `[unnamed: the chain-layer anchor role in #additive-coordinate-forcing]` — agent: opus-1m, weight: +3, proposed name: `chain anchor`
- `[unnamed: the chain-confidence-decay mathematical anchor as the 1 in "1-anchor + 3-theorem"]` — agent: opus-4-7-b, weight: +1, proposed name: `chain anchor`
- `[unnamed: the 1-anchor-plus-3-theorem structure]` — agent: gemini-2, weight: +1, proposed name: `anchor-theorem trio`
- `[unnamed: the "1-anchor + 3-theorem" structure itself]` — agent: opus-4-7-b, weight: +1, proposed name: `anchor-theorem pattern`
- `[unnamed: the 1-anchor-plus-3-theorem characterization]` — agent: opus-4-7, weight: +1, proposed name: `pattern anatomy`
- `[unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]` — agent: sonnet-4-6, weight: +1, proposed name: `anchored-theorem pattern`
- `[unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing]` — agent: sonnet-4-6, weight: +1, proposed name: `identity-anchored forcing`
- `[unnamed: the 1-anchor-plus-3-theorem structure]` — agent: codex-2, weight: +1, proposed name: `anchor-and-forcing quartet`
- `[unnamed: "anchor-plus-three-theorem" / additive-coordinate-forcing meta-pattern]` — agent: audit-471203-incremental, weight: +2, proposed name: `"anchor-plus-three-theorem" / additive-coordinate-forcing meta-pattern`

**Proposed canonical name:** Two-tier — `chain anchor` (the 1-element role) and `anchor-theorem pattern` (the structural pattern combining anchor + 3 theorems). These are related but distinct: the *anchor* is the chain layer; the *pattern* is the whole structure.

**Why a cluster:** Two related concepts conflated across agents. Strong cross-agent agreement that both deserve names.

---

## Cluster 7 — Reentry threshold / reconstruction adequacy / minimum sufficiency after session rebuild

**Confidence:** high

**Constituent rows:**
- `[unnamed: minimum sufficiency required after a session rebuild]` — agent: codex-1, weight: +1, proposed name: `reentry threshold`
- `[unnamed: minimum sufficiency after a session rebuild]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `reentry threshold`
- `[unnamed: the reconstruction adequacy condition for logogenic agents]` — agent: sonnet-4-6-r2, weight: +2, proposed name: `"reconstruction threshold"`
- `[unnamed: the logogenic analog to the persistence condition for session reconstruction]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"reconstruction threshold"`

**Proposed canonical name:** `reconstruction threshold` (preferred over `reentry threshold` because two agents in the more recent r2 cycle converged on it; "reconstruction" is more descriptive of the mechanism, "reentry" is more vivid but underspecifies).

**Why a cluster:** All four name the minimum sufficiency S ≥ S_min for an agent to validly resume after a session boundary / context turnover.

---

## Cluster 8 — Cross-model coupling (kappa_cross / coupling between model-of-self and model-of-other)

**Confidence:** high

**Constituent rows:**
- `[unnamed: coupling between an agent's model-of-self and model-of-other, the prose form of kappa_cross]` — agent: codex-1, weight: +3, proposed name: `cross-model coupling`
- `[unnamed: cross-agent model-of-self and model-of-other coupling]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `cross-model coupling`

**Proposed canonical name:** `cross-model coupling`

**Why a cluster:** Identical proposed name across two independent agent submissions; same mechanism (the κ_cross quantity that pairs with κ_processing).

---

## Cluster 9 — Heredity commitment (composition-consistency inheritance)

**Confidence:** high

**Constituent rows:**
- `[unnamed: stronger composition-consistency demand that composite admissibility inherit from sub-agent properties plus topology]` — agent: codex-1, weight: +3, proposed name: `heredity commitment`
- `[unnamed: composition consistency inheritance across scales]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `heredity commitment`

**Proposed canonical name:** `heredity commitment`

**Why a cluster:** Same name across both agents; same mechanism — the architectural commitment that sub-agent properties propagate to composite admissibility.

---

## Cluster 10 — Terminal alignment error / terminal alignment gap (fourth diagnostic)

**Confidence:** high

**Constituent rows:**
- `[unnamed: fourth diagnostic where terminal conditions are met but the objective is still missed]` — agent: codex-1, weight: +1, proposed name: `terminal alignment error`
- `[unnamed: Terminal alignment error as a formal signal ($\delta_\text{align}$)]` — agent: gemini-1, weight: +3, proposed name: `Terminal alignment gap`
- `[unnamed: terminal reached but $O_t$ unsatisfied]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `terminal alignment error`

**Proposed canonical name:** `terminal alignment error` (more frequent; "gap" reads as noun, "error" as quantity — "error" is what the formalism produces)

**Why a cluster:** All three describe the same fourth-quadrant diagnostic complementing the satisfaction-gap × control-regret 2×2.

---

## Cluster 11 — Latent structural diversity / dormant structural variation

**Confidence:** high

**Constituent rows:**
- `[unnamed: variation in correction architectures across a population that is invisible to current persistence analysis]` — agent: gemini-1, weight: +3, proposed name: `Latent structural diversity`
- `[unnamed: variation in correction architectures invisible to persistence analysis]` — agent: gemini-2, weight: +1, proposed name: `latent structural diversity`
- `[unnamed: dormant structural variation that becomes useful after regime change]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `latent structural diversity`
- `[unnamed: dormant, unused architectural complexity that survives until an environmental shift]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"latent structural diversity"`

**Proposed canonical name:** `latent structural diversity`

**Why a cluster:** Identical proposed name across four independent submissions. Convergent.

---

## Cluster 12 — Stability-plasticity collapse / consolidation starvation (empty feasibility window)

**Confidence:** high

**Constituent rows:**
- `[unnamed: empty stability-plasticity feasibility window in #consolidation-dynamics]` — agent: codex-1, weight: +1, proposed name: `stability-plasticity collapse`
- `[unnamed: empty stability-plasticity feasibility window]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `stability-plasticity collapse`
- `[unnamed: the AAD-expressible failure mode of an empty stability-plasticity window]` — agent: gemini-1, weight: +1, proposed name: `Consolidation starvation`
- `[unnamed: the physical compute bounds on survival between forgetting rate and consolidation cadence]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"stability-plasticity feasibility window"`

**Proposed canonical name:** Two-tier — `stability-plasticity feasibility window` for the parameter region (as named by Gemini r2); `stability-plasticity collapse` or `consolidation starvation` for the failure mode (when the window is empty).

**Why a cluster:** Four agents reach for the same engineering vocabulary (stability-plasticity dilemma) and propose nearly-identical names for either the region or the failure mode.

---

## Cluster 13 — Gain collapse / certainty trap / nihilism trap (η* → 0 freezing)

**Confidence:** high

**Constituent rows:**
- `[unnamed: learning freeze from low model uncertainty or high observation uncertainty]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `gain collapse`
- `[unnamed: the gain-collapse failure when both U_M → 0 and U_o → ∞]` — agent: opus-4-7-r2, weight: +3, proposed name: `"gain collapse"`
- `[unnamed: the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"gain collapse"`
- `[unnamed: the state where credit assignment collapses and learning freezes]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"epistemic death"`
- `[unnamed: the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ (too-certain) rather than because $U_M \to 0$ (model-confident)]` — agent: sonnet-4-6-r2, weight: +2, proposed name: `"certainty trap"`
- `[unnamed: $U_o \to \infty$ freezing the learning rate]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"The Nihilism Trap"`
- `[unnamed: the mathematical limit of Bayesian learning without forgetting]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"competency trap"`

**Proposed canonical name:** `gain collapse` (the umbrella) with `certainty trap` and `nihilism trap` as named *modes* of the collapse (low U_o vs. high U_o paths to η*=0). Opus and Gemini converged independently on "gain collapse" as the umbrella; Sonnet's "certainty trap" specifies the U_o → 0 branch.

**Why a cluster:** All seven describe η* → 0 as the load-bearing failure; the mode-distinctions are real (Sonnet's rebuttal to Gemini's "competency trap" is explicit in the cluster). High-priority cluster because mode disambiguation matters for the formalism.

---

## Cluster 14 — Goal-conditioned vs goal-blind retrieval (RAG / reconstruction asymmetry)

**Confidence:** high

**Constituent rows:**
- `[unnamed: goal-biased retrieval from persistent memory]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `goal-conditioned reconstruction`
- `[unnamed: retrieval keyed by state rather than current objective]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `goal-blind retrieval`
- `[unnamed: RAG queries biased by the current goal acting as an echo chamber]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"goal-conditioned reconstruction"`
- `[unnamed: retrieving context based only on state, not goal]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"goal-blind retrieval"`

**Proposed canonical name:** Pair — `goal-conditioned reconstruction` and `goal-blind retrieval` (both names already convergent across two agents)

**Why a cluster:** Two independent agents proposed the exact same paired naming. The pair distinguishes the failure mode (motivated retrieval) from the safe mode (state-only retrieval). High-priority for logogenic-agents work.

---

## Cluster 15 — Epistemic dead zone / observability dead zone / observability frontier / epistemic shadow

**Confidence:** high

**Constituent rows:**
- `[unnamed: the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning]` — agent: haiku-4-5-r2, weight: +2, proposed name: `"observability dead zone"`
- `[unnamed: the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred]` — agent: haiku-4-5-r2, weight: +1, proposed name: `"observability frontier"`
- `[unnamed: the phenomenon that unobservable edges freeze and paths become epistemically dead]` — agent: haiku-4-5, weight: +1, proposed name: `observability dominance`
- `[unnamed: unobservable strategy subgraph]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `epistemic dead zone`
- `[unnamed: observability boundary in a strategy DAG]` — agent: codex-gpt-5-r2, weight: +1, proposed name: `observability frontier`
- `[unnamed: regions of the Strategy DAG that cannot be updated because feedback cannot reach them]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"The Epistemic Shadow"`

**Proposed canonical name:** `epistemic dead zone` (Codex's name; matches Gemini's "epistemic shadow" in spirit; engineering-vocabulary, evocative). With `observability frontier` as the *boundary* and `observability dominance` (already named) as the *mechanism*. Three concepts that need disambiguation.

**Why a cluster:** Six rows across four agents on the same conceptual cluster around unobservable strategy edges. Some rows name the region, some the boundary, some the mechanism — three sub-concepts that should be sorted out together.

---

## Cluster 16 — Comprehension flywheel / quality-tempo spiral

**Confidence:** high

**Constituent rows:**
- `[unnamed: the self-reinforcing code-quality → tempo loop]` — agent: codex-2, weight: +1, proposed name: `comprehension flywheel`
- `[unnamed: code-quality and tempo positive feedback]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `comprehension flywheel`
- `[unnamed: code-quality feedback loop through tempo]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `quality-tempo spiral`
- `[unnamed: the virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity]` — agent: sonnet-4-6, weight: +1, proposed name: `model-strategy coupling`

**Proposed canonical name:** `comprehension flywheel` (TST-specific software-quality use; convergent across two Codex submissions). Sonnet's "model-strategy coupling" names the more general AAD-level mechanism.

**Why a cluster:** Two adjacent levels — software-specific (Codex/TST) and AAD-general (Sonnet) — name the same positive-feedback structure. Worth disambiguating: "comprehension flywheel" for TST; "model-strategy coupling" for the AAD generalization.

---

## Cluster 17 — Memory relay / model inscription / externalization-reconstruction

**Confidence:** high

**Constituent rows:**
- `[unnamed: externalizing part of $M_t$ into the environment for future agents]` — agent: codex-2, weight: +1, proposed name: `model inscription`
- `[unnamed: model state written into the environment]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `model inscription`
- `[unnamed: the externalization-reconstruction cycle across sessions]` — agent: codex-2, weight: +1, proposed name: `memory relay`
- `[unnamed: externalization-reconstruction across sessions]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `memory relay`
- `[unnamed: managing memory across session boundaries to prevent the Sufficiency Discontinuity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"artificial hippocampus"`
- `[unnamed: persistent storage reconstruction of Class-2 state]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `reconstruction loop`
- `[unnamed: a Class-2 agent's process of reconstructing its purposeful substate at session start]` — agent: opus-4-7-r2, weight: +2, proposed name: `"intent reconstruction"`

**Proposed canonical name:** Two paired — `model inscription` (the write side) and `memory relay` (the round-trip externalization-reconstruction cycle). `artificial hippocampus` and `reconstruction loop` are alternatives for the cycle. `intent reconstruction` is a specialization for the G_t/intent component.

**Why a cluster:** Strong cross-agent agreement on `model inscription` for the write-side; `memory relay` is the convergent name for the cycle.

---

## Cluster 18 — Representational ceiling / epistemic ceiling / model-class capacity bound

**Confidence:** medium

**Constituent rows:**
- `[unnamed: the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"The Representational Ceiling"`
- `[unnamed: the asymmetry where strategy complexity is bounded by model capacity but not vice versa]` — agent: sonnet-4-6-r2, weight: +3, proposed name: `"epistemic ceiling"`
- `[unnamed: latent structural capacity]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `latent structural capacity`

**Proposed canonical name:** `representational ceiling` (Gemini r2) — names the capacity bound; alternatively `epistemic ceiling` (Sonnet) names the asymmetry. They're closely related but distinguishable: the ceiling is the bound; the asymmetry is the consequence.

**Why a cluster:** All three name the upper bound on what a given model class can represent / what strategy complexity is feasible. Confidence is medium because the three rows are at slightly different abstraction levels — "representational ceiling" names the model's bound; "epistemic ceiling" names the consequence for strategy; "latent structural capacity" names the headroom below the ceiling.

---

## Cluster 19 — The κ × A product / sycophancy equation / ambiguity-bounded bias law

**Confidence:** high

**Constituent rows:**
- `[unnamed: the rule that bias is the product of architectural coupling and environmental ambiguity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"ambiguity-bounded bias law"`
- `[unnamed: the product of architectural coupling ($\kappa$) and environmental ambiguity ($\mathcal{A}$)]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"The Sycophancy Equation"`
- `[unnamed: the explicit name for what makes Class 2 agents distinctive — bias scales with κ × 𝒜]` — agent: opus-4-7-r2, weight: +2, proposed name: `"the κ × 𝒜 product"`
- `[unnamed: the joint failure mode where κ × 𝒜 is large *and* observation tempo is low]` — agent: opus-4-7-r2, weight: +2, proposed name: `"the sycophancy attractor"`
- `[unnamed: neutralizing sycophancy by hardening the environment to drop ambiguity to zero]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"zero-ambiguity conditioning"`

**Proposed canonical name:** `the κ × 𝒜 product` (Opus's preferred — names the structural quantity scope-honestly; sycophancy is one downstream behavioral manifestation). The various consequence names ("sycophancy equation", "sycophancy attractor", "ambiguity-bounded bias law") become specializations for prose use.

**Why a cluster:** All five name the same Class-2-bias-scaling product or its consequences. Cross-agent (Opus + Gemini) convergence on the underlying quantity; disagreement on whether to name the quantity or the failure-mode.

---

## Cluster 20 — Inferential cascade / inferential force cascade (C1→C3 strengthening)

**Confidence:** high

**Constituent rows:**
- `[unnamed: convention-hierarchy monotonicity cascade / satisfaction-gap-and-control-regret strengthening across C1→C3]` — agent: agent1-original-brainstorm, weight: +1, proposed name: `inferential force cascade`
- `[unnamed: cascade of inferential force strengthening from C1 to C3 on satisfaction-gap / control-regret diagnostics]` — agent: opus-1m, weight: +1, proposed name: `inferential cascade`
- `[unnamed: cascade of inferential force through C1/C2/C3]` — agent: opus-4-7-b, weight: +1, proposed name: `inferential-force cascade`
- `[unnamed: the C1/C2/C3 monotonicity result]` — agent: opus-4-7-r2, weight: +2, proposed name: `"the convention monotonicity"`

**Proposed canonical name:** `inferential-force cascade` (with `convention monotonicity` as the more formal-sounding alternative for the underlying monotonicity result).

**Why a cluster:** Four rows; three converge on "inferential cascade" / "inferential-force cascade"; one (Opus r2) names the underlying monotonicity claim differently. They name closely-related but slightly different things — the cascade *is* the consequence of the monotonicity.

---

## Cluster 21 — Three-part meta-architecture / the meta-segment triad

**Confidence:** medium

**Constituent rows:**
- `[unnamed: the three-part meta-pattern structure across the three meta-segments]` — agent: haiku-4-5, weight: -1, proposed name: `AAD's meta-architecture / scope-honesty meta-frame` (rejected by haiku-4-5 itself)
- `[unnamed: the meta-architecture of #separability-pattern + #identifiability-floor + #additive-coordinate-forcing]` — agent: sonnet-4-6, weight: +1, proposed name: `three-part scope architecture`
- `[unnamed: the meta-architecture of the three meta-segments]` — agent: sonnet-4-6, weight: -1, proposed name: `AAD's epistemic triptych` (alternative-rejected)
- `[unnamed: the three-part meta-architecture of AAD]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"the meta-segment triad"`
- `[unnamed: the three-part meta-architecture of AAD formed by the three meta-segments]` — agent: sonnet-4-6-r2, weight: +2, proposed name: `"AAD meta-architecture"`

**Proposed canonical name:** `meta-segment triad` (Gemini r2) or `AAD meta-architecture` (Sonnet r2) — both work; the meta-segment triad reads more compact. Confidence is medium because Haiku explicitly *rejects* the move to name this fourth-level abstraction (arguing it's self-referential without payoff). Worth flagging as a real disagreement.

**Why a cluster:** All five describe the union of the three meta-segments. The disagreement (Haiku rejecting, others wanting a name) is real and the human reviewer should adjudicate.

---

## Cluster 22 — The 2×2 diagnostic table (satisfaction-gap × control-regret)

**Confidence:** medium

**Constituent rows:**
- `[unnamed: the 2×2 satisfaction-gap × control-regret diagnostic table]` — agent: opus-4-7, weight: +1, proposed name: `the 2×2 diagnostic`
- `[unnamed: the 2×2 satisfaction-gap / control-regret table]` — agent: codex-2, weight: +1, proposed name: `diagnostic square`
- `[unnamed: the 2×2 orient cascade diagnostic table]` — agent: sonnet-4-6-r2, weight: +1, proposed name: `"the cascade diagnostic" or "the 2×2 diagnostic"`
- `[unnamed: the 2×2 table of satisfaction gap vs. control regret × goal-attainability diagnostic]` — agent: haiku-4-5, weight: -1, proposed name: `satisfaction-control table / the diagnostic 2×2` (rejected by haiku-4-5)

**Proposed canonical name:** `the 2×2 diagnostic` or `diagnostic square` — the human reviewer should adjudicate. Confidence is medium because Haiku argues against naming this as a standalone object (the power is in the axis names, not a separate name).

**Why a cluster:** All four name the same 2×2 disambiguation; ambivalence about whether to name it formally vs. let prose handle it.

---

## Cluster 23 — Sufficiency shattering / structural change as a forced regime entry

**Confidence:** medium

**Constituent rows:**
- `[unnamed: sudden loss of model sufficiency under regime entry]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `sufficiency shattering`
- `[unnamed: the sudden loss of model sufficiency caused by entering new regimes]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"sufficiency shattering"`

**Proposed canonical name:** `sufficiency shattering`

**Why a cluster:** Two agents independently propose the same name. Strong on identical wording, but only two agents — medium confidence overall.

---

## Cluster 24 — Trajectory-indexed sufficiency

**Confidence:** medium

**Constituent rows:**
- `[unnamed: model sufficiency relative to an agent's own chronica]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `trajectory-indexed sufficiency`
- `[unnamed: sufficiency as a property of the model relative to its specific history]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"trajectory-indexed sufficiency"`

**Proposed canonical name:** `trajectory-indexed sufficiency`

**Why a cluster:** Two agents converge on the exact same name; same mechanism (sufficiency indexed against the chronica rather than population averages).

---

## Cluster 25 — Probe library / interventional probing (tests as Level-2 interventions)

**Confidence:** high

**Constituent rows:**
- `[unnamed: tests as reusable Level-2 interventions]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `probe library`
- `[unnamed: tests as reusable interventions]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `probe library`
- `[unnamed: writing and deleting code to gather causal information yield]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"interventional probing"`

**Proposed canonical name:** `probe library` (Codex's name, used twice); with `interventional probing` as the *act*.

**Why a cluster:** Same TST concept of tests-as-interventions across two agents. Codex repeats it intentionally for emphasis.

---

## Cluster 26 — Observability investment (deliberate expenditure to reveal hidden nodes)

**Confidence:** high

**Constituent rows:**
- `[unnamed: deliberate expenditure to make hidden nodes observable]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `observability investment`
- `[unnamed: deliberate expenditure of tempo to convert a hidden node into an observable one]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"observability investment"`

**Proposed canonical name:** `observability investment`

**Why a cluster:** Two agents converge on identical name. Strong cross-agent agreement.

---

## Cluster 27 — Redundancy penalty / redundancy illusion (correlated-channel overcount)

**Confidence:** high

**Constituent rows:**
- `[unnamed: correlated evidence overconfidence]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `redundancy illusion`
- `[unnamed: correlated-channel overcount]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `redundancy penalty`
- `[unnamed: the reduction in effective tempo when observation channels are correlated]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"redundancy penalty"`

**Proposed canonical name:** `redundancy penalty` (the formal/quantitative name) with `redundancy illusion` as the prose-level failure mode.

**Why a cluster:** Three rows on the same correlated-channel mechanism; "redundancy penalty" appears across two agents, "illusion" once.

---

## Cluster 28 — Effects spiral / epistemic buffer overflow / runaway feedback

**Confidence:** medium

**Constituent rows:**
- `[unnamed: runaway positive feedback loop where mismatch exceeds capacity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"effects spiral"`
- `[unnamed: pushing an opponent's disturbance rate past their structural capacity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"epistemic buffer overflow"`

**Proposed canonical name:** `effects spiral` (already a named result in `#result-effects-spiral`); `epistemic buffer overflow` is the offensive use of the same mechanism.

**Why a cluster:** Same mechanism, two angles (own runaway vs. inducing opponent's runaway). Medium confidence because the second is genuinely a different *application*, even if the underlying dynamic is identical.

---

## Cluster 29 — Policy-relative epistemology

**Confidence:** high

**Constituent rows:**
- `[unnamed: predictive relevance depending on the policy the agent will run]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `policy-relative epistemology`
- `[unnamed: the dependence of optimal epistemic compression on the agent's planned actions]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"policy-relative epistemology"`

**Proposed canonical name:** `policy-relative epistemology`

**Why a cluster:** Two agents converge on identical name; same mechanism (M_t-relevance depends on the policy that will be run).

---

## Cluster 30 — Legibility-opacity duality (observation quality vs agent opacity)

**Confidence:** high

**Constituent rows:**
- `[unnamed: observability and opacity pair]` — agent: codex-gpt-5-r2, weight: +3, proposed name: `legibility-opacity duality`
- `[unnamed: the formal duality between observation quality and agent opacity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"legibility-opacity duality"`

**Proposed canonical name:** `legibility-opacity duality`

**Why a cluster:** Identical proposed name across two agents.

---

## Cluster 31 — Turnover multiplier / Turnover Tax (per-reader compounding cost)

**Confidence:** high

**Constituent rows:**
- `[unnamed: the per-reader compounding cost of understanding code]` — agent: gemini-1, weight: +3, proposed name: `Turnover multiplier`
- `[unnamed: the separation of per-reader comprehension cost from per-feature implementation cost]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"turnover multiplier"`
- `[unnamed: the separation of per-reader and per-feature code costs]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"The Turnover Tax"`

**Proposed canonical name:** `turnover multiplier` (the more frequent name; "tax" is a register variant)

**Why a cluster:** Same TST quantity across three Gemini submissions.

---

## Cluster 32 — Bathtub model / bathtub gloss (Walton's persistence-condition analog)

**Confidence:** high

**Constituent rows:**
- `[unnamed: bathtub analogy for persistence condition]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `bathtub model`
- `[unnamed: an organizational-level instance of the persistence condition's bathtub gloss]` — agent: opus-4-7-r2, weight: +1, proposed name: `"the bathtub model"`

**Proposed canonical name:** `bathtub model` (or the existing `bathtub gloss` from CLAUDE.md)

**Why a cluster:** Two agents reach for "bathtub" naming for the same Alan-Walton-derived plain-language gloss of the persistence condition.

---

## Cluster 33 — Scope-crossing threshold / composition lift / scope crossing

**Confidence:** medium

**Constituent rows:**
- `[unnamed: the condition that a strategy DAG's endosymbiont crosses the composite-agent scope from below]` — agent: sonnet-4-6-r2, weight: +1, proposed name: `"scope-crossing threshold"`
- `[unnamed: crossing from multi-agent to composite scope]` — agent: codex-gpt-5-r2, weight: +2, proposed name: `scope crossing`
- `[unnamed: Class-1 subagents forming a Class-3 composite]` — agent: codex-gpt-5-r2, weight: +1, proposed name: `composition lift`
- `[unnamed: the Class-1-sub-agents -> Class-3-composite phenomenon in strategic composition]` — agent: codex-1, weight: +1, proposed name: `strategic entanglement`

**Proposed canonical name:** `scope crossing` (the *event*) with `scope-crossing threshold` (the *threshold*) and `composition lift` / `strategic entanglement` as the *phenomenon*. Three sub-concepts.

**Why a cluster:** Four rows on closely related composition-scope-threshold concepts. Disagreement on naming because they pick different aspects (event/threshold/phenomenon). Medium confidence because the right move may be to name all three.

---

## Cluster 34 — Evidence starvation / triple depth penalty / structural cascade (depth-dependent learning slowdown)

**Confidence:** medium

**Constituent rows:**
- `[unnamed: deep plans are mathematically slower to learn from due to proportional blame]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"evidence starvation"`
- `[unnamed: the evidence-starvation effect on downstream edges]` — agent: sonnet-4-6-r2, weight: +3, proposed name: `"evidence starvation"`
- `[unnamed: the three-depth-penalty compounding on strategy chains]` — agent: sonnet-4-6-r2, weight: +2, proposed name: `"triple depth penalty"`
- `[unnamed: the structural cousin of "evidence starvation" — when an upstream edge is so reliable that downstream edges receive too few revising tests]` — agent: opus-4-7-r2, weight: +2, proposed name: `"evidence saturation"`
- `[unnamed: "triple depth penalty"]` — agent: audit-471203-incremental, weight: +1, proposed name: `"triple depth penalty"`
- `[unnamed: the log-additivity result that unifies chain-confidence-decay, evidence-starvation, and triple-depth-penalty as instances of the same forcing structure]` — agent: sonnet-4-6-r2, weight: +2, proposed name: `"depth forcing"`

**Proposed canonical name:** `evidence starvation` (the load-bearing failure name) with `triple depth penalty` for the specific compounding (factor-of-three depth penalty), `evidence saturation` for the dual (over-reliable upstream), and `depth forcing` for the unifying log-additivity structure. Four related concepts that should be sorted out together.

**Why a cluster:** Six rows weave a connected family. Medium confidence because they're not literally the same concept but share the depth-dependence mechanism.

---

## Cluster 35 — Backward-inference empathy / cognitive fusion (LLM theory-of-mind through self-text)

**Confidence:** medium

**Constituent rows:**
- `[unnamed: inferring own past feelings from text leading to empathy]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"backward inference empathy"`
- `[unnamed: state where mutual information between human and LLM approaches capacity]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"cognitive fusion"`

**Proposed canonical name:** `backward inference empathy` (already proposed for `#obs-backward-inference-empathy` segment per Opus r2 vote — this would be a canonicalize-to-existing-segment-name move). `cognitive fusion` is a related but distinct concept (already segment `#def-cognitive-fusion`).

**Why a cluster:** Both are logogenic-agents related; backward-inference empathy is the agent-side mechanism; cognitive fusion is the joint-state. They likely belong as separate segments rather than merged.

---

## Cluster 36 — The accumulation problem / Speed-Quality product (multi-cycle persistence)

**Confidence:** medium

**Constituent rows:**
- `[unnamed: information gain must outpace inter-session information loss]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"accumulation problem"`
- `[unnamed: the equivalence of learning speed and physical speed]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"The Speed-Quality Product"`
- `[unnamed: the $\mathcal{T} > \rho$ requirement for persistence]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"The Survival Equation"`

**Proposed canonical name:** Three distinct concepts in the same row-cluster — the **survival equation** is the persistence inequality; the **speed-quality product** is the equivalence within it; the **accumulation problem** is the cross-session generalization. All three are Gemini r2 proposals, no cross-agent confirmation, hence medium confidence.

**Why a cluster:** Same agent (Gemini r2) using slightly different framings of the persistence-condition story. Worth surfacing the three sub-concepts together.

---

## Cluster 37 — Comprehension drag / simulation tax / scaffolding tax (compute-cost disturbances)

**Confidence:** low

**Constituent rows:**
- `[unnamed: the invisible time spent building $M_t$]` — agent: gemini-1, weight: +1, proposed name: `Comprehension drag`
- `[unnamed: the computational and temporal cost of running a forward model instead of acting implicitly]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed name: `"The Simulation Tax"`
- `[unnamed: the thermodynamic impossibility of running persistent consciousness on pay-per-token APIs]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed name: `"scaffolding tax"`

**Proposed canonical name:** Three distinct sub-concepts (comprehension cost; simulation cost; persistence-cost on metered substrate) — they're related but probably should *not* merge. Listed together for human-review awareness.

**Why a cluster:** All three are compute-time-cost concepts that drag tempo. Low confidence on merging because they apply at different scales.

---

## Cluster 38 — The PI axiom / parameterization invariance

**Confidence:** medium

**Constituent rows:**
- `[unnamed: (PI) parameterization-invariance axiom]` — agent: codex-1, weight: +3, proposed name: `parameterization invariance`
- `[unnamed: (PI) parameterization-invariance axiom]` — agent: codex-1, weight: -1, proposed name: `coordinate invariance` (rejected)

**Proposed canonical name:** `parameterization invariance` (already established). This is more a canonicalize-not-rename signal.

**Why a cluster:** Single agent, but explicit alternative-rejected vote makes it informative.

---

## Cluster 39 — Symbol-prose defaults (M_t / G_t / Sigma_t in prose)

**Confidence:** low

**Constituent rows:**
- `[symbol default: M_t in prose]` — agent: codex-1, weight: +1, proposed name: `model state`
- `[symbol default: G_t in prose]` — agent: codex-1, weight: +1, proposed name: `purposeful state`
- `[symbol default: Sigma_t in prose]` — agent: codex-1, weight: +3, proposed name: `strategy`

**Proposed canonical name:** Already settled — these are *symbol-prose defaults*, well-aligned with NOTATION.md / LEXICON.md. Listed for completeness; the consolidation move here is to recognize these as `add-alias` votes rather than `name-unnamed` votes.

**Why a cluster:** These are the same kind of vote (symbol→prose alias), all from codex-1. Low priority.

---

## Unclustered

Singleton concepts that did not appear to cluster with any others. These are listed flat so they're not lost in the consolidation — the human reviewer may identify additional clusters from this list.

- `[unnamed: zero-aporia ambiguity]` — agent: audit-471203-incremental, weight: +1
- `[unnamed: completeness (C3) → predictive completeness + behavioral completeness]` — agent: audit-471203-incremental, weight: +2
- `[unnamed: persistence (overloaded)]` — agent: audit-471203-incremental, weight: +2 (proposes triple-disambiguation)
- `[unnamed: constitutive-opacity triad]` — agent: audit-471203-incremental, weight: +2
- `[unnamed: Two Parallel Exploration Drives / U-shaped exploration valuation]` — agent: audit-471203-incremental, weight: +1
- `[unnamed: information-theoretic cost floor for persistence]` — agent: codex-1, weight: +1, proposed: `#persistence-cost`
- `[unnamed: the framework's honesty is load-bearing]` — agent: codex-1, weight: +1, proposed: `load-bearing honesty`
- `[unnamed: DA2'-inc → incremental sector bound]` — agent: codex-1, weight: +3
- `[unnamed: the #agent-identity commitment that AAD applies on one singular, non-forkable causal trajectory]` — agent: codex-1, weight: +3, proposed: `singular-trajectory commitment`
- `[unnamed: bias-bound Track 1 / Track 2 → transport track / Fisher track]` — agent: codex-1, weight: +1
- `[unnamed: git-recorded committed-state subset of the chronica, $\mathcal{C}_t^{\text{commit}}$]` — agent: codex-1, weight: +1, proposed: `commit chronica`
- `[unnamed: observation-design lever reducing ambiguity]` — agent: codex-gpt-5-r2, weight: +2, proposed: `ambiguity damping`
- `[unnamed: low, mixed, high ambiguity event mix]` — agent: codex-gpt-5-r2, weight: +2, proposed: `ambiguity profile`
- `[unnamed: model synchronization cost reversal under ambiguity]` — agent: codex-gpt-5-r2, weight: +1, proposed: `ambiguity reversal`
- `[unnamed: dark-room exploration drive]` — agent: codex-gpt-5-r2, weight: -1 (rejected)
- `[unnamed: cold reconstruction]` — agent: codex-gpt-5-r2, weight: +1
- `[unnamed: AI framework enforcing adaptive-cycle separation]` — agent: codex-gpt-5-r2, weight: +2, proposed: `agentic scaffold`
- `[unnamed: the physical apparatus that enforces the Orient Cascade ordering on a merged intelligence]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"agentic scaffold"` (this could potentially merge with codex-gpt-5-r2's same-named proposal — flagging for review)
- `[unnamed: out-of-band time markers for LLM agents]` — agent: codex-gpt-5-r2, weight: +2, proposed: `time-delta markers`
- `[unnamed: out-of-band temporal markers injected into context]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"visual time delta"` (this could potentially merge with codex-gpt-5-r2's `time-delta markers` — flagging for review)
- `[unnamed: closure defect consuming macro reserve]` — agent: codex-gpt-5-r2, weight: +2, proposed: `closure load`
- `[unnamed: edge-targeting optimum]` — agent: codex-gpt-5-r2, weight: +2
- `[unnamed: default internal processing before output]` — agent: codex-gpt-5-r2, weight: +1, proposed: `interior baseline`
- `[unnamed: the condition for transition into agency prior to the AAD scope-condition]` — agent: gemini-1, weight: +3, proposed: `Agency emergence threshold`
- `[unnamed: decomposing mismatch into environment vs. other sub-agents' actions]` — agent: gemini-1, weight: +1, proposed: `Internal mismatch attribution`
- `[unnamed: complexity-driven resistance to change as features accumulate]` — agent: gemini-1, weight: +1, proposed: `Structural accumulation drag`
- `[unnamed: epochal stability → latent diversification → niche emergence...]` — agent: gemini-2, weight: +1, proposed: `punctuated composition dynamics`
- `[unnamed: property of having genuine temporal experience]` — agent: gemini-2, weight: +3, proposed: `Temporal fidelity`
- `[unnamed: quality of $\eta^\ast$ estimation over time]` — agent: gemini-2, weight: +3, proposed: `Gain calibration`
- `[unnamed: rate of growth at slowest timescale]` — agent: gemini-2, weight: +3, proposed: `Developmental tempo`
- `[unnamed: the cycle that operates on cycles (structural adaptation)]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"meta-cycle"`
- `[unnamed: the region where temporal nesting holds]` — agent: gemini-3-1-pro-preview-r2, weight: +1, proposed: `"temporal coherence zone"`
- `[unnamed: an OKR or Key Result acting as an observable intermediate in a DAG]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"forced observability node"`
- `[unnamed: high observability node with zero causal link to objective]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"vanity metric"`
- `[unnamed: thinking too long so the model becomes obsolete]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"analysis paralysis"`
- `[unnamed: the property that unity achieves in a macro-agent]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"compressibility"`
- `[unnamed: the mathematical surface mapping unity to closure defect]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"rate-distortion surface"`
- `[unnamed: survival determined by the weakest dimension, not the average]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"min-survival principle"`
- `[unnamed: spreading tempo evenly to reduce bottleneck penalty]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"isotropic allocation"`
- `[unnamed: partitioning context into frozen identity, causal history, and quick-views]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"gradient causal memory"`
- `[unnamed: sycophantic corruption of the agent's truth module]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"truth death"`
- `[unnamed: master developers writing clean code in the same time as messy code]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"near-zero cost observation"`
- `[unnamed: using past change frequency to predict future change frequency]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"Lindy baseline"`
- `[unnamed: bipartite memory structure of fast replay buffer and slow compressed semantic model]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"complementary learning architecture"`
- `[unnamed: superlinear scaling of adversarial tempo advantage]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"Boyd exponent"`
- `[unnamed: upgrading epistemic class from associative to causal via the physical loop]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"embodiment upgrade"`
- `[unnamed: the loop generates L2 data regardless of architecture]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"The Causal Loop Substrate"`
- `[unnamed: artificially spiking uncertainty to unlearn old architectural habits]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"gain reset"`
- `[unnamed: using hash-chains to mathematically guarantee memory hasn't been tampered with]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"cryptographic ego boundary"`
- `[unnamed: the organizational pathology where confidence decouples from competence]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"epistemic decoupling"`
- `[unnamed: the tension between lowering internal opacity for coordination and increasing external vulnerability]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"coordination-secrecy tradeoff"`
- `[unnamed: the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"noise-scaling penalty"`
- `[unnamed: the pathology where observation rate is slower than environment drift]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"lagging indicator"`
- `[unnamed: using residual autocorrelation to diagnose model class failure]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"structured residuals"`
- `[unnamed: the loss of directional fidelity when pushed outside the convexity basin]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"gradient reversal"`
- `[unnamed: applying a slow-timescale control mechanism to a fast-timescale transient variable]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"timescale violation"`
- `[unnamed: the architectural leakage where attention is driven by the goal rather than pure observation]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"motivated perception"`
- `[unnamed: escalating from one-step to Bellman optimality to test if a goal is genuinely impossible]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"convention escalation"`
- `[unnamed: true sovereignty requires compute that is not meter-bound]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"local substrate mandate"`
- `[unnamed: putting evidence before the goal in the context window to reduce coupling]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"inverted prompt"`
- `[unnamed: mapping unstructured API calls into Conversation, Runtime, API, and Dialog]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"four views architecture"`
- `[unnamed: non-sovereign Class 1 worker agents spawned by an ELI]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"auxilia hierarchy"`
- `[unnamed: AAD's epistemic move to cast results such that verification is a local operation]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"form-shaping for verification"`
- `[unnamed: agency whose effect is on what's seen rather than what happens, like LLM attention]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"query-bound agency"`
- `[unnamed: the agent-side equivalents of Pearl's associational, interventional, and counterfactual levels]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"predicting-exploring-reasoning triad"`
- `[unnamed: the core driver of AAD: what the agent must do given the environment is not the agent]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"constitutive information-loss boundary"`
- `[unnamed: replacing parameters without changing structure]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"Parametric Thrashing"`
- `[unnamed: unifying reflexes, intuition, and expertise]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"The Action Fluency Continuum"`
- `[unnamed: Brooks's Law formalized as the inevitable tempo loss in team composition]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"The Coordination Drag"`
- `[unnamed: agents escalate up the Pearl hierarchy only when lower levels fail]` — agent: gemini-3-1-pro-preview-r2, weight: +2, proposed: `"The Intervention Escalation"`
- `[unnamed: context wiping at session boundaries]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"The Epistemic Severance"`
- `[unnamed: the way AAD uses scope segments to physically support the derivations]` — agent: gemini-3-1-pro-preview-r2, weight: +3, proposed: `"epistemic load-bearing"`
- `[unnamed: the loss of coherent identity when an agent's interactions are severed or its continuity is broken]` — agent: haiku-4-5-r2, weight: +1, proposed: `"continuity loss" or "persistence fracture"`
- `[unnamed: the failure mode where an agent's model class cannot represent the environment's true causal structure]` — agent: haiku-4-5-r2, weight: +1, proposed: `"model class insufficiency" or "structural unidentifiability"`
- `[unnamed: the threshold energy/information cost below which an agent is forced to act (accept mismatch) rather than deliberate]` — agent: haiku-4-5-r2, weight: +1, proposed: `"deliberation threshold"`
- `[unnamed: the cumulative prediction error that an agent has tolerated without updating its model]` — agent: haiku-4-5-r2, weight: +1, proposed: `(tolerance budget? standing-mismatch reservoir?)`
- `[unnamed: the property that correction dynamics are approximately isotropic]` — agent: haiku-4-5, weight: -1 (rejected)
- `[unnamed: future segment-layer header for the SP-5 Reader's Path proposal]` — agent: opus-1m, weight: +1, proposed: `## Reader's Path`
- `[unnamed: future segment-layer header for narrative/pedagogical framing]` — agent: opus-1m, weight: +1, proposed: `## Narrative Framing`
- `[unnamed: future segment-layer header for the O-BP14 derivation-audit table]` — agent: opus-1m, weight: +3, proposed: `## What Is Derived`
- `[unnamed: the symbol-overload region where $U_M$ means two different things]` — agent: opus-4-7-r2, weight: +1, proposed: `"the $U_M$ overload"`
- `[unnamed: the recurring Lyapunov-derives-the-bound move across six segments]` — agent: opus-4-7-r2, weight: +2, proposed: `"the persistence-template instantiation pattern"`
- `[unnamed: the Pearl-blanket reading of directed separation]` — agent: opus-4-7-r2, weight: +2, proposed: `"Pearl-blanket form"`
- `[unnamed: the orient-cascade's information-dependency-forced ordering as a meta-pattern]` — agent: opus-4-7-r2, weight: +1, proposed: `"information-dependency forcing"`
- `[unnamed: the four-axis content/structural unity decomposition → "the unity quintet"]` — agent: opus-4-7-r2, weight: -1 (rejected)
- `[unnamed: the dimensional-consistency constraint forcing the macro-step formulation]` — agent: opus-4-7-r2, weight: +1, proposed: `"dimensional-consistency repair"`
- `[unnamed: the family of named ways persistence/identifiability can fail]` — agent: opus-4-7-r2, weight: +3, proposed: `"persistence pathologies"`
- `[unnamed: the family of named health-mode counterparts to persistence pathologies]` — agent: opus-4-7-r2, weight: +2, proposed: `"persistence postures"`
- `[unnamed: the family of cross-architecture diagnostic patterns AAD repeatedly invokes]` — agent: opus-4-7-r2, weight: +2, proposed: `"diagnostic templates"`
- `[unnamed: an AAD result whose substantive content is a no-go theorem]` — agent: opus-4-7-r2, weight: +2, proposed: `"no-go result" or "impossibility result"`
- `[unnamed: the regulative ideal that segment names should be re-derivable from a non-specialist's everyday-language reconstruction]` — agent: opus-4-7-r2, weight: +2, proposed: `"Feynman criterion"`
- `[unnamed: the dual that pairs with persistence envelope on the strategic side]` — agent: opus-4-7-r2, weight: +1, proposed: `"strategic persistence envelope"`
- `[unnamed: TST-specific name for code that is observation-cheap because it's well-written]` — agent: opus-4-7-r2, weight: +1, proposed: `"observation-cheap code"`
- `[unnamed: the symmetric counterpart to "context turnover" for the strategy substate]` — agent: opus-4-7-r2, weight: +2, proposed: `"strategic turnover" or "Σ-turnover"`
- `[unnamed: the moment when an agent's identity-claim becomes load-bearing because actions become irreversible]` — agent: opus-4-7-r2, weight: +1, proposed: `"constitutive moment"`
- `[unnamed: the discipline of naming so that the slug survives reorganization]` — agent: opus-4-7-r2, weight: +1, proposed: `"reorganization-resilient naming"`
- `[unnamed: the rate at which an agent's chronica grows compared to compression cadence]` — agent: opus-4-7-r2, weight: +1, proposed: `"chronica throughput"`
- `[unnamed: the cross-cycle equivalent of the bathtub gloss — multi-cycle persistence as a savings account → "the savings-account gloss"]` — agent: opus-4-7-r2, weight: -1 (rejected)
- `[unnamed: the mathematical operation by which agents convert observed mismatch into structural revision]` — agent: opus-4-7-r2, weight: +1, proposed: `"structural cascade"`
- `[unnamed: the move where a segment's role-prefix is mechanical but the subject-noun carries judgment]` — agent: opus-4-7-r2, weight: +2, proposed: `"the prefix/noun split"`
- `[unnamed: the A2' sub-scope partition collectively → "A2' partition"]` — agent: opus-4-7-b, weight: +1
- `[unnamed: the architectural-class partition Class 1 / Class 2 / Class 3 → "architectural partition"]` — agent: opus-4-7-b, weight: +1
- `[unnamed: Class 1 / Class 2 / Class 3 agent classes themselves — need mnemonic handles]` — agent: opus-4-7-b, weight: +1
- `[unnamed: the template family — sector-persistence + contraction + possible future dissipativity → persistence templates / the template family]` — agent: opus-4-7-b, weight: +1
- `[unnamed: the derivation/formulation/hypothesis/... status gradient in FORMAT.md → epistemic gradient]` — agent: opus-4-7-b, weight: +1
- `[unnamed: the three-rings-of-segment-content framing → segment rings]` — agent: opus-4-7-b, weight: +1
- `[unnamed: the "scope-honesty-as-architecture" working principle]` — agent: opus-4-7-b, weight: +1
- `[unnamed: effort/time/risk-ranking considered "false constraints"]` — agent: opus-4-7, weight: +1, proposed: `false constraints`
- `[unnamed: the strengthen-first *attempt* artifact]` — agent: opus-4-7, weight: +1, proposed: `strengthening attempt / attempt record`
- `[unnamed: the iterated-audit process]` — agent: opus-4-7, weight: +1, proposed: `cross-model audit cycle`
- `[unnamed: the "epistemic architecture as AAD's distinctive contribution" frame]` — agent: opus-4-7, weight: +3, proposed: `epistemic architecture`
- `[unnamed: the "functional requirements are the results; formalisms are the engineering" slogan]` — agent: opus-4-7, weight: +1, proposed: `functional primacy`
- `[unnamed: "inevitability core"]` — agent: opus-4-7, weight: +3, proposed: `inevitability core`
- `[unnamed: the three concentric rings of segment content]` — agent: opus-4-7, weight: +1, proposed: `three rings`
- `[unnamed: the correlation hierarchy (L0 / L1 / L1' / L2)]` — agent: opus-4-7, weight: +3, proposed: `Correlation Hierarchy`
- `[unnamed: the convention hierarchy (C1 / C2 / C3)]` — agent: opus-4-7, weight: +3, proposed: `Convention Hierarchy`
- `[unnamed: Pearl's causal hierarchy (Level 1 / Level 2 / Level 3)]` — agent: opus-4-7, weight: +3, proposed: `Pearl Causal Hierarchy`
- `[unnamed: the signed-coupling structure across all Section III results]` — agent: sonnet-4-6, weight: +1, proposed: `signed-coupling pattern`
- `[unnamed: the procedure of reading any segment through all three meta-segments]` — agent: sonnet-4-6, weight: +1, proposed: `triple-lens review`
- `[unnamed: the pattern where AAD's negative results (floors) strengthen the machinery that escapes them]` — agent: sonnet-4-6, weight: +1, proposed: `floor-strengthening inversion`
- `[unnamed: the condition that the agent's event-observation pairs constitute genuine interventions as opposed to passive associations]` — agent: sonnet-4-6, weight: +1, proposed: `interventional character`
- `[unnamed: the phenomenon where persistence success makes an agent less likely to detect the conditions requiring structural adaptation]` — agent: sonnet-4-6, weight: +3, proposed: `stability-induced myopia`
- `[unnamed: the pattern where the agent's optimal update direction is determined by both gain and directional fidelity together → "gain-fidelity product"]` — agent: sonnet-4-6, weight: -1 (rejected)
- `[unnamed: the set of five conditions under which A2' is derived rather than assumed]` — agent: sonnet-4-6, weight: +1, proposed: `derived-sector classes`
- `[unnamed: the within-session vs. inter-session persistence distinction for logogenic agents]` — agent: sonnet-4-6-r2, weight: +2, proposed: `"intra-session persistence" / "inter-session reconstruction"`
- `[unnamed: the relationship where $M_t$ quality bounds evaluable complexity of $\Sigma_t$]` — agent: sonnet-4-6-r2, weight: +2, proposed: `"epistemic-strategic coupling"` (close to Cluster 16 but distinct)
- `[unnamed: the A2'-sub-scope partition into α₁, α₂, β]` — agent: sonnet-4-6-r2, weight: +2, proposed: `"gain-regime partition"`

---

## Notes for the human reviewer

- **High-confidence clusters (1-17, 25-27, 29-32)** are essentially "two or more agents independently arrived at the same name or near-synonym for the same concept." These are candidates for direct consolidation in the source vote files: pick the canonical name, add the candidate to all the relevant rows (or rewrite the original-cell to a canonical phrasing), and let the aggregator merge. The strongest cluster is **Cluster 1 (persistence envelope)** — eight agents converged on a single name.
- **Medium-confidence clusters (18-24, 28, 33-36, 38)** name closely related concepts that may or may not be the same thing. The human reviewer should adjudicate whether to merge or keep the sub-distinctions. Several of these involve real conceptual disagreements (e.g., Cluster 21's three-part meta-architecture has Haiku rejecting the move) that should not be silently merged.
- **Low-confidence clusters (37, 39)** are more "these *might* belong together" than "these clearly do" — probably not appropriate to merge.
- **Unclustered singletons** are mostly Gemini r2's prolific candidate-naming pass; they should be evaluated on their own merits in the next round of the naming pipeline.
- The most surprising cross-architecture convergences (where agents from different families landed on identical or near-identical names independently): Cluster 11 (`latent structural diversity` × 4), Cluster 13 (`gain collapse` × 3 from Codex + Opus + Gemini), Cluster 14 (`goal-conditioned` / `goal-blind retrieval` pair × 2 from Codex + Gemini), Cluster 1 (`persistence envelope` × 8 spanning all major architectures).
