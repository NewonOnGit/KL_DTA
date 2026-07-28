"""Fold recursive return into the canonical store without adding a base record.

The fold preserves the verified PR #2 mediation axis ``h_R=diag(1,0)·N`` as a
namespaced NLP readout.  It must not be collapsed into the store's canonical
``h=diag(1,-1)·N``; that changes the frozen fixture from four contexts mapping
to two values into four contexts mapping to three.
"""

import json
from copy import deepcopy
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
DEEPENING = "recursive_return_learns_lexicon"
ATOMS = ("A1", "A8", "A9", "A10")

SPEC = {
    "is": "gradient return to the zero-residual channel, followed by a gated lexicon write",
    "state_space": "C = M2(R); P=[[0,0],[2,1]], R=(P+Pᵀ)/2, N=(P−Pᵀ)/2",
    "operator": {
        "formula": "L_R(X) = R·X + X·R − X",
        "alpha": 1,
        "objective": "E(X) = 1/2 ||L_R(X)||_F²",
    },
    "residual": (
        "ν_R(X) := L_R(X), namespaced from the global quadratic defect "
        "ν(X)=X²−X; ν_R=0 iff X∈ker(L_R)"
    ),
    "kernel": "rank(L_R)=2, dim ker(L_R)=2, and N∈ker(L_R) because {R,N}=N (A8)",
    "update": "X[t+1] = X[t]−eta·L_RᵀL_R(X[t])",
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
        "contains": ["N because {R,N}=N", "project_ker(h_R)"],
        "returned_state": "M_R(X*)=X* and X*≈M_R(X0)",
    },
    "commit": "only ν_R→0 commits a sign-aware word(X*) ↦ unit z(X*) dictionary value",
    "embedding": (
        "z(X*)=(<X*,R>,<X*,h_R>,<X*,N>), where h_R=diag(1,0)·N "
        "is not the store h=diag(1,−1)·N"
    ),
    "lexicon": {
        "commit_gate": "||L_R(X*)|| <= tolerance and ||z(X*)|| > tolerance",
        "embedding": "z(X*)=(<X*,R>,<X*,h_R>,<X*,N>)",
        "embedding_axes": ["R", "h_R", "N"],
        "axis_labels": ["A3:R", "P2:h", "A4|A8:N"],
        "kernel_axes": ["project_ker(h_R)", "N"],
        "mediation_axis": (
            "h_R=diag(1,0)·N is namespaced from the store h=diag(1,−1)·N"
        ),
        "inner_product": "<A,B>=4·tr(A·Bᵀ)",
        "on_shell_constraint": "<X*,R>=0",
        "word_threshold": 0.25,
        "key_semantics": "equal sign-aware quantized chord, not exact residue equality",
        "merge": "sum unit samples; expose normalized centroid and count",
        "persistence": (
            "runtime-derived; learned demonstration values are not canonical store data"
        ),
    },
    "verified_fixture": (
        "seed 7: four contexts return to two dictionary values; "
        "w1,w2,w4 align positive (>0.99), w3 is antipodal (<−0.98)"
    ),
    "atoms": list(ATOMS),
    "implementation": (
        "kl_dta return/config/projector/learning APIs; recursive_return_nlp.py "
        "is the pure NLP reader and executable demonstration"
    ),
    "provenance": {
        "pull_request": "NewonOnGit/KL_DTA#2",
        "integration_branches": [
            "agent/fold-recursive-return",
            "integrate-recursive-return",
        ],
        "artifact": "recursive_return_nlp.py",
        "correction": (
            "preserve PR #2 h_R=diag(1,0)·N separately from canonical "
            "store h=diag(1,−1)·N"
        ),
    },
}

DEEPENING_TEXT = (
    "recursive return learns a lexicon only after the zero-residual gate: gradient "
    "descent on 1/2||L_R(X)||² lands at the idempotent kernel projector M_R, then "
    "a sign-aware chord over (R,h_R,N) indexes a counted normalized centroid. "
    "h_R=diag(1,0)·N remains distinct from the store h=diag(1,−1)·N. N is a "
    "return axis because {R,N}=N; the R coordinate vanishes on-shell. equal keys "
    "mean the same quantized chord, not exact equality of returned residues. "
    "learned demonstration values remain derived and are not stored."
)


def fold(db):
    """Return an idempotently folded store object."""
    structure = db["structure"]
    structure["recursive_return"] = deepcopy(SPEC)
    structure["deepenings"][DEEPENING] = DEEPENING_TEXT

    chords = structure["chords"]
    chords["index"][DEEPENING] = "+".join(ATOMS)
    for names in chords["by_atom"].values():
        names[:] = [name for name in names if name != DEEPENING]
    for atom in ATOMS:
        chords["by_atom"].setdefault(atom, []).append(DEEPENING)
    return db


def main():
    db = json.loads(PATH.read_text(encoding="utf-8"))
    fold(db)
    PATH.write_text(
        json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        "recursive return internalized at structure.recursive_return; "
        f"base remains {len(db['base'])}"
    )


if __name__ == "__main__":
    main()
