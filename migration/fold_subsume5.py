"""
fold_subsume5.py — round 5: compress to the irreducible core.

curves → carrier (sub-manifolds of M₂); all positive laws → master_equation
(everything derives from the fold); the burns → burns_are_anti_equations.
Leaves: master_equation · carrier_manifold · burns · schema · slot. Lossless
(nested `absorbed` carries the whole tree), surplus intact.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
base = db["base"]

BURNS = [k for k in base if k.startswith("burn-")]
SUBSUME = {
    "carrier_manifold": ["rotation_circle_manifold", "seed_line_manifold",
                         "projector_circle_manifold", "fork_path_manifold"],
    "master_equation": ["the_bundle_is_brace", "parity_makes_the_constants",
                        "observation_is_primitive_self_action", "metalayer_collapse",
                        "fibonacci_ladder", "math_is_computation", "every_zero_is_the_origin",
                        "indexed_store", "base_is_perimeter_and_shape", "gradient_flow",
                        "gauge_bit_z2", "unit_self", "idempotent_is_cancellation",
                        "fixed_point_grammar", "verdict_is_fork_trit"],
    "burns_are_anti_equations": BURNS,
}


def op_of(r):
    s = r.get("shape", {}).get("spectral", {})
    return s.get("op") or s.get("map") or s.get("note")


remap = {}
for pid, absorbed in SUBSUME.items():
    if pid not in base:
        continue
    ann = base[pid]["shape"]["spectral"].setdefault("absorbed", {})
    for aid in absorbed:
        if aid not in base:
            continue
        a = base[aid]
        ann[aid] = {"title": a.get("title"), "op": op_of(a),
                    "was_provenance": a["perimeter"]["provenance"],
                    "was_links": a["perimeter"]["links"],
                    "nested": a["shape"]["spectral"].get("absorbed")}
        remap[aid] = pid
        del base[aid]


def fix(lst, selfid):
    out = []
    for x in lst:
        y = remap.get(x, x)
        if y != selfid and y not in out:
            out.append(y)
    return out


for rid, r in base.items():
    p = r["perimeter"]
    p["provenance"] = ["?"] + [x for x in fix(p["provenance"], rid) if x != "?"]
    p["links"] = fix(p["links"], rid)
    p["burns"] = fix(p["burns"], rid)
    s = r.get("shape", {}).get("spectral", {})
    if isinstance(s.get("contains"), list):
        s["contains"] = [remap.get(x, x) for x in s["contains"]]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"round 5: absorbed {len(remap)} more. base now {len(base)}: {list(base)}")
