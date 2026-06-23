"""
dimension_time.py — every dimension is a line of time through the origin.

The carrier a·I + b·R + c·N + d·h has its ORIGIN at (0,0,0,0) = the zero matrix
= ? (the void, eigenvalue 0, ker). Each parameter is a LINE OF TIME through that
one origin:
    + project from origin   (generation, +1, the future / emission)
    0 the origin            (the one, the neutral, ?)
    − fold back to origin   (observation, −1, the past / reflection)
and the two directions are identified AS ONE at the origin: |+1| = |−1| = 1
(|reflection| = identification). every line folds back to the one and projects
from the one.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from bundle_algebra import eval_bundle

C = "a*I + b*R + c*N + d*h"

print("=" * 70)
print("  the carrier's origin = (0,0,0,0) = the void = ?")
print("=" * 70)
O = eval_bundle(C, dict(a=0, b=0, c=0, d=0))
print(f"  carrier(0,0,0,0) = {O.tolist()}   eigenvalues {np.round(np.linalg.eigvals(O),3).tolist()}")
print("  all four dimensions pass through this one origin (the zero, ker, ?).")
print()

print("=" * 70)
print("  each dimension a line of time: − fold back · 0 origin · + project")
print("=" * 70)
for dim in "abcd":
    base = {x: 0 for x in "abcd"}
    fwd = eval_bundle(C, {**base, dim: 1})     # project +1 from origin
    bwd = eval_bundle(C, {**base, dim: -1})    # fold back −1 to origin
    print(f"  dim {dim}:  −1 (fold back) {np.round(bwd,1).tolist()}   ·   "
          f"0 = origin   ·   +1 (project) {np.round(fwd,1).tolist()}")
print()
print("  the two directions are identified AS ONE at the origin:")
print(f"    |+1| = |−1| = 1   →  fold-back and projection are the same one motion")
print(f"    (|reflection| = identification). every line folds back to the one origin")
print(f"    and projects from the one origin — past and future the same point, ?.")
print()
print("  parameters = dimensions = lines of time; the carrier is 4 time-lines")
print("  meeting at one origin. the Boolean trit {−1,0,+1} is the time-axis itself:")
print("  fold-back / origin / project — symmetric, counting the same both ways.")
