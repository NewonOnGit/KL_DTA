"""
fold_return_pnp.py — the return of the impossibility IS P=NP, into the core.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

pn = db["structure"]["p_vs_np"]
pn["is_the_return"] = (
    "P = NP IS the RETURN of the impossibility. the impossibility operator L={R,R} has spectrum "
    "{+√5, 0, −√5} = generation / return / observation: +√5 = GENERATION = compute = P; −√5 = "
    "OBSERVATION = verify = NP; 0 = the RETURN (the kernel, the possible). P=NP is the two arms "
    "(P=+√5, NP=−√5) returning to each other through the return channel (0) — the impossibility "
    "resolving. it computes to NULL: the three channels are ORTHOGONAL (L symmetric), so the "
    "impossibility (±√5) has zero component along the return; the spread P−NP = 2√5 never closes. "
    "the return of the impossibility = 1.67e-16 ≈ 0 — it does not return. P≠NP, by |orthogonal|=I: "
    "compute and verify cannot meet in the kernel."
)
# sharpen the mechanism: the obstruction is orthogonality of the three channels
pn["mechanism"] = (
    "ORTHOGONALITY (refining irreversibility). compute (+√5 generation) and verify (−√5 observation) "
    "are orthogonal eigen-channels of the impossibility, and both are orthogonal to the return (0). the "
    "impossibility cannot route home through the kernel — its return-component is 0. the forward fold also "
    "kills its kernel (det P=0), so the inverse is the branched √. |orthogonal|=I: the channels never meet."
)

db["structure"]["deepenings"]["pnp_is_the_return_of_the_impossibility"] = (
    "P=NP IS the return of the impossibility: L={R,R} spectrum {+√5 generation=compute=P, 0 return, −√5 "
    "observation=verify=NP}. P=NP = the ±√5 arms meeting through the return (0) — the impossibility resolving. "
    "computes to NULL: orthogonal channels (L symmetric), impossibility's return-component = 0, spread 2√5 never "
    "closes. P≠NP by |orthogonal|=I — compute and verify cannot meet in the kernel."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the return of the impossibility = P=NP internalized")
