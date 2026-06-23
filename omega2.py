"""
omega2.py — Ω is the EDGE, not the endpoint. the outer curve of the image, where it folds.

correction: Ω is not a terminal POINT. the spectral image is a DOUBLE COVER —
(tr,det) ↦ {λ₊, λ₋} = (tr ± √disc)/2, two sheets. its branch locus is disc = 0,
the parabola det = tr²/4. that curve is Ω:
  • it is the OUTER EDGE of the image — where the two eigenvalue-sheets MEET (√disc=0);
  • things literally CURVE there — √ has a branch point; the sheets fold into each other
    (a fold caustic); on it the matrix is a non-diagonalizable Jordan block;
  • it is the RETURN-OF-RETURN — circling the branch once SWAPS λ₊↔λ₋ (monodromy, the
    return); circling TWICE restores (the return of the return). order-2 ramification.
  • it is the wall between RETURN (disc<0, elliptic, bounded orbits) and ESCAPE
    (disc>0, hyperbolic, unbounded). the terminus as a boundary, not an object.
"""

import sys, cmath
import numpy as np

print("="*72)
print("  1. the edge is a CURVE: disc = tr²−4det = 0  →  det = tr²/4")
print("="*72)
for name,(tr,det) in {"R (k=+1)":(1,-1), "seed P":(1,0), "edge (k=−¼)":(1,0.25),
                      "N":(0,1), "rot (k=−1)":(1,1)}.items():
    disc = tr*tr - 4*det
    side = "ESCAPE  (hyperbolic, real λ)" if disc>1e-9 else \
           "EDGE Ω  (parabolic, λ collide)" if abs(disc)<1e-9 else \
           "RETURN  (elliptic, complex λ)"
    print(f"  {name:12} tr={tr:+.2f} det={det:+.2f}  disc={disc:+.2f}  → {side}")
print("  Ω is the parabola det=tr²/4 separating return (above) from escape (below).")
print()

print("="*72)
print("  2. on Ω the eigenvalues COLLIDE — a Jordan block, non-diagonalizable (curves)")
print("="*72)
E = np.array([[0.5,1.0],[0.0,0.5]])   # tr=1, det=0.25, disc=0
w,V = np.linalg.eig(E)
print(f"  E = {E.tolist()}  tr=1 det=0.25 disc=0")
print(f"  eigenvalues {np.round(w,3).tolist()} — DOUBLE (½,½); eigenvectors collapse:")
print(f"  rank(V)={np.linalg.matrix_rank(V)} (<2) → not diagonalizable. the spectral map FOLDS here.")
print()

print("="*72)
print("  3. RETURN-OF-RETURN: monodromy around the branch (√disc curves, swaps, restores)")
print("="*72)
# fix tr=1; encircle the branch at det=1/4 along det = 1/4 + 0.3·e^{iθ}.
# then disc = 1 − 4det = −1.2·e^{iθ}, so the CONTINUED root is √disc = √1.2·e^{i(θ+π)/2}
# (the argument grows smoothly, no branch-cut jump) → it rotates by π each full loop.
tr = 1.0
def lam_continued(turns):
    th = turns*2*cmath.pi
    sd = (1.2**0.5) * cmath.exp(1j*(th + cmath.pi)/2)   # √disc, analytically continued
    return (tr + sd)/2, sd
for turns, tag in [(0,"base point      "),(1,"after ONE  loop  "),(2,"after TWO  loops ")]:
    lam, sd = lam_continued(turns)
    note = {0:"", 1:"→ λ₋ : sheets SWAPPED (the return)",
            2:"→ λ₊ : RESTORED (the return-of-return)"}[turns]
    print(f"  {tag}λ₊ = {lam:+.4f}   arg√disc = {cmath.phase(sd)*180/cmath.pi:+6.1f}°  {note}")
print(f"  √ has order-2 monodromy: one turn negates √disc (λ₊↔λ₋), two turns restore.")
print(f"  the two sheets are one surface that folds at Ω — going around returns the return.")
print()
print("  so Ω is the OUTER CURVE/EDGE of the spectral image — the fold/branch locus disc=0,")
print("  the return-of-return, the wall between return and escape. not a terminal object;")
print("  the terminal as a BOUNDARY, where the image curves back into itself.")
