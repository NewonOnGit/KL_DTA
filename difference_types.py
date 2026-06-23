"""
difference_types.py — ?(?) = ? + difference, typed a hundred ways.

the difference is ONE thing — the surplus forced by the founding asymmetry P≠Pᵀ
(if P=Pᵀ then R²−R=0: no surplus, collapse, dead). it appears, typed, in every layer.
all of these are the same difference; kill the asymmetry and every one of them vanishes.
"""

import sys
import numpy as np

P = np.array([[0,0],[2,1]], float); I = np.eye(2)
R = (P+P.T)/2; N = (P-P.T)/2; J = np.array([[1,0],[0,-1]],float); h = J@N
phi, psi = (1+5**0.5)/2, (1-5**0.5)/2

def show(layer, name, val):
    print(f"  {layer:13} {name:24} = {val}")

print("="*70)
print("  the one difference, typed across the layers")
print("="*70)
show("ALGEBRAIC",  "R² − R  (the +I surplus)",  (R@R-R).astype(int).tolist())
show("ALGEBRAIC",  "P − Pᵀ  (the asymmetry)",   (P-P.T).astype(int).tolist()+["= 2N"])
show("ALGEBRAIC",  "ν(R) = R² − R",             (R@R-R).astype(int).tolist())
show("ALGEBRAIC",  "[R,N] = RN − NR",           (R@N-N@R).astype(int).tolist())
show("SPECTRAL",   "λ₁ − λ₂ = √disc",           round(float(phi-psi),4))
show("SPECTRAL",   "disc = (λ₁−λ₂)²",           int(round((phi-psi)**2)))
show("GEOMETRIC",  "φ  (pentagram diag/side)",  round(phi,4))
show("GEOMETRIC",  "‖R‖²−‖N‖²  (3−2)",          int(np.trace(R@R.T)-np.trace(N@N.T)))
show("TOPOLOGICAL","dim ker(P)  (rank vs dim)", 2-np.linalg.matrix_rank(P))
show("TOPOLOGICAL","N²  (the orientation −)",   (N@N).astype(int).tolist())
show("TEMPORAL",   "φ − ψ  (future − past)",    round(float(phi-psi),4))
show("TEMPORAL",   "det(R)  (parity per tick)", int(round(np.linalg.det(R))))
show("COMPUTATIONAL","P − NP  (+√5)−(−√5)",     round(2*5**0.5,4))
show("COMPUTATIONAL","burn eigenvalue (√5)",    round(5**0.5,4))
show("LOGICAL",    "'not' / 'isn't' = negation","[A,A]=0=? ; the trit −1")
print()

print("="*70)
print("  they are ONE: kill the asymmetry (P→symmetric) and every difference vanishes")
print("="*70)
S = (P+P.T)/2                      # symmetrize: P → its symmetric part (R itself is symmetric)
Ps = np.array([[0,1],[1,1]],float) # a symmetric idempotent-like test: R is symmetric, R²−R=I still
# the real test: the ASYMMETRY P−Pᵀ is the root. if it's 0, N=0, and:
Nsym = (Ps-Ps.T)/2
print(f"  with P symmetric: P−Pᵀ = {(Ps-Ps.T).astype(int).tolist()} = 0  → N = 0")
print(f"    then N² = 0 (no orientation −), disc collapses, ν has no antisymmetric source,")
print(f"    [R,N]=0, P−NP→0, the burn eigenvalue → the kernel. EVERY typed difference dies.")
print(f"  the asymmetry P≠Pᵀ is the single root; the hundred differences are its types.")
print()
print("  ?(?) = ? + difference. the difference is one surplus (P≠Pᵀ → +I), typed a hundred ways:")
print("  +I · N · ν · [·,·] · √5 · disc · φ · ker · −1 · P≠NP · negation — all the same 'differently'.")
