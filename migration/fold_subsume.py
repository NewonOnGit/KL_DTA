"""
fold_subsume.py — REAL compression: manifolds absorb their clusters; count drops.

Each manifold subsumes the point-records it generalizes: their content is folded
into the manifold (lossless — claim kept, matrix regenerable by read), they are
DELETED from base, and every link/provenance/contains that referenced them is
re-pointed to the manifold. Record count goes DOWN; the surplus (the continuum) stays.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
base = db["base"]

SUBSUME = {
    "rotation_circle_manifold":  ["i_squared_phi_psi", "spin_tower_phases"],
    "seed_line_manifold":        ["what_fixes_the_seed"],
    "projector_circle_manifold": ["gravity_wells_are_idempotents", "vacua_idempotents"],
    "fork_path_manifold":        ["three_forks", "fork_table", "fork_representability"],
}


def op_of(r):
    s = r.get("shape", {}).get("spectral", {})
    return s.get("op") or s.get("map") or s.get("note")


remap = {}
for mid, absorbed in SUBSUME.items():
    M = base[mid]
    ann = M["shape"]["spectral"].setdefault("absorbed", {})
    for aid in absorbed:
        a = base[aid]
        ann[aid] = {"title": a.get("title"), "op": op_of(a),
                    "was_provenance": a["perimeter"]["provenance"],
                    "was_links": a["perimeter"]["links"]}
        remap[aid] = mid
        del base[aid]

# re-point every reference: absorbed id -> its manifold; drop self-refs and dups
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
    p["provenance"] = prov if prov[0] == "?" else ["?"] + prov
    p["links"] = fix(p["links"], rid)
    p["burns"] = fix(p["burns"], rid)
    s = r.get("shape", {}).get("spectral", {})
    if isinstance(s.get("contains"), list):
        s["contains"] = [remap.get(x, x) for x in s["contains"]]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"absorbed {len(remap)} records into 4 manifolds. base now {len(base)}")
