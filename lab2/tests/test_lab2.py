import unittest
from pathlib import Path

import lab
from nonlinear import solve_equation
from nonlinear_system import solve_system


ROOT = Path(__file__).resolve().parents[1]


class Lab2Tests(unittest.TestCase):
    def test_all_scalar_equations_have_positive_root(self):
        for number in range(1, 31):
            tokens = lab.read_tokens(ROOT / "examples" / "scalar" / f"{number:02d}.txt")
            result = solve_equation(number, float(tokens[2]), float(tokens[3]))
            self.assertGreater(result["simple_x"], 0)
            self.assertGreater(result["newton_x"], 0)
            self.assertLess(abs(result["simple_f"]), 1e-6)
            self.assertLess(abs(result["newton_f"]), 1e-6)
            self.assertLessEqual(len(result["newton_rows"]), len(result["simple_rows"]))

    def test_all_systems_have_positive_solution(self):
        for number in range(1, 31):
            tokens = lab.read_tokens(ROOT / "examples" / "system" / f"{number:02d}.txt")
            x0 = [float(tokens[2]), float(tokens[3])]
            result = solve_system(number, x0, float(tokens[4]))
            for value in result["simple_x"] + result["newton_x"]:
                self.assertGreater(value, 0)
            for value in result["simple_f"] + result["newton_f"]:
                self.assertLess(abs(value), 1e-6)
            self.assertLessEqual(len(result["newton_rows"]), len(result["simple_rows"]))


if __name__ == "__main__":
    unittest.main()
