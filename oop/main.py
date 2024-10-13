from library_system import Library, PrintBook, EBook

def main():
    library = Library()
    
    book1 = PrintBook("1984", "George Orwell", 328)
    book2 = EBook("Python Programming", "John Doe", 2)

    library.add_book(book1)
    library.add_book(book2)

    print("Books in Library:")
    library.show_books()

if __name__ == "__main__":
    main()

