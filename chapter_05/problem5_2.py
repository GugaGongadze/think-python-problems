def check_fermat(a, b, c, n):
    if type(n) is int and n > 2 and (a ** n + b ** n == c ** n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def ask_user_for_fermat():
    a = int(input('a: '))
    b = int(input('a: '))
    c = int(input('a: '))
    n = int(input('a: '))

    check_fermat(a, b, c, n)

ask_user_for_fermat()