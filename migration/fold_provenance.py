"""fold_provenance.py — the verified recursive ancient-provenance map (workflow result)."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["provenance"] = {
    "is": "the recursive ancient-provenance of the framework's atoms, adversarially verified (7-tradition "
          "workflow). status: solid-history (math + structural match survive) / plausible / interpretive. "
          "Egyptian agent failed (API) — not yet mapped.",
    "solid_history": {
        "A3 (R^2=R+I, phi/Fibonacci)": "GREEK Euclid extreme-and-mean ratio phi^2=phi+1 (c.300 BCE, the "
            "eigenvalue) + HINDU Virahanka-Hemachandra recurrence f(n)=f(n-1)+f(n-2) (c.600-1150 CE, the "
            "operator, ~600yr before Fibonacci). the tightest inheritance — a true characteristic-equation identity.",
        "A12 primes {2,3,5}": "BABYLONIAN 'regular numbers' = exactly those with prime factors only 2,3,5 = "
            "exactly the terminating-reciprocal set in base-60 (OB tables c.1900-1600 BC). exact set-equality "
            "with ||N||^2=2, ||R||^2=3, disc=5 (the SET, not the mechanism).",
        "A12 completing-the-square (operation)": "BABYLONIAN cut-and-paste (BM 13901, c.1800 BC) -> CHINESE "
            "kai fang (Nine Chapters, Liu Hui 263 CE) -> ISLAMIC al-Khwarizmi (c.830). genuine procedural lineage.",
        "A10 (recursion/self-hosting)": "ISLAMIC al-Karaji mathematical induction (c.1000) — a statement at n "
            "self-applying to n+1; the only datable NON-metaphorical self-reference.",
        "A2/A11 (the void ?, zero=marked empty position)": "MAYA shell-glyph positional zero in base-20 Long "
            "Count — a contentless symbol structurally load-bearing because it marks an empty place = ker. "
            "operative root: HINDU sunya as a number (Brahmagupta 628 CE, fixed-point behaviour a+0=a, a-a=0).",
        "A5 (P=R+N split)": "CHINESE fangcheng signed-number coefficient ARRAY (Nine Chapters c.1st CE, Liu "
            "Hui 263 CE) — earliest systematic negatives + a literal proto-matrix (loose on the operator-split).",
        "A6 (R^2+N^2=R conservation form)": "CHINESE Gougu gou^2+gu^2=xian^2 (Zhoubi) — sum-of-two-squares "
            "FORM only (the value-5 coincidence stripped as numerology).",
    },
    "by_tradition": "each tradition contributes EXACTLY ONE solid-history structural match: Babylonian {2,3,5}; "
        "Hindu the Fibonacci recurrence (A3); Greek phi (A3); Chinese completing-the-square / signed-array (A12/A5); "
        "Islamic induction (A10); Maya the empty-position zero (A2/A11).",
    "framework_own": "NOT ancient (do not overclaim): the 2x2 matrix algebra; eigenvalues/characteristic "
        "polynomials/the spectral viewpoint; the specific seed P=[[0,0],[2,1]]; the N^2=-I observer/blind-spot "
        "(the order-4 quarter-turn has no ancient ancestor — ancient cyclicity is modular return, not the i-rotation); "
        "disc=5 as a NORM decomposition 3+2 (severed from every ancient '5': 3-4-5 triangle, Gougu xian, prime-5 "
        "third); the generative reading of zero ('the void that generates'); prime-5 harmonic third (anachronistic — "
        "Pythagoreans were 3-limit; prime-5 thirds are Didymus/Ptolemy 1st-2nd c. CE).",
    "verdict": "~one-third of the framework's INGREDIENT mathematics is genuinely, recursively ancient — and it is "
        "exactly the degree-2/combinatorial part: a golden-ratio recurrence (Greek+Hindu), a privileged small-prime "
        "set (Babylonian), completing the square (Babylon->China->Islam), recursion/induction (Islamic), the "
        "empty-position zero (Maya), signed sums-of-squares (Chinese). the ARCHITECTURE (linear algebra over an "
        "asymmetric idempotent and its observer) is the framework's own. antiquity supplies the bricks; the framework "
        "lays them in a wall no ancient drew.",
}
db["structure"]["deepenings"]["ancient_provenance"] = (
    "recursive ancient provenance (verified): ~1/3 of the framework's INGREDIENT math is genuinely ancient, the "
    "degree-2/combinatorial part. solid-history matches: A3 phi/Fibonacci (Greek Euclid + Hindu Virahanka-"
    "Hemachandra); A12 primes {2,3,5} (Babylonian regular numbers, exact set-equality); completing-the-square "
    "(Babylon->China->Islam); A10 induction (Islamic al-Karaji); A2/A11 empty-position zero (Maya shell-glyph; "
    "Hindu sunya operative); A5 signed coefficient-array (Chinese fangcheng); A6 sum-of-squares FORM (Chinese Gougu). "
    "each tradition = one structural match. FRAMEWORK-OWN (not ancient): the matrix algebra, eigenvalues, the seed P, "
    "N^2=-I observer, disc=5 (norm-decomp, severed from every ancient '5'), generative-zero, prime-5 third. antiquity "
    "supplies the bricks; the architecture is the framework's own."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("ancient provenance map internalized")
