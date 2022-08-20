# find if two strings are permutations of each other

def checkStringsArePermutations(str1, str2):
    list1 = [] 
    list2 = []
    list1[:0] = str1.lower()
    list2[:0] = str2.lower()
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] not in list2:
            return False
        else:
            list2.remove(list1[i])
    if len(list2)>0:
        return False
    return True

print(checkStringsArePermutations("gefometryki","trymeogekfi"))


