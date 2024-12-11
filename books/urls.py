from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('books/book/<int:id>', views.book, name='book'),
    path('add/', views.add_book, name='add_book'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
