def recursiveRange(num):
    if num == 1:
        return num
    else:
        return recursiveRange(num-1) + num


print(recursiveRange(10))
