"""
all_constants.py — ALL possible constants, not the six landmarks.

The seed doesn't emit a finite list — it generates a NUMBER FIELD. The named constants
(φ,√5,√3,√2,e,π) are just signposts. The full set:

  • R IS the Fibonacci matrix: Rⁿ = [[F_{n−1},F_n],[F_n,F_{n+1}]]. so every Fibonacci
    and Lucas number is a constant — tr(Rⁿ)=Lₙ, off-diagonal=Fₙ. infinitely many,
    the integer lattice ℤ[φ] of the golden field. the +√5 channel COUNTS them out.
  • the idempotent FAMILY (disc = 1+k²) gives 2,5,10,17,26,… — the framework quantities
    are these discriminants.
  • norms adjoin √2,√3; rotation/exp adjoin i,π,e. closure = ℚ(√2,√3,√5) ⊕ {e,π}.
"""

import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

R = np.array([[0,1],[1,1]], float)
phi = (1+5**0.5)/2

print("="*72)
print("  1. R is the Fibonacci matrix — Rⁿ reads out ALL Fibonacci & Lucas numbers")
print("="*72)
M = np.eye(2)
print("   n :  Rⁿ entries            Fₙ (off-diag)   Lₙ = tr(Rⁿ)   det=(−1)ⁿ")
for n in range(1, 9):
    M = M @ R
    fib = int(round(M[0,1])); luc = int(round(np.trace(M))); dt = int(round(np.linalg.det(M)))
    print(f"   {n} :  {M.astype(int).tolist()}        F={fib:<3}          L={luc:<3}        {dt:+d}")
print("   → every Fibonacci Fₙ and Lucas Lₙ is a seed constant. an INFINITE family,")
print("     the integer lattice ℤ[φ] of the golden field. φⁿ = Fₙ·φ + Fₙ₋₁.")
for n in range(2,7):
    F=[0,1,1,2,3,5,8,13]; lhs=phi**n; rhs=F[n]*phi+F[n-1]
    print(f"     φ^{n} = {lhs:.4f} = {F[n]}·φ + {F[n-1]} = {rhs:.4f}  ✓" if abs(lhs-rhs)<1e-9 else "x")
print()

print("="*72)
print("  2. the idempotent FAMILY: disc(k) = 1 + k²  — the framework's numbers")
print("="*72)
meaning = {2:"|S₀| (the two inputs)", 5:"disc = ‖R‖²+‖N‖² (THE seed)",
           10:"2·disc = Λ²(5)", 17:"dim_gauge + disc", 26:"d_crit (bosonic string)"}
for k in range(1,6):
    d = 1 + k*k
    print(f"   k={k}:  1+{k}² = {d:<3}  — {meaning.get(d,'')}")
print("   the seed is the k=2 member (disc=5); the others are its siblings.")
print()

print("="*72)
print("  3. the closure — all possible constants = a field, not a list")
print("="*72)
print("   ℤ            integers / counts (1,2,3,5; the seed entries)")
print("   ⊂ ℤ[φ]       golden integers = Fibonacci ∪ Lucas (R-powers, the +√5 channel)")
print("   ⊂ ℚ(√5)      the golden field (φ,ψ,√5; R²=R+I lives here)")
print("   ⊂ ℚ(√2,√3,√5) adjoin the norms ‖N‖²=2, ‖R‖²=3 (→ √2, √3)")
print("   ⊕ {i, π, e}  transcendental/analytic closure: i,π from N²=−I (rotation),")
print("                e from exp(h). the elliptic + exponential channels.")
print()
print("   the named six are LANDMARKS; the microscope's L0 is this entire field, whose")
print("   integer skeleton is the Fibonacci/Lucas lattice and whose family is 1+k².")
print("   'all possible constants' = the closure of the seed under +,×,eig,exp,norm.")
