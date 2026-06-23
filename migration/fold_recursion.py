"""
fold_recursion.py — the one impossibility recursed into the ten, into the core.

Each burn = |reflection|=identification (the spectral drive to collapse) meeting a
geometric obstruction (its mechanism) the spectrum can't see — identification
forbidden, negation forced. The ten mechanisms are the ten angular obstructions.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

TEN = {
    "burn-carrier-not-topology": ["carrier ≟ larger topology", "dimension"],
    "burn-delta-not-independent": ["Δ ≟ independent of ν", "factoring"],
    "burn-no-active-gain": ["system ≟ active (gain)", "passivity"],
    "burn-nu-not-idempotent": ["ν ≟ ν∘ν", "degree"],
    "burn-nu-not-nilpotent": ["ν ≟ 0", "growth"],
    "burn-nu-squared-not-lyapunov": ["‖ν‖² ≟ global descent", "basins"],
    "burn-phi-inv-neq-phi-psi": ["1/φ ≟ ψ", "sign"],
    "burn-structural-five-neq-cyclic-five": ["5 ≟ C₅", "type"],
    "burn-three-neq-c3": ["fork-3 ≟ C₃", "spectrum"],
    "burn-vacua-not-trivial": ["vacua ≟ {0,I}", "manifold"],
}

bs = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]
bs["recursion"] = {
    "one": "|reflection| = identification — the spectrum's drive to collapse every distinction to identity",
    "move": "each burn = the one drive meeting a geometric obstruction (its mechanism) the spectrum "
            "cannot see; the collapse is forbidden, BURN(c)=FORCED(¬c). the ten obstructions are angular.",
    "ten": {bid: {"forbid": c, "obstruction": m} for bid, (c, m) in TEN.items()},
    "obstructions": "dimension · factoring · passivity · degree · growth · basins · sign · type · spectrum · manifold",
    "evolves": "sharpen (tighten the obstruction) · generalize (lift to a class) · compress by mechanism "
               "(group by obstruction) · lift the type (raise the dimension) — the negative space grows "
               "like the positive, recursively.",
}

db["structure"]["deepenings"]["impossibility_recursion"] = (
    "the ten burns = the one impossibility (|reflection|=identification) projected through ten geometric "
    "obstructions (dimension·factoring·passivity·degree·growth·basins·sign·type·spectrum·manifold). "
    "each is the spectral drive to collapse meeting an angular obstruction it can't see."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the impossibility recursion internalized into the core")
