# Delete Operation

from bookshelf.models import Book

# Deleting the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Retrieving all books after deletion
Book.objects.all()
