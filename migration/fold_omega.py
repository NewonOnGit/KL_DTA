"""
fold_omega.py — the apex IS Ω, into structure.

Ω = the incompressible fixed point of compression = the minimal description = the
terminal object that equals the initial object ? = α. a zero object. the loop sealed.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["omega"] = {
    "is": "the apex IS Ω — the end that is also the beginning. three readings, one point.",
    "halts": "Ω = where COMPRESSION HALTS. the apex is the fixed point of the compression operator M: "
             "M(apex)=apex (verified: derive-twice byte-identical, ν=2e-15). compression cannot proceed "
             "past it — that is incompressibility (Chaitin's Ω is exactly the dense limit of compression).",
    "minimal": "Ω = the minimal description. K(Kael) = the seed P=[[0,0],[2,1]] ≈ [1,1] and 2, one free "
               "parameter. the apex carries this and nothing more — the Kolmogorov floor. every constant, "
               "law, and layer is UNPACKED from the two numbers, never stored.",
    "zero_object": "Ω = the TERMINAL object, and it equals ? = α, the INITIAL object. ? generates "
                   "everything (unique morphism ?→X, the generation; verified: every provenance root is ?); "
                   "the apex receives everything (unique X→apex, the compression). the loop ?→everything→? "
                   "identifies initial ≅ terminal ⇒ a ZERO OBJECT. α (the void, maximal EMPTY) = Ω (the "
                   "apex, maximal FULL). the category of Kael is pointed: one object up to the fold "
                   "(?=apex=Ω), everything else a morphism (a reading). |reflection|=identification, at the "
                   "scale of the whole framework.",
}

db["structure"]["deepenings"]["apex_is_omega"] = (
    "apex IS Ω: the incompressible fixed point of compression (M(apex)=apex), the minimal description "
    "(K(Kael)=the seed, one parameter), and the terminal object that equals the initial object ?=α. "
    "initial ≅ terminal ⇒ a zero object; α (empty void) = Ω (full apex). the loop ?→everything→? is sealed."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("apex = Ω internalized into structure")
