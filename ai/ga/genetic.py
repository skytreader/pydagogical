class GASolver(object):

    def __init__(self, initial_pool, show_print=True, max_iterations=float("inf"), max_pool_size=8):
        """
        Where `initial_pool` is a list of variations.
        """
        self.current_pool = initial_pool
        self.max_iterations = max_iterations
        self.max_pool_size = max_pool_size
        self.show_print = show_print

    def compute_fitness(self, variation):
        """
        Should return a value of 1 if the given variation is a solution to
        whatever problem we are trying to solve, and less than 1 for non-
        solutions. Of course, the higher the value, the "closer" the variation
        is to the actual solution.
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
        print("create_offspring: current_pool len is %d" % len(self.current_pool))
        cur_max_fitness = max(self.__compute_generation_fitness())

        new_pool = [self.mutate(variation) for variation in self.current_pool]
        new_gen_fittest = max(self.__compute_generation_fitness(new_pool))
        while new_gen_fittest <= cur_max_fitness:
            new_pool = [self.mutate(variation) for variation in self.current_pool]
            new_gen_fittest = max(self.__compute_generation_fitness(new_pool))

        self.current_pool.extend(new_pool)
        # There are more efficient ways to do this
        self.current_pool.sort(key=self.compute_fitness, reverse=True)
        self.current_pool = self.current_pool[:self.max_pool_size]

    def __conditional_print(self, s):
        if self.show_print:
            print(s)

    def solve(self):
        solution = None
        itercount = 0

        while solution is None and itercount < self.max_iterations:
            self.__conditional_print("Current pool is: %s" % self.current_pool)
            for variation in self.current_pool:
                if self.compute_fitness(variation) == 1:
                    solution = variation
                if solution is not None:
                    break

            if solution is None:
                self.create_offspring()
                self.__conditional_print("Fitness of current_pool: %s" % self.__compute_generation_fitness())

            itercount += 1

        if solution is None:
            max_variation = self.current_pool[0]

            for variation in self.current_pool[1:]:
                if self.compute_fitness(variation) > self.compute_fitness(max_variation):
                    max_variation = variation

            return max_variation
        else:
            return solution

class GenerationRater(object):

    def rate(self, variation):
        """
        Returns a value less than or equal to 1, in the spirit of
        `GASolver.compute_fitness`.
        """
        pass
