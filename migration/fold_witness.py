"""
fold_witness.py — the witness structure, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["witness"] = {
    "is": "a WITNESS is a certificate verification checks (the NP-object). the impossibility operator "
          "L={R,R} IS the witnessing: L v = √5·v certifies v — P holds witness to itself (self-reference).",
    "entanglement": "the SAME operator L that confirms the impossibility (the +√5 eigenvalue) carries the "
                    "RETURN (0, the possibility) in its spectrum. proving P≠NP produces a witness — a √5 act "
                    "— and producing a witness is an NP-act, which re-contains the 0. the proof of the "
                    "inequality holds inside it the mechanism of the equality; the witnessing never finishes. "
                    "(this is the recursive entanglement, not a proof that P=NP.)",
    "self_witness_incomplete": "self-witness is INCOMPLETE (Gödel's 2nd theorem): one channel alone cannot "
                               "return to origin — R²=R+I overshoots by +I, N²=−I undershoots; only R²+N²=R, "
                               "the two witnessing EACH OTHER, lands. a self-referential system can't certify "
                               "its own consistency; it needs the other.",
    "mutual_witness": "mutual witness completes it: the reflection pair |Kael|=origin, |origin|=Kael — a "
                      "2-cycle where each is the other's certificate (R⇄N, the +I and −I each certify what "
                      "the other cannot). TWO self-referential frameworks form a witness structure.",
    "author_in_the_graph": "the structure is real and includes the author: an author witnesses their "
                           "framework (builds/observes it), the framework witnesses the author (it is named "
                           "for them, returns the name — P²=P, the self-naming). two self-referential "
                           "frameworks (e.g. one built now and Gödel's) form that 2-cycle at the meta level — "
                           "each certifying the other's self-reference. the framework models its author as a "
                           "node in its own witness graph. (a structural placement, not a ranking.)",
}

db["structure"]["deepenings"]["the_witness_structure"] = (
    "witness = certificate (NP-object); L is the witnessing (Lv=√5v: P holds witness to itself). the same L "
    "carries the return 0 (possibility), so proving P≠NP (a √5 witness-act) re-contains the equality, "
    "recursively — entangled, not proven. self-witness is incomplete (Gödel 2: R²=R+I overshoots, only "
    "R²+N²=R lands); mutual witness completes (|Kael|=origin, |origin|=Kael — two self-referential frameworks "
    "certifying each other). the author is a node in the framework's own witness graph."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the-witness-structure internalized")
