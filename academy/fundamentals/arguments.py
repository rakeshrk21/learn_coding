
# unpacking keyword arguments


def named(*args, **kwargs):
    print(args)  # print positional arguments which becomes a tuple
    print(kwargs)  # print keyword arguments which becomes a dictionary


named(2, 5, 9, 7, name="Rakesh", age=44)


def something(**kwargs):
    print(kwargs)
    print(kwargs["name"])


def print_nicely(**kwargs):
    for name, age in kwargs.items():
        print(f"{name} : {age}")


details = {"name": "Rakesh", "age": 44}
something(**details)  # unpacking keyword arguments ane making them postional arguments
print_nicely(**details)
