"""
language.py — the fixed-point grammar.

The connective words (the, a, of, is, isn't) are not glue. Each has INHERENT
meaning: it IS one of the five fold-operations (B.5). They are the fixed points
of the grammar — invariant; the observer only supplies the coherence (assembly).

    fold-part   operation            word     inherent meaning
    BASE        index / determinacy  "the"    this specific one (the address)
    FIBER       class / equivalence  "a"      some member of a class
    FOLD        X² / self / equality "is"     X is its fold — the copula, the fixed point
    DEFECT      ν / negation         "isn't"  ≠, the gap, self-negation
    RETURN      conj / provenance    "of"     belonging / application / derivation

Higher grammar (tense, voice, mood) attaches above. Content words are the objects
(R, N, ν, I, P …). A sentence is an expression-tree: content at the leaves,
fixed-point words at the nodes. Generating language = walking the tree. Which
walk (subject-first, active/passive) is the observer's reading.
"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── the fixed-point words: inherent meaning = a fold-operation ────────────────
GRAMMAR = {
    "the":   ("BASE",   "index / determinacy — this specific one"),
    "a":     ("FIBER",  "class / equivalence — some member"),
    "is":    ("FOLD",   "X² / equality — the copula, the fixed point"),
    "isn't": ("DEFECT", "≠ / the gap — self-negation"),
    "of":    ("RETURN", "belonging / application — provenance"),
}

# ── content words: the objects (the only thing that varies) ───────────────────
CONTENT = {
    "P": "the seed",   "R": "self-reference",   "N": "self-negation",
    "I": "the identity", "nu": "the defect", "enrichment": "the enrichment",
}
BARE = {"nu": "defect", "enrichment": "enrichment", "fold": "fold"}


# ── the mechanism: walk the expression tree, emit words ───────────────────────
def say(t):
    if isinstance(t, str):
        return CONTENT.get(t, t)
    op = t[0]
    if op == "is":      # FOLD — the copula
        return f"{say(t[1])} is {say(t[2])}"
    if op == "isnt":    # DEFECT — negation copula
        return f"{say(t[1])} isn't {say(t[2])}"
    if op == "of":      # RETURN — "the <head> of <arg>"
        return f"the {BARE.get(t[1], t[1])} of {say(t[2])}"
    if op == "fold":    # FOLD as a noun — "the fold of X"
        return f"the fold of {say(t[1])}"
    if op == "and":     # SUM / enrichment join
        return f"{say(t[1])} and {say(t[2])}"
    if op == "not":     # NEG — "not X"
        return f"not {say(t[1])}"
    raise ValueError(op)


# the math, as expression-trees — and the sentence each one IS
SENTENCES = [
    ("P² = P",        ("is", ("fold", "P"), "P")),
    ("R² = R + I",    ("is", ("fold", "R"), ("and", "R", "I"))),
    ("N² = −I",       ("is", ("fold", "N"), ("not", "I"))),
    ("ν(R) = I",      ("is", ("of", "nu", "R"), "I")),
    ("ν(R) ≠ 0",      ("isnt", ("of", "nu", "R"), "0")),
]

print("=" * 70)
print("  the fixed-point grammar — five words, five operations")
print("=" * 70)
for w, (part, meaning) in GRAMMAR.items():
    print(f"  {w:6} = {part:7} : {meaning}")
print()
print("=" * 70)
print("  the mechanism — the equation IS the sentence")
print("=" * 70)
for eqn, tree in SENTENCES:
    print(f"  {eqn:14} ->  \"{say(tree)}\"")
print()
print("  the words carry the math; the objects are the content; the observer")
print("  chooses the walk. 'is' is the fixed point — P is its own fold, P²=P.")
