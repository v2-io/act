#!/usr/bin/env python3
"""
Apply manually-written rationales to the 69 flagged candidates.

Each rationale follows the journalistic stance from pass-a-brief.md:
  - Surfaces the substantive arguments the exploration team made
  - Preserves dissent verbatim where load-bearing
  - Avoids consensus-signaling language
  - Numbers (vote distribution) live in the card, not the rationale

Keys are (current, candidate) tuples.
"""

import json
from pathlib import Path

PATH = Path('msc/naming/master-list-curated.json')

RATIONALES = {
    # Heavy keeps — the load-bearing canonical names. Each has 8+ defenders;
    # rationale articulates the *case* without surfacing the tally.

    ('control regret', 'control regret'):
        "Pair-partner with satisfaction gap; the two names jointly carry the 2×2 orient-cascade diagnostic decomposition. "
        "Defenders cite three load-bearing properties: the RL-baggage transfers correctly (regret = best-achievable − current), "
        "the modifier 'control' narrows the regret to the attainability layer of the diagnostic, and the pair survives the "
        "communal-imagination test on first encounter. The principles file uses this pair as the canonical illustration of "
        "'names that do work for the reader'; renaming either half would damage the matched compound. Variants like "
        "'strategy regret' or 'execution regret' appear in working notes but the established form is in NOTATION.md and LEXICON.md.",

    ('satisfaction gap', 'satisfaction gap'):
        "One half of the two-name 2×2 diagnostic with control regret; defenders describe it as the crispest named pair in "
        "the project. The argument is that the two-word compound tells the reader the diagnostic direction (objective met "
        "vs. unmet) immediately, so the disambiguation table organizes itself in the reader's head on first encounter. "
        "Renaming would lose a load-bearing prose convention installed across NOTATION.md, LEXICON.md, and the segment Brief. "
        "Occasional paraphrases ('objective gap', 'attainability gap') exist; the canonical name is established and "
        "absorbing them is what canonicalization does.",

    ('orient cascade', 'orient cascade'):
        "Names two things at once: the structural shape (cascade = forced sequential resolution by information dependency) "
        "and the heritage (Boyd's 'Orient' from OODA, which the segment explicitly references). The argument for keeping it "
        "is that 'cascade' is the geometry the content actually has — the $M_t \\to \\Sigma_t \\to O_t$ resolution order is "
        "literally a cascade — and the OODA echo is informative without being captured by it. Considered alternatives "
        "('orientation sequence', 'diagnostic cascade', 'resolution order') were judged flatter or less memorable. "
        "Lowercase form is the canonical convention except sentence-initial.",

    ('directed separation', 'directed separation'):
        "Names a Pearl-blanket structural property the segment derives (epistemic update one-way independent of $G_t$). "
        "Defenders argue both halves are load-bearing: 'directed' captures the asymmetric information flow, 'separation' "
        "carries the conditional-independence sense from Pearl's d-separation lineage. The collision risk most often raised "
        "is the LQR/Kalman *separation principle*; defenders treat that as informative — the separation principle is a "
        "Class-1 *consequence* of directed separation, not a different concept — and propose handling it via a one-sentence "
        "Discussion clarification rather than a rename. The architectural Class 1/2/3 classification hangs off this name; "
        "renaming would break that tether.",

    ('identifiability floor', 'identifiability floor'):
        "Names a meta-pattern about hard lower boundaries on inference. The case for 'floor' is geometric: it captures the "
        "asymmetry that you cannot go below it without outside help (information augmentation, identifying assumptions, "
        "etc.) but you can climb above it via specific machinery the framework supplies. Defenders contrast this with "
        "'no-go theorem', which is too generic, too negative, and loses the boundary-and-escape structure. The name pairs "
        "structurally with separability-pattern (or separability-ladder, if that rename lands) and with the forced-coordinates "
        "meta-segment to form the three-segment epistemic-architecture trio. 'Escape the floor' has begun appearing as "
        "organic prose in the codebase, evidence the metaphor is doing work.",

    ('information bottleneck', 'information bottleneck'):
        "Adopted directly from Tishby, Pereira & Bialek 1999. The case for keeping is the prior-art-integration convention: "
        "adopted concepts retain their original names with citation, both for provenance and for letting the field's "
        "structural intuitions transfer. The word 'bottleneck' is doing real explanatory work in the AAD application — "
        "the policy-conditioned forward-predictive variant the framework uses is a sub-case of the standard formulation, "
        "not a different object. If a distinguishing label were needed for the AAD-specific variant ('Policy-Conditioned IB', "
        "'Forward-Predictive IB', 'AAD-IB') it could be added without disturbing the parent name.",

    ('chronica', 'chronica'):
        "A deliberately coined Greek-rooted noun ('records of time') for the complete interaction history. "
        "Three load-bearing properties cited by defenders: it avoids the $\\mathcal{H}$ collision with entropy in notation "
        "and read-aloud; it is a singular speakable noun where 'history' or 'interaction history' are not; and it carries "
        "the philosophical weight of the (PI) postulate's commitment to a singular non-forkable trajectory, which becomes "
        "more morally heavy in the logozoetic extensions. The Greek-vocabulary register is a deliberate framework "
        "commitment; chronica is the strongest exemplar. The notation $\\mathcal{C}_t$ pairs cleanly with the prose name. "
        "One vote treated this row as a Brief-field gloss exercise rather than a name vote — the slug is settled; the "
        "Feynman-criterion plain-language gloss is what's missing.",

    ('strategy DAG', 'strategy DAG'):
        "Adopted from probabilistic graphical models. Defenders argue both halves carry load: 'strategy' for $\\Sigma_t$ "
        "the state object, 'DAG' for the structural representation (acyclicity from temporal ordering, Markov from CMC). "
        "The acronym 'DAG' is pronounceable, field-standard, and used as a noun in graphical-models prose. The slug is "
        "referenced by name in many downstream segments, so renaming carries cascading editorial cost for negligible gain. "
        "Paraphrases ('strategy graph', 'strategy structure', 'agent's strategic causal model') appear in prose; "
        "canonicalization commits to the established form.",

    ('chain confidence decay', 'chain confidence decay'):
        "Self-descriptive compound naming the phenomenon (log-confidence is additive in chain depth, so aggregate confidence "
        "decays monotonically with depth). The defense is that the name names the phenomenon, not the proof — readers can "
        "paraphrase 'as chain depth grows, confidence decays' aloud. The segment is the structural anchor for the "
        "additive-coordinate-forcing meta-pattern (chain-rule identity → three downstream uniqueness theorems), so the "
        "name carries weight beyond its own segment.",

    ('persistence condition', 'persistence condition'):
        "The framework's central inequality ($\\alpha R \\gt \\rho$). Defenders cite three reasons to keep: it is canonical "
        "across adjacent fields (Lyapunov stability, RL viability, organizational persistence, software maintenance) so the "
        "baggage transfers; it is referenced throughout the codebase, making a rename expensive in editorial work; and the "
        "segment carries the canonical bathtub gloss in its Findings section, which is built on this name. Occasional "
        "paraphrases ('persistence criterion', 'adaptive persistence condition', 'the alpha-greater-than-rho-over-R "
        "condition') need standardizing on this canonical form.",

    ('logogenic agent', 'logogenic agent'):
        "A deliberately coined Greek-rooted term for language-constituted agents. The case for keeping is twofold: "
        "the term names a structural channel property (constituted-by-language) rather than a transient implementation "
        "technology, so it survives the LLM era; and it sits within the Greek-vocabulary register the framework deliberately "
        "maintains (chronica, prolepsis, aisthesis, etc.). The contrast with 'LLM-based agent' or 'language-based agent' is "
        "load-bearing: those are instantiation-level descriptions; logogenic is the architectural concept. Pairs with "
        "moral-continuity (logozoetic) cleanly.",

    ('symbiogenic composition', 'symbiogenic composition'):
        "Adopted from biology (Margulis, endosymbiotic-theory lineage). The case for keeping is unusually strong because "
        "the borrowed term names the AAD mechanism with precision: 'symbiogenic' means one entity integrating another that "
        "formerly had its own autonomy, and the $U_O$-crosses-threshold-from-below mechanism in the segment matches that "
        "biological meaning exactly. Defenders flag the high specialist-vocabulary cost (biology readers will recognize it; "
        "others may need an explanation) but treat that cost as worth the precision. A rare case where the adopted term "
        "*upgrades* the reader's intuition about the formalism rather than just labeling it.",

    ('sector persistence template', 'sector persistence template'):
        "Names the abstract Lyapunov-on-sector-bounded-correction pattern that six AAD results instantiate. The argument is "
        "that 'template' is the precise AAD term — it is not a metaphor; the segment is invoked across many other segments "
        "as a template, with each instantiation specifying its own state variable and disturbance rate. 'Sector' "
        "distinguishes it from contraction-based persistence variants. Long but structurally honest; shortening would erase "
        "which persistence machinery is in play.",

    ('temporal optimality', 'temporal optimality'):
        "TST's foundational normative postulate: among equivalent outcomes, least-time is preferred. Defenders describe it "
        "as theorem-target-shaped — short, forceful, memorable — rather than slogan-shaped. The argument for keeping is that "
        "the postulate is the foundational normative principle of TST and the name foregrounds the time dimension that "
        "AAD's descriptive grounding (via persistence) makes load-bearing. Renaming would weaken a well-established prior "
        "commitment carried over from the TST corpus.",

    ('adversarial destabilization', 'adversarial destabilization'):
        "The cooperative/adversarial complement to team-persistence. The case for keeping centers on the word "
        "'destabilization' itself: it signals direction (outward from the bounded region) where neutral words like 'dynamics' "
        "would not. Pairs naturally with the OODA 'inside the opponent's loop' framing that the segment articulates. "
        "The 'effects spiral' sub-result is handled adequately by Discussion mention without renaming.",

    ('agent spectrum', 'agent spectrum'):
        "Names the ±model × ±objective 2×2 picture. The defense centers on 'spectrum' being accurate: the segment explicitly "
        "treats the four corners as continuous regions, not discrete categories, so 'quadrants' or 'partition' or 'typology' "
        "would mis-describe what the segment is doing. Considered alternatives ('agent quadrants', 'agent types-partition', "
        "'agent classification') were judged worse on this exact dimension. Variants in prose ('agent quadrant', "
        "'agent typology', 'agent classification') need standardizing on the canonical form.",

    ('shared intent', 'shared intent'):
        "Maps directly to the Clausewitz / commander's-intent / Auftragstaktik tradition (acknowledged in the segment) and "
        "to the IB-compressed cross-agent communication object that the segment formalizes. The name is the operational "
        "concept — what gets transmitted between agents — and is distinct from teleological-unity, which is the *measured* "
        "alignment property ($U_O = I/H$). Defenders rebut a proposed rename to 'teleological unity' on these grounds: "
        "merging the two concepts would erase a useful distinction. The name is established prose vocabulary across the codebase.",

    ('AAD (Adaptation and Actuation Dynamics)', 'AAD (Adaptation and Actuation Dynamics)'):
        "The framework name itself, recently renamed (2026-04-16) from Agentic Cycle Theory to resolve a collision with "
        "the AI Consciousness Test (Schneider & Turner) in AI welfare literature. The case for keeping centers on rename "
        "cost: the rename has been paid, citation velocity is building under the new name, and any fresh alternative would "
        "face the same collision-checking burden ACT did. The acknowledged imperfection — 'Actuation' is a slightly weaker "
        "fit than 'Adaptation' for what Section II covers (purposeful agency with objectives, not mechanical actuation) — "
        "is judged to be cheaper to handle via a Section II preamble clarification than via another framework-level rename.",

    ('adaptive tempo', 'adaptive tempo'):
        "Names $\\mathcal{T} = \\sum_k \\nu^{(k)} \\eta^{(k)\\ast}$, the rate-of-useful-info-acquisition quantity. The "
        "central argument for the word 'tempo' is that it carries both *rate* and *quality* simultaneously, which is "
        "exactly what the formula compounds (rate × quality). The word is underused in the ML literature, which makes it "
        "available for AAD to own. Defenders contrast with 'learning rate' (which is $\\eta^\\ast$, a sub-quantity), "
        "'correction rate', or bare 'tempo'; the canonical form is 'adaptive tempo' bound to $\\mathcal{T}$. The Boyd-OODA "
        "lineage and the Greek-register fit are secondary supports.",

    ('agent opacity', 'agent opacity'):
        "Adopted from Hafez 2026 ($H_b^{A|B}$, backward predictive uncertainty). The case for keeping is twofold: "
        "prior-art-integration convention forbids renaming adopted concepts with proper attribution, and the word 'opacity' "
        "carries exactly the right intuition — the dual of observability — for the emitter side. Pairs naturally with "
        "'transparency' as the opposite, with observation-quality $U_o$ as the formal dual, and reads naturally in "
        "adversarial contexts ('adversaries want opacity; cooperators want transparency'). The dual framing is load-bearing "
        "in Section III.",

    ('causal information yield', 'causal information yield'):
        "Three-word noun naming the information gained from causal interventions, with the natural acronym 'CIY' as "
        "shorthand. The case for keeping is that the expansion is exact, reusable across exploration / querying / trust, "
        "and that the acronym earns its keep because the concept recurs widely in the framework. The currently-mixed prose "
        "use ('CIY' in some places, 'Causal Information Yield' in others) needs standardizing — the full form should be "
        "canonical in prose, the acronym a shorthand only.",

    ('composition closure', 'composition closure'):
        "Names the formulation that makes valid composite-agent status testable via the closure-defect $\\varepsilon^\\ast$. "
        "Defenders judge 'closure' technically precise (in the mathematical sense — does the operation stay within the "
        "set?) and the compound 'composition closure' tightly bound to the segment's content. A possible alternative — "
        "renaming to '#form-closure-defect' to foreground the central quantity — was considered, but the current name "
        "keeps the conceptual move audible and the closure-defect lives downstream. Mild concern noted that 'closure' has "
        "different connotations to readers from a software background, which slightly lowers the keep-confidence.",

    ('communication gain', 'communication gain'):
        "Direct analog of update-gain for inter-agent channels. The case for keeping rests on the parallel structure: "
        "AAD's gain-principle pattern instantiates uniformly across self ($\\eta^\\ast$ = update gain), inter-agent "
        "(communication gain), and possibly other channels, so the parallel naming is itself pedagogical. Defenders rebut "
        "'trust gain' on the grounds that trust is a *component* of communication gain (the trust-weighted uncertainty "
        "ratio), not the whole quantity, and that the rename would break the update-gain parallel.",

    ('deliberation cost', 'deliberation cost'):
        "Names the think-versus-act tradeoff under mismatch drift. The case for keeping is that 'cost' signals the "
        "tradeoff cleanly and pairs with the discussion segment `#disc-exploit-explore-deliberate` to form a clean "
        "two-segment naming compound. The phrase reads naturally as cost-benefit and is the formal penalty assessed against "
        "$\\mathcal{T}_\\Sigma$.",

    ('observability dominance', 'observability dominance'):
        "Names the derived claim that unobservable strategy edges are epistemically dead — the gain principle dominates "
        "the edge update when observability is low — regardless of nominal confidence. Defenders treat 'dominance' as "
        "technically precise (information-theoretic dominance) and the two-word phrase as memorable. The Discussion's "
        "absorbing-state analysis is what makes the name feel exactly right; the LEXICON 'Terms to Be Added' entry "
        "anticipates the segment promotion.",

    ('Pearl causal hierarchy', 'Pearl causal hierarchy'):
        "Adopted directly from Pearl with proper attribution. The case for keeping is the prior-art-integration "
        "convention: adopted external concepts retain attribution; renaming would lose provenance and create NIH-syndrome "
        "alternatives. The proper-noun form ('Pearl's causal hierarchy') is the field-standard name. Distinguishes Pearl's "
        "L0/L1/L2 hierarchy cleanly from AAD's *internal* correlation hierarchy and convention hierarchy, both of which "
        "the framework owns separately.",

    ('team persistence', 'team persistence'):
        "The cooperative composite analog of persistence-condition. The case for keeping is that 'team persistence' is "
        "plain English for what the derivation actually is (cooperative composite sector condition) and parallels the "
        "persistence-condition naming consistently. Reads as 'what makes a team persist' — self-descriptive at the right "
        "level of abstraction for a multi-agent claim.",

    ('approximation tiering', 'approximation tiering'):
        "Names the meta-pattern for tractability-indexed hierarchies (L0/L1/L2; C1/C2/C3; Tier 1/2/3). The case for "
        "keeping is that 'tiering' is precise — it names the operation (creating tiers under monotonicity) rather than "
        "just the result (tiers) — and avoids the 'hierarchy' overload that already crowds the framework. The four-component "
        "(AT1)–(AT4) structure is genuinely a tiering, not a continuum or a hierarchy; #disc-graceful-degradation was "
        "considered as an alternative but graceful-degradation is one property of the tiering, not the whole pattern.",

    ('consolidation dynamics', 'consolidation dynamics'):
        "Names the offline regime of $g_M$ (replay-driven model tightening). The case for keeping is that 'consolidation' "
        "imports the neuroscience baggage (memory consolidation, stability-plasticity) that's precisely what the "
        "segment is formalizing — engineering vocabulary that travels well. The dynamics suffix is accurate; the compound "
        "is an established lineage cue from the source field. Mild concern noted that the term is slightly clinical, "
        "but no obviously better alternative emerged.",

    ('loop interventional access', 'loop interventional access'):
        "Names the distinctive Pearl-Level-2-by-construction property: the feedback loop provides Level-2 (interventional) "
        "data by construction, which is the escape route from the on-policy causal-confounding problem. Defenders argue "
        "the phrase 'loop interventional access' lands in one read and the concept has no shorter form without loss. "
        "Specialist but precise — it names *where* the intervention happens (within the feedback loop) and is "
        "load-bearing for both #identifiability-floor and #agent-identity. Mild concern noted that the name is a mouthful "
        "for conversation; an informal short form ('the loop's Level-2 access', 'loop as Level 2 engine') is acceptable.",

    ('epistemic architecture', 'epistemic architecture'):
        "Framing-vocabulary phrase used in CLAUDE.md §7, the README, and OUTLINE.md preambles. "
        "The case for canonicalizing centers on positioning: three independent frontier-model audits converged on reframing "
        "AAD from 'integration of four disciplines' to 'epistemic architecture for bounded correction' — integration is a "
        "method, the contribution is the architecture. Standardizing 'epistemic architecture' as the primary positioning "
        "term displaces paraphrases like 'epistemic apparatus' or 'correction architecture'. Important caveat from "
        "defenders: this should remain *framing-vocabulary*, not be promoted to a fourth meta-segment alongside the three "
        "(identifiability-floor / separability-pattern / additive-coordinate-forcing) that already do the technical work.",

    ('strategic calibration', 'strategic calibration'):
        "Names the edge-residual aggregate that measures how well the strategy DAG is calibrated. The case for keeping "
        "centers on parallel construction with epistemic-calibration from broader literature and on the LEXICON.md prose "
        "form. The follow-on alias vote formalizes the symbol+English pair: 'strategic calibration' is the concept-name; "
        "the residual aggregate is its measurement. Acceptable but not load-bearing; no strong alternative offered.",

    ('strategic tempo', 'strategic tempo'):
        "Direct parallel to adaptive-tempo on the strategy axis. The case for keeping rests on the parallelism itself: "
        "an agent's adaptive tempo governs $M_t$-side persistence, its strategic tempo governs $\\Sigma_t$-side persistence — "
        "the matched pair compounds in prose ('the team has high adaptive tempo but lagging strategic tempo'). Distinguishes "
        "strategy-revision rate from epistemic-update rate cleanly.",

    ('unity dimension', 'unity dimension'):
        "Names the family of $U_M$, $U_O$, $U_\\Sigma$ (and possibly $U_\\Pi$ as a fourth candidate under discussion). "
        "The case for keeping is that 'unity' is the Clausewitz/Bungay-derived term established across NOTATION.md and "
        "the Section III preamble; it captures the coordinating-principle sense. Defenders rebut a proposed rename to "
        "'coherence dimension' on the grounds that 'coherence' is already doing soft duty elsewhere (strategic coherence, "
        "epistemic coherence) and the rename would create bleed. 'Unity' implies binary state to some readers; the segment "
        "preamble can clarify the dimensional gradient without renaming.",

    ('adaptive reserve', 'adaptive reserve'):
        "Two-word symbol-to-English alias for $\\Delta\\rho^\\ast = \\alpha R - \\rho$. The case for keeping rests on the "
        "engineering intuition the term carries: 'reserve' reads as shock-tolerance / shock-absorber-depth / crumple-zone, "
        "which is exactly the role $\\Delta\\rho^\\ast$ plays (margin before persistence fails). The compound lands on first "
        "read and is already established in NOTATION.md and LEXICON.md. Variants like 'shock tolerance' and 'disturbance "
        "margin' need standardizing on this canonical form. One of the project's cleanest symbol-to-English pairs.",

    ('mismatch signal', 'mismatch signal'):
        "Names $\\delta_t$, deliberately chosen over 'error' or 'residual' to foreshadow the aporia interpretation in the "
        "five-phase cycle. The case for keeping is two-register vocabulary discipline: 'mismatch' is the engineering register "
        "(flatter than 'error', which presupposes the agent was wrong); 'aporia' is the philosophical register (the cycle "
        "phase). Defenders rebut a proposed rename to 'aporia signal' on the grounds that the dual usage is correct: "
        "mismatch signal in formulas and engineering prose, aporia in cycle-phase prose. Renaming the slug to the Greek "
        "term would break the iconic mismatch-signal / satisfaction-gap / control-regret three-name engineering register.",

    ('strengthen first posture', 'strengthen first posture'):
        "Names the working-conventions methodology principle articulated in CLAUDE.md (and aliased as 'attempt the "
        "improbable'). The case for canonicalizing 'strengthen-first posture' as the primary directive form rests on a "
        "directive-vs-aspirational distinction: 'strengthen-first' tells an agent what to do (attempt strengthening before "
        "softening); 'attempt the improbable' is the spirit but less directive. For working conventions, the directive "
        "form wins. 'Attempt the improbable' remains useful as a spirit-level phrase but not as the procedural label. "
        "Variants ('strengthen before softening', 'strengthen-first discipline', 'the strengthening move') need standardizing "
        "on the hyphenated two-word form.",

    ('calibration laboratory', 'calibration laboratory'):
        "TST framing-vocabulary phrase: software is AAD's privileged high-identifiability calibration laboratory. "
        "Defenders argue 'laboratory' is the right metaphor — software has high identifiability, clean instrumentation, "
        "and supports exact measurement of AAD quantities — and that the phrase deserves promotion to a stable short name "
        "central to TST's architectural role. Variants in prose ('richest operationalization domain', 'best operationalization "
        "domain', 'privileged high-identifiability calibration laboratory') need standardizing on 'calibration laboratory' "
        "as the canonical short form, with 'privileged high-identifiability calibration laboratory' available as the modifier "
        "expansion when context warrants.",

    ('update gain', 'update gain'):
        "Adopted from Kalman / control theory. The case for keeping is the prior-art-integration convention plus the "
        "transfer of correct baggage: 'gain' in AAD plays the role the reader expects, and the formula "
        "$\\eta^\\ast = U_M / (U_M + U_o)$ is iconic in the framework. Renaming would lose a load-bearing prose convention. "
        "The follow-on alias votes formalize the symbol+English pair across NOTATION.md and LEXICON.md.",

    ('closure defect', 'closure defect'):
        "Names $\\varepsilon^\\ast$, the minimum achievable approximation error of the macro-description against the "
        "micro-system. Defenders cite three load-bearing properties: 'defect' carries the precise mathematical sense "
        "(a residual that cannot be eliminated, only minimized over admissible classes); 'closure' names the homomorphism "
        "property being approximated; the two-word compound is short, evocative ('something failing to seal cleanly'), and "
        "memorable. Already aliased in #form-composition-closure with the symbol+English pair maintained: "
        "$\\varepsilon^\\ast$ in math, 'closure defect' in prose, full expansion when introducing the quantity.",

    ('contraction over drift principle', 'contraction over drift principle'):
        "Names the organizing-principle slogan: an adaptive system is a projection whose contraction rate exceeds its "
        "target's drift rate. The case for canonicalizing rests on cite-ability: the full sentence is too long to repeat "
        "across segment cross-references; the compact name lets segments point back to it cleanly. Already attributed in "
        "CLAUDE.md and described as an organizing-principle slogan that 'has not yet been surfaced at segment level' — the "
        "name promotes that status without changing the content.",

    # Heavy renames

    ('concept the parameter space region within which an agent maintain bounded mismatch indefinitely',
     'Persistence envelope'):
        "Names the set $\\{(\\alpha, \\rho, R) : \\alpha R \\gt \\rho\\}$ — the region within which the persistence "
        "guarantee holds — using engineering-vocabulary that travels well across domains. The case rests on the "
        "flight-envelope / operating-envelope analogy: 'envelope' is the standard control-theory term for operating bounds "
        "within which guarantees apply, supporting prose like 'this organization sits well inside its persistence envelope' "
        "or 'the adversarial agent is pushing $B$'s persistence envelope.' "
        "The current paraphrase ('the region where the persistence condition holds', 'the adaptive regime') is verbose "
        "and non-memorable; the proposed name names the same set viewed dynamically. "
        "Considered alternatives ('stability envelope', 'safety envelope', 'adaptive basin') were rejected: stability "
        "collides with sector-stability, safety collides with AI-safety jargon, and 'basin' is mathematically loaded "
        "(basin of attraction) and would force formal justification at the derivation layer. Reserving 'basin' for the "
        "technical sense and using 'envelope' for the prose handle is the cleanest split.",

    ('additive coordinate forcing', 'Forced coordinate'):
        "The case rests on scope-honesty for a meta-segment. The current 'additive' qualifier covers three of the four "
        "primary instances (chain / divergence / update via Cauchy-FE) but undersells the Čencov / Fisher-metric fourth, "
        "which forces coordinates via reparameterization-invariance, not via additivity. The segment itself acknowledges "
        "this in the Discussion. 'Forced coordinate' covers both Cauchy-FE and Čencov machineries without overpromising "
        "additivity, and the noun form is more memorable than the gerund. Counter-argument from one defender: the noun "
        "form is passive — readers may not know what forces them — and the verb form ('forcing') better preserves the "
        "process structure. The companion candidate 'coordinate forcing' captures the verb form. The shape of the "
        "discussion is verb-form vs. noun-form, with both rejecting 'additive' as under-inclusive.",

    ('additive coordinate forcing', 'Coordinate forcing'):
        "Verb-form alternative to 'forced coordinate'. The shared argument with the noun-form variant is that 'additive' "
        "is under-inclusive (doesn't cover the Čencov / Fisher-metric fourth instance). The verb-form-specific case is "
        "that 'coordinate forcing' names the *move* (uniqueness theorem on AAD-internal axiom forcing a coordinate choice) "
        "rather than just the result, which parallels 'directed separation' and 'satisfaction gap' as verb-flavored "
        "compound nouns. Counter-argument from defenders of the noun form: 'forcing' is mechanical and cliché where "
        "'forced coordinate' lands as a thing. Considered acceptable as a fallback if 'forced coordinate' doesn't land.",

    ('concept the unupdatable region of the strategy DAG where edge receive no actionable feedback',
     'Epistemic dead zone'):
        "Names what the structure *does* (paths become epistemically dead — no signal can reach them) rather than what it "
        "*is* (a subgraph that happens to be unobservable). The case rests on geometric-and-operational compounding: "
        "'dead zone' is geometric (a region of the DAG) and operational (no signal reaches it). Pairs with #observability-"
        "dominance and #identifiability-floor as a trio of locality / dynamics / structure descriptors of the same "
        "phenomenon. Stronger than alternatives like 'unobservable strategy subgraph' (descriptive but inert) or "
        "'epistemic death' (overloaded by the gain-collapse failure mode).",

    ('separability pattern', 'Separability ladder'):
        "The case rests on the segment's own organizing structure: the meta-segment is a seven-row *ladder* "
        "(separable-core / structured-repair / general-open across seven axes of increasing difficulty), and the "
        "Brief, Discussion, and cross-citations all reach for 'ladder' or 'rungs' as the unit. 'Pattern' is generic "
        "filler that describes no specific structure; 'ladder' is the geometry the content actually has. Pairs "
        "mnemonically with #identifiability-floor ('the ladder above the floor'). Counter-argument from one defender: "
        "the rename would churn cross-references, but the segment itself already says 'six ladders' in prose, so the slug "
        "is lagging the prose. 'Staircase' was considered and rejected as whimsical without a precision gain — staircases "
        "are uniform, ladders intuitively get harder toward the top.",

    ('strategic composition', 'Equilibrium composition'):
        "Two arguments converge on the rename. First, 'strategic' is overloaded across Section II and III "
        "(strategic-tempo, strategic-calibration, strategic-dynamics-derivation), and the meta-segment's *distinctive* "
        "move is the equilibrium framing (Monderer-Shapley potential games, Rosen monotone games). Second, 'equilibrium' "
        "is scope-honest — it names the actual machinery — where 'strategic' is generic. Counter-argument from a defender: "
        "the section uses 'strategic' pervasively and breaking the pattern for one segment creates overload confusion in "
        "the other direction. The preferred rename pairs with the rejection of the broader-scoped 'game-theoretic composition' "
        "alternative, which would invite mechanism-design / information-design / non-equilibrium material into the same "
        "namespace prematurely.",

    ('$\\alpha_2$ a2 adaptive gain sub-scope', 'Adaptive gain regime'):
        "Symbol-to-English alias paralleling $\\alpha_1$'s 'derived-gain regime'. The case rests on prose-readability: "
        "'AMSGrad lands in $\\alpha_2$' reads cryptically, 'AMSGrad lands in the adaptive-gain regime' reads naturally. "
        "The English alias is already in implicit use; the symbol stays as shorthand. The parallel construction with the "
        "$\\alpha_1$ alias creates a maintained convention rather than free synonymy.",

    # Substantive dissent cases (3+ votes, one or more substantive negatives)

    ('additive coordinate forcing', 'Uniqueness coordinate forcing'):
        "An alternative rename argued for on the grounds that the broader discipline being named is uniqueness — "
        "a uniqueness theorem applied to an AAD-internal axiom — not additivity alone. More precise on the mechanism shared "
        "across all four instances. Counter-arguments: more abstract than the current name; less memorable than 'forced "
        "coordinates'; reads as a category label rather than a concept name; less smooth to say. Considered an honest "
        "alternative if 'forced coordinates' doesn't land but a weaker first choice.",

    ('additive coordinate forcing', 'Cauchy coordinate'):
        "Considered for compactness and crispness. The argument against, raised consistently across votes, is "
        "scope-dishonesty: the Čencov metric-layer fourth primary instance is *not* Cauchy-FE, so naming the meta-pattern "
        "for one of two machineries violates the same scope-honesty commitment the segment establishes in its own Discussion. "
        "A weak supporting case retained 'Cauchy' as long-form subtitle alongside the current name; the dominant view "
        "treats the candidate as actively misleading now that the Čencov instance is part of the primary four.",

    ('separability pattern', 'Separability staircase'):
        "Considered as a more whimsical alternative to 'ladder'. The argument against: 'staircase' doesn't carry the "
        "increasing-difficulty semantics as cleanly — staircases are uniform; ladders intuitively get harder toward the "
        "top. Whimsical without a compensating precision gain.",

    ('shared intent', 'Teleological unity'):
        "Proposed on the grounds that the rename would align with $U_O$ notation and unify with epistemic / strategic "
        "unity. Counter-arguments: the rename collapses two distinct concepts. Shared intent is the *operational* cross-agent "
        "communication object (the IB-compressed payload of $G_t$); teleological unity is the *measured* alignment property "
        "($U_O = I/H$). They are not the same — a multi-agent system can have high shared-intent communication and low "
        "measured teleological-unity, or vice versa — so merging them would erase a useful distinction the framework relies on.",

    ('auftragstaktik principle', 'Mission command principle'):
        "Argument for: the German term creates unnecessary lookup cost; 'mission command' is the standard modern English "
        "translation that conveys the exact same intent. Counter-argument: 'mission command' should be an English alias, "
        "not a replacement, because Auftragstaktik carries the specific historical doctrine (Moltke / Prussian command) "
        "that motivates the segment. The rename collapses the alias relationship into a wholesale replacement. The shape "
        "of the disagreement is rename-vs-add-alias rather than disagreement on the English term itself.",

    ('communication gain', 'Trust gain'):
        "Argument for: the formal definition is the trust-weighted uncertainty ratio, so 'trust gain' is more evocative "
        "of the inter-agent dynamic than the clinical 'communication gain'. Counter-argument: trust is a *component* of "
        "communication gain, not the whole quantity; renaming would break the parallel with update-gain and overcommit "
        "to one ingredient over the compound.",

    ('strategic composition', 'Game theoretic composition'):
        "Argued for on the grounds of reducing 'strategic' overload in Section III. The argument against, raised "
        "consistently: too broad. Game theory covers mechanism design, signaling, bargaining, and non-equilibrium material "
        "outside this segment's scope — the segment specifically derives equilibrium-convergence under "
        "Monderer-Shapley / Rosen, which is a tighter framing. If Section III later adds non-equilibrium game-theoretic "
        "material, a separate segment would be cleaner than sharing one overloaded bucket.",

    ('unity dimension', 'Coherence dimension'):
        "Argument for: 'unity' implies a binary state (unified or not); 'coherence' better suits a continuous gradient. "
        "Counter-argument: 'coherence' is already doing soft duty elsewhere (strategic coherence, epistemic coherence) "
        "and a rename would bleed into those informal usages. The framework's preference is to keep 'unity' narrow and "
        "let segment preambles clarify the dimensional gradient rather than rename to a term already in soft use.",

    ('mismatch signal', 'Aporia signal'):
        "Argument for: aligns with the Greek-vocabulary register (prolepsis / aisthesis / aporia / epistrophe / praxis) "
        "the framework deliberately uses. Counter-argument: keep two registers. 'Mismatch signal' is the engineering "
        "quantity that reads unambiguously to any engineer; 'aporia' is the cycle-phase / interpretive frame. The Greek "
        "naming is for the phases, not the sub-quantities. Renaming the slug would break the iconic mismatch-signal / "
        "satisfaction-gap / control-regret three-name engineering register; the dual alias *in prose* (mismatch in "
        "engineering register, aporia signal in cycle-phase register) is the right move and doesn't require slug rename.",

    ('strengthen first posture', 'Attempt the improbable'):
        "Considered as the spirit form of the working-conventions principle. Argument for: more memorable; captures the "
        "spirit better than 'strengthen-first' which sounds procedural. Argument against: less directive — "
        "'strengthen-first' tells an agent what to do; 'attempt the improbable' tells them how to feel. For working "
        "conventions where the goal is action-prompting, the directive form wins. The aspirational form is useful as a "
        "secondary phrase but not as the procedural label.",

    ('developer-as-act-agent', 'Developer as AAD agent'):
        "Argued for on the grounds that the 'act-agent' suffix is a stale internal abbreviation after the ACT → AAD "
        "rename, and the slug should match the segment heading without unexplained abbreviations. Counter-argument: "
        "embedding a framework acronym in a slug is exactly the rot pattern just cleaned up by the ACT→AAD rename; "
        "re-introducing it in a different slug perpetuates the fragility. The shape of the disagreement is whether to "
        "fix the abbreviation (rename) or to remove the framework-name from the slug entirely (different rename target).",

    ('Lohmiller-Slotine contraction', 'Lohmiller-Slotine contraction'):
        "Adopted external concept (Lohmiller-Slotine 1998). The case rests on the prior-art-integration convention: "
        "adopted concepts retain attribution. The single dissent vote was marked at -1 not as a substantive rejection but "
        "to expose the question per voting instructions — there is no genuine alternative; the segment imports the result "
        "verbatim.",

    ('Čencov invariance', 'Čencov invariance'):
        "Adopted external concept (Čencov 1982). Same prior-art-integration argument as Lohmiller-Slotine: adopted "
        "concepts retain attribution; the dissent vote was marked at -1 to expose the question, not as substantive rejection.",

    ('actuated agent', 'actuated agent'):
        "Names the formal Class 2/3 case (agents with both model and objective structure). The defense centers on a "
        "deliberate choice over 'purposeful agent' — 'actuated' avoids consciousness baggage while carrying the "
        "driven-toward-setpoint shape. The objection raised: the mechanical baggage of 'actuated' overrides the precise "
        "AAD boundary the term is meant to establish. Tied to the AAD framework name itself ('Actuation Dynamics'); "
        "renaming would cascade into the framework name.",

    ('indivisum', 'Causal lock'):
        "Argument for: 'causal lock' vividly names the mechanism (singular-trajectory non-forkability) where the Latin "
        "'indivisum' is opaque on first encounter. Counter-argument: register-mismatch with the rest of the PROPRIUM "
        "vocabulary (which is deliberately Latin / Greek). If the register is wrong, the whole PROPRIUM vocabulary should "
        "be replaced, not one term — half-rename produces the worst outcome. The disagreement is about whether to commit "
        "to the PROPRIUM register or to break it for vividness on a per-term basis.",

    ('strategy dimension', 'strategy dimension'):
        "Names the $\\Sigma_t$ dimension of $G_t = (O_t, \\Sigma_t)$. The defense is mild: specialist vocabulary but "
        "functional, no obviously better alternative. One vote considered renaming to '#purposeful-substate-split' and "
        "rejected it as worse. One concern flagged: 'strategy dimension' undersells $O_t$, the other half of the split, "
        "but no better alternative emerged. Weak keep.",

    ('and or', 'Strategy DAG topology'):
        "Argument for: the segment is named after the mechanism (AND/OR combination) rather than the subject being "
        "scoped (the DAG topology). Counter-argument: the rename overreaches. The segment is specifically about admitting "
        "AND/OR combination semantics for nodes; it does not define the full DAG topology. Acyclicity comes from "
        "#post-causal-structure / #deriv-graph-structure-uniqueness; node-types AND/OR are the segment's actual subject. "
        "Renaming to 'strategy-dag-topology' would conflict with #def-strategy-dag and over-claim the segment's scope.",

    ('convention hierarchy', 'Continuation hierarchy'):
        "Argument for: 'convention' collides with the game-theoretic / Lewisian sense (social conventions, conventions-as-"
        "equilibrium-selection), which is a distinct unrelated concept some readers will have in mind. What the C-hierarchy "
        "actually indexes is the choice of *continuation policy* for value-object evaluation (one-step, receding-horizon, "
        "Bellman). 'Continuation hierarchy' is self-announcing and keeps the C1/C2/C3 mnemonic intact. "
        "Counter-argument: 'continuation' is more self-descriptive but the project's 'convention' usage is established "
        "and the rename would churn across dozens of references — the cost of churn against the readability gain is "
        "the disagreement axis.",

    ('$U_o$ vs $U_O$ collision', '$U_o$ vs $U_O$ collision'):
        "Names a notation-discipline concern: $U_o$ (observation uncertainty, lowercase o) and $U_O$ (teleological unity, "
        "uppercase O) collide in serif fonts and in read-aloud, costing reader-time on every encounter. The proposed "
        "fix is renaming teleological unity to $U_\\Omega$ or $U_{\\text{goal}}$. Counter-argument considered and "
        "rejected: keep both and document the collision in NOTATION — footnotes don't prevent reader stumbles, and the "
        "rename is mechanical-cost-low and reader-cost-high if not done. The disagreement is about whether documentation "
        "or rename is the right fix; the rename position is preferred.",

    ('Bretagnolle-Huber identity', 'Bretagnolle-Huber identity'):
        "Adopted external theorem (Bretagnolle-Huber). Same prior-art-integration argument as Lohmiller-Slotine and "
        "Čencov: external attribution preserved, no genuine alternative exists. Dissent vote marked at -1 to expose the "
        "question per instructions, not as substantive rejection.",

    ('structural change as parametric limit', 'structural change as parametric limit'):
        "Names the formulation that treats discrete structural changes (pruning / grafting in the DAG) as continuous "
        "parametric limits. The defense is mild: long but accurate, the length is the price of precision. One vote "
        "considered shortening to '#structural-as-parametric-limit' or '#structural-to-parametric-limit' and rejected: "
        "'change' is load-bearing because the segment is about the *changes* to the DAG, not about the DAG states. "
        "Acceptable as-is.",
}


def main():
    with PATH.open() as f:
        data = json.load(f)

    applied = 0
    not_found = []
    for cur in data['currents']:
        for cand in cur['candidates']:
            key = (cur['current'], cand['candidate'])
            if key in RATIONALES and cand.get('consolidated_rationale') is None:
                cand['consolidated_rationale'] = RATIONALES[key]
                applied += 1

    # Verify all keys matched
    for key in RATIONALES:
        found = False
        for cur in data['currents']:
            if cur['current'] != key[0]:
                continue
            for cand in cur['candidates']:
                if cand['candidate'] == key[1]:
                    found = True
                    break
            if found:
                break
        if not found:
            not_found.append(key)

    print(f"Applied {applied} rationales")
    if not_found:
        print(f"NOT FOUND: {len(not_found)} keys")
        for k in not_found:
            print(f"  {k}")

    with PATH.open('w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {PATH}")


if __name__ == '__main__':
    main()
