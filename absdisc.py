"""
absdisc.py — |disc| = Ω.

disc = tr²−4det = (λ₁−λ₂)² carries a SIGN, and the sign is the regime:
    disc < 0   RETURN  (elliptic, complex λ, bounded)
    disc = 0   Ω        (the edge, λ collide)
    disc > 0   ESCAPE  (hyperbolic, real λ, unbounded)
a trit {−,0,+} on the disc-line, with Ω at the centre.

|disc| FOLDS that line at 0: it reflects RETURN onto ESCAPE across Ω, throwing away
the sign = the regime. so |·| is the reflection at Ω; its fixed point / zero IS Ω.
|reflection| = identification: |disc| identifies return and escape — it cannot tell
which side of the edge you are on. Ω is exactly where that information (the sign) dies,
and |disc| = |λ₁−λ₂|² is the spectral GAP that closes to 0 at the edge.
"""

import sys
import numpy as np

def trd(tr, det):
    disc = tr*tr - 4*det
    w = np.roots([1, -tr, det])
    gap2 = abs((w[0]-w[1])**2)
    return disc, gap2, w

print("="*70)
print("  disc is signed = the regime; |disc| folds the two regimes together")
print("="*70)
rows = {"N (return)":(0,1), "rot k=−1":(1,1), "Ω edge":(1,0.25),
        "seed P":(1,0), "R k=+1":(1,-1)}
print("  matrix        disc      sign→regime         |disc| = |λ₁−λ₂|²")
for nm,(tr,det) in rows.items():
    disc, gap2, w = trd(tr, det)
    reg = "RETURN" if disc < -1e-9 else "Ω edge" if abs(disc)<1e-9 else "ESCAPE"
    print(f"  {nm:12} {disc:+6.2f}    {reg:8}            {gap2:.3f}   "
          f"(λ={np.round(w,3).tolist()})")
print()
print("  |disc| is the same for a return matrix and an escape matrix at equal distance")
print("  from the edge — the SIGN (the regime) is gone. |·| identified them across Ω.")
print()

print("="*70)
print("  Ω = the zero / fixed point of |disc|;  |disc| = the Ω-field")
print("="*70)
d_ret,_,_ = trd(1, 0.25+0.30)     # return side, 0.30 past the edge
d_esc,_,_ = trd(1, 0.25-0.30)     # escape side, 0.30 before the edge
print(f"  return side (det=0.55): disc = {d_ret:+.2f},  |disc| = {abs(d_ret):.2f}")
print(f"  escape side (det=−0.05): disc = {d_esc:+.2f},  |disc| = {abs(d_esc):.2f}")
print(f"  |disc| equal on both sides → |disc| is the RADIAL coordinate around Ω:")
print(f"  it measures distance from the edge and is BLIND to the side. Ω = {{|disc|=0}}.")
print()
print("  |disc| = Ω: the absolute value of the discriminant is the Ω-coordinate — the")
print("  reflection that folds return onto escape across the edge (|reflection|=")
print("  identification), whose zero/fixed-point is Ω itself. the gap closing is the edge.")
