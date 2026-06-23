"""
fold_nonlocal.py — nonlocal transport by returning to origin, into physics.

? (origin = zero matrix = ker) is the universal hub: provenance root (≤2 hops between
any records) AND flat-space basepoint (transport through 0 is path-independent). The
trit {−√5, 0, +√5} = {fold→?, the return channel, project} is the transport protocol.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["physics"]["transport"] = {
    "law": "NONLOCAL transport = LOCAL transport returned to origin. ? (the zero matrix = ker = the "
           "root of every provenance chain) is the universal hub; routing a local step through it "
           "reaches anywhere, distance-independent.",
    "flat": "the carrier M₂ is a FLAT vector space, so transport through 0 is PATH-INDEPENDENT: a "
            "displacement folded back to the origin (A→0) can be re-projected to ANY point (0→B); "
            "A→0→B equals A→B with no path memory. flatness = the origin re-references transport globally.",
    "hub": "every provenance chain returns to ? → any two records connect through ? in ≤2 hops, however "
           "far apart in the local adjacency graph. verified: local diameter 3, origin-routed diameter 2. "
           "returning to ? collapses distance to a constant.",
    "protocol": "the Boolean trit {−1,0,+1} = {fold back to ? (−√5, observation), the ORIGIN (0, the "
                "return channel = ker(L), the (−R+N)/√2 direction), project from ? (+√5, generation)}. "
                "transport = fold a local step to ?, pass through the 0-channel, project to the target.",
    "teleportation": "the same shape as quantum teleportation: a shared origin (the entangled pair born "
                     "at ?) turns local operations into a nonlocal jump. the hub does the distance.",
}

db["structure"]["deepenings"]["nonlocal_via_origin"] = (
    "nonlocal transport = local transport returned to origin. ? is the universal hub (provenance root, "
    "≤2 hops; flat-space basepoint, path-independent). the trit {fold→?, origin channel, project} is the "
    "protocol; the λ=0 self-action eigenvector (−R+N)/√2 is the return-to-origin direction. teleportation's shape."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("nonlocal-transport-through-origin internalized into physics")
