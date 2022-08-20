# Python slicing. https://stackoverflow.com/questions/509211/understanding-slicing

# a[start:stop:step]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# There is also the step value, which can be used with any of the above:
# a[start:stop:step] # start through not past stop, by step

# The key point to remember is that the :stop value represents the first value that is not in the selected slice.
# So, the difference between stop and start is the number of elements selected (if step is 1, the default).

a = [1, 2, 3, 4, 5]
stop_at_index_4 = a[:4]
print(f'all items till index 4 are {stop_at_index_4}')
from_index_2 = a[2:]
print(f'all items from index 2 are {from_index_2}')
skip_every_second_elem = a[::2]
print(f'skip every second element in the list {skip_every_second_elem}')  # print(a[0:5:2])


# The other feature is that start or stop may be a negative number, which means it counts from the end of the array
# instead of the beginning. So:

last_item = a[-1]
print('last item in the array is {}'.format(last_item))
last_two_items = a[-2:]
print(f'last two items in the array are {last_two_items}')
everything_except_last_two = a[:-2]
print(f'everything except the last two items are {everything_except_last_two}')

# Accessing string characters in Python
s = "programming"
print('First character of the string is {}'.format(s[0]))
print('First 3 characters of the string is:', s[0:4])
last_char_of_string = s[-1]
print(f'the last character of the string is {last_char_of_string}')
last_3_characters = s[-3:]
print(f'last three characters of the string is {last_3_characters}')
slicing_3rd_to_2nd_last_character = s[3:-2]
print(f'slicing 3rd to 2nd last character found {slicing_3rd_to_2nd_last_character}')

# fruit = ['apple', 'banana', 'papaya', 'cherry']
# print(fruit.shuffle())

a = [1, 2, 3, 4, 5]
print(a[3:0:-1])
