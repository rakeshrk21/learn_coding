

names = ['Kiran', 'King', 'John', 'Corey']
print(dir(names))

# i_names = names.__iter__()  # how to get an iterator from an iterable (list). use the .__iter__()

i_names = iter(names)  # how to get an iterator from an iterable (list). use the iter()

while True:
    try:
        item = next(i_names)
        print(item)
    except StopIteration:
        break
