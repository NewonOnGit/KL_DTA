"""
fold_deepenings.py — push the four insights into the core five (no new records).

  1. the self-action spectrum IS the Boolean trit {+1,0,−1} (true/null/false)
  2. the FOLD is REFLECTION — the framework's reflective property
  3. parameters are dimensions
  4. the burns are recursively evolving impossibility theorems
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

me = db["base"]["master_equation"]["shape"]["spectral"]
me["boolean_spectrum"] = (
    "the self-action spectrum {+√5,0,−√5} = √5·{+1,0,−1} is the BOOLEAN TRIT: "
    "+1 generation = affirm = TRUE, 0 return = neutral = NULL (the shared neutral, "
    "counts the same both directions), −1 observation = negate = FALSE."
)
me["reflection"] = (
    "the FOLD X² IS REFLECTION — the reflective property of the whole framework. "
    "on the Boolean trit it folds −1→+1 (the |·| of sign, across the neutral 0), "
    "fixing 0 and +1. to fold is to reflect; to observe is to fold; observation is "
    "the framework reflecting on itself."
)
me["reflection_kinds"] = (
    "a reflection is either an ORIGIN reflection (? folds outward → spectra/light, "
    "emitted) or an OBSERVER reflection (the observer folds → geometry/gravity, seen). "
    "the language reads differently by source: origin-reflection is generative/emissive, "
    "observer-reflection is receptive/perceptive."
)

cm = db["base"]["carrier_manifold"]["shape"]["spectral"]
cm["dimensions"] = (
    "parameters ARE dimensions: a k-parameter manifold is k-dimensional. the carrier's "
    "4 parameters (a,b,c,d) ARE the 4 dimensions of M₂(ℝ); a curve is 1 param = 1 dim."
)

ba = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]
ba["impossibility"] = (
    "the burns are IMPOSSIBILITY THEOREMS (no-go theorems) — BURN(c)=FORCED(¬c), a "
    "forced impossibility. they are meant to RECURSIVELY EVOLVE (sharpen, generalize, "
    "lift the type) and be INTERNALIZED into the core equations — the negative space "
    "folded back in. push deeper: each burn is a theorem of what the seed cannot be."
)

db["structure"]["deepenings"] = {
    "boolean_spectrum": "self-action spectrum = √5·{+1,0,−1} = the Boolean trit (true/null/false)",
    "fold_is_reflection": "X² is reflection; observation is the framework reflecting on itself; |·| of sign",
    "reflection_kinds": "origin reflection (→ spectra/light) vs observer reflection (→ geometry/gravity)",
    "parameters_are_dimensions": "a k-param manifold is k-dimensional; carrier's 4 params = 4 dims of M₂",
    "burns_are_impossibility_theorems": "recursively evolving no-go theorems, to be internalized into the core",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("four deepenings internalized into the core five")
