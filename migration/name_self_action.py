"""
name_self_action.py — one-time: burn the name "L".

The self-action is not an operator L_{R,R}. It IS {R,R} — R paired with itself,
acting from both sides:  {R,R} : X ↦ R·X + X·R − X.  {s,s} is the self-action of
s. "L" was a lossy wrapper, the same mistake as P1/P2/P3.

Renames the record field  L_spectrum -> self_action  and fixes the op strings.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))


def fix_ops(s):
    if not s:
        return s
    if s.get("op"):
        s["op"] = (s["op"].replace("L_{R,R}", "{R,R}").replace("L_{N,N}", "{N,N}")
                   .replace("L_{R,R)", "{R,R}"))
    return s


for rid, r in db["base"].items():
    rebuilt = {}
    for k, v in r.items():
        rebuilt["self_action" if k == "L_spectrum" else k] = v
    rebuilt["spectral"] = fix_ops(rebuilt.get("spectral"))
    db["base"][rid] = rebuilt

db["self_action"] = {
    "is": "{R,R}",
    "operator": "{R,R} : X ↦ R·X + X·R − X",
    "definition": "{s,s} is the self-action of s. {R,R} is R acting on itself from both sides.",
    "spectrum": {
        "+√5": "Π₊ — generation  (rank 1, the φ-dyad)",
        "0":   "Π₀ — return      (rank 2, the kernel; the observer N lives here)",
        "-√5": "Π₋ — observation (rank 1, the ψ-dyad)",
    },
    "resolution": "Π₊ + Π₀ + Π₋ = I₄",
    "burned": "'L' was a lossy name for {R,R}; the labels P1/P2/P3 were lossy names for its eigenvalues.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("L -> {R,R}; record field L_spectrum -> self_action on all", len(db["base"]), "records")
