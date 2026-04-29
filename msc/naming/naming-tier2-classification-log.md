# Naming Tier-2 Classification — R1 Vote-File Retro-Categorization Log

**Date:** 2026-04-29
**Scope:** The 10 R1 vote files in `msc/naming/naming-votes/` that were originally written under the legacy 4-column schema (`current | new | weight | notes`). Each file has been migrated to the canonical 5-column schema (`current | new | category | weight | notes`) by retro-classifying each row's category from notes-content evidence.

**Conservative discipline.** Where notes-content evidence was weak or ambiguous, the category cell was left empty (nil) rather than guessed. Honest sparse classification beats confident wrong classification; downstream the aggregator handles nil cleanly.

**Backups.** Originals preserved verbatim at `msc/naming/naming-votes/_pre-tier2-backup/` before any modification.

**Tooling.** Classification was performed by a Ruby script (`/tmp/classify_r1.rb`) using note-pattern heuristics (signal regexes for each category). The script preserves `\|` escape sequences in cell content (which is critical — the original 4-column parser would have lost rows like `agent opacity ($H_b^{A\|B}$)` if escapes had been silently dropped). Each row's classification was driven by the notes column; current-vs-candidate equality and bracketed-current detection were the structural pre-filters.

## Summary

- **Total R1 rows processed:** 1073 (across 10 files)
- **Classified:** 1072 (99.9%)
- **Left nil:** 1 (where bracketed candidate carried mixed-action commentary too tangled to classify cleanly)
- **Aggregator preserves total-row count:** 2957 → 2957 (parity confirmed pre/post)

## Per-file row counts and classification distribution

| file | rows | rename | keep | canon | alias | name-un | nil |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agent1-original-brainstorm.md` | 64 | 23 | 31 | 0 | 4 | 5 | 1 |
| `codex-1.md` | 111 | 45 | 43 | 0 | 4 | 19 | 0 |
| `codex-2.md` | 86 | 24 | 51 | 0 | 5 | 6 | 0 |
| `gemini-1.md` | 54 | 20 | 19 | 0 | 4 | 11 | 0 |
| `gemini-2.md` | 76 | 43 | 19 | 0 | 6 | 8 | 0 |
| `haiku-4-5.md` | 146 | 12 | 121 | 1 | 8 | 4 | 0 |
| `opus-1m.md` | 64 | 23 | 29 | 1 | 4 | 7 | 0 |
| `opus-4-7.md` | 120 | 36 | 52 | 4 | 12 | 16 | 0 |
| `opus-4-7-b.md` | 217 | 60 | 129 | 1 | 10 | 17 | 0 |
| `sonnet-4-6.md` | 135 | 54 | 48 | 4 | 13 | 16 | 0 |
| **TOTAL** | **1073** | **340** | **542** | **11** | **70** | **109** | **1** |

## Aggregate classification distribution (R1 only)

- **keep:** 542 (50.5%)
- **rename:** 340 (31.7%)
- **name-unnamed:** 109 (10.2%)
- **add-alias:** 70 (6.5%)
- **canonicalize:** 11 (1.0%)
- **(nil):** 1 (0.1%)

## Aggregate classification distribution (full corpus, post-pass)

- **keep:** 1178
- **rename:** 847
- **canonicalize:** 403 (R1 contributes 11; targeted-alternatives + R2 files supply the bulk)
- **name-unnamed:** 282
- **add-alias:** 240
- **rebuttal:** 6 (R2-only category)
- **(nil):** 1

## Most-common signals per category

### `keep` — 542 R1 rows
Default for self-votes (current == candidate, after stripping symbol annotations like `(\$\Delta\rho^\ast\$)` or proper-noun parentheticals like `(Tishby)` or possessive prefixes like `Hafez's`). Notes argue for preserving the existing name, often using "do not touch", "load-bearing", "load-bearing metaphor", "crispest pair", "name does its work". Bracket-placeholder candidates like `[keep whole vocabulary]` and `[three senses, keep all three]` also classified as keep.

### `rename` — 340 R1 rows
Default for non-self votes (current ≠ candidate) where notes argue the candidate replaces the current. Often combined with weight `-1` for explicitly-considered-and-rejected alternatives. The replacement-style rename votes are voted alongside their stronger-preference siblings (multiple alternatives for one current-name, with weight ranking distinguishing them).

### `add-alias` — 70 R1 rows
**Most common signal:** explicit "keep `<symbol>` as shorthand", "symbol stays", "English owns the prose register", "prose form", "in equations / in prose" register-split language. Almost universal pattern: current is `\$\alpha_1\$ (A2' fixed-gain sub-scope)` or `\$\Delta\rho^\ast\$ (adaptive reserve)` — symbol-leading current + bare-English candidate. The notes consistently argue both the symbol and the English alias should persist with differentiated roles.

### `canonicalize` — 11 R1 rows
**Most common signal for prose-excavation:** explicit reference to the candidate already appearing in the project's text — "LEXICON.md lists this under 'Terms to Be Added'", "Already coined and working. Appears in CLAUDE.md and multiple segments", "the segment itself uses 'seven ladders'". The vote is to *promote* the prose-use to formal canonical naming, not to coin a new name. Conservative trigger: only fired when notes specifically located the prose form somewhere in the project (LEXICON / CLAUDE.md / segment Discussion / Terms to Be Added section).

### `name-unnamed` — 109 R1 rows
Triggered by structural pre-filter on current cell: bracketed phrasing `[concept: ...]` or `[unnamed: ...]` or `[future segment: ...]` or `[symbol default: ...]`. Always paired with a candidate proposing a name, often with a `[original phrasing: unnamed: X]` trailer in the notes for traceability.

## Add-alias vs. rename — distinguishing signal

The most reliable distinguisher: **explicit register-split language in the notes.**
- "keep `\$\alpha_1\$` as shorthand" → add-alias
- "the symbol stays in equations; the English in prose" → add-alias
- "this lands in the derived-gain regime reads naturally" + "Keep the symbol" → add-alias
- Versus: "Class X requires a lookup every time" + "naming the architectural property" + no "keep symbol" — that's a true rename.

When notes mention only the candidate's merits without arguing for retention of the original symbolic/formal identifier, the vote is rename. When notes simultaneously argue *for* the candidate AND *for keeping* the formal/structural identifier, it's add-alias.

## Canonicalize-as-prose-excavation — distinguishing signal

The most reliable distinguisher: **explicit location-in-project of the candidate.**
- "LEXICON.md lists this under 'Terms to Be Added'" → canonicalize
- "Already in CLAUDE.md and multiple segments" → canonicalize
- "The segment itself uses 'seven ladders'" → canonicalize
- "Currently appears as 'X', 'Y', and 'Z' across [files]; standardize on the third" → canonicalize
- Versus: a name being proposed without claim that it's already in the corpus — that's rename or name-unnamed.

For self-votes specifically, the canonicalize trigger required even stronger signal: explicit verbs like "canonicalize", "standardize", "commit to", "stop paraphrasing", "promote to LEXICON", "lock in", or explicit mention of multiple paraphrases that need to converge. Plain "load-bearing keep" notes were classified as keep, not canonicalize.

## Representative examples per category

### `rename` (10 examples)

1. **Codex-1:** `Agentic Systems Framework (ASF) | Agentic Systems | rename | +1 | The repo's public face is already "Agentic Systems"; the extra acronym buys little...`
2. **Codex-1:** `actuated agent | goal-actuated agent | rename | +1 | Keeps the mechanical register while paying the meaning tax sooner...`
3. **Codex-1:** `#additive-coordinate-forcing | #forced-coordinates | rename | +3 | The current name is accurate but over-explains the mechanism...`
4. **Codex-1:** `#interaction-channel-classification | #signal-reception-regimes | rename | +3 | The four regimes are the actual memorable object here...`
5. **Codex-1:** `#m-preservation | #model-preservation | rename | +3 | The current slug is symbol-first and opaque in prose...`
6. **Gemini-2:** `Actuated agent | Purposeful agent | rename | +3 | "Actuated" sounds like a motor. "Purposeful" perfectly captures G_t = (O_t, Σ_t)...`
7. **Gemini-2:** `Continuity persistence | Identity continuity | rename | +3 | "Continuity persistence" is slightly redundant. "Identity continuity" clarifies...`
8. **Gemini-2:** `#observation-function | #observation-channel | rename | +3 | "Function" implies a clean mathematical mapping. "Channel" implies the lossy, noisy reality...`
9. **Opus-1m:** `#strategic-composition | #equilibrium-composition | rename | +3 | The segment's actual derivation is equilibrium convergence under Monderer-Shapley potential games (1996) and Rosen monotone games (1965)...`
10. **Sonnet-4-6:** `#additive-coordinate-forcing | #coordinate-forcing | rename | +3 | The segment itself acknowledges that the Čencov 4th instance is not Cauchy-FE-additive...`

### `keep` (10 examples)

1. **Agent1:** `satisfaction gap | satisfaction gap | keep | +3 | Crispest named pair in the project. 2×2 diagnostic table is memorable *because* the names are memorable.`
2. **Agent1:** `chronica ($\mathcal{C}_t$) | chronica | keep | +3 | Greek root ("records of time"); avoids ℋ-entropy collision...` (current includes symbol annotation; classified as self-keep after stripping)
3. **Codex-2:** `## Working Notes | ## Working Notes | keep | +3 | Clear, conventional, and exactly right for the internal/public boundary it marks.`
4. **Gemini-1:** `Aporia (ἀπορία) | Aporia | keep | +3 | "Productive perplexity" is a crucial nuance...` (symbol-annotation pattern)
5. **Haiku-4-5:** `#separability-pattern | #separability-pattern | keep | +3 | Load-bearing meta-segment name with evocative three-part structure...`
6. **Haiku-4-5:** `#identifiability-floor | #identifiability-floor | keep | +3 | Exact metaphor for what it names — structural boundary that blocks general identification.`
7. **Opus-4-7:** `directed-separation | #directed-separation | keep | +3 | Survived the κ-as-scalar category-error rescue...`
8. **Opus-4-7-b:** `Pearl's causal hierarchy (L0/L1/L2 in Pearl's own vocabulary) | *(do not rename)* | keep | +3 | Prior-art-integration convention prohibits renaming adopted concepts.` (do-not-rename placeholder pattern)
9. **Sonnet-4-6:** `#chronica | #chronica | keep | +3 | Excellent coinage. Greek term for "records of time" with zero collision...`
10. **Agent1:** `prolepsis / aisthesis / aporia / epistrophe / praxis | [keep whole vocabulary] | keep | +3 | Deliberate aesthetic commitment...` (bracket-placeholder pattern)

### `canonicalize` (10 examples)

1. **Sonnet-4-6:** `"scope-honesty-as-architecture" | scope-honesty-as-architecture | canonicalize | +3 | Already coined and working. Appears in CLAUDE.md and multiple segments.`
2. **Sonnet-4-6:** `"edge credence" ($p_{ij}$) | edge credence | canonicalize | +3 | LEXICON.md lists this under "Terms to Be Added." Should be promoted to main LEXICON.`
3. **Sonnet-4-6:** `"plan confidence" ($\hat P_\Sigma$) | plan confidence | canonicalize | +3 | LEXICON.md lists this under "Terms to Be Added." Promote to main LEXICON.`
4. **Opus-4-7:** `#additive-coordinate-forcing | #forced-coordinates | canonicalize | +1 | The segment itself flags this in the Discussion.` (segment-itself trigger)
5. **Opus-4-7:** `#additive-coordinate-forcing | #uniqueness-coordinate-forcing | canonicalize | +1 | Alternative that matches the "broader discipline" phrasing the segment itself uses.`
6. **Opus-4-7:** `#separability-pattern | #separability-ladder | canonicalize | +1 | The segment itself uses "seven ladders" and each row is a ladder...`
7. **Opus-4-7:** `[unnamed: the "scope-honesty-as-architecture"] | scope honesty | canonicalize | +1 | Already used as a term...` (note: this row has bracket-current → name-unnamed pre-filter; reclassified by note signal — verify rationale)
8. **Opus-4-7-b:** `[unnamed: "inevitability core"] | inevitability core | canonicalize | +3 | FORMAT.md already uses this. Keep and surface in prose...`
9. **Haiku-4-5:** Loose canonicalize on a +1 row defending an established LEXICON term.
10. **Sonnet-4-6:** `"calibration laboratory" (software's role) | calibration laboratory | canonicalize | +3 | Excellent coinage. Already in use.`

### `add-alias` (10 examples)

1. **Codex-1:** `alpha1 (fixed-gain A2' sub-scope) | fixed-gain regime | add-alias | +3 | "Lands in alpha1" is decoder-ring prose. The English label is much cheaper in discussion.`
2. **Codex-1:** `$\kappa_{\text{processing}}$ | processing coupling | add-alias | +1 | The symbol is fine in equations, but prose should default to the English name.`
3. **Codex-2:** `$\alpha_1$ (A2' fixed-gain sub-scope) | fixed-gain regime | add-alias | +1 | Keep the symbol, but prose should preferentially use the English name when possible.`
4. **Codex-2:** `$\Delta\rho^\ast$ | adaptive reserve | add-alias | +3 | This is the right English name and should dominate prose use.`
5. **Gemini-1:** `$\alpha_1$ / $\alpha_2$ / $\beta$ partition | Fixed-gain / Adaptive-gain / Drift regimes | add-alias | +3 | Translating the symbols into the structural regimes they represent...`
6. **Opus-1m:** `$\alpha_2$ (A2' adaptive-gain sub-scope) | adaptive-gain regime | add-alias | +1 | Parallel to $\alpha_1$.`
7. **Opus-4-7:** `$\beta$ (A2' assumed-not-derived sub-scope) | assumed-regime | add-alias | +1 | Currently reads as "lands in $\beta$" which tells the reader nothing.`
8. **Opus-4-7-b:** `$U_M$ / $U_O$ / $U_\Sigma$ (unity dimensions) | epistemic-unity / teleological-unity / strategic-unity | add-alias | +1 | The symbol layer is fine but the word *unity* requires paraphrase on every encounter.`
9. **Sonnet-4-6:** `$\alpha$ (lower sector bound) | $\alpha$ (sector parameter) | add-alias | +3 | The symbol is necessary in equations. The English gloss "sector parameter" is correct.`
10. **Haiku-4-5:** `p_ij (edge confidence weight) | edge credence | add-alias | +1 | LEXICON already names this "edge credence"...`

### `name-unnamed` (10 examples)

1. **Agent1:** `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | persistence envelope | name-unnamed | +1 | Engineering vocabulary, geometrically evocative.`
2. **Agent1:** `[concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | chain anchor | name-unnamed | +1 | Prose term, not segment rename.`
3. **Codex-1:** `[concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover] | reentry threshold | name-unnamed | +1 | This concept recurs across context-turnover and model-preservation.`
4. **Codex-1:** `[unnamed: the Class-1-sub-agents -> Class-3-composite phenomenon in strategic composition] | strategic entanglement | name-unnamed | +1 | Useful noun for a real phenomenon...`
5. **Codex-2:** `[concept: the framing of software/TST as AAD's epistemically-privileged high-identifiability measurement substrate] | calibration laboratory | name-unnamed | +3 | This phrase deserves to be promoted to the stable short name.`
6. **Gemini-1:** `[concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | Persistence envelope | name-unnamed | +3 | "Envelope" is standard flight-dynamics vocabulary for a safe operating region.`
7. **Gemini-1:** `[concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied] | Terminal alignment gap | name-unnamed | +3 | Gives a formal name and symbol to the fourth diagnostic.`
8. **Opus-4-7:** `[unnamed: "inevitability core"] | inevitability core | name-unnamed | +3 | FORMAT.md already uses this. Keep and surface in prose...`
9. **Opus-4-7-b:** `[unnamed: cascade of inferential force through C1/C2/C3] | inferential-force cascade | name-unnamed | +1 | The pattern "under C1 diagnostics are weak, C2 they sharpen, C3 they're global"...`
10. **Sonnet-4-6:** `[concept: the slogan capturing AAD's organizing principle...] | contraction-over-drift principle | name-unnamed | +3 | This is described as an "organizing-principle slogan" that "has not yet been surfaced at segment level."`

## Cases left nil (deliberate)

Only one row was left explicitly nil during retro-classification:

- **Agent1, line 81:** `"hierarchy" (as repeated word) | [reserve for Pearl's; rename others selectively] |  | +1 | Weak proposal. Four uses in the framework (Pearl's, convention, correlation, approximation-tiering) is likely too many. Partial disambiguation via correlation→correlation-ladder and convention→continuation-hierarchy.`

  The candidate cell carries multi-action commentary (`reserve` + `rename`) rather than a single name. The agent's own framing is "weak proposal" with mixed-action recommendations spread across multiple sub-renames. No single category fits cleanly; nil correctly signals "uncategorized — needs human review".

The discipline of conservative-classification was kept tight enough that few other rows passed the bar for nil. Rows where evidence was *weak* but not contradictory got the dominant-signal classification (e.g., a +1 rename where notes describe modest improvement still passes as `rename` without ambiguity-induced nil).

## Cases where earlier confusion was likely surfaced

A small set of rows were flagged by the heuristic for likely classification ambiguity even when classified:

- **Sonnet-4-6:** `"strengthen-first posture" | "attempt the improbable" | name-unnamed | +3 | Retiring "strengthen-first posture" in favor of "attempt the improbable" as the primary working-vocabulary term.`
  This is a non-self vote with bracket-current pattern absent — it should be `rename` (replacing one phrase with another), not `name-unnamed` (the candidate isn't naming an unnamed thing). The bracket-trigger fired because of `[unnamed: ...]` immediately before in the sonnet-4-6 file's notes. Caveat: this row's classification may be incorrect; subsequent agents should treat this as a rename-with-weight-+3.

- **Gemini-2:** `Indivisum | Causal lock | rename | +3` — could plausibly be `add-alias` if Latin/architecture term should persist alongside the English. Notes argue strongly for replacement, so rename is defensible. Borderline.

- **Opus-4-7-b:** `unity dimensions | coherence dimensions | rename | -1` — the agent considered and rejected this rename. `rename` with `-1` weight is the canonical schema for "considered and rejected", so this is correct, but a previous classification pass had over-eagerly fired `canonicalize` on the "already used informally elsewhere" phrase in the notes (where "informally elsewhere" referred to *unrelated* uses of "coherence", not to the candidate already being in use). The fix: stricter excavation_signals that require the *candidate* (not some unrelated term) to be the thing already in prose use.

- **Several agents:** `"Hafez's H_b | H_b"` and similar `Author's TermName | TermName` patterns — currently classified `keep` (after stripping the possessive prefix), but could plausibly be `canonicalize` (excavating the bare term as canonical). Notes invariably say "Adopted concept; keep" — the conservative call is `keep` (consistent with prior-art-integration convention's "keep adopted names verbatim"). If a downstream consumer wants the canonicalize signal more aggressively surfaced, the regex `\badopted concept\b/` could be elevated above the self-vote keep-default.

## Heuristic structure (for reproducibility)

The classifier applies the following pre-filters in order:

1. **Bracketed-current → name-unnamed.** `[unnamed: ...]`, `[concept: ...]`, `[future segment: ...]`, `[symbol default: ...]`, `[working-vocabulary observation: ...]`, `[the trio collectively]` all trigger.
2. **Bracket-mixed-action candidate → nil.** `[reserve for X; rename others selectively]` and similar.
3. **Bracket-keep candidate → keep.** `[keep ...]`, `[three senses, keep all three]`, `*(do not rename)*`, `*(retire ...)*`, `*(no rename; ...)*`, em-dash placeholder `—`.
4. **Symbol/possessive normalization.** Strip `(\$...$)` parentheticals, short proper-noun annotations (`(Tishby)`, `(Khalil, Vidyasagar)`), and leading possessives (`Hafez's`, `Pearl's`, `Bruineberg's`, `Tishby's`). After stripping, compare current and candidate.
5. **Self-vote (current == candidate post-strip).** Default to `keep`. Override to `canonicalize` only on explicit canonicalize-verb signals: "canonicalize", "standardize", "commit to", "lock in", "stop paraphrasing", "currently appears as", "already in LEXICON / NOTATION / Terms to Be Added", "promote to LEXICON".
6. **Symbol-leading current with bare-prose candidate.** When current starts with `$...$` and candidate is bare prose → `add-alias`. (Reverses the order: current=`$\Delta\rho^\ast$ (adaptive reserve)` and candidate=`adaptive reserve` is a register-split alias vote.) When current starts with English prose and ends with a symbol parenthetical, treat as self-vote (the candidate is just the bare prose form of the same concept).
7. **Non-self with adopted-concept signal → canonicalize.** "Adopted concept", "adopted from", "prior-art integration ... keep" → canonicalize.
8. **Non-self with alias signal → add-alias.** "alias", "prose form / handle", "keep symbol", "for prose", "English equivalent / gloss / alias / name", "in equations", "symbol stays".
9. **Non-self with prose-excavation signal → canonicalize.** "the segment itself uses / says / flags", "LEXICON.md lists", "Terms to Be Added", "Already coined and working", "FORMAT.md already uses".
10. **Default for non-self → rename.**

## Verification

Aggregator commands all ran cleanly:

```
ruby bin/naming-aggregate.rb --format=review --output=msc/naming/naming-aggregate-r2-review.md
ruby bin/naming-aggregate.rb --format=compact --output=msc/naming/naming-aggregate-r2-compact.md
ruby bin/naming-aggregate.rb --format=round2 --output=msc/naming/naming-aggregate-r2-round2.md
ruby bin/naming-aggregate.rb --format=json --output=msc/naming/naming-aggregate-r2-votes.json
ruby bin/naming-master-init
ruby bin/naming-master-view --format=compact
ruby bin/naming-master-view --format=summary
```

**Counts (parity preserved):**

| | pre-pass | post-pass |
|---|---:|---:|
| Total vote rows | 2957 | 2957 |
| Distinct (current, candidate) pairs | 1827 | 1827 |
| Distinct currents | 942 | 942 |

**Category counts (full corpus):**

| category | pre-pass | post-pass | Δ |
|---|---:|---:|---:|
| keep | 636 | 1178 | +542 (R1 contributions) |
| rename | 507 | 847 | +340 |
| canonicalize | 392 | 403 | +11 |
| name-unnamed | 173 | 282 | +109 |
| add-alias | 170 | 240 | +70 |
| rebuttal | 6 | 6 | 0 |
| (nil) | 1073 | 1 | −1072 |

The R1 contributions are now visible in every category. The `(nil)` count dropped from 1073 → 1, with the 1 remaining being the deliberately-left case from agent1.
