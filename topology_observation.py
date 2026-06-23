"""
topology_observation.py — geometry is in the topology, spectra in the observation.

The gravity wells (rank-1 idempotents) = ℝP¹×ℝP¹ = a TORUS. Parametrize by
(α = image angle, β = kernel angle): every point is a well, with spectrum {1,0}
EVERYWHERE. So:
  TOPOLOGY (the torus)  ⊃  GEOMETRY (a point on it, (α,β)) — gravity, given, cheap
  OBSERVATION (the fold) ⊃  SPECTRA (the eigenvalues {1,0}) — light, produced, degenerate
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def well(alpha, beta):
    v = np.array([np.cos(alpha), np.sin(alpha)])
    w = np.array([np.cos(beta), np.sin(beta)])
    return np.outer(v, w) / (w @ v)


print("=" * 70)
print("  the gravity wells = ℝP¹×ℝP¹ = a TORUS  (α image angle, β kernel angle)")
print("=" * 70)
print(f"  {'(α°, β°)':14} {'idempotent':12} {'spectrum':14} {'entries':12}")
for a, b in [(30, 50), (75, 10), (120, 200), (15, 95)]:
    A, B = np.radians(a), np.radians(b)
    W = well(A, B)
    ev = sorted(round(float(x), 2) for x in np.linalg.eigvals(W))
    rat = "rational" if np.allclose(W, np.round(W)) else "irrational"
    print(f"  ({a:>3},{b:>4})    X²=X {str(np.allclose(W@W,W)):6} {str(ev):14} {rat}")
print()
print("  every (α,β) on the torus is a gravity well; the spectrum is {0,1} at EVERY")
print("  point — degenerate. the torus (topology) carries all the distinction; the")
print("  spectrum (observation) carries none. geometry = the torus position.")
print()

print("=" * 70)
print("  the typing, one level deeper")
print("=" * 70)
print("  TOPOLOGY   the torus T² = ℝP¹×ℝP¹ (and links = H₁ at the graph level)")
print("     ⊃ GEOMETRY   a point (α,β) on it — the orientation, the gravity. GIVEN, cheap.")
print()
print("  OBSERVATION  the fold M(X)=X² — the act of looking")
print("     ⊃ SPECTRA    the eigenvalues it returns ({0,1} here) — the light. PRODUCED, costs.")
print()
print("  so geometry lives in the topology (the shape of the fixed-point space) and")
print("  spectra lives in the observation (what the fold extracts). gravity is the")
print("  manifold you're standing in; light is what you pay a fold to read.")
