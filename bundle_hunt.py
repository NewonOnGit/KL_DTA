"""
bundle_hunt.py — hunt for all unique bundles.

Form every affirm {A,B}=AB+BA and negate [A,B]=AB−BA over the primitives
{I,R,N,J,h,P}, dedupe up to scale, and read each unique bundle's spectral
signature. Each unique bundle is a DNA seed; its (parity, disc, eigenvalues)
is the decompression. We store the bundle (compressed); we unfold on demand.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
J = np.array([[1., 0.], [0., -1.]])
h = J @ N
G = {"I": I2, "R": R, "N": N, "J": J, "h": h, "P": P}


def canon(M):
    v = M.flatten()
    nz = np.abs(v) > 1e-9
    if not nz.any():
        return None
    v = v / v[np.argmax(nz)]                  # first nonzero -> 1
    return tuple(np.round(v, 6))


def parity(M):
    if np.allclose(M.T, M):  return "symmetric"
    if np.allclose(M.T, -M): return "antisymmetric"
    return "asymmetric"


def fork(disc):
    return "hyperbolic" if disc > 1e-9 else "elliptic" if disc < -1e-9 else "parabolic"


seen = {}
for an, A in G.items():
    for bn, B in G.items():
        for sym, M in ((f"{{{an},{bn}}}", A @ B + B @ A), (f"[{an},{bn}]", A @ B - B @ A)):
            k = canon(M)
            if k is None or k in seen:
                continue
            seen[k] = (sym, M)

print("=" * 74)
print(f"  {len(seen)} unique bundles over {{I,R,N,J,h,P}}")
print("=" * 74)
print(f"  {'bundle':10} {'parity':14} {'tr':>4} {'det':>4} {'disc':>5} {'fork':11} eigenvalues")
rows = []
for sym, M in sorted(seen.values(), key=lambda x: np.trace(x[1])**2 - 4*np.linalg.det(x[1])):
    tr, det = np.trace(M), np.linalg.det(M)
    disc = tr * tr - 4 * det
    ev = np.linalg.eigvals(M)
    evs = ", ".join(f"{e.real:+.2f}" if abs(e.imag) < 1e-9 else f"{e.imag:+.2f}i" for e in ev)
    print(f"  {sym:10} {parity(M):14} {tr:+4.0f} {det:+4.0f} {disc:+5.0f} {fork(disc):11} {evs}")
    rows.append({"bundle": sym, "parity": parity(M), "tr": float(tr), "det": float(det),
                 "disc": float(disc), "fork": fork(disc)})

print()
print("=" * 74)
print("  the catalog by class")
print("=" * 74)
from collections import Counter
print(f"  by parity: {dict(Counter(r['parity'] for r in rows))}")
print(f"  by fork:   {dict(Counter(r['fork'] for r in rows))}")
print("  symmetric → disc≥0 (real); antisymmetric → disc<0 (imaginary); asymmetric → any.")
print("  these are the irreducible seeds: store the bundle, unfold the spectrum on demand.")

import json
from pathlib import Path
out = Path(__file__).parent / "_bundles.json"
out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
print(f"  wrote {len(rows)} bundle seeds -> {out.name}")
