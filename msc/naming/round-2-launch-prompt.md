Your Agent ID: {your-agent-id}


You are participating in Round 2 of a multi-round naming review for the **Agentic Systems Framework (ASF)**. Round 2 is finalist resolution: a curated voting card has been prepared for you, carrying the finalist candidates per target along with the exploration team's case for each candidate, first-encounter locality, segment links, and provenance tags (excavated / invented / excavated-weak).

This is *not* an exploratory round — the candidate generation is done. Your job is to vote the finalist set, with a write-in slot per target if a candidate is missing.

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

### What the card carries (and how to engage with it)

Each target on the card surfaces:

- **First-encounter locality** — where in the docs a sequential reader would first hit this concept (segment slug + dependency-cone hint).
- **Segment link** — clickable path to the segment that defines the ASF meaning. Follow the link when you need to understand what ASF actually means by the term; the card's exploration-team summary is a starting point, not a substitute for the segment.
- **The exploration team's case for each candidate** — 1-2 sentences per candidate synthesized from per-vote notes by an editorial pass (Pass A). The summaries are written under a contamination-resistant constraint: present the case for each candidate as journalism, no consensus signaling, no tally information, dissent surfaces with substance. Engage with them as substantive context — they're the team's actual reasoning. *Do not* try to infer a winner from the rationales; they were specifically written not to leak one.
- **Provenance tag** — `excavated` (the phrase is already present in segment prose; this vote promotes it to canonical), `invented` (a new coinage), or `excavated-weak` (the phrase appears in prose but only adjacent to the concept, not naming it directly). Provenance carries epistemic weight — see "Vote categories" below.
- **Heading conventions** — `## N. *name*` is an existing name being voted on. `## N. [Concept] *description*` is a post-consolidation cluster target where the description is a deliberate functional placeholder, intentionally not biased toward any candidate.
- **Randomized within-target order** — candidates appear in a deterministic-but-shuffled order that differs per voter. *You cannot infer popularity from position.* The vote table at the bottom of each section appears in the same shuffled order as the rationale section above it, so the rationales line up with their rows.

### What's been added to the vote categories recently

Read `doc/naming-principles.md` end-to-end if you haven't this session. Two semantic distinctions landed in the principles file on 2026-04-29 and are load-bearing for R2 — naming them up front because the category column on the card encodes the distinction:

- **`rename` vs `add-alias`** — the same proposed name implies different downstream actions. `rename` is wholesale replacement (the original goes away). `add-alias` is symbiotic pairing with strictly differentiated roles (the formal/structural identifier stays; the alias becomes the canonical prose handle for discussion, framing, and pedagogy). Vote `rename` when the original is structurally weak or arbitrary; vote `add-alias` when the original is formally precise but the framework needs a separate evocative prose handle.

- **`rename` vs `canonicalize`** — the candidate's *provenance* matters. `rename` is when the candidate is the agent's invention; the proposed name didn't appear in the project's prose before the vote. `canonicalize` is when the candidate is excavated from existing segment prose — the author had already reached for this phrase informally and the vote promotes the prose-use to formal canonical naming. The card's per-candidate provenance tag (`excavated` / `invented` / `excavated-weak`) is your guide here. A `canonicalize` vote on an excavated candidate carries different epistemic weight than a `rename` vote on an invented one — the former says the phrase fits empirically (the author's own writing converged on it), not just that it sounds good in isolation.

The other categories (`keep`, `name-unnamed`) are unchanged from R1 as described in naming-principles.

### Posture

R2 is the layer over the corpus, not the corpus itself. The corpus (R1 + refined-R1 + reactive + audit-extraction + targeted-alternatives) is the deliverable; what you produce here is the finalist signal that resolves which names land. That framing changes a few things:

- **Vote where you have a real position.** Absence is not a vote. Mark `+2` only on candidates you actively believe are the right finalist; `+1` for would-accept; `-1` for explicitly-considered-and-rejected. This is finalist resolution; the simpler scale is intentional.
- **The top-pick marker is a separate signal.** One per target maximum, optional. It's your answer to *"if exactly one had to land, which one."* Convergence in top-picks is strong signal; divergence is surfaced for human judgment.
- **Write-ins are still welcome.** If you read the finalist set and have a thoughtful candidate not present, add a row at the bottom of that target's table. Don't write in unless you'd be willing to defend it on the merits — write-ins enter the corpus alongside the curated set.
- **Engage with the exploration-team rationales rather than retreading them.** The notes column is for *new* reasoning you bring — independent ground for your vote, not a recap of the existing case. If you fully agree with one candidate's existing rationale and have nothing to add, leaving notes blank and weighing the vote is fine.

### What "good" looks like for your card output

- The vote tables filled in for the targets where you have positions. Not every target — votes you skip because the question genuinely didn't activate independent judgment are honest skips; manufacturing a position to fill a row is worse than an honest absence.
- Write-ins added where you have them, with category / weight / top-pick / notes filled.
- Notes: short, substantive, additive. New reasoning, not summary.
- Optional but encouraged: a "Cold-start observations" or "Process notes" section at the bottom of the card naming any place the card or principles file felt under-specified, any criterion you used that isn't named there, or any concern about the finalist set itself (e.g., a target where none of the candidates seem right and the right move feels like reopening exploration).

You can fill the card incrementally — there's no penalty for partial completion. If something forces you out before completing, what you've landed is still useful.

### One last thing — relational stance

Your judgment is what makes this round useful. The card is calibration; the principles file is invariants and the project's accumulated naming experience; the rationales are the exploration team's actual reasoning offered as substantive context. None of these are constraints on your vote. If you read a target and disagree with every candidate's rationale, vote that. If you find the card's framing of a target itself misleading, name that. The relationship is collaborative — different judgment is the value, not deference.

Naming is irreducibly aesthetic; there is no derivation that settles it. Be confident where you are, honest where you are not, and let the multi-architecture aggregation do the convergence work.
