"""
All methods take in an iterable and returns a set of tuples. The sequences are
not expected to be unique.
"""

def __reconstruct_original_chars(index_perms, seq):
    return [[seq[index] for index in permutation] for permutation in index_perms]
    for permutation in indices:
        perm = 

def permute_dfs(seq):
    if not seq:
        return set()

    permutations = set()
    seqlimit = len(seq)
    cur_index = 0
    genstack = [0]

    while cur_index < seqlimit and genstack:
        cur_prefix = genstack.pop()

        

    return permutations
