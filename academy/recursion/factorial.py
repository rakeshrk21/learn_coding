# factorial 4 is 4*3*2*1 = 24, factorial(0) = 1


def factorial(n):
    assert n == int(n), "the number is negative. Only positive integers are allowed"
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


print(factorial(7))