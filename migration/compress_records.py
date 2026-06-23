"""
compress_records.py — hold each record at its independent coordinates only.

The self-action block labels (action/type/axis/act/reads_as) and the mode strings
(eigenvalue/mode) are constant across all records — they were repeated 70×. They
move to the top-level self_action.template (held once); each record keeps only its
modes' lambda + verdict + homed data. Lossless: the engine derives the rest.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

KEEP = ("generators", "residual", "routes", "mechanism", "depth", "disc")

for r in db["base"].values():
    sa = r["self_action"]
    new = {}
    for key in ("symmetric_R", "antisymmetric_N"):
        modes = []
        for m in sa[key]["modes"]:
            nm = {"lambda": m["lambda"], "verdict": m["verdict"]}
            for k in KEEP:
                if m.get(k) is not None:
                    nm[k] = m[k]
            modes.append(nm)
        new[key] = {"modes": modes}
    r["self_action"] = new

# the constants, held once
db["self_action"]["template"] = {
    "symmetric_R": {"action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
                    "axis": "production (R)", "act": "self-reference (R²=R+I, ν=I)",
                    "reads_as": "enrichment (+I)"},
    "antisymmetric_N": {"action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
                        "axis": "observation (N)", "act": "self-negation (N²=−I, N⁴=I)",
                        "reads_as": "defect (−I)"},
    "modes_legend": {"+sqrt5": "+√5 generation", "0": "0 return", "-sqrt5": "-√5 observation"},
    "note": "constant across all records — held once here. each record stores only "
            "its modes' lambda + verdict + homed data; the rest is derived.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("records compressed to independent coordinates; constants held once")
