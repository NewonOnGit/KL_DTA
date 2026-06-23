"""
fold_origin_return.py — this is origin: the return channel (λ=0) IS ?.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["origin"]["this_is_origin"] = (
    "the RETURN channel of the impossibility L={R,R} (the λ=0 eigenvector, = (N−R)/√2, the "
    "return-to-origin direction) IS ?. one point with five faces: (1) the KERNEL of the "
    "impossibility — P₀ = ker = the void that generates; (2) the POSSIBLE — FORCED/on-shell "
    "directions dissolve into it (L·u=0, ν→0); (3) SOURCE and HOME — generation comes FROM it "
    "(+√5), return goes TO it (0); (4) UNREACHABLE for the impossible — ±√5 ⟂ 0, so P=NP is the "
    "return that 0-projects (P≠NP); (5) the CLOSURE — every provenance chain ends here (→?), the "
    "loop ?→everything→? closes here. L·(return)=0: the origin is the fixed point of the impossibility. "
    "this is origin."
)

db["structure"]["deepenings"]["the_return_is_the_origin"] = (
    "this is origin: the return channel (λ=0 of the impossibility, (N−R)/√2) IS ? — the kernel/P₀ (void "
    "that generates), the possible (FORCED dissolves into it), source and home (generation FROM +√5, return "
    "TO 0), unreachable for the impossible (±√5⟂0, P≠NP), and the closure (every chain →?). L·(return)=0: "
    "origin is the impossibility's fixed point."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("this-is-origin internalized")
