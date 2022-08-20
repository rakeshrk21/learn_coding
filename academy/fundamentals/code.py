name = "Rakesh"
print(f"Hello, {name}")
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)


def add(x, y=8):
    return x + y


def say_hello(name, surname):
    print(f"hello {name} {surname}")


print(add(7, 25))

print(say_hello(surname="Radhakrishnan", name="Rakesh"))

multiply = lambda x, y: x * y

print(multiply(5, 10))

numbers = [1, 2, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)


doubled = [num * 2 for num in numbers]

print(doubled)


friends = ["Sriram", "Anand", "Anil"]
start_a = []

for friend in friends:
    if friend.startswith("A"):
        start_a.append(friend)


print(start_a)

# list comprehension
lc_doubled = [friend for friend in friends if friend.startswith('A')]

print(lc_doubled)

print(lc_doubled is doubled)
print(lc_doubled[0] is start_a[0])
print("start_a: ", id(start_a), "lc_doubled: ", id(lc_doubled))

# collections
l = ["anil", "sriram", "anand"]  # maintains order, can add/remove elements
t = ("anil", "sriram", "anand")  # tuple maintains order, cannot add/remove elements in a tuple
s = {"anil", "sriram", "anand"}  # in set, order is not maintained, no duplicates
d = {"anil": 44, "sriram": 45, "anand": 43, "shailesh": 44}  # dictionary

# set operations
friends1 = {"anil", "sriram", "anand", "shailesh", "sid", "pavan", "sachin", "sunil", "naveen", "santhosh", "santhosh b"}
abroad = {"pavan", "abhishek"}

local_friends = friends1.difference(abroad)
print(local_friends)

total_friends = friends1.union(abroad)
print(total_friends)

common_friends = friends1.intersection(abroad)
print(common_friends)

#list of dictionaries

listOfFriends = [
    {"name": "Sriram", "age": 45},
    {"name": "anil", "age": 44},
    {"name": "shailesh", "age": 44}
]

print(listOfFriends[2]["name"])

for name, age in d.items():
    print(f"name is {name} and age is {age}")


# dictionary comprehension
users = [
    (0, "emp1", "password"),
    (1, "emp2", "$@$@#$@2"),
    (2, "emp3", "fdassdff"),
]

user_map = {user[1]: user for user in users}
print(user_map)
print(user_map["emp2"])

username_input = input("Enter username: ")
password_input = input("Enter password: ")

_, username, password = user_map[username_input]

if (username == username_input) & (password == password_input):
    print("login success!")
else:
    print("login failed!")

# unpacking positional arguments


def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == '+':
        return sum(args)

    elif operator == '*':
        print(args)
        print(*args)  # unpacking
        return multiply(*args)

    else:
        return "operand is incorrect!"


print(apply(2, 8, 9, operator='*'))



