# Naming Pilot — Rename Mapping Details

Live record of specific rename mappings for the role-prefix pilot workstream.
This file is **excluded** from `bin/rename-slug`'s substitution patterns
(`msc/naming/` directory-prefix exclusion in `EXCLUDED_DIR_PREFIXES`) so the
mappings below survive future renames verbatim and remain legible as a
historical record of which names were executed.

See [`PRACTICA.md`](../../PRACTICA.md) §"🌟 Current naming conventions refactor"
for the surrounding strategic pipeline and [`TODO.md`](../../TODO.md) §"Naming
pipeline — specific deferred items" for the specific subject-noun renames
queued for the refined Round 1 → Round 2 workflow.

## Landed — role-prefix pilot complete (2026-04-23)

| Date       | Old slug                        | New slug                                 | Executed by       | Notes |
|------------|---------------------------------|------------------------------------------|-------------------|-------|
| 2026-04-23 | `ai-agent-as-act-agent`         | `scope-logogenic-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; taxonomy-conformant (logogenic is the class). Type: `definition` → `scope`; H1 + formal tag updated. |
| 2026-04-23 | `developer-as-act-agent`        | `scope-developer-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; covers human AND AI developers in the software context (not narrowed to humans). Type: `definition` → `scope`; status: `exact` → `axiomatic` (resolves Finding 14 Option A); H1 + formal tag updated. |
| 2026-04-23 | `composition-scope-condition`   | `scope-composite-agent`                  | `bin/rename-slug` | Prefix + subject-noun; subject class is the composite agent, not the "condition". H1 + formal tags + prose references updated. |
| 2026-04-23 | `scope-condition` *(split)*     | `scope-adaptive-system` + `scope-agency` | manual + `bin/rename-slug` | Semantic split. The original segment defined two nested scopes ($\mathcal{S}_\text{adaptive}$ and $\mathcal{S}_\text{agency}$); downstream segments depend on one or the other, not on an abstract "condition". Executed as: script-driven rename to `scope-agency` (majority case), hand-authored `scope-adaptive-system.md` with adaptive content, 6 hand re-routings for adaptive-dependent files, one split-reference cleanup in `causal-structure.md`. |
| 2026-04-23 | `identifiability-floor`         | `discussion-identifiability-floor`       | `bin/rename-slug` | Pure role-prefix add; subject-noun already strong. |
| 2026-04-23 | `separability-pattern`          | `discussion-separability-pattern`        | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `separability-ladder` (Round-1 consensus) deferred to refined Round 1 + Round 2. |
| 2026-04-23 | `additive-coordinate-forcing`   | `discussion-additive-coordinate-forcing` | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `forced-coordinates` (Round-1 consensus; addresses Čencov-instance scope-honesty concern) deferred to refined Round 1 + Round 2. |

Seven slug changes total, one of which (scope-condition) was a 1:2 semantic split.
Nine total segment files moved or created; 01-aad-core lint-clean after every step.

## Landed — first align-slug batch (2026-04-24)

Three pure-prefix alignments landed via `bin/align-slug`, validating the wrapper and extending the role-prefix discipline to representative segments of three type categories.

| Date       | Old slug                  | New slug                            | Type      | Executed by       |
|------------|---------------------------|-------------------------------------|-----------|-------------------|
| 2026-04-24 | `agent-identity`          | `scope-agent-identity`              | scope     | `bin/align-slug`  |
| 2026-04-24 | `composition-consistency` | `postulate-composition-consistency` | postulate | `bin/align-slug`  |
| 2026-04-24 | `mismatch-decomposition`  | `result-mismatch-decomposition`     | result    | `bin/align-slug`  |

All three: pure role-prefix add (subject-noun preserved); H1 and formal tags updated by hand.

## Candidates — pending role-prefix alignment

Not yet aligned; align-slug will handle each mechanically. Pure prefix add for all:

- `sector-condition-stability` (type=result) → `result-sector-condition-stability`
- `mismatch-dynamics` (type=hypothesis) → `hypothesis-mismatch-dynamics`
- `recursive-update` (type=derived) → `derived-recursive-update`
- plus the remaining ~110 unprefixed slugs; a future dedicated cycle runs `bin/align-slug --all` once the TYPE_TO_PREFIX mapping is finalized and segments' `type:` frontmatter is audited for correctness.

Separately-deferred (subject-noun changes, not pure prefix — belong to refined Round 1 / Round 2):

- `graph-structure-uniqueness` → `#derivation-strategy-dag-sufficiency` (subject-noun substitution from "graph-structure-uniqueness" to "strategy-dag-sufficiency").
- `recursive-update-derivation` — pure prefix would yield `derivation-recursive-update-derivation` (awkward trailing "derivation"); wants subject-noun cleanup first.

## Deferred to refined Round 1 / Round 2

Subject-noun substitutions on the three meta-segments surfaced in Round 1 as
consensus renames but deserve the voting process rather than ad-hoc landing
during the role-prefix pilot. They are:

- `discussion-separability-pattern` → `discussion-separability-ladder` (Round-1 consensus; "ladder" more evocative than "pattern" for the three-rung shape).
- `discussion-additive-coordinate-forcing` → `discussion-forced-coordinates` (Round-1 consensus; current "additive" does not cover the Čencov-Fisher instance).
- A future broader pass over all non-role-prefix slugs (the subject-noun sweep that the pilot was meant to pave the way for).

## Pending subject-noun renames — surfaced post-R2 (2026-05-04+)

Subject-noun substitutions identified during the canonicalize-list curation pass that pulls from the R2-closed master list. These don't need re-voting — they're either segment-self-affirming (the segment's own formal expression already names the more specific concept) or already-resolved by slug discipline elsewhere and just want the segment to catch up.

- `scope-software` → `scope-evolving-software` (2026-05-04). Segment's formal expression already names the scope $\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\}$ and the Discussion uses "evolving systems" as the canonical prose form. The bare "software" subject-noun under-specifies (suggests all software; actual scope is *evolving* software where the developer-agent has a non-trivial adaptation problem). The stable-subsystem corollary in the same segment exits the scope precisely when systems are *non-evolving* ($\rho \to 0$). Adjacent-literature anchor: software-evolution research (Lehman's laws and successors) is the intended prior-art neighborhood. Citability test (criterion 9 in `doc/naming-principles.md`) currently fails on bare `software` and passes on `evolving-software`. Surfaced during canonicalize-list review (`msc/naming/to-canonicalize.md`, row 104, since removed from that list).

## Vocabulary commitments — non-slug, LEXICON + prose-pass (2026-05-04+)

These are vocabulary decisions where the operational landing is a LEXICON entry plus a prose-cleanup sweep across segments that currently reference the legacy form. They do *not* require `bin/rename-slug` because the legacy form is not a slug — it's prose vocabulary. Listed here for the same reason as slug renames: the historical record of what was decided, when, and why.

- **Class 1 / 2 / 3 → Separated / Coupled / Partial; family/axis = "Goal-Update Coupling Class"** (2026-05-04). The numbered classes in `#der-directed-separation`'s architectural taxonomy are renamed in prose to named-property labels. The axis collectively is the **Goal-Update Coupling Class** — measured by $\kappa_{\text{processing}}$ in engineered systems, pattern-attributable in biological systems. Naming rationale: the axis values name the *property the axis measures* (the directed-separation property of `#der-directed-separation`), not an architectural realization of it. `Separated` directly echoes the segment-derived property; a tightly-integrated system that happens to be goal-blind is also Separated. Resolves the contested-decision cluster surfaced in `r2-patterns.md` §3c (where the R2 cohort split across competing English-modifier slates: Modular/Merged/Scaffolded vs Modular/Integrated/Partially-coupled vs Modular/Coupled/Partially-modular). Chosen over those candidates because it works at the property layer, not the architectural-realization layer.

  *Operational landing:*
   1. LEXICON entry for "Goal-Update Coupling Class" with the three values, brief gloss of each, and pointer to `#der-directed-separation`.
   2. Prose-cleanup pass through segments that currently use Class 1/2/3 framing. Primary segments to touch: `01-aad-core/src/der-directed-separation.md` (canonical home — introduces the named-property framing), `01-aad-core/src/scope-observation-ambiguity-modulation.md` (cross-component reference), `01-aad-core/src/deriv-bias-bound.md` (bias-bound derivation references Class 2 throughout), `01-aad-core/src/result-section-ii-survival.md` (Class 1/2/3 survival classification). README's *Position & Lineage* and *Maturity Gradient* paragraphs also reference Class 1/2/3 in passing.
   3. Numbered backup retained where pedagogically useful: prose may read "**Separated** (Class 1)" on first use, then "Separated" thereafter. The numbered form is an aid for readers familiar with the prior framing, not the canonical form.
   4. The full ontology lattice in which this axis sits (Semantic Tier × Knowledge Type × Goal-Update Coupling × Arity) is under separate review in `msc/domain-unification-2026-05-04/`. The Separated/Coupled/Partial naming lands independently of whether the broader ontology lattice is ratified — the axis itself is well-defined and the naming improves the existing framing regardless of how the surrounding ontology evolves.

- **"Knowledge Type" family/axis name with Static / Learning attributes** (2026-05-04). Names the agent-classification axis that distinguishes systems whose causal mapping is fixed at design time (**Static**) from those that acquire or refine interventional structure during operation (**Learning**). Already in use across `doc/DOMAINS.md`'s mapping table; the commitment here is to elevate it from working-table convention to LEXICON-canonical vocabulary. Naming rationale: "Knowledge Type" describes what the axis measures — the *kind of knowledge* the agent carries — at the right level of abstraction. Citability: the bare term is generic, but the compound *"Knowledge Type axis"* / *"Knowledge Type: Static"* is project-distinctive enough in context. The two attribute names (Static / Learning) are concise, antonymous, and avoid loading false familiarity from "online/offline" (which carries deployment-context baggage) or "fixed/adaptive" (where "adaptive" overloads with the Tier 1 *Adaptive system* class).

  *Operational landing:*
   1. LEXICON entry for "Knowledge Type" axis with the two values and a one-line gloss of each. Pointer to where the axis becomes definitionally relevant (currently activates at Tier 2 in the proposed ontology; per refinement (b) in `recommended-agent-ontology.md`, Static can apply at Tier 3+ as well — wording should reflect this once ratified).
   2. Prose-discipline note: avoid "online/offline" and "fixed/adaptive" as synonyms in formal prose. The Knowledge Type axis is the canonical vocabulary; informal paraphrases drift the framing.
   3. Lands together with the Goal-Update Coupling Class entry above as part of the same systematic LEXICON pass — both are vocabulary commitments at the agent-classification layer.
   4. As with the Coupling axis, the Knowledge Type axis is currently part of the broader four-axis ontology under separate review in `msc/domain-unification-2026-05-04/`. The naming commitment lands independently; the axis-activation-tier and edge cases (e.g., refinement (b) on Static at Tier 3+, fixed-vs-learned collapsing into model-class capacity at Tier 1) are second-opinion items pending Joseph's review.

## Deferred / resolved separately

- The `aad-agent` vs `adaptive-agent` family debate was superseded by the
  taxonomy-conformant move to `scope-logogenic-agent` and `scope-developer-agent`.
  No remaining open question on these two destinations.
- `ASF` vs `Agentic Systems Framework` umbrella naming — Round 1 agents misread
  `ASF` as debt when it is the intentional parent-level name (AAD is Part I;
  TST is Part II). Re-surface in refined Round 1 with correct framing.

## Methodology forward — split role-prefix from subject-noun

**Going forward, role-prefix addition and subject-noun renaming are distinct operations executed in separate passes.** Joseph's 2026-04-24 clarification: do the file+tag change of prefixing the type as one mechanical pass, then execute subject-noun renames independently afterward. Reasons:

- Role-prefix addition is mechanical. Given a segment file with a known `type:` frontmatter value, the slug prefix is determined. No voting, no judgment, no content rewriting of conceptual vocabulary. The prefix change is idempotent under `bin/rename-slug` with no content-integrity risk.
- Subject-noun renaming is judgment. Changing what a segment is *called as a concept* (pattern vs ladder, additive-coordinate-forcing vs forced-coordinates) needs multi-agent voting, scope-honesty review, and usually prose rewriting inside the segment to keep the segment's self-presentation coherent with its new name. This process belongs in the refined-Round-1 → Round-2 → collision-audit → landing pipeline.

Bundling them in one pass (as the pilot briefly attempted for two meta-segments) creates two failure modes: (i) the rename script appears to succeed while the segment's prose has become internally inconsistent; (ii) subject-noun judgment gets entangled with prefix mechanics and voters can't vote cleanly on the noun choice.

When the full-sweep role-prefix pass lands (the ~120 remaining slugs), it should be a dedicated cycle that applies prefix additions mechanically without touching subject-nouns. Subject-noun work picks up in its own cycle after — informed by the refined Round 1 and Round 2.

## Pilot-validation observations (worth folding into refined Round 1 principles)

- **Role-prefix reads cleanly in cross-references.** `#scope-agency`, `#scope-composite-agent`, `#discussion-identifiability-floor` etc. read naturally in prose and sharpen the dependency graph. No awkward cases surfaced.
- **Semantic splits require hand work, not script.** The `scope-condition` split was worth it (the old name named nothing), but needed segment-authoring + per-reference classification. Tooling can assist on the bulk rename; the split judgment is irreducibly manual. Recommend: keep `bin/rename-slug` as a 1:1 tool only.
- **Formal-tag labels don't auto-update.** Tags like `*[Definition (slug)]*` embed the slug as a literal string. The mechanical rename doesn't touch them; `bin/rename-slug`'s stale-text scan surfaces them as warnings and the executing agent updates by hand. Low-cost convention.
- **H1 / opening-sentence framing drift.** Slug changes from `definition` to `scope` type imply H1 shifts (`# Definition: X as AAD Agent` → `# Scope: X Agent`) that the regex cannot detect. The "review the moved file" framing reminder in `bin/rename-slug` output is the right UX.
- **Script batch-mode re-planning.** Early batches failed when a later pair's edit list referenced a file that an earlier pair had already moved. Fix landed in this commit: re-plan each pair immediately before applying. Documented inline in the script.

## Why this file exists separately from TODO.md

`bin/rename-slug` performs global regex substitutions across live repo content.
TODO.md is live — references in its body must update with the rename. But a
*table of rename mappings themselves* would be catastrophically corrupted by
a rename sweeping through it (the old-slug column would get rewritten to match
the new-slug column). So rename-specific tables live here, and the script's
`msc/naming/` directory-prefix exclusion (`EXCLUDED_DIR_PREFIXES` in
`bin/rename-slug`) keeps this file — and all naming-cycle artifacts — frozen.

When a new rename lands or a pending row changes status, update this file by
hand.
