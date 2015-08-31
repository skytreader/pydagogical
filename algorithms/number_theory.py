def pulverize(a, b):
    """
    Given two integers a and b, find the integers s and t such that
    as + tb = gcd(a, b). The sequence of the return value corresponds to their
    multipliers in the expression.
    """
    print("here")
    s = 0
    _s = 1

    t = 1
    _t = 0

    r = b
    _r = a

    while r:
        print(r)
        q = int(_r / r)
        _r, r = r, _r - q * s
        _s, s = s, _s - q * s
        _t, t = t, _t - q * t

    return (s, t)
