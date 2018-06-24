def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False