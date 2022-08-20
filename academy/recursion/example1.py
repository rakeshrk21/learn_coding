n = int(input("provide an integer input: "))


def recursive_method(n):
    if n < 1:
        print("n is less than 1")

    else:
        recursive_method(n-1)
        print(n)


recursive_method(n)