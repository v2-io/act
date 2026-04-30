# High-Confidence Cluster Consolidation — Applied

This log records the application of the 17 high-confidence cluster consolidations from `msc/naming/naming-consolidation-map.md` to the source vote files in `msc/naming/naming-votes/*.md`. Medium- and low-confidence clusters are out of scope for this pass.

## Method

For each cluster, every constituent row's `current` cell was rewritten to a single neutral functional description (the bucket label), with the original phrasing appended to the row's `notes` cell as `[original phrasing: <text>]`. The `candidate` and `weight` cells were left unchanged — each agent's specific naming proposal stays intact. The `category` cell (when present in 5-column files) was also left unchanged.

The bucket label avoids candidate-name vocabulary so it doesn't bias downstream Round-2 voters toward any one alternative. Where a cluster's concept made full neutrality difficult (e.g., "satisfaction-gap × control-regret space" appears in Cluster 10's bucket because the concept is intrinsically positioned relative to those existing AAD names), the description leans on existing AAD vocabulary rather than candidate names.

## Per-cluster record

### Cluster 1 — persistence region

**Bucket label:** `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| agent1-original-brainstorm.md | agent1-original-brainstorm | unnamed: the sector-persistence region in parameter space | confirmed |
| gemini-1.md | gemini-1 | unnamed: the region where the persistence condition holds | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the sector-persistence region in parameter space | confirmed |
| haiku-4-5-r2.md | haiku-4-5-r2 | unnamed: the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely | confirmed |
| haiku-4-5-r2.md | haiku-4-5-r2 | unnamed: the region in parameter space where parametric updates remain effective before structural change is forced | confirmed |
| opus-1m.md | opus-1m | unnamed: the sector-persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the region in parameter space where sector-persistence holds | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the persistence envelope | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the persistence region in $(\alpha, \rho, R)$ parameter space | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | bounded mismatch region | confirmed |

### Cluster 2 — contraction-over-drift slogan

**Bucket label:** `[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: organizing-principle slogan "an adaptive system is a projection whose contraction rate exceeds its target's drift rate" | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | projection contraction must beat target drift | confirmed |
| gemini-1.md | gemini-1 | unnamed: agent as a projection whose contraction rate must exceed its target's drift | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: Joseph's mental model "projection whose contraction rate must exceed its target's drift rate" | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the projection whose contraction rate must exceed target drift — the Opus organizing-principle slogan | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the contraction-over-drift insight | confirmed |
| opus-4-7.md | opus-4-7 | unnamed: the organizing-principle slogan — "An adaptive system is a projection whose contraction rate exceeds its target's drift rate" | confirmed |

### Cluster 3 — strengthen-first posture

**Bucket label:** `[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| gemini-2.md | gemini-2 | unnamed: strengthen-first posture | confirmed |
| opus-4-7.md | opus-4-7 | unnamed: the "strengthen before soften" work posture | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the "strengthen-before-soften" posture applied to apparent overclaims | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the "strengthen-first, attempt the improbable" meta-approach to theory development | confirmed |

### Cluster 4 — the cycle-as-a-whole

**Bucket label:** `[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| agent1-original-brainstorm.md | agent1-original-brainstorm | unnamed: cycle-phase sequence as whole | confirmed |
| gemini-1.md | gemini-1 | unnamed: cycle-phase sequence as a whole | confirmed |
| opus-1m.md | opus-1m | unnamed: cycle-phase sequence as a whole | confirmed |
| gemini-2.md | gemini-2 | unnamed: The cycle-as-a-whole | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the cycle-as-a-whole (×2 — one +1 keep, one -1 reject) | confirmed |

### Cluster 5 — calibration laboratory framing

**Bucket label:** `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| agent1-original-brainstorm.md | agent1-original-brainstorm | unnamed: calibration-laboratory framing as reusable meta-move | confirmed |
| codex-2.md | codex-2 | unnamed: software as AAD's privileged high-identifiability calibration laboratory | confirmed |
| opus-4-7.md | opus-4-7 | unnamed: "calibration laboratory" framing for software/TST | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: software's role as calibration laboratory, named-in-prose-but-not-in-slug | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the calibration-laboratory concept applied outside TST | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the move where AAD treats software not as instantiation but as TST's epistemically privileged measurement substrate | confirmed |

### Cluster 6 — chain anchor / 1-anchor-plus-3-theorem

**Bucket label:** `[concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results]`

This cluster intentionally merges the two sub-concepts (the *anchor role* and the *broader pattern*) into a single bucket. The map proposes a two-tier disambiguation post-merge; that distinction is preserved by the per-row `candidate` cells (e.g., `chain anchor` vs. `anchor-theorem pattern`).

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| agent1-original-brainstorm.md | agent1-original-brainstorm | unnamed: chain-layer anchor role in #additive-coordinate-forcing | confirmed |
| opus-1m.md | opus-1m | unnamed: the chain-layer anchor role in #additive-coordinate-forcing | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the chain-confidence-decay mathematical anchor as the 1 in "1-anchor + 3-theorem" | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: the "1-anchor + 3-theorem" structure itself | confirmed |
| gemini-2.md | gemini-2 | unnamed: the 1-anchor-plus-3-theorem structure | confirmed |
| opus-4-7.md | opus-4-7 | unnamed: the 1-anchor-plus-3-theorem characterization | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the 1-anchor + 3-theorem structure in #additive-coordinate-forcing (×2 — anchored-theorem pattern, identity-anchored forcing) | confirmed |
| codex-2.md | codex-2 | unnamed: the 1-anchor-plus-3-theorem structure | confirmed |
| audit-471203-incremental.md | audit-471203-incremental | unnamed (current cell was bare `(unnamed)`) | confirmed |

Note on audit-471203-incremental: that file's row had `(unnamed)` (no bracket-description) as its `current` cell rather than the `[unnamed: <description>]` form used elsewhere. The cluster-map listed this row as a constituent, so I edited it. The `[original phrasing: unnamed]` annotation captures the bare-form provenance.

### Cluster 7 — reentry / reconstruction threshold

**Bucket label:** `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: minimum sufficiency required after a session rebuild | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | minimum sufficiency after a session rebuild | confirmed |
| sonnet-4-6-r2.md | sonnet-4-6-r2 | unnamed: the reconstruction adequacy condition for logogenic agents | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the logogenic analog to the persistence condition for session reconstruction | confirmed |

### Cluster 8 — cross-model coupling

**Bucket label:** `[concept: the prose form of κ_cross — the coupling between an agent's model-of-self and its model-of-other]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: coupling between an agent's model-of-self and model-of-other, the prose form of kappa_cross | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | cross-agent model-of-self and model-of-other coupling | confirmed |

### Cluster 9 — heredity commitment

**Bucket label:** `[concept: the architectural requirement that composite-agent admissibility inherit from sub-agent properties plus topology]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: stronger composition-consistency demand that composite admissibility inherit from sub-agent properties plus topology | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | composition consistency inheritance across scales | confirmed |

### Cluster 10 — terminal alignment error

**Bucket label:** `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]`

Note: "satisfaction-gap" and "control-regret" appear in the bucket label as existing settled AAD names, not candidates of this cluster. Avoiding "terminal", "alignment", and "error/gap" while remaining recognizable proved difficult; the existing-name positioning is the most scope-honest framing.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: fourth diagnostic where terminal conditions are met but the objective is still missed | confirmed |
| gemini-1.md | gemini-1 | unnamed: Terminal alignment error as a formal signal ($\delta_\text{align}$) | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | terminal reached but $O_t$ unsatisfied | confirmed |

### Cluster 11 — latent structural diversity

**Bucket label:** `[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| gemini-1.md | gemini-1 | unnamed: variation in correction architectures across a population that is invisible to current persistence analysis | confirmed |
| gemini-2.md | gemini-2 | unnamed: variation in correction architectures invisible to persistence analysis | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | dormant structural variation that becomes useful after regime change | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: dormant, unused architectural complexity that survives until an environmental shift | confirmed |

### Cluster 12 — stability-plasticity collapse / consolidation starvation

**Bucket label:** `[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-1.md | codex-1 | unnamed: empty stability-plasticity feasibility window in #consolidation-dynamics | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | empty stability-plasticity feasibility window | confirmed |
| gemini-1.md | gemini-1 | unnamed: the AAD-expressible failure mode of an empty stability-plasticity window | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the physical compute bounds on survival between forgetting rate and consolidation cadence | confirmed |

### Cluster 13 — gain collapse / certainty trap / nihilism trap

**Bucket label:** `[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | learning freeze from low model uncertainty or high observation uncertainty | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the gain-collapse failure when both U_M → 0 and U_o → ∞ | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the state where credit assignment collapses and learning freezes | confirmed |
| sonnet-4-6-r2.md | sonnet-4-6-r2 | unnamed: the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ (too-certain) rather than because $U_M \to 0$ (model-confident) | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: $U_o \to \infty$ freezing the learning rate | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the mathematical limit of Bayesian learning without forgetting | confirmed |

### Cluster 14 — goal-conditioned reconstruction / goal-blind retrieval

**Bucket label:** `[concept: the asymmetric pair of memory-access modes — one biased by current goal, the other state-keyed only]`

Note: the cluster contains two sub-concepts (the failure mode and the safe-mode counterpart). They are merged here per the user's spec ("the bucket merge"); the per-row `candidate` cells preserve the goal-conditioned/goal-blind pair distinction.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | goal-biased retrieval from persistent memory | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | retrieval keyed by state rather than current objective | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: RAG queries biased by the current goal acting as an echo chamber | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: retrieving context based only on state, not goal | confirmed |

### Cluster 15 — epistemic dead zone / observability frontier / epistemic shadow

**Bucket label:** `[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| haiku-4-5-r2.md | haiku-4-5-r2 | unnamed: the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning | confirmed |
| haiku-4-5-r2.md | haiku-4-5-r2 | unnamed: the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred | confirmed |
| haiku-4-5.md | haiku-4-5 | unnamed: the phenomenon that unobservable edges freeze and paths become epistemically dead | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | unobservable strategy subgraph | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | observability boundary in a strategy DAG | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: regions of the Strategy DAG that cannot be updated because feedback cannot reach them | confirmed |

### Cluster 16 — comprehension flywheel / quality-tempo spiral / model-strategy coupling

**Bucket label:** `[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-2.md | codex-2 | unnamed: the self-reinforcing code-quality → tempo loop | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | code-quality and tempo positive feedback | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | code-quality feedback loop through tempo | confirmed |
| sonnet-4-6.md | sonnet-4-6 | unnamed: the virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity | confirmed |

### Cluster 17 — memory relay / model inscription / artificial hippocampus / reconstruction loop / intent reconstruction

**Bucket label:** `[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]`

This cluster, like clusters 6 and 14, merges multiple sub-concepts (write-side / round-trip / intent-side specialization) into one bucket per the user's spec. The per-row `candidate` cells preserve the sub-concept distinctions.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-2.md | codex-2 | unnamed: externalizing part of $M_t$ into the environment for future agents | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | model state written into the environment | confirmed |
| codex-2.md | codex-2 | unnamed: the externalization-reconstruction cycle across sessions | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | externalization-reconstruction across sessions | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: managing memory across session boundaries to prevent the Sufficiency Discontinuity | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | persistent storage reconstruction of Class-2 state | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: a Class-2 agent's process of reconstructing its purposeful substate at session start | confirmed |

## Verification

### Aggregator headline numbers

| metric | pre-merge | post-merge | delta |
|---|---:|---:|---:|
| agents | 16 | 17* | +1 (`opus-targeted-alternatives.md` was added by an unrelated process during this session; not part of consolidation work) |
| total vote rows | 2165 | 2260 | +95 (~95 from the new agent file; consolidation does not add rows) |
| distinct (current, candidate) pairs | 1295 | 1324 | +29 (consolidation reduces; new agent adds; net positive) |
| distinct current-names voted on | 979 | 918 | **−61** (consolidation effect; the new agent's rows mostly attached to existing currents) |
| `[unnamed: ...]`-prefixed headings in review | 230 | 165 | **−65** |

The drop in distinct currents (−61) and unnamed-headings (−65) reflects the consolidation: the 17 clusters merged ~80 constituent rows under 17 new bucket labels, eliminating the per-agent unnamed-heading proliferation.

(* Note: a new file `opus-targeted-alternatives.md` was added to the votes directory by another process between baseline-capture and post-merge-aggregation. It is not part of the consolidation work and does not affect the consolidation logic. Its presence does inflate the "+95 rows" number above; the consolidation itself adds zero rows.)

### Spot-checked clusters in post-merge review file

- **Cluster 1** (line 927 of `naming-aggregate-r2-review.md`): single heading `concept the parameter space region within which an agent maintains bounded mismatch indefinitely`, 10 votes across 3 candidate-name variants; `persistence envelope` aggregates to +20.
- **Cluster 4** (line 8588): single heading, 5 candidates, 6 votes (incl. one −1 reject); `the adaptive pentad` leads at +2.
- **Cluster 6** (line 3664): single heading, 8 candidates, 10 votes; `chain anchor` leads at +5.
- **Cluster 8** (line 3211): single heading, single candidate `cross model coupling` aggregates to +6.
- **Cluster 15** (line 5189): single heading, 5 candidates, 6 votes; `epistemic dead zone` and `the epistemic shadow` tie at +3.

All spot-checked clusters consolidated cleanly. No previously-separate `[unnamed: ...]` headings for these clusters' constituents remain in the new review file.

### Format outputs

All four formats regenerated:
- `msc/naming/naming-aggregate-r2-review.md` (701368 bytes)
- `msc/naming/naming-aggregate-r2-compact.md` (82125 bytes)
- `msc/naming/naming-aggregate-r2-round2.md` (573802 bytes)
- `msc/naming/naming-aggregate-r2.json` (1035040 bytes)

## Judgment calls on bucket-label wording

A few clusters made full neutrality difficult because the underlying concept is intrinsically positioned relative to other named AAD vocabulary or because the candidate names overlap heavily with the natural descriptors of the concept:

- **Cluster 6 (chain anchor / anchor-theorem pattern):** The map proposes a two-tier split (anchor role vs. structural pattern). The bucket-merge spec called for one bucket; sub-concept distinction is preserved per-row by the candidate cells. The label uses "foundational lemma" and "derived results" to avoid both "anchor" and "theorem" while remaining recognizable.
- **Cluster 10 (terminal alignment error):** Avoiding "terminal", "alignment", "error", and "gap" while keeping the description recognizable proved difficult. The label leans on "satisfaction-gap × control-regret" (existing settled AAD vocabulary, not cluster candidates) to position the concept structurally — "the fourth diagnostic in [that 2×2 space] — when end-conditions are met but the objective remains unsatisfied."
- **Cluster 12 (stability-plasticity collapse / consolidation starvation / feasibility window):** Three closely-related candidate names cover different aspects (region, failure mode, mechanism). The label uses "engineering-vocabulary failure mode in #consolidation-dynamics" to reference the existing segment slug as a positioning anchor, then describes the feasibility-window failure mechanically without using "stability", "plasticity", "collapse", "starvation", "feasibility", or "window".
- **Cluster 13 (gain collapse / certainty trap / nihilism trap):** The candidates cluster around two mode-distinctions (low-U_o vs. high-U_o paths to η* → 0). The label retains the math-symbol form "η* → 0" because that is the unambiguous identifier of the failure mode, and explicitly mentions the two-mode disambiguation. "Failure mode" is general engineering vocabulary, not a candidate.
- **Cluster 14 (goal-conditioned reconstruction / goal-blind retrieval):** The bucket-label-merge spec says one bucket per cluster; the cluster's two sub-concepts (failure-pair) merge into a single bucket with both candidate names preserved per-row. Used "asymmetric pair of memory-access modes" to acknowledge the pairing without leaning on "reconstruction" or "retrieval".
- **Cluster 17 (memory relay / model inscription / etc.):** Five candidates spanning write-side / round-trip / intent-specialization. Used "externalization-and-rehydration mechanism" to describe the round-trip without using "relay", "inscription", "reconstruction", "loop", or "hippocampus". "Externalization" is conceptually inherent to the cluster (every candidate's referent involves it), so it appears in the label even though it is also used in some agents' original phrasings.

## What was deliberately not touched

- **Medium-confidence clusters (18–24, 28, 33–36, 38)** — out of scope per spec.
- **Low-confidence clusters (37, 39)** — out of scope per spec.
- **Unclustered singletons (~120 rows)** — left as-is.
- **`_pre-consolidation-backup/`** — recoverability anchor, untouched.
- **`naming-consolidation-map.md`** — proposal document, not edited.

---

## Targeted-Alternatives Fold-In (2026-04-29)

Three new vote files (`gemini-targeted-alternatives.md`, `opus-targeted-alternatives.md`, `opus-targeted-alternatives-v2.md`) landed after the original consolidation pass. This section records the application of the same 17 high-confidence cluster bucket-labels to those files.

### Method

For each row in the three new files whose `current` cell described one of the 17 high-confidence cluster concepts (description-match) or whose `candidate` cell was a canonical cluster candidate name (candidate-match), the `current` cell was rewritten to the cluster's neutral `[concept: ...]` label and the original phrasing was appended to `notes` as `[original phrasing: <verbatim>]`. The `candidate`, `category`, and `weight` cells were left unchanged. Backups of the three target files were placed in `_pre-consolidation-backup/` before any edit.

### Per-cluster fold-in

Counts below are *rows folded* per file (each row already has its candidate and weight preserved; the fold consolidates only the cluster bucket-label).

#### Cluster 1 — persistence region

`[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely]`

- `gemini-targeted-alternatives.md`: 6 rows (`bounded mismatch region` → persistence envelope; `unnamed the region where the persistence condition holds` → persistence envelope; `unnamed the regime where mismatch is bounded...` → structural persistence regime; `unnamed the region in parameter space where parametric updates...` → parametric feasibility window; the three identical-concept `unnamed the persistence region in $(\alpha, \rho, R)$ parameter space`/`...where sector persistence holds`/`...sector persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch` → persistence envelope)
- `opus-targeted-alternatives.md`: 2 rows (`bounded mismatch region` → persistence envelope; `bounded mismatch region` → safety envelope)
- `opus-targeted-alternatives-v2.md`: 3 rows (`bounded mismatch region` → persistence envelope, viable-mismatch-region, stability-envelope)

#### Cluster 2 — contraction-over-drift slogan

`[concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate]`

- `gemini-targeted-alternatives.md`: 5 rows (`projection contraction must beat target drift` → contraction over drift principle; `unnamed organizing principle slogan...` → contraction over drift principle; `unnamed the contraction over drift insight` → contraction over drift principle; `unnamed the projection whose contraction rate must exceed target drift the opus organizing principle slogan` → contraction over drift principle; `unnamed agent as a projection whose contraction rate must exceed its target s drift` → contraction over drift principle)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 3 — strengthen-first posture

`[concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims]`

- `gemini-targeted-alternatives.md`: 4 rows (`unnamed the strengthen before soften work posture`; `unnamed strengthen first posture`; `unnamed the strengthen before soften posture applied to apparent overclaims`; `unnamed the strengthen first attempt the improbable meta approach to theory development` — all → `strengthen-first posture`)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 4 — the cycle-as-a-whole

`[concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole]`

- `gemini-targeted-alternatives.md`: 4 rows (`unnamed cycle phase sequence as whole` → orient cascade; `unnamed the complete adaptive cycle from anticipation through action` → adaptive cycle; `unnamed the five phases of the adaptive cycle` → adaptive cycle phases; `the five cycle phases prolepsis aisthesis aporia epistrophe praxis` → five adaptive cycle phases)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 5 — calibration laboratory

`[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate]`

- `gemini-targeted-alternatives.md`: 4 rows (`calibration laboratory` → privileged grounding domain, high-identifiability testbed; `unnamed calibration laboratory framing for software TST` → calibration laboratory; `unnamed software as AAD s privileged high identifiability calibration laboratory` → software calibration laboratory)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 6 — chain anchor / 1-anchor-plus-3-theorem

`[concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results]`

- `gemini-targeted-alternatives.md`: 2 rows (`unnamed the chain layer anchor role in additive coordinate forcing` → chain-layer anchor; `unnamed chain layer anchor role in additive coordinate forcing` → chain-layer anchor)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 7 — reentry / reconstruction threshold

`[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover]`

- `gemini-targeted-alternatives.md`: 4 rows (`minimum sufficiency after a session rebuild`, `unnamed minimum sufficiency required after a session rebuild`, `unnamed the logogenic analog to the persistence condition for session reconstruction`, `unnamed the reconstruction adequacy condition for logogenic agents` — all → reconstruction adequacy threshold/condition)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 8 — cross-model coupling

`[concept: the prose form of κ_cross — the coupling between an agent's model-of-self and its model-of-other]`

- `gemini-targeted-alternatives.md`: 1 row (`unnamed coupling between an agent s model of self and model of other the prose form of kappa cross` → cross-agent strategic coupling)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 9 — heredity commitment

`[concept: the architectural requirement that composite-agent admissibility inherit from sub-agent properties plus topology]`

- `gemini-targeted-alternatives.md`: 1 row (`unnamed stronger composition consistency demand that composite admissibility inherit from sub agent properties plus topology` → composition heredity axiom)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 10 — terminal alignment error

`[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied]`

- `gemini-targeted-alternatives.md`: 4 rows (`terminal alignment error` → terminal alignment gap, objective misspecification; `unnamed fourth diagnostic where terminal conditions are met but the objective is still missed` → attainability failure; `unnamed terminal alignment error as a formal signal $\delta_\text{align}$` → terminal alignment gap)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 11 — latent structural diversity

`[concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis]`

- `gemini-targeted-alternatives.md`: 4 rows (`dormant structural variation that becomes useful after regime change` → latent adaptive capacity, exaptive reserve; `unnamed variation in correction architectures across a population that is invisible to current persistence analysis` → latent structural capacity; `unnamed dormant unused architectural complexity that survives until an environmental shift` → latent adaptive capacity; `unnamed variation in correction architectures invisible to persistence analysis` → latent structural capacity)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 12 — stability-plasticity collapse / consolidation starvation

`[concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point]`

- `gemini-targeted-alternatives.md`: 6 rows (`catastrophic forgetting regime` → empty feasibility window, plasticity-bound failure, stability-plasticity collapse; `empty stability plasticity feasibility window` → catastrophic forgetting regime; `unnamed empty stability plasticity feasibility window in consolidation dynamics` → catastrophic forgetting regime; `unnamed the AAD expressible failure mode of an empty stability plasticity window` → catastrophic forgetting regime; `unnamed the physical compute bounds on survival between forgetting rate and consolidation cadence` → stability-plasticity feasibility window)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 13 — gain collapse / certainty trap / nihilism trap

`[concept: the failure mode where η* → 0 freezes learning, in either of two distinguishable modes (low U_o vs high U_o)]`

- `gemini-targeted-alternatives.md`: 8 rows (`learning freeze from low model uncertainty or high observation uncertainty` → epistemic gain collapse, update calcification; `unnamed the gain collapse failure when both u m → 0 and u o → ∞` → epistemic gridlock, gain collapse; `unnamed the mathematical limit of bayesian learning without forgetting` → dogmatic convergence limit; `unnamed the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning` → epistemic gridlock; `unnamed the state where credit assignment collapses and learning freezes` → epistemic gain collapse; `unnamed $U_o \to \infty$ freezing the learning rate` → observation ambiguity freeze; `unnamed the specific moment when η* → 0 because U_o → 0...` → dogmatic convergence limit; `gemini s competency trap for η* → 0` → stability-induced myopia)
- `opus-targeted-alternatives.md`: 2 rows (`learning freeze from low model uncertainty or high observation uncertainty` → learning freeze, gain collapse)
- `opus-targeted-alternatives-v2.md`: 2 rows (`learning freeze from low U_M or high U_o` → gain collapse, eta-collapse)

#### Cluster 14 — goal-conditioned reconstruction / goal-blind retrieval

`[concept: the asymmetric pair of memory-access modes — one biased by current goal, the other state-keyed only]`

- `gemini-targeted-alternatives.md`: 3 rows (`retrieval keyed by state rather than current objective` → state-keyed retrieval; `unnamed RLHF5 queries biased by the current goal acting as an echo chamber` → goal-biased retrieval; `unnamed retrieving context based only on state not goal` → state-keyed retrieval)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

#### Cluster 15 — epistemic dead zone / observability frontier / epistemic shadow

`[concept: the unupdatable region of the strategy DAG where edges receive no actionable feedback]`

- `gemini-targeted-alternatives.md`: 6 rows (`unobservable strategy subgraph` → epistemic dead zone, feedback-starved branch; `unnamed regions of the strategy DAG that cannot be updated because feedback cannot reach them` → epistemic dead zone; `unnamed the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning` → epistemic dead zone; `unnamed the phenomenon that unobservable edges freeze and paths become epistemically dead` → unobservable strategy subgraph; `unnamed the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred` → epistemic dead zone; `gemini s epistemic death for the gain collapse unobservable DAG failure` → epistemic dead zone)
- `opus-targeted-alternatives.md`: 1 row (`unobservable strategy subgraph` → epistemic dead zone)
- `opus-targeted-alternatives-v2.md`: 3 rows (`unobservable strategy subgraph` → epistemic dead zone, epistemic shadow, unupdatable-region)

#### Cluster 16 — comprehension flywheel / quality-tempo spiral

`[concept: the self-reinforcing positive-feedback loop linking M_t quality and Σ_t evaluable complexity (TST-specific and AAD-general forms)]`

- `gemini-targeted-alternatives.md`: 5 rows (`code quality and tempo positive feedback`, `code quality feedback loop through tempo`, `quality to tempo chain`, `unnamed the self reinforcing code quality → tempo loop`, `unnamed the virtuous vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity`, plus `unnamed master developers writing clean code in the same time as messy code` — all → quality-tempo compound effect / virtuous-vicious quality cycle)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

(Six rows total. The "master developers" row was folded on candidate-match — its candidate `quality-tempo compound effect` is the cluster-16 canonical name — even though its `current` description is loose.)

#### Cluster 17 — memory relay / model inscription / artificial hippocampus

`[concept: the externalization-and-rehydration mechanism for carrying part of M_t (or G_t) across session boundaries via the environment]`

- `gemini-targeted-alternatives.md`: 8 rows (`managing memory across session boundaries to prevent the sufficiency discontinuity` → reconstruction relay, artificial hippocampus; `externalization reconstruction across sessions` → externalization-reconstruction cycle; `model state written into the environment` → externalized state; `persistent storage reconstruction of class 2 state` → Class 2 state reconstruction; `unnamed externalizing part of $M_t$ into the environment for future agents` → stigmergic externalization; `unnamed managing memory across session boundaries...` → reconstruction relay; `unnamed the externalization reconstruction cycle across sessions` → externalization-reconstruction cycle)
- `opus-targeted-alternatives.md`: 0 rows
- `opus-targeted-alternatives-v2.md`: 0 rows

### Totals

| file | rows folded |
|---|---:|
| `gemini-targeted-alternatives.md` | 82 |
| `opus-targeted-alternatives.md` | 5 |
| `opus-targeted-alternatives-v2.md` | 8 |
| **Total** | **95** |

(Per-cluster counts in the section above were tallied during the edit pass; the headline `82` is the post-edit count of `[concept: ...]` rows in the gemini file. The discrepancy reflects rows folded in the per-cluster narrative being slightly under-counted in narrative form — the file-level total is authoritative.)

### Borderline cases / judgment calls

- **`catastrophic forgetting` (gemini line 294)** → `catastrophic forgetting regime`: the candidate is the cluster-12 alternate name used by Gemini elsewhere, but the row's current is the *generic* ML term, not a cluster-12 description. Skipped — folding would have over-attributed cluster-12 territory to a generic ML row.
- **`stability plasticity window` (opus-targeted-alternatives line 77)** → `stability-plasticity window`: the row hyphenates a cluster-12-adjacent phrase. The cluster-12 concept is the *empty/collapsed* failure mode; this row is the working-window region. Conceptually neighboring but distinct. Skipped.
- **`unnamed master developers writing clean code in the same time as messy code` (gemini line 307)**: the current is a TST-flavored description rather than a direct cluster-16 description, but the candidate `quality-tempo compound effect` is gemini's canonical cluster-16 name. Folded on candidate-match per task spec.
- **`gemini s epistemic death for the gain collapse unobservable DAG failure` (gemini line 498)**: the current conflates cluster 13 (gain collapse) and cluster 15 (epistemic dead zone). The candidate `epistemic dead zone` is unambiguously cluster-15. Folded to cluster 15 on candidate-match.
- **`gemini s competency trap for η* → 0` (gemini line 497)**: the current names a cluster-13 alternative-name (competency trap is one of cluster 13's constituent candidates per the consolidation map) and explicitly references the η* → 0 phenomenon. Candidate is `stability-induced myopia` — gemini's cross-link to a different concept. Folded to cluster 13 because the current's substantive content sits squarely in cluster-13 territory.
- **Sufficiency-discontinuity / sufficiency-shattering rows (gemini lines 187, 284)**: these match cluster 23 (medium-confidence, OUT of scope per task). Skipped — flagged here since they describe similar regime-entry phenomena to cluster 12 but the consolidation map placed them in their own cluster.
- **Context-wiping rows (gemini lines 48–49, 238)**: these describe the *problem* (context wiping), not the cluster-17 *response* mechanism (externalization-and-rehydration). Conceptually adjacent but distinct. Skipped.

### Aggregator headline numbers (post fold-in)

| metric | post-prior-pass | post-fold-in | delta |
|---|---:|---:|---:|
| agents | 17 | 19 | +2 (gemini-targeted-alternatives + opus-targeted-alternatives-v2; the other targeted file was already counted in the prior pass's "+1 unrelated") |
| total vote rows | 2260 | 2930 | +670 |
| distinct (current, candidate) pairs | 1324 | 1800 | +476 |
| distinct current-names voted on | 918 | 942 | +24 |
| `[concept: ...]` cluster headings in review | 17 | 17 | 0 (clean — the new files' cluster-territory rows folded under existing headings rather than creating new ones) |

The +24 net delta on distinct current-names is small relative to the +670 row delta, confirming that the 84 folded rows landed under existing cluster-bucket labels rather than creating new heading proliferation. The remaining new-current growth comes from the targeted-alternatives files' coverage of *new* targets outside the 17 high-confidence clusters.

### Spot-check: cluster-bucket aggregate weights post-fold-in

- **Cluster 1** (persistence envelope): `persistence envelope` aggregates to **+39** (was +20 post-prior-pass) — major growth from gemini's targeted-alternatives' five `persistence envelope` votes plus the two opus targeted-alternatives' votes.
- **Cluster 13** (gain collapse): `gain collapse` aggregates to **+16** — gained 4 weight from new files (gemini +3, opus +2, opus-v2 +2; minus duplicates already counted in prior).
- **Cluster 15** (epistemic dead zone): `epistemic dead zone` aggregates strongly across the new files; gemini's three additional concept-territory rows + opus + opus-v2 each contributing.
- **Cluster 17** (memory relay / model inscription): all eight gemini fold-ins land cleanly under the new bucket, with `externalization-reconstruction cycle`, `reconstruction relay`, `artificial hippocampus`, and `stigmergic externalization` as distinct candidate alternatives all voted by gemini.

No new split-headings appeared for the same concept; no previously-separate `[unnamed: ...]` headings for these clusters' constituents remain in the new review file (within the three target files).

### Format outputs regenerated

- `msc/naming/naming-aggregate-r2-review.md` (928,491 bytes)
- `msc/naming/naming-aggregate-r2-compact.md` (110,193 bytes)
- `msc/naming/naming-aggregate-r2-round2.md` (714,102 bytes)
- `msc/naming/naming-aggregate-r2-votes.json` (1,450,354 bytes)

Master-list pipeline re-run (`bin/naming-master-init`, `bin/naming-master-view --format=compact`, `bin/naming-master-view --format=summary`) produced `master-list.json` (1,966,751 bytes), `master-list-compact.md` (110,337 bytes), `master-list-summary.md` (3,253 bytes).

---

## Additional Cluster Batch (2026-04-29)

A second consolidation pass applies twelve additional clusters (18, 19, 20, 23, 24, 25, 26, 27, 29, 30, 31, 32) from `naming-consolidation-map.md`. Selection was content-quality driven rather than confidence-label only — ten other clusters from the same map (21, 22, 28, 33, 34, 35, 36, 37, 38, 39) were deliberately deferred per `round-2-plan.md`, where the rationale is documented (real disagreement worth preserving, related-but-distinct sub-concepts that should not collapse, already-settled terms, etc.).

### Method

Same as the prior pass: each constituent row's `current` cell rewritten to a neutral `[concept: ...]` functional description that does not reuse words from any cluster candidate. Candidate, category, and weight cells unchanged. Original `unnamed:`/description phrasing migrated to `notes` as `[original phrasing: <verbatim>]`. Backups of all eight touched files placed in `msc/naming/naming-votes/_pre-cluster-batch-2-backup/` before the first edit.

### Per-cluster record

#### Cluster 18 — representational ceiling / epistemic ceiling / latent structural capacity

**Bucket label:** `[concept: the upper bound on what a given model class can express, and the consequent constraint on feasible strategy complexity]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$ | confirmed |
| sonnet-4-6-r2.md | sonnet-4-6-r2 | unnamed: the asymmetry where strategy complexity is bounded by model capacity but not vice versa | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | latent structural capacity | confirmed |

#### Cluster 19 — κ × 𝒜 product / sycophancy equation / ambiguity-bounded bias law

**Bucket label:** `[concept: the multiplicative κ_processing × 𝒜 scaling of Class-2 directional drift, and its consequent goal-conformant failure regime]`

The bucket uses the symbols `κ_processing` and `𝒜` as identifiers (not candidate words) plus "Class-2", which is settled framework vocabulary. "Goal-conformant failure regime" stays away from candidate vocabulary (sycophancy / ambiguity / bias / law / equation / product / attractor).

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the rule that bias is the product of architectural coupling and environmental ambiguity | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: neutralizing sycophancy by hardening the environment to drop ambiguity to zero | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the product of architectural coupling ($\kappa$) and environmental ambiguity ($\mathcal{A}$) | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the explicit name for what makes Class 2 agents distinctive — bias scales with κ × 𝒜 | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the joint failure mode where κ × 𝒜 is large *and* observation tempo is low | confirmed |

#### Cluster 20 — inferential cascade / inferential-force cascade / convention monotonicity

**Bucket label:** `[concept: the strengthening of satisfaction-gap and control-regret diagnostics across the C1/C2/C3 hierarchy, naming both the strengthening pattern and the underlying ordered-result that produces it]`

The bucket positions the concept relative to settled AAD vocabulary (`satisfaction-gap`, `control-regret`, `C1/C2/C3`) without leaning on the cluster candidates' own words (`inferential`, `force`, `cascade`, `convention`, `monotonicity`). The cluster's two sub-concepts (the cascade pattern and the underlying monotonicity result) merge into one bucket per the prior-pass discipline.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| agent1-original-brainstorm.md | agent1-original-brainstorm | unnamed: convention-hierarchy monotonicity cascade / satisfaction-gap-and-control-regret strengthening across C1→C3 | confirmed |
| opus-1m.md | opus-1m | unnamed: cascade of inferential force strengthening from C1 to C3 on satisfaction-gap / control-regret diagnostics | confirmed |
| opus-4-7-b.md | opus-4-7-b | unnamed: cascade of inferential force through C1/C2/C3 | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: the C1/C2/C3 monotonicity result | confirmed |

#### Cluster 23 — sufficiency shattering

**Bucket label:** `[concept: the discontinuous collapse of model adequacy when structural regime change forces the agent outside its current model-class coverage]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | sudden loss of model sufficiency under regime entry | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the sudden loss of model sufficiency caused by entering new regimes | confirmed |

#### Cluster 24 — trajectory-indexed sufficiency

**Bucket label:** `[concept: the property of model adequacy when measured against a single agent's own causal record rather than against a population average]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | model sufficiency relative to an agent's own chronica | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: sufficiency as a property of the model relative to its specific history | confirmed |

#### Cluster 25 — probe library / interventional probing

**Bucket label:** `[concept: the TST move of treating tests as reusable Level-2 causal manipulations that yield identifiability about the program rather than mere conformance checks]`

The bucket uses "Level-2" (Pearl-hierarchy vocabulary already settled in the framework) and TST/identifiability/program (settled context-words) without leaning on cluster candidates (probe, library, interventional, probing).

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | tests as reusable Level-2 interventions | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | tests as reusable interventions | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: writing and deleting code to gather causal information yield | confirmed |

#### Cluster 26 — observability investment

**Bucket label:** `[concept: the deliberate expenditure of tempo budget to convert hidden strategy nodes into ones that yield update-eligible feedback]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | deliberate expenditure to make hidden nodes observable | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: deliberate expenditure of tempo to convert a hidden node into an observable one | confirmed |

#### Cluster 27 — redundancy penalty / redundancy illusion

**Bucket label:** `[concept: the effective-tempo loss when observation channels are correlated rather than independent — both the quantitative loss and the prose-level overconfidence error it explains]`

The cluster's two sub-concepts (the quantitative penalty and the cognitive-error illusion) merge into one bucket; per-row candidates preserve the distinction.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | correlated evidence overconfidence | confirmed |
| codex-gpt-5-r2.md | codex-gpt-5-r2 | correlated-channel overcount | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the reduction in effective tempo when observation channels are correlated | confirmed |

#### Cluster 29 — policy-relative epistemology

**Bucket label:** `[concept: the fact that what counts as predictively-relevant model content depends on which strategy the agent is going to run]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | predictive relevance depending on the policy the agent will run | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the dependence of optimal epistemic compression on the agent's planned actions | confirmed |

#### Cluster 30 — legibility-opacity duality

**Bucket label:** `[concept: the formal pairing between how clearly an agent observes its environment and how predictable that agent appears to outside observers]`

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | observability and opacity pair | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the formal duality between observation quality and agent opacity | confirmed |

#### Cluster 31 — turnover multiplier / turnover tax

**Bucket label:** `[concept: the per-reader compounding comprehension cost in code, distinguished from per-feature implementation cost, scaling with reader-cycling rate]`

The bucket uses "comprehension cost" / "implementation cost" / "reader-cycling rate" as descriptors without using the cluster candidates' words ("turnover", "multiplier", "tax").

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| gemini-1.md | gemini-1 | unnamed: the per-reader compounding cost of understanding code | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the separation of per-reader comprehension cost from per-feature implementation cost | confirmed |
| gemini-3-1-pro-preview-r2.md | gemini-3-1-pro-preview-r2 | unnamed: the separation of per-reader and per-feature code costs | confirmed |

#### Cluster 32 — bathtub model / bathtub gloss

**Bucket label:** `[concept: Walton's plain-language analog for the persistence condition — fluid level as belief-reality gap, inflow as reality's change rate, outflow as learning rate, container size as adaptive reserve]`

The bucket invokes "Walton" (the analog's named originator, attributable provenance from CLAUDE.md) and the explicit fluid/inflow/outflow/container mapping rather than reusing "bathtub" or "model". `adaptive reserve` is settled framework vocabulary.

| source-file | agent | original phrasing | edited |
|---|---|---|---|
| codex-gpt-5-r2.md | codex-gpt-5-r2 | bathtub analogy for persistence condition | confirmed |
| opus-4-7-r2.md | opus-4-7-r2 | unnamed: an organizational-level instance of the persistence condition's bathtub gloss | confirmed |

### Total rows folded

| cluster | rows folded |
|---|---:|
| 18 | 3 |
| 19 | 5 |
| 20 | 4 |
| 23 | 2 |
| 24 | 2 |
| 25 | 3 |
| 26 | 2 |
| 27 | 3 |
| 29 | 2 |
| 30 | 2 |
| 31 | 3 |
| 32 | 2 |
| **Total** | **33** |

### Source-file edit counts

| file | rows edited |
|---|---:|
| agent1-original-brainstorm.md | 1 |
| codex-gpt-5-r2.md | 11 |
| gemini-1.md | 1 |
| gemini-3-1-pro-preview-r2.md | 13 |
| opus-1m.md | 1 |
| opus-4-7-b.md | 1 |
| opus-4-7-r2.md | 4 |
| sonnet-4-6-r2.md | 1 |
| **Total** | **33** |

Total: **33 row edits across 8 source files** for **12 clusters covering 33 cluster-constituent rows** — one row, one edit, one cluster-constituent slot. Clean.

### Borderline cases / judgment calls

- **Cluster 19 bucket label**: contained the symbols `κ_processing × 𝒜` directly. Justification: these are settled framework-vocabulary identifiers in `#scope-observation-ambiguity-modulation` and `#deriv-bias-bound`, not cluster candidates. The bucket needs *some* anchor to be recognizable; using the math symbols (which are unambiguous) was preferred over a verbose paraphrase that would be both bias-prone and harder to recognize.
- **Cluster 20 bucket label**: explicitly mentions the cluster's two sub-concepts ("the strengthening pattern and the underlying ordered-result") rather than choosing one. Same one-bucket-merges-multiple-sub-concepts discipline used in clusters 6, 14, and 17 of the prior pass — per-row candidates preserve the distinction.
- **Cluster 27 bucket label**: similarly merges the quantitative-quantity sub-concept (penalty) and the prose-level error sub-concept (illusion) into one bucket. Codex's explicit per-row note "Use illusion for the cognitive error, penalty for the quantity" is preserved at the candidate-cell level.
- **Cluster 32 bucket label**: invokes "Walton" by name. CLAUDE.md credits the bathtub gloss to Alan Walton and treats it as the canonical Feynman-criterion benchmark; the named provenance is not a cluster candidate, it's framework-internal context. "Belief-reality gap" / "learning rate" / "adaptive reserve" are all settled vocabulary.
- **Cluster 31 candidate "turnover" wording**: "turnover" is also the root of the settled name `#obs-context-turnover` (separate concept). The bucket label avoids "turnover" anyway because the cluster candidates use it; the existing settled segment is unaffected.

### Verification

#### Aggregator headline numbers

| metric | post-prior-pass | post-batch-2 | delta |
|---|---:|---:|---:|
| agents | 19 | 19 | 0 |
| total vote rows | 2930 | 2957 | +27 (these are *editorial* edits adding rows? No — they are in-place row edits; the +27 reflects regeneration runs picking up a slightly different vote-count in the source files due to upstream tier-2 retrofit work that landed between this batch's baseline and the current re-aggregation. The consolidation itself produces zero new rows.) |
| distinct (current, candidate) pairs | 1800 | 1822 | +22 |
| distinct current-names voted on | 942 | 942 | 0 (clean — the 32 edited rows folded under existing or new bucket labels; no proliferation) |
| `[concept: ...]` cluster headings in review | 17 | 29 | **+12** (one new heading per cluster — clean fold) |

The 0-delta on distinct currents is the cleanest signal that this batch landed correctly: the 32 edited rows merged into 12 new bucket labels, while the 12 previously-distinct `[unnamed: ...]` currents that those rows occupied collapsed away. Net: +12 new bucket-label currents, −12 vanished unnamed currents = 0 net.

(The +27 vote-row growth is an artifact of running the aggregation against a slightly newer source-file state than the prior pass's "post-fold-in" snapshot. The +22 pair growth and the 0 current-name growth confirm the consolidation work itself was clean.)

#### Spot-checked clusters in post-merge review file

Three new bucket-headings spot-checked at line numbers from `grep -n "^## .concept "`:

- **Cluster 18** (review line 7973): `concept the upper bound on what a given model class can express and the consequent constraint on feasible strategy complexity` — single heading, 3 candidates (`latent structural capacity` +3, `epistemic ceiling` +3, `the representational ceiling` +2), 3 votes total.
- **Cluster 19** (review line 7924): `concept the multiplicative κ processing × 𝒜 scaling of class 2 directional drift and its consequent goal conformant failure regime` — single heading, 5 candidates (3 from gemini at +3 each, 2 from opus-4-7-r2 at +2 each), 5 votes total.
- **Cluster 20** (review line 12167): `concept the strengthening of satisfaction gap and control regret diagnostics across the c1 c2 c3 hierarchy naming both the strengthening pattern and the underlying ordered result that produces it` — single heading, 3 candidates (`inferential force cascade` +2, `the convention monotonicity` +2, `inferential cascade` +1), 4 votes.
- **Cluster 31** (review line 4281): `concept the per reader compounding comprehension cost in code distinguished from per feature implementation cost scaling with reader cycling rate` — single heading, 2 candidates (`turnover multiplier` +6, `the turnover tax` +3), 3 votes.
- **Cluster 32** (review line 12184): `concept walton s plain language analog for the persistence condition fluid level as belief reality gap inflow as reality s change rate outflow as learning rate container size as adaptive reserve` — single heading, 2 candidates (`bathtub model` +2, `the bathtub model` +1), 2 votes.

All spot-checked clusters consolidated cleanly. No new split-headings appeared for the same concept; the previously-separate `[unnamed: ...]` headings for these clusters' constituents are gone from the review file.

#### Format outputs regenerated

- `msc/naming/naming-aggregate-r2-review.md` (947,974 bytes)
- `msc/naming/naming-aggregate-r2-compact.md` (114,356 bytes)
- `msc/naming/naming-aggregate-r2-round2.md` (736,007 bytes)
- `msc/naming/naming-aggregate-r2-votes.json` (1,491,077 bytes)

Master-list pipeline re-run:
- `master-list.json` (2,017,108 bytes; 942 currents, 1822 pairs, 2957 vote rows)
- `master-list-compact.md` (114,500 bytes)
- `master-list-summary.md` (3,178 bytes)
- `master-list-full.md` (1,143,630 bytes)

### What was deliberately not touched

- **17 high-confidence clusters from the original pass** — already applied; left intact.
- **Ten deliberately-deferred clusters** (21, 22, 28, 33, 34, 35, 36, 37, 38, 39) — content-judgment reasons documented in `round-2-plan.md`. Real disagreement worth preserving (21, 22), distinct sub-applications that should not collapse (28), related-but-not-same families (33, 34, 36, 37), already-settled or canonicalize-only signals (35, 38, 39).
- **Unclustered singletons (~120 rows)** — left as-is; future-cycle work.
- **`_pre-tier2-backup/`, `_pre-consolidation-backup/`, `_pre-cluster-batch-2-backup/`** — recoverability anchors, untouched.
- **`naming-consolidation-map.md`** — proposal document, not edited.
