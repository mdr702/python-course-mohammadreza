# Magic Methods in Python | متدهای جادویی در پایتون
# __init__, __str__, __repr__, __len__, __add__, etc.

class Book:
    def __init__(self, title, author, pages, price):
        """Constructor - called when object is created"""
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    # String representation (for users)
    def __str__(self):
        return f"📖 '{self.title}' by {self.author}"
    
    # Official representation (for developers)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages}, {self.price})"
    
    # Length - returns number of pages
    def __len__(self):
        return self.pages
    
    # Addition - combine two books (total pages)
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
    
    # Greater than - compare by pages
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented
    
    # Less than
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    # Equality
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return NotImplemented


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    # Length - returns number of books
    def __len__(self):
        return len(self.books)
    
    # Get item by index
    def __getitem__(self, index):
        return self.books[index]
    
    # Set item by index
    def __setitem__(self, index, value):
        self.books[index] = value
    
    # String representation
    def __str__(self):
        return f"📚 Library '{self.name}' with {len(self.books)} books"
    
    # Iteration
    def __iter__(self):
        return iter(self.books)


# Creating books
print("=== Creating Books ===")
book1 = Book("Python Crash Course", "Eric Matthes", 544, 350000)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 592, 420000)
book3 = Book("Clean Code", "Robert Martin", 464, 580000)
book4 = Book("Python Crash Course", "Eric Matthes", 544, 350000)  # Same as book1

# __str__ method (used by print)
print("\n=== __str__ Method ===")
print(book1)
print(book2)

# __repr__ method (used in debug)
print("\n=== __repr__ Method ===")
print(repr(book1))
print(repr(book2))

# __len__ method
print("\n=== __len__ Method ===")
print(f"Pages in '{book1.title}': {len(book1)}")
print(f"Pages in '{book2.title}': {len(book2)}")

# __add__ method
print("\n=== __add__ Method ===")
total_pages = book1 + book2
print(f"Total pages: {total_pages} pages")

# Comparison methods
print("\n=== Comparison Methods ===")
print(f"Is '{book1.title}' longer than '{book2.title}'? {book1 > book2}")
print(f"Is '{book2.title}' longer than '{book1.title}'? {book2 > book1}")
print(f"Is '{book1.title}' equal to '{book4.title}'? {book1 == book4}")

# Working with Library
print("\n=== Library Class ===")
library = Library("Central Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)
print(f"Number of books: {len(library)}")

# __getitem__ method
print("\n=== __getitem__ Method ===")
print(f"First book: {library[0]}")
print(f"Second book: {library[1]}")

# Iteration (__iter__ method)
print("\n=== Iteration ===")
for book in library:
    print(f"  {book}")

# More magic methods examples
print("\n=== More Magic Methods ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v2 - v1 = {v2 - v1}")
print(f"v1 * 3 = {v1 * 3}")
