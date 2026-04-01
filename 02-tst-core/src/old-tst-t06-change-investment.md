---
label: T-06
type: Theorem
subtype: Derived
name: Change Investment Principle
dependencies:
  - "[[t01-time-optimality.md|T-01]]"
  - "[[t04-change-expectation-baseline.md|T-04]]"
  - "[[t05-dual-optimization.md|T-05]]"
older-tag: FP-004
revision: 0.2
---

# T-06 Theorem (Derived): Change Investment

**Statement:** Changes that increase individual implementation time but decrease amortized time over expected future changes are preferred, with preference strength proportional to expected change count.

## Simple Form (Core Principle)

$$
\begin{aligned}
&\text{For change implementation options } C_1, C_2 \text{ for feature } F: \\
&\text{if } \text{time}(C_1) > \text{time}(C_2) \quad \text{// } C_1 \text{ takes longer now} \\
&\text{but } E\left[\sum_i \text{time}_{\text{future}}(F_i \mid C_1)\right] < E\left[\sum_i \text{time}_{\text{future}}(F_i \mid C_2)\right] \quad \text{// but saves time later} \\
&\text{then } \text{prefer}(C_1) \propto E[\text{num\_future\_changes}]
\end{aligned}
$$

## Limit Form (Primary Decision Rule)

$$
\begin{aligned}
&\text{As } n_{\text{future}} \to \infty: \\
&\text{prefer}(C_1, C_2) = \arg\min(E[\text{time}_{\text{future\_per\_change}}(F \mid C)])
\end{aligned}
$$

**In practice:** Choose the implementation that minimizes expected future change time, ignoring current implementation time differences for long-lived systems.

## Threshold Form (Practical Application)

$$
\begin{aligned}
&\text{For finite } n_{\text{future}} \text{ (from T-03, default to } n_{\text{past}}\text{):} \\
&\text{Choose } C_1 \text{ over } C_2 \text{ when:} \\
&\text{time}(C_1) - \text{time}(C_2) < n_{\text{future}} \times \left[E[\text{time}_{\text{future}}(F \mid C_2)] - E[\text{time}_{\text{future}}(F \mid C_1)]\right]
\end{aligned}
$$
Or more intuitively: "Accept $X$ extra minutes now to save $Y$ minutes per future change when $X < n_{\text{future}} \times Y$"

## Amortized Time Calculation

$$
\text{time}_{\text{amortized}}(C) = \text{time}(C) + \frac{E\left[\sum_i \text{time}_{\text{future}}(F_i \mid C)\right]}{1 + n_{\text{future}}}
$$

**Critical Insight:** This principle explains why software typically exhibits one of two patterns:

1. **Positive compound** (principled): Each change makes future changes easier
2. **Negative compound** (technical debt): Each change makes future changes harder

The inflection point is whether changes are made with future amortization in mind.

**Boundary Conditions:**

- **Information Requirement:** Requires estimating future change patterns
- **Discount Rate:** Future time savings might be worth less than present time (team might not exist, code might be replaced)
- **Local vs Global:** A local optimization might increase global implementation time

## Discussion: The Near-Zero Cost Insight

In practice, the "principled" implementation often requires minimal additional time over the "quick" implementation—it's primarily a matter of making better architectural decisions, not spending significantly more time. The question becomes: "Which organization of this code will make future changes easier?" rather than "How much time should I invest?"

Examples:

- Choosing the right module boundaries (near-zero time difference)
- Naming variables clearly (seconds of difference)
- Extracting a function vs inline code (minutes of difference)

The skill is in prediction, not in time investment.

**Prediction Under Uncertainty:** All applications of this principle operate under uncertainty about future changes. The "art" lies in:

1. **Pattern Recognition:** What kinds of changes have happened before?
2. **Domain Knowledge:** What changes are typical in this problem space?
3. **Strategic Context:** What's on the roadmap or likely to be?
4. **Probabilistic Thinking:** Not "will this change?" but "what's the probability?"

When uncertainty is high, bias toward changes that preserve optionality.

**Aggregation Across Scopes:** When a change affects multiple modules differently:

$$
\text{net\_impact} = \sum_i P(\text{change in module}_i) \times \text{time\_impact}(\text{module}_i)
$$
A change that makes one module easier and another harder is preferred only if the expected time savings exceed the expected time costs.

**The Compound Effect:** This principle predicts a bifurcation in codebases:

- **Virtuous cycle:** Principled changes → easier future changes → more capacity for principled changes
- **Vicious cycle:** Rushed changes → harder future changes → less capacity for principled changes

The initial conditions (early changes) have outsized impact due to compounding.

## Meta: Status and Planning

### Future Research Directions

- Formal treatment of time-to-comprehension (especially for team turnover)
- Discount rates for future time (though empirically may be less important than expected)
- Proxy metrics for measuring actual time impact
- Quantification of optionality preservation in high-uncertainty contexts