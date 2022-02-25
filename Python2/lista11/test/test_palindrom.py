import unittest
import context
from palindrom import palindrom


class test_palindrom(unittest.TestCase):

    quick_cases = ['a'*i for i in range(10)]

    def test_quick(self):
        for case in self.quick_cases:
            self.assertTrue(palindrom(case))

    def test_corners(self):
        self.assertTrue(palindrom("Eine güldne, gute Tugend: Lüge nie!"))
        self.assertTrue(palindrom("Ala"))
        self.assertTrue(palindrom("A"))
        self.assertTrue(palindrom("abc ccc cba"))
        self.assertTrue(palindrom("a         a"))


if __name__ == '__main__':
    unittest.main()
