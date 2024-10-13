# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (Size: {self.file_size}MB)"

class PrintBook(Book):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = num_pages

    def __str__(self):
        return f"{super().__str__()} (Pages: {self.num_pages})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

