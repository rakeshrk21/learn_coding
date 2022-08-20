# implement an algo to determine if all items of the list are unique

li = [1 ,20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21, 35]

def checkIfListContainsUniqueElements(li):
    my_list = []
    for i in range(len(li)):
        if li[i] in my_list:
            return False
        else:
            my_list.append(li[i])
    return True

print(checkIfListContainsUniqueElements(li))