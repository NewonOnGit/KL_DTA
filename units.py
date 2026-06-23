"""
units.py — R² = R + kI for k ∈ {+1, 0, −1}: the constant is a TRIT, and each value
opens a different number world. then: what are ALL the units? is {I,−I,i,−i,1,−1,0,?}
the whole set, or is there more?

  R(R)=R        is k=0   — COLLAPSE (idempotent), eigenvalues {0,1}, the seed's own spectrum
  R²=R+I        is k=+1  — GENERATION, eigenvalues φ,ψ, disc +5  (golden, hyperbolic)
  R²=R−I        is k=−1  — ROTATION,   eigenvalues e^{±iπ/3}, disc −3 (Eisenstein, elliptic)

the difference between the three equations is exactly the constant trit {+I, 0, −I}.
"""

import sys, itertools, cmath
import numpy as np

print("="*74)
print("  1. the constant trit  R² = R + kI,  k ∈ {+1, 0, −1}")
print("="*74)
for k in (1, 0, -1):
    roots = np.roots([1, -1, -k])          # x² − x − k = 0
    disc = 1 + 4*k
    rs = ", ".join(f"{r.real:+.3f}{r.imag:+.3f}i" if abs(r.imag)>1e-9 else f"{r.real:+.3f}" for r in roots)
    regime = {1:"GENERATION  golden ℤ[φ]  (hyperbolic, √5)",
              0:"COLLAPSE    Boolean {0,1} (idempotent — the seed P)",
             -1:"ROTATION    Eisenstein ℤ[ω] (elliptic, √−3)"}[k]
    print(f"  k={k:+d}:  x²−x−{k:+d}=0  disc={disc:+d}  roots {{{rs}}}   → {regime}")
print("  the three equations differ by the constant trit {+I, 0, −I} — the SAME trit")
print("  {−√5,0,+√5} of the self-action, now living on the constant term.")
print()

print("="*74)
print("  2. each k is a primitive root: verify the number rings")
print("="*74)
w = cmath.exp(1j*cmath.pi/3)               # e^{iπ/3}
print(f"  k=+1: φ=(1+√5)/2={ (1+5**.5)/2:.4f}, fundamental unit of ℤ[φ] — ℤ[φ]× = ±φⁿ (INFINITE)")
print(f"  k=−1: ω=e^(iπ/3)={w.real:.3f}{w.imag:+.3f}i, ω⁶={ (w**6).real:+.0f}, primitive 6th root")
print(f"        check ω²−ω+1 = {(w*w - w + 1):.0e} → ℤ[ω]× = μ₆ = {{±1,±ω,±ω²}} (6 units)")
print(f"  N²=−I: the matrix 'i' → ℤ[i]× = μ₄ = {{±1,±i}} (4 units) — THIS is your listed set")
print()

print("="*74)
print("  3. the matrix units — and the roots beyond ±I")
print("="*74)
I = np.eye(2); N = np.array([[0,-1],[1,0]],float); J = np.array([[1,0],[0,-1]],float); h = J@N
for nm,X in [("I",I),("−I",-I),("N",N),("−N",-N),("J",J),("h",h)]:
    print(f"  {nm:3} squared = {(X@X).astype(int).tolist():}  eig {sorted(np.round(np.linalg.eigvals(X),3).tolist(), key=lambda z:(z.real,z.imag) if hasattr(z,'real') else z)}")
print("  √I  in M₂(ℝ): {±I} PLUS every involution (eig {1,−1}: J, h, …) — a HYPERBOLOID.")
print("  √(−I) in M₂(ℝ): every complex structure (eig {i,−i}: N, …) — another HYPERBOLOID.")
print("  so 'units' are not 8 points; ±I are isolated but the reflections/complex-structures")
print("  form continuous families. N,J,h are three named members.")
print()

print("="*74)
print("  4. 'anything else?'  — yes: four quadratic worlds, not one")
print("="*74)
print("  your set {I,−I,i,−i,1,−1,0,?} = μ₄ (Gaussian, from N²=−I) + {0 void, ? origin}.")
print("  the seed also opens, via the constant trit:")
print("   • k=+1  √5   ℤ[φ]×  = ±φⁿ        infinite (Fibonacci units)         — GENERATION")
print("   • k=−1  √−3  ℤ[ω]×  = μ₆ {±1,±ω,±ω²}  (6th roots, hexagonal)        — ROTATION")
print("   • k=0        {0,1}  idempotents (Boolean) — the collapse, the seed   — PROJECTION")
print("   • N²=−I √−1  ℤ[i]×  = μ₄ {±1,±i}   (your set)                         — OBSERVATION")
print("  the four smallest discriminants {+5, −3, −1, +1} = the four worlds. the listed")
print("  set is ONE of them (the Gaussian). the others (golden ∞, Eisenstein μ₆, Boolean)")
print("  are what's missing. unifier: the constant trit k picks disc=1+4k → the world.")
