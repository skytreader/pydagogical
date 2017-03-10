#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.genetic import GASolver
from errors import UnreachableSolutionException

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

class SmartermindSolver(MasterMindSolver)
    """
    Mastermind solver that "breaks" the conventions of GASolver, in the interest
    of being smarter.
    """

    def __pick_distinct_subset(self, universe, length, autoexclude=None):
        """
        Choose a distinct subset from universe of the specified length.
        autoexclude is assumed to be a subset of universe that can no longer be
        chosen. If it is already at least the specified length, it becomes the
        return value.

        universe - an iterable
        length
        autoexclude - an iterable

        Returns a set.
        """

        if len(autoexclude) >= length:
            return set(autoexclude)

        uniset = set(universe)
        exclude_set = set(autoexclude)
        choices = uniset - exclude_set

        if len(choices) < length:
            raise UnreachableSolutionException("Can't pick a subset of length %d with the given constraints." % length)

        distinct_subset = set()

        while len(distinct_subset) < length:
            item = random.choice(universe)
            if item not in distinct_subset:
                distinct_subset.add(item)

        return distinct_subset

    def mutate(self, variation):
        variation_decision = self.mastermind.decide(variation)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 -m ai.ga.mastermind_solver <numslots>")
        exit(1)

    numslots = int(sys.argv[1])
    mastermind = MasterMind(numslots)
    solver = MastermindSolver(mastermind)
    solver.solve()
