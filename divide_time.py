"""
divide_time.py — divide time in half.

a tick is a power Xⁿ. half a tick is √X. dividing time in half is the operation X ↦ √X,
which HALVES every eigenphase (θ ↦ θ/2) and DOUBLES every period (T ↦ 2T). three consequences:

  1. N = √(−I).  −I is the half-turn (θ=π, period 2 — the PARITY tick). its half is the
     quarter-turn N (θ=π/2, period 4). so OBSERVATION (N) is literally half the orientation
     flip. dividing the flip in half is N²=−I read backwards.
  2. the DYADIC clock tower: keep halving — −I(2) → N(4) → √N(8) → … period 2ⁿ. binary time.
  3. √ is TWO-VALUED (±): half-time is a DOUBLE COVER. a full 2π turn sends the half-tick to
     MINUS itself — a SPINOR. you need 4π (two full turns) to come back. spin-½, from halving.
  and the arrow: √R is COMPLEX (ψ<0 ⇒ √ψ imaginary) — half a step of the real generation
  arrow dips into the imaginary, i.e. into observation. the half-tick of R is N-flavoured.
"""

import sys
import numpy as np

I = np.eye(2)
R = np.array([[0,1],[1,1]],float)
N = np.array([[0,-1],[1,0]],float)

def sqrtm2(X):
    w,V = np.linalg.eig(X.astype(complex))
    return V @ np.diag(np.sqrt(w)) @ np.linalg.inv(V)

print("="*72)
print("  1. N = √(−I): observation is HALF the orientation flip")
print("="*72)
print(f"  −I = rotation by π  (θ=π, period 2 — the PARITY tick, det flips)")
print(f"  N  = rotation by π/2 (θ=π/2, period 4)   N² = {(N@N).astype(int).tolist()} = −I  ✓")
print(f"  so N = √(−I): dividing the half-turn (−I) in half gives the quarter-turn (N).")
print(f"  the observer (N) is the half-tick of the parity. half of a flip is a turn.")
print()

print("="*72)
print("  2. the dyadic clock tower — keep halving, period doubles: 2 → 4 → 8 → …")
print("="*72)
M = -I; T = 2
for step in range(4):
    th = abs(np.angle(np.linalg.eigvals(M.astype(complex))[0]))
    period = 2*np.pi/th if th>1e-9 else np.inf
    print(f"  {'√'*step}(−I)  θ = {np.degrees(th):6.1f}°   period = {period:.0f}")
    M = sqrtm2(M)
print(f"  each half-step doubles the period: T = 2ⁿ. binary/dyadic time, the bit-tower.")
print()

print("="*72)
print("  3. half-time is a DOUBLE COVER → spinors")
print("="*72)
hN = sqrtm2(N)                          # √N: period 8 (eighth-turn)
full_turn = np.linalg.matrix_power(hN, 4)   # 4 eighth-turns = π... = one half of 2π in N-ticks
print(f"  √N = eighth-turn (period 8). four of them: (√N)⁴ = {np.round(full_turn.real,3).tolist()}")
print(f"  = N² = −I, NOT I — a 2π turn (in N's full-ticks) lands on MINUS one under the half.")
print(f"  you must go around TWICE (4π) to return: (√N)⁸ = N⁴ = I. that is SPIN-½.")
print(f"  halving time forces the ± branch of √ — the spinor double cover, from one division.")
print()

print("="*72)
print("  the arrow can't be halved in the reals: √R is COMPLEX")
print("="*72)
sR = sqrtm2(R)
w = np.linalg.eigvals(R)
print(f"  R eigenvalues {np.round(w,3).tolist()} — one is NEGATIVE (ψ<0).")
print(f"  √R eigenvalues {np.round(np.sqrt(w.astype(complex)),3).tolist()} — √ψ is IMAGINARY.")
print(f"  max |Im(√R)| = {np.abs(sR.imag).max():.3f} ≠ 0: half a step of the generation ARROW")
print(f"  dips into the imaginary = into observation. between two real ticks lies an N-tick.")
