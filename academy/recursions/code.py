t = [i for i in range(3, 0, -1)]
k = [i for i in range(100, 200, 1)]
# print(t)
# print(len(t))
# print(k)
# r = range(3, -1, -1)
# print(r)

# print a two dimentional array
# a = [[]] * 3
# print([i for i in range(3, -1, -1)])
# print([j for j in range(3)])
# print(range(3))

# a = [
#     [1, 3, 9, 4],
#     [5,  0, 9, -3]
# ]
# print(f'length of a is {len(a)}')
#
# for i in range(len(a)):
#     output = ""
#     print(f'i is {i}')
#     for j in range(len(a[i])):
#         print(f'j is {j}')
#         print(f'value is {str(a[i][j])}')
#         output += " " + str(a[i][j])
#     print(output)

towers = [[]] * 3
towers[0] = [i for i in range(3, 0, -1)]
towers[1] = []
towers[2] = []

output = ""
for i in range(3, -1, -1):
    for j in range(3):
        if len(towers[j]) > i:
            output += " " + str(towers[i][j])
        else:
            output += '\n'
    print(output + "-------")
