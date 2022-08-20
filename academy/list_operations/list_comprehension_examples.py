# Find all of the numbers from 1-1000 that are divisible by 7

divisible_by_seven = [i for i in range(0, 1001) if i % 7 == 0]
print(divisible_by_seven)


# Find all of the numbers from 1-1000 that have a 3 in them
three = [i for i in range(0, 1000) if '3' in str(i)]
print(three)


# Count the number of spaces in a string
str = "i suck big time! i just have been the most in disciplined person ever. I'm an addict"
spaces = [s for s in str if s == ' ']
print(len(spaces))

# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled
# while eating yuky yams”


# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
# Result would look like (index, value), (index, value)

mix = ["hi", 4, 8.99, "apple", ('t,b', 'n')]
test = [(i, s) for i, s in enumerate(mix)]
print(test)

# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common = [e for e in list_a if e in list_b]
print(common)


# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
words = sentence.split()
numbers = [num for num in words if not num.isalpha()]
print(numbers)


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word
# ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

print(['even' if i % 2 == 0 else 'odd' for i in range(20)])

# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9,
# list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_d = [2, 7, 1, 12]
print([(i, i) for i in list_c if i in list_d])

# Find all of the words in a string that are less than 4 letters
something = "i suck big time! i just have been the most in disciplined person ever. I'm an addict"
print([j for j in something.split() if len(j) <= 4])


# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides
# 1 (2-9)
no_dups = set()
for n in range(1, 1000):
    for d in range(2, 9):
        if n % d != 0:
            no_dups.add(n)

print(no_dups)