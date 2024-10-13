class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (Print, {self.page_count} pages)"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} (EBook, {self.file_size} MB)"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]  # Returns a list of book descriptions

    def show_books(self):
        for book in self.books:
            print(book)


# Example usage:
if __name__ == "__main__":
    library = Library()
    
    book1 = PrintBook("1984", "George Orwell", 328)
    book2 = EBook("Python Programming", "John Doe", 2)

    library.add_book(book1)
    library.add_book(book2)

    print("Books in Library:")
    print(library.list_books())

