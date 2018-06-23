'''

recurse(3, 0)
    ⬇
recurse(2, 3)
    ⬇
recurse(1, 5)
    ⬇
recurse(0, 6)   ➡   print(6)

'''

def recurse(n, s):
    '''
    n ➡ non-negative integer
    s ➡ integer

    recursively calls itself until n is 0 and prints then prints s

    '''


    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)

# Q1. What would happen if you called this function like this: recurse(-1, 0)?
# A1. In that case n would never be equal to 0 and function would call itself recursively until interpreter decided that enough was enough.