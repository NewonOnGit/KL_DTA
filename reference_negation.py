"""
reference_negation.py — the two self-actions are self-reference and self-negation.

  symmetric  {R,·}  = self-reference   R² = R + I   (defect held AS the identity)
  antisym    [R,·]  = self-negation    N² = -I      (N is the matrix i)

Where i²/N² leads, and why the identity only returns when the residual is squared
back to origin — and the synthesis: P² = P is the CANCELLATION of the two.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
show = lambda M: np.round(M, 6).tolist()

print("=" * 68)
print("  SELF-REFERENCE  =  R   (the symmetric self-action {R,·})")
print("=" * 68)
nu_R = R @ R - R
print(f"  R² = R + I            : {np.allclose(R@R, R + I2)}")
print(f"  ν(R) = R² − R = {show(nu_R)}  = I  : {np.allclose(nu_R, I2)}")
print("  self-reference holds its DEFECT AS THE IDENTITY. ν(R) = I, not 0.")
print("  the fixed point R(R)=R (idempotent) is the collapsed form; R²=R+I is")
print("  the primitive one — it keeps the surplus instead of killing it.")
print()

print("=" * 68)
print("  SELF-NEGATION  =  N   (the antisymmetric self-action [R,·]; N is i)")
print("=" * 68)
N2 = N @ N
N4 = N2 @ N2
print(f"  N² = -I               : {np.allclose(N2, -I2)}     (self-negation² = -I = i²)")
print(f"  N⁴ = (N²)² = (-I)² = I : {np.allclose(N4, I2)}     period 4 — the spin/return cycle")
print("  i²/N² leads to -I (the arrow), then squares back to +I. The identity")
print("  RETURNS as identity only when the residual (-I) is squared to origin.")
print()

print("=" * 68)
print("  SYNTHESIS — P² = P is the CANCELLATION of +I and −I")
print("=" * 68)
RN = R @ N + N @ R                 # {R,N}
P2 = P @ P
print(f"  P = R + N             : {np.allclose(P, R + N)}")
print(f"  {{R,N}} = RN + NR = N    : {np.allclose(RN, N)}")
print("  expand P² with P = R + N:")
print("     P² = R²  +  {R,N}  +  N²")
print("        = (R + I) + (N) + (−I)        ← +I from self-reference, −I from self-negation")
print("        =  R + N  =  P")
lhs = R @ R + RN + N @ N
print(f"  R² + {{R,N}} + N² = {show(lhs)}  = P : {np.allclose(lhs, P)}")
print(f"  the +I (surplus of self-reference) and −I (self-negation) ANNIHILATE.")
print(f"  P² = P : {np.allclose(P2, P)}   — the seed is idempotent BECAUSE the two")
print("  defects cancel back to the origin. ker(ν) is reachable only there.")
print()
print("  self-reference makes +I, self-negation makes −I, the fold cancels them:")
print("  the idempotent origin is the residual squared back to zero.")
