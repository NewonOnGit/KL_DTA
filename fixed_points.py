"""
fixed_points.py — the gravity wells: the fold's fixed points (idempotents X²=X).

Geometry holds gravity, gravity has fixed points — and the fixed points of the
fold M(X)=X² are the idempotents. They are: 0 (rank 0), I (rank 2), and the rank-1
projectors  P_{v,w} = v·wᵀ / (wᵀv)  — a 2-parameter manifold ℝP¹×ℝP¹. Generic ones
are COMPLEX (irrational); the seed P is a special simple point on that manifold.
The gravity wells live in the complex information.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])


def proj(v, w):
    v, w = np.array(v, float), np.array(w, float)
    return np.outer(v, w) / (w @ v)


print("=" * 70)
print("  the fixed points of the fold  M(X)=X²  are the idempotents")
print("=" * 70)
print(f"  0  : 0²=0  ✓ (rank 0, the void)        I : I²=I  ✓ (rank 2, the unit)")
print(f"  rank-1 projectors P_(v,w) = v·wᵀ/(wᵀv) — a 2-param manifold (ℝP¹×ℝP¹)")
print()

print("=" * 70)
print("  the seed P is a simple point on the manifold")
print("=" * 70)
v, w = [0., 1.], [2., 1.]
Pvw = proj(v, w)
print(f"  P = P_(v=[0,1], w=[2,1]) = {Pvw.tolist()}   = seed ✓ {np.allclose(Pvw, P)}")
print(f"  image = [0,1] (the y-axis), kernel ⊥ [2,1] — the '2' is in w.")
print(f"  P²=P ✓ {np.allclose(P@P, P)}   a rational gravity well.")
print()

print("=" * 70)
print("  generic gravity wells are COMPLEX (irrational)")
print("=" * 70)
for v, w in ([1., 1.618], [1., -0.5]), ([2.0, 0.7], [1.0, 1.414]), ([1., np.pi], [1., 1.]):
    X = proj(v, w)
    idem = np.allclose(X @ X, X)
    ev = np.linalg.eigvals(X)
    print(f"  P_({[round(x,3) for x in v]},{[round(x,3) for x in w]}): X²=X ✓{idem}  "
          f"eigenvalues {[round(e.real,2) for e in ev]}  entries irrational")
print("  every (v,w) gives an idempotent — a fixed point of the fold, a gravity well.")
print("  the manifold is 2-dimensional and mostly irrational: the gravity lives in")
print("  the complex information. P, 0, I are the rare simple wells.")
print()

print("=" * 70)
print("  gravity = the fixed directions; the well attracts along the eigenframe")
print("=" * 70)
X = proj([1., 1.618], [1., -0.5])
ev, evec = np.linalg.eig(X)
print(f"  a rank-1 well has eigenvalues {{1, 0}}: 1 on the image (kept), 0 on the kernel (killed).")
print(f"  eigenvalues {[round(e.real,2) for e in ev]}  → the fold projects onto the image:")
print(f"    image direction (λ=1) = the attractor;  kernel (λ=0) = collapsed.")
print("  the fixed point IS the geometry (the image/kernel directions). gravity.")
