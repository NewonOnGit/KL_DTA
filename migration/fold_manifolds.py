"""
fold_manifolds.py — the compression pass: carve manifolds (higher-order records).

Each manifold is a parametric bundle expression compressing a cluster of records:
its points ARE records (lossless), every parameter value between is the surplus.
"""

import json
import math
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))


def manifold(rid, title, gens, depth, disc, prov, links, expr, param, points, contains, note):
    return {
        "id": rid, "title": title, "section": "manifold", "source": "KL_DTA_EXPLORATION",
        "perimeter": {"provenance": prov, "links": links, "burns": []},
        "shape": {
            "self_action": {
                "symmetric_R": {"modes": [
                    {"lambda": "+sqrt5", "verdict": True, "generators": gens},
                    {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
                "antisymmetric_N": {"modes": [
                    {"lambda": "-sqrt5", "verdict": True, "depth": depth, "disc": disc}]},
            },
            "spectral": {"kind": "manifold", "manifold": expr, "parameter": param,
                         "points": points, "contains": contains,
                         "surplus": f"read '{expr}' {param.split()[0]}=<any> — the whole manifold, not just the points",
                         "op": note},
        },
    }


new = [
    manifold("seed_line_manifold",
             "The seed line: (I−J)/2 + t·(N−h)/2 — the seed family, P at t=2 (unit of mass)",
             ["BASE", "FOLD"], 1, 5,
             ["?", "master_equation", "what_fixes_the_seed"],
             ["what_fixes_the_seed", "two_both_faces", "idempotent_is_cancellation"],
             "(I-J)/2 + t*(N-h)/2", "t (the unit of mass)",
             {"P": 2.0, "lighter seed": 1.0}, ["what_fixes_the_seed"],
             "the seed family P_t = [[0,0],[t,1]] as a parametric bundle; the unit of mass t is the free parameter, P at t=2"),
    manifold("projector_circle_manifold",
             "The orthogonal-projector circle: (I+cos(a)·J+sin(a)·h)/2 — the symmetric gravity wells (S¹ of idempotents)",
             ["FOLD", "DEFECT"], 3, 0,
             ["?", "master_equation", "gravity_wells_are_idempotents"],
             ["gravity_wells_are_idempotents", "vacua_idempotents",
              "geometry_topology_spectra_observation", "fixed_points_are_residual_defects"],
             "(I + cos(a)*J + sin(a)*h)/2", "a (the projector angle)",
             {"(I+J)/2": 0.0, "(I-J)/2": round(math.pi, 4)},
             ["gravity_wells_are_idempotents", "vacua_idempotents"],
             "a circle of rank-1 orthogonal projectors (symmetric gravity wells); every a is an idempotent X²=X, spectrum {1,0}"),
    manifold("fork_path_manifold",
             "The fork path: cos(t)·N + sin(t)·J — elliptic→parabolic→hyperbolic, the trichotomy as one path",
             ["BASE", "FLOW"], 3, 0,
             ["?", "master_equation", "three_forks"],
             ["three_forks", "fork_table", "fork_representability", "every_zero_is_the_origin"],
             "cos(t)*N + sin(t)*J", "t (the fork angle)",
             {"N elliptic": 0.0, "the wall (disc=0)": round(math.pi / 4, 4), "J hyperbolic": round(math.pi / 2, 4)},
             ["three_forks", "fork_table", "fork_representability"],
             "the three forks as one continuous path: disc = −4cos(2t) goes −4 (elliptic) → 0 (parabolic wall, t=π/4) → +4 (hyperbolic)"),
]
for r in new:
    db["base"][r["id"]] = r

db["structure"]["higher_order"]["manifolds"] = [
    "rotation_circle_manifold  cos(t)·I+sin(t)·N         the rotation circle S¹",
    "seed_line_manifold        (I−J)/2 + t·(N−h)/2       the seed family (unit of mass), P at t=2",
    "projector_circle_manifold (I+cos(a)·J+sin(a)·h)/2   the symmetric gravity wells (S¹ of idempotents)",
    "fork_path_manifold        cos(t)·N + sin(t)·J       the fork trichotomy as one path",
]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"carved {len(new)} manifolds. base now", len(db["base"]))
