class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]  # Returns a list of book descriptions

    def show_books(self):
        for book in self.books:
            print(book)  # Print each book's string representation


# Example usage:
if __name__ == "__main__":
    library = Library()
    
    book1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    book2 = EBook("Snow Crash", "Neal Stephenson", 500)
    book3 = Book("Pride and Prejudice", "Jane Austen")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Books in Library:")
    library.show_books()  # Call the method to print the books

