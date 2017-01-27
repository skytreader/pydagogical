#! /usr/bin/env python3

from ai.ga.genetic import GenerationRater

import random
import string

class MasterMind(GenerationRater):
    
    def __init__(self, numslots, charset=string.ascii_lowercase):
        self.numslots = numslots
        self.charset = charset
        self.sequence = [random.choice(charset) for _ in range(numslots)]
        print("Mastermind: The sequence is %s" % self.sequence)
    
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

    def rate(self, variation):
        decision = self.decide(variation)
        return sum([1 if d else 0.5 for d in decision]) / len(variation)
