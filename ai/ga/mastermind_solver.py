#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.genetic import GASolver

import random
import sys

class MastermindSolver(GASolver):

    def __init__(self, mastermind):
        self.mastermind = mastermind
        initial_pool_ = [[
            random.choice(mastermind.charset) for _ in range(mastermind.numslots)
        ]]
        super().__init__(initial_pool_)

    def mutate(self, variation):
        mutate_count = random.randint(0, self.mastermind.numslots - 1)
        mutations_done = 0
        i = 0
        mutation = [c for c in variation]
        limit = len(variation)

        while mutations_done < mutate_count:
            if random.choice((True, False)):
                mutation[i % limit] = random.choice(self.mastermind.charset)
                mutations_done += 1
            i += 1

        return mutation

    def compute_fitness(self, variation):
        return self.mastermind.rate(variation)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 -m ai.ga.mastermind_solver <numslots>")
        exit(1)

    numslots = int(sys.argv[1])
    mastermind = MasterMind(numslots)
    solver = MastermindSolver(mastermind)
    solver.solve()
