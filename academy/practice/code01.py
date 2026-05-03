my_dict = {"rakesh": 47, "umesh": 45, "dinesh": 42}
my_tuple = (4, "rakesh", 24.8) # tuples are immutable list
(id, name, rate) = my_tuple # tuple unpacking
my_tuple1 = (7, 98, 35)

my_list = [95, 87, 89, 42, 95, 87]
no_dups= list(set(my_list))
print(no_dups)
print(my_list.append(5))
my_set = set(my_list)
my_set1 = {67, 454, 435, 74564, 43531, 12332, 943 }
my_set1.add(999)
my_set1.remove(67)
my_set3 = my_set1.union(my_set)
my_list1 = [i**2 for i in range(0,101)]

# [expression for item in iterable if condition]
my_list1 = [i**2 for i in range(0,101) if i <8000]
my_list3 = []
for i in range(0, 101):
    if i < 8000:
        my_list3.append(i**2)

dict_comprehension = {i:i*20  for i in range(0,10) if i<80}

def myFunction(my_list):
    listxy = []
    for i in range(10):
        for j in range(5):
            listxy.append(i*j)
    return my_list + listxy

# simple lambda
add = lambda x, y: x + y
multiply = lambda x, y: x * y
no_arg = lambda: "Good Morning!"

# map() -> use map when you need to transform each element of the iterable
# syntax: map(function(which transforms the el), iterable ) and return the iterable
my_set4 = map(lambda x: x*5, my_set1)

# filter() -> use filter to filter each element of the iterable based on a function that returns true/false
# syntax: filter(function(return true/false), iterable )

even_numbers = filter(lambda x: x % 2 == 0, my_set1)

def sum(*args, **kwargs):
    print(args)
    total = 0
    for num in args:
        total = total +num
    print(total)

    print(kwargs)
    for item, value in kwargs.items():
        print(item)
        print(value)


if __name__ == '__main__':
    # print(my_dict.keys())
    # print(my_dict.values())
    # print(my_dict.items())
    # print(my_tuple[2])
    # print(id)
    # print(name)
    # print(rate)
    # print(len(my_tuple))
    # print(min(my_tuple1))
    # print(87 in my_tuple1)
    # print(7 in my_tuple1)
    # print(type(my_set))
    # print(my_set1)
    # print(my_set3)
    # print(my_set3.pop())
    # print(my_list1)
    # print(sorted(my_dict.values())[0])
    # print(sorted(my_list1))
    # print(sorted(my_list3))
    # print(dict_comprehension)
    # print(myFunction([7, 12, 8, 12]))
    # print(f"{no_arg()} Addition: {add(4,5)} & product: {multiply(4,5)}")
    print(set(my_set4))
    print(list(even_numbers))
    sum(1, 3, 5, 7, 9, name="raks", num=55)
    calories = {'apple' : 2, 'mango': 8, 'orange': 9}
    print('apple' in calories.keys())
    print('apple' in calories)

    
