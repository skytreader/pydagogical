from ..mastermind import MasterMind

import unittest

class MasterMindTests(unittest.TestCase):

    def test_rating(self):
        mm = MasterMind(8)
        mm.sequence = ['m', 't', 'k', 'n', 'k', 'z', 'q', 'f']
        guess1 = ['z', 'm', 'k', 'n', 'k', 'm', 'o', 'p']
        self.assertAlmostEqual(mm.rate(guess1), 0.5, delta=0.001)

        mm.sequence = ['o', 'j', 'n', 'h', 'd', 'o', 'u', 'h']
        guess2 = ['o', 'j', 'n', 'y', 'd', 's', 'u', 'h']
        self.assertAlmostEqual(mm.rate(guess2), 6/8, delta=0.001)
