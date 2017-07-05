"""
All methods take in an iterable and returns a set of tuples. The sequences are
not expected to be unique.
"""

def __reconstruct_original_chars(index_perm, seq):
    return [seq[index] for index in index_perm]

def generate_next_state(curstate, limit):
    """
    Assumes that len(curstate) != limit.
    """
    next_state = curstate
    for i in range(limit):
        if i not in curstate:
            next_state.append(i)
            return next_state

def permute_dfs(seq):
    if not seq:
        return set()

    permutations = set()
    seqlimit = len(seq)
    cur_index = 0
    genstack = [[cur_index]]

    while cur_index < seqlimit:
        cur_prefix = genstack.pop()
        print(cur_prefix)
        next_state = generate_next_state(cur_prefix, seqlimit)

        if len(next_state) == seqlimit:
            permutations.add(tuple(__reconstruct_original_chars(next_state, seq)))
        else:
            genstack.append(next_state)

        if not genstack:
            cur_index += 1
            genstack = [[cur_index]]

    return permutations
