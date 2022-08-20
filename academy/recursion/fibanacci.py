# compute the fibonacci series recursively

n = int(input("enter and integer number: "))


def f(x):
    i = 0
    j = 1
    k = 2

    if x == 0:
        return 0

    if x == 1:
        return 1

    while k <= x:
        total = i + j
        i = j
        j = total
        k += 1
    return total


#print(f"The fibonacci number at index {n} is {f(n)}")

a = [0 for i in range(n+1)]


def r(x):
    assert (x >= 0) and int(x) == x, 'Fibonacci number cannot be negative or have non integer value'
    if x in [0, 1]:
        return x

    # if the array has the value of the fibonacci, return that
    if a[x] != 0:
        return a[x]

    num = r(x-1) + r(x-2)
    a.insert(x, num)
    return num


print(f"The fibonacci number at index {n} is {r(n)}")
