#! /usr/bin/env python3

from ai.ga.genetic import GenerationRater

import random
import string

class MasterMind(GenerationRater):
    
    def __init__(self, numslots, charset=string.ascii_lowercase):
        self.numslots = numslots
        self.charset = charset
        self._sequence = [random.choice(charset) for _ in range(numslots)]
        print("Mastermind: The sequence is %s" % self.sequence)

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, seq):
        """
        This should only be called by unit tests!
        """
        self._sequence = seq
        print("Mastermind: The sequence is %s" % self.sequence)
    
    def decide(self, guess):
        return MasterMind.blind_decide(self.sequence, guess)

    @staticmethod
    def blind_decide(sequence, guess):
        """
        Returns a dictionary with two fields: "completely-correct" and
        "symbol-correct" and whose values are counts of symbols in the guess
        which do precisely that.
        """
        verdict = {
            "completely-correct": 0,
            "symbol-correct": 0
        }
        if len(guess) != len(sequence):
            raise Exception("Invalid guess")

        seqclone = [s for s in sequence]
        guessclone = [s for s in guess]
        
        for g, seq in list(zip(guessclone, sequence)):
            if g == seq:
                verdict["completely-correct"] += 1

                # FIXME conditional looks extraneous
                if g in seqclone:
                    seqclone.remove(g)
                guessclone.remove(g)

        for g in guessclone:
            if g in seqclone:
                verdict["symbol-correct"] += 1
                seqclone.remove(g)

        return verdict

    def rate(self, variation):
        decision = self.decide(variation)
        return ((1 * decision["completely-correct"]) + (0.5 * decision["symbol-correct"])) / len(variation)
