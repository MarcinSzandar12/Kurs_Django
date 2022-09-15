from django.urls import path
from .views import *
from django.conf import settings

app_name="books"
urlpatterns = [
   path('home/', Homepage.as_view(), name='home'),
   path('books_list/', BookList.as_view(), name='book_list'),
   path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_details'),
   path('authors_list/', AuthorList.as_view(), name='author_list'),
   path('author_detail/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
   path('book/borrow/<int:id>/', BorrowBook, name='borrow_book'),
   path('borrowed_books/', BorrowedBooks.as_view(), name='borrowed_books'),
   path('book/return/<int:id>/', ReturnBook, name='return_book'),
]