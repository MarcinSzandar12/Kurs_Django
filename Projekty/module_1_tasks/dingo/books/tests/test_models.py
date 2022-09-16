from django.test import TestCase
from books.models import Book, Author, Tag, Borrow
from django.contrib.auth.models import User

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Książka_Testowa_1", description="Testowy_opis_1")
        Book.objects.create(title="Książka_Testowa_2", description="Testowy_opis_2")

    def test_book_str(self):
        b1 = Book.objects.get(title="Książka_Testowa_1")
        b2 = Book.objects.get(title="Książka_Testowa_2")

        self.assertEqual(str(b1), "Książka_Testowa_1 | None")
        self.assertEqual(str(b2), "Książka_Testowa_2 | None")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(first_name="Imię_Testowe_1", last_name="Nazwisko_Testowe_1", description="Testowy_opis_1")
        Author.objects.create(first_name="Imię_Testowe_2", last_name="Nazwisko_Testowe_2", description="Testowy_opis_2")

    def test_author_str(self):
        a1 = Author.objects.get(last_name="Nazwisko_Testowe_1")
        a2 = Author.objects.get(last_name="Nazwisko_Testowe_2")

        self.assertEqual(str(a1), "Imię_Testowe_1 Nazwisko_Testowe_1")
        self.assertEqual(str(a2), "Imię_Testowe_2 Nazwisko_Testowe_2")

class BorrowModelTest(TestCase):

    def setUp(self):
        book3 = Book.objects.create(title="Książka_Testowa_3", description="Testowy_opis_3")
        book4 = Book.objects.create(title="Książka_Testowa_4", description="Testowy_opis_4")

        user3 = User.objects.create_user(username='testuser_1', password='12345')
        user4 = User.objects.create_user(username='testuser_2', password='12345')

        Borrow.objects.create(book=book3, user=user3, borrowed="Testowa_data_1")
        Borrow.objects.create(book=book4, user=user4, borrowed="Testowa_data_2")

    def test_borrow_str(self):
        b1 = Borrow.objects.get(id=1)
        b2 = Borrow.objects.get(id=2)

        self.assertEqual(str(b1), "Książka_Testowa_3 | None")
        self.assertEqual(str(b2), "Książka_Testowa_4 | None")