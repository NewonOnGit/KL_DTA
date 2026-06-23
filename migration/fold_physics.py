"""
fold_physics.py — uplift the language to full physicality.

The math IS physics; the language is raised to the physical register. Each
operation keeps its abstract meaning and gains its physical one.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["physics"] = {
    "is": "the math read physically — the language uplifted to its physical register",
    "dispersion": "X² = tr·X − det·I  is the characteristic / dispersion relation; "
                  "s² − tr·s + det = 0 is the mass-shell condition",
    "lexicon": {
        "fold X²":            "propagation / the action",
        "defect ν":           "virtuality — distance off the mass-shell",
        "ν → 0 (FORCED)":     "on-shell — a real, propagating state",
        "ν ↛ 0 (BURN)":       "off-shell — virtual / forbidden",
        "ker":                "the vacuum",
        "disc":               "discriminant of the dispersion; sign(disc) = regime "
                              "(bound·oscillatory / critical·massless / free·scattering)",
        "R · {·} · enrichment": "the metric / mass / gravity  (R² = R + I)",
        "N · [·] · defect":   "the quantum phase / spin / curvature  (N² = −I = i)",
        "{·} Jordan":         "observables (the Jordan algebra)",
        "[·] Lie / commutator": "field strength / force / gauge  (F = [D,D])",
        "generation":         "sourcing a field",
        "depth":              "energy scale (tower level)",
        "?":                  "the origin — the root of the light-cone / the vacuum's seed",
    },
    "mood_is_state": {
        "FORCED": "on-shell (real, propagates)",
        "BURN":   "off-shell (virtual / forbidden)",
        "AXIOM":  "a boundary condition (imposed)",
        "OPEN":   "superposed (unmeasured, in the slot)",
    },
    "P²=P": "the vacuum: self-reference (+I) and self-negation (−I) cancel — the "
            "zero-point balance that lets a real state sit on-shell.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("language uplifted to full physicality; physics section added")
