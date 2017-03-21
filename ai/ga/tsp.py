#! /usr/bin/env python3

from ai.ga.genetic import GASolver

import math
import random
import sys

class TSPSolver(GASolver):
    
    def __init__(self, cities, max_iterations=100, mutation_style="naive"):
        self.cities = cities
        self.mutation_style = mutation_style
        initial_pool_ = [[i for i in range(len(self.cities))]]
        self.MUTATION_FNS = {
            "naive": self.__naive_mutation,
            "stochastic2opt": self.__stochastic2opt_mutation,
            "doublebridge": self.__doublebridge_mutation
        }
        print("original pathlen %s" % self.path_cost(initial_pool_[0]))
        super().__init__(initial_pool_, max_iterations=max_iterations)

    def __naive_mutation(self, variation):
        choose_left = random.choice((True, False))
        split_index = random.choice(range(len(variation)))
        mutant = []

        if choose_left:
            shuffleable = variation[0:split_index+1]
            maintain = variation[split_index+1:]
            random.shuffle(shuffleable)
            mutant.extend(shuffleable)
            mutant.extend(maintain)
        else:
            shuffleable = variation[split_index+1:]
            maintain = variation[0:split_index+1]
            random.shuffle(shuffleable)
            mutant.extend(maintain)
            mutant.extend(shuffleable)

        return mutant

    def __stochastic2opt_mutation(self, variation):
        """
        Looks for a random subsequence in the variation and reverses them.

        See also: https://en.wikipedia.org/wiki/2-opt
        """
        perm = [variation[i] for i in range(len(variation))]
        upper_bound = len(perm) - 1
        c1, c2 = random.randint(0, upper_bound), random.randint(0, upper_bound)
        exclude = [c1]
        
        if c1 == 0:
            exclude.append(upper_bound)
        else:
            exclude.append(c1 - 1)
        
        if c1 == upper_bound:
            exclude.append(0)
        else:
            exclude.append(c1 + 1)
        
        while c2 in exclude:
            c2 = random.randint(0, upper_bound)
        
        if c2 < c1:
            c1, c2 = c2, c1
        
        perm_range = perm[c1:c2]
        perm_range.reverse()
        perm[c1:c2] = perm_range
        
        return perm

    def __doublebridge_mutation(self, variation):
        """
        Partitions the permutation into 4 subsequences and then shuffles those
        subsequences to create a new permutation.
        """
        pos1 = 1 + random.randint(0, math.floor(len(variation) / 4))
        pos2 = pos1 + 1 + random.randint(0, math.floor(len(variation) / 4))
        pos3 = pos2 + 1 + random.randint(0, math.floor(len(variation) / 4))
        p1 = variation[0:pos1] + variation[pos3:len(variation)]
        p2 = variation[pos2:pos3] + variation[pos1:pos2]
        return p1 + p2

    def euc_2d(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return math.sqrt((dx ** 2) + (dy ** 2))

    def path_cost(self, variation):
        distance = 0
        limit = len(variation)

        for i in range(limit):
            c2 = variation[(i + 1) % limit]
            distance += self.euc_2d(self.cities[variation[i]], self.cities[c2])

        return distance

    def compute_fitness(self, variation):
        return 1 / self.path_cost(variation)

    def mutate(self, variation):
        return self.MUTATION_FNS[self.mutation_style](variation)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage python3 -m ai.ga.tsp <naive|stochastic2opt|doublebridge>")
        exit(1)

    berlin52 = [
        [565,575],[25,185],[345,750],[945,685],[845,655],
        [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
        [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
        [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
        [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
        [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
        [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
        [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
        [830,610],[605,625],[595,360],[1340,725],[1740,245]
    ]

    solver = TSPSolver(berlin52, mutation_style=sys.argv[1])
    solver.solve()
