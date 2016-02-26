#! /usr/bin/env python3

import math
import random

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

class NeuralNetwork(object):
    
    def __init__(self, neurons, weights):
        """
        neurons is a list-of-lists of neurons. The order in which the neurons
        are listed is taken as the order of the layers.

        weights is a list-of-lists, assumed to have the same dimensions as
        neurons.
        """
        self.neurons = neurons
        self.weights = weights

    def feed(self, i, include_bias=False):
        current_inputs = i

        for idx, layer in enumerate(self.neurons):
            new_inputs = []
            for jdx, neuron in enumerate(layer):
                new_inputs.append(neuron.feed(current_inputs, self.weights[idx], include_bias))

            # The previous layer's output is the next layer's input
            current_inputs = new_inputs

        # This should now contain the last layer's output
        return current_inputs

class BackPropagationTrainer(object):
    
    def __init__(self, network, learning_rate):
        """
        network is the neural network instance

        learning_rate is a number between 0 and 1.

        TODO Check that properly.
        """
        self.network = network
        self.learning_rate = learning_rate

    def train(self, inp, expected):
        # TODO Should I include the bias here??
        result = self.network.feed(inp)
        deltas = [(x - y) for x, y in zip(result, expected)]

        # This would assume that the weights is mutable. It should never be tuples then
        for idx, ws in enumerate(self.network.weights):
            news = [w for w in ws]

            for jdx, d in enumerate(deltas):
                news[jds] -= (d * self.learning_rate)

def and_experiment(possible_inputs):
    """
    Experiment on a perceptron.
    """
    and_neuron = Neuron(mcp_factory(0), 1, -0.6)

    for inp in possible_inputs:
        print(inp, and_neuron.feed(inp, [0.5, 0.5], True))

def xor_experiment(possible_inputs):
    """
    Experiment with a two-layer neural network.
    """
    simple_thres = mcp_factory(0)
    xor_neurons = ((Neuron(simple_thres, -1.5, 1), Neuron(simple_thres, -0.5, 1)),
      (Neuron(simple_thres, -0.5, 1),))
    xor_network = NeuralNetwork(xor_neurons, ((1, 1), (-2, 1)))
    
    for inp in possible_inputs:
        print(inp, xor_network.feed(inp, True))

def or_experiment(possible_inputs):
    """
    Experiment for a neural network with a hidden layer.
    """
    simple_thres = mcp_factory(0)
    or_neurons = ((Neuron(simple_thres) for _ in range(2)),
      (Neuron(simple_thres) for _ in range(5)),
      (Neuron(simple_thres),))
    # essentially random. I don't care!!!!
    weights = [[random.uniform(1, 8) for _ in range(2)],
      [random.uniform(1, 8) for _ in range(5)],
      [random.uniform(1, 8)]]

if __name__ == "__main__":
    possible_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    and_experiment(possible_inputs)
    xor_experiment(possible_inputs)
