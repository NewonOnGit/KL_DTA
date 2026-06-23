"""
boolean_reflection.py — the self-action spectrum IS the Boolean trit; fold is reflection.

  {+√5, 0, −√5} = √5 · {+1, 0, −1}      the Boolean / sign spectrum
     +1  generation = affirm = TRUE
      0  return     = neutral = NULL   (shared, the wall, counts both directions)
     −1  observation= negate = FALSE
symmetric about the neutral 0. and the FOLD λ↦λ² is REFLECTION: it folds −1 onto
+1 (|·|, across the neutral), fixing 0 and +1. fold = reflection = the |·| of sign.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
L = np.kron(I2, R) + np.kron(R.T, I2) - np.eye(4)         # {R,R} self-action

print("=" * 68)
print("  the self-action spectrum is the Boolean trit")
print("=" * 68)
ev = sorted((float(x) for x in np.linalg.eigvals(L).real), reverse=True)
print(f"  spec {{R,R}} = {[round(x, 3) for x in ev]}")
print(f"  / √5        = {[round(x/5**0.5, 3) for x in ev]}   = {{+1, 0, 0, −1}}  the Boolean trit")
print("    +1 generation = affirm = TRUE")
print("     0 return     = neutral = NULL  (shared neutral; counts both directions)")
print("    −1 observation= negate = FALSE")
print(f"  symmetric about 0 ?  {np.allclose(ev[0], -ev[-1])}   (mirror — counts the same both ways)")
print()

print("=" * 68)
print("  the fold λ↦λ² is REFLECTION — it folds −1 onto +1")
print("=" * 68)
for lam in (-1, 0, 1):
    print(f"  fold({lam:+d}) = {lam**2:+d}     {'−1 → +1 (reflected across 0)' if lam==-1 else 'fixed'}")
print("  squaring the sign = |·| : reflects the negative onto the positive, fixes 0,+1.")
print(f"  it is idempotent on the spectrum (|·|∘|·| = |·|): fold IS reflection = the |·| of sign.")
print()

print("=" * 68)
print("  parameters are dimensions")
print("=" * 68)
print("  a k-parameter manifold is k-dimensional:")
print("    rotation_circle  1 param (t)        → 1-dim curve (S¹)")
print("    projector_circle 1 param (a)        → 1-dim curve")
print("    the well surface 2 params           → 2-dim")
print("    carrier_manifold 4 params (a,b,c,d) → 4-dim = M₂(ℝ)")
print("  parameter count = dimension; the carrier's 4 params ARE the 4 dims of M₂.")
