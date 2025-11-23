# CRUD Operations for Book Model

This file documents all the Create, Retrieve, Update, and Delete operations performed on the `Book` model in the `bookshelf` app.


# 1. CREATE

# python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(
    title="1984", author="George Orwell", publication_year=1949
)

book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

# 2. # Retrieve all books
books = Book.objects.all()
books
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve specific attributes of the first book
book = books[0]
book.title, book.author, book.publication_year
# Expected Output:
# ('1984', 'George Orwell', 1949)

# 3. # Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book.title
# Expected Output:
# 'Nineteen Eighty-Four'

# 4. # Delete the book instance
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>

