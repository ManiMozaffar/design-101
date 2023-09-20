class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.current_reader: str | None = None

    def start_reading(self, reader: str) -> str:
        if self.current_reader is not None:
            return f"{self.current_reader} is currently reading {self.title}."

        self.current_reader = reader
        return f"{self.current_reader} has started reading {self.title}."

    def stop_reading(self) -> str:
        if self.current_reader is None:
            return "No one is currently reading the book."

        reader = self.current_reader
        self.current_reader = None
        return f"{reader} has stopped reading {self.title}."


# Using the Book class
book = Book("1984", "George Orwell", 328)
print(book.start_reading("Alice"))  # Output: Alice has started reading 1984.
print(book.stop_reading())  # Output: Alice has stopped reading 1984.
