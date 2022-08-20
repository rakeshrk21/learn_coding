def i(arr):
    t = 1
    for i in arr:
        t = i * t
    return t


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr.pop() * productOfArray(arr)


print(productOfArray([1, 2, 3, 10]))
