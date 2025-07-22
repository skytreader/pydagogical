#! /usr/bin/python3

from collections import Counter

def add_partition_at(partition, insert_index):
    new_partition = [_ for _ in partition]
    new_partition[insert_index - 1] -= 1
    new_partition.insert(insert_index, 1)
    return new_partition

def generate_new_partitions(partition):
    """
    Assuming partition is sorted in a non-increasing order, enumerate the next
    generation of partitions with |P_new| = |P_current| + 1.

    |P_current| >= 2

    Invariant: this generates all partitions of size |P_new| with the same least
    component as the original partition. (Proof?)
    """
    new_generation = []
    subtrahend = partition[1]

    while subtrahend <= (partition[0] - subtrahend):
        new_partition = [_ for _ in partition]
        new_partition[0] = partition[0] - subtrahend
        new_partition.insert(1, subtrahend)
        new_generation.append(new_partition)
        subtrahend += 1

    return new_generation

def integer_partitions(n, max_partitions=0):
    """
    Generate integer coefficients in an iterative and lexicographic manner.

    Lexicographic allows us to take advantage of certain constraints when
    performing what is essentialy graph traversal.

    In general, n >= max_partitions
    """

    partitions = set([n])

    # Seed the possibility queue with |P|=2
    possibility_stack = [[n - i, i] for i in range(1, (n // 2) + 1)]

    while possibility_stack:
        partition = possibility_stack.pop()
        if max_partitions and len(partition) < max_partitions:
            partitions.add(tuple(partition))
            for gen in generate_new_partitions(partition):
                possibility_stack.append(gen)

    return partitions
