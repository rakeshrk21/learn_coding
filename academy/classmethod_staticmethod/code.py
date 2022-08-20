class ClassTest:
    def instance_method(self):
        print(f"Called the instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called the class method of {cls}")

    @staticmethod
    def static_method():
        print("called static method")


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight)


test = ClassTest()
test.instance_method()
ClassTest.class_method()
ClassTest.static_method()

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python", 600)
print(book)
print(light)
