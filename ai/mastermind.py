#! /usr/bin/env python3

import random
import string

class MasterMind(object):
    
    def __init__(self, numslots, charset=string.ascii_lowercase):
        self.numslots = numslots
        self.charset = charset

    def initialize(self):
        self.sequence = [random.choice(self.charset) for _ in range(self.numslots)]
    
    def decide(self, guess):
        """
        True for a correct symbol in the correct location.
        False for a correct symbol in the wrong location.
        """
        verdict = []
        if len(guess) != self.numslots:
            raise Exception("Invalid guess")

        seqset = set(self.sequence)
        
        for g, seq in zip(guess, self.sequence):
            if g == seq:
                verdict.insert(0, True)
                seqset.remove(g)

        for g in guess:
            if g in seqset:
                verdict.insert(0, False)

        return verdict
