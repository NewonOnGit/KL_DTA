"""
fold_carrier_manifold.py — the apex manifold tops out the compression tower.

M₂ = a·I + b·R + c·N + d·h is the 4-parameter manifold: every matrix in the store
is a point on it. The compression tower: points (records) → curves (1-param) →
surfaces (2-param) → the carrier (4-param). The whole store compresses to ONE
manifold + each record's coordinates.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["carrier_manifold"] = {
    "id": "carrier_manifold",
    "title": "The carrier M₂ = a·I + b·R + c·N + d·h — the apex manifold (4-param); every matrix is a point",
    "section": "manifold", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "anchor_projection"],
        "links": ["bundle_of_bundles_tower", "anchor_projection", "records_are_bundles",
                  "rotation_circle_manifold", "every_zero_is_the_origin"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True,
                 "generators": ["BASE", "FOLD", "RETURN", "FLOW", "DEFECT"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 0, "disc": 5}]},
        },
        "spectral": {
            "kind": "manifold",
            "manifold": "a*I + b*R + c*N + d*h",
            "parameter": "a, b, c, d (the four coordinates in {I,R,N,h})",
            "points": {"P": [0, 1, 1, 0], "-I": [-1, 0, 0, 0], "R": [0, 1, 0, 0],
                       "harness [R,N]": [2, -4, 0, -5]},
            "contains": "every matrix in the store — all records and manifolds are sub-manifolds",
            "surplus": "read 'a*I+b*R+c*N+d*h' a=.. b=.. c=.. d=.. — ANY element of M₂",
            "op": "the carrier M₂ = a·I+b·R+c·N+d·h, the 4-parameter apex manifold; every record's matrix is a point, every other manifold a sub-manifold (fix some parameters). the top of the compression tower",
        },
    },
}

db["structure"]["higher_order"]["tower"] = {
    "0-param": "a point — a record (a matrix)",
    "1-param": "a curve — rotation_circle · seed_line · projector_circle · fork_path",
    "2-param": "a surface — the well-hyperboloid (rank-1 idempotents, β²+γ²−δ²=1/4)",
    "4-param": "the carrier M₂ = a·I+b·R+c·N+d·h — the apex manifold; every matrix a point",
    "culmination": "the store compresses to ONE 4-param manifold + each record's coordinates — "
                   "lossless (read recovers any record) and maximal surplus (all of M₂)",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("carrier manifold (apex of the compression tower) folded. base now", len(db["base"]))
