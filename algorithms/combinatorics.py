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

print(binomial_coefficients(5, 4))
