class E_LibraryBook:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_reader = None
        self.time_left_to_return = None

    def checkout(self, reader: str, time_to_return: int):
        self.current_reader = reader
        self.time_left_to_return = time_to_return

    def return_book(self):
        self.current_reader = None
        self.time_left_to_return = None


class RetailBook:
    def __init__(self, title: str, author: str, price: float, stock: int, isbn: str):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        self.isbn = isbn

    def update_stock(self, new_stock: int):
        self.stock = new_stock

    def update_price(self, new_price: float):
        self.price = new_price
