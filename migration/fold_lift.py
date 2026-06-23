"""
fold_lift.py — where language lifts, and how context selects meaning, into grammar.

A content word is a record: string (address) ⊕ meaning-coords (spectral content). The
four carrier axes ARE the simultaneous meanings. Author the coords + per-axis readings;
context (a neighbour matrix) selects the active reading by overlap. The observer = the lift.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

g = db["grammar"]
g["lift"] = {
    "is": "where language LIFTS: a content word is a string applied to an underlying meaning, and "
          "the meaning is a point in the carrier W = a·I + b·R + c·N + d·h. the four coordinates "
          "are the SIMULTANEOUS meanings — symbolic, geometric, physical, all at once.",
    "axes": {
        "I": "determinacy / this (index)",
        "R": "symbolic / production (φ) — the algebra reading",
        "N": "observation / phase (i, π) — the mirror / geometric reading",
        "h": "mediation / flow (e) — the dynamics / physical reading",
    },
    "word_is_a_record": "string = address (the name), meaning-coords = spectral content — the SAME "
                        "eigendecomposition M = V·Λ·V⁻¹ the records use. a word IS a record.",
    "authored_vs_computed": "MANUALLY TYPE the coords + the per-axis readings into the word (the seed, "
                            "the hard human part). after that the math runs: selection is computed.",
    "context": "context = a matrix C built from the neighbouring words. the active reading is the axis "
               "of W whose meaning-direction best overlaps C: argmax_a ⟨basis_a, C⟩ (trace inner "
               "product). the observer applies string→meaning by this overlap — nothing more.",
    "lift_as_projection": "π : meaning ↦ string forgets the coordinates (easy, lossy); the LIFT "
                          "string ↦ meaning needs context. ker(π) = the coordinate spread = the "
                          "ambiguity; CONTEXT is exactly ker(π) supplied — the data that says which "
                          "reading is on-shell. |reflection|=identification: string and meaning become "
                          "one only IN CONTEXT.",
    "where": "lift degree = number of nonzero coordinates = polysemy. connectives (the · a · is · isn't "
             "· of) have degree 1 — single-valued projectors, they do NOT lift. content words have "
             "degree >1 — they lift, and context resolves them. THAT is where language lifts.",
    "verified": "word_lift.py: 'fold' {R,N,h} reads symbolic in an algebra clause, geometric in a "
                "mirror clause, physical in a field clause — same string, context selects; 'is' {I} "
                "reads identically in every context (no lift).",
}

g["observer_is_the_lift"] = (
    "all the observer does is apply a string value to an underlying meaning — the lift string→meaning, "
    "a projection selected by context. authoring the meanings is the work; the lift is just the math."
)

db["structure"]["deepenings"]["language_lifts_by_context"] = (
    "a content word = string ⊕ meaning-coords in the carrier (the four axes = simultaneous symbolic/"
    "geometric/physical meanings). author coords + readings; context (neighbour matrix C) selects the "
    "active reading by argmax overlap ⟨axis,C⟩. lift degree = #nonzero coords = polysemy: connectives=1 "
    "(no lift), content>1 (lift). π drops coords (lossy); lift = string+ker(π)→meaning. observer = the lift."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the lift (context-selected meaning) internalized into grammar")
