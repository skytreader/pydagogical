#!/usr/bin/env python3

"""
Problem statement: It's Christmas and Alice and Bob's office is having an
exchange gift activity. To facilitate this, every person in the office will draw
a name from the pool; this will be the person to whom they will give their gift.

However, for some reason or another, Alice does not want to draw Bob, Alice
accepts that it can't be avoided completely but she wonders _when_ should she
draw a name to minimize her chances of drawing Bob. There are two factors to her
decision:

1. Is she is the nth person to draw a name, there is $1 / N - (n-1)$ chance of
drawing Bob, where N is the number of people in their office. Obviously, she
minimizes her chance of drawing Bob by being the first person to draw. At that
point there is $1 / N$ chance of drawing Bob and will only increase after.

2. However, somewhere in the $n < N$ draws that will take place will come a
point where someone else draws Bob's name. After that, Alice is completely safe
as there is 0 probability of drawing Bob. So she chould minimize her chances by
determining the average number of draws it would take to draw Bob and just
drawing after that.

What strategy should Alice choose?

(Possible) Variables:
- The number of participants.
- Whether to use plain random or SystemRandom.
"""

import random

class ExchangeGiftSimulator(object):

    def __init__(self, participant_count, locrand=random):
        self.participants = ["Participant %s" % d for d in range(participant_count - 1)]
        self.random = locrand

    def make_alice_choose(self):
        raise NotImplementedError("Please implement Alice's strategy for drawing.")
