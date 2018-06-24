import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def estimate_pi():
    pi_inverse = 0
    k = 0
    limit = 1e-15
    factor = (2 * math.sqrt(2)) / 9801

    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = (factorial(k) ** 4) * (396 ** (4 * k))
        evaluation = factor * num / den
        pi_inverse += evaluation

        if abs(evaluation) < limit:
            break

        k += 1

    return 1 / pi_inverse