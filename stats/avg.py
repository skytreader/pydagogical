#! /usr/bin/env python3

import math

def mean(numset):
    return sum(numset) / len(numset)

def variance(numset):
    m = mean(numset)
    setsize = len(numset)
    varterms = ((((x - m) ** 2) / setsize) for x in numset)
    return sum(varterms)

def standard_deviation(numset):
    return math.sqrt(variance(numset))
