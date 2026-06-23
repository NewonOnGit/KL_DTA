"""
embed_spectral.py — one-time: install the SEED into KL_DTA.json.

After this, the file holds the seed P (≈ [1,1] and 2) and the generation maps.
The spectral core — I, R, N, J, h, L_{R,R}, its spectrum, the constants — is NOT
stored; kl_dta.py regenerates it from the seed on load. Store the seed, serve the
bulk.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

seed = {
    "P": [[0, 0], [2, 1]],
    "note": "the only stored matrix; P²=P, rank 1, P≠Pᵀ. ≈ [1,1] and 2. Everything regenerates from P.",
    "regenerate": {
        "I": "identity",
        "R": "(P + Pᵀ)/2   — production generator, R²=R+I",
        "N": "(P - Pᵀ)/2   — observer/rotation, N²=-I",
        "J": "sign(diag)   — gauge bit, J²=I",
        "h": "J·N          — mediation generator, h²=I",
        "L_RR": "X ↦ R·X + X·R - X   — the self-action",
        "spectrum_L_RR": "{+√5, 0, -√5} = {+√disc, 0, -√disc}",
        "basis": "{I, R, N, h} spans M₂(ℝ); every object is 4 coordinates",
    },
    "generation_maps": {
        "1": "identity element I",
        "phi": "fixpoint(x ↦ √(1+x))",
        "psi": "1 - phi",
        "disc": "tr(R)² - 4·det(R) = 5 = ‖R‖²+‖N‖²",
        "sqrt5": "2·phi - 1 = spectrum(L_RR)",
        "pi": "2·arg(eig(N))",
        "e": "base of exp on the mediation generator h",
    },
}

# spectral coordinates in {I, R, N, h} — how objects are HELD (not as matrices)
primitives = {
    "I":    [1, 0, 0, 0],
    "R":    [0, 1, 0, 0],
    "N":    [0, 0, 1, 0],
    "h":    [0, 0, 0, 1],
    "-I":   [-1, 0, 0, 0],
    "R^2":  [1, 1, 0, 0],   # = I + R
    "N^2":  [-1, 0, 0, 0],  # = -I
    "h^2":  [1, 0, 0, 0],   # = I
    "P":    [0, 1, 1, 0],   # = R + N   (the seed decomposes as R+N)
}

# rebuild with seed inserted after grade_internalization, before base
order = ["$self", "carrier", "master_equation", "structure", "grade_internalization"]
new = {k: db[k] for k in order if k in db}
new["seed"] = seed
new["spectral_primitives"] = primitives
for k, v in db.items():
    if k not in new:
        new[k] = v

PATH.write_text(json.dumps(new, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"seed installed into {PATH.name}")
print(f"  top-level keys now: {list(new.keys())}")
