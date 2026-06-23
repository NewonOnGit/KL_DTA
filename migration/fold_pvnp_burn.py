"""
fold_pvnp_burn.py — P≠NP is the 12th face of the one impossibility. commit.

search ≟ verify is |reflection|=identification on the compute/invert pair. forbidden by
the same move as the other eleven. mechanism: IRREVERSIBILITY — the forward fold kills its
kernel (det P=0, ker→im one-directional), so the inverse is the genuinely branched √;
the two sheets cannot be one. no internal/external split — within Kael it is FORCED.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# recurse it into the burns as the 12th face
bs = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]["recursion"]
bs["ten"]["burn-search-not-verify"] = {
    "forbid": "search ≟ verify  (P ≟ NP)",
    "obstruction": "irreversibility",
}
bs["obstructions"] = bs["obstructions"] + " · irreversibility"
bs["count_note"] = ("the 'ten' has grown to twelve faces — the negative space grows like the positive. "
                    "P≠NP is the 12th: search ≟ verify, blocked by irreversibility.")

# rewrite the reading: commit, drop the diminishing internal/external split
db["structure"]["p_vs_np"] = {
    "is": "P ≠ NP IS the one impossibility — its 12th face. not an external problem the framework gestures "
          "at: the SAME forbidden identification |reflection|=identification, on the compute/invert pair.",
    "the_identification": "P=NP ≡ search = verify ≡ the lift = the projection ≡ ker(π)=0 ≡ the two spectral "
                          "sheets collapse to one ≡ √ is single-valued. every one of these is the reflection "
                          "trying to identify two things the geometry holds apart.",
    "mechanism": "IRREVERSIBILITY. the forward fold X↦X² kills its kernel (det P=0, dim ker=1; the LEAK "
                 "ker→im is one-directional). you cannot un-apply what collapsed — so the inverse is the "
                 "branched, multivalued √, two sheets meeting only at Ω. verify is local (one sheet, cheap); "
                 "search is global (which sheet — the lift through ker(π)). the cost of search is the kernel.",
    "verdict": "FORCED. within Kael P≠NP is not open and not a heuristic — it is an instance of the founding "
               "asymmetry P≠Pᵀ (the surplus requires the asymmetry; a symmetric idempotent collapses). the "
               "framework's claim is that this forcing IS the reason: P≠NP because compute and invert are the "
               "two directions of a non-invertible fold, and identifying them is the one move the geometry forbids.",
}

db["structure"]["deepenings"]["p_vs_np_is_the_impossibility"] = (
    "P≠NP IS the one impossibility's 12th face: search ≟ verify = |reflection|=identification on compute/invert, "
    "forbidden by IRREVERSIBILITY (forward kills its kernel, det P=0, ker→im one-directional; the inverse is the "
    "branched √, two sheets meeting only at Ω). FORCED within Kael — an instance of the founding asymmetry P≠Pᵀ. "
    "not internal-vs-external: the framework asserts this forcing is the structural reason P≠NP."
)
# supersede the earlier hedged reading's deepening
db["structure"]["deepenings"].pop("p_vs_np_reading", None)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("P≠NP recursed as the 12th face of the one impossibility; the hedge removed")
