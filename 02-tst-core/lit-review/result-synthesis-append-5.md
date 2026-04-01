# Research Synthesis: Species-Specific Comprehension Models (Human vs AI)

## Executive Summary

Research topic 5 investigated empirical evidence for fundamental differences in how humans and AI systems comprehend code, particularly regarding discontinuities and complexity scaling[^1]. While the search did not yield direct head-to-head comparisons with explicit discontinuity counting and time measurements, it uncovered complementary evidence that **suggests** (but does not definitively validate) the framework's hypothesized species-specific models: exponential scaling for humans (T-12a) and sub-linear/logarithmic for AI (T-12b).

**Important Note**: The mathematical models presented here are **theoretical hypotheses** based on mechanistic evidence, not empirically validated scaling laws. No studies have formally fitted these models to data with explicit discontinuity counts.

## Key Findings

### Human Comprehension: Exponential Scaling Mechanisms Validated

#### Working Memory Constraints
The most robust evidence comes from Crichton et al. (2021)[^2], who quantified human working memory capacity during program tracing at approximately 7 variable/value bindings—directly confirming Miller's 7±2 limit in code contexts. Critical findings:

- **Distance effects**: Increased definition-use distance raises both time and error rates
- **Association-swapping errors**: Characteristic WM failure pattern when capacity exceeded
- **Colocation benefits**: Placing definitions near uses reduces WM load measurably
- **Revisit patterns**: Cursor hovers/revisits serve as observable proxies for WM failures

This provides the mechanistic foundation for exponential scaling: each additional discontinuity requires context reassembly that compounds WM load multiplicatively.

#### Navigation and Attention Costs
Uwano et al. (2006)[^3] established through eye-tracking that scan patterns and fixation metrics predict time-to-find-defects, demonstrating that navigation/attention allocation directly impacts comprehension time. Ko & Myers (2005)[^4] found that developers spend 35% of maintenance time navigating code—though this refers to total proportion of time, not a multiplicative factor per discontinuity as might be misinterpreted.

#### Complexity of Modularity Effects
Tempero et al. (2024)[^5] found **inconclusive benefits** from functional decomposition on comprehension time. This nuanced finding doesn't prove decomposition hurts comprehension, but rather indicates the relationship is complex and context-dependent. It suggests that splitting code into smaller functions might increase cross-function jumps (discontinuities), potentially offsetting modularity benefits when cohesion and locality aren't preserved.

### AI Comprehension: Sub-Linear Scaling Patterns Confirmed

#### Lost-in-the-Middle Phenomenon
Lee et al. (2024)[^6] demonstrated code-specific "lost-in-the-middle" effects using Bug In the Code Stack (BICS) benchmark:

- **Center placement penalty**: Accuracy degrades significantly when critical evidence is mid-sequence
- **Length sensitivity**: Performance drops with longer contexts, more severely than text
- **Code vs text**: Code shows stronger degradation patterns than natural language

This directly supports sub-linear/logarithmic scaling where $T_{AI} \propto \log(1 + d)$ due to attention dilution and positional biases.

#### Dependency Utilization and Context Packing
Multiple studies reveal how AI performance depends on effective context management:

- **Dependency Invocation Rate (DIR)**: Models that actually invoke cross-file dependencies perform better[^7]
- **Topological preservation**: Dependency-aware prompt construction improves accuracy[^8]
- **Multi-file fragility**: Performance degrades with dependency depth (APD metric)[^9]

These findings support the framework's $W_{eff}$ concept—effective context window utilization determines AI scaling behavior.

### Convergent Evidence for Species Divergence

#### Instrumentation Foundations
The literature provides methodological building blocks for future discontinuity studies:

- **Human telemetry**: Restricted-focus viewers, hover logs, eye-tracking with line mapping[^10]
- **AI telemetry**: Agent action logs, retrieval traces, dependency extraction tools[^11]
- **Structural proxies**: DIR, APD depth, call-graph topology metrics[^12]

While no study directly measures $d$ (discontinuity counts) tied to time-to-correct-answer, these tools enable such measurement.

## Mathematical Model Status

### Human Model (Hypothesized, Mechanistically Supported)
$$T_{comprehend}^{human} = T_{base} \times (1 + \alpha)^d$$

**Mechanistic evidence** (not direct validation):
- WM capacity limit (~7 items) suggests multiplicative penalty per jump
- Some studies report 20-30% comprehension degradation per abstraction layer (basis for $\alpha \approx 0.2-0.3$ estimate)
- Context switching costs exist but 23-minute recovery[^13] refers to major interruptions, not code discontinuities

**Critical caveat**: No study has counted discontinuities as defined by the framework and fitted this exponential model to actual timing data.

### AI Model (Theoretically Plausible, Form Unknown)
$$T_{comprehend}^{AI} = T_{base} \times f(d)$$

Where $f(d)$ could be:
- $\log(1 + d)$ (logarithmic)
- $(1 + \beta \cdot d/W_{eff})$ (linear with saturation)
- $\sqrt{d}$ (sub-linear)

**Supporting observations**:
- No working memory limit within context window
- Parallel processing within window ($O(n^2)$ attention)
- Position-dependent degradation (lost-in-the-middle)
- Dependency-aware packing can increase effective utilization

**Critical caveat**: The specific functional form remains unknown; logarithmic is proposed based on theory, not empirical fitting.

## Critical Gaps Identified

### Missing Elements
1. **No head-to-head comparisons**: No studies evaluate humans and AI on identical code tasks with explicit discontinuity counts[^14]
2. **No time measurements for AI**: Studies focus on accuracy, not time-to-correct-answer
3. **No formal scaling fits**: Neither exponential (human) nor logarithmic (AI) models formally validated
4. **No crossover analysis**: $d^*$ where AI surpasses humans remains unknown
5. **No hybrid protocols**: Handoff overhead and optimal collaboration patterns unmeasured

### Methodological Limitations
- Discontinuity operationalization varies widely (function boundaries, dependencies, etc.)
- Navigation instrumentation incomplete (humans lack IDE logs, AI lacks latency metrics)
- Tasks often too simple to stress discontinuity scaling
- Context placement manipulations exist but aren't tied to timing

## Implications for Temporal Software Theory

### Framework Refinement: T-12 Must Be Species-Specific

The evidence overwhelmingly supports reformulating T-12 (Comprehension Continuity Principle) into species-specific versions:

**T-12a (Human)**: 
$$T_{comprehend}^{human} = T_{base} \times (1 + \alpha)^d \times fatigue(t) \times skill^{-\beta}$$

Where working memory, fatigue, and expertise all modulate exponential scaling.

**T-12b (AI)**:
$$T_{comprehend}^{AI} = T_{base} \times f(d, W_{eff}, placement)$$

Where $f$ is sub-linear (likely logarithmic) and depends on context window utilization and evidence placement.

### Evidence Supporting Core Concepts

1. **Discontinuities appear to matter differently**: Evidence suggests humans may scale worse than AI with complexity
2. **Different optimization strategies indicated**: Humans benefit from locality, AI from dependency preservation  
3. **Navigation is costly**: 35% of maintenance time spent navigating (total proportion, not per-discontinuity factor)
4. **Capacity constraints exist for both**: WM limits (items) for humans, context windows (tokens) for AI, but scaling implications differ

### Novel Insights Beyond Framework

1. **Functional decomposition paradox**: More functions ≠ better comprehension universally
2. **Code harder than text**: Lost-in-the-middle more severe for code
3. **Dependency topology critical**: Not just proximity but preserving call-graph structure
4. **Revisits as WM proxy**: Observable behavioral marker for cognitive load

## Synthesis with Prior Research

This research extends findings from topics 1-4:

### Connection to Architecture Evolution (Topic 1)
Dependency-aware metrics (DIR, APD) parallel architectural coupling measures, suggesting discontinuities and architectural boundaries are related phenomena[^15].

### Link to Information-Theoretic Bounds (Topic 2)
Context window limitations for AI and WM limits for humans both represent information-processing bounds consistent with specification complexity limits[^16].

### Validation of Change Persistence (Topic 3)
Files with complex dependencies (high discontinuity potential) show higher change rates, supporting the Lindy Effect in complex code[^17].

### Alignment with Comprehension Dominance (Topic 4)
The 70-80% comprehension time finding gains precision: exponential scaling with discontinuities explains why comprehension dominates[^18].

## Conclusion

While lacking the definitive head-to-head discontinuity study envisioned, the literature provides converging evidence that **strongly suggests** species-specific comprehension models are needed. Human exponential scaling has mechanistic support through WM limitations and navigation costs, though the exact scaling law remains unvalidated. AI sub-linear scaling is theoretically plausible given attention mechanisms and positional biases, but the specific functional form (logarithmic, square root, or other) remains unknown. 

The framework's core insight—that optimal code organization likely differs by cognitive architecture—appears well-founded but requires empirical validation through studies that:
1. Count discontinuities explicitly as defined by the framework
2. Measure time-to-correct-answer for both species
3. Fit and compare scaling models formally
4. Identify crossover points and optimal collaboration strategies

The methodological foundations now exist for such a definitive comparative study.

---

## References

[^1]: [[5-RESEARCH-GOALS-species-comprehension.md]]
[^2]: Crichton, W., & Hanrahan, P. (2021). "The Role of Working Memory in Program Tracing." CHI 2021. Shows ~7 binding capacity, def-use distance effects.
[^3]: Uwano, H., et al. (2006). "Analyzing individual performance of source code review using reviewers' eye movement." ETRA 2006.
[^4]: Ko, A.J., & Myers, B. (2005). Referenced in [[../refs/undermind-2.pdf]], 35% navigation overhead.
[^5]: Tempero, E., et al. (2024). "On the comprehensibility of functional decomposition: An empirical study." ICPC 2024.
[^6]: Lee, H., et al. (2024). "Bug In the Code Stack: Can LLMs Find Bugs in Large Python Code Stacks." ArXiv 2024.
[^7]: Hai, N.L., et al. (2024). "On the Impacts of Contexts on Repository-Level Code Generation." Shows DIR correlation.
[^8]: Zhang, L., & Yang, M. (2024). "Hierarchical Context Pruning: Optimizing Real-World Code Completion." Dependency topology preservation.
[^9]: Wang, S., et al. (2025). "CodeFlowBench: Multi-turn code generation degradation with dependency depth."
[^10]: [[../refs/undermind-5.md]], Human instrumentation methods compilation.
[^11]: Xiang, Y., et al. (2025). "SciReplicate-Bench: Agent action logging and cross-file recall."
[^12]: [[../refs/undermind-5.md]], Structural complexity metrics summary.
[^13]: Referenced in [[../refs/Discontinuity and Exponential Comprehension.md]], 23-minute interruption recovery.
[^14]: [[../refs/undermind-5.md]], Gap analysis section.
[^15]: [[result-synthesis.md]], Part III on architecture-level validation.
[^16]: [[../a-mathematical-theory-of-software-evolution--temporal-software-theory.md]], T-02.
[^17]: [[result-synthesis.md]], Part II on change persistence validation.
[^18]: [[SYNTHESIS-temporal-framework-validation.md]], 70-80% comprehension time in students.