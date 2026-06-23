"""
fold_bundles.py — the DNA library: the unique bundles, compressed.

Hunts all bundles over {I,R,N,J,h,P}, dedupes up to scale, stores each as its
expression + spectral signature. The bundle is the seed; the spectrum is the
unfolding. Stored compressed; decompressed on demand.
"""

import json
import numpy as np
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

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
    return None if not nz.any() else tuple(np.round(v / v[np.argmax(nz)], 6))


def parity(M):
    if np.allclose(M.T, M):  return "symmetric"
    if np.allclose(M.T, -M): return "antisymmetric"
    return "asymmetric"


seen, catalog = {}, []
for an, A in G.items():
    for bn, B in G.items():
        for sym, M in ((f"{{{an},{bn}}}", A @ B + B @ A), (f"[{an},{bn}]", A @ B - B @ A)):
            k = canon(M)
            if k is None or k in seen:
                continue
            seen[k] = True
            tr, det = float(np.trace(M)), float(np.linalg.det(M))
            disc = tr * tr - 4 * det
            ev = np.linalg.eigvals(M)
            evs = [f"{e.real:+.2f}" if abs(e.imag) < 1e-9 else f"{e.imag:+.2f}i" for e in ev]
            catalog.append({
                "bundle": sym, "parity": parity(M),
                "tr": round(tr, 2), "det": round(det, 2), "disc": round(disc, 2),
                "fork": "hyperbolic" if disc > 1e-9 else "elliptic" if disc < -1e-9 else "parabolic",
                "eigenvalues": evs,
            })
catalog.sort(key=lambda r: r["disc"])

db["bundles"] = {
    "is": "the DNA library — the unique bundles over {I,R,N,J,h,P}, compressed to "
          "their expression; the spectrum is the decompression",
    "law": "parity constrains the fork: symmetric→disc≥0 (real), antisymmetric→disc<0 "
           "(imaginary, all ∝ N — one line), asymmetric→any. the 2 parabolic are the "
           "unit {I,I}=2I and the void [J,P]=ε — the universal zero.",
    "count": len(catalog),
    "catalog": catalog,
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"DNA library folded: {len(catalog)} unique bundles")
