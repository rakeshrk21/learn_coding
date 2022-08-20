fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print((fruit_list1, fruit_list2, fruit_list3))

s = 0

for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        s += 1
    if ls[1] == 'Kiwi':
        s += 20

print(s)

