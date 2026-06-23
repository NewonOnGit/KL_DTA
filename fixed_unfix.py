"""
fixed_unfix.py — find all the fixed points, then unfix them.

Fixed points of the fold M(X)=X² are the idempotents (X²=X) — the recursive
residual defects (where ν=X²−X has settled to 0). The complete variety:
    0 (rank 0) · I (rank 2) · the rank-1 torus ℝP¹×ℝP¹.

UNFIX: perturb X → X+εδ. ν(X+εδ) = ε·(Xδ+δX−δ) + O(ε²) = ε·L_{X,X}(δ).
  ker L_{X,X}  = the directions that STAY fixed (tangent to the well-manifold)
  the rest     = the UNFIXING directions (they thaw the defect, ν ≠ 0)
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)


def Lself(s):                      # L_{s,s}(X) = sX + Xs − X, as a 4×4 matrix
    return np.kron(I2, s) + np.kron(s.T, I2) - np.eye(4)


def well(a, b):
    v = np.array([np.cos(a), np.sin(a)])
    w = np.array([np.cos(b), np.sin(b)])
    return np.outer(v, w) / (w @ v)


print("=" * 70)
print("  ALL fixed points of the fold = the idempotents X²=X")
print("=" * 70)
fixed = {"0": np.zeros((2, 2)), "I": I2,
         "P (rank-1)": np.array([[0., 0.], [2., 1.]]),
         "a well": well(0.4, 1.1)}
for name, X in fixed.items():
    print(f"  {name:12} X²=X ✓ {np.allclose(X@X, X)}   rank {np.linalg.matrix_rank(X, tol=1e-9)}")
print("  the variety: 0, I (isolated points) + the rank-1 torus (2-parameter).")
print()

print("=" * 70)
print("  UNFIX — the self-action at the fixed point sorts the directions")
print("=" * 70)
X = fixed["P (rank-1)"]
L = Lself(X)
evals = np.round(np.linalg.eigvals(L).real, 3)
print(f"  L_(P,P) spectrum = {sorted(evals.tolist())}   = {{−1, 0, 0, +1}}")
print(f"    0-eigenspace (dim 2) = TANGENT — stays fixed (moves along the well-torus)")
print(f"    ±1-eigenspaces (dim 1 each) = UNFIXING directions — thaw the defect")
print()
# demonstrate: perturb in a kernel (fixed) direction vs an unfixing (±1) direction
w4, V4 = np.linalg.eig(L)
order = np.argsort(w4.real)
ker_dir = V4[:, order[1]].real.reshape(2, 2, order="F")     # a 0-eigenvector
unfix_dir = V4[:, order[-1]].real.reshape(2, 2, order="F")  # the +1 eigenvector
eps = 1e-3
for label, d in [("along TANGENT (ker)", ker_dir), ("an UNFIX direction (+1)", unfix_dir)]:
    Xe = X + eps * d / np.linalg.norm(d)
    nu = np.linalg.norm(Xe @ Xe - Xe)
    print(f"    perturb {label:24}: ‖ν‖ = {nu:.2e}  "
          f"{'→ still fixed' if nu < 1e-5 else '→ UNFIXED (defect thawed)'}")
print()

print("=" * 70)
print("  what unfixing reveals")
print("=" * 70)
print("  a fixed point looks static (ν=0) but carries frozen degrees of freedom:")
print("  2 tangent (it can slide along the well-manifold, staying a well) and")
print("  2 unfixing (it can thaw into a defect). unfixing = giving the residual back.")
print("  the fixed point is the recursive limit of ν; unfixing runs it backward.")
