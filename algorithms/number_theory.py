def pulverize(a, b):
    """
    Given two integers a and b, find the integers s and t such that
    as + tb = gcd(a, b). The sequence of the return value corresponds to their
    multipliers in the expression.
    """
    s = 0
    _s = 1

    t = 1
    _t = 0

    r = b
    _r = a

    while r:
        q = int(_r / r)
        _r, r = r, _r - q * r
        _s, s = s, _s - q * s
        _t, t = t, _t - q * t

    return (_s, _t)

def gcd(x, y):
    a = x
    b = y

    while b:
        a, b = b, a % b
    
    return a

if __name__ == "__main__":
    print(gcd(5, 3))
    print(gcd(3, 5))
    print(gcd(258, 147))
    print(gcd(147, 258))
    print(pulverize(258, 147))
