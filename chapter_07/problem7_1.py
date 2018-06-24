import math

def mysqrt(a):
    estimate = 1
    epsilon = 0.0001
    while True:
        if abs(estimate ** 2 - a) < epsilon:
            return float(round(estimate, 1))
        else:
            estimate = (estimate + a / estimate) / 2


def test_square_root():
    print('a    ', 'mysqrt(a)    ', 'math.sqrt(a)', 'diff')
    print('-    ', '---------    ', '------------', '----')

    for i in range(1, 10):
        print(i, '   ', mysqrt(i), '         ', round(math.sqrt(i), 1), '        ', mysqrt(i) - math.sqrt(i))

test_square_root()