# retrieve


from bookshelf.models import Book

# Retrieving the created book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
