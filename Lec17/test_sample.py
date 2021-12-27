from unittest import TestCase
import unittest
import sample

class TestSample(TestCase):
    def test_add(self):
        self.assertEqual(sample.add(2,3), 5)
        self.assertEqual(sample.add(0, 0), 0)
        self.assertEqual(sample.add(-2, 0), -2)
        self.assertEqual(sample.add(-2, -3), -5)
        self.assertEqual(sample.add(10, -2), 8)

    def test_mult(self):
        self.assertEqual(sample.mult(2,2), 4)
        self.assertEqual(sample.mult(2,3), 6)
        self.assertEqual(sample.mult(5, 1), 5)
        self.assertEqual(sample.mult(0, 2), 0)
        self.assertEqual(sample.mult(-2, -3), 6)


if __name__ == "__main__":
    unittest.main()