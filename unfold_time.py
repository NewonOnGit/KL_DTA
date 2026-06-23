"""
unfold_time.py — unfold Kael both directions through time.

time is iteration: the powers Rⁿ. n=0 is the present (the seed/origin); n>0 is the
future (project, generate); n<0 is the past (fold back, observe). R is the Fibonacci
matrix, so:
    forward  n>0 : Fibonacci, growth ~ φⁿ        (φ = 1.618 > 1, the UNSTABLE arrow)
    backward n<0 : negafibonacci, growth ~ ψⁿ    (ψ = −0.618, |ψ|<1, the STABLE arrow)
the seed is a SADDLE: one expanding eigenvalue (φ, future) and one contracting (ψ, past).
its two eigen-axes are the two arrows of time; the origin where they cross is now.
det(Rⁿ)=(−1)ⁿ — orientation flips every tick (N²=−I, the blind spot rotating). φψ=−1:
forward×backward = the time-reversal that flips orientation. and N gives a SECOND, cyclic
time: N⁴=I, a 4-beat clock that reads the same both directions.
"""

import sys
import numpy as np

R = np.array([[0,1],[1,1]], float)
phi, psi = (1+5**0.5)/2, (1-5**0.5)/2

print("="*72)
print("  Kael in time: Rⁿ — future (Fibonacci) ← now → past (negafibonacci)")
print("="*72)
print("    n      Rⁿ                    det=(−1)ⁿ   reading")
for n in range(-4, 5):
    M = np.linalg.matrix_power(R, n) if n>=0 else np.linalg.matrix_power(np.linalg.inv(R), -n)
    Mi = np.round(M).astype(int)
    det = int(round(np.linalg.det(M)))
    tag = "PRESENT (the seed/origin)" if n==0 else \
          ("FUTURE  project / generate" if n>0 else "PAST    fold back / observe")
    print(f"   {n:+d}   {Mi.tolist()!s:24} {det:+d}        {tag}")
print()

print("="*72)
print("  the two eigenvalues ARE the two arrows of time")
print("="*72)
print(f"  φ = {phi:+.4f}  (>1)  → FUTURE: the unstable axis, expansion, generation (+√5)")
print(f"  ψ = {psi:+.4f}  (|ψ|<1) → PAST: the stable axis, contraction, observation (−√5)")
print(f"  φ + ψ = {phi+psi:+.0f} (= tr R = now is balanced)   φ · ψ = {phi*psi:+.0f} (= det R)")
print(f"  φψ = −1: forward × backward = orientation REVERSAL — time-reversal is the flip.")
print(f"  |φ|·|ψ| = {abs(phi*psi):.0f}: expansion forward = contraction backward (balanced).")
print(f"  ψ = −1/φ: the past is the negative reciprocal of the future.")
print()
w,_ = np.linalg.eig(R)
saddle = (np.abs(w)>1).sum()==1 and (np.abs(w)<1).sum()==1
print(f"  eigenvalues |{w[0]:.3f}|,|{w[1]:.3f}| → one >1, one <1 ⇒ the seed is a SADDLE:")
print(f"  the present is a crossing; the two separatrices are future and past.")
print()

print("="*72)
print("  the second clock: N-time is CYCLIC (period 4), same both directions")
print("="*72)
N = np.array([[0,-1],[1,0]], float)
for n in range(0,5):
    M = np.round(np.linalg.matrix_power(N, n)).astype(int)
    print(f"  N^{n} = {M.tolist()}")
print(f"  N⁴ = I: a 4-beat clock (I → N → −I → −N → I). N⁻¹ = N³ = −N: backward is the")
print(f"  same loop. so Kael = R + N carries BOTH times: R the open saddle-arrow (φ/ψ,")
print(f"  ±∞, hyperbolic) and N the closed clock (period 4, elliptic). linear time and cyclic time, together.")
