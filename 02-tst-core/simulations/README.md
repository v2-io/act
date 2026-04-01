# Simulation Validity Guide

## Valid Simulations (with proper stochastic termination)

These simulations use the mathematically correct P(terminate at k | survived to k) = 1/(k+1) formula:

### Core Valid Simulations

1. **lindy_corrected.py** ✅
   - Correct 1/(k+1) termination
   - All projects start at k=1 
   - Shows 50% survive past k=1 (matches theory exactly)
   - Demonstrates E[additional] ≈ 2k with survivor bias

2. **lindy_stochastic.py** ✅
   - Correct 1/(k+1) termination
   - Projects start at random k (1-20)
   - Comprehensive stochastic analysis

3. **lindy_gaussian_start.py** ✅
   - Pure 1/k termination (also valid but different)
   - Gaussian starting distribution (μ=50, σ=15)
   - Models studying established projects

4. **stochastic_regime_breakout.py** ✅
   - Correct 1/(k+1) termination
   - Projects start at k~50 (established)
   - Shows regime breakout is rare but possible

5. **three_regimes_stochastic.py** ✅
   - Uses 1/(k+5) termination (less aggressive)
   - Compares three starting regimes
   - 20,000 iterations per scenario

6. **lindy_math_verification.py** ✅
   - Proves why 1/(k+1) is correct
   - Shows 1/k would cause 100% immediate termination
   - Mathematical verification tool

## Invalid Simulations (moved to invalid_no_termination/)

These simulations lack proper stochastic termination and are mathematically invalid:

- **lindy_simple.py** ❌ - No termination, runs forever
- **lindy_tooling.py** ❌ - No termination
- **regime_transitions.py** ❌ - No termination
- **three_regimes.py** ❌ - No termination

## Key Mathematical Insight

The correct termination probability MUST be:
- **P(terminate at k | survived to k) = 1/(k+1)**

NOT 1/k because:
- 1/k would mean P(terminate at k=1) = 1/1 = 100% immediate death
- 1/(k+1) gives P(terminate at k=1) = 1/2 = 50% survival (matches Lindy theory)

## Visualization Files

All PNG files are outputs from the valid simulations:
- `lindy_corrected_analysis.png` - From corrected simulation
- `stochastic_breakout.png` - Regime breakout attempts
- `three_regimes_stochastic.png` - Three regime comparison
- `lindy_gaussian_analysis.png` - Gaussian starting distribution
- `lindy_math_verification.png` - Mathematical proof

## Usage

Always use the valid simulations for analysis. The invalid ones are kept only for historical reference and to understand why proper termination is critical.