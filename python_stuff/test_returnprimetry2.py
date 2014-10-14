import unittest
from returnprimetry2 import is_prime

class PrimesTestCase(unittest.TestCase):

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()

