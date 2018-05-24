#! /usr/bin/env python3
from ai.ants import TravellingSalesAnts
from stats.avg import mean, standard_deviation

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="statistics for ant colonies.")
    parser.add_argument(
        "--ants", "-a", type=int, default=100, required=False,
        help="The number of ants in our colony."
    )
    parser.add_argument(
        "--iters", "-i", type=int, default=100, required=False,
        help="The number of runs our algorithm will do."
    )
    parser.add_argument(
        "--samplesize", "-s", type=int, default=100, required=False,
        help="The number of samples to make a statistic of."
    )

    args = parser.parse_args()
    if args.ants <= 0 or args.iters <= 0 or args.samplesize <= 0:
        print("ants, iters, and samplesize should all be greater than 0")
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
    solutions = []

    for _ in range(args.samplesize):
        solver = TravellingSalesAnts(berlin52, args.ants, max_iters=args.iters)
        solutions.append(solver.solve())

    print("ACO with %s ants, running for %s iters:" % (args.ants, args.iters))
    print("Mean solution: %s" % mean(solutions))
    print("Stddev: %s" % standard_deviation(solutions))
