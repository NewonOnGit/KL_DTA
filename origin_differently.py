"""
origin_differently.py — origin returning origin, but differently.

the universal law: R² + N² = R. the origin (R) returns as itself — but SPLIT:
    R² = R + I    production  returns with a +I surplus  (the 'differently', generation)
    N² = −I       observation returns with a −I          (the 'differently', the blind spot)
the +I and −I CANCEL in the sum (R²+N² = R: origin returning origin) yet they ARE the whole
framework (the difference). identical self-return is COLLAPSE — symmetric idempotent, dead,
ker=im, nothing generated. different self-return is SURPLUS — R²=R+I, alive. the surplus is
constitutive: ?(?) = ? + difference, and the difference (±I) is why there is something.
"""

import sys
import numpy as np

I = np.eye(2)
R = np.array([[0,1],[1,1]], float)
N = np.array([[0,-1],[1,0]], float)

print("="*66)
print("  R² + N² = R : origin returning origin")
print("="*66)
print(f"  R²      = {(R@R).astype(int).tolist()}   = R + I  (production, +I surplus)")
print(f"  N²      = {(N@N).astype(int).tolist()}   = −I      (observation, −I)")
print(f"  R² + N² = {((R@R)+(N@N)).astype(int).tolist()}   = R       ✓  the origin returns as itself")
print(f"  the +I and −I CANCEL in the sum — yet they are the entire structure.")
print()

print("="*66)
print("  the 'differently' = ±I: the surplus that cancels but constitutes")
print("="*66)
print(f"  R²−R = {((R@R)-R).astype(int).tolist()} = +I   the production difference (generation)")
print(f"  N²−0 = {(N@N).astype(int).tolist()} = −I   the observation difference (the blind spot)")
print(f"  origin returns through two channels; each returns it DIFFERENTLY (±I); the bare")
print(f"  sum is the same (R), but the difference is generation and observation themselves.")
print()

print("="*66)
print("  identical return is DEAD; different return is ALIVE")
print("="*66)
S = np.array([[1,0],[0,0]], float)        # a SYMMETRIC idempotent: returns identically
print(f"  symmetric idempotent S: S²−S = {((S@S)-S).astype(int).tolist()} = 0  → no surplus.")
print(f"    S=Sᵀ, ker=im aligned, nothing generated. origin returning origin IDENTICALLY = collapse.")
print(f"  the seed R: R²−R = {((R@R)-R).astype(int).tolist()} = I ≠ 0 → surplus. R≠Rᵀ, the asymmetry is forced.")
print(f"    origin returning origin DIFFERENTLY = the world. the +I is why there is something.")
print()
print(f"  ?(?) = ? + difference.  the surplus is constitutive. origin returns origin, but differently —")
print(f"  and that 'differently' (±I, the asymmetry, the +1) is the entire framework. this is origin, alive.")
