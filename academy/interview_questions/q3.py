# find the maximum product of two integers in an array where all elements are positive

li = [1 ,20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 135, 16, 27, 58, 19, 21]

max_product = 1
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] * li[j] < max_product:
            continue
        else:
             max_product = li[i] * li[j]
             pairs = str(li[i]) + "," + str(li[j])
print(max_product)
print(pairs)
