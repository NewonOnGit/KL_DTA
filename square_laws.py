"""
square_laws.py — burns are square laws.

the master equation X²=tr·X−det·I is THE square law (the quadratic/dispersion). its discriminant
disc=tr²−4det is itself a square: (λ1−λ2)². the impossibility operator L has burn-eigenvalues ±√disc,
so L²=disc·I on the burn-eigenspace: each BURN squared = disc. a burn is ±√disc — two roots with the
SAME square but OPPOSITE sign. the forbidden identification +√disc ≟ −√disc IS the burn: |X|²=X²
(squaring identifies) but |X|≠X (the roots differ). the impossibility is the ± of the square root.
"""
import sys
import numpy as np

R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
def sa(X):
    b=[np.array(v,float).reshape(2,2) for v in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
    return np.column_stack([(X@B+B@X-B).reshape(-1) for B in b])

print("="*70)
print("  the square law and its discriminant")
print("="*70)
print(f"  master eq: X² = tr·X − det·I  — THE square law (the quadratic / the dispersion).")
print(f"  disc = tr²−4det = (λ1−λ2)²  — itself a SQUARE (the squared spread). disc(R)={int(np.trace(R)**2-4*np.linalg.det(R))}=5.")
print()

print("="*70)
print("  the impossibility is √disc: L² = disc·I on the burns")
print("="*70)
L=sa(R)
ev=sorted(np.linalg.eigvals(L).real)
print(f"  L_{{R,R}} eigenvalues = {[round(e,3) for e in ev]} = {{−√5, 0, 0, +√5}} = {{−√disc,0,0,+√disc}}")
L2ev=sorted(np.linalg.eigvals(L@L).real)
print(f"  L² eigenvalues = {[round(e,3) for e in L2ev]} = {{5,0,0,5}}: on the burn-eigenspace L²=disc·I.")
C=R@N-N@R
print(f"  the observer C=[R,N]: C² = {np.round(C@C,1).tolist()} = 5·I = disc·I — the observer is a square law too.")
print(f"  so each BURN, squared, gives disc. a burn is ±√disc.")
print()

print("="*70)
print("  the burn = +√disc ≟ −√disc : same square, opposite sign (forbidden)")
print("="*70)
print(f"  the square law x²=disc has TWO roots: +√disc and −√disc. they share the SAME square (disc)")
print(f"  but are NOT equal (opposite sign). the BURN is the forbidden identification of the two roots.")
print(f"  this IS |reflection|=identification: |X|² = X² (squaring identifies — same square) but |X| ≠ X")
print(f"  (the roots differ — the reflection is not the identity). the gap between 'same square' and")
print(f"  'same value' is the burn. the obstruction is SIGN — squaring loses it; the ± is irreducible.")
print()
print("  BURNS ARE SQUARE LAWS: each is a quadratic (x²=disc) whose two roots (±√disc) cannot collapse.")
print("  the impossibility is the ± of the square root; disc is the square; the burn is the refusal to choose a sign.")
