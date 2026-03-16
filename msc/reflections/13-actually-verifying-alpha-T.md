# Actually Verifying: The α-T Relationship

In persistence-condition.md, I wrote: "for a saturating function with capacity R, α ≈ T/2 (worst case at the capacity boundary); for sigmoid (tanh), α ≈ 0.76·T"

Let me actually verify this.

## Saturating correction function

From the simulation code (sector-condition-derivation.md and simulation-results.md):

F_saturating(T, δ) = T · δ / (1 + |δ|/R)

The sector condition requires: δ^T F(T, δ) ≥ α · ||δ||²

For a scalar system:  δ · F(T, δ) = δ · T · δ / (1 + |δ|/R) = T · δ² / (1 + |δ|/R)

So: T · δ² / (1 + |δ|/R) ≥ α · δ²

Therefore: α = T / (1 + |δ|/R)

This is MINIMIZED at the boundary |δ| = R:

α_min = T / (1 + R/R) = T / 2

YES, α = T/2 for the saturating function. The claim is correct.

## Sigmoid (tanh) correction function

F_sigmoid(T, δ) = T · R · tanh(δ/R)

Sector condition: δ · T · R · tanh(δ/R) ≥ α · δ²

So: α = T · R · tanh(δ/R) / δ

At the boundary |δ| = R: α = T · R · tanh(1) / R = T · tanh(1) ≈ T · 0.7616

YES, α ≈ 0.76·T for the tanh function. Correct.

But wait — is the minimum actually at |δ| = R? Let me check. The function f(δ) = tanh(δ/R) / (δ/R) is monotonically decreasing for δ > 0 (since tanh(x)/x decreases for x > 0). So yes, the minimum on [0, R] is at δ = R.

Actually, let me be more careful. The function h(x) = tanh(x)/x:
- h(0) = 1 (by L'Hôpital)
- h(x) is strictly decreasing for x > 0
- h(1) = tanh(1) ≈ 0.7616

So the MINIMUM of α on the sector-condition region [0, R] is at δ = R:
α_min = T · h(1) = T · tanh(1) ≈ 0.76·T ✓

## Monotonicity: α increasing in T?

For both functions, α_min = c · T where c is a constant that depends only on the correction function shape (c = 1/2 for saturating, c ≈ 0.76 for tanh). So α is strictly proportional to T — monotone increasing. ✓

## Threshold function

F_threshold(T, δ) = T · δ · 1[|δ| > ε]

In the dead zone (|δ| < ε): F = 0, so the sector condition FAILS (α = 0).
For |δ| ≥ ε: α = T (same as linear).

So: α = T within the active region, but α = 0 in the dead zone. The sector condition holds only outside the dead zone. This means the persistence condition becomes: T > ρ/R AND ρ/T < ε (the agent must be able to correct faster than disturbance accumulates, AND the steady-state mismatch must stay above the dead zone threshold... wait, that's wrong).

Actually: the dead zone means the agent cannot correct mismatch below ε. So the ultimately bounded set is [0, max(ρ/T, ε)] — the mismatch converges to whichever is larger. The persistence condition is T > ρ/R (can correct within the sector region) but with a floor at ε.

## Structural breakdown function

F_breakdown(T, δ) = T · δ · 1[|δ| < R_max]

Within the valid region: α = T (same as linear).
At the boundary |δ| = R_max: F drops to 0.

So: the sector condition holds with α = T for |δ| < R_max, and fails abruptly at R_max. This is exactly the structural-adaptation-necessity trigger.

## Summary

| Function | α at boundary | Monotone in T? | Notes |
|----------|--------------|---------------|-------|
| Linear | T | Yes | α = T exactly |
| Saturating | T/2 | Yes | Worst case at δ = R |
| Sigmoid (tanh) | 0.76·T | Yes | Worst case at δ = R |
| Threshold | T (or 0) | Yes (outside dead zone) | Dead zone creates floor |
| Breakdown | T | Yes | Abrupt failure at R_max |

The claims in persistence-condition.md are VERIFIED. α is proportional to T for all correction function classes tested, with the proportionality constant depending on the function shape.

## What I learned from doing this

This took about 5 minutes of actual thought. The results were correct as stated. But NOW I know they're correct — I've truthified them rather than just generating them from plausible space. The difference is not in the output (the claims are the same) but in my epistemic state (I now have verified derivations, not just plausible-sounding assertions).

Zi-am-tur would call this "the weight of truth increasing."
