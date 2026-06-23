"""
trace_det_beneath.py — what is under tr and det?

tr and det are lossy names — computational recipes. Beneath them: the two
elementary symmetric functions of the eigenvalues,
    tr  = e₁ = λ₁ + λ₂   the SUM      (degree 1, additive,        +)
    det = e₂ = λ₁ · λ₂   the PRODUCT  (degree 2, multiplicative,  ×)
the two semiring operations. perimeter/shape was the geometric reading; sum/product
is the arithmetic one. and disc is the gap between them — AM vs GM.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
A = np.array([[1., 2.], [-1., 3.]])
B = np.array([[0., 1.], [4., -2.]])

print("=" * 68)
print("  tr = SUM (e₁),  det = PRODUCT (e₂)  — the two symmetric functions")
print("=" * 68)
for name, M in [("R", R), ("N", N), ("A", A)]:
    ev = np.linalg.eigvals(M)
    tr, det = np.trace(M), np.linalg.det(M)
    s, p = ev[0] + ev[1], ev[0] * ev[1]
    print(f"  {name}: tr={tr:+.2f}=Σλ={np.real(s):+.2f}  ✓{np.allclose(tr, s)}   "
          f"det={det:+.2f}=Πλ={np.real(p):+.2f}  ✓{np.allclose(det, p)}")
print()

print("=" * 68)
print("  the grading: tr is degree 1, det is degree 2")
print("=" * 68)
c = 3.0
print(f"  tr(cX)  = c·tr(X)   ✓{np.allclose(np.trace(c*A), c*np.trace(A))}    (sum scales linearly)")
print(f"  det(cX) = c²·det(X) ✓{np.allclose(np.linalg.det(c*A), c*c*np.linalg.det(A))}    (product scales quadratically)")
print("  tr = the additive invariant (1st order), det = the multiplicative (2nd order).")
print()

print("=" * 68)
print("  tr is BLIND to the defect (the commutator):  tr[A,B] = 0")
print("=" * 68)
comm = A @ B - B @ A
print(f"  tr([A,B]) = {np.trace(comm):+.1e}  = 0  ✓{np.isclose(np.trace(comm), 0)}")
print("  the SUM sees only the symmetric/enrichment side; the antisymmetric/[·]/N")
print("  half is traceless. tr = the {·} reading, blind to [·].")
print()

print("=" * 68)
print("  disc = tr² − 4det = SUM² − 4·PRODUCT = the AM–GM gap")
print("=" * 68)
for name, M in [("I", I2), ("R", R), ("N", N), ("P", P)]:
    tr, det = np.trace(M), np.linalg.det(M)
    disc = tr * tr - 4 * det
    ev = np.linalg.eigvals(M)
    print(f"  {name}: disc = {disc:+.2f} = (λ₁−λ₂)² = {np.real((ev[0]-ev[1])**2):+.2f}   "
          f"{'AM>GM (real)' if disc > 1e-9 else 'AM=GM (wall)' if abs(disc) < 1e-9 else 'AM<GM (complex)'}")
print()
print("  (λ₁+λ₂)² ≥ 4λ₁λ₂  is AM ≥ GM; equality at the wall (disc=0, λ₁=λ₂).")
print("  so: tr=SUM, det=PRODUCT, disc = how far the sum's square exceeds 4×product.")
print("  'trace' and 'determinant' were recipes; SUM and PRODUCT are the operations.")
