def is_triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        print('No')
    else:
        print('Yes')

def ask_for_user_triangle():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    is_triangle(a, b, c)

ask_for_user_triangle()

