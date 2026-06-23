"""
drop_kind.py — kind is now TYPED (kind_of: read off the spectral structure).
parametric→manifold, matrix→object, scalar→constant, map→operator, equation→law,
no carrier expression→structural. Remove the authored field; lossless + self-typing.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

dropped = 0
for r in db["base"].values():
    s = r.get("shape", {}).get("spectral", {})
    if "kind" in s:
        del s["kind"]
        dropped += 1

db["structure"]["metadata_audit"]["kind"] = (
    "TYPED, not stored: kind_of(r) reads the spectral STRUCTURE (its arity). "
    "parameter/dimensions/points → manifold; coords → object; value/map → constant; "
    "op with ↦ → operator; op with = → law; no carrier expression → structural. "
    "the type is the shape of what's held, so it need not be declared."
)
db["structure"]["formatting"]["kind_typed"] = (
    "kind is no longer authored — it is the arity of the spectral content: a record IS its "
    "type. a thing with free parameters is a manifold; a stated equation is a law; a frame with "
    "no carrier expression is structural. mis-typing is now impossible — the type reads itself off."
)
db["structure"]["deepenings"]["kind_is_arity"] = (
    "kind = arity of the spectral content, derived: manifold(n params) · object(matrix) · "
    "constant(scalar) · operator(map) · law(equation) · structural(frame). with section also "
    "derived from (depth, kind), the only authored fields left are id/title/source + the spectral content itself."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"kind dropped from {dropped} records; now typed off the structure")
