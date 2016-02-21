#! /usr/bin/env python3

import math

SIGMOID = lambda x: 1 / (1 + (math.e ** -x))

def mcp_factory(on_minval):
    """
    Returns a threshold function where `on_minval` is the lowest possible value
    for the function to return 1.
    """
    return lambda x: 1 if x >= on_minval else 0

class Neuron(object):
    
    def __init__(self, decision_fn, bias=1, bias_weight=1):
        """
        decision_fn should take in a number for an input and return a number.
        """
        self.decision_fn = decision_fn
        self.bias = bias
        self.bias_weight = bias_weight

    def feed(self, i, w, include_bias=False):
        """
        Feed input to this neuron and get an output value. i is the list of
        inputs while w is the list of weights for each respective input. Hence
        we expect them to be of the same length.

        FIXME Throw an exception if they are not of the same length.
        """
        if include_bias:
            _i = [_ for _ in i]
            _w = [_ for _ in w]
            _i.insert(0, self.bias)
            _w.insert(0, self.bias_weight)
            i, w = _i, _w

        return self.decision_fn(sum(list(map(lambda x: x[0] * x[1], zip(i, w)))))

if __name__ == "__main__":
    and_neuron = Neuron(mcp_factory(0), 1, -0.6)
    possible_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]

    for inp in possible_inputs:
        print(inp, and_neuron.feed(inp, [0.5, 0.5], True))
