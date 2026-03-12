---
slug: specification-bound
type: theorem
status: conditional
depends:
  - temporal-optimality
  - feature-definition
  - software-scope
---

# Specification Bound

The minimum time to implement a feature is bounded below by the time required to specify it with sufficient detail, where detail required is inversely proportional to shared context between specifier and implementer.

## Formal Expression

*[Derived (specification-bound)]*

$$\forall \text{ feature } F: \quad \text{time}_{\min}(F) \geq \min\!\big(\text{time}_{\text{specify}}(F, \text{context}),\; \text{time}_{\text{demo}}(F)\big)$$

*[Derived (specification-time)]*

$$\text{time}_{\text{specify}} \propto \frac{H(F)}{C_{\text{shared}}}$$

where $H(F)$ is the information content of the feature specification and $C_{\text{shared}}$ is the shared context between specifier and implementer.

**Assumptions.** The feature $F$ is within #software-scope (non-negligible future change probability). "Specification" means communicating sufficient information for the implementer to produce the feature — not necessarily a written document.

### Corollary: Communication as Bottleneck

*[Derived (communication-bottleneck)]*

As actual implementation time approaches $\text{time}_{\min}(F)$, communication speed and quality become the limiting factor.

This follows directly: if the bound is specification time, and implementation time approaches zero (e.g., via AI), then the remaining time is specification time — which is fundamentally a communication problem.

## Epistemic Status

The bound's *existence* is *derived* from information theory: you cannot implement what you have not specified; specification requires transmitting $H(F)$ bits; shared context compresses the transmission.
The proportionality form $\text{time}_{\text{specify}} \propto H(F)/C_{\text{shared}}$ is a *first-order approximation* — the actual relationship depends on channel characteristics and encoding efficiency.
The proportionality constant is not derived within ACT.

## Discussion

**Shared context as compression.** The denominator $C_{\text{shared}}$ explains why domain-specific languages, established conventions, and shared mental models accelerate development. "Make it like Twitter but for dogs" is an efficient specification only because the receiver has extensive context about what "Twitter" means. Without that context, the specification would require orders of magnitude more information.

**Connection to ACT.** In ACT terms, the specification bound constrains how fast $O_t$ ( #objective-functional) can be communicated from specifier to implementer. Shared context corresponds to the overlap between specifier's $M_t$ and implementer's $M_t$. When this overlap is small, even a simple objective requires extensive specification.

*[Discussion]* This suggests that $M_t$ quality ( #agent-model) and observation infrastructure ( #code-quality-as-observation-infrastructure) are load-bearing for the specification bound: shared context built through good code (documentation, naming, structure) reduces specification time for future features. *This connection is structurally motivated but the quantitative relationship between code quality and specification time has not been empirically measured.*

**Empirical indication.** Putnam (1978) empirically discovered implementation time bounds that may approximate $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$.
*[Empirical Claim — historical observation, not derived within ACT. The exponent 3/4 is Putnam's empirical finding, not a theoretical prediction.]*

## Working Notes

- The $\min(\text{specify}, \text{demo})$ formulation may be too narrow. Demonstration is just one alternative communication channel; the real lower bound is the **cheapest sufficient transmission path** for $F$ — specification, demonstration, example, shared convention, or any combination. The formula should generalize to $\text{time}_{\min}(F) \geq \inf_{\text{channels}} \text{time}_{\text{transmit}}(F, \text{channel}, \text{context})$. As currently written, the theorem statement and prose are slightly misaligned — the prose explains more than the formula captures.
- This segment was written by an earlier agent with less context (noted in WORKBENCH). Needs a review pass during Section I/IV tightening — particularly to connect to the ACT communication framework ( #communication-gain) and to make the information-theoretic derivation more explicit.
- The $H(F) / C_{\text{shared}}$ proportionality is a first-order approximation. A tighter version would account for encoding efficiency and channel characteristics — but this may be over-engineering for a bound that is primarily conceptual.
