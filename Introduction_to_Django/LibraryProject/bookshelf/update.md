# Update Operation


from bookshelf.models import Book

# Retrieving and updating the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.title
