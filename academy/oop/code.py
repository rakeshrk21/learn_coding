class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"The name is {self.name} and his age is {self.age}"

    def __repr__(self):
        return f"<Person>({self.name}, {self.age}, {self.weight})"


person = Person("Rakesh", 44, 78)
print(person.name)
print(person.age)
print(person)
print(person.__repr__())