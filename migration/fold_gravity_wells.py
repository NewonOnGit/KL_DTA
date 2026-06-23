"""
fold_gravity_wells.py — the gravity wells: the fold's fixed points.

Idempotents X²=X: 0, I, and the rank-1 manifold P_(v,w)=v·wᵀ/(wᵀv) (ℝP¹×ℝP¹).
ALL have spectrum {1,0} (identical light) but distinct geometry — gravity is in
the geometry, the spectrum is degenerate across the wells. generic wells are
complex; P is a rare simple one (the 2 in w).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["gravity_wells_are_idempotents"] = {
    "id": "gravity_wells_are_idempotents",
    "title": "The gravity wells: idempotent fixed points — a complex manifold, identical light, distinct geometry",
    "section": "gauged_fold", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "vacua_idempotents"],
        "links": ["vacua_idempotents", "geometry_gravity_spectra_light", "what_fixes_the_seed",
                  "flow_strata", "two_information_types"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "DEFECT", "BASE"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 3, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "fixed points of M(X)=X² are the idempotents: 0, I, and rank-1 projectors P_(v,w)=v·wᵀ/(wᵀv) — the gravity wells, a 2-param manifold ℝP¹×ℝP¹. ALL share spectrum {1,0} (identical light, degenerate) but differ in geometry (v,w) — gravity is the geometry; the spectrum can't tell wells apart. generic wells are COMPLEX (irrational); P=P_([0,1],[2,1]) is a rare simple well, the 2 in w (the kernel covector)"},
    },
}

db.setdefault("physics", {})["gravity_wells"] = {
    "are": "the idempotents X²=X — fixed points of the fold; 0, I, and the rank-1 manifold ℝP¹×ℝP¹",
    "spectrum": "all rank-1 wells have eigenvalues {1,0} — light is DEGENERATE across the manifold",
    "geometry": "the wells differ only in (image v, kernel ⊥w) — gravity is in the geometry alone",
    "complex": "generic wells are irrational; 0, I, P are the rare simple ones. P = v=[0,1], w=[2,1]",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("gravity wells folded. base now", len(db["base"]))
