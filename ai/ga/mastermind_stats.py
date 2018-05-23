#! /usr/bin/env python3

from ai.mastermind import MasterMind
from ai.ga.mastermind_solver import MastermindSolver, SmartermindSolver, TYPE_CONSTRUCTOR_MAP

from stats.avg import mean, standard_deviation

import argparse
import string
import sys

def print_results(numlist, simlen):
    print("Solved %s / %s" % (len(numlist), simlen))
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
    parser.add_argument(
        "--strict-soln", action="store_true",
        help="If present, we will only note those runs which managed to find a solution."
    )

    args = parser.parse_args()
    stats = {i: [] for i in args.include}
    max_iters = args.maxiters if args.maxiters > 0 else float("inf")

    for i in range(args.simlen):
        print("Simulating %s / %s" % (i + 1, args.simlen))
        mastermind = MasterMind(numslots=args.codelen, charset=args.charset)
        for included_solver in args.include:
            solver = TYPE_CONSTRUCTOR_MAP[included_solver](
                mastermind, max_iterations=max_iters
            )

            soln = solver.solve()
            if args.strict_soln:
                if soln.ans_score == 1:
                    stats[included_solver].append(soln.iters)
            else:
                stats[included_solver].append(soln.iters)

    for solver in args.include:
        print("=" * 60)
        print("%s solver stats:" % solver)
        print_results(stats[solver], args.simlen)
