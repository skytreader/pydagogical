#! /usr/bin/env python3

from .errors import UnreachableSolutionException
from .genetic import GASolver, StandardGASolver

import argparse
import matplotlib.pyplot as plt
import random
import string
import sys

class DumbMonkey(GASolver):

    def __init__(self, solution_string, max_iterations=float("inf")):
        self.alphabet = "".join([
            string.ascii_lowercase, string.ascii_uppercase, string.punctuation,
            " "
        ])
        for char in solution_string:
            if char not in self.alphabet:
                raise UnreachableSolutionException("Character in solution not in alphabet")
        self.limit = len(solution_string)
        initial_pool = "".join([
            random.choice(self.alphabet) for _ in range(self.limit)
        ])
        super(DumbMonkey, self).__init__(initial_pool=[initial_pool], max_pool_size=1, max_iterations=max_iterations)
        self.solution_string = solution_string

    def create_offspring(self):
        len_cp_now = len(self.current_pool)
        self.current_pool = [self.mutate(variation) for variation in self.current_pool]
        assert len(self.current_pool) == len_cp_now

    def compute_fitness(self, variation):
        return 1 if variation == self.solution_string else 0
    
    def mutate(self, variation):
        """
        Mutate is rather misleading; a better term would be "replace".
        """
        spam = "".join([
            random.choice(self.alphabet) for _ in range(self.limit)
        ])
        return spam

class LessDumbMonkey(DumbMonkey):

    def __init__(self, solution_string, max_iterations=float("inf")):
        super(LessDumbMonkey, self).__init__(solution_string, max_iterations=max_iterations)
        self.solution_string = solution_string

    def create_offspring(self):
        GASolver.create_offspring(self)

    def compute_fitness(self, variation):
        correct_chars = 0

        for v, actual in zip(variation, self.solution_string):
            if v == actual:
                correct_chars += 1

        return correct_chars / self.limit

    def mutate(self, variation):
        mutate_count = random.randint(0, len(variation) - 1)
        mutant = [char for char in variation]
        # Optimization note: you can be really unlucky if the last few mistakes
        # is at the end of the string and mutate_count always comes up short.
        for _ in range(mutate_count):
            new = random.choice(self.alphabet)
            rand_index = random.randint(0, len(mutant) - 1)
            mutant[rand_index] = new

        return "".join(mutant)

class StandardMonkey(StandardGASolver):

    def __init__(self, solution_string, max_iterations=float("inf")):
        self.alphabet = "".join([
            string.ascii_lowercase, string.ascii_uppercase, string.punctuation,
            " "
        ])
        for char in solution_string:
            if char not in self.alphabet:
                raise UnreachableSolutionException("Character in solution not in alphabet")
        self.solution_string = solution_string
        self.limit = len(self.solution_string)
        initial_pool = [
            [
                random.choice(self.alphabet) for _ in self.solution_string
            ] for __ in range(2)
        ]
        print("Initial pool: %s" % initial_pool)
        super().__init__(initial_pool, max_iterations=max_iterations)

    def compute_fitness(self, variation):
        correct_chars = 0

        for v, actual in zip(variation, self.solution_string):
            if v == actual:
                correct_chars += 1

        return correct_chars / self.limit

    def mutate(self, variation):
        mutate_count = random.randint(0, len(variation) - 1)
        mutant = [char for char in variation]
        # Optimization note: you can be really unlucky if the last few mistakes
        # is at the end of the string and mutate_count always comes up short.
        for _ in range(mutate_count):
            new = random.choice(self.alphabet)
            rand_index = random.randint(0, len(mutant) - 1)
            mutant[rand_index] = new

        return mutant
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Infinite monkeys theorem.")
    parser.add_argument(
        "--monkey", "-m", help="The type of monkey to use.", type=str,
        choices=("dumb", "lessdumb", "standard"), required=True
    )
    parser.add_argument(
        "--limit", "-l", help="The number of iterations to do before giving up.",
        type=int, default=0, required=False
    )

    args = vars(parser.parse_args())

    _type = args["monkey"]
    max_iters = args["limit"] if args["limit"] > 0 else float("inf")
    
    target = "When in disgrace from fortune and men's eyes,"
    
    if _type == "dumb":
        monkey = DumbMonkey(target, max_iters)
    elif _type == "lessdumb":
        monkey = LessDumbMonkey(target, max_iters)
    elif _type == "standard":
        monkey = StandardMonkey(target, max_iters)
    else:
        print("We don't have that kind of monkey.")
        exit(1)

    soln = monkey.solve()
    plt.plot(monkey.stats["fittest_per_gen"])
    plt.show()
