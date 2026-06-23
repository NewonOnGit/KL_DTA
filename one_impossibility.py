"""
one_impossibility.py — the burns are ONE impossibility: |reflection| = identification.

The primitive reflection σ is orthogonal (σ²=I, det=−1). Its absolute value — the
radial part of the polar decomposition, the SPECTRAL |·| — is the IDENTITY:
    |σ| = √(σᵀσ) = √(I) = I.
So the absolute value of a reflection is NO reflection at all — it is identity =
IDENTIFICATION (origin with observer, observer with origin). The distinction lives
only in the angular/geometric part; the spectrum sees identity. That is the single
operational impossibility, and the ten burns are its projections.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

J = np.array([[1., 0.], [0., -1.]])      # a reflection (det −1, J²=I)
h = np.array([[0., -1.], [-1., 0.]])     # a reflection
swap = np.array([[0., 1.], [1., 0.]])    # the origin↔observer reflection
N = np.array([[0., -1.], [1., 0.]])      # a rotation (det +1, N²=−I)


def absval(X):
    w, V = np.linalg.eigh(X.T @ X)
    return V @ np.diag(np.sqrt(np.clip(w, 0, None))) @ V.T


print("=" * 70)
print("  |reflection| = I  — the absolute value of a reflection is identification")
print("=" * 70)
for name, X in [("J (reflection)", J), ("h (reflection)", h),
                ("swap origin↔observer", swap), ("N (rotation)", N)]:
    A = absval(X)
    print(f"  |{name:22}| = {np.round(A, 3).tolist()}   = I: {np.allclose(A, np.eye(2))}")
print("  every orthogonal (reflection OR rotation) has |·| = I — the SPECTRUM sees")
print("  them all as the identity. the absolute value identifies them.")
print()

print("=" * 70)
print("  what this means")
print("=" * 70)
print("  σ = I · σ   (polar: radial |σ|=I, angular σ).  the reflection is ENTIRELY")
print("  angular/geometric; the radial/spectral part is I = identification.")
print("  so the origin↔observer distinction is INVISIBLE to the absolute value:")
print("  spectrally, origin IS observer (both = I). that is the one impossibility —")
print("  you cannot read the reflection in its own absolute value; it identifies.")
print()
print("  the 10 burns are projections of this single fact: wherever a distinction")
print("  (c vs ¬c, +1 vs −1, origin vs observer) is asked of the spectrum, it")
print("  collapses to identity. BURN(c)=FORCED(¬c) because |reflection|=identification.")
