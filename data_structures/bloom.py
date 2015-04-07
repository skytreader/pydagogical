class BloomFilter(object):
    
    def __init__(self, bitcount, hashfuns):
        """
        Initialize a Bloom Filter.

        bitcount - integer indicating how many bits do we allocate.
        hashfuns - an iterable of functions for hashing. Should each return an
          integer.
        """
        self.bit_array = [False for i in range(bitcount)]
        self.hashfuns = hashfuns

    def add(self, element):
        for f in hashfuns:
            self.bit_array[f(element)] = True

    def query(self, element):
        for f in hashfuns:
            if not self.bit_array[f(element)]:
                return False

        return True
