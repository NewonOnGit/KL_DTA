"""
symmetry_audit.py — is R symmetric or antisymmetric? depends on the involution.

  transpose  τ(X) = Xᵀ       — the naive one
  Cartan     θ(X) = −Xᵀ      — the framework's canonical involution (gives B_θ ≻ 0)

and there are two levels: the ELEMENT (R, N) and its SELF-ACTION ({R,·}, {N,·}).
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
tau = lambda X: X.T
theta = lambda X: -X.T


def parity(M, inv):
    if np.allclose(inv(M), M):   return "symmetric"
    if np.allclose(inv(M), -M):  return "antisymmetric"
    return "neither"


print("=" * 66)
print("  ELEMENT level — R and N under each involution")
print("=" * 66)
print(f"  {'':4} {'τ (transpose)':>16} {'θ (Cartan −Xᵀ)':>18}")
for name, M in [("R", R), ("N", N)]:
    print(f"  {name:4} {parity(M, tau):>16} {parity(M, theta):>18}")
print("  under the framework's θ:  R is ANTIsymmetric,  N is SYMMETRIC.")
print("  (under plain transpose it's the reverse — which is what the old labels used.)")
print()

print("=" * 66)
print("  OPERATOR level — the self-actions {R,·}, {N,·} (4×4 matrices)")
print("=" * 66)


def act(s):                      # {s,·} : X -> sX + Xs  as a 4×4 matrix
    return np.kron(I2, s) + np.kron(s.T, I2)


for name, s in [("{R,·}", R), ("{N,·}", N)]:
    T = act(s)
    p = "symmetric" if np.allclose(T.T, T) else "antisymmetric" if np.allclose(T.T, -T) else "neither"
    print(f"  {name:6} operator is {p}")
print("  the SELF-ACTION has the OPPOSITE parity of its element:")
print("    R (θ-antisymmetric)  ->  {R,·} (symmetric operator)")
print("    N (θ-symmetric)      ->  {N,·} (antisymmetric operator)")
print("  the self-action inverts parity.")
print()

print("=" * 66)
print("  the seed's self-action splits:  {P,·} = {R,·} + {N,·}")
print("=" * 66)
X = np.array([[1., 2.], [3., -1.]])
lhs = P @ X + X @ P
rhs = (R @ X + X @ R) + (N @ X + X @ N)
print(f"  {{P,·}} = {{R,·}} + {{N,·}}  ✓ {np.allclose(lhs, rhs)}")
print("  so the two self-actions are {R,·} and {N,·}, summing to the seed's.")
print()
print("  VERDICT: under the Cartan θ (the framework's involution), R is")
print("  ANTIsymmetric and N is SYMMETRIC — the old symmetric_R/antisymmetric_N")
print("  labels were transpose-based and backwards. The operators flip parity.")
