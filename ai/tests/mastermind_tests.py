from ..mastermind import MasterMind

import unittest

class MasterMindTests(unittest.TestCase):

    def test_rating(self):
        mm = MasterMind(8)
        mm.sequence = ['m', 't', 'k', 'n', 'k', 'z', 'q', 'f']
        guess = ['z', 'm', 'k', 'n', 'k', 'm', 'o', 'p']
        self.assertAlmostEqual(mm.rate(guess), 0.5, delta=0.001)
