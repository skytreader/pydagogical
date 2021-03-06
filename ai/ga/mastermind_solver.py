#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.genetic import GASolver, SolutionStat, StandardGASolver
from .errors import UnreachableSolutionException

import argparse
import itertools
import random
import string

import matplotlib.pyplot as plt

class SGASolver(StandardGASolver):

    def __init__(self, mastermind, max_iterations=float("inf"), pool_size=4):
        self.mastermind = mastermind
        initial_pool = [[
            random.choice(mastermind.charset) for _ in range(mastermind.numslots)
        ] for _ in range(pool_size)]

        super().__init__(initial_pool, max_iterations)

    def _should_crossover(self, parents):
        parent_scores = [self.mastermind.rate(parents[0]), self.mastermind.rate(parents[1])]

        return parent_scores[0] < 0.7 and parent_scores[1] < 0.7

    def mutate(self, variation):
        """
        [PREBYS] assumes that the variation is a binary string; this does not.
        For this version, $p_m$ for all possible $m$ is 0.5.
        """
        score = self.mastermind.rate(variation)
        t_count = len([x for x in self.mastermind.decide(variation) if not x])
        mutatables = len(variation) - t_count
        mutated_count = 0
        mutation = [c for c in variation]
        for idx, c in enumerate(mutation):
            if mutated_count == mutatables:
                break
            if random.random() > score:
                mutation[idx] = random.choice(self.mastermind.charset)
                mutated_count += 1

        return mutation

    def compute_fitness(self, variation):
        return self.mastermind.rate(variation)

class AustereSGASolver(SGASolver):
    """
    SGA solver which only allows the fittest members of current generation to be
    parents.
    """

    def _select_parents(self, ifm):
        self.current_pool = sorted([x[0] for x in ifm], key=lambda x: x[1], reverse=True)
        parents = [ifm[0][0], ifm[1][0]]
        self.current_pool = self.current_pool[:2]
        return parents

class EligibleFitnessSolver(SGASolver):
    """
    SGA solver which follows the suggestion from [BERGHMAN] and scores children
    using the concept of eligible codes.
    """

    def __init__(self, mastermind, max_iterations=float("inf"), pool_size=4):
        """
        If you can't choose wisely, choose randomly: set the expected length
        of the eligible codes subset to be half of that of pool_size (round
        down). 
        """
        super().__init__(mastermind, max_iterations, pool_size)
        self.guess_history = []
        # length of the eligible codes subset
        self.len_ecs = int(pool_size / 2)

    def play_guess(self, variation):
        """
        Appends the variation to the guess_history and returns the
        generated history entry. The history entry is a dictionary with two
        fields: "guess" and "score".
        """
        history_entry = {
            "guess": variation,
            "score": self.mastermind.decide(variation)
        }
        self.guess_history.append(history_entry)
        print("Played guess: %s" % history_entry)
        return history_entry

    def compute_fitness(self, variation):
        zero_count = 0
        for gh in self.guess_history:
            decision = MasterMind.blind_decide(variation, gh["guess"])

            if decision == gh["score"]:
                zero_count += 1

        return zero_count / len(self.guess_history)

    def _select_parents(self, population):
        if len(population) == 1:
            raise ValueError("Can't select parents with a population of 1.")
        p0 = random.choice(population)
        p1 = random.choice(population)

        while p1 == p0:
            p1 = random.choice(population)

        return (p0, p1)

    def make_new_population(self, population):
        new_pop = set()

        crossover = self._crossover(self._select_parents(population))
        for co in crossover:
            new_pop.add(tuple(co))

        p0, p1 = self._select_parents(population)
        new_pop.add(tuple(self.mutate(p0)))
        new_pop.add(tuple(self.mutate(p1)))

        p0, p1 = self._select_parents(population)
        for p in itertools.permutations(p0):
            new_pop.add(tuple(p))
        for p in itertools.permutations(p1):
            new_pop.add(tuple(p))

        return list(new_pop)

    def solve(self):
        itercount = 0
        initial_guess = [
            random.choice(self.mastermind.charset) for _ in range(self.mastermind.numslots)
        ]
        last_guess = self.play_guess(initial_guess)

        while last_guess["score"]["completely-correct"] != self.mastermind.numslots and itercount < self.max_iterations:
            population = [
                [
                    random.choice(self.mastermind.charset) for _ in range(self.mastermind.numslots)
                ] for __ in range(self.max_pool_size)
            ]
            h = 0
            eligible_codes_subset = set()

            while h < self.max_iterations and len(eligible_codes_subset) < self.len_ecs:
                population = self.make_new_population(population)
                print("new populations: %s" % population)
                genfitness = self.compute_generation_fitness(population)
                individual_fitness_map = list(zip(population, genfitness))
                
                for individual in individual_fitness_map:
                    if individual[1] == 1:
                        eligible_codes_subset.add(individual[0])
                h += 1

            random_eligible_code = random.choice(list(eligible_codes_subset))
            self.stats["fittest_per_gen"].append(self.mastermind.rate(random_eligible_code))
            last_guess = self.play_guess(random_eligible_code)
            itercount += 1

        return SolutionStat(
            answer=last_guess["guess"], ans_score=last_guess["score"],
            iters=itercount, max_iters=self.max_iterations
        )

class MastermindSolver(GASolver):

    def __init__(self, mastermind, max_iterations=float("inf")):
        self.mastermind = mastermind
        initial_pool_ = [[
            random.choice(mastermind.charset) for _ in range(mastermind.numslots)
        ]]
        super().__init__(initial_pool_, max_iterations=max_iterations)

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

    When mutating a variation, this takes into account the fitness of the
    current variation (both the "correct" score and the "misplaced" score). The
    hypothesis is that this should be statistically better than plain
    MastermindSolver above.
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

# Works under the assumption that solver constructors can all survive with
# the same form of arguments.
TYPE_CONSTRUCTOR_MAP = {
    "naive": MastermindSolver,
    "smart": SmartermindSolver,
    "standard": SGASolver,
    "austere": AustereSGASolver,
    "eligible": EligibleFitnessSolver
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and solve mastermind instances.")
    parser.add_argument(
        "--solver", "-s", help="The type of solver to use", type=str,
        choices=("naive", "smart", "standard", "austere", "eligible"), required=True
    )
    parser.add_argument(
        "--len", "-l", help="The length of the code to be guessed", type=int,
        required=True
    )
    parser.add_argument(
        "--charset", "-c", help="The allowed alphabet for the mastermind",
        type=str, default=string.ascii_lowercase, required=False
    )
    parser.add_argument(
        "--maxiters", "-m", help="The maximum number of iterations before solver forcibly quits",
        type=int, default=0, required=False
    )

    args = vars(parser.parse_args())

    _type = args["solver"]
    numslots = int(args["len"])
    charset = args["charset"]
    max_iters = int(args["maxiters"]) if args["maxiters"] > 0 else float("inf")

    mastermind = MasterMind(numslots, charset=charset)
    constructor = TYPE_CONSTRUCTOR_MAP[_type]
    solver = constructor(mastermind, max_iterations=max_iters)

    soln = solver.solve()
    print("Got solution: %s" % soln)
    print(solver.stats["fittest_per_gen"])
    plt.plot(solver.stats["fittest_per_gen"])
    plt.show()
