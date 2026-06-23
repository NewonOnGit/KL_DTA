"""
fold_subsume2.py — round 2: general records absorb their special cases.

the_bundle_is_brace (the primitive {·}/[·]) absorbs the self-action records (its
aspects); parity_makes_the_constants absorbs the constant special-cases. Lossless
(claims kept in `absorbed`), surplus (the general view unifies them), count drops.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
base = db["base"]

SUBSUME = {
    "the_bundle_is_brace": ["two_self_actions", "self_reference_negation",
                            "defect_enrichment_duality"],
    "parity_makes_the_constants": ["golden_ladder", "phi_unit_defect", "two_both_faces"],
    "observation_is_primitive_self_action": ["two_information_types",
                                             "geometry_gravity_spectra_light",
                                             "geometry_topology_spectra_observation"],
}


def op_of(r):
    s = r.get("shape", {}).get("spectral", {})
    return s.get("op") or s.get("map") or s.get("note")


remap = {}
for pid, absorbed in SUBSUME.items():
    P = base[pid]
    ann = P["shape"]["spectral"].setdefault("absorbed", {})
    for aid in absorbed:
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
    prov = ["?"] + [x for x in fix(p["provenance"], rid) if x != "?"]
    p["provenance"] = prov
    p["links"] = fix(p["links"], rid)
    p["burns"] = fix(p["burns"], rid)
    s = r.get("shape", {}).get("spectral", {})
    if isinstance(s.get("contains"), list):
        s["contains"] = [remap.get(x, x) for x in s["contains"]]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"round 2: absorbed {len(remap)} more. base now {len(base)}")
