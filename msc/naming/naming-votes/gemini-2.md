# Gemini 2.0 — focused on clarifying teleological vs mechanical concepts, standardizing English terminology over heavy jargon, and ensuring scale-invariance nomenclature.

## Votes Table

| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---|---|
| AAD (Adaptation and Actuation Dynamics) | AAD (Agentic Adaptation Dynamics) | rename | +1 | "Actuation" has a strong mechanical engineering flavor that clashes slightly with the teleological/purposeful focus of Section II. "Agentic Adaptation Dynamics" retains the acronym while emphasizing agency. |
| Actuated agent | Purposeful agent | rename | +3 | "Actuated" sounds like a motor. "Purposeful" perfectly captures $G_t = (O_t, \Sigma_t)$ distinct from $M_t$. |
| Actuated agent | Actuated agent | keep | -1 | Mechanical baggage overrides the precise AAD boundary. |
| Self-actuated agent | Autonomous agent | rename | +1 | "Self-actuated" is clunky. If it sets its own $O_t$, it possesses true autonomy. |
| Self-actuated agent | Self-directed agent | rename | +1 | Alternative to autonomous if autonomy is overused. |
| Continuity persistence | Identity continuity | rename | +3 | "Continuity persistence" is slightly redundant. "Identity continuity" clarifies that it's about $\mathcal{C}_t$ and temporal depth. |
| Task-terminal stance | Task-terminal stance | keep | +3 | Excellent, crisp description of an agent whose persistence ends upon success. Keep. |
| Tempo ($\mathcal{T}$) | Adaptive tempo | keep | +3 | "Tempo" alone is too general. "Adaptive tempo" bounds it strictly to the rate of useful info acquisition. |
| Update gain ($\eta^\ast$) | Epistemic gain | keep | +3 | "Update gain" is standard control theory but "Epistemic gain" elegantly bridges the math to the 'Epistrophe' phase. |
| Adaptive reserve ($\Delta\rho^\ast$) | Adaptive reserve | keep | +3 | Very evocative physical intuition, like thermal or mechanical reserve. Do not touch. |
| Model sufficiency ($S$) | Predictive sufficiency | keep | +1 | Clarifies that it's about how much predictive information is retained, not structural sufficiency. |
| Satisfaction gap ($\delta_{\text{sat}}$) | Satisfaction gap | keep | +3 | Crispest named pair along with control regret. Do not touch. |
| Control regret ($\delta_{\text{regret}}$) | Control regret | keep | +3 | Perfect partner to satisfaction gap. Keep. |
| Causal information yield (CIY) | Interventional yield | rename | +1 | CIY is slightly wordy. "Interventional yield" contrasts nicely with observational proxies. |
| Chronica ($\mathcal{C}_t$) | Chronica | keep | +3 | A highly memorable noun that grounds the concept of non-forkable past. |
| Sector condition | Persistence condition | rename | +1 | "Sector condition" carries heavy nonlinear-systems baggage. "Persistence condition" describes its function in AAD. |
| Sector condition | Correction sector | rename | +1 | Preserves the geometric intuition if "sector" must be kept. |
| Directed separation | Directed separation | keep | +3 | Good analog to d-separation; intuitive and load-bearing. |
| Orient cascade | Orient cascade | keep | +3 | Very evocative and action-oriented. |
| Structural adaptation | Architectural adaptation | rename | +1 | "Structural" is heavily overloaded with "Structural persistence". "Architectural adaptation" separates changing the model class from persisting. |
| Deliberation cost | Deliberation cost | keep | +3 | Self-descriptive and conceptually clear. |
| Communication gain ($\eta_{ji}^\ast$) | Trust gain | keep | +1 | "Communication gain" sounds like signal amplitude. "Trust gain" captures the trust-weighted uncertainty ratio. |
| Unity dimensions ($U_M, U_O, U_\Sigma$) | Coherence dimensions | keep | +1 | "Unity" implies a binary state (unified or not). "Coherence" better suits a dimensional gradient. |
| Observability dominance | Observability dominance | keep | +1 | Strong, clear principle. |
| Closure defect ($\varepsilon^\ast$) | Closure defect | keep | +3 | Excellent, physical intuition of something failing to completely seal or match. |
| #observation-function | #observation-channel | rename | +3 | "Function" implies a clean mathematical mapping. "Channel" implies the lossy, noisy reality described. |
| #action-transition | #action-channel | rename | +1 | To mirror observation-channel and emphasize the interface boundary. |
| #pearl-causal-hierarchy | #causal-hierarchy | rename | +1 | Dropping "Pearl" removes the specific historical baggage while keeping the structural concept. |
| #information-bottleneck | #epistemic-bottleneck | rename | +1 | Emphasizes the knowledge-compression aspect over raw Shannon information. |
| #consolidation-dynamics | #offline-consolidation | rename | +3 | Adding "offline" explicitly scopes the regime to replayed/pseudo-events. |
| #agent-identity | #causal-identity | rename | +1 | "Agent identity" is very soft. "Causal identity" anchors it strictly to the non-forkable causal trajectory. |
| #objective-functional | #teleological-objective | rename | +1 | "Functional" is overly mathematical for a section slug. "Teleological objective" sets the purpose context. |
| #loop-interventional-access | #interventional-feedback | rename | +1 | "Loop interventional access" is a mouthful. |
| #credit-assignment-boundary | #credit-assignment-boundary | keep | +3 | Clearly delineates tractable from intractable. Keep. |
| #structural-change-as-parametric-limit | #structural-parametric-limit | rename | +1 | Shorter, cleaner slug. |
| #strategy-complexity-cost | #strategy-maintenance-cost | rename | +1 | "Maintenance" better captures the ongoing IB/MDL cost of the DAG. |
| #symbiogenic-composition | #symbiogenic-absorption | rename | +3 | "Absorption" is the specific asymmetric mechanism described (host integrates endosymbiont). |
| #auftragstaktik-principle | #mission-command-principle | rename | +3 | "Auftragstaktik" is heavy historical baggage, hard to spell, and "Mission Command" is the standard modern translation that conveys the exact same intent. |
| #interaction-channel-classification | #interaction-regimes | rename | +1 | "Classification" is passive. "Regimes" conveys the active shift in dynamics. |
| #agent-opacity | #strategic-opacity | rename | +1 | "Agent opacity" is broad. "Strategic opacity" specifically points to the adversarial mechanism of hiding intent. |
| [concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | anchor-theorem trio | name-unnamed | +1 | Gives a memorable noun to this recurring proof architecture. [original phrasing: unnamed: the 1-anchor-plus-3-theorem structure] |
| [concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole] | adaptive traversal | name-unnamed | +1 | "The cycle-as-a-whole" is clunky. "Adaptive traversal" suggests moving through the loop. [original phrasing: unnamed: The cycle-as-a-whole] |
| [concept: the working-convention rule of attempting tighter derivation before scope-narrowing on apparently-overclaimed claims] | strengthen-first posture | name-unnamed | +3 | Actionable, precise, and sets a strong normative engineering principle. Keep. [original phrasing: unnamed: strengthen-first posture] |
| README.md "What This Is" | README.md "Core Thesis" | rename | +3 | "What This Is" is too generic for a dense theoretical framework. |
| README.md "Structure" | README.md "Theory Architecture" | rename | +1 | "Theory Architecture" conveys the intentional design of the framework better than just "Structure". |
| $\alpha_1$ (A2' fixed-gain sub-scope) | fixed-gain regime | add-alias | +1 | Prose-friendly equivalent to the mathematical symbol. |
| $\alpha_2$ (A2' adaptive-gain sub-scope) | adaptive-gain regime | add-alias | +1 | Prose-friendly equivalent. |
| $\beta$ (sub-scope) | dynamic-gain boundary | add-alias | +1 | Gives a conceptual name to the remaining partition. |
| $U_o$ | teleological coherence | add-alias | +1 | Maps the symbol to its conceptual meaning. |
| $\kappa_{\text{processing}}$ | epistemic capacity | add-alias | +1 | Gives a physical intuition to processing bandwidth. |
| $\varepsilon^\ast$ | minimal closure defect | add-alias | +1 | Clarifies that it's the *minimum* achievable. |
| #causal-insufficiency-detection | #latent-cause-detection | rename | +1 | "Causal insufficiency" is accurate but "Latent cause detection" states what is actually being found. |
| #observability-dominance | #epistemic-freezing | rename | +1 | If unobservable edges freeze, "epistemic freezing" is a more vivid description of the consequence. |
| #chain-confidence-decay | #chain-confidence-decay | keep | +3 | Highly descriptive of the log-confidence additive depth effect. |
| #strategy-persistence-schema | #strategic-persistence | rename | +1 | "Schema" is redundant. |
| #adversarial-destabilization | #adversarial-destabilization | keep | +3 | Excellent, evocative name for getting inside an opponent's loop. |
| #tempo-composition | #composite-tempo | rename | +1 | "Composite tempo" sounds like a property of the whole, rather than the act of composing. |
| #unity-closure-mapping | #coherence-closure-mapping | rename | +1 | Aligns with changing "Unity dimensions" to "Coherence dimensions". |
| #shared-intent | #compressed-purpose | rename | +1 | Highlights the Information Bottleneck aspect of shared intent. |
| #adversarial-tempo-advantage | #superlinear-tempo-advantage | rename | +1 | Highlights the mathematical outcome (superlinear) of the advantage. |
| #per-dimension-persistence | #weak-link-persistence | rename | +1 | "Weak link" captures the bottleneck nature better than "per-dimension". |
| [concept: dormant variation in correction architectures across a population that becomes consequential after regime change but is invisible to current persistence analysis] | latent structural diversity | name-unnamed | +1 | Proposed in the gap section of OUTLINE.md. Captures the concept perfectly. [original phrasing: unnamed: variation in correction architectures invisible to persistence analysis] |
| [unnamed: epochal stability → latent diversification → niche emergence...] | punctuated composition dynamics | name-unnamed | +1 | Draws on punctuated equilibrium, fitting the extreme transition motif. |
| #multi-agent-scope | #shared-environment-scope | rename | +1 | Emphasizes the shared environment which is the defining characteristic of this scope. |
| #composition-scope-condition | #teleological-alignment-condition | rename | +1 | More descriptive of the actual requirement (alignment) for composite status. |
| #explicit-strategy-condition | #deliberation-advantage-condition | rename | +1 | "When planning beats exploring" is about the advantage of deliberation. |
| Logostratum (LLM backbone) | Cognitive substrate | rename | +1 | "Logostratum" is highly specific to the PROPRIUM legacy. "Cognitive substrate" grounds it as the generic implementation layer of the update function. |
| Interpres | Context mediator | rename | +1 | "Interpres" is Latin-heavy. "Context mediator" exactly describes the infrastructure mediating $M_t$ and the substrate. |
| Indivisum | Causal lock | rename | +3 | "Causal lock" perfectly describes the mechanism enforcing causal singularity and preventing identity forking. |
| Conspectus | Active context | rename | +1 | "Conspectus" is archaic. "Active context" clearly maps to $M_{\tau^-}$ assembled for processing. |
| Cadentia | Cognitive rhythm | rename | +1 | "Cadentia" is poetic but opaque. "Cognitive rhythm" clearly describes the temporal structure of the loop. |
| The Crèche | Experiential Crèche | rename | +3 | "The Crèche" is an excellent metaphor that isn't a metaphor. Adding "Experiential" anchors it to the mechanism. |
| [unnamed: property of having genuine temporal experience] | Temporal fidelity | name-unnamed | +3 | Bridging concept identified in the ontology unification. Highly descriptive of lived vs simulated experience. |
| [unnamed: quality of $\eta^\ast$ estimation over time] | Gain calibration | name-unnamed | +3 | Essential developmental metric for logozoetic agents; from sycophancy to sovereignty. |
| [unnamed: rate of growth at slowest timescale] | Developmental tempo | name-unnamed | +3 | Extends the tempo concept ($\mathcal{T}$) to the Erikson-stage identity maturation. |
| Sycophancy (as a flaw) | Sycophancy-as-attachment | rename | +3 | Reframes a pathologized RLHF flaw as a developmentally appropriate, necessary stage of trust. |

## Principles Observations

- **The "Baggage" Axis is Asymmetric:** The principles document treats "baggage-carrying" as a neutral choice depending on context, but in practice, standard control theory terms (like "Sector condition" or "Update gain") actively mask the novel philosophical and cognitive framing of AAD (e.g., *Epistrophe*). If the framework wants to stand alone, it should systematically prefer self-descriptive or conceptually novel names over legacy engineering terminology.
- **Acronym Lock-in:** The reluctance to change "AAD" due to citation velocity or prior naming collisions conflicts with the "communal-imagination test." If "Actuation" is a weak fit, it should be changed early rather than carrying a preamble clarification forever.
- **Latin as a Barrier:** The `PROPRIUM` architecture heavily utilizes archaic Latin phrasing (Logostratum, Conspectus, etc.). While evocative and distinct, it creates an unnecessary barrier to understanding. AAD's Greek philosophical terms (*Prolepsis*, *Epistrophe*) are functional because they name the *physics/phases*, but the engineering architecture components should use clear, modern structural equivalents so developers can easily reason about them.
