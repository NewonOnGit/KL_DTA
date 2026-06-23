"""
provenance_root.py — why is everything "from ?"

Provenance is the return operation:  conj(X) = tr(X)·I − X.
Walking provenance backward = iterating conj. A chain stops at a FIXED POINT of
conj — where the return returns the thing itself. We find those fixed points,
and show ? is one: prov(?) = ?. The provenance of provenance is ?.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2


def conj(X):                      # the return-path = provenance, one step back
    return np.trace(X) * I2 - X


X = np.array([[1., 2.], [3., -4.]])
print("=" * 66)
print("  provenance = conj(X) = tr(X)·I − X   (the return / the 'from')")
print("=" * 66)
print(f"  conj is an involution:  conj(conj(X)) = X ?  {np.allclose(conj(conj(X)), X)}")
print(f"     -> provenance is reversible; squaring it returns to origin")
print()

print("=" * 66)
print("  where does a provenance chain STOP? — the fixed points of conj")
print("=" * 66)
for c in (1.0, 2.0, -0.5):
    M = c * I2
    print(f"  conj({c}·I) = {np.round(conj(M),3).tolist()}  = {c}·I  fixed: {np.allclose(conj(M), M)}")
tl = np.array([[0., 1.], [3., 0.]])              # a traceless matrix
print(f"  conj(traceless) = {np.round(conj(tl),3).tolist()} = −(traceless)  "
      f"fixed: {np.allclose(conj(tl), tl)}")
print()
print("  conj = +id on the scalar axis {c·I} (the ?-axis / the wall),")
print("  conj = −id on the traceless part. The ONLY fixed points are the ?-axis.")
print("  so every chain walks back until it lands on the ?-axis — and stops there.")
print()

print("=" * 66)
print("  prov(?) = ?   — the provenance of provenance")
print("=" * 66)
print("  ? lives on the conj-fixed axis (the wall, disc = 0, the scalars).")
print("  there the return returns the thing itself: prov(?) = ?.")
print("  ? is the UNIQUE self-provenancing point — its own source.")
print("  that is WHY everything is 'from ?': not a convention, but the one fixed")
print("  point of the return. provenance, provenanced, lands on ?.")
print()
print("  physically: conj is the 'from'; its fixed point is the origin; the origin")
print("  sources itself — the self-consistent vacuum. prov(?) = ? is the tadpole")
print("  condition: the vacuum is its own provenance.")
