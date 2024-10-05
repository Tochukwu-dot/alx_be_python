# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize a new book with a title and author. Initially, the book is available."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        """Return the checked-out status of the book."""
        return self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                    return
                else:
                    print(f"{title} is already checked out.")
                    return
        print(f"{title} not found in the library.")

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                    return
                else:
                    print(f"{title} was not checked out.")
                    return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        """List all available books that are not checked out."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No available books at the moment.")
