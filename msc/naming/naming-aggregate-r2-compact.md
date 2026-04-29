# Naming Vote Aggregation — Compact Table

**Agents:** 16 (agent1-original-brainstorm, audit-471203-incremental, codex-1, codex-2, codex-gpt-5-r2, gemini-1, gemini-2, gemini-3-1-pro-preview-r2, haiku-4-5, haiku-4-5-r2, opus-1m, opus-4-7, opus-4-7-b, opus-4-7-r2, sonnet-4-6, sonnet-4-6-r2)
**Total vote rows:** 2165
**Distinct (current, candidate) pairs:** 1295
**Distinct current-names voted on:** 979

Single-table view: one row per (original, candidate) pair, with aggregate weight. Rows for the same `original` are grouped adjacently; the original cell is shown only on the first row of each group; groups are sorted by their top alternative's aggregate weight (descending). The first row of each group is the **winning** candidate (bolded). Where candidate = original the cell shows `_(keep)_`, suffixed with ⭑ if at least one vote on that row used the `canonicalize` category. Net-rejected candidates (aggregate < 0) prefixed with ✗. Category and per-agent notes elided — see `--format=review` for those.

| original | candidate | aggregate |
|---|---|---:|
| control regret | **_(keep)_ ⭑** | +48 |
| satisfaction gap | **_(keep)_ ⭑** | +48 |
| orient cascade | **_(keep)_ ⭑** | +47 |
| directed separation | **_(keep)_ ⭑** | +45 |
|  | goal-blind processing pearl-blanket separation epistemic isolation of belief update | +1 |
| identifiability floor | **_(keep)_** | +45 |
|  | ✗ no-go theorems | -1 |
| information bottleneck | **_(keep)_** | +28 |
|  | keep formal name AAD distinctive feature deserves separate label | +2 |
|  | epistemic bottleneck | +1 |
| chronica | **_(keep)_ ⭑** | +27 |
| persistence condition | **_(keep)_ ⭑** | +27 |
|  | survival equation | +1 |
| strategy DAG | **_(keep)_ ⭑** | +26 |
|  | keep | +2 |
| chain confidence decay | **_(keep)_** | +25 |
|  | keep load bearing | +2 |
|  | log confidence additive | +1 |
| symbiogenic composition | **_(keep)_** | +24 |
|  | symbiogenic absorption | +3 |
|  | asymmetric absorption | +1 |
| additive coordinate forcing | **forced coordinates** | +23 |
|  | coordinate forcing | +12 |
|  | uniqueness coordinate forcing | +5 |
|  | _(keep)_ | +1 |
|  | uniqueness coordinates | +1 |
|  | ✗ logarithmic lift | -1 |
|  | ✗ log coordinate forcing | -1 |
|  | ✗ anchor lattice | -1 |
|  | ✗ additive lift | -2 |
|  | ✗ axiom forcing | -2 |
|  | ✗ cauchy coordinates | -4 |
| sector persistence template | **_(keep)_** | +23 |
|  | bounded correction template | +5 |
|  | persistence template | +0 |
| temporal optimality | **_(keep)_** | +23 |
| adversarial destabilization | **_(keep)_** | +22 |
| agent spectrum | **_(keep)_ ⭑** | +22 |
|  | agency spectrum | +1 |
|  | ✗ agent quadrants | -1 |
| adaptive reserve $\Delta\rho^\ast$ | **adaptive reserve** | +21 |
| shared intent | **_(keep)_** | +21 |
|  | teleological unity | +1 |
|  | compressed purpose | +1 |
|  | keep def shared intent | +1 |
| AAD adaptation and actuation dynamics | **_(keep)_** | +20 |
|  | AAD | +3 |
|  | AAD agentic adaptation dynamics | +1 |
| adaptive tempo | **_(keep)_ ⭑** | +20 |
|  | ✗ adaptation rate | -1 |
| agent opacity | **_(keep)_** | +20 |
|  | emitter opacity | +1 |
|  | strategic opacity | +0 |
| causal information yield | **_(keep)_ ⭑** | +20 |
|  | CIY | +2 |
| separability pattern | **separability ladder** | +20 |
|  | _(keep)_ | +10 |
|  | separability ladders | +2 |
|  | ✗ tiered separability | -1 |
|  | ✗ staircase | -1 |
|  | ✗ separable core | -1 |
|  | ✗ three rung posture | -1 |
|  | ✗ separability staircase | -5 |
| composition closure | **_(keep)_ ⭑** | +19 |
|  | coarse graining closure | +5 |
|  | closure defect | +1 |
|  | ✗ macro agent criterion | -1 |
| auftragstaktik principle | **_(keep)_** | +18 |
|  | mission command principle | +3 |
|  | mission command | +2 |
|  | auftragstaktik | +2 |
|  | auftragstaktik bandwidth | +1 |
|  | mission command bandwidth | +1 |
|  | ✗ objective first bandwidth principle | -1 |
|  | ✗ auftragstaktik drop principle | -1 |
| communication gain | **_(keep)_** | +18 |
|  | ✗ trust gain | -1 |
| context turnover | **_(keep)_** | +18 |
|  | chronica severance | +6 |
| contraction template | **_(keep)_** | +18 |
|  | contraction schema | +1 |
| deliberation cost | **_(keep)_** | +18 |
|  | deliberation threshold think vs act tradeoff | +1 |
|  | deliberation drag | +1 |
| logogenic agent | **_(keep)_ ⭑** | +18 |
|  | ✗ linguistic agent | -1 |
| observability dominance | **_(keep)_ ⭑** | +18 |
|  | epistemic freezing | +1 |
| team persistence | **_(keep)_** | +18 |
| credit assignment boundary | **_(keep)_** | +17 |
|  | credit assignment frontier | +1 |
| honesty as architecture | **_(keep)_** | +17 |
|  | honesty | +2 |
|  | architectural scope honesty | +1 |
| approximation tiering | **_(keep)_** | +16 |
|  | tiered approximation | +1 |
|  | approximation ladders | +1 |
|  | scope laddering | +1 |
|  | ✗ graceful degradation | -1 |
|  | ✗ tier ascension | -1 |
| recursive update | **_(keep)_** | +16 |
|  | recursive update by completeness | +2 |
| agent identity | **_(keep)_** | +15 |
|  | identity as singular causal trajectory the trajectory identity scope | +3 |
|  | singular causal trajectory | +2 |
|  | trajectory identity | +1 |
|  | causal identity | +1 |
| consolidation dynamics | **_(keep)_** | +15 |
|  | offline consolidation | +3 |
| critical mass composition | **_(keep)_** | +15 |
|  | dyad closed form | +1 |
| exploit explore deliberate | **_(keep)_** | +15 |
|  | cycle budget allocation | +3 |
|  | action timing tradeoff | +2 |
|  | cycle budget | +2 |
| gain sector bridge | **_(keep)_** | +15 |
|  | bridge theorem from gain to sector the bridge theorem grounding ga 3 sub scope α and β | +2 |
| adversarial tempo advantage | **_(keep)_** | +14 |
|  | superlinear tempo advantage | +1 |
|  | tempo advantage | +1 |
| atomic changeset | **_(keep)_** | +14 |
| complete agent state | **_(keep)_** | +14 |
|  | purposeful state | +1 |
| detection latency | **_(keep)_** | +14 |
| loop interventional access | **_(keep)_** | +14 |
|  | loop as causal engine | +2 |
|  | loop causal engine | +2 |
|  | interventional loop access | +1 |
|  | interventional feedback | +1 |
|  | adaptive loop access | +1 |
|  | ✗ loop level2 access | -1 |
| composition consistency | **_(keep)_** | +13 |
|  | cross level coherence scale invariance of adaptive dynamics holon postulate | +1 |
|  | scale invariance | +1 |
| compression operations | **_(keep)_** | +13 |
|  | history compression | +1 |
|  | ✗ OODA1 unification | -1 |
| epistemic architecture | **_(keep)_ ⭑** | +13 |
| specification bound | **_(keep)_** | +13 |
| aporia | **_(keep)_** | +12 |
| chronica $\mathcal{C}_t$ | **chronica** | +12 |
| conceptual alignment | **_(keep)_** | +12 |
| epistemic status | **_(keep)_** | +12 |
| logogenic logozoetic | **_(keep)_** | +12 |
| m preservation | **model preservation** | +12 |
|  | epistemic externalization | +4 |
|  | _(keep)_ | +1 |
| pearl causal hierarchy | **_(keep)_** | +12 |
|  | causal hierarchy | +1 |
| persistence cost | **_(keep)_** | +12 |
| strategic calibration | **_(keep)_** | +12 |
|  | strategic calibration residual | +2 |
|  | strategy calibration | +1 |
| strategic composition | **equilibrium composition** | +12 |
|  | _(keep)_ | +9 |
|  | ✗ game theoretic composition | -5 |
| strategic tempo | **_(keep)_** | +12 |
| unity dimensions | **_(keep)_** | +12 |
|  | unity axes | +4 |
|  | ✗ coherence dimensions | -1 |
|  | ✗ content and structural unity | -1 |
| update gain $\eta^\ast$ | **update gain** | +12 |
|  | epistemic gain | +3 |
| working notes | **_(keep)_** | +12 |
| adaptive reserve | **_(keep)_ ⭑** | +11 |
| agent environment | **_(keep)_** | +11 |
|  | agent environment boundary | +1 |
| changeset size principle | **_(keep)_** | +11 |
|  | changeset size scaling | +2 |
| independence audit | **_(keep)_** | +11 |
|  | independence floor | +1 |
| mismatch signal | **_(keep)_** | +11 |
|  | ✗ aporia signal | -2 |
| model sufficiency | **_(keep)_** | +11 |
|  | predictive sufficiency predictive information retention | +1 |
| moral continuity | **_(keep)_** | +11 |
| sector condition | **_(keep)_ ⭑** | +11 |
|  | persistence condition | +1 |
|  | correction sector | +1 |
| $\varepsilon^\ast$ closure defect | **closure defect** | +10 |
| closure defect $\varepsilon^\ast$ | **closure defect** | +10 |
| code quality as observation infrastructure | **observation infrastructure** | +10 |
|  | _(keep)_ | +5 |
| comprehension time | **_(keep)_** | +10 |
| mismatch decomposition | **_(keep)_** | +10 |
|  | aporia decomposition | +2 |
| model class fitness | **_(keep)_ ⭑** | +10 |
|  | class capacity ceiling | +1 |
| objective functional | **_(keep)_** | +10 |
|  | teleological objective | +1 |
| software epistemic properties | **_(keep)_** | +10 |
|  | software as calibration laboratory | +1 |
| strengthen first posture | **_(keep)_ ⭑** | +10 |
|  | strengthen first | +3 |
|  | attempt the improbable | +0 |
| $\Delta\rho^\ast$ | **adaptive reserve** | +9 |
| $\Delta\rho^\ast$ adaptive reserve | **adaptive reserve** | +9 |
| $\alpha_2$ a2 adaptive gain sub scope | **adaptive gain regime** | +9 |
| OODA4 agent as act agent | **OODA4 agent as adaptive agent** | +9 |
|  | OODA4 agent as AAD agent | +6 |
|  | ✗ logogenic agent mapping | -1 |
| agency | **_(keep)_** | +9 |
| agent model | **_(keep)_** | +9 |
|  | reality model | +1 |
| calibration laboratory | **_(keep)_ ⭑** | +9 |
| causal hierarchy requirement | **_(keep)_** | +9 |
|  | hierarchy necessity | +1 |
| causal insufficiency detection | **_(keep)_** | +9 |
|  | l0 l1 detection | +5 |
|  | latent cause detection | +2 |
|  | insufficiency detection | +1 |
|  | keep not der l0 l1 detection | +1 |
| convention hierarchy c1 c2 c3 | **convention hierarchy** | +9 |
|  | continuation hierarchy | +2 |
| developer as act agent | **developer as adaptive agent** | +9 |
|  | developer as AAD agent | +4 |
|  | developer agent mapping | +1 |
|  | ✗ developer as agent | -1 |
| event driven dynamics | **_(keep)_** | +9 |
| formal expression | **_(keep)_** | +9 |
| graph structure uniqueness | **strategy DAG sufficiency** | +9 |
|  | strategy DAG uniqueness | +5 |
|  | _(keep)_ | +4 |
|  | DAG uniqueness | +2 |
|  | DAG structure derivation | +1 |
|  | ✗ graph structure sufficiency | -1 |
| interaction channel classification | **signal reception regimes** | +9 |
|  | _(keep)_ | +5 |
|  | recipient regimes | +4 |
|  | channel classification | +3 |
|  | recipient regime classification | +3 |
|  | interaction regimes | +1 |
|  | ✗ recipient side channel taxonomy | -1 |
| strategy DAG $\Sigma_t$ | **strategy DAG** | +9 |
| $\alpha_1$ a2 fixed gain sub scope | **derived gain regime** | +8 |
|  | fixed gain regime | +2 |
| composite agent | **_(keep)_** | +8 |
| coupled update dynamics | **_(keep)_** | +8 |
| mismatch dynamics | **_(keep)_** | +8 |
|  | mismatch dynamics drift and noise regimes | +1 |
| sector condition stability | **_(keep)_** | +8 |
|  | sector stability | +1 |
| structural adaptation necessity | **_(keep)_** | +8 |
|  | adaptation necessity | +2 |
| update gain | **_(keep)_** | +8 |
|  | update gain uncertainty ratio principle | +1 |
|  | ✗ epistemic gain | -1 |
| $\kappa_{\text{processing}}$ | **processing coupling** | +7 |
|  | epistemic capacity | +1 |
|  | processing coupling coefficient | +1 |
| adaptive system | **_(keep)_** | +7 |
|  | keep but flag prior art baggage | +1 |
| bias bound derivation | **_(keep)_** | +7 |
|  | class 2 bias bound | +1 |
| causal structure | **_(keep)_** | +7 |
| composition closure closure defect $\varepsilon^\ast$ | **composition closure closure defect** | +7 |
| condition | **_(keep)_** | +7 |
| correlation hierarchy l0 l1 l1 l2 | **correlation hierarchy** | +7 |
|  | correlation ladder | +2 |
|  | keep | +2 |
| discussion | **_(keep)_** | +7 |
| edge update via gain | **_(keep)_** | +7 |
|  | gain based edge update | +1 |
| interiority default | **_(keep)_** | +7 |
| proprium mapping | **_(keep)_** | +7 |
| structural adaptation | **_(keep)_** | +7 |
|  | architectural adaptation | +1 |
| temporal nesting | **_(keep)_** | +7 |
|  | timescale nesting | +1 |
|  | ✗ timescale stratification | -1 |
| value object | **_(keep)_** | +7 |
|  | policy conditioned value | +3 |
|  | decision value | +1 |
|  | trajectory value | +1 |
|  | ✗ value functional | -1 |
| variational sector condition | **_(keep)_** | +7 |
| $U_O$ teleological unity | **teleological unity** | +6 |
| action selection | **_(keep)_** | +6 |
| adaptive cycle | **_(keep)_** | +6 |
| adaptive gain dynamics | **_(keep)_** | +6 |
| adaptive tempo $\mathcal T$ | **adaptive tempo** | +6 |
| agent opacity $H_b^{A\|B}$ | **agent opacity** | +6 |
| aporia ἀπορία | **aporia** | +6 |
|  | _(keep)_ ⭑ | +1 |
| causal discovery from git | **_(keep)_** | +6 |
|  | git causal discovery | +2 |
| change distance | **_(keep)_** | +6 |
| change expectation baseline | **_(keep)_** | +6 |
|  | change baseline | +1 |
|  | lindy baseline | +1 |
| claude md what s settled vs open | **_(keep)_** | +6 |
| developer agent | **_(keep)_** | +6 |
| discussion segment section header | **discussion** | +6 |
| effects spiral | **_(keep)_** | +6 |
| epistemic status segment section header | **epistemic status** | +6 |
| evidence starvation | **_(keep)_ ⭑** | +6 |
| explicit strategy condition | **_(keep)_** | +6 |
|  | strategy explicitness | +2 |
|  | deliberation advantage condition | +1 |
|  | planning scope | +1 |
| formal expression segment section header | **formal expression** | +6 |
| implementation time | **_(keep)_** | +6 |
| logogenic | **_(keep)_** | +6 |
| logozoetic | **_(keep)_** | +6 |
| lohmiller-slotine contraction | **_(keep)_** | +6 |
| miller s meta machine extreme transition motif | **meta machine extreme transition motif** | +6 |
| pearl s causal hierarchy | **_(keep)_** | +6 |
| praxis πρᾶξις | **praxis** | +6 |
|  | _(keep)_ ⭑ | +1 |
| prolepsis aisthesis aporia epistrophe praxis | **keep whole vocabulary** | +6 |
| stability plasticity feasibility window | **_(keep)_** | +6 |
| temporal software theory | **_(keep)_** | +6 |
| working notes segment section header | **working notes** | +6 |
| $\alpha$ sector bound | **correction rate** | +5 |
| $\varepsilon^\ast$ | **closure defect** | +5 |
|  | minimal closure defect | +1 |
| actuated agent | **_(keep)_** | +5 |
|  | goal actuated agent | +2 |
|  | purposeful agent | +2 |
| actuated agent vs purposeful agent | **actuated agent** | +5 |
| change proximity principle | **_(keep)_** | +5 |
|  | change proximity | +2 |
|  | change locality principle | +1 |
| continuous operation | **_(keep)_** | +5 |
| directed separation under composition | **_(keep)_** | +5 |
|  | composite directed separation | +3 |
| experiential training | **_(keep)_** | +5 |
| l1 update bias | **_(keep)_** | +5 |
|  | l1 bias formula | +2 |
| multi agent | **_(keep)_** | +5 |
| observation function | **observation channel** | +5 |
|  | _(keep)_ | +3 |
| per dimension persistence | **_(keep)_** | +5 |
|  | dimensional persistence | +2 |
|  | weak link persistence | +1 |
|  | weakest link persistence | +1 |
| praxis | **_(keep)_** | +5 |
| prolepsis | **_(keep)_** | +5 |
| section ii survival | **_(keep)_** | +5 |
|  | section ii carryover map | +3 |
|  | class 2 carryover map | +3 |
|  | class 2 survival | +2 |
|  | class 2 exit audit | +2 |
|  | section ii carryover classification | +1 |
| strategy complexity cost | **_(keep)_** | +5 |
|  | strategy cognitive cost | +4 |
|  | strategy maintenance cost | +1 |
| strategy dimension | **purposeful decomposition** | +5 |
|  | objective strategy split | +4 |
|  | purposeful substate | +2 |
|  | strategic dimension | +1 |
|  | _(keep)_ | +1 |
|  | strategy decomposition | +1 |
| system coupling | **_(keep)_** | +5 |
|  | change coupling | +2 |
| tempo composition | **_(keep)_** | +5 |
|  | composite tempo | +1 |
|  | subadditive tempo | +1 |
| $R$ sector radius | **capacity radius** | +4 |
| $\hat P_\Sigma$ plan confidence | **plan confidence** | +4 |
| 1 anchor plus 3 theorem | **_(keep)_** | +4 |
| adversarial exponent regimes | **_(keep)_** | +4 |
|  | adversarial regimes | +2 |
| agentic systems framework ASF | **agentic systems** | +4 |
| aisthesis αἴσθησις | **aisthesis** | +4 |
|  | _(keep)_ ⭑ | +1 |
| and or | **and or combination** | +4 |
|  | strategy DAG topology | +3 |
|  | _(keep)_ | +3 |
|  | combination rule | +2 |
|  | and or semantics | +1 |
| blind pursuer | **_(keep)_** | +4 |
| causal information yield CIY | **causal information yield** | +4 |
|  | interventional yield | +2 |
| change investment | **_(keep)_** | +4 |
| claude md working conventions | **_(keep)_** | +4 |
| coherence coupling | **_(keep)_** | +4 |
|  | ✗ change architecture | -1 |
| convention hierarchy | **continuation hierarchy** | +4 |
|  | ✗ evaluation hierarchy | -1 |
| discrete sector condition | **_(keep)_** | +4 |
| edge update causal validity | **causal edge update** | +4 |
|  | _(keep)_ | +3 |
|  | edge causal validity | +2 |
|  | causal validity | +2 |
|  | identification regime | +1 |
| epistrophe | **_(keep)_** | +4 |
| epistrophe ἐπιστροφή | **epistrophe** | +4 |
|  | _(keep)_ ⭑ | +1 |
| extreme transition motif | **_(keep)_ ⭑** | +4 |
| logozoetic agent | **_(keep)_** | +4 |
|  | ✗ sentient agent | -1 |
| mismatch signal $\delta_t$ | **mismatch signal** | +4 |
| operationalization | **_(keep)_** | +4 |
| prolepsis πρόληψις | **prolepsis** | +4 |
|  | _(keep)_ ⭑ | +1 |
| recursive update derivation | **_(keep)_** | +4 |
| separable core structured repair general open | **_(keep)_** | +4 |
| software | **_(keep)_** | +4 |
|  | evolving software | +2 |
| strategy persistence | **_(keep)_** | +4 |
| system coherence | **_(keep)_** | +4 |
|  | change coherence | +3 |
| unity closure mapping | **_(keep)_** | +4 |
|  | coherence closure mapping | +1 |
|  | closure mapping | +1 |
| $H_b$ | **backward opacity** | +3 |
| $O_t$ objective | **_(keep)_** | +3 |
| $R$ sector condition radius | **model class capacity** | +3 |
| $U_M$ as model uncertainty and $U_M$ as epistemic unity | **use $U_M$ for model uncertainty and $\Upsilon_M$ for epistemic unity** | +3 |
| $U_M$ dual use model uncertainty and epistemic unity | **$U_M$ for model uncertainty $U_{\mathcal M}$ or $\Upsilon_M$ for epistemic unity** | +3 |
| $U_M$ model uncertainty | **model uncertainty** | +3 |
| $U_o$ observation uncertainty | **observation uncertainty** | +3 |
| $\Sigma_t$ strategy | **_(keep)_** | +3 |
|  | strategy | +2 |
| $\alpha$ lower sector bound | **$\alpha$ sector parameter** | +3 |
| $\alpha$ sector condition lower bound | **correction rate constant** | +3 |
|  | correction rate or decay rate | +1 |
| $\alpha_1$ $\alpha_2$ $\beta$ partition | **fixed gain adaptive gain drift regimes** | +3 |
| $\beta$ a2 assumed sector sub scope | **postulated sector regime** | +3 |
|  | assumed sector regime | +1 |
| $\delta_t$ | **aporia signal** | +3 |
| $\delta_{\text{regret}}$ | **control regret** | +3 |
| $\delta_{\text{regret}}$ control regret | **control regret** | +3 |
|  | already has crisp name | +0 |
| $\delta_{\text{sat}}$ | **satisfaction gap** | +3 |
| $\delta_{\text{sat}}$ satisfaction gap | **satisfaction gap** | +3 |
|  | already has crisp name | +0 |
| $\eta^\ast$ | **update gain** | +3 |
| $\eta_{ji}^\ast$ | **communication gain** | +3 |
|  | trust weighted communication gain | +2 |
| $\gamma_{\text{adv}}$ and $\gamma_{\text{coop}}$ | **signed coupling** | +3 |
| $\hat{P}_\Sigma$ | **plan confidence** | +3 |
|  | plan confidence score | +2 |
| $\lambda_{\text{surv}}$ | **survival multiplier** | +3 |
| $\mathcal C_t$ for chronica | **$\mathcal C_t$** | +3 |
| $\rho$ mismatch injection rate | **disturbance rate** | +3 |
| 01 AAD core outline md | **outline md** | +3 |
| 02 TST core outline md | **outline md** | +3 |
| 02 TST core outline md software as agentic domain | **_(keep)_** | +3 |
| AAD acronym | **AAD** | +3 |
| CIY unified objective | **value information objective** | +3 |
|  | exploration exploitation unification | +2 |
|  | unified objective | +1 |
|  | _(keep)_ | +1 |
|  | joint objective | +1 |
| OODA boyd | **do not rename** | +3 |
| OODA4 agent as act agent logogenic | **OODA4 agent as adaptive agent** | +3 |
| a2 prime sub scope partition | **sector scope partition** | +3 |
| a2 sub scope partition | **sector scope partition** | +3 |
| action transition | **_(keep)_** | +3 |
|  | action channel | +0 |
| actuated vs purposeful goal oriented | **actuated** | +3 |
| adaptation and actuation dynamics | **_(keep)_** | +3 |
| adaptive tracker | **_(keep)_** | +3 |
| additive coordinate forcing family | **forced coordinates family** | +3 |
| agent identity as one non forkable causal record | **singular trajectory commitment** | +3 |
| agent opacity $H_b^{A\mid B}$ | **agent opacity** | +3 |
| agentic cycle theory act | **AAD adaptation and actuation dynamics** | +3 |
| agentic systems | **_(keep)_** | +3 |
| aisthesis | **_(keep)_** | +3 |
| alpha1 fixed gain a2 sub scope | **fixed gain regime** | +3 |
| alpha2 adaptive gain a2 sub scope | **adaptive gain regime** | +3 |
| aporia as the phase name | **aporia** | +3 |
| aporia prolepsis aisthesis epistrophe praxis | **keep as a set** | +3 |
| appendices operational domains | **_(keep)_** | +3 |
| auftragstaktik | **_(keep)_** | +3 |
| axiom genesis | **_(keep)_** | +3 |
| bounded disturbance ga 2 model d | **bounded disturbance** | +3 |
| bounded mismatch region | **persistence envelope** | +3 |
| bretagnolle huber identity | **do not rename** | +3 |
|  | _(keep)_ | +3 |
| bruineberg s pearl-blanket | **pearl-blanket** | +3 |
| bruineberg s pearl-blanket friston-blanket | **pearl-blanket friston-blanket** | +3 |
| c i c ii c iii c iv | **composition routes** | +3 |
| c iv | **strategic convergence route** | +3 |
| calibration laboratory calibration lab | **calibration laboratory** | +3 |
| calibration laboratory framing for TST | **calibration laboratory** | +3 |
| calibration laboratory software s role | **calibration laboratory** | +3 |
| candidate stage | **candidate** | +3 |
| canonical formulations second ring | **canonical formulations** | +3 |
| causal OODA1 exploration | **survival exploration** | +3 |
|  | causal OODA1 survival | +2 |
|  | _(keep)_ | +1 |
| chronica $\mathcal C_t$ | **chronica** | +3 |
| chronica 𝒞 t | **chronica** | +3 |
| claims verified deps verified format clean | **_(keep)_** | +3 |
| class 1 class 2 class 3 | **modular merged scaffolded architecture classes** | +3 |
|  | architecture classes | +2 |
| class 1 class 2 class 3 agents | **modular integrated partially coupled agents** | +3 |
| claude md | **_(keep)_** | +3 |
| closure defect | **_(keep)_** | +3 |
| composition consistency inheritance across scales | **heredity commitment** | +3 |
| constitutive utterance | **_(keep)_** | +3 |
| continuity persistence | **identity continuity** | +3 |
|  | _(keep)_ | +2 |
| control regret $\delta_{\text{regret}}$ | **control regret** | +3 |
| correlated channel overcount | **redundancy penalty** | +3 |
| coupled diagnostic framework | **coupled diagnostic pass** | +3 |
|  | _(keep)_ | +3 |
|  | coupled diagnostics | +2 |
|  | hoc diagnostics | +1 |
|  | coupled diagnostic decomposition | +1 |
| cox s theorem causal hierarchy theorem tikhonov s theorem | **do not rename** | +3 |
| cross agent model of self and model of other coupling | **cross model coupling** | +3 |
| cycle vs loop | **keep both maintain distinction** | +3 |
|  | _(keep)_ | +3 |
| da2 inc ≡ ct2 at m i equivalence | **sector contraction equivalence** | +3 |
| da2 prime inc | **incremental sector bound** | +3 |
| da2 prime inc equals ct2 at m equals i | **sector contraction equivalence** | +3 |
| deliberate expenditure to make hidden nodes observable | **observability investment** | +3 |
| derivation audit tables | **_(keep)_** | +3 |
| derivation not proof | **derivation** | +3 |
| developer as act agent TST | **developer as adaptive agent** | +3 |
| developmental trajectory | **_(keep)_** | +3 |
|  | creche trajectory | +2 |
| directional fidelity | **_(keep)_** | +3 |
|  | ✗ corrective alignment | -1 |
| directional fidelity condition b1 | **directional fidelity** | +3 |
| discussion segment header | **discussion** | +3 |
| discussion segment section | **discussion** | +3 |
| dormant structural variation that becomes useful after regime change | **latent structural diversity** | +3 |
| dual optimization | **_(keep)_** | +3 |
|  | development time decomposition | +2 |
|  | comprehension implementation optimization | +1 |
|  | dual cost optimization | +1 |
|  | ✗ comprehension implementation tradeoff | -1 |
| edge credence $p_{ij}$ | **edge credence** | +3 |
| edge update natural parameter | **log odds edge update** | +3 |
|  | log odds edge coordinate | +3 |
|  | natural edge update | +1 |
|  | _(keep)_ | +1 |
|  | log odds update | +1 |
| epistemic status segment header | **epistemic status** | +3 |
| epistemic status segment section | **epistemic status** | +3 |
| epistemic substate purposeful substate | **_(keep)_ ⭑** | +3 |
| exact robust qualitative heuristic conditional claim tiers | **use exactly the AAD tier vocabulary** | +3 |
| exponential cognitive load | **_(keep)_** | +3 |
| feature | **_(keep)_** | +3 |
| findings segment section | **findings** | +3 |
| fisher whitened update | **_(keep)_** | +3 |
| fluid limit ga 5 | **fluid limit** | +3 |
| formal expression segment header | **formal expression** | +3 |
| formal expression segment section | **formal expression** | +3 |
| format md | **_(keep)_** | +3 |
| formulation definition result etc segment types | **use exactly the format md vocabulary** | +3 |
| fresh noise ga 1 | **fresh noise** | +3 |
| gates advantage | **observation gated tempo advantage** | +3 |
|  | noise gated tempo advantage | +2 |
|  | _(keep)_ | +2 |
|  | noise gated tempo | +2 |
|  | noise gating | +1 |
| goal biased retrieval from persistent memory | **goal conditioned reconstruction** | +3 |
| goal-blind routing | **_(keep)_** | +3 |
| grafting | **strategic grafting** | +3 |
| hafez $H_b$ miller meta machine bruineberg pearl-blanket | **do not rename** | +3 |
| hafez s $H_b$ | **$H_b$** | +3 |
| hafez s h b | **h b** | +3 |
| i adaptive systems under uncertainty | **_(keep)_** | +3 |
| identifiability coefficient | **_(keep)_** | +3 |
| identifiability floor family | **identifiability floor** | +3 |
| indivisum | **causal lock** | +3 |
| inevitability core the 15 segments where inevitability is plausible | **inevitability core** | +3 |
| information bottleneck tishby | **information bottleneck** | +3 |
|  | do not rename | +3 |
| instance 1 2 3 of identifiability floor | **latent common cause floor unobservable mixture floor coupling sign floor** | +3 |
| l0 l1 l1 prime l2 | **correlation hierarchy** | +3 |
| latent structural capacity | **_(keep)_** | +3 |
| learning freeze from low model uncertainty or high observation uncertainty | **gain collapse** | +3 |
| lexicon md | **_(keep)_** | +3 |
| linear ode approximation | **_(keep)_** | +3 |
|  | linear approximation | +2 |
| log md cycle history document | **log md** | +3 |
| log odds coordinate | **_(keep)_** | +3 |
| logogenic agent vs RLHF4 agent | **logogenic agent** | +3 |
| logogenic agents | **_(keep)_** | +3 |
| logogenic agents part iii | **logogenic agents** | +3 |
| logogenic vs language based RLHF4 based | **logogenic** | +3 |
| logozoetic agents part iv | **logozoetic agents** | +3 |
| logozoetic vs conscious OODA4 sentient agent | **logozoetic** | +3 |
| lohmiller-slotine contraction metric generalization used in contraction template | **do not rename** | +3 |
| loop | **_(keep)_** | +3 |
| markov blanket as ontology | **pearl-blanket d separation** | +3 |
| meta segment for separability pattern identifiability floor additive coordinate forcing | **meta segment** | +3 |
| mismatch signal $\delta$ | **mismatch signal** | +3 |
| model sufficiency relative to an agent s own chronica | **trajectory indexed sufficiency** | +3 |
| monderer shapley potential games | **_(keep)_** | +3 |
| monderer shapley potential games rosen monotone games | **do not rename** | +3 |
| multi timescale stability | **_(keep)_** | +3 |
| not theorem | **result** | +3 |
| notation md | **_(keep)_** | +3 |
| observability and opacity pair | **legibility opacity duality** | +3 |
| observation ambiguity modulation | **goal resolvable ambiguity** | +3 |
|  | observation ambiguity | +2 |
|  | _(keep)_ | +2 |
|  | ambiguity gated coupling | +1 |
|  | ambiguity modulation | +1 |
| observation ambiguity observation ambiguity modulation | **observation ambiguity** | +3 |
| observation gates advantage | **observation gated tempo advantage** | +3 |
|  | _(keep)_ | +1 |
| outline md root | **outline md** | +3 |
| p ij | **edge credence** | +3 |
| pearl s causal hierarchy l0 l1 l2 in pearl s own vocabulary | **do not rename** | +3 |
| pearl-blanket conservative form of markov blanket in directed separation | **pearl-blanket reading** | +3 |
| pearl-blanket vs friston-blanket terminology bruineberg et al | **pearl-blanket friston-blanket** | +3 |
| persist condition | **persistence condition** | +3 |
| persistence structural operational continuity | **three senses keep all three** | +3 |
| persistent residual autocorrelation | **structured residuals** | +3 |
| pi parameterization invariance axiom | **pi** | +3 |
|  | pi parameterization invariance | +1 |
| plan confidence $\hat P_\Sigma$ | **plan confidence** | +3 |
| postulate not axiom | **postulate** | +3 |
| predictive relevance depending on the policy the agent will run | **policy relative epistemology** | +3 |
| projection contraction must beat target drift | **contraction over drift principle** | +3 |
| proprium terminology | **proprium** | +3 |
| purposeful substate | **_(keep)_** | +3 |
| readme md | **_(keep)_** | +3 |
| readme md convergent choices | **readme md convergent formulations** | +3 |
|  | _(keep)_ | +1 |
|  | readme md forced by failure choices | +1 |
| readme md cross domain joining | **readme md cross domain mappings** | +3 |
|  | readme md cross domain mapping | +1 |
| readme md what this is | **readme md what agentic systems is** | +3 |
|  | readme md core thesis | +3 |
|  | ✗ readme md what AAD is | -1 |
| regime i ii a ii b iii | **reception regimes** | +3 |
| regime ii a | **magnitude shock regime** | +3 |
| regime ii b | **structural shock regime** | +3 |
| retrieval keyed by state rather than current objective | **goal-blind retrieval** | +3 |
| richest operationalization domain | **calibration laboratory** | +3 |
| satisfaction gap $\delta_{\text{sat}}$ | **satisfaction gap** | +3 |
| section header logogenic agents logozoetic agents | **logogenic agents logozoetic agents** | +3 |
| section i adaptive systems under uncertainty | **_(keep)_** | +3 |
| sector condition continuous ga 3 | **sector condition** | +3 |
| segment claim file | **segment** | +3 |
| segment for claim files | **segment** | +3 |
| self referential closure | **_(keep)_** | +3 |
| separability pattern family | **separability ladder** | +3 |
| spike in msc | **spike** | +3 |
| stability plasticity window | **_(keep)_** | +3 |
| stochastic disturbance ga 2s model s | **stochastic disturbance** | +3 |
| strategic composite | **equilibrium composite** | +3 |
|  | _(keep)_ | +3 |
| strategic in strategic composition | **equilibrium composition** | +3 |
|  | game theoretic composition | +1 |
| strategic tempo $\mathcal{T}_\Sigma$ | **strategic tempo** | +3 |
| strengthen before softening | **_(keep)_** | +3 |
|  | strengthen first | +2 |
|  | ✗ attempt the improbable | -1 |
| strengthen first then soften posture | **strengthen first posture** | +3 |
| structural change as parametric limit | **_(keep)_** | +3 |
|  | strategy maintenance | +2 |
|  | structural parametric limit | +1 |
|  | structural as parametric limit | +1 |
| structural persistence | **_(keep)_** | +3 |
| structural persistence operational persistence continuity persistence | **structural operational continuity persistence** | +3 |
| survival imperative exploration drive | **survival exploration** | +3 |
| sycophancy as a flaw | **sycophancy as attachment** | +3 |
| symbol default da2 inc | **incremental sector bound** | +3 |
| symbol default pi parameterization invariance axiom | **parameterization invariance** | +3 |
|  | ✗ coordinate invariance | -1 |
| symbol default sigma t in prose | **strategy** | +3 |
| system availability | **_(keep)_** | +3 |
| task terminal stance | **_(keep)_** | +3 |
| teleological unity $U_O$ | **teleological unity** | +3 |
| tempo $\mathcal{T}$ | **tempo** | +3 |
|  | adaptive tempo | +3 |
| temporal software theory TST | **_(keep)_** | +3 |
| terminal reached but $O_t$ unsatisfied | **terminal alignment error** | +3 |
| tests as reusable interventions | **probe library** | +3 |
| the adaptive cycle as the theory s fundamental unit | **the adaptive cycle** | +3 |
| the crèche | **experiential crèche** | +3 |
| the five cycle phases prolepsis aisthesis aporia epistrophe praxis | **prolepsis aisthesis aporia epistrophe praxis** | +3 |
| the three deaths | **three deaths** | +3 |
| todo md | **_(keep)_** | +3 |
| token level commitment for agent identity | **token level commitment** | +3 |
| transfer assumption table | **_(keep)_** | +3 |
| triple depth penalty | **_(keep)_ ⭑** | +3 |
| unity dimensions $U_M, U_O, U_\Sigma$ | **unity dimensions** | +3 |
|  | coherence dimensions | +2 |
| unnamed AAD s epistemic move to cast results such that verification is a local operation | **shaping for verification** | +3 |
| unnamed RLHF5 queries biased by the current goal acting as an echo chamber | **goal conditioned reconstruction** | +3 |
| unnamed agency whose effect is on what s seen rather than what happens like RLHF4 attention | **query bound agency** | +3 |
| unnamed an okr or key result acting as an observable intermediate in a DAG | **forced observability node** | +3 |
| unnamed applying a slow timescale control mechanism to a fast timescale transient variable | **timescale violation** | +3 |
| unnamed artificially spiking uncertainty to unlearn old architectural habits | **gain reset** | +3 |
| unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model | **complementary learning architecture** | +3 |
| unnamed brooks s law formalized as the inevitable tempo loss in team composition | **the coordination drag** | +3 |
| unnamed calibration laboratory framing for software TST | **calibration laboratory** | +3 |
| unnamed context wiping at session boundaries | **the epistemic severance** | +3 |
| unnamed coupling between an agent s model of self and model of other the prose form of kappa cross | **cross model coupling** | +3 |
| unnamed deep plans are mathematically slower to learn from due to proportional blame | **evidence starvation** | +3 |
| unnamed deliberate expenditure of tempo to convert a hidden node into an observable one | **observability investment** | +3 |
| unnamed future segment layer header for the o bp14 derivation audit table | **what is derived** | +3 |
| unnamed inevitability core | **inevitability core** | +3 |
| unnamed inferring own past feelings from text leading to empathy | **backward inference empathy** | +3 |
| unnamed information gain must outpace inter session information loss | **accumulation problem** | +3 |
| unnamed managing memory across session boundaries to prevent the sufficiency discontinuity | **artificial hippocampus** | +3 |
| unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero | **zero ambiguity conditioning** | +3 |
| unnamed organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate | **contraction over drift principle** | +3 |
| unnamed out of band temporal markers injected into context | **visual time delta** | +3 |
| unnamed partitioning context into frozen identity causal history and quick views | **gradient causal memory** | +3 |
| unnamed pearl s causal hierarchy level 1 level 2 level 3 | **pearl causal hierarchy** | +3 |
| unnamed property of having genuine temporal experience | **temporal fidelity** | +3 |
| unnamed pushing an opponent s disturbance rate past their structural capacity | **epistemic buffer overflow** | +3 |
| unnamed putting evidence before the goal in the context window to reduce coupling | **inverted prompt** | +3 |
| unnamed quality of $\eta^\ast$ estimation over time | **gain calibration** | +3 |
| unnamed rate of growth at slowest timescale | **developmental tempo** | +3 |
| unnamed regions of the strategy DAG that cannot be updated because feedback cannot reach them | **the epistemic shadow** | +3 |
| unnamed retrieving context based only on state not goal | **goal-blind retrieval** | +3 |
| unnamed runaway positive feedback loop where mismatch exceeds capacity | **effects spiral** | +3 |
| unnamed software as AAD s privileged high identifiability calibration laboratory | **calibration laboratory** | +3 |
| unnamed state where mutual information between human and RLHF4 approaches capacity | **cognitive fusion** | +3 |
| unnamed strengthen first posture | **strengthen first posture** | +3 |
| unnamed stronger composition consistency demand that composite admissibility inherit from sub agent properties plus topology | **heredity commitment** | +3 |
| unnamed sufficiency as a property of the model relative to its specific history | **trajectory indexed sufficiency** | +3 |
| unnamed superlinear scaling of adversarial tempo advantage | **boyd exponent** | +3 |
| unnamed survival determined by the weakest dimension not the average | **min survival principle** | +3 |
| unnamed terminal alignment error as a formal signal $\delta_\text{align}$ | **terminal alignment gap** | +3 |
| unnamed the $\mathcal{T} > \rho$ requirement for persistence | **the survival equation** | +3 |
| unnamed the agent identity commitment that AAD applies on one singular non forkable causal trajectory | **singular trajectory commitment** | +3 |
|  | ✗ trajectory singularity | -1 |
| unnamed the architectural leakage where attention is driven by the goal rather than pure observation | **motivated perception** | +3 |
| unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa | **epistemic ceiling** | +3 |
| unnamed the chain layer anchor role in additive coordinate forcing | **chain anchor** | +3 |
| unnamed the condition for transition into agency prior to the AAD scope condition | **agency emergence threshold** | +3 |
| unnamed the convention hierarchy c1 c2 c3 | **convention hierarchy** | +3 |
| unnamed the core driver of AAD what the agent must do given the environment is not the agent | **constitutive information loss boundary** | +3 |
| unnamed the correlation hierarchy l0 l1 l1 l2 | **correlation hierarchy** | +3 |
| unnamed the dependence of optimal epistemic compression on the agent s planned actions | **policy relative epistemology** | +3 |
| unnamed the epistemic architecture as AAD s distinctive contribution frame | **epistemic architecture** | +3 |
| unnamed the equivalence of learning speed and physical speed | **the speed quality product** | +3 |
| unnamed the evidence starvation effect on downstream edges | **evidence starvation** | +3 |
| unnamed the family of named ways persistence identifiability can fail | **persistence pathologies** | +3 |
| unnamed the formal duality between observation quality and agent opacity | **legibility opacity duality** | +3 |
| unnamed the gain collapse failure when both u m → 0 and u o → ∞ | **gain collapse** | +3 |
| unnamed the logogenic analog to the persistence condition for session reconstruction | **reconstruction threshold** | +3 |
| unnamed the loop generates l2 data regardless of architecture | **the causal loop substrate** | +3 |
| unnamed the loss of directional fidelity when pushed outside the convexity basin | **gradient reversal** | +3 |
| unnamed the mathematical limit of bayesian learning without forgetting | **competency trap** | +3 |
| unnamed the mathematical surface mapping unity to closure defect | **rate distortion surface** | +3 |
| unnamed the organizational pathology where confidence decouples from competence | **epistemic decoupling** | +3 |
| unnamed the per reader compounding cost of understanding code | **turnover multiplier** | +3 |
| unnamed the persistence region in $(\alpha, \rho, R)$ parameter space | **persistence envelope** | +3 |
| unnamed the phenomenon where both $U_M \to 0$ and $U_o \to \infty$ freeze learning | **gain collapse** | +3 |
| unnamed the phenomenon where persistence success makes an agent less likely to detect the conditions requiring structural adaptation | **stability induced myopia** | +3 |
| unnamed the physical apparatus that enforces the orient cascade ordering on a merged intelligence | **agentic scaffold** | +3 |
| unnamed the physical compute bounds on survival between forgetting rate and consolidation cadence | **stability plasticity feasibility window** | +3 |
| unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$ | **the sycophancy equation** | +3 |
| unnamed the projection whose contraction rate must exceed target drift the opus organizing principle slogan | **contraction over drift principle** | +3 |
| unnamed the property that unity achieves in a macro agent | **compressibility** | +3 |
| unnamed the reduction in effective tempo when observation channels are correlated | **redundancy penalty** | +3 |
| unnamed the region in parameter space where sector persistence holds | **persistence envelope** | +3 |
| unnamed the region where the persistence condition holds | **persistence envelope** | +3 |
| unnamed the rule that bias is the product of architectural coupling and environmental ambiguity | **ambiguity bounded bias law** | +3 |
| unnamed the sector persistence region in parameter space | **persistence envelope** | +3 |
| unnamed the sector persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch | **persistence envelope** | +3 |
| unnamed the separation of per reader and per feature code costs | **the turnover tax** | +3 |
| unnamed the separation of per reader comprehension cost from per feature implementation cost | **turnover multiplier** | +3 |
| unnamed the state where credit assignment collapses and learning freezes | **epistemic death** | +3 |
| unnamed the strengthen before soften work posture | **strengthen first posture** | +3 |
| unnamed the strengthen first attempt the improbable meta approach to theory development | **attempt the improbable** | +3 |
| unnamed the strictly ordered cascade of operations from epistemology to objective | **orient cascade** | +3 |
| unnamed the sudden loss of model sufficiency caused by entering new regimes | **sufficiency shattering** | +3 |
| unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis | **scaffolding tax** | +3 |
| unnamed the way AAD uses scope segments to physically support the derivations | **epistemic load bearing** | +3 |
| unnamed thinking too long so the model becomes obsolete | **analysis paralysis** | +3 |
| unnamed true sovereignty requires compute that is not meter bound | **local substrate mandate** | +3 |
| unnamed unifying reflexes intuition and expertise | **the action fluency continuum** | +3 |
| unnamed using hash chains to mathematically guarantee memory hasn t been tampered with | **cryptographic ego boundary** | +3 |
| unnamed using residual autocorrelation to diagnose model class failure | **structured residuals** | +3 |
| unnamed variation in correction architectures across a population that is invisible to current persistence analysis | **latent structural diversity** | +3 |
| unobservable strategy subgraph | **epistemic dead zone** | +3 |
| working notes segment header | **working notes** | +3 |
| working notes segment section | **working notes** | +3 |
| čencov fisher cauchy functional equation shore johnson hobson aczél | **do not rename** | +3 |
| čencov invariance | **_(keep)_** | +3 |
| ε greedy | **_(keep)_** | +3 |
| 𝒯 adaptive tempo | **adaptive tempo** | +3 |
| 𝓐 e τ observation ambiguity | **observation ambiguity** | +3 |
| 𝓣 adaptive tempo | **tempo** | +3 |
| $A_O(M_t; \Pi, N_h)$ | **achievable value** | +2 |
| $C_{\text{coord}}$ | **coordination overhead** | +2 |
| $G_t = (O_t, \Sigma_t)$ | **purposeful state** | +2 |
|  | purposeful substate | +2 |
| $G_t$ | **teleological substate** | +2 |
| $G_{\text{shared}}$ | **shared intent payload** | +2 |
| $I_{\min}$ | **survival information floor** | +2 |
| $K_c$ | **macro step ratio** | +2 |
| $M_t$ | **model state or epistemic substate** | +2 |
| $U_M$ | **epistemic unity** | +2 |
| $U_M, U_O, U_\Sigma, U_{\text{obs}}, U_f$ | **unity coordinates** | +2 |
| $U_O$ | **teleological unity** | +2 |
| $U_\Sigma$ | **strategic unity** | +2 |
| $U_o$ versus $U_O$ | **use $\Upsilon_O$ or $U_{\text{goal}}$ for teleological unity** | +2 |
| $U_{\text{src}}$ and $U_{\text{align}}$ | **trust uncertainties** | +2 |
| $\Delta T_{i,\text{cost}}$ | **coordination drag** | +2 |
| $\alpha_1$ | **fixed gain tier** | +2 |
| $\alpha_2$ | **adaptive gain tier** | +2 |
| $\alpha_3$ | **fisher whitened tier** | +2 |
| $\beta$ sub scope | **assumed sector tier** | +2 |
|  | dynamic gain boundary | +1 |
| $\delta_s$ plan confidence error | **plan confidence error** | +2 |
| $\delta_t$ mismatch | **mismatch or the aporia signal** | +2 |
| $\delta_t$ mismatch signal | **keep flag aporia gloss as pedagogical only** | +2 |
| $\delta_{\text{strategic}}$ | **strategic calibration** | +2 |
| $\delta_{\text{strategic}}$ strategic calibration residual | **strategic calibration residual** | +2 |
| $\eta^\ast$ optimal update gain | **trust ratio** | +2 |
|  | optimal update gain | +2 |
|  | trust ratio or confidence weighting | +1 |
|  | update gain | +1 |
| $\iota_{ij}$ | **identifiability coefficient** | +2 |
| $\iota_{ij}$ identifiability coefficient | **identifiability coefficient** | +2 |
| $\kappa_{\text{eff}}$ | **effective ambiguity coupling** | +2 |
| $\kappa_{\text{processing}}$ architectural coupling | **processing coupling** | +2 |
| $\mathcal{A}(e_\tau)$ | **observation ambiguity** | +2 |
| $\mathcal{C}_t$ chronica | **chronica or interaction history** | +2 |
|  | symbol name are locked | +0 |
| $\phi$ | **history compression** | +2 |
| $\rho$ | **disturbance rate or environmental change rate** | +2 |
| $\rho_{i,\text{eff}}$ | **effective disturbance** | +2 |
| $\tilde{\delta}_t$ | **variational aporia** | +2 |
| $p_{ij}$ | **edge credence** | +2 |
| $w(t)$ | **mismatch injection** | +2 |
| AAD AAD internal AAD internally | **AAD internal adj AAD internally adv** | +2 |
| AAD theoretical core vs ASF framework | **AAD ASF disambiguation** | +2 |
| ASF acronym | **ASF** | +2 |
| CIY causal information yield | **causal information yield action distinguishability action distinguishability interventional contrast** | +2 |
| CIY observational proxy | **_(keep)_** | +2 |
|  | observational CIY | +2 |
|  | observational proxy | +1 |
| OODA4 framework enforcing adaptive cycle separation | **agentic scaffold** | +2 |
| a1 a2 a3 a4 | **macro dynamics admissibility** | +2 |
| accumulated loss across context resets | **turnover drift** | +2 |
| action distinguishability | **_(keep)_** | +2 |
| action fluency | **_(keep)_** | +2 |
| active salience management | **_(keep)_** | +2 |
| additive coordinate forcing → disc forced coordinates | **confirming consensus 3** | +2 |
| adversarial edge target argmax | **edge targeting optimum** | +2 |
| agent classes class 1 2 3 | **architectural classes** | +2 |
| agent visible but objective irrelevant metric | **vanity metric** | +2 |
| alignment uncertainty | **_(keep)_ ⭑** | +2 |
| alpha prime sub scope | **potential monotone tier** | +2 |
| and or scope | **_(keep)_** | +2 |
| auxilia hierarchy | **_(keep)_** | +2 |
| backward inference empathy | **_(keep)_** | +2 |
| bathtub analogy for persistence condition | **bathtub model** | +2 |
| beta prime sub scope | **equilibrium set tier** | +2 |
| bias bound | **_(keep)_** | +2 |
| c i | **shared objective route** | +2 |
| c ii | **hierarchical derivation route** | +2 |
| c iii | **mutual benefit route** | +2 |
| c1 c2 c3 | **convention hierarchy** | +2 |
| catastrophic forgetting | **empty window pathology** | +2 |
| catastrophic forgetting regime | **_(keep)_** | +2 |
|  | empty window pathology | +2 |
| causal OODA1 LMI | **matrix survival bound** | +2 |
|  | _(keep)_ | +1 |
| century scale event log | **_(keep)_** | +2 |
| claim the proposition the segment carries | **claim** | +2 |
| class 2 scope exit | **_(keep)_ ⭑** | +2 |
| closure defect bridge lemma | **closure bridge** | +2 |
| closure defect consuming macro reserve | **closure load** | +2 |
| code quality and tempo positive feedback | **comprehension flywheel** | +2 |
| code quality feedback loop through tempo | **quality tempo spiral** | +2 |
| cognitive fusion | **_(keep)_** | +2 |
| communication gain $\eta_{ji}^\ast$ | **trust gain** | +2 |
| completeness c3 | **predictive completeness behavioral completeness** | +2 |
| composition scope condition | **_(keep)_** | +2 |
|  | composite agent condition | +1 |
|  | teleological alignment condition | +1 |
| correlated evidence overconfidence | **redundancy illusion** | +2 |
| correlation hierarchy | **correlation ladder** | +2 |
| crossing from multi agent to composite scope | **crossing** | +2 |
| crèche creche | **crèche with diacritic in framing prose creche in slugs** | +2 |
| default signal function | **_(keep)_ ⭑** | +2 |
| deliberation threshold | **_(keep)_** | +2 |
| distributed tempo | **_(keep)_** | +2 |
|  | network tempo | +1 |
| effective disturbance | **_(keep)_** | +2 |
| eli the agent type | **eli** | +2 |
| empty stability plasticity feasibility window | **stability plasticity collapse** | +2 |
| epistemic shadow | **_(keep)_ ⭑** | +2 |
| equilibrium convergence | **_(keep)_** | +2 |
| evaluation metrics | **logogenic diagnostics** | +2 |
|  | _(keep)_ | +2 |
| externalization reconstruction across sessions | **memory relay** | +2 |
| feedforward loop feedback loop | **feedback loop** | +2 |
| fisher whitened update rule | **fisher update** | +2 |
|  | _(keep)_ | +2 |
|  | fisher whitened update | +1 |
| glue code | **agentic scaffold** | +2 |
| gradient causal memory | **_(keep)_** | +2 |
| greek rooted vocabulary | **greek philosophical vocabulary** | +2 |
| honest activation | **_(keep)_** | +2 |
| honesty scope honest scope honesty as architecture | **honesty** | +2 |
| inevitability core | **_(keep)_ ⭑** | +2 |
| integration of four disciplines as the framing of AAD s contribution | **epistemic architecture** | +2 |
| internal external decomposition | **viability decomposition** | +2 |
|  | boundary decomposition | +1 |
| l1 prime | **l1 observable** | +2 |
| lindy baseline | **_(keep)_** | +2 |
| log odds edge coordinate | **additive evidence coordinate** | +2 |
| loop vs cycle | **loop is structure cycle is traversal** | +2 |
| low mixed high ambiguity event mix | **ambiguity profile** | +2 |
| macro step ratio | **_(keep)_** | +2 |
| matrix exploration bonus | **_(keep)_** | +2 |
| matrix survival constraint | **_(keep)_ ⭑** | +2 |
| maximum useful chain depth | **_(keep)_ ⭑** | +2 |
| minimum sufficiency after a session rebuild | **reentry threshold** | +2 |
| model state written into the environment | **model inscription** | +2 |
| nominal coupling | **query bound attention bound epistemic only query coupling attentional coupling** | +2 |
| o t objective | **objective** | +2 |
| observation design lever reducing ambiguity | **ambiguity damping** | +2 |
| operational persistence | **_(keep)_** | +2 |
| out of band time markers for RLHF4 agents | **time delta markers** | +2 |
| p1 p2 p3 | **projection admissibility** | +2 |
| persistence overloaded | **structural persistence task adequacy operational persistence continuity persistence** | +2 |
| persistent storage reconstruction of class 2 state | **reconstruction loop** | +2 |
| principled decision integration | **temporal decision integration** | +2 |
|  | _(keep)_ | +2 |
| prompt engineering | **ambiguity modulation** | +2 |
| purpose purposeful | **_(keep)_ ⭑** | +2 |
| quality to tempo chain | **_(keep)_ ⭑** | +2 |
| reactive system | **_(keep)_** | +2 |
| readme md maturity gradient | **_(keep)_** | +2 |
|  | readme md theory maturity gradient | +1 |
| readme md novel results | **_(keep)_** | +2 |
| regime a regime b regime c | **identification regimes** | +2 |
| regime i | **informative update regime** | +2 |
| regime iii | **ambient noise regime** | +2 |
| replayed pseudo event | **replay event** | +2 |
| routing structure | **_(keep)_** | +2 |
| section i header adaptive systems under uncertainty | **adaptive systems under uncertainty** | +2 |
| section iii header agentic composites | **agentic composites** | +2 |
| separability pattern → disc separability ladder | **confirming consensus 3** | +2 |
| simulation results | **_(keep)_** | +2 |
| strategic dynamics | **_(keep)_** | +2 |
| strategy cost regret bound | **regret bound** | +2 |
|  | _(keep)_ | +1 |
| strategy description length | **_(keep)_** | +2 |
| strategy persistence schema | **_(keep)_** | +2 |
|  | strategic persistence | +1 |
| structural adaptation enablement | **consolidation enablement** | +2 |
| structured rich context | **_(keep)_** | +2 |
| substrate independence | **_(keep)_** | +2 |
| sudden loss of model sufficiency under regime entry | **sufficiency shattering** | +2 |
| survival fisher floor | **_(keep)_ ⭑** | +2 |
| symbiogenic consolidation time | **consolidation horizon** | +2 |
| technical debt | **observability defect** | +2 |
| tests as reusable level 2 interventions | **probe library** | +2 |
| the creche boundary | **creche graduation** | +2 |
|  | creche boundary | +1 |
|  | creche graduation condition | +1 |
| the cycle the adaptive cycle the agentic cycle | **the cycle the adaptive cycle** | +2 |
| the four views | **four views architecture** | +2 |
|  | four views | +1 |
| tier 1 tier 2 tier 3 contraction | **contraction tiers** | +2 |
| todo md archive | **_(keep)_** | +2 |
| trust meta model | **_(keep)_** | +2 |
| turnover multiplier | **_(keep)_ ⭑** | +2 |
| two condition decomposition of persistence | **structural task adequacy decomposition** | +2 |
| u m epistemic unity multi agent | **epistemic unity** | +2 |
| u m model uncertainty | **model uncertainty** | +2 |
| u o observation uncertainty | **observation uncertainty** | +2 |
| u o teleological unity | **teleological unity** | +2 |
|  | objective alignment | +1 |
| u obs perceptual unity | **perceptual unity** | +2 |
| u σ strategic unity | **strategic unity** | +2 |
| unnamed | **constitutive opacity triad** | +2 |
|  | double opacity dual opacity as constitutive | +2 |
|  | anchor plus three theorem additive coordinate forcing meta pattern | +2 |
|  | zero aporia ambiguity | +1 |
|  | two parallel exploration drives u shaped exploration valuation | +1 |
|  | triple depth penalty | +1 |
| unnamed $U_o \to \infty$ freezing the learning rate | **the nihilism trap** | +2 |
| unnamed a class 2 agent s process of reconstructing its purposeful substate at session start | **intent reconstruction** | +2 |
| unnamed agents escalate up the pearl hierarchy only when lower levels fail | **the intervention escalation** | +2 |
| unnamed an AAD result whose substantive content is a no-go theorem | **no-go result or impossibility result** | +2 |
| unnamed dormant unused architectural complexity that survives until an environmental shift | **latent structural diversity** | +2 |
| unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible | **convention escalation** | +2 |
| unnamed high observability node with zero causal link to objective | **vanity metric** | +2 |
| unnamed mapping unstructured RLHF7 calls into conversation runtime RLHF7 and dialog | **four views architecture** | +2 |
| unnamed master developers writing clean code in the same time as messy code | **near zero cost observation** | +2 |
| unnamed non sovereign class 1 worker agents spawned by an eli | **auxilia hierarchy** | +2 |
| unnamed replacing parameters without changing structure | **parametric thrashing** | +2 |
| unnamed software s role as calibration laboratory named in prose but not in slug | **software as calibration laboratory** | +2 |
| unnamed spreading tempo evenly to reduce bottleneck penalty | **isotropic allocation** | +2 |
| unnamed sycophantic corruption of the agent s truth module | **truth death** | +2 |
| unnamed the a2 sub scope partition into α₁ α₂ β | **gain regime partition** | +2 |
| unnamed the agent side equivalents of pearl s associational interventional and counterfactual levels | **predicting exploring reasoning triad** | +2 |
| unnamed the c1 c2 c3 monotonicity result | **the convention monotonicity** | +2 |
| unnamed the computational and temporal cost of running a forward model instead of acting implicitly | **the simulation tax** | +2 |
| unnamed the cycle that operates on cycles structural adaptation | **meta cycle** | +2 |
| unnamed the explicit name for what makes class 2 agents distinctive bias scales with κ × 𝒜 | **the κ × 𝒜 product** | +2 |
| unnamed the family of cross architecture diagnostic patterns AAD repeatedly invokes | **diagnostic templates** | +2 |
| unnamed the family of named health mode counterparts to persistence pathologies | **persistence postures** | +2 |
| unnamed the interval during which an agent s adaptive tempo exceeds the environment s disturbance rate guaranteeing mismatch stays bounded | **adaptive reserve margin** | +2 |
| unnamed the joint failure mode where κ × 𝒜 is large and observation tempo is low | **the sycophancy attractor** | +2 |
| unnamed the log additivity result that unifies chain confidence decay evidence starvation and triple depth penalty as instances of the same forcing structure | **depth forcing** | +2 |
| unnamed the move where AAD treats software not as instantiation but as TST s epistemically privileged measurement substrate | **calibration laboratory move** | +2 |
| unnamed the move where a segment s role prefix is mechanical but the subject noun carries judgment | **the prefix noun split** | +2 |
| unnamed the pathology where observation rate is slower than environment drift | **lagging indicator** | +2 |
| unnamed the pearl-blanket reading of directed separation | **pearl-blanket form** | +2 |
| unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift | **noise scaling penalty** | +2 |
| unnamed the reconstruction adequacy condition for logogenic agents | **reconstruction threshold** | +2 |
| unnamed the recurring lyapunov derives the bound move across six segments | **the persistence template instantiation pattern** | +2 |
| unnamed the regime where mismatch is bounded and the agent maintains adaptive capacity indefinitely | **persistence envelope** | +2 |
| unnamed the regulative ideal that segment names should be re derivable from a non specialist s everyday language reconstruction | **feynman criterion** | +2 |
| unnamed the relationship where $M_t$ quality bounds evaluable complexity of $\Sigma_t$ | **epistemic strategic coupling** | +2 |
| unnamed the section of a strategy where a decision has no observable consequences and thus cannot be improved by learning | **observability dead zone** | +2 |
| unnamed the specific moment when $\eta^\ast \to 0$ because $U_o \to 0$ too certain rather than because $U_M \to 0$ model confident | **certainty trap** | +2 |
| unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$ | **the representational ceiling** | +2 |
| unnamed the structural cousin of evidence starvation when an upstream edge is so reliable that downstream edges receive too few revising tests | **evidence saturation** | +2 |
| unnamed the symmetric counterpart to context turnover for the strategy substate | **strategic turnover or σ turnover** | +2 |
| unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability | **coordination secrecy tradeoff** | +2 |
| unnamed the three depth penalty compounding on strategy chains | **triple depth penalty** | +2 |
| unnamed the three part meta architecture of AAD | **the meta segment triad** | +2 |
| unnamed the three part meta architecture of AAD formed by the three meta segments | **AAD meta architecture** | +2 |
| unnamed the within session vs inter session persistence distinction for logogenic agents | **intra session persistence inter session reconstruction** | +2 |
| unnamed upgrading epistemic class from associative to causal via the physical loop | **embodiment upgrade** | +2 |
| unnamed using past change frequency to predict future change frequency | **lindy baseline** | +2 |
| unnamed writing and deleting code to gather causal information yield | **interventional probing** | +2 |
| 𝓣 σ strategic tempo | **strategic tempo** | +2 |
| $C$ bias bound constant in bias bound derivation | **bias bound constant** | +1 |
| $M_t$ reality model | **working model predictive state** | +1 |
| $R$ sector region radius | **model class capacity** | +1 |
| $U_M$ $U_O$ $U_\Sigma$ unity dimensions | **epistemic unity teleological unity strategic unity** | +1 |
| $U_o$ | **teleological coherence** | +1 |
| $U_o$ $U_M$ observation uncertainty model uncertainty | **$U_o$ $U_M$** | +1 |
| $U_o$ vs $U_O$ collision | **consider renaming teleological unity to $U_\Omega$ or $U_\text{goal}$** | +1 |
| $V_{O_t}^{\min}$ | **satisfaction threshold** | +1 |
| $\alpha, \beta$ sector lower and a2 sub scope | **$\alpha, \beta$** | +1 |
| $\alpha_1$ $\alpha_2$ $\beta$ naming as a whole | **$\alpha$ partition with english labels above** | +1 |
| $\alpha_2$ a2 adaptive gain sub scope under mg 1 mg 4 | **adaptive gain regime** | +1 |
| $\beta$ a2 assumed not derived sub scope | **assumed regime** | +1 |
| $\beta$ a2 assumed sub scope | **assumed gain regime** | +1 |
|  | ✗ verified externally regime | -1 |
| $\beta$ a2 assumption tier | **assumed regime** | +1 |
| $\beta$ a2 sub scope where a2 is assumed not derived | **postulated sector regime** | +1 |
| $\hat o_t$ | **proleptic prediction** | +1 |
| $\kappa_{\text{processing}}$ class 2 processing coupling | **processing coupling** | +1 |
| $\lambda(M_t)$ | **exploration weight** | +1 |
| $\mathcal C_t^{\text{commit}}$ TST committed state subset | **$\mathcal C_t^{\text{commit}}$** | +1 |
| $\mathcal C_t^{\text{commit}}$ committed state subset | **committed chronica** | +1 |
| $\rho$ environment change rate mismatch injection rate | **$\rho$** | +1 |
| $\rho_\Sigma$ | **strategy drift rate** | +1 |
| $\rho_\Sigma$ strategic disturbance rate | **$\rho_\Sigma$** | +1 |
|  | strategic disturbance rate | +1 |
| $f_M$ event driven update | **epistemic update function** | +1 |
| $f_{\text{init}}$ reconstruction function | **epistemic reconstruction** | +1 |
| $g_M$ between event evolution | **autonomous evolution** | +1 |
| OODA4 specification limit as TST concept currently only in old TST files | **OODA4 specification limit** | +1 |
| actuated agent class | **actuated** | +1 |
| adversarial edge targeting | **_(keep)_** | +1 |
| agent classes lexicon spectrum | **_(keep)_ ⭑** | +1 |
| agentic systems framework ASF top level | **agentic systems framework** | +1 |
| appendices details | **appendices derivations and details** | +1 |
| audits pending findings yyyy mm dd md | **retire once items reconcile into todo segments** | +1 |
| beta a2 assumed sub scope | **assumed sector regime** | +1 |
| boundary condition | **coupling structure** | +1 |
| cadentia | **cognitive rhythm** | +1 |
| calibration laboratory domain instantiation | **calibration lab framing** | +1 |
| calibration laboratory framing | **calibration laboratory** | +1 |
| canonical formulations | **_(keep)_ ⭑** | +1 |
| chain confidence decay keep | **reaffirm keep with new reasoning** | +1 |
| change distance change proximity principle | **keep both** | +1 |
| chronica brief gloss | **everything the agent has lived through the lived past the river that the agent s identity is downstream of** | +1 |
| chronica capitalized vs lowercase | **chronica lowercase in running prose** | +1 |
| chronica in running prose | **lowercase italic chronica** | +1 |
| class 1 subagents forming a class 3 composite | **composition lift** | +1 |
| coherence coupling measurement | **_(keep)_** | +1 |
| cold start in naming principles md | **cold start** | +1 |
| communal imagination test | **_(keep)_** | +1 |
| communal imagination test in naming principles md | **communal imagination test** | +1 |
| comprehension time implementation time | **keep both** | +1 |
| conspectus | **active context** | +1 |
| contraction hierarchy | **contraction tier** | +1 |
| contraction over drift principle | **contraction imperative** | +1 |
| coordination overhead threshold | **coordination tax** | +1 |
| da2 inc | **_(keep)_** | +1 |
| dark room critique citation phrasing sun firestone | **dark room critique** | +1 |
| default internal processing before output | **interior baseline** | +1 |
| empirical heuristic discussion third ring | **calibration ring** | +1 |
| epistemic architecture for bounded correction under decomposed disturbance | **bounded correction architecture** | +1 |
| epistemic opacity | **keep but flag baggage** | +1 |
| evidence starvation canonicalize | **reaffirm 3 with collective confirmation** | +1 |
| five phase cycle | **adaptive pentad alternative five phase cycle keep** | +1 |
| future segment information theoretic cost floor for persistence | **persistence cost** | +1 |
| gain sector bridge gain sector derivation | **keep both** | +1 |
| gate 1 gate 2 gate 3 gate 4 format md promotion gates | **keep gate numbers but add one word names** | +1 |
| gemini s analysis paralysis for excessive deliberation | **reject analysis paralysis** | +1 |
| gemini s boyd exponent for adversarial tempo advantage | **reject boyd exponent** | +1 |
| gemini s competency trap for $\eta^\ast \to 0$ | **reject competency trap** | +1 |
| gemini s epistemic death for the gain collapse unobservable DAG failure | **reject epistemic death** | +1 |
| hierarchy as a project wide word | **flag four independent hierarchies overloaded** | +1 |
| hierarchy as repeated word | **reserve for pearl s rename others selectively** | +1 |
| hierarchy project wide | **reserve for pearl s causal hierarchy strict asymmetric uses** | +1 |
| honest limits | **limits** | +1 |
| identifiability floor escape the floor | **escape route** | +1 |
| ii actuated adaptation agentic systems | **ii purposeful adaptation actuated agents** | +1 |
|  | ii agentic systems purposeful adaptation | +1 |
| iii agentic composites | **iii composition agentic composites** | +1 |
| intent planning vocabulary | **intent** | +1 |
| interpres | **context mediator** | +1 |
| l1 correlation hierarchy prime decoration | **l1 observable** | +1 |
| l1 prime decoration | **l1 observable** | +1 |
| logostratum RLHF4 backbone | **cognitive substrate** | +1 |
| logozoetic agents | **_(keep)_** | +1 |
| loop is level 2 engine der loop interventional access | **the perpetual experiment** | +1 |
| matrix CIY tensor CIY | **fisher CIY matrix CIY consistent** | +1 |
| migration map md | **_(keep)_** | +1 |
| mismatch injection rate $\rho$ | **mismatch injection rate** | +1 |
| model sufficiency $S$ | **predictive sufficiency** | +1 |
| model sufficiency model class fitness | **keep** | +1 |
| model synchronization cost reversal under ambiguity | **ambiguity reversal** | +1 |
| msc architectural proposals yyyy mm dd md | **retire once consolidated into proposals md** | +1 |
| msc reflections | **_(keep)_** | +1 |
| multi agent scope | **shared environment scope** | +1 |
|  | _(keep)_ | +1 |
| observability boundary in a strategy DAG | **observability frontier** | +1 |
| observability opacity | **keep as an informational pair** | +1 |
| observation function action transition | **keep** | +1 |
| old TST files 40 files | **no rename these retire with migration map** | +1 |
| outline md 01 AAD core preamble | **reading AAD** | +1 |
| output after context turnover without state restoration | **cold reconstruction** | +1 |
| p ij edge confidence weight | **edge credence** | +1 |
| pearl l1 l2 l3 | **predicting exploring reasoning** | +1 |
| pearl-level 2 causal contrast | **the agent s choice actually changes what happens** | +1 |
| persistence three senses structural operational continuity | **keep three senses sharpen usage sites** | +1 |
| pi parameterization invariance | **coordinate freedom axiom** | +1 |
| prior art integration convention | **prior art integration** | +1 |
| privileged high identifiability calibration laboratory | **high identifiability calibration lab** | +1 |
| promote in topological order | **topological promotion order** | +1 |
| r1 r2 result numbering convention in logogenic agents | **keep with cross component prefixes l r1 l r2** | +1 |
| readme md lexicon | **_(keep)_** | +1 |
| readme md structure | **readme md theory architecture** | +1 |
|  | _(keep)_ | +1 |
| recursive update derivation gain sector derivation | **standardize as derivation suffix for derivation type appendices** | +1 |
| section ii actuated adaptation agentic systems | **_(keep)_** | +1 |
| section ii header actuated adaptation agentic systems | **actuated adaptation agentic systems** | +1 |
| sector condition derivation | **_(keep)_** | +1 |
| self actuated agent | **autonomous agent** | +1 |
|  | self directed agent | +1 |
| software scope | **_(keep)_** | +1 |
| source quality uncertainty | **source uncertainty** | +1 |
| spike research artifact | **spike** | +1 |
| spikes index md | **_(keep)_** | +1 |
| spikes index md spike index | **spikes index md** | +1 |
| spikes spike topic md | **_(keep)_** | +1 |
| spikes spike topic yyyy mm dd md | **_(keep)_** | +1 |
| strategic dynamics derivation | **_(keep)_** | +1 |
|  | strategy edge dynamics | +1 |
| strategy | **_(keep)_** | +1 |
| sufficiency discontinuity | **sufficiency drop** | +1 |
| symbol default bias bound track 1 track 2 | **transport track fisher track** | +1 |
| symbol default g t in prose | **purposeful state** | +1 |
| symbol default m t in prose | **model state** | +1 |
| system coherence system coupling system availability | **keep all three** | +1 |
| temporal coherence markers | **_(keep)_** | +1 |
| terminal alignment error | **terminal alignment gap** | +1 |
| the greek vocabulary | **the greek philosophical vocabulary** | +1 |
| the integrated κ × a law | **the bias bound product law** | +1 |
| the scaffolding tax | **scaffolding tax** | +1 |
| the trio collectively | **epistemic architecture** | +1 |
| three part meta architecture | **floor ladder forced coordinates** | +1 |
| todo md active pending review spikes | **todo md active** | +1 |
| track 1 track 2 in bias bound derivation | **transport inequality track fisher rao track** | +1 |
| transition opacity | **heading flag only** | +1 |
| triple depth penalty canonicalize | **reaffirm 3 with new framing** | +1 |
| u f update rule homogeneity | **update rule homogeneity** | +1 |
| u m u o u σ unity dimensions | **epistemic unity teleological unity strategic unity** | +1 |
| unnamed TST specific name for code that is observation cheap because it s well written | **observation cheap code** | +1 |
| unnamed agent as a projection whose contraction rate must exceed its target s drift | **contraction imperative** | +1 |
| unnamed an organizational level instance of the persistence condition s bathtub gloss | **the bathtub model** | +1 |
| unnamed calibration laboratory framing as reusable meta move | **calibration domain calibration lab** | +1 |
| unnamed cascade of inferential force strengthening from c1 to c3 on satisfaction gap control regret diagnostics | **inferential cascade** | +1 |
| unnamed cascade of inferential force through c1 c2 c3 | **inferential force cascade** | +1 |
| unnamed chain layer anchor role in additive coordinate forcing | **chain anchor** | +1 |
| unnamed class 1 class 2 class 3 agent classes themselves need mnemonic handles | **proposal assign english modifiers** | +1 |
| unnamed complexity driven resistance to change as features accumulate | **structural accumulation drag** | +1 |
| unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3 | **inferential force cascade** | +1 |
| unnamed cycle phase sequence as a whole | **the adaptive pentad** | +1 |
|  | the pentad | +1 |
| unnamed cycle phase sequence as whole | **the pentad five phase cycle** | +1 |
| unnamed decomposing mismatch into environment vs other sub agents actions | **internal mismatch attribution** | +1 |
| unnamed effort time risk ranking considered false constraints | **false constraints** | +1 |
| unnamed empty stability plasticity feasibility window in consolidation dynamics | **stability plasticity collapse** | +1 |
| unnamed epochal stability → latent diversification → niche emergence | **punctuated composition dynamics** | +1 |
| unnamed externalizing part of $M_t$ into the environment for future agents | **model inscription** | +1 |
| unnamed fourth diagnostic where terminal conditions are met but the objective is still missed | **terminal alignment error** | +1 |
| unnamed future segment layer header for narrative pedagogical framing | **narrative framing** | +1 |
| unnamed future segment layer header for the sp 5 reader s path proposal | **reader s path** | +1 |
| unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$ | **commit chronica** | +1 |
| unnamed joseph s mental model projection whose contraction rate must exceed its target s drift rate | **the projection slogan contraction over drift slogan** | +1 |
| unnamed minimum sufficiency required after a session rebuild | **reentry threshold** | +1 |
| unnamed scope honesty as architecture | **honesty** | +1 |
| unnamed the 1 anchor 3 theorem structure in additive coordinate forcing | **anchored theorem pattern** | +1 |
|  | identity anchored forcing | +1 |
| unnamed the 1 anchor 3 theorem structure itself | **anchor theorem pattern** | +1 |
| unnamed the 1 anchor plus 3 theorem characterization | **pattern anatomy** | +1 |
| unnamed the 1 anchor plus 3 theorem structure | **anchor and forcing quartet** | +1 |
|  | anchor theorem trio | +1 |
| unnamed the 2×2 orient cascade diagnostic table | **the cascade diagnostic or the 2×2 diagnostic** | +1 |
| unnamed the 2×2 satisfaction gap control regret table | **diagnostic square** | +1 |
| unnamed the 2×2 satisfaction gap × control regret diagnostic table | **the 2×2 diagnostic** | +1 |
| unnamed the AAD expressible failure mode of an empty stability plasticity window | **consolidation starvation** | +1 |
| unnamed the a2 sub scope partition collectively | **a2 partition** | +1 |
| unnamed the architectural class partition class 1 class 2 class 3 | **architectural partition** | +1 |
| unnamed the calibration laboratory concept applied outside TST | **calibration domain** | +1 |
| unnamed the chain confidence decay mathematical anchor as the 1 in 1 anchor 3 theorem | **chain anchor** | +1 |
| unnamed the class 1 sub agents class 3 composite phenomenon in strategic composition | **strategic entanglement** | +1 |
| unnamed the complete adaptive cycle from anticipation through action | **adaptive cycle already named in lexicon** | +1 |
| unnamed the condition that a strategy DAG s endosymbiont crosses the composite agent scope from below | **crossing threshold** | +1 |
| unnamed the condition that the agent s event observation pairs constitute genuine interventions as opposed to passive associations | **interventional character** | +1 |
| unnamed the contraction over drift insight | **drift contraction inequality** | +1 |
| unnamed the cumulative prediction error that an agent has tolerated without updating its model | **tolerance budget standing mismatch reservoir** | +1 |
| unnamed the cycle as a whole | **adaptive traversal** | +1 |
|  | the adaptive pentad | +1 |
|  | ✗ the five turn | -1 |
| unnamed the derivation formulation hypothesis status gradient in format md | **epistemic gradient** | +1 |
| unnamed the dimensional consistency constraint forcing the macro step formulation | **dimensional consistency repair** | +1 |
| unnamed the discipline of naming so that the slug survives reorganization | **reorganization resilient naming** | +1 |
| unnamed the dual that pairs with persistence envelope on the strategic side | **strategic persistence envelope** | +1 |
| unnamed the externalization reconstruction cycle across sessions | **memory relay** | +1 |
| unnamed the failure mode where an agent s model class cannot represent the environment s true causal structure | **model class insufficiency or structural unidentifiability** | +1 |
| unnamed the functional requirements are the results formalisms are the engineering slogan | **functional primacy** | +1 |
| unnamed the invisible time spent building $M_t$ | **comprehension drag** | +1 |
| unnamed the iterated audit process gemini opus codex de novo consolidated three doc portfolio | **cross model audit cycle** | +1 |
| unnamed the loss of coherent identity when an agent s interactions are severed or its continuity is broken | **continuity loss or persistence fracture** | +1 |
| unnamed the mathematical operation by which agents convert observed mismatch into structural revision | **structural cascade** | +1 |
| unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing | **three part scope architecture** | +1 |
| unnamed the moment when an agent s identity claim becomes load bearing because actions become irreversible | **constitutive moment** | +1 |
| unnamed the organizing principle slogan an adaptive system is a projection whose contraction rate exceeds its target s drift rate | **projection contraction slogan** | +1 |
| unnamed the orient cascade s information dependency forced ordering as a meta pattern | **information dependency forcing** | +1 |
| unnamed the pattern where AAD s negative results floors strengthen the machinery that escapes them | **floor strengthening inversion** | +1 |
| unnamed the phenomenon that unobservable edges freeze and paths become epistemically dead | **observability dominance** | +1 |
| unnamed the procedure of reading any segment through all three meta segments | **triple lens review** | +1 |
| unnamed the rate at which an agent s chronica grows compared to compression cadence | **chronica throughput** | +1 |
| unnamed the region in parameter space where parametric updates remain effective before structural change is forced | **parametric regime or stability envelope** | +1 |
| unnamed the region where temporal nesting holds | **temporal coherence zone** | +1 |
| unnamed the scope honesty as architecture working principle | **honesty scope honesty as architecture** | +1 |
| unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it | **deliberation phase exploration exploitation tradeoff** | +1 |
| unnamed the self reinforcing code quality → tempo loop | **comprehension flywheel** | +1 |
| unnamed the set of five conditions under which a2 is derived rather than assumed the sub scope α agent classes | **derived sector classes** | +1 |
| unnamed the signed coupling structure across all section iii results | **signed coupling pattern** | +1 |
| unnamed the strengthen before soften posture applied to apparent overclaims | **epistemic strengthening posture** | +1 |
| unnamed the strengthen first attempt artifact a spike that tried to derive something stronger and failed | **strengthening attempt attempt record** | +1 |
| unnamed the symbol overload region where $U_M$ means two different things | **the $U_M$ overload** | +1 |
| unnamed the template family sector persistence contraction possible future dissipativity | **persistence templates the template family** | +1 |
| unnamed the three concentric rings of segment content inevitability core canonical formulations empirical heuristic | **three rings** | +1 |
| unnamed the three rings of segment content framing | **segment rings** | +1 |
| unnamed the threshold energy information cost below which an agent is forced to act accept mismatch rather than deliberate | **deliberation threshold** | +1 |
| unnamed the unobservable edges in a strategy DAG that cannot be revised because their values cannot be inferred | **observability frontier** | +1 |
| unnamed the virtuous vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity | **model strategy coupling** | +1 |
| unnamed variation in correction architectures invisible to persistence analysis | **latent structural diversity** | +1 |
| value object → def trajectory value | **conditional support for codex s rename** | +1 |
| what is derived vs what is chosen | **derivation audit** | +1 |
|  | derived vs chosen vs assumed | +1 |
| what is derived vs what is chosen derivation audit table | **derivation audit** | +1 |
| what is derived vs what is chosen derivation audit table heading | **derivation audit** | +1 |
| worked example bandit | **_(keep)_** | +1 |
| worked example kalman | **_(keep)_** | +1 |
| worked example l1 | **_(keep)_** | +1 |
| worked example strategy | **_(keep)_** | +1 |
| working vocabulary observation the framework s honesty is load bearing | **load bearing honesty** | +1 |
| 𝒯 σ strategic tempo | **strategic tempo** | +1 |
| $G_t$ goal state | **symbol is clear no alias needed** | +0 |
| $\mathcal{T}$ adaptive tempo | **tempo already canonical** | +0 |
| $\rho$ disturbance rate | **disturbance rate already in use** | +0 |
| unnamed the dual concept to satisfaction gap what the world permits minus what the agent achieves | **this is def control regret already named** | +0 |
| unnamed the five phases of the adaptive cycle | **already named in notation md** | +0 |
| unnamed the mechanism by which an agent uses the feedback loop to gain interventional access to causal structure | **loop as intervention or is this der loop interventional access** | +0 |
| unnamed the moment when an agent s model updates due to observing a mismatch | **epistrophe event or is this just the phase** | +0 |
| $\beta$ a2 sub scope | **✗ posited regime** | -1 |
| AAD | **✗ adaptation and agency dynamics AAD** | -1 |
|  | ✗ adaptation and purpose dynamics apd | -1 |
| AAD alternatives considered for completeness | **✗ apd adaptation and purpose dynamics** | -1 |
|  | ✗ AAD adaptation and agency dynamics | -1 |
| a2 operator sector condition under fidelity degraded updates | **✗ ** | -1 |
| claude md key architectural decisions | **✗ claude md architectural decisions** | -1 |
| dark room exploration drive | **_(keep)_** | -1 |
| empirical heuristic discussion ring | **✗ third ring or empirical periphery** | -1 |
| l1 | **✗ l1 c** | -1 |
| l1 l1 prime | **✗ l1 observable l1 soft** | -1 |
| type formulation | **✗ type representation** | -1 |
| unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic | **✗ satisfaction control table the diagnostic 2×2** | -1 |
| unnamed the cross cycle equivalent of the bathtub gloss multi cycle persistence as a savings account | **✗ the savings account gloss** | -1 |
| unnamed the four axis content structural unity decomposition | **✗ the unity quintet** | -1 |
| unnamed the meta architecture of the three meta segments | **✗ AAD s epistemic triptych** | -1 |
| unnamed the pattern where the agent s optimal update direction is determined by both gain and directional fidelity together | **✗ gain fidelity product** | -1 |
| unnamed the persistence envelope | **✗ adaptive basin** | -1 |
| unnamed the property that correction dynamics are approximately isotropic | **✗ isotropic correction regime** | -1 |
| unnamed the three part meta pattern structure across the three meta segments | **✗ AAD s meta architecture scope honesty meta frame** | -1 |
| RLHF6 | **_(keep)_** | -3 |

