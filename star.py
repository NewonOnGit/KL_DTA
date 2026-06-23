"""
star.py — the body (5 base records) is a 5-point star {5/2}, not a 5-cycle C₅.

5 = disc = ‖R‖² + ‖N‖² = 3 + 2. The five records split exactly: 3 FORCED (the R-part,
visible, production) + 2 framing (schema=AXIOM, slot=OPEN — the N-part, hidden). The
figure on 5 points that carries φ is the PENTAGRAM {5/2}: connect every SECOND vertex.
Step 2 = the fold ν (degree 2, the master equation X²). gcd(2,5)=1 → one closed stroke
through all five. Its segment ratio is φ = R's eigenvalue (R²=R+I). The body draws
itself by the fold; the radical of the whole thing is √5 = the self-action spectrum.
"""

import sys, io, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

phi = (1 + 5 ** 0.5) / 2
R = np.array([[0, 1], [1, 1]], float)
N = np.array([[0, -1], [1, 0]], float)
nR2 = float(np.trace(R @ R.T))
nN2 = float(np.trace(N @ N.T))

print("=" * 70)
print("  1. five points, split 3 + 2 = ‖R‖² + ‖N‖² = disc")
print("=" * 70)
print(f"  ‖R‖² = {nR2:.0f}  (the 3 FORCED: master_equation·carrier_manifold·burns) — R, visible")
print(f"  ‖N‖² = {nN2:.0f}  (the 2 framing: schema=AXIOM · slot=OPEN)              — N, hidden")
print(f"  total = {nR2+nN2:.0f} = disc = the 5 vertices of the star")
print()

print("=" * 70)
print("  2. the figure is {5/2} (step 2), not C₅ (step 1) — the burn 5 ≟ C₅")
print("=" * 70)
# one closed stroke visits all five iff gcd(step,5)=1
def stroke(step):
    seq, v = [0], 0
    for _ in range(5):
        v = (v + step) % 5; seq.append(v)
    return seq
print(f"  step 1 (pentagon / C₅) : {stroke(1)}  — adjacent, a rotation")
print(f"  step 2 (pentagram {{5/2}}): {stroke(2)}  — skip one = the FOLD ν (degree 2)")
print(f"  gcd(2,5) = {math.gcd(2,5)} → step 2 is ONE closed stroke through all five.")
print(f"  the body draws itself by applying the degree-2 self-action and returning.")
print()

print("=" * 70)
print("  3. the star's ratio is φ = R's eigenvalue (R² = R + I)")
print("=" * 70)
# unit circumradius; chord across angular separation θ = 2 sin(θ/2)
side = 2 * math.sin(math.radians(72) / 2)     # step-1 chord (pentagon side)
diag = 2 * math.sin(math.radians(144) / 2)    # step-2 chord (pentagram diagonal)
print(f"  side  (step 1) = 2 sin 36° = {side:.5f}")
print(f"  diag  (step 2) = 2 sin 72° = {diag:.5f}")
print(f"  diag / side = {diag/side:.6f}   φ = {phi:.6f}   match: {abs(diag/side-phi)<1e-9}")
print(f"  so the FOLD-edge is φ× the cycle-edge: stepping by ν scales by φ. φ²=φ+1 ↔ R²=R+I.")
print()

print("=" * 70)
print("  4. the radical is √5 — the self-action spectrum IS the pentagram's number")
print("=" * 70)
# self-action {R,R}: X ↦ RX + XR − X, as a 4×4 on vec(X); its spectrum is {+√5,0,0,−√5}
basis = [np.array(b, float).reshape(2, 2) for b in
         ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
M = np.column_stack([(R @ B + B @ R - B).reshape(-1) for B in basis])
sa = sorted(round(float(x), 6) for x in np.linalg.eigvals(M).real)
print(f"  self-action {{R,R}} spectrum = {sa}  →  ±√5 = ±{5**0.5:.5f}")
print(f"  disc = {nR2+nN2:.0f};  φ = (1+√5)/2;  the spread is √5.")
print(f"  √5 = {5**0.5:.6f} is the diagonal of the 1×2 rectangle and the pentagram's radical.")
print(f"  the body's count (5), its eigen-spread (√5), and its edge-ratio (φ) are one figure.")
