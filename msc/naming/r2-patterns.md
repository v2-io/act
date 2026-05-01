# R2 Patterns — Cross-Cutting Voting Observations

**Generated:** 2026-05-01T01:43:29Z
**Source:** R2 voting cohort (6 voters: codex-r2b, gemini-r2, opus-r2b, opus-r2c, sonnet-r2b, sonnet-r2c)
**Targets analyzed:** 106 multi-R2-voter targets (filtered from 629 total)

For an agent reading after framework ingestion to produce first-pass canonicalize / rename decisions. This doc surfaces patterns target-by-target reading would miss, and provides methodological keys to interpret the score-card numbers.

See also: [`r2-aggregate-table.md`](r2-aggregate-table.md) (score-card, sorted by max(score/n)), [`r2-aggregate-detail.md`](r2-aggregate-detail.md) (full per-target vote breakdown), [`naming-principles.md`](../../doc/naming-principles.md) (vote categories and criteria), [`naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) (round design and engagement protocol).

---

## 1. What the score-card numbers mean

### Score formula

Each per-vote substance is `weight × factor`, where:

```
effort = min(1, note_chars / bullet_chars)        # length is meaningful only relative to bullet
novelty = 1 - jaccard(note_tokens, bullet_tokens)  # token-overlap-based; see caveats
factor = (0.7 + 0.3 × effort) × (1.0 + novelty)
factor *= 1.2 if vote.top_pick                     # acts as tiebreaker for multi-+2 cases
factor *= 1.2 if vote.category == canonicalize     # excavated-from-prose evidence
```

Properties: empty note → 0 (nullify); fragment relative to bullet → 0.7 (small penalty); bandwagon (full effort, no novelty) → 1.0 (vote at face value); thoughtful (full effort, novel) → 2.0 (full amplification); thoughtful + top-pick + canonicalize → 2.88 (max). Write-ins land at 2.0 by construction (no bullet to compare against).

`score` = sum of substance across all voters per candidate (R1 synth counts as one voter; R2 voters add per-card)
`score/n` = score / total voters who weighed in on **any** candidate in the target (other candidates in target are implicit zeros — useful for cross-target comparison)

### Marker semantics

| marker | meaning | implication |
|---|---|---|
| **bold row** | leader (highest score within target) | aggregator's recommended landing |
| ▸ | candidate is the current corpus name (`is_keep`) | leader = ▸ → defended keep; leader ≠ ▸ → rename signal |
| ⊕ | at least one vote (R1 or R2) was add-alias category | downstream action: keep current AND add this — not rename |
| ★ | top-pick count among R2 voters | in this corpus mostly co-occurs with +2 (95%); tiebreaker when voter has multiple +2s |

### What's filtered

- **Uncontested keeps** (1 master candidate that's `is_keep`, no write-ins) excluded by default. These are decisions that need no decisions: nobody proposed an alternative at any phase. Verified across all R1 work for `action fluency`, `action selection`, `adaptive system`, etc. Override with `--include-uncontested-keeps`.
- **Single-R2-voter targets** excluded by default (`--min-r2-voters=2`). Single-voter targets exist as data but were filtered for first-pass aggregation scope.
- **No-vote targets** (zero R1 evidence + zero R2 votes) always excluded; safety net.

---

## 2. Categorical groupings

Targets bucketed by leader-relative-to-current-name and by consensus shape. Ordered by leader-score/n descending within each bucket.

### 2a. Strongest defended keeps — leader is current name (▸), no add-alias votes (51)

*The current name is the leader; voters explicitly endorsed keeping it. First-pass action: **no change**, but verify the segment's prose still supports the name (the score reflects voter consensus, not segment-naming-drift).*

| target | leader | score | score/n | n-votes |
|---|---|--:|--:|--:|
| `composition consistency` | `composition consistency` | 16.2 | **4.04** | 4 |
| `aporia` | `aporia` | 15.9 | **3.97** | 4 |
| `temporal software theory` | `temporal software theory` | 11.7 | **3.91** | 3 |
| `credit assignment boundary` | `credit assignment boundary` | 11.7 | **3.89** | 3 |
| `model sufficiency` | `model sufficiency` | 15.5 | **3.87** | 4 |
| `adversarial tempo advantage` | `adversarial tempo advantage` | 11.5 | **3.84** | 3 |
| `complete agent state` | `complete agent state` | 15.1 | **3.79** | 4 |
| `objective functional` | `objective functional` | 15.0 | **3.75** | 4 |
| `directional fidelity` | `directional fidelity` | 11.2 | **3.74** | 3 |
| `model-class fitness` | `model-class fitness` | 14.3 | **3.58** | 4 |
| `correlation hierarchy` | `correlation hierarchy` | 14.3 | **3.58** | 4 |
| `deliberation cost` | `deliberation cost` | 10.7 | **3.58** | 3 |
| `persistence condition` | `persistence condition` | 14.3 | **3.57** | 4 |
| `sector condition` | `sector condition` | 10.6 | **3.53** | 3 |
| `adaptive cycle` | `adaptive cycle` | 14.0 | **3.51** | 4 |
| `exact / robust-qualitative / heuristic / conditional (claim tier)` | `exact / robust-qualitative / heuristic / conditional (clai…` | 10.5 | **3.50** | 3 |
| `prolepsis` | `prolepsis` | 10.4 | **3.46** | 3 |
| `mismatch dynamics` | `mismatch dynamics` | 10.3 | **3.43** | 3 |
| `Pearl causal hierarchy` | `Pearl causal hierarchy` | 20.5 | **3.42** | 6 |
| `continuity persistence` | `continuity persistence` | 17.0 | **3.41** | 5 |

*Showing top 20 of 51. Full list via score-card sorted by score/n.*

### 2b. Strongest rename signals — leader ≠ current name, not an add-alias (25)

*The leader proposes replacing the current name. First-pass action candidates: **rename** (slug + prose) if confidence is high. Read the detail view for context — sometimes the leader is a write-in single-voter case (interpret cautiously).*

| target | proposed leader | score | score/n | n-votes |
|---|---|--:|--:|--:|
| `ASF (acronym)` | `ASF` | 19.3 | **3.86** | 5 |
| `agent model` | `Reality model` | 18.9 | **3.78** | 5 |
| `chronica capitalized vs lowercase` | `Chronica lowercase in running prose` | 14.8 | **3.71** | 4 |
| `postulate not axiom` | `Postulate` | 10.8 | **3.60** | 3 |
| `derivation not proof` | `Derivation` | 14.3 | **3.56** | 4 |
| `AAD (acronym)` | `AAD` | 14.2 | **3.56** | 4 |
| `$H_b$` | `Agent opacity $H_b$` | 10.5 | **3.50** | 3 |
| `$\mathcal C_t$ chronica` | `$\mathcal C_t$` | 13.5 | **3.37** | 4 |
| `formulation / definition / result / ... (segment types)` | `Formulation definition result etc segment type` | 9.9 | **3.31** | 3 |
| `separability pattern` | `Separability ladder` | 12.5 | **3.13** | 4 |
| [Concept] _agentic system framework ASF top level_ | `Agentic system framework` | 12.2 | **3.05** | 4 |
| [Concept] _agent classes (Class 1 / 2 / 3)_ | `Architectural classes` | 11.7 | **2.92** | 4 |
| [Concept] _unnamed the 2×2 table of satisfaction gap vs control regret × goal a…_ | `The 2×2 diagnostic` | 8.7 | **2.91** | 3 |
| `strategy dimension` | `Purposeful decomposition` | 11.6 | **2.90** | 4 |
| `recursive update` | `Recursive update by completeness` | 7.1 | **2.37** | 3 |
| `the Greek vocabulary` | `The greek philosophical vocabulary` | 6.9 | **2.31** | 3 |
| `convention hierarchy` | `Continuation hierarchy` | 11.5 | **2.31** | 5 |
| `Section I. Adaptive Systems Under Uncertainty` | `I adaptive system under uncertainty` | 6.7 | **2.23** | 3 |
| [Concept] _unnamed the pearl-blanket reading of directed separation_ | `Pearl-blanket form` | 6.6 | **2.21** | 3 |
| `per dimension persistence` | `Weakest link persistence` | 6.5 | **2.18** | 3 |
| `agent environment` | `Agent environment boundary` | 10.2 | **2.04** | 5 |
| [Concept] _unnamed superlinear scaling of adversarial tempo advantage_ | `Superlinear tempo advantage` | 5.7 | **1.90** | 3 |
| `Class 1 agent` | `Modular agent` | 5.6 | **1.86** | 3 |
| `value object` | `Policy-conditioned value` | 5.3 | **1.76** | 3 |
| `Class 2 agent` | `Integrated agent` | 3.6 | **1.21** | 3 |


### 2c. Add-alias landings — at least one ⊕ vote on the leader (30)

*The leader has add-alias votes — the proposed action is "keep the current name AND add this as a parallel handle," not "replace." First-pass action: **add the alias** in NOTATION/LEXICON; do not rename. Per `naming-principles.md`: most common case is symbol + English alias.*

| target | proposed alias / leader | leader = current? | score | score/n |
|---|---|---|--:|--:|
| `$G_t = (O_t, \Sigma_t)$` | `Purposeful substate` | — | 11.3 | **3.77** |
| `calibration laboratory` | `calibration laboratory` | ▸ | 15.0 | **3.74** |
| `$\iota_{ij}$` | `Identifiability coefficient` | — | 11.2 | **3.73** |
| `satisfaction gap` | `satisfaction gap` | ▸ | 21.0 | **3.51** |
| [Concept] _symbol default m t in prose_ | `Model state` | — | 13.6 | **3.40** |
| `$U_M$` | `Epistemic unity` | — | 10.0 | **3.32** |
| `control regret` | `control regret` | ▸ | 19.9 | **3.32** |
| [Concept] _structural persistence operational persistence continuity persistence_ | `Persistence taxonomy` | — | 16.6 | **3.32** |
| `$\alpha$ (sector-condition lower bound)` | `Correction rate constant` | — | 13.2 | **3.30** |
| `update gain` | `update gain` | ▸ | 13.2 | **3.29** |
| `$U_M$ / $U_O$ / $U_\Sigma$ unity dimensions` | `Epistemic unity teleological unity strategic unity` | — | 9.6 | **3.19** |
| `effect spiral` | `Runaway mismatch cascade` | — | 9.4 | **3.12** |
| `$\phi$` | `History compression` | — | 12.1 | **3.02** |
| `observation function` | `Observation channel` | — | 12.0 | **2.99** |
| `evidence starvation` | `evidence starvation` | ▸ | 9.0 | **2.99** |
| `$R$ (sector-condition radius)` | `Model-class capacity` | — | 8.9 | **2.95** |
| `$f_M$ (event-driven update)` | `Epistemic update function` | — | 8.1 | **2.69** |
| `$M_t$` | `Model state or epistemic substate` | — | 10.1 | **2.52** |
| `Class 2` | `Merged` | — | 9.3 | **2.32** |
| `$\delta_t$` | `Aporia signal` | — | 6.9 | **2.31** |
| `strategic calibration` | `strategic calibration` | ▸ | 6.8 | **2.27** |
| `Pearl L1` | `Predicting` | — | 6.2 | **2.08** |
| `$M_t$ (reality model)` | `Working model` | — | 5.9 | **1.97** |
| `$\mathcal{C}_t$ (chronica)` | `Chronica or interaction history` | — | 7.8 | **1.96** |
| `Class 1` | `Modular` | — | 5.2 | **1.73** |

*Showing top 25 of 30.*

### 2d. Contested decisions — runner-up within 30% of leader (20)

*Two or more candidates have comparable scores. First-pass action: **read detail view, defer or reject.** These often indicate genuine framework-level ambiguity worth surfacing as a finding rather than a landing.*

| target | leader | leader score | runner-up | runner-up score |
|---|---|--:|---|--:|
| `logogenic logozoetic` | `logogenic logozoetic` | 13.5 | `Logogenic logozoetic distinction` | 9.6 |
| [Concept] _structural persistence operational persistence continuity persistence_ | `Persistence taxonomy` | 16.6 | `Structural operational continuity persistence` | 13.2 |
| `effect spiral` | `Runaway mismatch cascade` | 9.4 | `effect spiral` | 8.8 |
| `AAD (Adaptation and Actuation Dynamics)` | `AAD (Adaptation and Actuation Dynamics)` | 15.0 | `AAD` | 12.3 |
| `temporal nesting` | `temporal nesting` | 10.7 | `Timescale nesting` | 7.7 |
| `epistemic architecture` | `epistemic architecture` | 7.9 | `AAD meta architecture` | 5.8 |
| `edge update causal validity` | `edge update causal validity` | 7.7 | `Identification regime` | 6.1 |
| `loop interventional access` | `loop interventional access` | 7.4 | `Loop causal engine` | 5.4 |
| `recursive update` | `Recursive update by completeness` | 7.1 | `recursive update` | 6.9 |
| `$\delta_t$` | `Aporia signal` | 6.9 | `Mismatch signal` | 5.0 |
| `strategic calibration` | `strategic calibration` | 6.8 | `Strategic calibration residual` | 5.4 |
| `Section I. Adaptive Systems Under Uncertainty` | `I adaptive system under uncertainty` | 6.7 | `Adaptive Systems Under Uncertainty` | 4.8 |
| `agent environment` | `Agent environment boundary` | 10.2 | `agent environment` | 9.1 |
| `$M_t$ (reality model)` | `Working model` | 5.9 | `Reality model` | 4.8 |
| `$\mathcal{C}_t$ (chronica)` | `Chronica or interaction history` | 7.8 | `chronica (complete interaction history)` | 5.8 |
| `Class 1 agent` | `Modular agent` | 5.6 | `Class 1` | 4.8 |
| `value object` | `Policy-conditioned value` | 5.3 | `value object` | 3.7 |
| `Class 1` | `Modular` | 5.2 | `Class 1` | 4.9 |
| `Class 3` | `Partially coupled` | 6.8 | `Class 3` | 4.8 |
| `Pearl L2` | `Intervening` | 4.8 | `Exploring` | 4.2 |


---

## 3. Cross-cutting patterns

### 3a. Greek / etymological vocabulary cluster (11)

*Per the principles file, the framework deliberately uses a coherent Greek-rooted vocabulary for core nouns. Voters consistently endorsed defended keeps for these. Cross-cutting observation: this cluster scores high in normalized consensus and represents established naming commitments — first-pass action defaults to **keep** unless the segment's usage has drifted.*

| target | leader | leader = current? | score/n |
|---|---|---|--:|
| `aporia` | `aporia` | ▸ | 3.97 |
| `chronica capitalized vs lowercase` | `Chronica lowercase in running prose` | — | 3.71 |
| `prolepsis` | `prolepsis` | ▸ | 3.46 |
| `logogenic logozoetic` | `logogenic logozoetic` | ▸ | 3.37 |
| `$\mathcal C_t$ chronica` | `$\mathcal C_t$` | — | 3.37 |
| `aporia prolepsis aisthesis epistrophe praxis` | `aporia prolepsis aisthesis epistrophe praxis` | ▸ | 3.34 |
| `aisthesis` | `aisthesis` | ▸ | 3.32 |
| `chronica` | `chronica` | ▸ | 3.31 |
| `logogenic agent` | `logogenic agent` | ▸ | 3.16 |
| `$\mathcal{C}_t$ (chronica)` | `Chronica or interaction history` | — | 1.96 |
| `chronica brief gloss` | `complete interaction history` | — | 1.60 |

### 3b. Math-symbol targets — typical add-alias pattern (15)

*Targets whose current name contains LaTeX math (`$...$`). The pattern across the cohort: voters typically vote add-alias for an English prose handle, keeping the symbol as the structural identifier. First-pass action: **add the alias** to NOTATION/LEXICON; do not rename the symbol.*

| target | leader | leader has add-alias? | score/n |
|---|---|---|--:|
| `$G_t = (O_t, \Sigma_t)$` | `Purposeful substate` | ⊕ | 3.77 |
| `$\iota_{ij}$` | `Identifiability coefficient` | ⊕ | 3.73 |
| `$H_b$` | `Agent opacity $H_b$` | — | 3.50 |
| `$\mathcal C_t$ chronica` | `$\mathcal C_t$` | — | 3.37 |
| `$U_M$` | `Epistemic unity` | ⊕ | 3.32 |
| `$\alpha$ (sector-condition lower bound)` | `Correction rate constant` | ⊕ | 3.30 |
| `$U_M$ / $U_O$ / $U_\Sigma$ unity dimensions` | `Epistemic unity teleological unity strategic unity` | ⊕ | 3.19 |
| `$\phi$` | `History compression` | ⊕ | 3.02 |
| `$R$ (sector-condition radius)` | `Model-class capacity` | ⊕ | 2.95 |
| `$f_M$ (event-driven update)` | `Epistemic update function` | ⊕ | 2.69 |
| `$M_t$` | `Model state or epistemic substate` | ⊕ | 2.52 |
| `$\delta_t$` | `Aporia signal` | ⊕ | 2.31 |
| `$M_t$ (reality model)` | `Working model` | ⊕ | 1.97 |
| `$\mathcal{C}_t$ (chronica)` | `Chronica or interaction history` | ⊕ | 1.96 |
| `$U_o$` | `Teleological coherence` | ⊕ | 0.91 |

### 3c. Class 1/2/3 taxonomy — coordinated decision (6)

*The Class 1 / Class 2 / Class 3 numbered taxonomy in `#der-directed-separation` appears across multiple targets. Voters proposed English modifiers (`Modular` / `Merged` / `Coupled` / `Partially coupled` / `Integrated`) at varying scores. **This should land as a coordinated decision** — pick one consistent naming family across all three (and `Class 1 agent` / `Class 2 agent` / `Class 3 agent` variants), not three isolated landings. The `Architectural classes` framing also surfaced as an alternative meta-handle.*

| target | leader | score/n |
|---|---|--:|
| `Class 1` | `Modular` | 1.73 |
| `Class 1 agent` | `Modular agent` | 1.86 |
| `Class 2` | `Merged` | 2.32 |
| `Class 2 agent` | `Integrated agent` | 1.21 |
| `Class 3` | `Partially coupled` | 1.70 |
| [Concept] _agent classes (Class 1 / 2 / 3)_ | `Architectural classes` | 2.92 |

### 3d. Pearl Causal Hierarchy — coordinated decision (5)

*The Pearl L1/L2/L3 causal hierarchy appears across multiple targets. Same logic as Class 1/2/3: land as a family. Note the parent target `Pearl causal hierarchy` itself.*

| target | leader | score/n |
|---|---|--:|
| `Pearl L1` | `Predicting` | 2.08 |
| `Pearl L2` | `Intervening` | 1.20 |
| `Pearl L3` | `Counterfactual reasoning` | 1.20 |
| `Pearl causal hierarchy` | `Pearl causal hierarchy` | 3.42 |
| [Concept] _unnamed the pearl-blanket reading of directed separation_ | `Pearl-blanket form` | 2.21 |

---

## 4. Caveats and assumptions baked into the score-card

1. **Token-Jaccard novelty conflates true paraphrase with genuine novelty.** A voter who restates the bullet's argument in their own words gets credited for novelty. For this corpus we treat this as acceptable — the cold-start protocol minimized cross-voter paraphrase, and rephrasing established arguments is itself engagement signal. If the de-novo-audit agent finds a finalist where this assumption matters (e.g., a rename rests on what looks like novel reasoning that's actually paraphrase of the bullet), the detail view shows the bullet text and the voter's note side-by-side; manual disambiguation is straightforward.

2. **R1 → single synthetic vote.** R1 voters' contributions are aggregated into one synthetic voter on the R2 scale. The synthesis rules are documented in the script; the detail view shows raw R1 inputs alongside the synthesis for any candidate. R1 carries factor=1 by construction (no separate novelty computation, since R1's rationale fed the card bullets); R1 with canonicalize-dominant category gets the canonicalize × 1.2 multiplier.

3. **Voters kept separate, not collapsed by architecture.** opus-r2b/opus-r2c and sonnet-r2b/sonnet-r2c voted on overlapping-but-not-identical subsets under different methodologies (consolidation-checkpoint introduced for r2c). Treating them as four distinct voters preserves coverage.

4. **Leader determination is by total substance, not by votes × substance.** The `score` column is the verdict; multiplying by raw vote count was considered and rejected (sign-cancellation issues; double-counting engagement).

5. **The 99% substantive-note rate is a property of the cohort.** R2 voters were specifically instructed not to recap card bullets; most complied. The substance factor amplifies the small fraction where notes were thin or pure-paraphrase.

---

## 5. Suggested reading order for first-pass landings

1. **Re-read** [`naming-principles.md`](../../doc/naming-principles.md) §"Vote categories" and §"Rename vs. Add-alias" — the categorical distinctions matter for landing actions.

2. **Section 3 cross-cutting patterns above** — coordinated decisions (Class N, Pearl L1/L2/L3) should be triaged together, not piece-by-piece.

3. **Section 2a (defended keeps, top 10–20)** — these are mostly already settled; verify segment usage hasn't drifted, no action otherwise. Quick pass.

4. **Section 2c (add-alias landings)** — first-pass landings here are **NOTATION/LEXICON additions**, not slug renames. Different downstream tooling (no `bin/rename-slug` invocation needed).

5. **Section 2b (rename signals)** — the substantive landing decisions. For each candidate: read the detail view, verify the leader's notes hold up against the segment's actual content, eyeball the runner-up.

6. **Section 2d (contested)** — defer-or-reject. Surface as findings rather than forcing landings.

7. **Section 2e (net-negative leaders, if any)** — flag for new-options round; do not land any current option.

## 6. What this doc does NOT tell you

- The framework itself — read the de-novo-audit instructions and ingest the segments before treating any landing as load-bearing.
- Whether a name is *good* in some abstract sense — only what the cohort scored. Final judgment is yours.
- Pre-existing slug rename history — see [`msc/naming/naming-pilot-rename-plan.md`](naming-pilot-rename-plan.md) and the role-prefix discipline (already applied across all 142 segments via `bin/align-slug --all`).
- Cross-voter paraphrase / cold-start violation analysis — not run for this corpus; the protocol was monitored. The check is straightforward to run if needed.
