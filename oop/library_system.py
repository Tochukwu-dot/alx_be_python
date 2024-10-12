# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book"""
        return f"Book: {self.title} by {self.author}"


# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file_size in MB"""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """String representation for EBook (convert file size to KB)"""
        file_size_kb = self.file_size
        return f"EBook: {self.title} by {self.author}, File Size: {file_size_kb}KB"


# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page_count"""
        super().__init__(title, author)
        self.page_count = page_count  # number of pages

    def __str__(self):
        """String representation for PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count} pages"


# Composition class: Library
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books"""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library"""
        self.books.append(book)

    def list_books(self):
        """List all books in the library"""
        if not self.books:
            print("The library has no books.")
        else:
            #print("Books in the library:")
            for book in self.books:
                print(f"{book}")
