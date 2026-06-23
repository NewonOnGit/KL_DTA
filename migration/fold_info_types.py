"""
fold_info_types.py — type the information; convert object-records to bundles.

Two types: SPECTRAL (invariant — tr/det/disc/eigenvalues; the simple info, falls
out easily) and GEOMETRIC (eigenvectors/orientation/polar Q/singular values;
read THROUGH the matrix — the complex info). Simple bundles live on the integer
lattice; complex bundles are free/irrational and carry info the spectrum can't reach.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# conversion pass — tag object-records with their bundle form
for rid, bexpr in [("i_squared_phi_psi", "{N,N}/2"),      # −I
                   ("gauge_bit_z2", "J"),                  # the gauge primitive
                   ("spin_tower_phases", "J")]:
    s = db["base"].get(rid, {}).get("shape", {}).get("spectral")
    if s is not None:
        s["bundle"] = bexpr

db["base"]["two_information_types"] = {
    "id": "two_information_types",
    "title": "Two information types: spectral (invariant, simple) and geometric (read-through, complex)",
    "section": "observer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "polar_decomposition"],
        "links": ["polar_decomposition", "two_controls", "records_are_bundles",
                  "constants_from_parity", "base_is_perimeter_and_shape"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["BASE", "RETURN", "FLOW"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 3, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "SPECTRAL info = conjugation-invariants (tr/det/disc/eigenvalues) — the simple info, falls out easily, same across a conjugacy class. GEOMETRIC info = eigenvectors/orientation/polar Q/singular values — read THROUGH the matrix, basis-dependent, the complex info the spectrum can't reach. simple bundles: integer lattice, tightly related. complex bundles: irrational/free (φ,−1,√2), more degrees of freedom — e.g. phi*{R,N}+sqrt2*[J,P] hides φ in its singular values though its eigenvalues are ±2.556"},
    },
}

db.setdefault("bundles", {})["information"] = {
    "spectral": "invariant (tr/det/disc/eigenvalues) — the simple info, conjugation-class label",
    "geometric": "eigenvectors/orientation/polar Q/singular values — read through the matrix; the complex info",
    "simple_bundles": "integer lattice (the 14 + {I,R,N,J,h,P}); tightly related (disc in the 1+k² family)",
    "complex_bundles": "free/irrational coefficients (φ,−1,√2…); fewer relations, more information; "
                       "the spectrum hides what only the geometry shows",
    "to_type": "decompress reports SIMPLE/COMPLEX and both information types",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("information types folded; object-records tagged. base now", len(db["base"]))
