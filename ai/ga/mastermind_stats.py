#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.mastermind_solver import MastermindSolver, SmartermindSolver

from stats.avg import mean, standard_deviation

import argparse
import string
import sys

def print_results(numlist):
    print("Mean iterations: %s" % mean(numlist))
    print("Standard deviation: %s" % standard_deviation(numlist))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Empirical stats for mastermind solvers.")
    parser.add_argument("--charset", dest="charset", type=str, help="The possible characters for the hidden code.", default=string.ascii_lowercase)
    parser.add_argument("--codelen", dest="codelen", type=int, help="The length of the code to guess.", required=True)
    parser.add_argument("--simlen", dest="simlen", type=int, help="The number of simulations to run.", default=1000)

    args = parser.parse_args()
    naive_iters = []
    smart_iters = []

    for i in range(args.simlen):
        print("Simulating %s / %s" % (i + 1, args.simlen))
        mastermind = MasterMind(numslots=args.codelen, charset=args.charset)
        naive_solver = MastermindSolver(mastermind)
        smart_solver = SmartermindSolver(mastermind)

        naive_soln = naive_solver.solve()
        smart_soln = smart_solver.solve()

        naive_iters.append(naive_soln.iters)
        smart_iters.append(smart_soln.iters)

    print("=" * 60)
    print("Naive solver stats:")
    print_results(naive_iters)
    print("=" * 60)
    print("Smart solver stats:")
    print_results(smart_iters)
