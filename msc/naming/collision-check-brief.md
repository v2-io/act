# Collision check — naming-cycle finalists

Brief for the agent doing the external-collision sweep on likely R2 finalists. Self-contained; readable cold.

## What we're doing

The Agentic Systems Framework (ASF) has been running a multi-round naming cycle. We're approaching Round 2 voting and want to sweep the likely-finalist list for external-world naming collisions before locking finalists in.

The concrete worry is the ACT → AAD precedent: the framework's mathematical core was originally called Agentic Cycle Theory (ACT), and on 2026-04-16 we discovered the AI welfare literature had recently established "AI Consciousness Test (ACT)" (Schneider & Turner). Forced rename mid-stream. We'd rather catch that pattern *before* committing this time.

The 47 candidates below are terms that are likely to survive R2 voting *and* where there's enough collision-suspicion in the prior to warrant a look. Some have known collisions we want verified; others are intuition-flags worth either confirming or relaxing. The list is calibration, not assignment — if you find candidates we should have flagged, raise them; if some on the list look obviously clean on first look, say so and move on.

## What's been excluded (and why)

Terms ASF deliberately adopts from prior art with citation are *not* on this list. Pearl's causal hierarchy, Tishby's information bottleneck, Lohmiller-Slotine contraction analysis, Holling's adaptive cycle (when used in Holling's sense), Boyd's OODA, Auftragstaktik, McClelland's complementary learning systems, Maturana's autopoiesis, Levitt-March competency trap, Tomasello's shared intentionality (when cited), the Greek-philosophy vocabulary (*aporia*, *prolepsis*, *aisthesis*, *epistrophe*, *praxis*) — adoption-with-citation is the discipline, not collision. The list below is restricted to terms ASF presents as its own coinage or its own framing.

A subtle case worth naming: when ASF coins a *compound* on top of an adopted term ("Pearl-blanket reading" extends "Markov blanket"; "orient cascade" extends Boyd's "orient"), the compound is the project's coinage and is in scope. The base term is not.

## What "collision" means here

The bar isn't "any external use of these words." It's: **how much confusion or consternation would a reader from adjacent literature experience if ASF published a public-facing artifact using this term tomorrow?** Two failure modes count:

1. **Semantic import mismatch** — a reader from field X reads the term, imports the established field-X meaning, and is now reasoning about ASF claims with the wrong frame. (E.g., "directed separation" being read as Pearl's *d-separation*; "cognitive fusion" being read as Hayes's ACT therapy concept.)

2. **Territorial step-on** — the term is closely associated with a specific researcher / school, and using it without acknowledgment looks like either ignorance or appropriation. (The ACT precedent: Schneider & Turner had recently established the term in AI welfare; we landed on it independently and looked sloppy until we renamed.)

Acronyms by themselves don't need this scrutiny — bare 3-letter strings collide constantly and that's fine. Pure non-overlap on the actual concept is what matters.

## What you're working with

- **Master list**: `msc/naming/master-list-curated.json` is the authoritative source. Each candidate has a `segment_link` field pointing to the segment that defines its ASF meaning, plus a `consolidated_rationale` summarizing why voters favored it. Read enough of these to actually understand what ASF means by each term — the collision check is meaningless without that grounding. (Compact view at `msc/naming/master-list-compact.md` if json is unwieldy.)
- **Repository context**: `CLAUDE.md` at the repo root has the framework overview; component `OUTLINE.md` files have section structure; `NOTATION.md` and `LEXICON.md` define vocabulary. Skim what helps; don't try to read everything.
- **The 47 candidates**: list below.

## Posture

Treat this like a literature search where you're the one with the most context after this run. We're checking your judgment, not auditing it — if you think a flagged candidate is fine, say so and explain. If you find something we didn't flag, raise it.

The 1M-context budget here means you can afford to read ASF's actual usage of each term carefully before searching. Shallow searches that don't know what ASF *means* by the term will produce a lot of false positives. The depth of your understanding is the bottleneck on the search quality, not the number of queries. Spend the tokens on understanding.

When ASF's usage is the same as / closely related to / unrelated to the external usage — that distinction is what separates "this is fine, just cite it" from "the meaning has drifted, we should rename." Surfacing that distinction is the deliverable.

## What's useful to come back with

A markdown report at `msc/naming/collision-check-2026-04-29.md` with:

- Per-candidate verdict: **severe** (rename or strongly disambiguate) / **moderate** (acknowledge in epistemic status, flag in lexicon, or cite-on-first-use) / **minor** (note for completeness, no action needed) / **clean** (no notable collision found).
- 1-3 sentence rationale citing the most relevant external usage(s) with source (paper, author, year, link or canonical pointer).
- Whether ASF's usage matches / is adjacent to / is unrelated to the external usage — this distinction matters more than the existence of a collision per se.
- A separate "Additional flags" section for anything you discovered that the list missed.
- A short "Calibration notes" section at the top if you think the bar should shift one way or the other after seeing the actual landscape.

The format above is a starting point — adjust if a different structure serves the work better.

## The 47 candidates with collision-suspicion notes

1. **directed separation** — Pearl's *d-separation* in causal graphical models is the dominant adjacent term
2. **orient cascade** — leans on Boyd's "Orient" stage; check the compound for prior usage
3. **control regret** — online learning / bandits / regret-minimizing control literature
4. **satisfaction gap** — possible CSP/SAT-solver, satisficing (Simon), management/HR senses
5. **chronica** — Latin medical *chronica*; historical chronicles; possibly biology
6. **identifiability floor** — *identifiability* heavily loaded in stats / causal inference
7. **adaptive reserve** — Crabtree-Miller-Stange *Practice Adaptive Reserve* (primary care medicine); also reliability/engineering
8. **calibration laboratory** — metrology / industrial calibration labs are literal things
9. **adaptive cycle** *(ASF's use)* — Holling's panarchy theory in ecology/resilience is heavily established; ASF's use is closer to OODA reframe; check whether the namespace clash is recoverable
10. **integrated agent** *(Class 2 finalist)* — Tononi's IIT framing of "integrated" is dominant
11. **modular agent** *(Class 1 finalist)* — modular-agent literature in agent-based modeling and modular RL
12. **scaffolded agent** *(Class 3 finalist)* — Vygotsky's scaffolding (developmental psychology); also instructional design
13. **proprium** — Gordon Allport's personality theory (1955)
14. **cognitive fusion** — Acceptance & Commitment Therapy (Hayes); central concept there with quite different meaning
15. **stability-plasticity window** — Grossberg's *stability-plasticity dilemma* in NN learning is foundational
16. **mismatch signal** — predictive coding *prediction error*; mismatch-negativity ERP in cognitive neuroscience
17. **action selection** — heavily used in RL & computational neuroscience (basal ganglia models)
18. **recursive update** — Bayesian recursive estimation; Kalman recursion
19. **update gain** — Kalman gain (control theory) is the dominant adjacent term
20. **agent opacity** — XAI / transparency literature uses "opacity" widely
21. **strategy DAG** — planning / game theory / strategic-graph literature
22. **shared intent** — Tomasello's *shared intentionality* (developmental psychology / social cognition)
23. **epistemic dead zone** — generic-sounding but check for established cognitive-science or epistemology use
24. **observability frontier** — control-theory observability is established; "frontier" might be ASF-specific
25. **observation infrastructure** — DevOps observability stack (Prometheus/Grafana/etc.)
26. **logogenic agent** — verify no established clinical / linguistic / philosophical usage
27. **logozoetic agent** — same; coined for the project, verify uniqueness
28. **the crèche** — Christmas/Catholic; French daycare; possibly AI-research uses
29. **honesty as architecture** — Anthropic Constitutional AI / "honest, helpful, harmless" framing
30. **agent identity** — philosophy of mind / personal identity literature
31. **moral continuity** — personal identity philosophy (Parfit, etc.)
32. **teleological unity** — philosophy of mind / functionalism / philosophy of biology
33. **epistemic architecture** — overloaded (epistemology + software architecture + cognitive architecture)
34. **artificial hippocampus** — neural memory architectures (Neural Turing Machine, MERLIN, Differentiable Neural Computer, etc.)
35. **goal-conditioned reconstruction** — *goal-conditioned* RL is a major active subfield
36. **separability ladder** — adjacent to Pearl's *ladder of causation*; also separability has uses in physics/ML
37. **closure defect** — group theory / category theory closure has technical meaning
38. **convention hierarchy** — Lewis's *Convention* (game theory / philosophy of language); also possibly type theory
39. **forced coordinate / additive coordinate forcing** — set-theory *forcing*; possibly physics constrained coordinates
40. **gain collapse** — control-theory closed-loop gain; ML training-instability sense
41. **evidence starvation** — Bayesian evidence; possibly clinical or epidemiological
42. **effective disturbance** — robust control / disturbance rejection
43. **causal information yield (CIY)** — combines two heavy terms (causal + information); verify the compound is novel
44. **inevitability core** — possibly novel; check
45. **self-referential closure** — adjacency to Maturana's autopoiesis; also possibly logic/foundations
46. **directional fidelity** — possibly novel; check signal-processing / control adjacency
47. **Pearl-blanket reading** — ASF coinage on top of adopted Markov-blanket concept; check whether "Pearl-blanket" is used elsewhere

## A note on this brief

What you decide to flag, how deeply you read each candidate, what query patterns you use, and how you weight different external sources are all your call — your judgment on the actual landscape is what makes this useful. The list above is calibration, not assignment. If 47 turns out to mean 35 (because some are clean on first scan and dwelling adds nothing) or 60 (because you found a dozen more that deserve flagging), that's the right call.

If you discover the bar is miscalibrated — too lax or too strict in light of what's actually out there — name that in the report. The next pass will benefit from knowing.
