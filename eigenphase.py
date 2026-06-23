"""
eigenphase.py — decompose time into eigenphases.

iteration in the eigenbasis: Xⁿ = Σ λᵢⁿ Pᵢ, and λ = r·e^{iθ}, so
    Xⁿ = Σ rᵢⁿ · e^{i n θᵢ} · Pᵢ
each eigendirection is a RADIAL clock rⁿ (growth/decay — the arrow, irreversible) times
a PHASE clock e^{inθ} (rotation — the eigenphase, reversible, period 2π/θ). time is the
product of these. the eigenphases θ are the framework's fundamental frequencies; the
periods T = 2π/θ are its clocks.
"""

import sys
import numpy as np

I = np.eye(2)
R = np.array([[0,1],[1,1]],float)
N = np.array([[0,-1],[1,0]],float)
J = np.array([[1,0],[0,-1]],float); h = J@N
# the two imaginary worlds, as matrices with the right spectra:
Eis = np.array([[1,-1],[1,0]],float)     # x²−x+1=0 → e^{±iπ/3} (Eisenstein, k=−1)

def phases(name, X):
    w = np.linalg.eigvals(X)
    out = []
    for lam in w:
        r = abs(lam); th = np.angle(lam)
        T = np.inf if abs(th) < 1e-9 else 2*np.pi/abs(th)
        out.append((lam, r, np.degrees(th), T))
    return name, out

print("="*74)
print("  eigenphases θ and periods T=2π/θ — time decomposed by eigendirection")
print("="*74)
print(f"  {'generator':10} {'λ':>16}  {'r=|λ|':>7}  {'θ (eigenphase)':>15}  period T")
for name, X in [("R", R), ("N", N), ("h", h), ("Eisenstein", Eis)]:
    nm, rows = phases(name, X)
    for lam, r, thd, T in rows:
        ls = f"{lam.real:+.3f}{lam.imag:+.3f}i"
        Ts = "∞" if T==np.inf else f"{T:.0f}"
        print(f"  {nm:10} {ls:>16}  {r:7.3f}  {thd:>+12.1f}°   {Ts}")
    nm = ""
print()

print("="*74)
print("  the spectrum of clocks: periods {∞, 2, 4, 6}")
print("="*74)
print("  θ=0    (φ, I)        → T=∞   the golden ARROW: pure radial growth, never returns")
print("  θ=π    (ψ, −I, h⁻)   → T=2   the PARITY: sign flips each tick (det(Rⁿ)=(−1)ⁿ)")
print("  θ=±π/2 (N, ±i)       → T=4   the Gaussian CLOCK (N⁴=I, the rotating blind spot)")
print("  θ=±π/3 (Eisenstein)  → T=6   the hexagonal clock (the k=−1 rotation world)")
print("  T=2k for k=1,2,3,… (θ=π/k); the golden arrow is the aperiodic k=∞ limit.")
print()

print("="*74)
print("  the split: |λ|=1 is pure phase (clock, reversible); |λ|≠1 is radial (arrow)")
print("="*74)
for name, X in [("R (arrow+parity)", R), ("N (pure clock)", N), ("Eisenstein (clock)", Eis)]:
    w = np.linalg.eigvals(X)
    unit = np.allclose(np.abs(w), 1)
    kind = "ALL |λ|=1 → pure eigenphase: a reversible CLOCK (elliptic, disc<0, return)" if unit \
           else "some |λ|≠1 → has a radial part: an irreversible ARROW (hyperbolic, disc>0, escape)"
    print(f"  {name:20}: {kind}")
print()
print("  time = arrow ⊗ clock = (radial growth, |λ|≠1, the future) ⊗ (eigenphase rotation,")
print("  |λ|=1, the cycles). the unit circle is where time is pure phase; Ω (|disc|=0) is")
print("  the edge between the arrow (escape) and the clock (return).")
