class Book:
    def __init__(
        self, title: str, author: str, pages: int, price: float, stock: int, isbn: str
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_reader = None
        self.time_left_to_return = None
        self.price = price
        self.stock = stock
        self.isbn = isbn

    def checkout(self, reader: str):
        self.current_reader = reader

    def return_book(self):
        self.current_reader = None

    def update_stock(self, new_stock: int):
        self.stock = new_stock

    def update_price(self, new_price: float):
        self.price = new_price
