---
label: T-09
type: Theorem
subtype: Empirical
name: Change-Set Size Principle
dependencies:
  - "[[d02-atomic-change-set.md|D-02]]"
older-tag: FP-008
revision: 0.2
---

# T-08 Theorem (Empirical): Change-Set Size Principle

**Statement:** Time to implement a feature is proportional to the size of its atomic change-set for non-automatically-generated code.

$$
\text{time}_{\text{implementation}}(F) \propto |\text{changeset}(F)|
$$
Where $|\text{changeset}|$ measures:
- Lines changed (added + deleted + modified)
- Files touched
- Modules affected

Excluding: generated code, build artifacts, automated reformatting

**Justification:**

- **Empirical:** Strong correlation observed across projects and developers
- **Cognitive:** Each change requires context switching and validation
- **Mechanical:** Physical time to type/modify code
- **Verification:** Testing burden scales with change size

**Critical Insight:** This provides our first measurable proxy for the abstract concepts in T-01 through T-06. We can now evaluate architectural decisions by their expected impact on future change-set sizes.

## Discussion: Why This Proxy Works

Change-set size correlates with:

1. **Cognitive Load:** More changes = more mental context to maintain
2. **Error Probability:** More changes = more opportunities for bugs
3. **Review Time:** Linear correlation with code review duration
4. **Test Surface:** More changes = more test scenarios

**Limitations:**

- **Quality Variance:** 10 lines of complex logic ≠ 10 lines of boilerplate
- **Language Dependence:** Some languages are more verbose
- **Tool Assistance:** AI/IDE support can make large changes faster

Despite limitations, this remains the best easily-measurable proxy for implementation time.

**Historical Analysis Enabled:** With this principle, we can analyze git history to:

- Measure which architectural decisions led to smaller future changes
- Identify patterns that correlate with change-set explosion
- Validate whether refactoring actually reduced future change sizes

**Practical Application:** When making architectural decisions, ask: "Will this choice lead to smaller or larger change-sets for likely future features?"

Examples:

- **Good:** Centralized configuration (single-point changes)
- **Bad:** Scattered magic numbers (many-point changes)
- **Good:** Well-defined interfaces (local changes)
- **Bad:** Leaky abstractions (cascade changes)