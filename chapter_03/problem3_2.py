def do_twice(f, val):
    f(val)
    f(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'Spam')

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

do_four(print_twice, 'Spam')
