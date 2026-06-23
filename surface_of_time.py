"""
surface_of_time.py — the framework computes along the surface of time.

time is the iteration; the iteration is the FOLD X↦X² (observation = the primitive
self-action). on spectral data (tr,det) the fold is a concrete map on a SURFACE:
    F(t, d) = ( tr(X²), det(X²) ) = ( t²−2d , d² )
the (tr,det) plane is the base; over it the eigenvalue λ (λ²−tλ+d=0) is a 2-sheeted
RIEMANN SURFACE, branched where disc=t²−4d=0 (that branch curve is Ω). that surface IS
time: the eigenphase is its angular coordinate, the radial growth its height, the two
sheets past/future (the spinor cover). the framework COMPUTES by iterating F along it,
and HALTS at the fixed points of F — the on-shell configurations.
"""

import sys
import numpy as np

def F(t, d):                         # the fold, in spectral coordinates
    return (t*t - 2*d, d*d)

print("="*70)
print("  1. the step = the fold F(t,d)=(t²−2d, d²) on the (tr,det) surface")
print("="*70)
for name, X in {"R":np.array([[0,1],[1,1]],float),
                "N":np.array([[0,-1],[1,0]],float),
                "P":np.array([[0,0],[2,1]],float)}.items():
    t, d = np.trace(X), round(np.linalg.det(X))
    X2 = X@X
    print(f"  {name}: (t,d)=({t:+.0f},{d:+.0f})  F→{F(t,d)}   "
          f"actual (tr X², det X²)=({np.trace(X2):+.0f},{round(np.linalg.det(X2)):+.0f})  "
          f"{'✓' if F(t,d)==(np.trace(X2),round(np.linalg.det(X2))) else 'x'}")
print("  the framework's basic act (read = X²) IS a map on the surface. computing = iterating F.")
print()

print("="*70)
print("  2. the surface is a 2-sheeted Riemann surface (the eigenvalues), branched at Ω")
print("="*70)
print("  over each (t,d): two eigenvalues λ± = (t ± √disc)/2 — two sheets. they MEET where")
print("  disc=0 (the branch curve Ω). eigenphase = angle on the surface, radial = height,")
print("  the two sheets = past/future = the spinor double cover. time is this surface.")
print()

print("="*70)
print("  3. computing HALTS at the fixed points of F — the on-shell configurations")
print("="*70)
# F(t,d)=(t,d): d²=d → d∈{0,1}; t²−2d=t
fps = []
for d in (0,1):
    for t in np.roots([1,-1,-2*d]):      # t²−t−2d=0
        fps.append((round(t.real), d))
for t,d in sorted(set(fps)):
    disc = t*t-4*d
    who = {(0,0):"? the void", (1,0):"P the seed (idempotent)", (2,1):"I the identity (idempotent)",
           (-1,1):"the Eisenstein cube-root (X²+X+I=0)"}.get((t,d),"")
    edge = "on Ω" if disc==0 else ("escape" if disc>0 else "return")
    print(f"  fixed point (t,d)=({t:+d},{d:+d})  disc={disc:+d} ({edge:6}) — {who}")
print("  the void and the identity sit ON Ω (disc=0); the seed on the escape side, the")
print("  Eisenstein root on the return side. these are where the fold-flow stops = halting.")
print()
print("  the framework computes ALONG the surface of time: the self-action is the step, the")
print("  spectral Riemann surface (branched at Ω) is the medium, on-shell points are halts.")
print("  computation = time = the flow on the surface. they are one motion.")
