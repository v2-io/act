# R2 Voting Cohort — Progress

**Generated:** 2026-04-30T19:31:10Z
**Voters discovered:** 6 (`codex-r2b`, `gemini-r2`, `opus-r2b`, `opus-r2c`, `sonnet-r2b`, `sonnet-r2c`)
**Targets per card:** 629
**Substantive-notes threshold:** ≥ 30 chars (tunable via `--notes-threshold=N`)

## At a glance

| voter | tgt voted | votes | top-picks | substantive | write-ins | can-vote | gap | drift | seq max | off-scale |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `codex-r2b` | 58 | 113 | 58 | 113 (100%) | 8 | 58 | – | – | 58 | – |
| `gemini-r2` | 190 | 193 | 191 | 189 (98%) | 4 | 466 | 276 | – | 240 | – |
| `opus-r2b` | 54 | 141 | 44 | 140 (99%) | 5 | 54 | – | – | 45 | – |
| `opus-r2c` | 78 | 219 | 76 | 216 (99%) | – | 78 | – | – | – | – |
| `sonnet-r2b` | 43 | 137 | 43 | 136 (99%) | 3 | 43 | – | – | 4 | – |
| `sonnet-r2c` | 48 | 140 | 48 | 140 (100%) | – | 44 | – | -4 | – | – |

*Columns:* `tgt voted` = unique targets with at least one voted candidate-row in the card (the ground truth); `votes` = total candidate-row votes (multiple per target possible); `top-picks` = rows marked as top-pick; `substantive` = rows whose notes column meets the threshold; `write-ins` = voted rows on or after the `*(write-in)*` placeholder (new candidates not in the curated finalist set); `can-vote` and `gap` come from the tracker (gap = can-vote rows that haven't cast yet); `drift` = tracker's `voted=true` count minus card's `tgt voted` (positive = stale `voted=true` markers in tracker; negative = card has cast votes the tracker hasn't synced to yet — re-run `bin/naming-master-tracker` to resync); `seq max` = highest voting-sequence integer; `off-scale` = votes using R1's wider scale (+3 / -2 / -3) instead of R2's spec (+2 / +1 / -1).

## Cohort coverage

- **Targets with ≥1 voter:** 335 / 629 (53%)
- **Targets with ≥2 voters:** 110 / 629
- **Targets with ≥3 voters:** 20 / 629
- **Targets with ≥4 voters:** 5 / 629
- **Total candidate-row votes:** 943
- **Substantive votes (cohort-wide):** 934 (99%)
- **Off-scale residual:** 0 (R2 spec is +2/+1/-1; off-scale votes can be clamped at aggregation time but signal the R1-scale prior leaking through)

## Off-scale breakdown

- `codex-r2b`: clean (no off-scale votes)
- `gemini-r2`: clean (no off-scale votes)
- `opus-r2b`: clean (no off-scale votes)
- `opus-r2c`: clean (no off-scale votes)
- `sonnet-r2b`: clean (no off-scale votes)
- `sonnet-r2c`: clean (no off-scale votes)


## Vote-category distribution

| voter | rename | keep | canonicalize | add-alias | name-unnamed |
|---|--:|--:|--:|--:|--:|
| `codex-r2b` | 23 | 39 | 17 | 30 | 4 |
| `gemini-r2` | 15 | 126 | 7 | 17 | 25 |
| `opus-r2b` | 54 | 29 | 19 | 12 | 27 |
| `opus-r2c` | 121 | 54 | 17 | 20 | 7 |
| `sonnet-r2b` | 60 | 37 | 25 | 8 | 7 |
| `sonnet-r2c` | 62 | 47 | 6 | 7 | 18 |

## Write-ins

Candidates voters added beyond the curated finalist set — voted rows on or after the `*(write-in)*` placeholder. These enter the corpus alongside the curated candidates and may signal targets where the methodology's pre-clustering missed something the voter found load-bearing.

| voter | target # | candidate | category | weight | notes excerpt |
|---|--:|---|---|--:|---|
| `codex-r2b` | 29 | Reality model | add-alias | +2 | Segment title and content support this directly: $M_t$ is the agent's compres… |
| `codex-r2b` | 40 | Counterfactual reasoning | add-alias | +2 | Best brief-grade gloss for Pearl L3: "given what happened, what would have ha… |
| `codex-r2b` | 56 | complete interaction history | add-alias | +2 | Best first-use gloss. It stays English-accessible while preserving the key pr… |
| `codex-r2b` | 161 | Adaptive Systems Under Uncertainty | keep | +2 | The defining scope segment makes "under uncertainty" load-bearing: $\mathcal … |
| `codex-r2b` | 176 | Intervening | add-alias | +2 | Direct agent-side gloss for Pearl L2: "what will I observe if I do this?" |
| `codex-r2b` | 205 | chronica (complete interaction history) | canonicalize | +2 | Canonicalize the pairing: `chronica` names the complete, singular, non-forkab… |
| `codex-r2b` | 236 | event-driven dynamics | keep | +2 | Correctly names the formulation choice: asynchronous typed events, not clock … |
| `codex-r2b` | 255 | information-loss boundary | rename | +2 | Defining segment names this directly as `information-loss-boundary`; it carri… |
| `gemini-r2` | 59 | Class 3 | write-in | +2 | Consistent with my vote on Class 1. The numbered taxonomy (Class 1/2/3) is ne… |
| `gemini-r2` | 80 | Class 1 | write-in | +2 | The numbered taxonomy (Class 1/2/3) is neutral and structurally clean. Replac… |
| `gemini-r2` | 432 | Class 2 | write-in | +2 | Consistent with my votes on Class 1 and Class 3. The neutral, numbered taxono… |
| `gemini-r2` | 477 | Closure defect | name-unnamed | +2 | Dropping the repetitive 'Composition closure closure defect' in favor of just… |
| `opus-r2b` | 33 | Legendre-Fenchel forcing | name-unnamed | +2 | Write-in. Names the *geometric target* the four layers manifest, per the curr… |
| `opus-r2b` | 35 | template instantiation | name-unnamed | +1 | Write-in. Shorter and more usable than the full phrase. Pattern: a segment na… |
| `opus-r2b` | 136 | effects spiral | keep | +2 | Write-in (the corrected plural form). The principles file uses "effects spira… |
| `opus-r2b` | 287 | temporal precedence | rename | +2 | Write-in. Names exactly the postulate's content: "event A can be a cause of e… |
| `opus-r2b` | 419 | persistence-template family | name-unnamed | +2 | Write-in. Cleaner than the offered candidate. The three current/proposed temp… |
| `sonnet-r2b` | 3 | *(write-in)* | name-unnamed | +1 | Write-in: "model-unity collision" or "$U_M$ disambiguation" would be cleaner … |
| `sonnet-r2b` | 21 | *(write-in)* | rename | +1 | Write-in: "directional-fidelity bridge" — names the key assumption (B1 direct… |
| `sonnet-r2b` | 283 | Miller extreme transition motif | keep | +1 | Write-in: "Miller's extreme transition motif" (with possessive, naming just t… |

## Quality signal — substantive-note distribution

| voter | total votes | substantive | empty-or-thin | sub-rate |
|---|--:|--:|--:|--:|
| `codex-r2b` | 113 | 113 | 0 | 100% |
| `gemini-r2` | 193 | 189 | 4 | 98% |
| `opus-r2b` | 141 | 140 | 1 | 99% |
| `opus-r2c` | 219 | 216 | 3 | 99% |
| `sonnet-r2b` | 137 | 136 | 1 | 99% |
| `sonnet-r2c` | 140 | 140 | 0 | 100% |

*Substantive-note rate is the headline depth-of-engagement signal — a +2 with substantive notes carries different aggregation weight than a +2 with no notes, regardless of identical face-value weight.*

