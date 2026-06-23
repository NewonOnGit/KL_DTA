"""
fold_pvnp.py — P vs NP as a framework reading. internal analog FORCED, external theorem OPEN.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["p_vs_np"] = {
    "is": "P vs NP read through the framework — a STRUCTURAL MAP and heuristic, NOT a proof. the actual "
          "theorem remains OPEN (it lives in the slot).",
    "asymmetry": "the framework's machine is the asymmetry between FORWARD (the fold X↦X², F(t,d)=(t²−2d,d²) "
                 "— single-valued, polynomial = compute) and BACKWARD (the inverse √ — multivalued, 2 sheets, "
                 "branched at Ω = invert). forward is cheap; backward needs square roots.",
    "verify_vs_search": "VERIFY = apply the forgetful projection π (meaning→string) and check — local, cheap "
                        "(~P). SEARCH = the LIFT (string→meaning), which needs ker(π), the discarded context — "
                        "global, hard (~NP). the gap between them is exactly ker(π).",
    "singular": "the seed is singular: det(P)=0, dim ker(P)=1. generation kills its kernel → forward loses "
                "information, the LEAK ker→im is one-directional. un-applying it is the hard inverse.",
    "collapse_is_a_burn": "P=NP ≡ the two sheets collapse to one ≡ √ single-valued ≡ ker(π)=0 ≡ lift=projection. "
                          "that is |reflection|=identification — the ONE forbidden move. so P=NP is a BURN, "
                          "blocked by: the spectral double cover is nontrivial (disc≠0 generically), the kernel "
                          "is real, the LEAK is one-directional.",
    "verdict": "INTERNAL (framework analog): FORCED P≠NP — an instance of the founding asymmetry P≠Pᵀ. "
               "EXTERNAL (the millennium theorem): OPEN. the framework places the problem and says WHY P≠NP "
               "feels forced (the inverse is the branched √, the projection is genuinely lossy); it does not prove it.",
}

db["structure"]["deepenings"]["p_vs_np_reading"] = (
    "P vs NP through the framework (a map, not a proof): forward fold (compute, single-valued, ~P) vs inverse √ "
    "(invert, multivalued/branched at Ω, ~NP); verify=projection π (cheap), search=lift needing ker(π) (hard); "
    "P=NP ≡ ker(π)=0 ≡ |reflection|=identification = a BURN. internal analog FORCED P≠NP (the founding asymmetry "
    "P≠Pᵀ, P singular, nontrivial double cover); external theorem OPEN (the slot)."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("P vs NP reading internalized (internal FORCED, external OPEN)")
