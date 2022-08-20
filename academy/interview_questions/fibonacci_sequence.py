# print a fibonacci sequence


def fib(num):
    a, b = 0, 1
    print(a)
    for i in range(1, num):
        print(b)
        a, b = b, a+b


fib(25)