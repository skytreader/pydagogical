#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.mastermind_solver import MastermindSolver, SmartermindSolver, TYPE_CONSTRUCTOR_MAP

from stats.avg import mean, standard_deviation

import argparse
import string
import sys

def print_results(numlist):
    print("Mean iterations: %s" % mean(numlist))
    print("Standard deviation: %s" % standard_deviation(numlist))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Empirical stats for mastermind solvers.")
    parser.add_argument(
        "--charset", dest="charset", type=str, default=string.ascii_lowercase,
        help="The possible characters for the hidden code."
    )
    parser.add_argument(
        "--codelen", dest="codelen", type=int, required=True,
        help="The length of the code to guess." 
    )
    parser.add_argument(
        "--simlen", type=int, default=1000, help="The number of simulations to run."
    )
    parser.add_argument(
        "--include", "-i", type=str, action="append",
        help="The types of solvers to benchmark.",
        choices=("naive", "smart", "standard", "austere", "eligible"),
        required=True
    )
    parser.add_argument(
        "--maxiters", type=int, default=0, required=False,
        help="Max number of iterations _per solver type_."
    )

    args = parser.parse_args()
    iter_counts = {i: [] for i in args.include}
    max_iters = args.maxiters if args.maxiters > 0 else float("inf")
    solvers = [TYPE_CONSTRUCTOR_MAP[i] for i in args.maxiters]

    for i in range(args.simlen):
        print("Simulating %s / %s" % (i + 1, args.simlen))
        mastermind = MasterMind(numslots=args.codelen, charset=args.charset)
        for included_solver in args.include:
            solver = TYPE_CONSTRUCTOR_MAP[included_solver](
                mastermind, max_iterations=max_iters
            )

            solver.solve()
            iter_counts[included_solver].append(solver.iters)

    for solver in args.include:
        print("=" * 60)
        print("%s solver stats:" % solver)
        print_results(iter_counts[solver])
