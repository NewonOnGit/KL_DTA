"""
drop_section.py — section is now DERIVED (section_of: radius=depth, role=kind).
Remove the authored field from every base record. Lossless (regenerable exactly),
and more functional: any new record auto-sections; the band is now a law, not a label.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

dropped = 0
for r in db["base"].values():
    if "section" in r:
        del r["section"]
        dropped += 1

# record the now-derived field in the format/metadata reading
db["structure"]["metadata_audit"]["section"] = (
    "DERIVED, not stored: section_of(r) = f(radius=provenance depth, role=kind). "
    "manifold→manifold; depth1→thesis(law)/schema(else); depth≥2→metalayer. the shell is a law."
)
db["structure"]["formatting"]["section_derived"] = (
    "section is no longer authored — it is computed from the geometry (provenance depth = radius) "
    "and the role (kind). the shell falls out of where a record sits and what it is; removing it "
    "from the base loses nothing and makes every future record self-locating."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"section dropped from {dropped} records; now derived")
