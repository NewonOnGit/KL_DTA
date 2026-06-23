"""
fold_light_gravity.py — geometry is gravity, spectra is light.

GEOMETRY (degree-1 action, eigenvectors = fixed points) = gravity, cheap/direct.
SPECTRA (degree-2 fold, eigenvalues) = light, costs one fold. origin emits spectra;
the observer projects geometry; recovering spectra is the inverse — circular,
completed by evolution. seeing spectra completes the circle.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["geometry_gravity_spectra_light"] = {
    "id": "geometry_gravity_spectra_light",
    "title": "Geometry is gravity (fixed points, degree-1, cheap); spectra is light (the fold, degree-2, costs)",
    "section": "observer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "two_information_types"],
        "links": ["two_information_types", "polar_decomposition", "observer_unifies_projections",
                  "gradient_flow", "projection_spectral_triple", "observer_dynamics"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "FLOW", "RETURN"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 4, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "X = Q·P: Q = geometry = gravity (degree-1 action X·v; eigenvectors are FIXED points; cheap, direct). P = spectra = light (degree-2: λ solves λ²−tr·λ+det=0, the master equation/the FOLD; eigenvalues = frequencies; costs one fold). origin projects spectra (emitted, simple); the observer is a projector OF that projection and sees geometry directly; to see spectra it inverts itself — circular (observer→origin→observer), completed by evolution. seeing spectra completes the circle. that inverse is why geometry is easy and spectra costs"},
    },
}

db.setdefault("physics", {})["light_and_gravity"] = {
    "geometry = gravity": "the eigenvectors (fixed directions, degree-1 action) — the fixed points; "
                          "read directly, cheap. the metric, where things settle.",
    "spectra = light": "the eigenvalues (degree-2, the fold λ²−tr·λ+det=0) — the frequencies; "
                       "costs one fold to see (square X). radiated, not fixed.",
    "projection": "origin emits spectra (light, simple); the observer projects geometry (gravity, seen). "
                  "to recover spectra the observer inverts itself — circular, completed by evolution.",
    "cost": "seeing geometry is degree 1 (direct); seeing spectra is degree 2 (one fold). "
            "the fold IS observation, and its output is the spectrum.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("light & gravity folded — the keystone. base now", len(db["base"]))
