# count =0
# total = 0
#
# while True:
#     n = input("Enter a number: ")
#     if n == 'done':
#         break
#     f = float(n)
#     total += f
#     count += 1
#     average = total/count
#
# print(average)


l = list()
while True:
    n = input("Enter a number: ")
    if n == 'done':
        break
    else:
        l.append(float(n))

li = [i for i in l]
print(li)
print(sum(li)/len(li))


