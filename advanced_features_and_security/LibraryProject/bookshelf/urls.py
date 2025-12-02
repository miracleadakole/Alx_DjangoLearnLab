from django.urls import path
from . import views

urlpatterns = [
    # Temporary home view just to verify routing works
    path('', views.index, name='bookshelf-home'),
]