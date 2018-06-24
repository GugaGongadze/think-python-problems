def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)