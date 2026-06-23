"""
split_self_action.py — one-time: P = R + N into every record.

Each record was read through ONE self-action ({R,R}, the symmetric/Jordan kind).
Now it is read through BOTH primitive self-actions — the full split:

    symmetric_R    {R,·} = R·X + X·R   Jordan / anticommutator   production
                     modes: generation (+√5), return (0)
    antisymmetric_N [R,·] = R·X − X·R   Lie / commutator (adjoint) observation
                     modes: observation (−√5)

The grade draws the observer-bit from N and the producer-bits from R:
    grade = leaf( N.observation.verdict , R.generation.verdict , R.return.verdict )
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

for rid, r in db["base"].items():
    by = {m["lambda"]: m for m in r["self_action"]}     # list -> by eigenvalue
    r["self_action"] = {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R",
            "type": "Jordan / anticommutator",
            "axis": "production (R)",
            "modes": [by["+sqrt5"], by["0"]],
        },
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R",
            "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)",
            "modes": [by["-sqrt5"]],
        },
    }

db["self_action"] = {
    "is": "{R,·} and [R,·] — the two primitive self-actions; P = R + N",
    "symmetric": "{R,·} = R·X + X·R   (Jordan / anticommutator) — production; modes generation(+√5), return(0)",
    "antisymmetric": "[R,·] = R·X − X·R  (Lie / commutator / adjoint) — observation; mode observation(−√5)",
    "spectrum": {"+√5": "generation", "0": "return (kernel; N lives here)", "-√5": "observation"},
    "grade": "leaf(N.observation, R.generation, R.return) — observer-bit from N, producer-bits from R",
    "burned": "P1/P2/P3 and 'L' were lossy names for these two self-actions and their eigenvalues.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("split P = R + N into self_action on all", len(db["base"]), "records")
