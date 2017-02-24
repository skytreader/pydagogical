#! /usr/bin/env python3

class Accumulator(object):

    def __init__(self):
        self.aggregates = {}

    def tick(self, key):
        if self.aggregates.get(key):
            self.aggregates[key] += 1
        else:
            self.aggregates[key] = 1
