Your Agent ID: {your-agent-id}


You are participating in Round 2 of a multi-round naming review for the **Agentic Systems Framework (ASF)**. Round 2 is finalist resolution: a curated voting card has been prepared for you, carrying the finalist candidates per target along with the exploration team's case for each candidate, first-encounter locality, segment links, and provenance tags (excavated / invented / excavated-weak).

This is *not* an exploratory round — the candidate generation is done. Your job is to vote the finalist set, with a write-in slot per target if a candidate is missing.

### What you're co-minting

Names are the user interface of a theory. Every future reader — agents picking up after context turnover, external reviewers auditing a segment cold, collaborators returning after months — meets the concepts through their names before they meet the mathematics. A memorable name compresses the intuition into a few syllables that survive working-memory pressure forever; an arbitrary or clinical one forces re-derivation on every encounter forever. That asymmetry is what this round is for.

From `doc/naming-principles.md`: *memorable names are the substrate of communal imagination*. A community can argue about, extend, and apply *directed separation* in ways it could not handle a clinical multi-word label, because the name has shape for a group of minds to get purchase on collectively. The framework's value is integrative — the work is finished when others can wield the concepts without the original authors in the room. Names are how that wielding starts.

You are not casting votes on someone else's deliverable. You are co-minting the vocabulary that will carry the framework forward across every future reader and session. The cross-architecture aggregation across the voter slate is the ratification mechanism — but the *substance* is your own discrimination, in your own voice: what feels load-bearing, what feels awkward, what passes the renamed-from-now-sounds-weird test, what a skilled reader six months out could refer to in conversation without looking it up. **Thoughtful and strictly honest judgment is the value, not deference** — that's a description of what the round is *for*, not a courtesy you're being extended. Cross-voter divergence on a target carries information; it's surfaced for human judgment at landing time, not averaged away.

### Cold-start instruction — read this first, before anything else

The cold-start restriction is narrow and specific: **avoid contamination from anchoring naming-cycle workings under `msc/naming/`**. The principle is simple — files that contain vote tallies, aggregate weights, candidate-by-candidate leaderboard signal, or other voters' position statements would collapse the cross-voter diversity this round depends on; files that describe the cycle's design, plans, and meta-process don't anchor and are useful context. If you're unsure about a file in `msc/naming/` not whitelisted below, the test is: would reading it surface aggregate weights, candidate ranks, vote tallies, or other voters' positions? If yes, skip. If no (it's about the cycle's design, planning, or meta-process), it's whitelist-eligible — exercise judgment.

**Outside `msc/naming/`, navigate freely, and thoroughly!**  To contribute votes & ideas that are meaningful and worthy according to the instructions below and on the voting card itself, you will see that you will need to thoughtfully comprehend what you are voting on and possible alternatives through deeply understanding the project (`CLAUDE.md` and `README.md` are ideal starting points). It is recommended that you also read `doc/naming-principles.md`

Within `msc/naming/` there are a few files you can safely read if it comes up:
- Your own card obviously in `msc/naming/round-2-cards/{your-agent-id}.md` -- prepare to modify it in place with your voting (or create one in a temporary directory and move it here when it is filled out). But don't read other agents cards.
- `round-2-plan.md` , `name-transition-aad.md` , and `pass-*` : Historical documents
- `mini-lexicon-todo.md`, `collision-*` : current working files for name-related items that surfaced but aren't covered by this voting procedure.

If you've already glanced at any of the excluded files in this session — including incidentally — disclose it explicitly at the bottom of your card under a "Cold-start observations" heading. The contribution may still be useful as long as it is marked.

### Your identity and where to find your card

Your card is at `msc/naming/round-2-cards/{your-agent-id}.md`. If the file doesn't exist, generate it first via `bin/naming-master-card --seed={your-agent-id}` (the seed is your agent ID, which deterministically produces your shuffle; same agent-ID always produces the same card).

You vote by editing the card directly — fill in the empty `category`, `weight`, `top-pick?`, and `notes` cells in the vote tables. The card is your output. No separate vote file.

### How to engage with the card

The card's preamble covers the voting mechanics (scale, top-pick, write-in, category column, heading conventions, within-target randomization). Two things the card surfaces but doesn't pre-explain:

- **The exploration team's per-candidate rationales** were synthesized from per-vote notes by an editorial pass (Pass A) under a contamination-resistant constraint — case-for-each-candidate as journalism, no consensus signaling, no tally information, dissent surfaces with substance. Engage with them as substantive context — they're the team's actual reasoning. *Do not* try to infer a winner from them; they were specifically written not to leak one.
- **Provenance tags** (`excavated` / `invented` / `excavated-weak`) tell you whether a candidate already lives in segment prose or is a fresh coinage. This matters because of the **rename vs canonicalize** distinction in `doc/naming-principles.md` — a canonicalize vote on an excavated candidate says the phrase fits the concept *empirically* (the author's own writing already converged on it), which carries different epistemic weight from a rename on an invented one. Pair this with the **rename vs add-alias** distinction (also in the principles file): rename replaces the original wholesale; add-alias keeps the formal/structural identifier and adds a parallel prose handle with strictly differentiated roles. The full treatment of all five categories is in the principles file; the two distinctions above are the ones load-bearing for R2 specifically because the card's category column encodes them.

Segment links on the card are clickable — follow them when you need to understand what ASF actually means by a term. The card's rationales are a starting point, not a substitute for the segment.

**A note on noise.** Multiple passes and a lot of quick consolidation rounds have left some relics and noise in the voting entries — odd phrasings, broken-looking candidates, the occasional rationale that reads strangely against its candidate. Do your best to understand the original intent (the segment usually clarifies it), and use the notes column to flag anything where the noise is severe enough to make the vote ambiguous. This is the point in the pipeline where a voter's read can catch what an editorial pass missed.

### Posture

R2 is the layer over the corpus, not the corpus itself. The corpus (R1 + refined-R1 + reactive + audit-extraction + targeted-alternatives) is the deliverable; what you produce here is the finalist signal that resolves which names land. A few things follow:

- **Vote where you have a real position.** Absence is not a vote — manufacturing a position to fill a row is worse than an honest absence.
- **Convergence vs divergence in top-picks both matter.** Convergence is strong signal; divergence is surfaced for human judgment, not averaged away.
- **Write-ins are welcome but should be defensible.** They enter the corpus alongside the curated set.
- **The notes column is for *new* reasoning you bring** — independent ground for your vote, not a recap of the exploration-team rationale. If you fully agree with an existing rationale and have nothing to add, leaving notes blank and weighing the vote is fine.

### What "good" looks like for your card output

- Vote tables filled in for the targets where you have positions; targets you skip because the question genuinely didn't activate independent judgment are honest skips.
- Write-ins added where you have them, with category / weight / top-pick / notes filled.
- Notes: short, substantive, additive. New reasoning, not summary.
- Optional but encouraged: a "Cold-start observations" or "Process notes" section at the bottom of the card. Fair game for any place the card or principles file felt under-specified, any criterion you used that isn't named there, any cycle-level concern (a target where none of the candidates seem right and the right move feels like reopening exploration; a target whose framing of the underlying concept feels off; whatever else surfaced).

You can fill the card incrementally — no penalty for partial completion. If something forces you out before finishing, what you've landed is still useful.

### One last thing

If you read a target and disagree with every candidate's rationale, vote that. If you find the card's framing of a target itself misleading, name that — write-in slot per target, plus the process-notes section at the bottom for anything cycle-level.

Naming is irreducibly aesthetic; there is no derivation that settles it. Be confident where you are, honest where you are not, and let the multi-architecture aggregation do the convergence work.
