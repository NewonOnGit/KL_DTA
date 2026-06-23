"""
fold_subsume4.py — round 4: the foundational and structural clusters collapse.
Lossless (claims kept in `absorbed`), surplus (the general unifies), count drops.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
base = db["base"]

SUBSUME = {
    "master_equation": ["defect_nu", "anchor_projection", "five_part_fold",
                        "five_generators", "godel_unification"],
    "metalayer_collapse": ["grading_tree", "kernel_internalization", "links_are_homology",
                           "fixed_points_are_residual_defects", "records_are_bundles",
                           "bundle_of_bundles_tower"],
    "base_is_perimeter_and_shape": ["trace_det_are_sum_product", "eigen_spine_spectrum",
                                    "two_controls", "polar_decomposition"],
    "gradient_flow": ["flow_strata", "self_steering_circuit", "conjugation_equivariance"],
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
print(f"round 4: absorbed {len(remap)} more. base now {len(base)}")
