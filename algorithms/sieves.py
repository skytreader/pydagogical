import math

class Sieve(object):
    
    def is_prime(self, i):
        raise NotImplementedException("is_prime is not yet implemented!")

class SieveOfEratosthenes(object):
    
    def __init__(self, size):
        self.sieve = [True for i in range(size)]
        limit = math.ceil(math.sqrt(size))

        for i in range(1, limit):
            # Remember that cell i represents integer i + 1.
            if self.sieve[i]:
                for j in range(i + i + 1, size, (i + 1)):
                    self.sieve[j] = False
    
    def is_prime(self, i):
        return self.sieve[i - 1]
