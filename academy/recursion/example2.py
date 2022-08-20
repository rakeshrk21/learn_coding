# compute the power of two iteratively and recursively

n = int(input("enter and integer number: "))


def iterative(n):
    i = 0
    num = 1
    while i < n:
        num = num * 2
        i += 1
    return num


print(iterative(n))
