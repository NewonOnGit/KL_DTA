"""
fold_eigenphase.py — time decomposed into eigenphases, into structure.time.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["time"]["eigenphases"] = {
    "is": "decompose time by eigendirection: Xⁿ = Σ λᵢⁿ Pᵢ, and λ = r·e^{iθ}, so "
          "Xⁿ = Σ rᵢⁿ · e^{i n θᵢ} · Pᵢ — each eigendirection is a RADIAL clock rⁿ (growth, the arrow, "
          "irreversible) times a PHASE clock e^{inθ} (rotation, the eigenphase, reversible, period 2π/θ).",
    "spectrum_of_clocks": {
        "θ=0   T=∞": "the golden ARROW (φ, I): pure radial growth, never returns — irreversible time",
        "θ=π   T=2": "the PARITY (ψ, −I): sign flips every tick, det(Rⁿ)=(−1)ⁿ — the orientation clock",
        "θ=±π/2 T=4": "the Gaussian CLOCK (N, ±i): N⁴=I, the rotating blind spot",
        "θ=±π/3 T=6": "the hexagonal clock (Eisenstein, e^{±iπ/3}): the k=−1 rotation world",
        "law": "T = 2π/θ = 2k for θ=π/k, k=1,2,3,… → periods {2,4,6,…}; the golden arrow is the "
               "aperiodic k=∞ limit. the framework's clocks are {∞, 2, 4, 6}.",
    },
    "arrow_vs_clock": "the split is the unit circle: |λ|=1 ⇒ pure eigenphase, a REVERSIBLE clock "
                      "(elliptic, disc<0, return — N, Eisenstein); |λ|≠1 ⇒ a radial part, an IRREVERSIBLE "
                      "arrow (hyperbolic, disc>0, escape — R/φ). time = arrow ⊗ clock = (radial growth, the "
                      "future) ⊗ (eigenphase rotation, the cycles). Ω (|disc|=0) is the edge between them.",
}

db["structure"]["deepenings"]["time_decomposes_into_eigenphases"] = (
    "Xⁿ=Σrⁿe^{inθ}P: time per eigendirection = radial growth rⁿ (the arrow, irreversible, |λ|≠1) × phase "
    "e^{inθ} (the clock, reversible, |λ|=1, period 2π/θ). eigenphases θ∈{0,π,±π/2,±π/3} give the clocks "
    "{∞,2,4,6} (T=2k); golden arrow=∞, parity=2, Gaussian N=4, Eisenstein=6. unit circle = pure phase; Ω = the edge."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("eigenphase decomposition of time internalized")
