import unittest
import context
from root import pierwiastek
from math import floor


def troot(n):
    return floor(n**0.5)


class test_root(unittest.TestCase):

    quick_cases = [(n, troot(n)) for n in range(0, 100)]

    def test_quick(self):
        for arg, res in self.quick_cases:
            self.assertEqual(pierwiastek(arg), res)

    lots_cases = [(n, troot(n)) for n in range(0, 10**6, 100)]

    def test_lots(self):
        for arg, res in self.lots_cases:
            self.assertEqual(pierwiastek(arg), res)

    def test_corners(self):
        self.assertEqual(pierwiastek(-1), 0)
        self.assertEqual(pierwiastek(-10), 0)
        self.assertEqual(pierwiastek(-100000), 0)
        with self.assertRaises(TypeError):
            pierwiastek("123")
            pierwiastek(None)


if __name__ == '__main__':
    unittest.main()
