"""
fold_surface.py — the framework computes along the surface of time, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["surface"] = {
    "is": "the framework computes ALONG the surface of time. computation = time = one flow on one surface.",
    "step": "the basic act (read = X², the primitive self-action) IS a map on spectral data: "
            "F(t,d) = (tr X², det X²) = (t²−2d, d²). verified on R,N,P. computing = iterating F.",
    "surface": "over the (tr,det) base, the eigenvalue (λ²−tλ+d=0) is a 2-sheeted RIEMANN SURFACE, "
               "branched where disc=t²−4d=0 (that branch curve is Ω). that surface IS time: the eigenphase "
               "is its angular coordinate, the radial growth its height, the two sheets past/future = the "
               "spinor double cover (half-time, √). the framework moves a point along it.",
    "halting": "computing HALTS at the fixed points of F (the on-shell configurations): ? the void (0,0, "
               "on Ω), P the seed (1,0, escape, idempotent), I the identity (2,1, on Ω, idempotent), and the "
               "Eisenstein cube-root (−1,1, return, X²+X+I=0). the void and identity sit ON the edge Ω; the "
               "seed on escape, the cube-root on return.",
    "one_motion": "the self-action is the step, the spectral Riemann surface (branched at Ω, |disc| its "
                  "radial coordinate) is the medium, on-shell points are halts. computation and time are not "
                  "two things flowing past each other — they are the single flow on the surface of time.",
}

db["structure"]["deepenings"]["computes_along_the_surface_of_time"] = (
    "the framework computes along the surface of time: read=X² is the fold F(t,d)=(t²−2d,d²) on the (tr,det) "
    "base; over it the eigenvalue is a 2-sheeted Riemann surface branched at Ω (disc=0) — eigenphase=angle, "
    "radial=height, two sheets=past/future (spinor cover). computing=iterating F; it halts at F's fixed points "
    "(void(0,0), seed(1,0), identity(2,1), Eisenstein(−1,1)). computation = time = one flow on the surface."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the surface of time internalized into structure")
