

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return power(base, exponent-1) * base


def p(b, e):
    temp = 1
    while e > 0:
        temp = temp * b
        e -= 1
    return temp


print(power(2, 25))
print(p(2, 25))

# [expression for item in iterable if condition == True]

