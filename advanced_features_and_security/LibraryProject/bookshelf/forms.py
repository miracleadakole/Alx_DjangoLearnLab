from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
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
