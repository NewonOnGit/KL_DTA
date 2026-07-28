from pathlib import Path
import subprocess
import sys
import unittest

import numpy as np

import recursive_return_nlp as nlp


ROOT = Path(__file__).resolve().parents[1]
POSITIVE = ("+P2:h", "+A4|A8:N")
NEGATIVE = ("-P2:h", "-A4|A8:N")


class RecursiveReturnNLPRegressionTests(unittest.TestCase):
    def test_import_is_silent(self):
        process = subprocess.run(
            [sys.executable, "-c", "import recursive_return_nlp"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(process.stdout, "")
        self.assertEqual(process.stderr, "")

    def test_seed_seven_four_contexts_return_to_two_values(self):
        result = nlp.run_demo(seed=7)

        self.assertEqual(len(result["states"]), 4)
        self.assertEqual(set(result["dictionary"]), {POSITIVE, NEGATIVE})
        self.assertEqual(result["words"]["w1 (obs-ish)"], POSITIVE)
        self.assertEqual(result["words"]["w2 (obs-ish)"], POSITIVE)
        self.assertEqual(result["words"]["w4 (mediate)"], POSITIVE)
        self.assertEqual(result["words"]["w3 (build-ish)"], NEGATIVE)

        for value in result["dictionary"].values():
            self.assertAlmostEqual(float(np.linalg.norm(value)), 1.0, places=12)

    def test_alignment_and_antipodal_sign_are_preserved(self):
        residues = nlp.run_demo(seed=7)["residues"]
        positive_names = ["w1 (obs-ish)", "w2 (obs-ish)", "w4 (mediate)"]
        negative = residues["w3 (build-ish)"]

        for index, left in enumerate(positive_names):
            for right in positive_names[index + 1 :]:
                self.assertGreater(float(residues[left] @ residues[right]), 0.99)
            self.assertLess(float(residues[left] @ negative), -0.98)

        returned = nlp.run_demo(seed=7)["states"]["w1 (obs-ish)"]
        self.assertEqual(nlp.word(returned), POSITIVE)
        self.assertEqual(nlp.word(-returned), NEGATIVE)

    def test_learning_is_repeatable_and_has_no_global_dictionary_state(self):
        first = nlp.run_demo(seed=7)["dictionary"]
        second = nlp.run_demo(seed=7)["dictionary"]
        self.assertEqual(set(first), set(second))
        for key in first:
            np.testing.assert_allclose(first[key], second[key], atol=1e-12)

    def test_dictionary_commit_requires_return_to_zero(self):
        with self.assertRaises(RuntimeError):
            nlp.learn_contexts({"unreturned": np.ones((2, 2))}, iters=0)


if __name__ == "__main__":
    unittest.main()
