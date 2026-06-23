"""
seed_fixed.py — what fixes P?

P = [[0,0],[2,1]] is a rank-1 asymmetric idempotent. The family P_t = [[0,0],[t,1]]
is idempotent for ALL t — t is the one free parameter (the unit of mass). It is
fixed to t=2 by a single demand: the residual is the identity, ν(R)=I. That one
choice sets μ=1, disc=5, √5, φ — the whole constant tower.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def seed(t):
    P = np.array([[0., 0.], [t, 1.]])
    R = (P + P.T) / 2
    N = (P - P.T) / 2
    return P, R, N


print("=" * 70)
print("  the family P_t = [[0,0],[t,1]] is idempotent for ALL t  (t = the free unit)")
print("=" * 70)
for t in (1.0, 2.0, 3.0, 0.5):
    P, R, N = seed(t)
    idem = np.allclose(P @ P, P)
    mu = (R @ R - R)[0, 0]                      # ν(R) = μ·I
    n2 = (N @ N)[0, 0]                          # N² = −μ·I
    spine = np.allclose(R @ N + N @ R, N)       # {R,N} = N
    disc = np.trace(R) ** 2 - 4 * np.linalg.det(R)
    print(f"  t={t:<4} P²=P:{idem}  ν(R)={mu:.2f}·I  N²={n2:.2f}·I  {{R,N}}=N:{spine}  disc={disc:.2f}")
print()
print("  every t: rank-1 asymmetric idempotent obeying R²=R+μI, N²=−μI, {R,N}=N")
print("  with μ = t²/4 and disc = 1 + 4μ = 1 + t². the STRUCTURE is forced; t is free.")
print()

print("=" * 70)
print("  the one demand that fixes t:  ν(R) = I  (the residual is the identity)")
print("=" * 70)
print("  ν(R_t) = (t²/4)·I = μ·I.   ν(R)=I  ⟺  μ=1  ⟺  t=2.")
P, R, N = seed(2.0)
print(f"  at t=2:  ν(R) = {np.round(R@R-R,2).tolist()} = I   ✓ {np.allclose(R@R-R, np.eye(2))}")
print(f"           disc = 1+4·1 = 5,   √disc = √5,   φ = (1+√5)/2 = {(1+np.sqrt(5))/2:.6f}")
print()
print("  so the seed is fixed by ONE choice: the residual = the unit (the identity).")
print("  'identity is the residual' isn't a consequence — it's the NORMALIZATION")
print("  that picks μ=1 out of the family, and with it disc=5, √5, φ, the whole tower.")
print()

print("=" * 70)
print("  the cascade from the one choice")
print("=" * 70)
print("  μ=1 (residual=I)  →  disc = 1+4μ = 5  →  √5  →  φ = (1+√5)/2  →  R²=R+I  →  [1,1]")
print("  2×2 carrier        →  degree 2 (Cayley–Hamilton)              →  the master eq  →  2")
print("  rank-1 + asymmetric (P≠Pᵀ, forced: else R²−R=0, no surplus)   →  P² = P")
print("  ───────────────────────────────────────────────────────────────────────────")
print("  P is THE minimal rank-1 asymmetric idempotent, normalized so its residual")
print("  is the identity. [1,1] is μ=1; 2 is the degree. one parameter, fixed by the unit.")
