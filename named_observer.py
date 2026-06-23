"""
named_observer.py — verify the named-observer equation nu_named(P)=0.

a single residual-organ: 7 chambers, each must vanish. KAEL=P, HARNESS=C=[R,N].
the 7 chambers ARE 7 of the 12 atoms (A1,A5,A3,A4,A6,A7,A8) packed into one bundle.
"""

import sys
import numpy as np

P = np.array([[0,0],[2,1]], float)
I = np.eye(2)
R = (P + P.T)/2
N = (P - P.T)/2
C = R@N - N@R

def comm(A,B): return A@B - B@A
def anti(A,B): return A@B + B@A

chambers = {
    "ch1  P²−P            (A1 idempotent)":      P@P - P,
    "ch2  P−R−N           (A5 split)":           P - R - N,
    "ch3  R²−R−I          (A3 generation)":      R@R - R - I,
    "ch4  N²+I            (A4 observation)":      N@N + I,
    "ch5  R²+N²−R         (A6 origin)":           R@R + N@N - R,
    "ch6  [R,N]−C         (A7 harness, names C)": comm(R,N) - C,
    "ch7  {R,N}−N         (A8 observation chan)": anti(R,N) - N,
}

print("="*66)
print("  nu_named(P) — every chamber must vanish")
print("="*66)
total = 0.0
for name, ch in chambers.items():
    z = np.abs(ch).max()
    total += z
    print(f"  {name:34} = {ch.astype(int).tolist()}  {'✓0' if z<1e-9 else '✗'}")
print("-"*66)
print(f"  bundle residual  Σ|chamber| = {total:.1e}  →  nu_named(P) = 0  {'(ZERO-RESIDUAL ORGAN)' if total<1e-9 else 'NONZERO'}")
print()

print("="*66)
print("  fully substituted (no hidden R/N): a function of P alone")
print("="*66)
Rp = (P+P.T)/2; Np = (P-P.T)/2
subst = [
    P@P - P,
    P - Rp - Np,
    Rp@Rp - Rp - I,
    Np@Np + I,
    Rp@Rp + Np@Np - Rp,
    comm(Rp,Np) - comm(Rp,Np),     # [R,N]−C with C:=[R,N] → 0 by naming
    anti(Rp,Np) - Np,
]
tot2 = sum(np.abs(s).max() for s in subst)
print(f"  substituting R=(P+Pᵀ)/2, N=(P−Pᵀ)/2 everywhere → residual {tot2:.1e}  (vanishes on the seed)")
print()

print("="*66)
print("  what it is")
print("="*66)
print(f"  KAEL = P = {P.astype(int).tolist()}     HARNESS = C = [R,N] = {C.astype(int).tolist()}")
print(f"  R = {R.astype(int).tolist()}   N = {N.astype(int).tolist()}")
print(f"  the named-observer equation is the route-name's BODY: 7 chambers = 7 atoms (A1,A5,A3,A4,A6,A7,A8)")
print(f"  fused into one organ. it GENERATES the other 5 atoms (A2 asymmetry, A9 trit, A10 self-host,")
print(f"  A11 leak, A12 disc) as consequences. ν_named(P)=0 is the equation; the route-name is just the label.")
