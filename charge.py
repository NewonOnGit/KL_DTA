"""
charge.py — this is literal charge.

N² = −I generates U(1): exp(θN) = cosθ·I + sinθ·N = the phase rotation. U(1) IS
electromagnetism, and its conserved Noether quantity is electric CHARGE. so:
    N eigenvalues ±i  →  charge ±1  (particle / antiparticle)
    +I (production overshoot)  =  positive charge
    −I (observation undershoot) =  negative charge
    (+I) + (−I) = 0   IS charge CONSERVATION / neutrality  =  R²+N² = R (the completion)
charge is the incompletion made physical: real, irreducible (±I never vanish alone),
yet always balancing (they only cancel). charge conservation = the incompletion completing
itself, completely incomplete. one more TYPE of the one difference — the electromagnetic one.
"""

import sys
import numpy as np

N = np.array([[0,-1],[1,0]], float); I = np.eye(2); R = np.array([[0,1],[1,1]], float)

print("="*68)
print("  1. N² = −I generates U(1): exp(θN) = the phase rotation (electromagnetism)")
print("="*68)
for th in (np.pi/2, np.pi):
    E = np.cos(th)*I + np.sin(th)*N
    print(f"  exp({th:.3f}·N) = {np.round(E,3).tolist()}  (a rotation — the U(1) phase e^{{iθ}})")
print(f"  {{exp(θN)}} = the circle U(1) = the gauge group of electromagnetism.")
print()

print("="*68)
print("  2. the charge = the eigenvalue of the generator N (±i → ±1)")
print("="*68)
w = np.linalg.eigvals(N)
print(f"  N eigenvalues = {np.round(w,3).tolist()} = ±i  →  charge q = ±1 (particle / antiparticle)")
print(f"  charge is the sign of the observation-clock (the eigenphase ±π/2): the two directions of N-time.")
print()

print("="*68)
print("  3. ±I are the two charges; their sum is conservation = the completion")
print("="*68)
pos = R@R - R       # +I
neg = N@N           # −I
print(f"  +I (production overshoot)   = {pos.astype(int).tolist()}  → positive charge")
print(f"  −I (observation undershoot) = {neg.astype(int).tolist()}  → negative charge")
print(f"  (+I)+(−I) = {(pos+neg).astype(int).tolist()} = 0   CHARGE CONSERVATION / neutrality")
print(f"  R² + N² = {((R@R)+(N@N)).astype(int).tolist()} = R   the completion IS the neutral (charge-0) return.")
print()

print("="*68)
print("  4. charge = the incompletion, made physical (completely incomplete)")
print("="*68)
print(f"  the ±I never vanish alone — only cancel. a charged particle = an UNPAIRED incompletion;")
print(f"  pair creation/annihilation = a +I and −I appearing/cancelling. charge is REAL and IRREDUCIBLE,")
print(f"  yet always conserved (balances to 0). charge conservation = the incompletion completing itself,")
print(f"  completely incomplete. this is literal charge — the electromagnetic TYPE of the one difference.")
