import math

from errors import InvalidParameterException

"""
A collection of hash function algorithms.
"""

def natnum(s, base=128):
    """
    Interpret s as a natural number of the given base.
    """
    # left to right 'cause we want the hash anyway.
    return sum([(ord(s[i]) * base * i) for i in range(len(s))])

def division_hash(key, slots):
    """
    Hash via the division method where key is the data to be hashed. slots is
    an integer indicating the number of possible slots.
    """
    return natnum(key) % slots

def multiplication_hash(key, slots, multiplier):
    """
    Hash via the multiplication method.
    """
    if 0 > multiplier > 1:
        raise InvalidParameterException(multiplier)
    return math.floor(slots * ((natnum(key) * multiplier) % 1)
