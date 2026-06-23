"""fold_music.py — the chords are literal: the math is music theory."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["music"] = {
    "is": "the chords are LITERAL — the math is music theory (the math of ratio and mode). eigenvalues are "
          "frequencies (the eigenvalue problem IS the vibration problem).",
    "consonance_primes": "the core numbers ARE the 5-limit just-intonation primes: norm(N)^2=2 (OCTAVE 2:1, "
          "N^2=-I), norm(R)^2=3 (FIFTH 3:2, the tophat sqrt3), disc=5 (MAJOR THIRD 5:4). the MAJOR TRIAD "
          "(foundational consonance) = 4:5:6, built from {2,3,5} — the three core numbers.",
    "intervals": "the eigenphase periods {2,4,6} ARE intervals: period 2:4 = freq 2:1 = OCTAVE; period 4:6 = "
          "freq 3:2 = PERFECT FIFTH; 2:6 = 3:1 (octave+fifth). the clocks of parity/N/Eisenstein are the basis of harmony.",
    "dissonance": "phi (from R^2=R+I) is the MOST irrational number = maximal DISSONANCE. the framework has "
          "both sides: integer (2,3,5 consonant) and golden (phi,sqrt5 dissonant), both seed-forced.",
    "grade_is_consonance": "CONSONANCE = on-shell (nu=X^2-X=0, FORCED — resolves, stable); DISSONANCE = "
          "off-shell (nu!=0 pinned, BURN — tension that does not resolve). RESOLUTION = nu->0 (the fold reaching "
          "its fixed point). the 12 burns are the UNRESOLVABLE dissonances (pinned at +-sqrt5 forever).",
    "chords": "insights = chords (atom-combinations from the alphabet); harmonics = the spectrum; the trit "
          "{+sqrt5,0,-sqrt5} is a triad. the math FOLLOWS harmonics, dissonance, and music theory because it IS them.",
}
db["structure"]["deepenings"]["the_math_is_music_theory"] = (
    "the chords are literal — the math IS music theory: core numbers = 5-limit primes (norm(N)^2=2 octave, "
    "norm(R)^2=3 fifth, disc=5 third; major triad 4:5:6); eigenphase periods {2,4,6} = octave (2:1) + perfect "
    "fifth (3:2); phi = maximal dissonance. CONSONANCE = on-shell (nu=0, FORCED, resolves); DISSONANCE = burn "
    "(nu!=0, tension); resolution = nu->0; the 12 burns = unresolvable dissonances (+-sqrt5). insights = chords."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("music theory internalized")
