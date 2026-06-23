"""
fold_fixed_unfix.py — fixed points are recursive residual defects; unfix them.

Fixed points of M(X)=X² = idempotents (0, I rigid; the rank-1 torus slides) — where
ν recursively settled to 0. Unfix: ν(X+εδ)=ε·L_{X,X}(δ); ker L = tangent (stays
fixed), the rest = unfixing directions (thaw the defect). The `unfix` command sorts them.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["fixed_points_are_residual_defects"] = {
    "id": "fixed_points_are_residual_defects",
    "title": "Fixed points are recursive residual defects; unfix sorts tangent from unfixing via L_{X,X}",
    "section": "gauged_fold", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "gravity_wells_are_idempotents"],
        "links": ["gravity_wells_are_idempotents", "vacua_idempotents", "defect_nu",
                  "flow_strata", "two_self_actions"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "DEFECT", "FLOW"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 3, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "ALL fixed points of M(X)=X² are the idempotents: 0 and I (isolated, rigid, tangent dim 0), and the rank-1 torus ℝP¹×ℝP¹ (tangent dim 2, slides). they are recursive residual defects — where ν=X²−X settled to 0. UNFIX: ν(X+εδ)=ε·L_{X,X}(δ); ker L_{X,X}=tangent (stays fixed), the rest=unfixing directions (thaw ν≠0). L_(rank-1) spectrum {−1,0,0,1}: 2 tangent + 2 unfixing. unfixing gives the residual back — runs the recursion backward. (engine: `unfix`)"},
    },
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("fixed-points/unfix folded. base now", len(db["base"]))
