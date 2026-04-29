# codex-1

OpenAI Codex - focused on slug legibility, memorable-noun potential, and symbol-to-English upgrades that reduce six-month-later lookup cost.

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---|---|
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | keep | +1 | "Actuation" is imperfect, but framework-level churn is more expensive than the remaining mismatch; clarify in prose rather than rename again. |
| Agentic Systems Framework (ASF) | Agentic Systems | rename | +1 | The repo's public face is already "Agentic Systems"; the extra acronym buys little and increases cognitive inventory. |
| README.md "What This Is" | README.md "What Agentic Systems Is" | rename | +1 | The current heading is generic; the framework name should anchor the reader immediately. |
| ## Working Notes | ## Working Notes | keep | +3 | This is established public API across segments and FORMAT.md; clearer than most substitutes and not worth churn. |
| ## Epistemic Status | ## Epistemic Status | keep | +3 | Precise, load-bearing, and distinctive to the project's honesty posture. Keep. |
| adaptive cycle | adaptive cycle | keep | +3 | Strong central noun phrase: specific enough to own, broad enough to travel across the framework. |
| Aporia | Aporia | keep | +3 | This earns its weight. "Error" and "mismatch" lose the productive-perplexity sense that makes the term memorable and accurate. |
| Epistrophe | Epistrophe | keep | +1 | Slightly harder on first contact than "update," but it preserves the turning-toward distinction the theory actually uses. |
| actuated agent | goal-actuated agent | rename | +1 | Keeps the mechanical register while paying the meaning tax sooner; "actuated" alone is a touch too bare on first read. |
| satisfaction gap | satisfaction gap | keep | +3 | One of the cleanest names in the repo. The phrase explains the diagnostic almost by itself. |
| control regret | control regret | keep | +3 | Crisp, properly scoped, and pairs perfectly with satisfaction gap. |
| adaptive reserve | adaptive reserve | keep | +3 | Strong engineering noun: it sounds like what it measures and is easy to use in discussion. |
| #chronica | #chronica | keep | +3 | Distinctive, speakable, and better than another overloaded "history" or "trace." Strong keep. |
| #directed-separation | #directed-separation | keep | +3 | Excellent theory name: concrete structural image, low baggage, easy to cite aloud. |
| orient cascade | orient cascade | keep | +3 | Memorable and faithful to the staged dependency structure; this is exactly the kind of communal-imagination name the project needs more of. |
| #strategy-dag | #strategy-dag | keep | +3 | Blunt and effective. The slug is legible instantly, and the concept it names is load-bearing. |
| #additive-coordinate-forcing | #forced-coordinates | rename | +3 | The current name is accurate but over-explains the mechanism. "Forced coordinates" is shorter, more noun-like, and broad enough to cover the metric-layer case too. |
| #additive-coordinate-forcing | #uniqueness-coordinate-forcing | rename | -1 | More abstract than the current name and less memorable than "forced coordinates." It sounds like a category label, not a concept people will use. |
| #separability-pattern | #separability-pattern | keep | +1 | Slightly clinical, but honest about what the segment is doing across multiple ladders. I considered renaming it and did not find a cleaner winner. |
| #strategic-composition | #equilibrium-composition | rename | +1 | "Strategic" is overloaded across Section II and III. The segment's distinctive move is the equilibrium framing, so the name should expose that. |
| #strategic-composition | #game-theoretic-composition | rename | -1 | Accurate but too broad and too textbook-ish; it imports more baggage than the segment needs. |
| #interaction-channel-classification | #signal-reception-regimes | rename | +3 | The four regimes are the actual memorable object here. The current name reads like taxonomy boilerplate. |
| #interaction-channel-classification | #recipient-side-channel-taxonomy | rename | -1 | Too procedural and too long. This would make the concept harder to say, not easier. |
| #m-preservation | #model-preservation | rename | +3 | The current slug is symbol-first and opaque in prose. The concept is about preserving model state, and the English should say so directly. |
| #observation-ambiguity-modulation | #goal-resolvable-ambiguity | rename | +3 | The segment introduces a first-class quantity; the name should foreground the quantity, not the fact that it modulates something downstream. |
| #coupled-diagnostic-framework | #post-hoc diagnostics | rename | +1 | "Framework" is generic filler here. The distinctive move is diagnostic extraction after the coupled update. |
| #context-turnover | #context-turnover | keep | +3 | Excellent name: short, accurate, and immediately legible to anyone who has worked with LLM agents. |
| temporal optimality | temporal optimality | keep | +3 | Strong, disciplined, and reusable. It sounds like a theorem target rather than a slogan. |
| atomic changeset | atomic changeset | keep | +1 | Not beautiful, but serviceable and honest. I considered alternatives and did not see one that improved both precision and memorability. |
| #change-proximity-principle | #change-locality-principle | rename | +1 | "Locality" is a more durable systems word than "proximity" and better matches architectural intuition. |
| code quality as observation infrastructure | observation infrastructure | rename | +1 | The durable concept is the investment class, not the full sentence. This gives the idea a reusable noun slot. |
| logogenic agent | logogenic agent | keep | +3 | Novel but justified; it names the structural property rather than today's implementation technology. Strong keep. |
| logozoetic agent | logozoetic agent | keep | +1 | Heavier than "logogenic" but still earns the novelty. The existential distinction is real enough to warrant a distinct term. |
| alpha1 (fixed-gain A2' sub-scope) | fixed-gain regime | add-alias | +3 | "Lands in alpha1" is decoder-ring prose. The English label is much cheaper in discussion. |
| alpha2 (adaptive-gain A2' sub-scope) | adaptive-gain regime | add-alias | +3 | Same reasoning as alpha1: the English does the work the symbol cannot do in prose. |
| beta (A2' assumed sub-scope) | assumed-sector regime | rename | +1 | Not elegant, but much more informative than a bare beta when the distinction is whether the sector condition is assumed rather than derived. |
| $\kappa_{\text{processing}}$ | processing coupling | add-alias | +1 | The symbol is fine in equations, but prose should default to the English name. It clarifies the architectural quantity immediately. |
| #identifiability-floor | #identifiability-floor | keep | +3 | Strong metaphor and well-matched to the segment's job: it names a hard lower boundary while still leaving room for explicit escape routes. |
| #identifiability-floor | #no-go theorems | rename | -1 | Too generic and too negative. It loses the boundary-and-escape structure that makes the current name useful. |
| #approximation-tiering | #tiered-approximation | rename | +1 | Slight improvement in natural-language flow. The current phrase is serviceable but abstract. |
| #sector-persistence-template | #bounded-correction-template | rename | +3 | Better public-facing name for what the result actually unifies. "Sector" names the proof device; "bounded correction" names the concept. |
| #sector-persistence-template | #persistence-template | rename | -1 | Too broad. It would erase the special bounded-correction structure that distinguishes this template from every other persistence discussion in the repo. |
| value object | policy-conditioned value | rename | +3 | "Value object" is overloaded from software design and hides the continuation-convention dependence. The proposed name says what the quantity actually is. |
| Convention Hierarchy | continuation hierarchy | rename | +3 | The hierarchy is specifically about continuation rules. "Convention" alone is underspecified and too generic. |
| agent spectrum | agent spectrum | keep | +1 | Useful, legible, and already doing real explanatory work in Section II setup. |
| blind pursuer | blind pursuer | keep | +1 | Borderline stylized, but memorable and semantically right for goal pursuit without a real world model. |
| #composition-scope-condition | #composite-agent condition | rename | +1 | The core decision is whether a composite agent exists, not whether "composition" is in scope in some generic sense. |
| team persistence | team persistence | keep | +3 | Strong keep: plain-language, memorable, and exactly the right level of abstraction. |
| distributed tempo | network tempo | rename | +1 | Shorter and easier to say aloud. The important content is tempo distributed across a communication network. |
| coordination overhead threshold | coordination tax | rename | +1 | This deserves a reusable noun slot. The current phrase explains; the proposed phrase sticks. |
| adversarial destabilization | adversarial destabilization | keep | +3 | Exact, vivid, and result-shaped. This is a good permanent name. |
| effects spiral | effects spiral | keep | +3 | Memorable without being whimsical. It is the kind of pattern-name people will actually reuse in discussion. |
| strategic composite | equilibrium composite | rename | +1 | The segment's distinctiveness is equilibrium convergence under partial opposition; the noun should expose that. |
| information bottleneck | information bottleneck | keep | +3 | Correct baggage-carrying adoption. This is exactly the kind of prior-art name that should remain untouched. |
| [concept: the minimum-sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover] | reentry threshold | name-unnamed | +1 | This concept recurs across context-turnover and model-preservation. It deserves a short noun phrase instead of repeated paraphrase. [original phrasing: unnamed: minimum sufficiency required after a session rebuild] |
| [unnamed: the Class-1-sub-agents -> Class-3-composite phenomenon in strategic composition] | strategic entanglement | name-unnamed | +1 | Useful noun for a real phenomenon: individually modular agents can create a non-modular composite through mutual modeling and opposed goals. |
| #graph-structure-uniqueness | #strategy-dag-sufficiency | rename | +3 | The segment explicitly proves sufficiency, not necessity. "Uniqueness" overclaims, while "strategy DAG" names the actual object. |
| #graph-structure-uniqueness | #graph-structure-sufficiency | rename | -1 | Better epistemically than "uniqueness" but still too generic; the reader needs to know this is about the strategy DAG. |
| #ciy-unified-objective | value-information objective | rename | +3 | The durable idea is a joint value-plus-information policy objective. Leading with "CIY" hides the structure behind house jargon. |
| #causal-information-yield | #causal-information-yield | keep | +3 | Long, but exact and reusable. The acronym earns its keep because the concept recurs across exploration, querying, and trust. |
| #composition-closure | #coarse-graining closure | rename | +3 | The defining move is approximate commutation with coarse-graining. "Composition closure" is too generic to carry that. |
| #critical-mass-composition | #critical-mass-composition | keep | +3 | Vivid and mathematically honest: a threshold at which composition starts to persist. Strong keep. |
| #shared-intent | #shared-intent | keep | +3 | Compact, portable, and directly connected to the commander's-intent analogy. This already sounds like a concept, not a paper section. |
| #auftragstaktik-principle | #mission-command principle | rename | +1 | The current German term is exact but creates unnecessary lookup cost. The English doctrine term keeps the baggage while lowering entry cost. |
| #auftragstaktik-principle | #objective-first bandwidth principle | rename | -1 | Accurate-ish but too explanatory and strips away the doctrinal lineage that gives the claim its empirical grounding. |
| #communication-gain | #communication-gain | keep | +3 | Excellent parallel with update gain: short, compositional, and immediately predictive of meaning. |
| #change-expectation-baseline | #change-expectation-baseline | keep | +3 | Exact, memorable, and appropriately conservative. This is one of TST's cleaner names. |
| #dual-optimization | comprehension-implementation optimization | rename | +1 | "Dual optimization" is pure abstraction. The contribution is jointly optimizing future comprehension and implementation cost, and the name should say that. |
| #specification-bound | #specification-bound | keep | +3 | Strong theorem-style name: short, honest, and portable across prose and examples. |
| #conceptual-alignment | #conceptual-alignment | keep | +3 | Good permanent name. It is legible to software people and faithful to the domain-model argument. |
| #software-epistemic-properties | software as calibration laboratory | rename | +1 | The current title is accurate but inventory-like. The segment's memorable claim is that software is AAD's calibration lab. |
| #developer-as-act-agent | #developer-as-aad-agent | rename | +3 | The slug should match the segment heading and avoid the unexplained "act" abbreviation. The expansion cost is needless here. |
| #ai-agent-as-act-agent | #ai-agent-as-aad-agent | rename | +3 | Same issue as the developer segment: the slug should not force readers to remember an internal shortening. |
| #coupled-update-dynamics | #coupled-update-dynamics | keep | +1 | Slightly textbook, but it says exactly what the logogenic section needs and pairs cleanly with directed separation. |
| #section-ii-survival | #section-ii carryover classification | rename | +1 | "Survival" is a bit cute for what is really a transfer analysis of which Section II claims carry over to Class 2 agents. |
| #system-coherence | change coherence | rename | +1 | The quantity is about change locality within a module, not coherence in a broad philosophical sense. The shorter name better matches the measure. |
| #system-coupling | #system-coupling | keep | +1 | Standard enough to keep, especially as the paired opposite of coherence. Renaming risks churn with little gain. |
| #causal-discovery-from-git | #causal-discovery-from-git | keep | +1 | Slightly long, but concrete and honest. This is exactly the sort of hypothesis title that should not be made more clever. |
| README.md "## Cross-Domain Joining" | README.md "## Cross-Domain Mappings" | rename | +3 | The section is a mapping table, not a process description. "Mappings" is plainer and more reusable. |
| README.md "## Convergent Choices" | README.md "## Convergent Formulations" | rename | +3 | Better names what the section is about: representational choices that convergence pressure made non-arbitrary. |
| README.md "## Maturity Gradient" | README.md "## Theory Maturity Gradient" | rename | +1 | Adds just enough specificity to stop the heading from sounding like a generic project-health label. |
| 02-tst-core/OUTLINE.md "## Software as Agentic Domain" | 02-tst-core/OUTLINE.md "## Software as Agentic Domain" | keep | +3 | Clear, ambitious, and accurate. This heading earns its weight. |
| [concept: the architectural requirement that composite-agent admissibility inherit from sub-agent properties plus topology] | heredity commitment | name-unnamed | +3 | Strong name from the jacobian-strengthening spike: short, memorable, and explicit about the architectural bet being made. [original phrasing: unnamed: stronger composition-consistency demand that composite admissibility inherit from sub-agent properties plus topology] |
| [concept: the prose form of κ_cross — the coupling between an agent's model-of-self and its model-of-other] | cross-model coupling | name-unnamed | +3 | Clean English complement to kappa_processing. This gives the opacity and theory-of-mind work a reusable noun slot. [original phrasing: unnamed: coupling between an agent's model-of-self and model-of-other, the prose form of kappa_cross] |
| [unnamed: git-recorded committed-state subset of the chronica, $\mathcal{C}_t^{\text{commit}}$] | commit chronica | name-unnamed | +1 | Slightly stylized, but useful. The committed slice shows up often enough in the git/chronica work to deserve a short handle. |
| [concept: the engineering-vocabulary failure mode in #consolidation-dynamics — the parameter region where forgetting and learning rates jointly fail to admit a viable operating point] | stability-plasticity collapse | name-unnamed | +1 | The failure mode is precisely that the feasible interval disappears. Slightly long, but honest and reusable. [original phrasing: unnamed: empty stability-plasticity feasibility window in #consolidation-dynamics] |
| [concept: the fourth diagnostic in the satisfaction-gap × control-regret space — when end-conditions are met but the objective remains unsatisfied] | terminal alignment error | name-unnamed | +1 | The DAG-type-closure spike identifies a real gap in the diagnostic vocabulary. This name is plain, disciplined, and fits the existing apparatus. [original phrasing: unnamed: fourth diagnostic where terminal conditions are met but the objective is still missed] |
| [future segment: information-theoretic cost floor for persistence] | #persistence-cost | name-unnamed | +1 | Best of the spike's candidates: broad enough to absorb later extensions without misdescribing the current result. |
| epistemic architecture | epistemic architecture | keep | +3 | This is the right umbrella for AAD's distinctive contribution: it names the organization of scope, proof ceilings, and escape routes, not just the integrated ingredients. |
| scope-honesty-as-architecture | scope-honesty-as-architecture | keep | +1 | Hyphen-heavy, but uniquely exact. The phrase says the limits are part of the construction, not editorial cleanup. |
| scope-honesty-as-architecture | architectural scope honesty | rename | +1 | Slightly cleaner in prose while preserving the key point that scope is surfaced structurally. |
| [working-vocabulary observation: the framework's honesty is load-bearing] | load-bearing honesty | name-unnamed | +1 | Useful short handle for review and framing prose, as long as it stays downstream of the fuller architectural phrase. |
| strengthen-first-then-soften posture | strengthen-first posture | rename | +3 | The mnemonic is in the first half. "Then soften" is still the policy, but it does not need to sit in the name. |
| [concept: the slogan capturing AAD's organizing principle that an adaptive system's correction rate must exceed its target's change rate] | contraction-over-drift principle | name-unnamed | +3 | The slogan is too long to cite repeatedly. A short label would let intros and reviews point back to it cleanly. [original phrasing: unnamed: organizing-principle slogan "an adaptive system is a projection whose contraction rate exceeds its target's drift rate"] |
| calibration-laboratory domain instantiation | calibration-lab framing | rename | +1 | Better as framing language than as a formal category label. The idea is excellent; the phrase can be lighter. |
| privileged high-identifiability calibration laboratory | high-identifiability calibration lab | rename | +1 | Keeps the identification point while reducing adjective drag in repeated prose. |
| transfer-assumption table | transfer-assumption table | keep | +3 | Exact and operational. This is the phrase readers need when moving results out of software into weaker-identification domains. |
| derivation-audit tables | derivation-audit tables | keep | +3 | Strong keep. This names a concrete artifact and a valuable house practice at the same time. |
| [symbol default: (PI) parameterization-invariance axiom] | parameterization invariance | name-unnamed | +3 | In prose, the durable concept is the invariance commitment, not the parenthetical acronym or the "axiom" suffix. Save `(PI)` for formulas and tables. |
| [symbol default: (PI) parameterization-invariance axiom] | coordinate invariance | name-unnamed | -1 | Too broad. It loses the fact that the issue is reparameterizing the model state, not arbitrary geometric invariance. |
| A2' sub-scope partition | sector-scope partition | add-alias | +3 | Much cheaper in prose than theorem-label-plus-apostrophe. The reader needs to know this is the sector-condition scope split. |
| [symbol default: DA2'-inc] | incremental sector bound | name-unnamed | +3 | `#composition-closure` already gives the English. Use the symbol only where the exact algebraic condition matters. |
| DA2'-inc ≡ (CT2)-at-M=I equivalence | sector-contraction equivalence | rename | +3 | The point is the equivalence between the incremental sector bound and Euclidean contraction. The current label reads like notebook shorthand. |
| [unnamed: the #agent-identity commitment that AAD applies on one singular, non-forkable causal trajectory] | singular-trajectory commitment | name-unnamed | +3 | Short, exact, and load-bearing across agent identity, sufficiency, and loop-interventional access. |
| [unnamed: the #agent-identity commitment that AAD applies on one singular, non-forkable causal trajectory] | trajectory singularity | name-unnamed | -1 | The concept is right, but the phrase sounds pathological rather than architectural. |
| [symbol default: M_t in prose] | model state | name-unnamed | +1 | Good neutral default when the argument is about sufficiency, persistence, or update mechanics rather than worldview. |
| [symbol default: G_t in prose] | purposeful state | name-unnamed | +1 | Better than "goal state" because it includes both objective and strategy. This matches the repo's actual decomposition. |
| [symbol default: Sigma_t in prose] | strategy | name-unnamed | +3 | After first introduction, the English should be the prose default. The symbol is still right in equations and exact statements. |
| 1-anchor-plus-3-theorem | 1-anchor-plus-3-theorem | keep | +3 | Awkward-looking but very valuable. It preserves the asymmetry between the chain identity and the three theorem-level layers. |
| separable core / structured repair / general open | separable core / structured repair / general open | keep | +1 | A little essayistic, but this triad already does real explanatory work in the separability meta-pattern and should remain literal. |
| [symbol default: bias-bound Track 1 / Track 2] | transport track / Fisher track | name-unnamed | +1 | If these labels survive in framing prose, they should expose the real distinction instead of forcing readers to remember which numbered track is which. |

## Principles Observations

- The principles cover memorability and baggage well, but they under-specify acronym discipline. This repo already carries enough acronym load that each new one is now costly.
- The principles mention symbol names, but not mixed symbol/prose drift. Several important distinctions already have good English names and should probably default to English in prose once introduced.
- Greek-vocabulary evaluation probably deserves to be explicit. In this repo the right test is not "Greek or English?" but "does the Greek preserve a distinction English would flatten?"

## Additional Feedback

- The repo now clearly has **three naming layers** that should probably be governed explicitly rather than implicitly: `(1)` formal segment/slugs, `(2)` prose defaults for symbols and theorem labels, `(3)` framing/posture vocabulary for the methodology. A lot of current friction comes from mixing those layers.
- The strongest names in the repo tend to name the **object, regime, or failure mode**. The weakest names tend to name the **proof device, theorem label, or internal notebook handle**. As a default bias: public-facing names should expose the thing the reader reasons about, not the machinery that happened to prove it.
- A recurring failure mode is **theorem-polarity overclaim**: names like `uniqueness`, generic `framework`, or symbol-only labels can silently claim more than the segment proves. This is not fully handled by Epistemic Status alone. Naming review should explicitly ask: "does the title overstate sufficiency/necessity/exactness?"
- The repo would benefit from a lightweight **prose-default policy**: after first introduction, prefer English over symbols in running text unless the symbol itself is doing real mathematical work. The high-value candidates are already visible from this sweep: `parameterization invariance`, `sector-scope partition`, `incremental sector bound`, `singular-trajectory commitment`, `purposeful state`.
- Framework-facing headings deserve the same naming rigor as theorem segments. For cold-start readers, README/OUTLINE headings are part of the theory's interface, not decoration. Several of the best leverage renames in this sweep were heading-level, not segment-level.
- There is enough recurring unnamed content now that a small **reserved prose-handle layer** may be worth formalizing somewhere (`LEXICON.md` or a naming appendix): `reentry threshold`, `heredity commitment`, `cross-model coupling`, `contraction-over-drift principle`, `terminal alignment error`, and similar handles that are useful across multiple segments.
- AAD appears to have an emergent and mostly successful **register split**: Greek/philosophical names for foundational experiential distinctions, plain engineering English for diagnostics/bounds/failure modes, and symbolic labels only where exact formal reference matters. Making that split explicit would help future naming work stay coherent.
