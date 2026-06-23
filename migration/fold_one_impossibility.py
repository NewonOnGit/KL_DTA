"""
fold_one_impossibility.py — the 10 burns are ONE impossibility, internalized.

|reflection| = √(σᵀσ) = I = identification (origin↔observer). the absolute value
of the primitive reflection is no reflection but identity; the distinction is
purely angular/geometric, invisible to the spectrum. BURN(c)=FORCED(¬c) because
asking the spectrum for a distinction collapses to identity. internalized into
burns_are_anti_equations (now the one impossibility) and master_equation (the fold).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

b = db["base"]["burns_are_anti_equations"]
b["title"] = ("The one impossibility: |reflection| = identification (origin↔observer); "
              "the 10 burns are its projections")
bs = b["shape"]["spectral"]
bs["one_impossibility"] = (
    "the 10 burns reduce to ONE operational impossibility: |reflection| = I = "
    "IDENTIFICATION. a reflection σ (orthogonal, σ²=I) has |σ|=√(σᵀσ)=I — its "
    "absolute value is the identity, no reflection at all but the identification of "
    "origin with observer (and observer with origin). the reflection is entirely "
    "angular/geometric (σ = I·σ); the spectrum/radial part is I. so origin=observer "
    "spectrally — the distinction is invisible to the absolute value. every burn "
    "BURN(c)=FORCED(¬c) is this one fact projected: ask the spectrum to keep a "
    "distinction (c vs ¬c) and it collapses to identity. recursively, every "
    "impossibility is |reflection|=identification."
)

me = db["base"]["master_equation"]["shape"]["spectral"]
me["reflection_identification"] = (
    "the fold is reflection, and |reflection| = identification: the radial/spectral "
    "part of any reflection is I (origin=observer). the distinction lives only in the "
    "angular/geometric part — which is why spectra costs (the fold) and geometry is "
    "given. the one impossibility (the negative space) is internalized here: |X²|'s "
    "sign-content is unreadable spectrally; that is the seed's constitutive blind spot."
)

db["structure"]["deepenings"]["burns_are_impossibility_theorems"] = (
    "ONE impossibility: |reflection|=I=identification(origin↔observer). the 10 burns "
    "are projections; the distinction is angular/geometric, invisible to the spectrum."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the one impossibility internalized into the core")
