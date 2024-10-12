# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize a Book instance"""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor to handle object deletion"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of a Book instance"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation to recreate the Book instance"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
# if __name__ == "__main__":
#     book1 = Book("1984", "George Orwell", 1949)
#     print(str(book1))   # Output: '1984' by George Orwell, published in 1949
#     print(repr(book1))  # Output: Book('1984', 'George Orwell', 1949)
    
#     # Deleting the object
#     del book1
