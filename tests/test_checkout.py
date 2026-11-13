import unittest


class Checkout(unittest.TestCase):
    def test_total(self):
        self.assertEqual(2 + 2, 5)   # bug introduced on purpose: CI must fail
