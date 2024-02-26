import unittest
from test_palindrom import test_palindrom
from test_root import test_root

alltests = unittest.TestSuite()
alltests.addTest(test_palindrom("test_corners"))
alltests.addTest(test_palindrom("test_quick"))
alltests.addTest(test_root("test_corners"))
alltests.addTest(test_root("test_quick"))
unittest.TextTestRunner(verbosity=3).run(alltests)
