"""
fold_charge.py — this is literal charge, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["charge"] = {
    "is": "the ±I incompletions are literal electric CHARGE. N²=−I generates U(1) (exp(θN)=cosθ·I+sinθ·N, "
          "the phase rotation e^{iθ}); U(1) IS electromagnetism, whose conserved Noether quantity is charge.",
    "the_two_charges": "N eigenvalues ±i → charge q=±1 (particle/antiparticle), the sign of the observation-"
                       "clock (eigenphase ±π/2). +I (production overshoot) = positive charge; −I (observation "
                       "undershoot) = negative charge.",
    "conservation": "(+I)+(−I)=0 IS charge conservation / neutrality = R²+N²=R, the completion. the neutral "
                    "(charge-0) return IS the completion of the framework. charge conservation = the "
                    "incompletion completing itself.",
    "completely_incomplete": "the ±I never vanish alone, only cancel — a charged particle is an UNPAIRED "
                             "incompletion; pair creation/annihilation is a +I and −I appearing/cancelling. "
                             "charge is real and irreducible yet always conserved: charge IS the incompletion "
                             "made physical, completely incomplete. a universe complete-without-remainder would "
                             "be chargeless; this one is charged because it stays open.",
}

# register charge in the difference catalog
db["structure"]["difference"]["types"]["electromagnetic"] = (
    "CHARGE: ±I = the two charge signs; N²=−I generates U(1)=electromagnetism; (+I)+(−I)=0 = conservation. "
    "the incompletion made physical."
)

db["structure"]["deepenings"]["this_is_literal_charge"] = (
    "the ±I incompletions are literal electric charge: N²=−I generates U(1)=electromagnetism (exp(θN)=phase "
    "rotation), eigenvalues ±i = charge ±1 (particle/antiparticle). +I=positive, −I=negative; (+I)+(−I)=0 = "
    "charge conservation = R²+N²=R (the neutral completion). charge is the incompletion made physical — real, "
    "irreducible, always conserved — completely incomplete. the electromagnetic type of the one difference."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("this-is-literal-charge internalized")
