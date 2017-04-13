#! /usr/bin/env python3

def get_non_decreasing_subranges(lnum):
    """
    Return inclusive subranges that are non-decreasing within lnum. Thecontinuity
    of subranges is based on the longest possible chains of non-decreasing subranges.
    """
    i = 1
    subrange_start = 0
    limit = len(lnum)
    subranges = set()

    while i < limit:
        if lnum[i] < lnum[i - 1]:
            subranges.add((subrange_start, i - 1))
            subrange_start = i
        i += 1

    if lnum and lnum[subrange_start] <= lnum[i - 1]:
        subranges.add((subrange_start, i - 1))
    
    return subranges
