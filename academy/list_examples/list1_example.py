

class List1Example:
    li = [3, 4, 6]
    for i in range(len(li)):
        print(li[i])
        j = i + 1
        for j in range(len(li)):
            print(li[j])
