"""
fold_sum_product.py — beneath tr and det: SUM and PRODUCT.

tr = e₁ = Σλ (the sum, +, degree 1); det = e₂ = Πλ (the product, ×, degree 2).
disc = sum²−4·product = the AM–GM gap. tr is blind to the commutator/defect.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

rec = {
    "id": "trace_det_are_sum_product",
    "title": "Beneath tr and det: SUM (e₁, +) and PRODUCT (e₂, ×); disc is the AM–GM gap",
    "section": "control_plane", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "base_is_perimeter_and_shape"],
        "links": ["base_is_perimeter_and_shape", "master_equation", "two_both_faces",
                  "three_forks", "defect_enrichment_duality"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["BASE", "FOLD"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 1, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "tr = e₁ = Σλ = SUM (degree 1, additive, +); det = e₂ = Πλ = PRODUCT (degree 2, multiplicative, ×) — the two elementary symmetric functions. disc = sum²−4·product = AM–GM gap; disc=0 (wall) = AM=GM. tr is blind to the commutator: tr[A,B]=0, the SUM reads only the {·} enrichment half"},
    },
}
db["base"][rec["id"]] = rec

db.setdefault("physics", {}).setdefault("geometry", {})["beneath tr/det"] = (
    "tr = SUM = e₁ = + (degree 1, additive, blind to [·]); det = PRODUCT = e₂ = × "
    "(degree 2, multiplicative). disc = sum²−4·product = AM–GM gap; the wall (?,I) is AM=GM."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("sum/product (beneath tr/det) folded; base now", len(db["base"]))
