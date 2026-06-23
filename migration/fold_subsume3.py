"""
fold_subsume3.py — round 3: collapse the remaining clusters into their general records.
Lossless (claims kept in `absorbed`), surplus (the general unifies), count drops hard.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
base = db["base"]

SUBSUME = {
    "metalayer_collapse": ["build_is_master_equation", "compression_not_layering",
                           "internalization_removes_trace", "verification_is_provenance"],
    "observation_is_primitive_self_action": ["observer_unifies_projections", "observer_dynamics",
                                             "witnessing_internalized", "projection_spectral_triple"],
    "fibonacci_ladder": ["power_via_index", "deposit_walk", "return_axis"],
    "math_is_computation": ["analog_digital", "affirm_negate", "rlc_damping"],
    "every_zero_is_the_origin": ["provenance_is_self_rooted", "origin_is_opening", "naming_unnaming"],
    "indexed_store": ["constants_map", "four_product_primitives"],
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
                    "was_links": a["perimeter"]["links"]}
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
print(f"round 3: absorbed {len(remap)} more. base now {len(base)}")
