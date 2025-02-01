import unittest
from core.point import Point

class TestPoint(unittest.TestCase):

    def test_addition(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)

    def test_subtraction(self):
        p1 = Point(5, 5)
        p2 = Point(2, 3)
        result = p1 - p2
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 2)

    def test_multiplication_scalar(self):
        p = Point(3, 4)
        result = p * 2
        self.assertEqual(result.x, 6)
        self.assertEqual(result.y, 8)

    def test_multiplication_elementwise(self):
        p1 = Point(2, 3)
        p2 = Point(4, 5)
        result = p1 * p2
        self.assertEqual(result.x, 8)
        self.assertEqual(result.y, 15)

    def test_division_scalar(self):
        p = Point(6, 8)
        result = p / 2
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 4)

    def test_division_elementwise(self):
        p1 = Point(8, 9)
        p2 = Point(2, 3)
        result = p1 / p2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 3)

    def test_division_by_zero(self):
        p = Point(4, 5)
        with self.assertRaises(ZeroDivisionError):
            p / 0

    def test_elementwise_division_by_zero(self):
        p1 = Point(4, 5)
        p2 = Point(2, 0)
        with self.assertRaises(ZeroDivisionError):
            p1 / p2

    def test_repr(self):
        p = Point(3, 4)
        self.assertEqual(repr(p), "Point(3, 4)")

    def test_str(self):
        p = Point(3, 4)
        self.assertEqual(str(p), "(3, 4)")

    def test_clone(self):
        p = Point(3, 4).clone()
        p_clone = p.clone()
        self.assertEqual(p.x, p_clone.x)
        self.assertEqual(p.y, p_clone.y)
        self.assertIsNot(p, p_clone)

if __name__ == "__main__":
    unittest.main()