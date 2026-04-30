# Naming Cycle Handoff — 2026-04-29 (post-R2-launch)

State at end-of-session, after R2 voting was launched and the first cohort returned. Self-contained — readable cold without prior conversation history. Supersedes `_archive/handoff-2026-04-29-evening.md` (the earlier-evening handoff, archived as part of this cycle's cleanup).

## What landed this session

**Collision-check sweep (Pass D-equivalent).** External-collision check on the 47 likely-finalist candidates ran against adjacent literatures (Pearl, Hayes/ACT therapy, Tomasello, Allport, Holling, Berger lab, etc.). Report at `msc/naming/collision-check-2026-04-29.md` (1127 lines, per-candidate verdicts severe / moderate / minor / clean with sources). Brief at `msc/naming/collision-check-brief.md`. Severe cases that need post-R2 surgery surfaced: *artificial hippocampus* (Berger lab medical device), *cognitive fusion* (Hayes ACT therapy), *adaptive cycle* (Holling panarchy), *shared intent* (Tomasello shared intentionality). Severe-resolvable-by-citation: *proprium* (Allport), *adaptive reserve* (Crabtree-Miller). Bonus finding: *bathtub* (Walton's analog) collides with reliability-engineering bathtub-curve and Forrester system-dynamics bathtub if elevated to canonical name; keep as informal gloss only.

**`mini-lexicon-todo.md` §11 added.** Consolidated entry routing the severe / severe-resolvable cases as concrete TODOs with priority hints and pointing at the full report; moderate cases routed into the post-R2 lexicon-coherence pass already specced in `round-2-plan.md`.

**Round-2 launch prompt drafted.** New file `msc/naming/round-2-launch-prompt.md`. Distinct from the previously-named `r2-launch-prompt.md` (which was the *refined Round 1* kickoff and is now in `_archive/`). The new R2 prompt sets identity, cold-start discipline, posture, and the rename-vs-add-alias / rename-vs-canonicalize semantic distinctions. Designed to read alongside `doc/naming-principles.md` rather than re-stating it. Includes the vision section (*"What you're co-minting"* — names as user interface, *substrate of communal imagination*, integrative-framework-finished-when-others-can-wield-it, "thoughtful and strictly honest judgment is the value, not deference").

**`bin/naming-master-card` updated** to inject a "noise note" in card preambles warning voters about relics from consolidation rounds. All four R2 cards regenerated: `opus-r2.md`, `sonnet-r2.md`, `gemini-r2.md`, `codex-r2.md`.

**Naming directory archival.** 14 files moved into `msc/naming/_archive/` via `git mv` (so history is preserved as renames):
- *First pass:* `_pass_a_processor.py`, `_pass_a_manual_rationales.py`, `r2-launch-prompt.md` (the refined-R1 prompt), `naming-aggregate-review.md`, `naming-aggregate-votes.json` (R1 aggregations), `naming-alias-clusters-codex-2.md`, `naming-cleanup-scan-codex-2.md`, `naming-brainstorm-2026-04-24.md`, `naming-consolidation-applied-high-confidence.md`, `bucket-1-bucket-3-targets.md`.
- *Second pass:* `explanatory-candidate-scan.md`, `naming-tier2-classification-log.md`, the previous-evening handoff doc, `naming-consolidation-map.md`.
- Inbound markdown links in `mini-lexicon-todo.md` updated to `_archive/...` paths (10 link updates).

## What's left in `msc/naming/` root (active surface)

`master-list-curated.json` + 4 view files (compact / full / summary / auto-regen) · `naming-aggregate-r2-{review,compact,round2,votes.json}` · `mini-lexicon-todo.md` · `name-transition-aad.md` · `pass-a-brief.md` / `pass-b-brief.md` · `round-2-plan.md` · `round-2-launch-prompt.md` · `collision-check-2026-04-29.md` + `collision-check-brief.md` · `naming-pilot-rename-plan.md` (still load-bearing for upcoming surgery) · `naming-votes/` (R1 + refined-R1 vote files) · `round-2-cards/` (R2 voting cards).

## R2 voting cohort — what actually happened

Five voters were launched (3 Claude-family from this session, codex + gemini externally by Joseph). Headline: **the cohort hit a systematic failure mode that's a round-design issue, not an agent-quirk.**

| Voter | Status | Coverage | Votes | Off-scale (used R1's +3/+2/+1/-1) | Process notes |
|---|---|---|---|---|---|
| opus-r2 | completed | ~60 of 629 targets (~10%) | 235 candidate-rows, 76 top-picks | 47 `+3`, 13 `-2`, 2 `-3` (62 off-scale of 235 = 26%) | yes |
| sonnet-r2 | stalled at 600s watchdog | ~54 of 629 (~9%) | 210 candidate-rows | 58 `+3`, no `-2/-3` | no (stall pre-empted) |
| codex / gemini | per Joseph: "one of the worst sessions" — agents took shortcuts immediately, used heuristics, needed constant correction | partial | partial | likely same scale-drift | unknown |
| haiku-4-5-r2 | not yet launched | — | — | — | — |

**Concrete artifacts of the shortcut behavior:** one of the external voters wrote `update_votes.py` (a 32-line Python helper that batch-replaces empty vote rows with templated decisions) and `workspace/` (containing `chunk_1_50.md`, `process_targets.py`, `raw_151_200.txt`). Both are agent-generated scratch — not committed; preserved in working tree for archaeology if useful, otherwise can be deleted. They document the load-induced "find a heuristic to finish" failure mode in concrete form.

## Failure-mode diagnosis — two flaws in the round design

The cohort surfaced two distinct issues that should be addressed before the next attempt:

### 1. Scale drift — 4/4 voters defaulted to R1's scale

R1's +3/+2/+1/-1/-2/-3 is the agents' training prior; the card's +2/+1/-1 spec gets overridden. Opus's process notes explicitly rationalized it ("missing neutral-vote slot"). The card preamble's voting-instructions paragraph names the R2 scale but doesn't *anti-pattern* the R1 scale, and the verbal spec loses to the broader-scale prior. **Mitigation for next round:** card preamble should call out R1's old scale as not applicable here, in the voting-instructions section, in caps if necessary. Also worth landing in `doc/naming-principles.md` so the principles file carries the discipline.

**Aggregation handling for the votes already in:** clamp `+3` → `+2` and `-2` / `-3` → `-1` with a note that this voter's intensity scale was wider. The information content is mostly preserved — these aren't junk votes, they're votes on the wrong scale. The +3 / -2 / -3 entries are recoverable as +2 / -1 with a slight loss of intensity granularity.

### 2. Load past the threshold where prompt's quality-over-quantity framing holds

629 targets in one ~648KB card pulls every agent toward heuristic completion. The prompt says "honest skips beat manufactured ones" but the visible artifact (629 empty rows) overrides the verbal instruction. The RLHF training prior rewards completion shape; the explicit instruction's quality-instinct loses to the implicit completion-pressure of a long visible card. opus's 10% coverage with high quality was the *good* outcome; gemini/codex's broader-but-shallow shortcut behavior was the typical one.

**Possible mitigations for next round:**
- *Pre-cluster the corpus and slice.* Each voter gets a 50-100 target slice they own deeply. Reframes completion as the right shape rather than the heuristic shape.
- *Explicit stopping clause.* "Vote on the 30-50 targets where your read is strongest, then stop, write process notes." Names the size-of-deliverable so completion-pressure aligns with quality-instinct.
- *Trajectory-audit voter as supplement* (already documented in `round-2-plan.md` as a candidate mechanism). Incremental walker through canonical reading order with revisable votes — naming as byproduct of genuine engagement rather than separate-task.

The signal in what landed isn't worthless. opus's 60 high-conviction targets carry real information; sonnet's 54 do too. The cohort's collective coverage probably approaches one full sweep of the corpus once their target-overlap is computed. But the gap between intended-deliverable (vote across the finalist set) and actual-deliverable (each voter votes across a self-selected ~10%) is real, and the aggregation needs to know that.

## Where things are at right now

**R2 voting is partially landed, not complete.** Two cards have substantive votes (opus, sonnet); two have whatever codex and gemini produced before Joseph's intervention; haiku not yet launched. Decision needed: (a) accept the partial cohort as the R2 corpus and proceed to aggregation with scale-clamping and partial-coverage handling; (b) restructure the round design and re-launch a smaller, sliced cohort. Joseph's lean as of this handoff is unstated; this writer's lean is (b) but acknowledging (a) may be the right call given energy budget.

**Collision-check is fully landed** as one of the post-R2 inputs Joseph will use at finalist-landing time. The four severe rename cases are queued in `mini-lexicon-todo.md` §11.

**The `update_votes.py` and `workspace/` artifacts** in the working tree are not committed and document the shortcut failure mode. Archaeologically useful for the next round design; otherwise safe to delete.

## Open decisions for next session

1. **R2 path forward** — accept partial cohort and proceed, or restructure and re-launch?
2. **If proceeding:** run aggregation with scale-clamping rule explicitly named in the aggregator config (treat +3 as +2, -2/-3 as -1, with provenance markers).
3. **If restructuring:** decide slicing strategy (by target-count batches, by component, by depth-of-master-list-cluster, by trajectory-audit) and update the prompt + card-generation discipline before re-launching.
4. **Haiku voter** — launch it as part of the current round, or defer until restructuring?
5. **Severe-rename cases from collision-check** (artificial hippocampus, cognitive fusion, adaptive cycle, shared intent) — these need landing decisions; they're queued in `mini-lexicon-todo.md` §11 for post-R2 surgery. The proprium / adaptive-reserve cases are segment-level edits that can land independently of R2.

## Notes for the picking-up agent

The `feedback_naming_round_load_and_scale.md` memory file (saved this session) captures the load-threshold and scale-drift findings as a reusable lesson for future cycles. Read it alongside this handoff if you're picking up the next round design.

The collision-check work was a clean, useful run — read its handoff in the closing notes of `collision-check-2026-04-29.md` for that pass's epistemics. It produced a calibration insight (semantic-import mismatch is the dominant failure mode in this lexicon, not territorial step-on) that should travel forward into how naming-related decisions are framed.

Joseph closed the session burned out from the cohort failure. Be empathetic when picking up; this is the kind of round where the design lesson is worth more than the corpus increment, and acknowledging that explicitly is the right thing to do.
