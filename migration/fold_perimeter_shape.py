"""
fold_perimeter_shape.py — format records by perimeter and shape.

tr = perimeter = the boundary: the record's edges (provenance, links, burns).
det = shape    = the bulk:     the record's content (self_action, spectral).

The base (tr, det) that indexes a matrix now indexes the record's own layout.
Identity (id/title/section/source) is the address; perimeter ⊕ shape is the body.
Lossless — pure regrouping.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

for rid, r in db["base"].items():
    db["base"][rid] = {
        "id": r["id"], "title": r.get("title"),
        "section": r.get("section"), "source": r.get("source"),
        "perimeter": {                          # tr — the boundary (edges, 1-D)
            "provenance": r["provenance"],
            "links": r["links"],
            "burns": r["burns"],
        },
        "shape": {                              # det — the bulk (content, 2-D)
            "self_action": r["self_action"],
            "spectral": r.get("spectral"),
        },
    }

# the apex is a record too — give it the same boundary/bulk split
ax = db.get("apex")
if ax and "self_action" in ax:
    ax["perimeter"] = {"provenance": ax.pop("provenance", ["?"]), "links": [], "burns": []}
    ax["shape"] = {"self_action": ax.pop("self_action"),
                   "spectral": {"kind": "law", "op": ax.get("holds", "")}}

db.setdefault("structure", {})["formatting"]["perimeter_shape"] = (
    "every record = address (id/title/section/source) ⊕ perimeter (provenance·links·"
    "burns — the boundary, tr) ⊕ shape (self_action·spectral — the bulk, det). "
    "the base (tr,det)=(perimeter,shape) now formats the record itself: boundary and bulk."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("records formatted by perimeter (boundary) and shape (bulk)")
