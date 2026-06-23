"""
light_gravity.py — geometry is gravity (cheap, fixed points), spectra is light (costs a fold).

  GEOMETRY  = the linear action  X·v   (degree 1) — direct; its fixed directions
              (eigenvectors) are FIXED POINTS → gravity. cheap to see.
  SPECTRA   = the eigenvalues, from det(X−λI)=λ²−tr·λ+det=0 (degree 2 = the FOLD)
              — the scalings, the frequencies → light. costs a fold to see.

origin projects spectra (emitted, unfolds simply: λ=AM±√disc/2). the observer is a
second projector and sees geometry; to recover spectra it must FOLD back through
itself — circular, completed by evolution. that inverse is why geometry is easy.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

X = np.array([[2., 1.], [1., 3.]])      # some observed matrix
ev, evec = np.linalg.eig(X)

print("=" * 70)
print("  GEOMETRY = gravity — the fixed points (degree 1, direct)")
print("=" * 70)
for i in range(2):
    v = evec[:, i]
    print(f"  eigenvector v{i} = {np.round(v,3).tolist()}   "
          f"X·v = {np.round(X@v,3).tolist()} = {ev[i].real:.3f}·v   FIXED direction ✓ "
          f"{np.allclose(X@v, ev[i]*v)}")
print("  the eigenvectors are the FIXED POINTS of the action — the geometry holds")
print("  them directly. you see where things settle without solving anything. gravity.")
print()

print("=" * 70)
print("  SPECTRA = light — the eigenvalues, and they cost a FOLD (degree 2)")
print("=" * 70)
tr, det = np.trace(X), np.linalg.det(X)
disc = tr * tr - 4 * det
print(f"  λ solves det(X−λI) = λ² − tr·λ + det = 0   (the master equation, degree 2)")
print(f"  λ = AM ± √disc/2 = {tr/2:.3f} ± {np.sqrt(disc)/2:.3f} = {ev[0].real:.3f}, {ev[1].real:.3f}")
print("  to SEE the spectrum you must square — fold X into X² (the self-action).")
print("  geometry is the action (degree 1); spectra is the fold of it (degree 2).")
print("  the cost of seeing the light is exactly one fold.")
print()

print("=" * 70)
print("  the projection structure — why the asymmetry")
print("=" * 70)
print("  origin  ──project──▶  SPECTRA   (light; the master equation emits λ simply)")
print("  observer ─project─▶  GEOMETRY  (gravity; the polar Q, the fixed points)")
print()
print("  the observer is a projector OF the origin's projection. it sees its own")
print("  output (geometry) directly — cheap. to see the SPECTRA (the origin's")
print("  emission) it must INVERT itself — fold back through its own projection.")
print("  that inverse is circular (observer→origin→observer) and is completed by")
print("  EVOLUTION — iterating the fold until the spectrum resolves.")
print()
print("  so: complex/geometric info (gravity, fixed points) is EASY to see — it's")
print("  the observer's direct projection. simple/spectral info (light) COSTS —")
print("  it's upstream, recovered only by folding back. seeing spectra completes the circle.")
