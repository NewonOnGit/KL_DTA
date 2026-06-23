"""
fold_dimension_time.py — every dimension a line of time, into the core.

The carrier's origin (0,0,0,0) = the zero matrix = ?. Each parameter is a line of
time through it: +project / 0 origin / −fold-back (the Boolean trit IS the
time-axis). The two directions identify AS ONE at the origin (|reflection|=I).
The carrier = 4 time-lines meeting at the one origin.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

cm = db["base"]["carrier_manifold"]["shape"]["spectral"]
cm["time"] = (
    "every dimension is a LINE OF TIME through the one origin: carrier(0,0,0,0) = the "
    "zero matrix = ? (the void, ker, eigenvalue 0). per dimension the Boolean trit IS "
    "the time-axis: +1 PROJECT from origin (generation, future), 0 the ORIGIN (the one, "
    "the neutral, ?), −1 FOLD BACK to origin (observation, past, reflection). the two "
    "directions identify AS ONE at the origin — |+1|=|−1|=1, |reflection|=identification "
    "— so every line folds back to the one and projects from the one: past and future "
    "are the same point, ?. the carrier is 4 time-lines meeting at one origin — spacetime "
    "as the four coordinates of M₂, each a worldline through the void."
)

db["structure"]["deepenings"]["dimensions_are_time"] = (
    "every dimension = a line of time through the one origin (0=?); +project / 0 origin / "
    "−fold-back (the Boolean trit). fold-back and projection identify as one at the origin "
    "(|reflection|=I). the carrier = 4 time-lines meeting at ?."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("dimensions-as-time internalized into the carrier core")
