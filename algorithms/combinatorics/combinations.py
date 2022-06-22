#! /usr/bin/python3

def binomial_coefficients(n, m):
    limit = n + 1
    bin_coeff = [[None for _ in range(limit)] for _ in range(limit)]

    for i in range(limit):
        bin_coeff[i][0] = 1
        bin_coeff[i][i] = 1

    for i in range(1, limit):
        for j in range(1, i):
            bin_coeff[i][j] = bin_coeff[i - 1][j - 1] + bin_coeff[i - 1][j]

    return bin_coeff[n][m]

def generate_combinations(n, m):
    """
    Generate all m combinations from a universe of n. This is a _generator_ to
    curb NP growth.

    The universe will be the integers [0, n-1].

    Assurances:

    - the return order is _lexicographically least_. One element in the universe
    counts for one character in the ordering criteria.
    """
    def make_neighbors(partial_combi):
        for spam in range(partial_combi[-1] + 1, n):
            clone = [x for x in partial_combi]
            clone.append(spam)
            yield tuple(clone)

    skew = [[x] for x in range(n)]

    while skew:
        # Must use the skew as a queue rather than stack to ensure ordering.
        # Call pop with no arguments to perform DFS instead.
        combi = skew.pop(0)

        if len(combi) == m:
            yield combi
        else:
            for neighbor in make_neighbors(combi):
                skew.append(neighbor)
