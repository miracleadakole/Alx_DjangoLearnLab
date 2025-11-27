from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import CustomLoginView
from .views import CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path("login/", CustomLoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path("logout/", CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path("register/", views.register, name="register"),
]
urlpatterns += [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]
