# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book"""
        return f"'{self.title}' by {self.author}"


# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file_size"""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """String representation for EBook"""
        return f"'{self.title}' by {self.author} (EBook, {self.file_size}MB)"


# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page_count"""
        super().__init
