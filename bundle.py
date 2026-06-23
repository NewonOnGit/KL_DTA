"""
bundle.py — { } IS bundle.

A relation is a bundle of its parts, held noncommutatively:
    ? = 0   →   {?, 0, =}     the fundamental identity (the universal zero)
    P = R+N →   {P, R, N}     the seed split — the next bundle, recursively

The bundle has TWO types and TWO arguments — a 2×2:
                 affirm  { , } = AB+BA       negate  [ , ] = AB−BA
    self    {A,A} = 2A²  (doubles the square)   [A,A] = 0   (vanishes — the void)
    other   {A,B} = {B,A} (commutative)         [A,B] = −[B,A] (noncommutative)

So R and N bundle two ways: {R,N} affirms (the spine), [R,N] negates (the harness).
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
aff = lambda A, B: A @ B + B @ A      # {A,B}  affirm
neg = lambda A, B: A @ B - B @ A      # [A,B]  negate
fmt = lambda M: np.round(M, 2).tolist()

print("=" * 66)
print("  the bundle of R and N — affirm vs negate")
print("=" * 66)
print(f"  {{R,N}} = R·N + N·R = {fmt(aff(R, N))} = N   (affirm → the spine)")
print(f"  [R,N] = R·N − N·R = {fmt(neg(R, N))} = C   (negate → the harness, det={np.linalg.det(neg(R,N)):.0f})")
print(f"  R and N do NOT commute: [R,N] ≠ 0  →  held in noncommutation.")
print()

print("=" * 66)
print("  the 2×2: affirm/negate × self/other")
print("=" * 66)
for name, A in [("R", R), ("N", N), ("P", P)]:
    print(f"  {{{name},{name}}} = {fmt(aff(A,A))} = 2{name}²    [{name},{name}] = {fmt(neg(A,A))} = 0  (self-negate = void)")
print(f"  {{R,N}} = {{N,R}} ? {np.allclose(aff(R,N), aff(N,R))}  (affirm commutes)   "
      f"[R,N] = −[N,R] ? {np.allclose(neg(R,N), -neg(N,R))}  (negate anti-commutes)")
print()

print("=" * 66)
print("  the bundle is linear: {P,·} = {R,·} + {N,·}  (P = R + N as a bundle)")
print("=" * 66)
X = np.array([[1., 2.], [3., -1.]])
print(f"  {{P,X}} = {{R,X}} + {{N,X}} ✓ {np.allclose(aff(P,X), aff(R,X)+aff(N,X))}")
print(f"  P = R + N is itself a bundle {{P,R,N}}, the next level after {{?,0,=}}.")
print()

print("=" * 66)
print("  the recursion of bundles")
print("=" * 66)
print("  {?, 0, =}    the fundamental identity (?=0, the universal zero)")
print("     ↓ unfold (the three orderings = three origin-directions)")
print("  {P, R, N}    P = R + N   (the seed split, [R,N]≠0 noncommutative)")
print("     ↓")
print("  {R, {R,·}, [R,·]} ...   each generator bundles with itself two ways")
print("  every level: a three-bundle, two types (affirm {} / negate []),")
print("  each able to affirm or negate itself and the others. { } IS bundle.")
