import math
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from f6 import Position, distance  # noqa: E402


class PositionTests(unittest.TestCase):
    def test_vertices(self):
        self.assertEqual(Position(1, 0, 0).to_xy(), (0.0, 0.0))
        self.assertEqual(Position(0, 1, 0).to_xy(), (1.0, 0.0))
        x, y = Position(0, 0, 1).to_xy()
        self.assertAlmostEqual(x, 0.5)
        self.assertAlmostEqual(y, math.sqrt(3) / 2)

    def test_edges_of_triangle_are_unit_length(self):
        L, D, A = Position(1, 0, 0), Position(0, 1, 0), Position(0, 0, 1)
        for p, q in ((L, D), (D, A), (A, L)):
            self.assertAlmostEqual(distance(p, q), 1.0)

    def test_normalise(self):
        p = Position.from_weights(2, 2, 4, mass=1)
        self.assertAlmostEqual(p.alpha, 0.5)
        self.assertEqual(p.pole(), "Α")

    def test_rejects_bad_input(self):
        with self.assertRaises(ValueError):
            Position(0.5, 0.5, 0.5)
        with self.assertRaises(ValueError):
            Position(-0.1, 0.6, 0.5)
        with self.assertRaises(ValueError):
            Position(1, 0, 0, mass=-1)


if __name__ == "__main__":
    unittest.main()
