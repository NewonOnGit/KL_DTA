"""Recursive return with a sign-aware learned dictionary.

The return dynamics live in :mod:`kl_dta`; this module supplies the language
readout and the deterministic four-context demonstration from PR #2.

The two residuals remain distinct:

* the store defect is ``ν(X) = X² - X``;
* the recursive-return residual is ``ν_R(X) = L_R(X)``.

Nothing runs and no dictionary mutates at import time.
"""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np

from kl_dta import (
    project_to_return_kernel,
    recursive_return,
    regen_core,
    return_kernel,
    return_projector,
    return_residual,
)


CORE = regen_core()
I = CORE["I"]
P = CORE["P"]
R = CORE["R"]
N = CORE["N"]
Lmat = CORE["L"]

# PR #2's mediation axis is intentionally namespaced.  It uses the rank-one
# selector J_R=diag(1,0), not the store's canonical reflection J=diag(1,-1).
J_RETURN = np.array([[1.0, 0.0], [0.0, 0.0]])
H_RETURN = J_RETURN @ N

AXIS_NAMES = ("A3:R", "P2:h", "A4|A8:N")


def cartan(A, B):
    """The PR's Cartan-scaled Frobenius pairing."""
    return float(4 * np.trace(np.asarray(A) @ np.asarray(B).T))


def embedding(X):
    """Three-projection semantic embedding z(X)."""
    return np.array([cartan(X, R), cartan(X, H_RETURN), cartan(X, N)])


def word(X, tau=0.25):
    """Return a sign-aware sparse chord over the semantic axes."""
    value = embedding(X)
    scale = np.linalg.norm(value)
    if scale == 0:
        return ()
    return tuple(
        f"{'+' if coefficient > 0 else '-'}{name}"
        for coefficient, name in zip(value, AXIS_NAMES)
        if abs(coefficient) / scale > tau
    )


def unit_embedding(X):
    """Return the unit semantic ray of X, or the zero embedding unchanged."""
    value = embedding(X)
    norm = np.linalg.norm(value)
    return value if norm == 0 else value / norm


def demo_contexts(seed=7):
    """Return the frozen PR #2 contexts without mutating NumPy's global RNG."""
    rng = np.random.RandomState(seed)
    return {
        "w1 (obs-ish)": N + 0.4 * rng.randn(2, 2),
        "w2 (obs-ish)": N - 0.5 * rng.randn(2, 2),
        "w3 (build-ish)": (R - I) + 0.3 * rng.randn(2, 2),
        "w4 (mediate)": H_RETURN + 0.4 * rng.randn(2, 2),
    }


def learn_contexts(
    contexts: Mapping[str, np.ndarray],
    *,
    eta=0.15,
    iters=300,
    tau=0.25,
    commit_tol=1e-10,
):
    """Return contexts to the kernel and commit their sign-aware unit rays.

    Dictionary values are normalized sums.  This keeps merging order-independent
    while preserving the PR's verified ``four contexts -> two values`` result.
    """
    sums = {}
    residues = {}
    trajectories = {}
    words = {}
    states = {}

    for name, initial in contexts.items():
        returned, trajectory = recursive_return(initial, eta=eta, iters=iters)
        residual_norm = float(np.linalg.norm(return_residual(returned)))
        if residual_norm >= commit_tol:
            raise RuntimeError(
                f"{name} did not return: ||ν_R||={residual_norm:.3e} "
                f">= commit tolerance {commit_tol:.3e}"
            )

        key = word(returned, tau=tau)
        value = unit_embedding(returned)
        sums[key] = sums.get(key, np.zeros_like(value)) + value
        residues[name] = value
        trajectories[name] = trajectory
        words[name] = key
        states[name] = returned

    dictionary = {}
    for key, total in sums.items():
        norm = np.linalg.norm(total)
        dictionary[key] = total if norm == 0 else total / norm

    return {
        "dictionary": dictionary,
        "residues": residues,
        "trajectories": trajectories,
        "words": words,
        "states": states,
    }


def run_demo(seed=7):
    """Run and return the deterministic PR #2 regression scenario."""
    return learn_contexts(demo_contexts(seed))


def main():
    """Print the readable demonstration while keeping import behavior silent."""
    np.set_printoptions(precision=4, suppress=True)
    projector = return_projector()
    result = run_demo()

    print("=" * 70)
    print("  THE ENVIRONMENT")
    print("=" * 70)
    print(f"  ker(L_R) dim = {return_kernel().shape[0]}")
    print(f"  M_R idempotent: {np.allclose(projector @ projector, projector)}")
    print(f"  N in ker(L_R): {np.allclose(return_residual(N), 0)}")

    print("\n" + "=" * 70)
    print("  THE RECURSIVE RETURN")
    print("=" * 70)
    for name, returned in result["states"].items():
        trajectory = result["trajectories"][name]
        residual = np.linalg.norm(return_residual(returned))
        fixed = np.allclose(project_to_return_kernel(returned), returned, atol=1e-10)
        print(
            f"  {name:16} ||ν_R|| {trajectory[0]:6.2f} -> {residual:.1e} "
            f"  M_R(X*)=X*:{fixed}  word={result['words'][name]}"
        )
        print(f"  {'':16} z=(<R>,<h>,<N>)={np.round(embedding(returned), 3).tolist()}")

    print("\n  alignment of returned semantic rays:")
    names = list(result["residues"])
    for left in names:
        row = "  ".join(
            f"{np.dot(result['residues'][left], result['residues'][right]):+.2f}"
            for right in names
        )
        print(f"   {left:16} {row}")

    print("\n" + "=" * 70)
    print("  THE LEARNED DICTIONARY")
    print("=" * 70)
    for key, value in result["dictionary"].items():
        print(f"   {str(key):36} -> {np.round(value, 3).tolist()}")
    print(
        f"\n  {len(result['states'])} contexts returned to "
        f"{len(result['dictionary'])} dictionary values."
    )


if __name__ == "__main__":
    main()
