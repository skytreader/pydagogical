import unittest

from ..sieves import SieveOfEratosthenes

SIEVE_LIMIT = 100
CARMICHAEL_NUMBERS = (561, 1105, 1729, 2465, 2821, 6601, 8911)
PRIMES = (2, 3, 7, 11)
COMPOSITES = (4, 6, 8, 9, 10, 12)

class SieveTest(unittest.TestCase):
    
    def setUp(self):
        self.eratosthenes = SieveOfEratosthenes(SIEVE_LIMIT)
    
    def test_is_prime(self):
        for p in PRIMES:
            self.assertTrue(self.eratosthenes.is_prime(p))

        for c in COMPOSITES:
            self.assertFalse(self.eratosthenes.is_prime(c))
