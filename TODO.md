# TODO — Deferred Organizational Items

## Project Structure

- **Root-level assembly index.** A root OUTLINE.md or INDEX.md that assembles the full "Agentic Systems book" — covering all sections including ACT core, composition, software, logogenic agents, and framework-level content. Deferred until there is organized AS content beyond ACT to assemble.

- **`framework/` directory.** For structured non-mathematical content: architectural guidance, engineering patterns, philosophical foundations (emergence conditions, identity sufficiency, constitutive choice). Currently this material lives informally in msc/ and msc/reflections/. Create when enough content warrants organization.

- **Multiple index support.** The `bin/build` tool can already assemble any outline file. Future indexes for specific outputs: a paper (Sections I+II), a preprint, a monograph, topical selections. Each would be its own OUTLINE file selecting and ordering a subset of segments.

## Content

- **~~Absorb agentic-tft content.~~** Done (2026-03-20). Eight design-relevant documents moved to `msc/agentic-tft-*.md` with origin notes and relevance pointers. Five superseded documents moved to `_obs/agentic-tft-*`. References updated in `03-logogenic-agents/OUTLINE.md` (source material table), `04-logozoetic-agents/OUTLINE.md`, `WORKBENCH.md`, and `CLAUDE.md`. The documents are *sources* for logogenic/logozoetic work, not yet distilled into segments — that distillation should happen when the scope of `03-logogenic-agents/` is decided.

- **Section IV standalone paper outline.** Fastest path to external credibility — no theoretical blockers, high internal coherence (84% self-contained dependencies). Draft outline exists at `msc/2026-03-14-section-iv-paper-outline.md`.

- **Promote segments past draft.** 89 segments at `draft`, zero past it. The 15-20 strongest segments in Sections I+II should be promoted to `candidate` stage.

## Section II Diagnostic Chain — Codex Review (2026-04-02)

Six issues identified by Codex automated review. Items 1-3 are HIGH priority (affect core diagnostic chain); 4-6 are MEDIUM.

1. ~~**HIGH — Q_O causal validity conditions on wrong state.**~~ **FIXED 2026-04-02.** Rewrote causal validity paragraph in value-object.md. Two mechanisms: (1) do-operator severs action-selection confounding from $G_t$, (2) continuation policy is a parameter. Under directed separation, $M_t$ alone is sufficient. Class 2 degradation cross-referenced.

2. ~~**HIGH — Orient cascade contradicts 2×2 diagnostic.**~~ **FIXED 2026-04-02.** Removed "if feasible" gate on step 3. Cascade now evaluates $\delta_{\text{regret}}$ regardless of $\delta_{\text{sat}}$'s sign, with all four 2×2 quadrants explicitly handled. Step 5 entry conditions clarified.

3. ~~**HIGH — Strategy-persistence overstates Prop B.5.**~~ **FIXED 2026-04-02.** Changed "Resolved" to "partially resolved." B.5 proves sector transfer to $\delta_s$ (plan-confidence error); transfer to $\delta_{\text{strategic}}$ (calibration residual) remains open and requires credit-assignment machinery.

4. ~~**MEDIUM — Composition bridge assumes extra contraction.**~~ **FIXED 2026-04-02.** Added caveat in tempo-composition.md that the connection depends on the bridge lemma's contraction assumption, which is not formally derived from (A4).

5. ~~**MEDIUM — A_O mixes full-policy and one-step attainability.**~~ **FIXED 2026-04-02.** Clarified in satisfaction-gap.md that $A_O$ inherits the continuation convention. Under canonical default, $A_O$ is best-first-action (one-step improvement), not full-policy optimum. Distinction made explicit.

6. ~~**MEDIUM — Graph-structure-uniqueness overclaims.**~~ **FIXED 2026-04-02.** Title/summary qualified: "DAG (exact), Markov conditional on causal sufficiency." OUTLINE entry updated to match.

## Tooling

- **Lint-md directory arguments.** Currently accepts file paths; could accept directory paths to lint all .md files within. Low priority.
