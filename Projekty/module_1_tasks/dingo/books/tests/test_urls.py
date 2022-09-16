from unittest import TestCase
from django.urls import resolve
from books.views import Homepage, BookList, BookDetailView, BorrowedBooks, AuthorList, AuthorDetailView, BorrowHistory

class TestUrls(TestCase):
   def test_resolution_for_homepage(self):
       resolver = resolve('home/')
       self.assertEqual(resolver.func, Homepage)

   def test_resolution_for_booklist(self):
       resolver = resolve('books_list/')
       self.assertEqual(resolver.func, BookList)

   def test_resolution_for_bookdetailview(self):
       resolver = resolve('book_detail/1/')
       self.assertEqual(resolver.func, BookDetailView)

   def test_resolution_for_borrowedbooks(self):
       resolver = resolve('borrowed_books/')
       self.assertEqual(resolver.func, BorrowedBooks)

   def test_resolution_for_borrowhistory(self):
       resolver = resolve('borrow_history/')
       self.assertEqual(resolver.func, BorrowHistory)

   def test_resolution_for_authorlist(self):
       resolver = resolve('authors_list/')
       self.assertEqual(resolver.func, AuthorList)

   def test_resolution_for_authordetailview(self):
       resolver = resolve('author_detail/1/')
       self.assertEqual(resolver.func, AuthorDetailView)