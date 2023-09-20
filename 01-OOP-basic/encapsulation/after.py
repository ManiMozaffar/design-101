from typing import Optional


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author} with {self.pages} pages"


class BookManager:
    def __init__(self) -> None:
        self.current_reader: Optional[str] = None
        self.book: Optional[Book] = None

    def assign_book(self, book: Book) -> None:
        self.book = book

    def start_reading(self, reader: str) -> str:
        if self.book is None:
            return "No book assigned to read."

        if self.current_reader is not None:
            return f"{self.current_reader} is currently reading {self.book}."

        self.current_reader = reader
        return f"{self.current_reader} has started reading {self.book}."

    def stop_reading(self) -> str:
        if self.current_reader is None:
            return "No one is currently reading the book."

        reader = self.current_reader
        self.current_reader = None
        return f"{reader} has stopped reading {self.book}."


# Using the Book and BookManager classes
book = Book("1984", "George Orwell", 328)
book_manager = BookManager()
book_manager.assign_book(book)

print(
    book_manager.start_reading("Alice")
)  # Output: Alice has started reading 1984 by George Orwell with 328 pages.
print(
    book_manager.stop_reading()
)  # Output: Alice has stopped reading 1984 by George Orwell with 328 pages.
