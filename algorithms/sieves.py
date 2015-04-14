class Sieve(object):
    
    def is_prime(self, i):
        raise NotImplementedException("is_prime is not yet implemented!")

class SieveOfEratosthenes(object):
    
    def __init__(self, size):
        self.sieve = [True for i in range(size)]
    
    def is_prime(self, i):
        return self.sieve[i - 1]
