"""
fold_recursive_return.py — internalize the PR #2 investigation without adding a
sixth base record.

The canonical store keeps the algorithm and its invariants. Learned dictionary
values remain runtime-derived outputs; synthetic demonstration values are not
written into KL_DTA.json.
"""

import json
from copy import deepcopy
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
DEEPENING = "recursive_return_learns_lexicon"
ATOMS = ("A1", "A8", "A9", "A10")

SPEC = {
    "is": "gradient return to the zero-residual channel, followed by a gated lexicon write",
    "state_space": "M2(R)",
    "operator": {
        "formula": "L_R(X) = R X + X R - X",
        "alpha": 1,
        "objective": "E(X) = 1/2 ||L_R(X)||_F^2",
    },
    "update": "X[t+1] = X[t] - eta L_R^T L_R X[t]",
    "solver": {
        "eta": 0.15,
        "max_iterations": 300,
        "tolerance": 1e-10,
        "svd_tolerance": 1e-9,
    },
    "fixed_point": {
        "map": "M_R = orthogonal projector onto ker(L_R)",
        "law": "M_R(M_R(X)) = M_R(X)",
        "kernel_dimension": 2,
        "contains": ["N because {R,N}=N", "project_ker(h)"],
    },
    "lexicon": {
        "commit_gate": "||L_R(X*)|| <= tolerance and ||z(X*)|| > tolerance",
        "embedding": "z(X*) = (<X*,R>, <X*,h>, <X*,N>)",
        "embedding_axes": ["R", "h", "N"],
        "axis_labels": ["A3:R", "h", "A4|A8:N"],
        "kernel_axes": ["project_ker(h)", "N"],
        "on_shell_constraint": "<X*,R> = 0",
        "word_threshold": 0.25,
        "key_semantics": "equal sign-aware quantized chord, not exact residue equality",
        "merge": "sum unit samples; expose normalized centroid and count",
        "persistence": "runtime-derived; learned demonstration values are not canonical store data",
    },
    "atoms": list(ATOMS),
    "provenance": {
        "pull_request": "NewonOnGit/KL_DTA#2",
        "artifact": "recursive_return_nlp.py",
        "correction": "use canonical J=diag(1,-1) and h=JN from regen_core",
    },
}

DEEPENING_TEXT = (
    "recursive return learns a lexicon only after the zero-residual gate: gradient descent on "
    "1/2||L_R(X)||^2 lands at the idempotent kernel projector M_R, then a sign-aware chord over "
    "(R,h,N) indexes a counted normalized centroid. N is a return axis because {R,N}=N; the R "
    "coordinate vanishes on-shell. equal keys mean the same quantized chord, not exact equality "
    "of returned residues. learned demonstration values remain derived and are not stored."
)


def fold(db):
    """Return an idempotently folded store object."""
    structure = db["structure"]
    structure["recursive_return"] = deepcopy(SPEC)
    structure["deepenings"][DEEPENING] = DEEPENING_TEXT

    chords = structure["chords"]
    chords["index"][DEEPENING] = "+".join(ATOMS)
    for atom, names in chords["by_atom"].items():
        chords["by_atom"][atom] = [name for name in names if name != DEEPENING]
    for atom in ATOMS:
        names = chords["by_atom"].setdefault(atom, [])
        names.append(DEEPENING)
    return db


def main():
    db = json.loads(PATH.read_text(encoding="utf-8"))
    fold(db)
    PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
    print("recursive return internalized at structure.recursive_return; base remains", len(db["base"]))


if __name__ == "__main__":
    main()
