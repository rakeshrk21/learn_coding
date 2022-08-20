# find missing number in a integer array of 1 to 100

import random

a = [i for i in range(1, 51)]
del a[24]
del a[31]
del a[8]

random.shuffle(a)
print(a)

b = [36, 47, 19, 8, 22, 45, 24, 39, 41, 29, 20, 32, 50, 37, 27, 7, 34, 4, 12, 46, 30, 18, 26, 40, 44, 48, 49, 38, 1, 3,
     23, 13, 15, 5, 2, 17, 16, 43, 21, 10, 14, 35, 11, 31, 6, 28, 42]
missing_numbers = []

numbers = [i for i in range(1, 51)]
for num in numbers:
    if num not in b:
        missing_numbers.append(num)

print(missing_numbers)