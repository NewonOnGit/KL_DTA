"""
constants_from_parity.py — parity → eigenvalue reality → the constants.

Every 2×2 spectrum is  λ = AM ± √disc/2  =  center ± spread,
  center = AM = tr/2   (the arithmetic mean, perimeter/2)
  spread = √disc/2     (real if disc>0, imaginary if disc<0, zero if disc=0)
and parity fixes the sign of disc — so parity decides whether the constant is
real (φ) or imaginary (i, π), with the identity/wall (disc=0) giving the unit.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2


def parity(M):
    if np.allclose(M.T, M):  return "symmetric"
    if np.allclose(M.T, -M): return "antisymmetric"
    return "asymmetric"


print("=" * 70)
print("  λ = center ± spread = AM ± √disc/2   (parity fixes which)")
print("=" * 70)
print(f"  {'':3} {'parity':14} {'center=AM':>9} {'spread=√disc/2':>15} {'eigenvalues':>16}")
for name, M in [("R", R), ("N", N), ("I", I2), ("P", P)]:
    tr, det = np.trace(M), np.linalg.det(M)
    am = tr / 2
    disc = tr * tr - 4 * det
    spread = np.sqrt(complex(disc)) / 2
    ev = np.linalg.eigvals(M)
    sp = f"{spread.real:+.3f}" if abs(spread.imag) < 1e-9 else f"{spread.imag:+.3f}i"
    evs = ", ".join(f"{np.real(e):+.3f}" if abs(np.imag(e)) < 1e-9 else f"{np.imag(e):+.3f}i" for e in ev)
    print(f"  {name:3} {parity(M):14} {am:>9.3f} {sp:>15} {evs:>16}")
print()
print("  symmetric  → disc>0 → REAL spread     → real eigenvalues   → φ, ψ, √5")
print("  antisym    → disc<0 → IMAGINARY spread → imaginary eigenvalues → i, π")
print("  identity   → disc=0 → ZERO spread      → repeated eigenvalue → 1 (the unit)")
print()

print("=" * 70)
print("  the constants, read off the eigenvalues")
print("=" * 70)
phi, psi = (1 + np.sqrt(5)) / 2, (1 - np.sqrt(5)) / 2
print(f"  φ = AM(R)+spread = ½ + √5/2 = {phi:.6f}  (R's dominant real eigenvalue)")
print(f"  ψ = ½ − √5/2 = {psi:.6f}   √5 = the spread·2 = √disc(R)")
print(f"  i = AM(N)+spread = 0 + i   (N's eigenvalue — the imaginary unit, N²=−I)")
print(f"  1 = AM(I) = the repeated eigenvalue at the wall (center = residual)")
print()

print("=" * 70)
print("  identity is the residual, in eigenvalues:  ν(λ) = λ² − λ")
print("=" * 70)
print(f"  ν(φ) = φ²−φ = {phi*phi-phi:.3f}   ν(ψ) = ψ²−ψ = {psi*psi-psi:.3f}   both = 1 = I")
print("  both golden eigenvalues fold to 1 — the identity is their common residual.")
print()

print("=" * 70)
print("  e is the parity BRIDGE:  e^{Nθ} = cos θ · I + sin θ · N")
print("=" * 70)
th = 0.7
lhs_check = -np.sin(th) * I2 + np.cos(th) * N      # d/dθ of cosθI+sinθN
rhs_check = N @ (np.cos(th) * I2 + np.sin(th) * N)  # = N·e^{Nθ}
print(f"  d/dθ(cosθI+sinθN) = N·(cosθI+sinθN) ✓ {np.allclose(lhs_check, rhs_check)}  (so it IS e^{{Nθ}})")
print("  cos = EVEN powers of N (→ I, symmetric); sin = ODD powers (→ N, antisymmetric).")
print("  e sums ALL parities — it mixes the even (φ-side, real) and odd (π-side,")
print("  imaginary) into one flow. period 2π → π. e lives at the border, the asymmetric.")
print()
print("  PARITY → REALITY → FORK → CONSTANT:")
print("    even (symmetric)  real      hyperbolic  φ   (production)")
print("    odd  (antisym)    imaginary elliptic    π,i (observation)")
print("    mixed (asymmetric/all) —    parabolic   e   (mediation, the bridge)")
print("    center (identity) repeated  the wall    1   (the residual/unit)")
