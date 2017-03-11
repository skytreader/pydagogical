#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.genetic import GASolver
from .errors import UnreachableSolutionException

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

class SmartermindSolver(MastermindSolver):
    """
    Mastermind solver that "breaks" the conventions of GASolver, in the interest
    of being smarter.
    """

    def __pick_distinct_subset(self, universe, length, autoexclude=None):
        """
        Choose a distinct subset from universe of the specified length.
        autoexclude is assumed to be a subset of universe that can no longer be
        chosen. If it is impossible to pick a subset of the specified length,
        UnreachableSolutionException is raised.

        universe - an ordered iterable
        length
        autoexclude - an iterable of indices to exclude from the return value

        Returns a set containing the indices of the chosen subset.
        """
        autoexclude = [] if autoexclude is None else autoexclude

        uniset = set([idx for idx in range(len(universe))])
        exclude_set = set(autoexclude)
        choices = list(uniset - exclude_set)

        if len(choices) < length:
            raise UnreachableSolutionException("Can't pick a subset of length %d with the given constraints." % length)

        distinct_subset = set()

        while len(distinct_subset) < length:
            distinct_subset.add(random.choice(choices))

        return distinct_subset

    def mutate(self, variation):
        varclone = [x for x in variation]
        variation_decision = self.mastermind.decide(variation)
        t_count = sum([1 for d in variation_decision if d])
        f_count = sum([1 for d in variation_decision if not d])

        guess_correct = self.__pick_distinct_subset(variation, t_count)
        guess_misplaced = self.__pick_distinct_subset(variation, f_count, autoexclude=guess_correct)

        untouchables = guess_correct.union(guess_misplaced)
        varindices = set(range(len(variation)))
        replaceables = varindices - untouchables

        for misplaced in guess_misplaced:
            swap_index = self.__pick_distinct_subset(variation, 1, guess_correct).pop()
            varclone[misplaced], varclone[swap_index] = varclone[swap_index], varclone[misplaced]

            if swap_index in replaceables:
                replaceables.remove(swap_index)
                replaceables.add(misplaced)

        for replace in replaceables:
            varclone[replace] = random.choice(self.mastermind.charset)

        return varclone

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 -m ai.ga.mastermind_solver (naive|smart) <numslots>")
        exit(1)

    _type = sys.argv[1]
    numslots = int(sys.argv[2])

    mastermind = MasterMind(numslots)

    if _type == "naive":
        solver = MastermindSolver(mastermind)
    elif _type == "smart":
        solver = SmartermindSolver(mastermind)
    else:
        print("type can only be either naive or smart")
        exit()

    solver.solve()
