---
label: T-04
type: Theorem
subtype: Fundamental
name: Change Expectation Baseline
dependencies:
  - "[[t02-implementation-time-lower-bound#D-01 Definition Feature|D-01]]"
older-tag: FP-003
revision: 0.3
---
	
# T-04 Theorem (Fundamental): Change Expectation Baseline

## Formal Definitions

### Theorem Statement

Absent specific information about a software system's future, the expected number of future feature additions equals the observed number of past features added (uninformative prior). With additional information, this serves as the baseline to adjust from.

### Formal Expression

$$
\begin{aligned}
&\text{With no information: } E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} \\
&\text{With information } I: E[n_{\text{future}} \mid n_{\text{past}}, I] = n_{\text{past}} \times \text{adjustment}(I)
\end{aligned}
$$

Where $n_{\text{past}}$ = number of features added to date, $n_{\text{future}}$ = number of features to be added

#### Discrete Finite Adjustment Form

For small $n_{\text{past}}$ or discrete simulations, following Laplace's rule of succession:

$$E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} + 1$$

With termination probability at each step: $P(\text{terminate}) = \frac{1}{n_{\text{past}} + 2}$

#### Mathematical Basis (Lindy Effect)

This theorem is *not* empirical but emerges mathematically from Bayesian inference with uninformative priors. Following Ord (2023)[^1], the Lindy effect arises from pure mathematics:

**Starting point**: Maximum ignorance about system lifetime, represented by the scale-invariant (Jeffreys) prior:
$$\rho(T) \propto \frac{1}{T} \text{ for } T > 0$$

This is the unique prior satisfying:
- Scale invariance: $P(T \in [a,b]) = P(T \in [ca,cb])$ for any scale factor $c$
- Maximum entropy for positive scale parameters (Jaynes, 1968)[^2]
- Copernican principle: observing at random point yields median future = past (Gott, 1993)[^3]

**Bayesian update**: After observing survival to time $t_0$:
$$\rho(T|T > t_0) = \begin{cases} 
0 & \text{if } T \leq t_0 \\
\frac{t_0}{T^2} & \text{if } T > t_0 
\end{cases}$$

This is a Pareto distribution with $\alpha = 1$, yielding:
$$\text{Median}[\text{remaining lifetime}] = \text{current age} = t_0$$

### Corollary 1

Investment in abstraction and flexibility should scale proportionally with $n_{\text{past}}$, as the expected return period equals the observed lifetime.

### Corollary 2

Systems with minimal feature history (e.g., $n_{\text{past}} < 3$) warrant minimal structural investment, as the expected future is similarly brief. The apparent tension with compounding benefits resolves mathematically: the expected value of any investment is $\Delta t \times E[n_{\text{future}}]$, where $\Delta t$ is time saved per future change. When $E[n_{\text{future}}]$ is small, only investments with disproportionately high $\Delta t$ are justified.

### Corollary 3

With specific information $I$, the baseline serves as the prior for Bayesian updating:

$$P(n_{\text{future}} | n_{\text{past}}, I) = \frac{P(I | n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} | n_{\text{past}})}{P(I | n_{\text{past}})}$$

Where $P(n_{\text{future}} | n_{\text{past}})$ is the uninformative prior from the main theorem. This establishes the baseline as the starting point for all domain-specific reasoning, not a claim about actual futures.

### Scope

- **Applies to**: Here we are defining features specifically as defined in [[t02-implementation-time-lower-bound#D-01 Definition Feature|T-02's D-01]].
- **Information updates**: As per Corollary 3, specific knowledge (sunset dates, roadmaps) updates and may dominate the prior
- **System discontinuities**: When $P(F_{\text{future}} | S_{\text{old}}) \neq P(F_{\text{future}} | S_{\text{new}})$ (e.g., after major rewrites), this constitutes information $I$ that updates the baseline via Corollary 3—very likely dominating the uninformative prior (for better or worse, which TST makes no claim about at this point)

## Discussion

### The Null Hypothesis of Change

This principle doesn't claim empirical truth about all software, but provides the principled default assumption when you lack better information. It's the "null hypothesis" of feature prediction—deliberately conservative, assuming the future will resemble the past unless you have specific information suggesting otherwise.

- - -
[^1]: Ord, T. (2023). "The Lindy Effect." arXiv:2308.09045, Section 2: "Mathematical mechanisms for producing a Lindy effect"
[^2]: Jaynes, E. T. (1968). "Prior Probabilities." IEEE Transactions on Systems Science and Cybernetics, 4(3), 227-241
[^3]: Gott, J. R. (1993). "Implications of the Copernican principle for our future prospects." Nature, 363, 315-319
