---
label: T-13
type: Theorem
subtype: Empirical
name: Comprehension Continuity Principle
dependencies:
  - "[[t05-dual-optimization.md|T-05]]"
  - "[[t12-comprehension-proximity-correlation.md|T-12]]"
older-tag: FP-012
revision: 0.2
---

# T-13 Theorem (Empirical): Comprehension Continuity Principle

**Statement:** Time-to-comprehension increases exponentially with discontinuities—points where understanding requires searching elsewhere for context.

$$
\text{time}_{\text{comprehension}}(\text{code}) = \text{base\_time} \times (1 + \alpha)^{\text{discontinuities}(\text{code})}
$$
Where $\alpha \approx 0.2$ (empirically observed) and discontinuities include:
- Symbol resolution searches ("where is this defined?")
- Usage searches ("what calls this?")
- Type inference gaps ("what type is this?")
- Behavioral inference gaps ("what does this do?")
- Context switches between files/modules/services

$$
\text{discontinuity\_score} = \sum_{\text{element}} \text{search\_probability}(\text{element}) \times \text{search\_cost}(\text{element})
$$
**Justification:**

- **Cognitive Science:** Each discontinuity requires context switching and working memory reload
- **Empirical:** Studies show comprehension time increases 20-30% per discontinuity
- **Practical:** Linear code is debugged 2-5x faster than jump-heavy code

**Critical Insight:** A single 100-line function may be more comprehensible than 10 ten-line functions if the latter requires 20 discontinuous jumps to understand the flow. This challenges conventional "small functions" wisdom.

**Boundary Conditions:**

- **IDE Support:** Modern tools can reduce search cost but not context-switch cost
- **Familiarity:** Well-known patterns create mental shortcuts around discontinuities
- **Documentation:** Can create "bridges" over discontinuities

## Discussion: The Comprehension vs. Changeability Tension

Traditional advice emphasizes small, focused units (functions, classes, modules) for changeability. However, this creates comprehension discontinuities. The resolution:

- For $n_{\text{past}} < 10$: Favor continuity (inline code, larger functions)
- For $n_{\text{past}} > 10$: Favor modularity (accept discontinuities for change isolation)

**Types of Discontinuities:**

1. **Lexical:** Symbol must be found elsewhere in same file
2. **File:** Must open another file
3. **Module:** Must understand another module's context
4. **Service:** Must understand another service's API
5. **Network:** Must trace through network calls

Each level approximately doubles comprehension time.

**Measuring Discontinuities in Practice:** Count the number of times understanding a feature requires:

- Searching for a definition
- Opening a new file
- Reading documentation
- Tracing through indirection
- Mental context switching

**Anti-Patterns That Create Discontinuities:**

- Premature abstraction
- Over-interfacing
- Excessive indirection
- Clever code minimization
- Naming minimalism