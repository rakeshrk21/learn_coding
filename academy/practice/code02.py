a = lambda x, y : x + y

# how to simplify this
def summation(*args):
    total = 0
    for i in args:
        total += i
    return total

# [expression for item in iterable if condition]
my_list = [ i*2 for i in range(1,101) if i>20]
my_dict = {i:i*10 for i in range(1,11) if i*10 > 11} # condition on the value

# map() -> use map when you need to transform each element of the iterable
# syntax: map(function(which transforms the el), iterable ) and return the iterable

my_set = { i*3 for i in range(1,101) if i%2!=0}
my_mapped_list = list(map(lambda i: i*50, my_set))
my_filtered_list = list(filter(lambda i: i <5250, my_mapped_list))


if __name__ == "__main__":
    print(a(5, 4))
    print(summation(1,4,5,6))
    print(my_list)
    print(my_dict)
    print(my_mapped_list)
    print(my_filtered_list)