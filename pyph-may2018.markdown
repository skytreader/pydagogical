# For the PythonPH May 2018 meet-up held at Kalibrr

## Requirements

Everything is written in Python 3.

The scripts use matplotlib to plot the fittest individuals per generation
although it should be trivial to remove the bits needing matplotlib in the code.

## The scripts

All scripts are invoked as packages:

    python -m dotted.package.notation

Note that if you are in a virtualenv created with Python 3, the `python` command
will _usually_ point to Python 3 by default.

All scripts take in command line arguments. Passing `-h` (or nothing at all),
will show you instructions on how to use them.
 
- [Infinite Monkey Theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)
intro: `ai/ga/monkeys.py`
- Mastermind
  - solver: `ai/ga/mastermind_solver.py`
  - stats: `ai/ga/mastermind_stats.py`
- Iterated Local Search and Guided Local Search: see [CleverAlgorithms-Python](https://github.com/skytreader/CleverAlgorithms-Python)
- Ant Colony Optimization
  - just see it run: `ai/ants.py`
  - gather some stats: `ai/ants_stats.py`
