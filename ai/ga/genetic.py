class GASolver(object):

    def __init__(self, initial_pool, max_iterations=float("inf"), max_pool_size=8):
        self.current_pool = initial_pool
        self.max_iterations = max_iterations
        self.max_pool_size = max_pool_size

    def compute_fitness(self, variation):
        """
        Should return a value of 1 if the given variation is a solution to
        whatever problem we are trying to solve.
        """
        pass

    def __compute_generation_fitness(self, generation=None):
        if generation is None:
            return [self.compute_fitness(variation) for variation in self.current_pool]
        else:
            return [self.compute_fitness(variation) for variation in generation]

    def mutate(self, variation):
        pass

    def create_offspring(self):
        """
        Adds mutations to current_pool.
        """
        cur_max_fitness = max(self.__compute_generation_fitness())
        print("Creating offspring. Must beat fitness of %s." % cur_max_fitness)

        new_pool = [self.mutate(variation) for variation in self.current_pool]
        new_gen_fittest = max(self.__compute_generation_fitness(new_pool))
        while new_gen_fittest <= cur_max_fitness:
            print("Got a generation whose fittest is %s." % new_gen_fittest)
            new_pool = [self.mutate(variation) for variation in self.current_pool]
            new_gen_fittest = max(self.__compute_generation_fitness(new_pool))
        print("loop end with fiitest being %s" % new_gen_fittest)

        self.current_pool.extend(new_pool)
        print("1. current pool looks like %s fit %s" % (self.current_pool, self.__compute_generation_fitness()))
        # There are more efficient ways to do this
        self.current_pool.sort(key=self.compute_fitness, reverse=True)
        self.current_pool = self.current_pool[:self.max_pool_size]
        print("2. current pool looks like %s fit %s" % (self.current_pool, self.__compute_generation_fitness()))

    def solve(self):
        solution = None
        itercount = 0

        while solution is None and itercount < self.max_iterations:
            print("Current pool is: %s" % self.current_pool)
            for variation in self.current_pool:
                if self.compute_fitness(variation) == 1:
                    solution = variation
                if solution is not None:
                    break

            if solution is None:
                self.create_offspring()
                print("Fitness of current_pool: %s" % self.__compute_generation_fitness())

            itercount += 1

        if solution is None:
            max_variation = self.current_pool[0]

            for variation in self.current_pool[1:]:
                if self.compute_fitness(variation) > self.compute_fitness(max_variation):
                    max_variation = variation

            return max_variation
        else:
            return solution
