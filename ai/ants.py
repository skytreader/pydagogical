import math
import random
import sys

class TravellingSalesAnts(object):
    """
    Solve TSP via Ant Colony Optimization.
    """

    def __init__(
        self, cities, ant_count, evap_factor=0.5, backtrip_constant=1,
        max_iters=100
    ):
        self.cities = cities
        self.city_count = len(cities)
        self.ant_count = ant_count
        self.antroutes = [None for ant in range(self.ant_count)]
        self.evap_factor = evap_factor
        self.backtrip_constant = backtrip_constant
        self.max_iters = max_iters
        self.pheromone_matrix = [
            [0 for city in self.cities]
            for city in self.cities
        ]
        origpath = [i for i in range(self.city_count)]
        print("Original path cost: %s" % self.path_cost(origpath))

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

    def _ant_tour(self, antno, is_return_trip=False):
        if is_return_trip:
            print("Ant %d is a touring machine returning." % antno)
        else:
            print("Ant %d is a touring machine beginning." % antno)
        cindices = [i for i in range(len(self.cities))]
        current = random.choice(cindices)
        self.antroutes[antno] = [current]

        while len(self.antroutes[antno]) != self.city_count:
            next_city = self.get_random_next(self.antroutes[antno], current)
            dist = self.euc_2d(self.cities[current], self.cities[next_city])
            if is_return_trip:
                self.pheromone_matrix[current][next_city] += self.backtrip_constant / dist
            current = next_city
            self.antroutes[antno].append(current)

    def get_random_next(self, visited, src):
        visit_set = set(visited)
        cindices = set([i for i in range(len(self.cities))])
        choices = list(cindices - visit_set)
        choices.sort(key=lambda dest: self.pheromone_matrix[src][dest], reverse=True)
        # pick the top n based on pheromones
        n = len(choices)
        if n >= 4:
            n = int(n / 4)
        next_city = random.choice(choices[:n])
        return next_city

    def _evaporate_pheromones(self):
        for start_idx, start_point in enumerate(self.pheromone_matrix):
            for end_idx, dest_point in enumerate(start_point):
                self.pheromone_matrix[start_idx][end_idx] = (
                    (1 - self.evap_factor) * self.pheromone_matrix[start_idx][end_idx]
                )

    def _forage_rounds(self):
        for i in range(self.ant_count):
            self._ant_tour(i)
        self._evaporate_pheromones()
        for i in range(self.ant_count):
            self._ant_tour(i, is_return_trip=True)

    def solve(self):
        for i in range(self.max_iters):
            self._forage_rounds()

        mintour = float("inf")
        mindex = -1

        for idx, route in enumerate(self.antroutes):
            tour_cost = self.path_cost(route)
            if tour_cost < mintour:
                mintour = tour_cost
                mindex = idx

        print("Min path has length: %s" % mintour)
        print("Path found: %s" % self.antroutes[mindex])
        return mintour

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 %s <antcount>" % sys.argv[0])
        exit(1)

    antcount = int(sys.argv[1])
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

    solver = TravellingSalesAnts(berlin52, antcount)
    solver.solve()
