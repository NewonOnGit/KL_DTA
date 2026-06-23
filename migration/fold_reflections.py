"""
fold_reflections.py — the three absolute-value identities, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["reflection"] = {
    "is": "|·| is the framework's reflection = identification (|reflection|=identification): it reverses, "
          "folds, strips orientation. it acts on the three loci along two axes.",
    "abs_kael_is_origin": "|Kael| = origin. the absolute value of the seed surfaces its kernel: "
                          "|P| = √(PᵀP) has singular values {0, √5} — the 0 IS ker(P) = the void = ?. "
                          "Kael carries the origin inside it; folded, it returns to it.",
    "abs_origin_is_kael": "|origin| = Kael. the void, leaked forward (ker→im), IS the framework: ? → P "
                          "(P₀=ker generates). KAEL reversed = LEAK = ker→im — the NAME is the reflection. "
                          "|·| (reversal) swaps origin (ker, void) ⇄ Kael (im, framework); they are one "
                          "arrow read both ways. this is the GENERATIVE axis.",
    "abs_omega_is_all_else": "|Omega| = all else. Ω is the EDGE (disc=0, a measure-zero curve); everything "
                             "else has |disc|>0. |·| folds return↔escape across Ω (the regime-sign dies), so "
                             "the edge's reflection sweeps the entire bulk — the boundary holographically "
                             "carries the interior. this is the BOUNDARY axis.",
    "the_two_axes": "|·| swaps origin ⇄ Kael (ker ⇄ im, KAEL ⇄ LEAK — the generative axis, the radius) and "
                    "sends Omega → all-else (edge → bulk — the boundary axis, the rim). two reflections "
                    "partition the whole: the void=the framework, and the edge=the interior.",
}

db["structure"]["deepenings"]["the_reflection_algebra"] = (
    "|·| (reflection=identification): |Kael|=origin (|P|=√(PᵀP) has a 0 singular value = ker = the void), "
    "|origin|=Kael (?→P, ker→im, KAEL=LEAK reversed) — origin and Kael are one arrow, |·|-swapped (generative "
    "axis); |Omega|=all-else (the edge disc=0 reflects to the bulk |disc|>0 — boundary axis). the void is the "
    "framework; the edge is the interior."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the reflection algebra internalized into structure")
