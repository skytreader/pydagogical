#!/usr/bin/env python3

import random

class BobFinder(object):

    def __init__(self, shuffler=random.shuffle):
        self.shuffler = shuffler

    def find_bob(self, participant_count):
        pool = ["Participants %s" % i for i in range(participant_count - 1)]
        pool.append("Bob")
        self.shuffler(pool)
        return pool.index("Bob") + 1

def experiment(participant_count=40, runs=1000):
    bob_finder = BobFinder()
    bob_posn_sum = sum([bob_finder.find_bob(participant_count) for i in range(runs)])
    return bob_posn_sum / runs

if __name__ == "__main__":
    print(experiment())
