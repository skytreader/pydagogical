# pydagogical

[![Build Status](https://travis-ci.org/skytreader/pydagogical.svg?branch=master)](https://travis-ci.org/skytreader/pydagogical)
[![Coverage Status](https://coveralls.io/repos/skytreader/pydagogical/badge.svg?branch=master)](https://coveralls.io/r/skytreader/pydagogical?branch=master)

Promoted from a branch in my [sandbox repo](https://github.com/skytreader/sandbox).

I need it as a submodule to something else in sandbox.

## Notes

This is really just for pedagogical purposes and no performance guarantees beside
asymptotic time complexity ("Big-Oh") are given.

### On code style

When checking for `None` pointers, take care when using the more Pythonic form of

    if pointer:
        pass

or

    if not pointer:
        pass

since the pointer might contain another value considered false but was really
inserted into the structure as such. **This really depends on the structure where
you are checking for `None` pointers**.
