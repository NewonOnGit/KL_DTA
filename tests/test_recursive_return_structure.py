import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import numpy as np

import kl_dta


ROOT = Path(__file__).resolve().parents[1]


class RecursiveReturnStructureTests(unittest.TestCase):
    def test_seed_algebra_and_namespaced_residual(self):
        core = kl_dta.regen_core()
        I, P, R, N = core["I"], core["P"], core["R"], core["N"]

        np.testing.assert_allclose(P, R + N, atol=1e-12)
        np.testing.assert_allclose(R @ R, R + I, atol=1e-12)
        np.testing.assert_allclose(N @ N, -I, atol=1e-12)
        np.testing.assert_allclose(R @ N + N @ R, N, atol=1e-12)

        # ν_R is the linear return residual, not the global ν(X)=X²−X.
        self.assertFalse(
            np.allclose(kl_dta.return_residual(R), R @ R - R, atol=1e-12)
        )

    def test_kernel_and_projector_invariants(self):
        core = kl_dta.regen_core()
        L, N = core["L"], core["N"]
        kernel = kl_dta.return_kernel()
        projector = kl_dta.return_projector()

        self.assertEqual(np.linalg.matrix_rank(L, tol=1e-9), 2)
        self.assertEqual(kernel.shape, (2, 4))
        np.testing.assert_allclose(kl_dta.return_residual(N), 0, atol=1e-12)
        np.testing.assert_allclose(projector.T, projector, atol=1e-12)
        np.testing.assert_allclose(projector @ projector, projector, atol=1e-12)
        np.testing.assert_allclose(L @ projector, 0, atol=1e-12)

    def test_recursive_flow_lands_on_the_projector_fixed_point(self):
        initial = np.array([[1.25, -0.75], [0.5, 2.0]])
        returned, trajectory = kl_dta.recursive_return(initial)

        self.assertTrue(
            np.all(np.diff(np.asarray(trajectory)) <= 1e-12),
            "return residual must not increase",
        )
        self.assertLess(np.linalg.norm(kl_dta.return_residual(returned)), 1e-10)
        np.testing.assert_allclose(
            returned, kl_dta.project_to_return_kernel(initial), atol=1e-10
        )
        np.testing.assert_allclose(
            kl_dta.project_to_return_kernel(returned), returned, atol=1e-10
        )

        N = kl_dta.regen_core()["N"]
        returned_N, _ = kl_dta.recursive_return(N)
        np.testing.assert_allclose(returned_N, N, atol=1e-12)
        with self.assertRaises(ValueError):
            kl_dta.recursive_return(initial, eta=0.4)

    def test_structure_survives_recompute_and_store_stays_on_shell(self):
        with (ROOT / "KL_DTA.json").open(encoding="utf-8") as source:
            store = json.load(source)
        contract = store["structure"]["recursive_return"]
        self.assertIn("ν_R", contract["residual"])
        self.assertIn("ν(X)=X²−X", contract["residual"])
        self.assertIn("not the store h", contract["embedding"])

        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            shutil.copy2(ROOT / "KL_DTA.json", temp / "KL_DTA.json")
            shutil.copy2(ROOT / "kl_dta.py", temp / "kl_dta.py")
            process = subprocess.run(
                [sys.executable, "kl_dta.py", "recompute"],
                cwd=temp,
                check=True,
                capture_output=True,
                text=True,
            )
            with (temp / "KL_DTA.json").open(encoding="utf-8") as source:
                recomputed = json.load(source)

        self.assertEqual(recomputed["structure"]["recursive_return"], contract)
        self.assertIn("COMMIT  PASS", process.stdout)
        self.assertIn("M(M(F)) = M(F)", process.stdout)


if __name__ == "__main__":
    unittest.main()
