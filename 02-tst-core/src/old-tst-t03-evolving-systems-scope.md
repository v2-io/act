---
label: T-03
type: Theorem
subtype: Scope
name: Evolving Systems Scope
dependencies:
  - "[[t01-time-optimality.md|T-01]]"
  - "[[t02-implementation-time-lower-bound.md|T-02]]"
revision: 0.1
---

# T-03 Theorem (Scope): Evolving Systems Scope

## Formal Definitions

### Theorem Statement

This theorem restricts the domain of Temporal Software Theory to systems with non-negligible probability of future change, establishing that for such systems, optimization must consider total lifecycle time rather than initial implementation time alone.

### Formal Expression

$$
\begin{aligned}
\mathcal{S}_{\text{evolving}} &= \{S : P(n_{\text{future}}(S) > 0) > \varepsilon\} \\
\text{(Or equivalently): }
\mathcal{S}_{\text{evolving}} &= \{S : E[n_{\text{future}}(S)] \ge \varrho > 0 \} \\\\
\text{Domain}(\text{TST}) &= \mathcal{S}_{\text{evolving}}
\end{aligned}
$$

Where $\mathcal{S}_{\text{evolving}}$ is the set of systems that evolve through discrete [[t02-implementation-time-lower-bound#Definition D-01 *"Feature"*|features]], and $\varepsilon$ represents a non-negligible probability threshold and $\varrho$ is unknown or calculated according to later theorems.

### Corollary 1: Evolution as Optimization Target

$$ \text{For } S \in \mathcal{S}_{\text{evolving}} :$$
$$ \text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) $$

Where $F_0$ is the initial or current implementation and, in practice:
$$\sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) \gg \text{time}(F_0)$$

In this domain, software engineering becomes less about building initial systems and much more about engineering systems where future features can be implemented efficiently.

### Scope & Boundaries

**Scope Characterization:**

Systems within $\mathcal{S}_{\text{evolving}}$ typically exhibit:
- Requirements that evolve with understanding
- Dependencies that require updates
- Bugs that emerge through use
- Security vulnerabilities discovered over time
- Market conditions that shift

Systems outside $\mathcal{S}_{\text{evolving}}$ include:
- Provably correct algorithms
- Write-once embedded firmware
- Pure prototypes (intended disposal)
- Systems with mandated freeze dates

**Boundary Behavior:**
$$
\begin{aligned}
&\text{As } P(\text{change}) \to \varepsilon: \text{ non-temporal factors dominate} \\
&\text{As } P(\text{change}) \to 1: \text{ optimizing for future implementation time becomes dominant}
\end{aligned}
$$

## Discussion

### The Threshold ε

The threshold $\varepsilon$ is deliberately left unspecified. In practice, it represents the boundary below which the cost of applying TST principles exceeds their benefit. The framework's prescriptions vary continuously with $P(\text{change})$, not discontinuously at $\varepsilon$—as change probability decreases, the strength of the framework's recommendations weakens proportionally.

### The Core Extraction Insight

A profound implication emerges when we consider factoring out stable components. For any subsystem $s$ where $P(\text{change}(s)) < \varepsilon$:

$$\text{time}_{\text{future}}(s) \to 0 \implies \text{velocity}(s) \to \infty$$

This creates a powerful incentive to identify and extract truly stable algorithms and implementations. Once extracted and proven stable, these components effectively operate at infinite velocity—they never consume future implementation time. This suggests an architectural pattern:

1. **Identify invariant cores:** Algorithms, mathematical functions, proven data structures
2. **Extract and isolate:** Move these to separate, frozen modules
3. **Reap infinite velocity:** These components never appear in future change-sets

Examples include: sorting algorithms, hash functions, mathematical operations, and well-proven data structures. The framework thus provides mathematical justification for the common practice of using battle-tested libraries rather than reimplementing core algorithms.

### The Paradigm Shift

Traditional software engineering often focused on getting the initial implementation "right." This theorem establishes that for evolving systems—which comprise nearly all practical software—the initial implementation is merely the first term in a series. The optimization target must include the entire series, weighted by probability.

### Why This Scope Matters

By explicitly narrowing to evolving systems, we:
1. **Justify investment in flexibility:** Time spent on abstractions and good architecture is rational when $E[n_{\text{future}}] > 0$
2. **Explain technical debt:** Shortcuts that save initial time but increase future change time are mathematically suboptimal
3. **Ground all subsequent principles:** Everything that follows assumes we're optimizing for continuous change
4. **Incentivize stable core extraction:** Components with $P(\text{change}) < \varepsilon$ should be factored out to achieve infinite velocity