import unittest


class Smoke(unittest.TestCase):
    def test_service_name(self):
        self.assertEqual("dora-agent-test".upper(), "DORA-AGENT-TEST")
