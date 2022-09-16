from http import client
from django.test import TestCase, Client
from django.urls import reverse
from books.models import Book, Author, Borrow

class TestViews(TestCase):

    def SetUp(self):
        self.client = Client()
        self.book_list_url = reverse('book_list')
        self.book_details_url = reverse('book_details', args=['1'])
        self.borrowed_books_list_url = reverse('borrowed_books')
        self.borrow_history_list_url = reverse('history_list')

        self.author_list_url = reverse('author_list')
        self.author_details_url = reverse('author_details', args=['1'])

        self.book1 = Book.objects.create(id='1', title="Book 1")
        self.author1 = Author.objects.create(id='1', first_name="Pogram", last_name="Tester")
        self.borrow1 = Borrow.objects.create(id='1', book="Book 2", user="User_Tester")



    def test_books_list_GET(self):
        response = self.client.get(self.book_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books_list.html')

    def test_book_details_GET(self):
        response = self.client.get(self.book_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_details.html')

    def test_borrowed_books_list_GET(self):
        response = self.client.get(self.borrowed_books_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/borrowed_books.html')

    def test_borrow_history_list_GET(self):
        response = self.client.get(self.borrow_history_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/borrow_history.html')



    def test_authors_list_GET(self):
        response = self.client.get(self.author_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/author_list.html')

    def test_author_details_GET(self):
        response = self.client.get(self.author_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/author_details.html')
