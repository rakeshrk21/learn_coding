# find the maximum product of two integers in an array where all elements are positive
import json

def find_max_product(li):
    max_product = li[0]
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] * li[j] < max_product:
                continue
            else:
                max_product = li[i] * li[j]
                pairs = str(li[i]) + "," + str(li[j])
    print(max_product)
    print(pairs)

def reverse_list(li):
    i = 0
    j = len(li)-1

    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1

    print(li)

def find_list_min_max(li):
    min = max = li[0]
    for i in range(len(li)):
        if li[i] < min:
            min = li[i]
        if li[i]> max:
            max = li[i]
    
    return (min, max)

def missing_num(li):
    for i in range(101):
        if i not in li:
            return i

def fib(num):
    # 0,1,1,2,3,5,8
    if num == 0:
        return []
    if num == 1:
        return [0]
  
    fib = []

    x = 0
    y = 1
    fib.append(x)
    fib.append(y)
    count = 2
    while count < num:
        x, y = y, x+y
        count +=1
        fib.append(y)
    return fib

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    my_dict = {}

    for i in range(len(str1)):
        if str1[1] in my_dict:
            my_dict[str1[i]] = my_dict[str1[i]] + 1
        else:
            my_dict[str1[i]] = 1

    for i in range(len(str2)):
        if str2[1] in my_dict:
            my_dict[str2[i]] = my_dict[str2[i]] - 1
        else:
            return False

    
    for key, value in my_dict.items():
        if value  != 0:
            return False
        
    return True

def max_array_product(li):
    maxSoFar = li[0]
    currentMax = li[0]
    startIndex = 0
    start = 0
    end = 0

    for i in range(1, len(li)):

        # if currentMax is less than 0
        if currentMax < 0:
            currentMax = li[i]
            startIndex = i
        else:
            currentMax = currentMax * li[i]

        if currentMax > maxSoFar:
            maxSoFar = currentMax
            end = i
            start = startIndex

    return (start, end, maxSoFar)

def read_json():
    dict1 = {"Rakesh": 25}
    print(dict1)
    print(json.dumps(dict1))



if __name__ == '__main__':
    li = [1 ,20, 30, -44, 5, 56, -57, 8, 9, 10, 31, -12, 13, 135, -16, 27, 58, 19, 21]
    find_max_product(li)
    reverse_list(li)
    print(find_list_min_max(li))
    missing_num(li)
    missing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    print(missing_num(missing))
    print(fib(5))
    li_max_product = [1 ,20, 30, -44, 5, 56, -57, 8, 9, 10, 31, -12, 13, 135, -16, 27, 58, 19, 21]
    print(max_array_product(li_max_product))
    read_json()