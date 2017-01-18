from genetic import GASolver

import random
import string
import sys

class DumbMonkey(GASolver):

    def __init__(self, solution_string):
        self.alphabet = "".join([
            string.ascii_lowercase, string.ascii_uppercase, string.punctuation,
            " "
        ])
        self.limit = len(solution_string)
        initial_pool = "".join([
            random.choice(self.alphabet) for _ in range(self.limit)
        ])
        super(DumbMonkey, self).__init__(initial_pool=initial_pool)

    def compute_fitness(self, variation):
        """
        DumbMonkey has no notion of fitness, whatsoever.
        """
        return 0
    
    def mutate(self, variation):
        """
        Mutate is rather misleading; a better term would be "replace".
        """
        return "".join([
            random.choice(self.alphabet) for _ in range(self.limit)
        ])

class LessDumbMonkey(DumbMonkey):

    def __init__(self, solution_string):
        super(LessDumbMonkey, self).__init__(solution_string)
        self.solution_string = solution_string

    def compute_fitness(self, variation):
        correct_chars = 0

        for v, actual in zip(variation, self.solution_string):
            if v == actual:
                correct_chars += 1

        return correct_chars / self.limit

    def mutate(self, variation):
        mutate_count = random.randint(0, len(variation) - 1)
        mutant = [char for char in variation]
        for _ in range(mutate_count):
            new = random.choice(self.alphabet)
            rand_index = random.randint(0, len(mutant) - 1)
            mutant[rand_index] = new

        return "".join(mutant)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python %s <option>" % sys.argv[0])
        print("Where possible options are: dumb, lessdumb")
        exit(1)
    
    target = "When in disgrace from fortune and men's eyes,"
    
    if sys.argv[1] == "dumb":
        monkey = DumbMonkey(target)
    elif sys.argv[1] == "lessdumb":
        monkey = LessDumbMonkey(target)
    else:
        print("We don't have that kind of monkey.")
        exit(1)

    monkey.solve()
