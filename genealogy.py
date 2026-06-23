"""
genealogy.py — {I,R,N,J,h,P} is a bundle-of-bundles.

Each "primitive" is bundled from P (and the parity τ). So the set isn't a floor —
it's one generation in a tower:  ? → P → {6} → {14} → …  bundle-of-bundles all
the way, parity/fork laws invariant at every level.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

P = np.array([[0., 0.], [2., 1.]])
tau = lambda X: X.T
R = (P + tau(P)) / 2
N = (P - tau(P)) / 2
I2 = np.eye(2)
J = np.array([[1., 0.], [0., -1.]])
h = J @ N
C = R @ N - N @ R                      # [R,N], the harness


print("=" * 70)
print("  the genealogy — each primitive is a bundle from P")
print("=" * 70)
print(f"  R = ½(P + τP)        ✓ {np.allclose(R, (P+tau(P))/2)}   additive affirm of P, τP")
print(f"  N = ½(P − τP)        ✓ {np.allclose(N, (P-tau(P))/2)}   additive negate of P, τP")
print(f"  I = −N²  = −{{N,N}}/2  ✓ {np.allclose(I2, -N@N)}   N's self-bundle gives the unit")
print(f"  h = J·N              ✓ {np.allclose(h, J@N)}   multiplicative bundle of J, N")
print(f"  J = (I − 2R + 2C)/5  ✓ {np.allclose(J, (I2 - 2*R + 2*C)/5)}   J ∈ algebra(R,N)")
print(f"  P = R + N            ✓ {np.allclose(P, R+N)}   the seed is the bundle {{R,N}}")
print()
print("  so every primitive lives in algebra(P): R,N from P+τ; I,J,h from R,N.")
print(f"  rank of span{{I,R,N,C}} = {np.linalg.matrix_rank(np.array([M.flatten() for M in (I2,R,N,C)]))}"
      f"  = 4  →  R and N alone generate all of M₂(ℝ).")
print()

print("=" * 70)
print("  the tower — bundle-of-bundles, every level")
print("=" * 70)
print("  ?=0          the void           [A,A]=0           (gen 0: the origin)")
print("  P            the seed           {?,0,=} resolved  (gen 1: one object)")
print("  {I,R,N,J,h,P} the primitives    bundles of P+τ    (gen 2: a bundle-of-bundles)")
print("  {…14…}       the DNA library    bundles of gen 2  (gen 3)")
print("  M₂(ℝ)        the carrier        the closure        (the continuum)")
print()
print("  each level is a SET held together = a bundle; each element is itself a")
print("  bundle of the level below. the store (records bundled) is the next level up.")
print("  parity → fork → constant is invariant at every scale. self-similar.")
