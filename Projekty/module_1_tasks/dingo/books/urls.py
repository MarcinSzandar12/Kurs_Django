from django.urls import path
from .views import Homepage, BookList, BookDetailView, AuthorList, AuthorDetailView
from django.conf import settings

app_name="books"
urlpatterns = [
   path('home/', Homepage.as_view(), name='home'),
   path('books_list/', BookList.as_view(), name='book_list'),
   path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_details'),
   path('authors_list/', AuthorList.as_view(), name='author_list'),
   path('author_detail/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
]