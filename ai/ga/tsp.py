#! /usr/bin/env python3

from ai.ga.genetic import GASolver

import math
import random

class TSPSolver(GASolver):
    
    def __init__(self, cities):
        self.cities = cities
        initial_pool_ = [cities]
        super().__init__(initial_pool_)

    def euc_2d(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return math.sqrt((dx ** 2) + (dy ** 2))

    def path_cost(self, variation):
        distance = 0
        limit = len(variation)
        i = 1
    
        while i < limit:
            distance += self.euc_2d(self.cities[i-1], self.cities[i])
    
        return distance

    def compute_fitness(self, variation):
        return 1 / self.path_cost(variation)

    def mutate(self, variation):
        choose_left = random.choice((True, False))
        split_index = random.choice(range(len(variation)))

        if choose_left:
            shuffleable = variation[0:split_index+1]
            maintain = variation[split_index+1:]
            mutant = []
            mutant.extend(random.shuffle(shuffleable))
            mutant.extend(maintain)
            return mutant
        else:
            shuffleable = variation[split_index+1:]
            maintain = variation[0:split_index+1]
            mutant = []
            mutant.extend(maintain)
            mutant.extend(random.shuffle(shuffleable))
            return mutant

if __name__ == "__main__":
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

    solver = TSPSolver(berlin52)
    solver.solve()
