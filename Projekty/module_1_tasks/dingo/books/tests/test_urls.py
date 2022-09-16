from unittest import TestCase
from django.urls import resolve
from books.views import LibHomepage, BookList, BookDetailView, BorrowedBooks, AuthorList, AuthorDetailView, BorrowHistory

class TestUrls(TestCase):
   def test_resolution_for_homepage(self):
       resolver = resolve('/books/home/')
       self.assertEqual(resolver.func.__name__, LibHomepage.as_view().__name__)

   def test_resolution_for_booklist(self):
       resolver = resolve('/books/books_list/')
       self.assertEqual(resolver.func.__name__, BookList.as_view().__name__)

   def test_resolution_for_bookdetailview(self):
       resolver = resolve('/books/book_detail/1/')
       self.assertEqual(resolver.func.__name__, BookDetailView.as_view().__name__)

   def test_resolution_for_borrowedbooks(self):
       resolver = resolve('/books/borrowed_books/')
       self.assertEqual(resolver.func.__name__, BorrowedBooks.as_view().__name__)

   def test_resolution_for_borrowhistory(self):
       resolver = resolve('/books/borrow_history/')
       self.assertEqual(resolver.func.__name__, BorrowHistory.as_view().__name__)

   def test_resolution_for_authorlist(self):
       resolver = resolve('/books/authors_list/')
       self.assertEqual(resolver.func.__name__, AuthorList.as_view().__name__)

   def test_resolution_for_authordetailview(self):
       resolver = resolve('/books/author_detail/1/')
       self.assertEqual(resolver.func.__name__, AuthorDetailView.as_view().__name__)