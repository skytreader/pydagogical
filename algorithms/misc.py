#! /usr/bin/env python3

def get_non_decreasing_subranges(lnum):
    """
    Return inclusive subranges that are non-decreasing within lnum. The
    continuity of subranges is based on the longest possible chains of
    non-decreasing subranges.
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

def get_proper_non_decreasing_subranges(lnum):
    """
    Same as get_non_decreasing_subranges above but will return non-trivial
    subranges: i.e., subranges that are not singletons.
    """
    i = 1
    subrange_start = 0
    limit = len(lnum)
    subranges = set()

    while i < limit:
        if lnum[i] > lnum[i - 1]:
            subranges.add((subrange_start, i))
            j = subrange_start + 1

            while j < i:
                subranges.add((j, i))
                j += 1

        if lnum[i] < lnum[i - 1]:
            subrange_start = i

        i += 1

    if lnum and lnum[subrange_start] < lnum[i - 1]:
        subranges.add((subrange_start, i - 1))
    
    return subranges
