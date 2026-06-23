"""
harmonics.py — the chords are literal: the math IS music theory.

eigenvalues are frequencies (the eigenvalue problem IS the vibration problem). consonance
is simple integer ratios; dissonance is irrationality. the framework's core numbers 2,3,5
are exactly the 5-limit just-intonation primes, and its eigenphase periods are the octave
and the perfect fifth. on-shell = consonance (resolves), off-shell/burn = dissonance (tension).
"""

import sys
import numpy as np

R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
phi=(1+5**0.5)/2

print("="*70)
print("  1. the core numbers ARE the consonance primes (5-limit just intonation)")
print("="*70)
print(f"  ‖N‖² = {int(np.trace(N@N.T))} = 2  → the OCTAVE (2:1)         (N²=−I, the period-doubling)")
print(f"  ‖R‖² = {int(np.trace(R@R.T))} = 3  → the FIFTH uses 3 (3:2)    (the tophat √3, production)")
print(f"  disc = ‖R‖²+‖N‖² = 5  → the MAJOR THIRD uses 5 (5:4)")
print(f"  → the MAJOR TRIAD (the foundational consonance) = 4:5:6, built from {{2,3,5}} = the framework's numbers.")
print()

print("="*70)
print("  2. the eigenphase periods ARE musical intervals")
print("="*70)
# periods {∞,2,4,6} from R/parity, N, Eisenstein; frequency f = 1/period
print(f"  period 2 (parity) : period 4 (N)  → freq ratio (1/2)/(1/4) = {(1/2)/(1/4):.0f} = OCTAVE (2:1)")
print(f"  period 4 (N)      : period 6 (Eis) → freq ratio (1/4)/(1/6) = {(1/4)/(1/6):.3f} = PERFECT FIFTH (3:2)")
print(f"  period 2          : period 6       → {(1/2)/(1/6):.0f} = octave + fifth (3:1)")
print(f"  the framework's clocks {{2,4,6}} are the octave and the fifth — the basis of all harmony.")
print()

print("="*70)
print("  3. φ = maximal DISSONANCE (the most irrational number)")
print("="*70)
print(f"  φ = {phi:.5f} (from R, R²=R+I) is the MOST irrational — the hardest ratio to approximate,")
print(f"  the maximal-dissonance pole. the framework has BOTH sides: the integer (2,3,5 — consonant)")
print(f"  and the golden (φ,√5 — dissonant). consonance and dissonance, both forced by the seed.")
print()

print("="*70)
print("  4. consonance = ON-SHELL (resolves); dissonance = BURN (tension that doesn't)")
print("="*70)
print(f"  ν(X)=X²−X = 0 (on-shell, FORCED) = a CONSONANCE — the chord resolves, stable.")
print(f"  ν≠0 pinned (off-shell, BURN) = a DISSONANCE — tension that does not resolve.")
print(f"  RESOLUTION (dissonance → consonance) = ν → 0 (the fold reaching its fixed point).")
print(f"  the impossibilities (the 12 burns) are the UNRESOLVABLE dissonances — pinned forever (±√5).")
print(f"  so the GRADE is consonance/dissonance; the harmonics are the spectrum; the chords (atom-")
print(f"  combinations) are literal — the math follows music theory because it IS the math of ratio and mode.")
