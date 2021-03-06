import math
import random

class SolutionStat(object):

    def __init__(self, answer, iters, max_iters, ans_score):
        self.answer = answer
        self.iters = iters
        self.max_iters = max_iters
        self.ans_score = ans_score

    def __str__(self):
        return "{'answer': '%s', 'iters': '%s', 'max_iters': '%s', 'ans_score': '%s'}" % (self.answer, self.iters, self.max_iters, self.ans_score)

class GASolver(object):

    def __init__(self, initial_pool, show_print=True, max_iterations=float("inf"), max_pool_size=8):
        """
        Where `initial_pool` is a list of variations.
        """
        self.current_pool = initial_pool
        self.max_iterations = max_iterations
        self.max_pool_size = max_pool_size
        self.show_print = show_print
        self.stats = {
            "fittest_per_gen": []
        }

    def compute_fitness(self, variation):
        """
        Should return a value of 1 if the given variation is a solution to
        whatever problem we are trying to solve, and less than 1 for non-
        solutions. Of course, the higher the value, the "closer" the variation
        is to the actual solution.
        """
        raise NotImplementedError("The fitness function for this solver is unimplemented.")

    def compute_generation_fitness(self, generation=None):
        if generation is None:
            return [self.compute_fitness(variation) for variation in self.current_pool]
        else:
            return [self.compute_fitness(variation) for variation in generation]

    def mutate(self, variation):
        """
        _Return_ a mutation of the given variation.
        """
        raise NotImpementedError("The mutation function for this solver is unimplemented.")

    def create_offspring(self):
        """
        Adds mutations to current_pool.

        This _desperately_ tries to create an offspring with a better fitness
        than its parents.
        """
        cur_max_fitness = max(self.compute_generation_fitness())

        new_pool = [self.mutate(variation) for variation in self.current_pool]
        new_gen_fittest = max(self.compute_generation_fitness(new_pool))
        itercount = 0
        if self.max_iterations != float("inf"):
            pool_mutation_limit = int(math.ceil(self.max_iterations / 10))
        else:
            pool_mutation_limit = float("inf")

        while new_gen_fittest <= cur_max_fitness and itercount < self.max_iterations:
            new_pool = [self.mutate(variation) for variation in self.current_pool]
            new_gen_fittest = max(self.compute_generation_fitness(new_pool))
            itercount += 1

        self.current_pool.extend(new_pool)
        # FIXME There are more efficient ways to do this
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
                gen_fitness = self.compute_generation_fitness()
                self.stats["fittest_per_gen"].append(max(gen_fitness))
                self.__conditional_print("Fitness of current_pool: %s" % self.compute_generation_fitness())

            itercount += 1

        if solution is None:
            max_variation = self.current_pool[0]
            max_var_fitness = self.compute_fitness(max_variation)

            for variation in self.current_pool[1:]:
                cand_var_fitness = self.compute_fitness(max_variation)
                if self.compute_fitness(variation) > cand_var_fitness:
                    max_variation = variation
                    max_var_fitness = cand_var_fitness

            print("Exhausted possibilities. Best answer has score: %s" % self.compute_fitness(max_variation))
            self.stats["fittest_per_gen"].append(max_var_fitness)
            return SolutionStat(
                answer=max_variation, ans_score=max_var_fitness,
                iters=itercount, max_iters=self.max_iterations
            )
        else:
            score = self.compute_fitness(solution)
            self.stats["fittest_per_gen"].append(score)
            return SolutionStat(
                answer=solution, ans_score=score, iters=itercount,
                max_iters=self.max_iterations
            )

class StandardGASolver(GASolver):
    """
    Implementation of an SGA based on [PREBYS].

    Differences:
    - [PREBYS] suggests to drop chromosomes in the event that population size is
      odd. We take a more merciful approach and just make room for _another_
      chromosome.
    - Most decisions here still work on the assumption that this will be used to
      solve instances of Mastermind.
    """

    def __init__(self, initial_pool, max_iterations=float("inf")):
        max_pool_size = len(initial_pool)
        if max_pool_size == 1:
            raise ValueError("We need an initial pool of at least 2 to make children.")

        if max_pool_size % 2:
            max_pool_size += 1

        super().__init__(initial_pool, max_iterations=max_iterations, max_pool_size=max_pool_size)

    def _crossover(self, parents):
        division_limit = random.randint(1, len(parents[0]) - 1)

        p0a = list(parents[0][:division_limit])
        p0b = list(parents[0][division_limit:])

        p1a = list(parents[1][:division_limit])
        p1b = list(parents[1][division_limit:])

        p0a.extend(p1b)
        p1a.extend(p0b)

        return (p0a, p1a)

    def _should_crossover(self, parents):
        """
        Override this method to tweak the behavior of your GA. Maybe you want it
        to mutate more than it should crossover?
        """
        return random.choice((True, False))

    def _select_parents(self, ifm):
        """
        Where ifm (individual fitness map) is a list of tuples where each tuple
        is a parent and its corresponding fitness score.
        """

        def all_low_fitness(ifm, threshold=0.2):
            is_all_low = True

            for i in ifm:
                is_all_zero = i[1] <= 0

                if not is_all_zero:
                    return False

            return True

        if len(ifm) < 2:
            raise ValueError("_select_parents needs to be given a population of at least 2. Given %s." % len(ifm))

        if all_low_fitness(ifm):
            individuals = [i[0] for i in ifm]
            p0 = random.choice(individuals)
            p1 = random.choice(individuals)
            
            while p1 == p0:
                p1 = random.choice(individuals)

            return [p0, p1]

        self.current_pool = [x[0] for x in ifm]
        parents = []

        while len(parents) < 2:
            for i in ifm:
                # FIXME Ugly. Rewrite.
                unchosen_ifm = [i for i in ifm if i[0] not in parents]
                if all_low_fitness(unchosen_ifm):
                    parents.append(random.choice(unchosen_ifm)[0])

                # The probability of parenthood is in direct proportion to fitness
                if i[0] not in parents and random.random() <= i[1]:
                    parents.append(i[0])

                if len(parents) == 2:
                    break

        return parents

    def solve(self):
        # This iteration limiting is not in [PREBYS] and yet we do them because
        # they make sense from an engineering perspective.
        solution = None
        itercount = 0
        
        new_generation = self.current_pool

        while solution is None and itercount < self.max_iterations:
            fittest = max(self.compute_generation_fitness())
            self.stats["fittest_per_gen"].append(fittest)
            new_generation = []

            while len(new_generation) < self.max_pool_size:
                generation_fitness = self.compute_generation_fitness()
                individual_fitness_map = list(zip(self.current_pool, generation_fitness))
                chosen_parents = self._select_parents(individual_fitness_map)

                # Randomly decide if we should crossover
                children = None
                if self._should_crossover(chosen_parents):
                    children = self._crossover(chosen_parents)
                else:
                    children = chosen_parents

                new_generation.extend([self.mutate(c) for c in children])

            self.current_pool = new_generation
            print("new generation: %s %s" % (new_generation, self.compute_generation_fitness(new_generation)))

            for child in new_generation:
                if self.compute_fitness(child) == 1:
                    solution = child
                    break

            itercount += 1

        if solution is None:
            max_variation = new_generation[0]
            max_var_fitness = self.compute_fitness(max_variation)

            for variation in self.current_pool[1:]:
                cand_var_fitness = self.compute_fitness(max_variation)
                if self.compute_fitness(variation) > cand_var_fitness:
                    max_variation = variation
                    max_var_fitness = cand_var_fitness

            print("Exhausted possibilities. Best answer has score: %s" % self.compute_fitness(max_variation))
            self.stats["fittest_per_gen"].append(max_var_fitness)
            return SolutionStat(
                answer=max_variation, ans_score=max_var_fitness,
                iters=itercount, max_iters=self.max_iterations
            )
        else:
            score = self.compute_fitness(solution)
            self.stats["fittest_per_gen"].append(score)
            return SolutionStat(
                answer=solution, ans_score=score, iters=itercount,
                max_iters=self.max_iterations
            )

class GenerationRater(object):

    def rate(self, variation):
        """
        Returns a value less than or equal to 1, in the spirit of
        `GASolver.compute_fitness`.
        """
        pass
