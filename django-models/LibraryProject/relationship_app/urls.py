from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import CustomLoginView
from .views import CustomLogoutView
from .views import add_book
from .views import edit_book
from .views import delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path("login/", CustomLoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path("logout/", CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path("register/", views.register, name="register"),
]
urlpatterns += [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]
