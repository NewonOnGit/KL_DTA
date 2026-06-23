"""
cut1_master_equation.py — the first migration cut: master_equation record → MORPHISM.

reify the equation as a function-with-provenance (THE typing): the master equation is the
function m(X) = X² − tr(X)·X + det(X)·I, whose LAW is m(X)=0 ∀X (Cayley-Hamilton). inline body.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

me = db["base"]["master_equation"]
me["morphism"] = {
    "type": "Carrier → Carrier",
    "body": "X@X - tr(X)*X + det(X)*I",      # inline; evaluates to 0 for all X (the law holds)
    "fold": "X@X",                            # the generative reading (the FOLD opcode)
    "law": "X@X == tr(X)*X - det(X)*I",       # Cayley-Hamilton, the identity it asserts
    "verdict": "FORCED",                      # the grade = the VERDICT field
    "provenance": ["?"],                      # → ? (carried by the morphism itself)
    "note": "the equation IS a function; reifying it as a callable body with provenance is the typing. "
            "run: kl_dta.py call master_equation <X>",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("cut 1: master_equation is now a morphism (inline body + signature + provenance)")
