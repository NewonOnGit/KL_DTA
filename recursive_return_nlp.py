"""
recursive_return_nlp.py — executable provenance demo for structure.recursive_return.

The implementation lives in kl_dta.py and the contract lives in KL_DTA.json.
This file supplies four deterministic candidate contexts and displays the learned
runtime dictionary. A shared key means the same sign-aware quantized chord; it
does not assert exact equality of returned matrices.
"""

import numpy as np

from kl_dta import (
    learn_recursive_return,
    regen_core,
    speak_recursive_return,
)


def demo_tokens():
    """Build deterministic off-shell contexts from the canonical store core."""
    core = regen_core()
    rng = np.random.RandomState(7)
    return {
        "w1 (obs-ish)": core["N"] + 0.4 * rng.randn(2, 2),
        "w2 (obs-ish)": core["N"] - 0.5 * rng.randn(2, 2),
        "w3 (antipode)": -core["N"] + 0.3 * rng.randn(2, 2),
        "w4 (mediate)": core["h"] + 0.4 * rng.randn(2, 2),
    }


def main():
    np.set_printoptions(precision=4, suppress=True)
    dictionary = {}
    results = {}

    print("=" * 72)
    print("  RECURSIVE RETURN — canonical core, gated runtime lexicon")
    print("=" * 72)
    for token, initial in demo_tokens().items():
        result = learn_recursive_return(dictionary, initial)
        results[token] = result
        print(
            f"  {token:16} ||nu|| {result['initial_residual']:6.2f}"
            f" -> {result['residual']:.1e}  fixed:{result['fixed']}"
        )
        print(f"  {'':16} {speak_recursive_return(result)}")

    print("\n  returned-value alignment (cosine):")
    names = list(results)
    for left in names:
        lv = results[left]["value"]
        row = []
        for right in names:
            rv = results[right]["value"]
            row.append(float(lv @ rv) if lv is not None and rv is not None else float("nan"))
        print(f"   {left:16} " + "  ".join(f"{value:+.2f}" for value in row))

    print("\n" + "=" * 72)
    print("  RUNTIME DICTIONARY — quantized chord -> normalized centroid")
    print("=" * 72)
    for key, entry in dictionary.items():
        print(f"   {str(key):30} -> {np.round(entry['value'], 3).tolist()}  n={entry['count']}")
    print(
        f"\n  {len(results)} contexts committed to {len(dictionary)} chord buckets."
        " These learned values are derived smoke, not canonical store bones."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
