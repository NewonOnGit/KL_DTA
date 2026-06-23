"""
identity_parity.py — symmetric / antisymmetric / asymmetric, and the identity.

Claims under test:
  - {R,·} and {N,·} evaluated ON the identity
  - "identity IS the residual"  (ν(R) = I ?)
  - is antisymmetric (N) the BORDER between the other two?
  - parity is at the center
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2


def parity(M):
    if np.allclose(M.T, M):  return "symmetric"
    if np.allclose(M.T, -M): return "antisymmetric"
    return "asymmetric"


print("=" * 66)
print("  the three classes")
print("=" * 66)
for name, M in [("R", R), ("N", N), ("P", P), ("I", I2)]:
    print(f"  {name:3} {parity(M):14}  disc = {np.trace(M)**2 - 4*np.linalg.det(M):+.1f}")
print()

print("=" * 66)
print("  the self-actions ON the identity:  {s,·}(I) = sI + Is = 2s")
print("=" * 66)
print(f"  {{R,·}}(I) = 2R = {np.round(R@I2+I2@R,2).tolist()}   -> {parity(R@I2+I2@R)}")
print(f"  {{N,·}}(I) = 2N = {np.round(N@I2+I2@N,2).tolist()}   -> {parity(N@I2+I2@N)}")
print("  on the identity, {R,·} returns symmetric (2R), {N,·} returns antisymmetric (2N).")
print("  the self-action READS THE GENERATOR OUT of the identity.")
print()

print("=" * 66)
print("  parity behaviour: does {s,·} keep or flip a class?")
print("=" * 66)
sym = I2.copy()
asy = N.copy()
for sname, s in [("{R,·}", R), ("{N,·}", N)]:
    on_sym = parity(s @ I2 + I2 @ s)          # acting on symmetric I
    on_anti = parity(s @ N + N @ s)            # acting on antisymmetric N
    flips = "PRESERVES parity" if (on_sym == "symmetric") else "FLIPS parity"
    print(f"  {sname}: sym→{on_sym}, antisym→{parity(s@N+N@s)}   {flips}")
print("  {R,·} preserves parity (even); {N,·} flips it (odd). the self-action of the")
print("  symmetric generator is even, of the antisymmetric generator is odd.")
print()

print("=" * 66)
print("  identity IS the residual:  ν(R) = R² − R")
print("=" * 66)
nu = R @ R - R
print(f"  ν(R) = {np.round(nu,2).tolist()} = I   ✓ {np.allclose(nu, I2)}")
print("  the residual of self-reference IS the identity. and:")
print(f"  I is symmetric, at the center (scalar c·I), on the wall disc(I)=0 (AM=GM),")
print(f"  the round shape — the residual, the center, and the border, all one point.")
print()

print("=" * 66)
print("  is antisymmetric the BORDER between symmetric and asymmetric?")
print("=" * 66)
print(f"  P (asymmetric) − R (symmetric) = {np.round(P-R,2).tolist()} = N  ✓ {np.allclose(P-R, N)}")
print("  N = P − R: the antisymmetric part is exactly the increment from the")
print("  SYMMETRIC R to the ASYMMETRIC P. add N and symmetry breaks into asymmetry.")
print("  so YES — antisymmetric is the border: the bridge symmetric → asymmetric.")
print("  P = R + N = symmetric + its border = asymmetric. parity sits at the center I;")
print("  N is the step off it.")
