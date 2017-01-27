#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.genetic import GASolver

import random

class MastermindSolver(GASolver):

    def __init__(self, mastermind):
        self.mastermind = mastermind
        initial_pool = [
            random.choice(mastermind.charset) for _ in range(mastermind.numslots)
        ]
        super().__init__(self, initial_pool)

    def mutate(self, variation):
        mutate_count = random.randint(0, self.mastermind.numslots - 1)
