from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # Prevent XSS by cleaning input
        return forms.utils.html.escape(title)

    def clean_author(self):
        author = self.cleaned_data.get("author")
        return forms.utils.html.escape(author)
