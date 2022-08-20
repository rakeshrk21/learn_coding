
class Book:
    def __init__(self, name: str, page_count : int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def read(self, pages: int):
        try:
            if self.page_count >= self.page_read + pages:
                self.page_read += pages
        except ValueError as e:
            print(f"The total pages read is greater than the number of pages in the book")
        finally:
            print("Thank you!")

    def __str__(self):
        return (
            f"The reader has read {self.page_read} pages in the book with name {self.name} that has {self.page_count} pages"
        )


book = Book("Sherlock", 100)
book.read(25)
book.read(25)
book.read(25)
book.read(25)

print(book)
