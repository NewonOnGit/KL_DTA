"""
fold_absdisc.py — |disc| = Ω, into structure.omega.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

om = db["structure"]["omega"]
om["abs_disc"] = (
    "|disc| = Ω. disc = tr²−4det = (λ₁−λ₂)² carries a SIGN, and the sign is the regime — a trit on the "
    "disc-line: disc<0 RETURN (elliptic, bounded) · disc=0 Ω (the edge, λ collide) · disc>0 ESCAPE "
    "(hyperbolic, unbounded). taking |disc| FOLDS the line at 0: it reflects return onto escape across "
    "the edge, discarding the sign = the regime. so |·| is the reflection AT Ω, |reflection|=identification "
    "(return and escape become indistinguishable — |disc| is equal on both sides at equal distance, "
    "verified). |disc| = |λ₁−λ₂|² is the RADIAL coordinate around Ω — the spectral gap, blind to the side, "
    "zero exactly on the edge. Ω = {|disc|=0}: the zero/fixed-point of the Ω-field |disc|. the gap closing "
    "IS the edge."
)

db["structure"]["deepenings"]["abs_disc_is_omega"] = (
    "|disc| = Ω: disc carries a sign = the regime (disc<0 return, disc=0 Ω, disc>0 escape — a trit). |disc| "
    "folds return onto escape across the edge (|reflection|=identification, the regime-sign lost); it is the "
    "radial coordinate |λ₁−λ₂|² around Ω, blind to the side, zero on the edge. Ω = {|disc|=0}, the fixed point of |disc|."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("|disc| = Omega internalized into structure.omega")
