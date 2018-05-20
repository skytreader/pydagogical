"""
All methods take in an iterable and returns a set of tuples. The sequences are
not expected to be unique.
"""

def __reconstruct_original_chars(index_perm, seq):
    return [seq[index] for index in index_perm]

def generate_next_states(curstate, limit):
    """
    Assumes that len(curstate) != limit.
    """
    next_states = []
    for i in range(limit):
        if i not in curstate:
            next_state = [i for i in curstate]
            next_state.append(i)
            next_states.append(next_state)
    return next_states

def permute_dfs(seq):
    if not seq:
        return set()

    permutations = set()
    seqlimit = len(seq)
    cur_index = 0
    genstack = [[cur_index]]

    while cur_index < seqlimit:
        cur_prefix = genstack.pop()
        next_states = generate_next_states(cur_prefix, seqlimit)

        for state in next_states:
            if len(state) == seqlimit:
                permutations.add(tuple(__reconstruct_original_chars(state, seq)))
            else:
                genstack.append(state)

        if not genstack:
            cur_index += 1
            genstack = [[cur_index]]

    return permutations

# Totes unfinished!
def permute_heaps(seq):
    def generate_2perm(seq2):
        return (
            (seq2[0], seq2[1]),
            (seq2[1], seq2[0])
        )

    if not seq:
        return set()
    elif len(seq) == 1:
        return set(((seq[0]),),)
    elif len(seq) == 2:
        return set(generate_2perm(seq))
    else:
        i = 0
        __seq = [x for x in seq]
        limit = len(__seq)
        subrange_limit = 2
        all_perms = []

        while i < limit:
            subrange = __seq[0:subrange_limit]
            if subrange_limit == 2:
                twoperms = generate_2perm(subrange)
                all_perms.extend(twoperms)

            new_perms = []
            for perm in all_perms:
                np = [x for x in perm]
                np.append(__seq[subrange_limit])

            i += 1

        return all_perms
