"""
fold_rotation_circle.py — the first higher-order record: a manifold.

A manifold IS a parametric bundle expression. The rotation circle S¹ =
cos(t)·I + sin(t)·N compresses the rotation-content records into one object:
  LOSSLESS  its points ARE records — I (t=0), N (t=π/2), −I (t=π, = i_squared_phi_psi)
  SURPLUS   read any t — the whole circle, every rotation between the points
"""

import json
import math
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["rotation_circle_manifold"] = {
    "id": "rotation_circle_manifold",
    "title": "The rotation circle S¹: cos(t)·I + sin(t)·N — a higher-order manifold record",
    "section": "manifold", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "spin_tower_phases"],
        "links": ["i_squared_phi_psi", "spin_tower_phases", "observer_dynamics",
                  "observation_is_primitive_self_action", "constants_from_parity"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FLOW", "RETURN", "FOLD"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 2, "disc": -4}]},
        },
        "spectral": {
            "kind": "manifold",
            "manifold": "cos(t)*I + sin(t)*N",
            "parameter": "t ∈ [0, 2π), period 2π → π",
            "points": {"I": 0.0, "N": round(math.pi / 2, 4),
                       "-I (= i_squared_phi_psi)": round(math.pi, 4),
                       "-N": round(3 * math.pi / 2, 4)},
            "contains": ["i_squared_phi_psi", "spin_tower_phases"],
            "surplus": "read 'cos(t)*I+sin(t)*N' t=<any> — the whole circle, not just the points",
            "op": "the rotation circle S¹ = exp(t·N) = cos(t)·I + sin(t)·N — a manifold (parametric bundle); its points are records (lossless), every t between is the surplus",
        },
    },
}

db.setdefault("structure", {})["higher_order"] = {
    "is": "a manifold IS a parametric bundle expression — a higher-order record",
    "lossless": "the stored records are POINTS on it (fix the parameter to recover each)",
    "surplus": "read/unfix at any parameter value — the whole continuum, not just the points",
    "first": "rotation_circle_manifold = cos(t)·I + sin(t)·N (S¹); -I at t=π is i_squared_phi_psi",
    "standard": "compression must add functionality (R²=R+I) or it failed (R(R)=R)",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("first higher-order record (rotation circle manifold) folded. base now", len(db["base"]))
