import sys
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import kl_dta


class RecursiveReturnTests(unittest.TestCase):
    def setUp(self):
        self.core = kl_dta.regen_core()

    def test_store_core_and_return_axis_stay_distinct(self):
        expected_j = np.array([[1.0, 0.0], [0.0, -1.0]])
        self.assertTrue(np.array_equal(self.core["J"], expected_j))
        self.assertTrue(np.array_equal(self.core["h"], expected_j @ self.core["N"]))
        _, h_return, _ = kl_dta.recursive_return_axes()
        self.assertFalse(np.array_equal(h_return, self.core["h"]))
        self.assertTrue(
            np.array_equal(
                h_return,
                np.array([[1.0, 0.0], [0.0, 0.0]]) @ self.core["N"],
            )
        )

    def test_kernel_and_projector_invariants(self):
        projector, basis = kl_dta.recursive_return_projector()
        self.assertEqual(basis.shape, (2, 4))
        self.assertTrue(np.allclose(projector @ projector, projector, atol=1e-10))
        self.assertTrue(np.allclose(self.core["L"] @ projector, 0, atol=1e-10))
        self.assertTrue(
            np.allclose(self.core["L"] @ self.core["N"].reshape(-1), 0, atol=1e-10)
        )
        for vector in basis:
            embedding = kl_dta.recursive_return_embedding(vector.reshape(2, 2))
            self.assertAlmostEqual(float(embedding[0]), 0.0, places=9)

    def test_descent_converges_to_orthogonal_projection(self):
        initial = np.array([[0.4, -1.5], [0.7, 0.2]])
        result = kl_dta.recursive_return_result(initial)
        projector, _ = kl_dta.recursive_return_projector()
        expected = (projector @ initial.reshape(-1)).reshape(2, 2)

        self.assertTrue(result["converged"])
        self.assertTrue(result["fixed"])
        self.assertLessEqual(result["residual"], 1e-10)
        self.assertTrue(np.allclose(result["state"], expected, atol=1e-9))
        self.assertTrue(
            np.all(np.diff(np.asarray(result["trajectory"])) <= 1e-12),
            msg="the residual trajectory must not climb",
        )

    def test_rejects_unstable_eta(self):
        with self.assertRaisesRegex(ValueError, "eta must satisfy"):
            kl_dta.recursive_return(self.core["R"], eta=0.4)

    def test_commit_gate_rejects_nonconvergence_and_zero_direction(self):
        dictionary = {}
        off_shell = kl_dta.learn_recursive_return(
            dictionary, self.core["R"], max_iterations=0
        )
        self.assertFalse(off_shell["committed"])
        self.assertEqual(dictionary, {})

        zero = kl_dta.learn_recursive_return(dictionary, np.zeros((2, 2)))
        self.assertTrue(zero["converged"])
        self.assertFalse(zero["committed"])
        self.assertIn("zero embedding", zero["reason"])
        self.assertEqual(dictionary, {})

    def test_quantized_chords_merge_with_counted_centroid(self):
        dictionary = {}
        n, h, r = self.core["N"], kl_dta.recursive_return_axes()[1], self.core["R"]
        first = kl_dta.learn_recursive_return(dictionary, n + 0.02 * h + 0.3 * r)
        second = kl_dta.learn_recursive_return(dictionary, 2 * n - 0.01 * h - 0.2 * r)
        antipode = kl_dta.learn_recursive_return(dictionary, -n + 0.2 * r)

        self.assertTrue(first["committed"] and second["committed"] and antipode["committed"])
        self.assertEqual(first["word"], second["word"])
        self.assertNotEqual(first["word"], antipode["word"])
        self.assertEqual(len(dictionary), 2)

        merged = dictionary[first["word"]]
        self.assertEqual(merged["count"], 2)
        self.assertAlmostEqual(float(np.linalg.norm(merged["value"])), 1.0, places=10)
        self.assertTrue(np.allclose(merged["sum"], first["value"] + second["embedding"] /
                                    np.linalg.norm(second["embedding"]), atol=1e-10))
        self.assertIn("count=2", kl_dta.speak_recursive_return(second))


if __name__ == "__main__":
    unittest.main()
