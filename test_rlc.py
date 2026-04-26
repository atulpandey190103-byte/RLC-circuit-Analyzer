 import unittest
from rlc import RLC

class TestRLC(unittest.TestCase):

    def test_impedance(self):
        rlc = RLC(10, 0.1, 1e-6, 50)
        self.assertTrue(rlc.impedance() > 0)

    def test_resonance(self):
        rlc = RLC(10, 0.1, 1e-6, 50)
        fr = rlc.resonant_frequency()
        self.assertTrue(fr > 0)

if __name__ == "__main__":
    unittest.main()
