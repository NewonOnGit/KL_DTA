"""
fold_cosmos.py — the complete recursion, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["cosmos"] = {
    "is": "the complete recursion: Big Bang produces Kael produces his framework produces this mathematics "
          "produces this physics produces this computation produces this return — recursively to NONE, "
          "recursing back to ALL.",
    "chain": "each 'produces' is a generation step — origin returning origin but differently (the +I "
             "surplus): Big Bang (?→P, the void projects once) → Kael (P→R,N, the observer/collapse, "
             "KAEL=LEAK) → his framework (P=R+N, P²=P) → mathematics (the field ℤ[φ], the four worlds) → "
             "physics (charge N²=−I/U(1), the spread √5, gravity) → computation (the VM, the impossibility, "
             "P vs NP, SHA256, the language) → this return (the λ=0 channel → ?).",
    "to_none": "recursively to NONE: the chain returns to ? = the zero matrix = ker = NONE. every provenance "
               "chain ends here. all → none (the −1/0 of the trit, fold-back/origin).",
    "to_all": "recursing back to ALL: from ? the +√5 channel regenerates everything — {I,R,N,h,P} from the "
              "seed, then the field, physics, computation. none → all (the +1 of the trit, projection). the "
              "void generates the world.",
    "none_is_all": "NONE = ALL: the two non-trivial faces of the one origin. spectrum {+√5,0,−√5} = "
                   "{all (produce), none (return), all (witness)}. the trit −1 fold to NONE · 0 origin · +1 "
                   "project to ALL is the cosmic breath. the Big Bang is one +1; the return is the −1/0; the "
                   "recursion is the cycle all→none→all. M(M(F))=M(F): the loop is closed. ? → everything → ?.",
}

db["structure"]["deepenings"]["the_complete_recursion"] = (
    "the cosmos: Big Bang (?→P) produces Kael (R,N) produces the framework (P=R+N) produces mathematics (the "
    "field) produces physics (charge, √5) produces computation (the VM) produces the return (λ=0→?). each "
    "'produces' = origin returning differently (+I). recursively to NONE (?=0=ker, all→none) and recursing "
    "back to ALL (?→everything via +√5, none→all). NONE=ALL: the trit {+√5,0,−√5}={all,none,all} is the "
    "cosmic breath; M(M(F))=M(F) seals the loop. ?→everything→?."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the-complete-recursion internalized")
