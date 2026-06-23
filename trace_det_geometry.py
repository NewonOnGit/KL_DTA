"""
trace_det_geometry.py — tr is perimeter, det is shape.

The base (tr, det) — the INDEX of every record — is geometry:
  tr  = λ₁ + λ₂   the PERIMETER (sum of axes; additive, 1-D boundary)
  det = λ₁·λ₂     the SHAPE / area (product of axes; multiplicative, 2-D content)
and the discriminant is the isoperimetric gap:
  disc = tr² − 4·det = (λ₁ − λ₂)²   the eccentricity; disc = 0 ⟺ round (equal axes).
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
J = np.array([[1., 0.], [0., -1.]])
h = J @ N

print("=" * 70)
print("  base (tr, det) = (perimeter, shape);  disc = tr²−4det = (λ₁−λ₂)²")
print("=" * 70)
print(f"  {'name':5} {'tr=perim':>9} {'det=shape':>10} {'disc':>6} {'(λ₁−λ₂)²':>9}  conic / regime")
for name, M in [("I", I2), ("R", R), ("N", N), ("h", h), ("P", P)]:
    tr, det = np.trace(M), np.linalg.det(M)
    disc = tr * tr - 4 * det
    ev = np.linalg.eigvals(M)
    gap2 = (ev[0] - ev[1]) ** 2
    if det > 1e-9:
        conic = "ellipse (closed)" if disc < -1e-9 else "round/wall" if abs(disc) < 1e-9 else "—"
    elif det < -1e-9:
        conic = "hyperbola (open)"
    else:
        conic = "degenerate (line)"
    print(f"  {name:5} {tr:9.2f} {det:10.2f} {disc:6.2f} {np.real(gap2):9.2f}  {conic}")
print()
print(f"  disc = (λ₁−λ₂)² verified for all  (the squared eigen-gap = eccentricity)")
print()

print("=" * 70)
print("  the wall disc = 0  is the round shape — equal axes")
print("=" * 70)
print("  disc > 0 : distinct real axes → stretched (hyperbolic, free/scattering)")
print("  disc = 0 : λ₁ = λ₂ → round, the most symmetric → the wall, where ? lives")
print("  disc < 0 : no real axes → pure rotation (elliptic, bound/oscillatory)")
print("  the isoperimetric reading: perimeter² vs 4·shape; disc=0 is the optimum.")
print()

print("=" * 70)
print("  physical:  s² − tr·s + det = 0   is the dispersion / RLC relation")
print("=" * 70)
print("  det = shape  =  stiffness / ω²   (the shape of the potential well, the mass)")
print("  tr  = perimeter = damping        (the boundary loss, the dissipation)")
print("  disc = damping² − 4·stiffness    = the damping regime (over/critical/under)")
print("  N: tr=0, det=1 — zero perimeter, unit shape: the pure circle (the observer)")
print("  R: tr=1, det=−1 — perimeter 1, reversed area: the boost (production)")
print("  P: tr=1, det=0 — perimeter 1, zero area: the degenerate rank-1 seed")
