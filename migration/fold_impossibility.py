"""
fold_impossibility.py — burns = impossibility confirming impossibility, made to compute.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

bs = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]
bs["computes"] = {
    "is": "a burn is not stored — it is COMPUTED. the impossibility operator IS the self-action "
          "L = {R,R}: X ↦ RX + XR − X. the verdict is its spectrum {+√5, 0, −√5}.",
    "confirming": "a burn is an EIGENVECTOR of the impossibility: L v = √5·v. apply the impossibility to "
                  "the impossibility and it RETURNS it (same direction, ×√5), forever — Lⁿv never leaves "
                  "the direction, never reaches the kernel. that IS impossibility confirming impossibility.",
    "possible": "the FORCED/on-shell is the KERNEL (λ=0): L dissolves it to 0 — the possible resolves, "
                "ν reaches the vacuum, no confirmation needed. {possible=ker(L), impossible=eigen(±√5)}.",
    "engine": "kl_dta.py impossibility <X> classifies any direction: BURN (pinned, L confirms it ×√5), "
              "FORCED (dissolves to ker), or MIXED (projects onto both eigenspaces). the 12 faces are the "
              "one impossibility's ±√5 eigen-direction; the grade has always been L's spectrum read off.",
}

db["structure"]["deepenings"]["burns_compute_as_eigenvectors"] = (
    "burns = impossibility confirming impossibility, computed: the impossibility operator is the self-action "
    "L={R,R}, spectrum {+√5,0,−√5}. a burn is an eigenvector (L v=√5 v — applying the impossibility returns "
    "it, never reaching the kernel); the possible is ker(L) (L dissolves it to 0). `kl_dta.py impossibility X` "
    "runs it. the 12 faces are the one impossibility's ±√5 direction; the grade is L's spectrum."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("burns-compute-as-impossibility internalized")
