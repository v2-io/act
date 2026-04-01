# Mathematical Foundations of the Lindy Effect

> **Origin**: `~/src/_core/tst/vault/04-workspace/1-inbox/lindy-mathematical-foundations.md` (2025). Mathematical grounding for the change-expectation-baseline claim.
>
> **Relevance**: Provides rigorous Bayesian derivation for `02-tst-core/src/change-expectation-baseline.md`. Key results: Jeffreys prior $\rho(t) \propto 1/t$ yields the Lindy prediction, maximum entropy justification, uncertainty over hazard rates converging to power law with $\alpha=1$, and connection to Laplace's Law of Succession. The current segment references the Pareto(1) pathology but should incorporate this fuller derivation.

Based on extensive research, there are indeed several mathematical justifications for the Lindy Effect in terms of Bayesian statistics, particularly involving scale-invariant priors and maximum entropy principles. Here are the key mathematical foundations:

## 1. **Bayesian Justification via Scale-Invariant (Jeffreys) Prior**

Richard Gott provided a Bayesian case for the Lindy effect by starting with maximal ignorance about the lifespan of some entity, using a 'vague prior' that assigns equal likelihood to a lifespan of any order of magnitude[^1]. This is mathematically expressed as:

- Prior density: ρ(t) ∝ 1/t (log-uniform or Jeffreys prior for scale parameters)
- This is the scale-invariant prior, meaning it's invariant under changes of scale

After observing current age t₀, updating this prior via Bayes' theorem yields ρ(t) = 0 for t < t₀, and ρ(t) ∝ 1/t² thereafter, which is precisely a Pareto distribution with α = 1[^1].

This gives the narrow Lindy effect where **median future lifespan = current age**.

## 2. **Maximum Entropy Justification**

The log-uniform prior (ρ(t) ∝ 1/t) is the maximum entropy prior for a variable that takes a positive real value, which is a prominent way of formalising having maximal ignorance[^1]. This connects to the principle that:

- When you have minimal information about a positive-valued parameter
- The maximum entropy distribution (least informative) is the log-uniform distribution
- This naturally leads to power-law behavior after conditioning on survival

## 3. **Uncertainty Over Hazard Rates**

A particularly elegant mechanism emerges when considering uncertainty about constant hazard rates. If the hazard rate k is uniformly distributed over [0, K], the effective survival curve approaches a power law tail with exponent α = 1[^1]:

For uniform prior on hazard rate k ∈ [0, K]:
- Individual survival curves: S_k(t) = e^(-kt)
- Effective survival: S(t) ≈ 1/(Kt) for large Kt
- Effective hazard: λ(t) ≈ 1/t (declining, producing Lindy effect)

This shows that a Lindy effect can arise even when the object itself has constant hazard rate - the declining effective hazard comes from Bayesian updating that weights lower hazard rates more heavily as time passes[^1].

## 4. **Connection to Survival Analysis**

The mathematical foundation requires:
- **Broad Lindy Effect**: Any heavy-tailed distribution (declining hazard rate)
- **Narrow Lindy Effect (mean)**: Pareto distribution with α = 2
- **Narrow Lindy Effect (median)**: Pareto distribution with α = 1

The formulation in terms of median is more expressive, allowing Pareto distributions with any exponent α > 0 to qualify[^1].

## 5. **Key Mathematical Results**

The Lindy Effect emerges from several converging mathematical principles:

### Copernican Principle
Assuming you observe something at a random point in its lifetime leads to the median estimate that remaining lifetime equals past lifetime[^1].

### Laplace's Law of Succession
Similar mathematics appear in Laplace's analysis of runs of white balls from an urn with unknown composition, yielding a discrete power law with α = 1[^1].

### Power Law Invariance
The Pareto distribution is the unique distribution satisfying the exact Lindy property that expected (or median) future lifetime is proportional to past lifetime.

## Critical Insight

The Lindy effect can arise from epistemic uncertainty rather than physical robustness - "There is an evidential increase in robustness as time passes without failure, but no causal increase. The change is in the observer, not in the object being observed"[^1].

This mathematical framework shows the Lindy Effect isn't just an empirical observation but has deep connections to:
- Information theory (maximum entropy)
- Bayesian inference (scale-invariant priors)
- Survival analysis (hazard functions)
- The principle of indifference in probability

The mathematics is particularly elegant in showing how maximal ignorance (represented by the scale-invariant prior) naturally leads to the Lindy Effect after conditioning on observed survival.

---

## References

[^1]: Ord, Toby. "The Lindy Effect." arXiv preprint arXiv:2308.09045 (2023). Available at: https://arxiv.org/pdf/2308.09045 (Published: August 17, 2023)

### Additional Sources Consulted

- Eliazar, I. "Lindy's Law." Physica A: Statistical Mechanics and its Applications, 486, 797-805 (2017)
- Taleb, Nassim Nicholas. "Antifragile: Things that Gain from Disorder." Random House (2012)
- Gott, J. Richard, III. "Implications of the Copernican principle for our future prospects." Nature, 363, 315–319 (1993)
- Wikipedia. "Jeffreys prior." https://en.wikipedia.org/wiki/Jeffreys_prior (Accessed: 2025)
- Wikipedia. "Principle of maximum entropy." https://en.wikipedia.org/wiki/Principle_of_maximum_entropy (Accessed: 2025)