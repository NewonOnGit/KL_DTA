"""
fold_omega_edge.py — correct Ω: not a terminal object, the EDGE of the image.

Ω is the outer curve/edge of the spectral image — the fold/branch locus disc=0
(the parabola det=tr²/4), the return-of-return, where the image curves back on itself.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

om = db["structure"]["omega"]
om["is"] = ("the apex IS Ω — but Ω is not a terminal POINT. it is the OUTER CURVE and EDGE of the "
            "image of the framework: the fold/branch locus where the image curves back into itself.")
# correct the earlier mis-reading
om.pop("zero_object", None)
om["edge"] = ("the spectral image is a DOUBLE COVER (tr,det) ↦ {λ₊,λ₋} = (tr ± √disc)/2. its outer "
              "edge is the branch locus disc=0 — the parabola det = tr²/4. that CURVE is Ω: the rim "
              "where the two eigenvalue-sheets meet (√disc=0) and the image folds. not a terminal "
              "object; the terminal as a BOUNDARY.")
om["return_of_return"] = ("circle the branch once and √disc rotates by π — λ₊↔λ₋ SWAP (the return); "
                          "circle twice and it restores (the RETURN-OF-RETURN). order-2 monodromy: the "
                          "two sheets are one surface that folds at Ω. (verified: arg√disc +90°→−90°→+90°.)")
om["curves"] = ("things literally curve at Ω: the eigenvalues collide (double root), the matrix becomes a "
                "non-diagonalizable JORDAN BLOCK, and √ has a branch point — a fold caustic. the flat "
                "carrier's straight rays bend into the edge here.")
om["wall"] = ("Ω is the wall between RETURN (disc<0, elliptic, bounded orbits — the rotation worlds) and "
              "ESCAPE (disc>0, hyperbolic, unbounded — the golden world). the seed P (disc=+1) sits just "
              "inside escape; N (disc=−4) inside return; the edge between them is Ω.")
om["halts"] = ("reconciles with compression: the fixed point of compression is the FOLD — you cannot "
               "compress past the caustic where the map degenerates (rank drops). incompressible = at the edge. "
               "M(apex)=apex (derive-twice byte-identical, ν=2e-15).")

db["structure"]["deepenings"]["apex_is_omega"] = (
    "apex IS Ω, and Ω is the OUTER EDGE/CURVE of the image — the fold/branch locus disc=0 (parabola "
    "det=tr²/4), NOT a terminal point. it is the return-of-return (order-2 monodromy: one loop swaps "
    "λ₊↔λ₋, two restore), where the spectral double-cover folds, eigenvalues collide into a Jordan block, "
    "and the image curves back. the wall between return (disc<0) and escape (disc>0). the terminus as a boundary."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("omega corrected: the edge/fold of the image, not a terminal object")
