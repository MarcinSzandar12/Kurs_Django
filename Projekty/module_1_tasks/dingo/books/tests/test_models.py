from django.test import TestCase
from books.models import Book, Author, Tag, Borrow

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Książka_Testowa_1", descritpion="Testowy_opis_1")
        Book.objects.create(title="Książka_Testowa_2", descritpion="Testowy_opis_2")

    def test_book_str(self):
        b1 = Book.objects.get(title="Książka_Testowa_1")
        b2 = Book.objects.get(title="Książka_Testowa_2")

        self.assertEqual(str(b1), "id:1, title=Książka_Testowa_1, descritpion=Testowy_opis_1")
        self.assertEqual(str(b2), "id:2, title=Książka_Testowa_2, descritpion=Testowy_opis_2")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(first_name="Imię_Testowe_1", last_name="Nazwisko_Testowe_1", descritpion="Testowy_opis_1")
        Author.objects.create(first_name="Imię_Testowe_2", last_name="Nazwisko_Testowe_2", descritpion="Testowy_opis_2")

    def test_book_str(self):
        a1 = Author.objects.get(last_name="Nazwisko_Testowe_1")
        a2 = Author.objects.get(last_name="Nazwisko_Testowe_2")

        self.assertEqual(str(a1), "id:1, first_name=Imię_Testowe_1, last_name=Nazwisko_Testowe_1, descritpion=Testowy_opis_1")
        self.assertEqual(str(a2), "id:2, first_name=Imię_Testowe_2, last_name=Nazwisko_Testowe_2, descritpion=Testowy_opis_2")

class TagModelTest(TestCase):

    def setUp(self):
        Tag.objects.create(word="Testowy_Tag_1", created="Testowa_data_1")
        Tag.objects.create(word="Testowy_Tag_2", created="Testowa_data_2")

    def test_book_str(self):
        t1 = Tag.objects.get(word="Testowy_Tag_1")
        t2 = Tag.objects.get(word="Testowy_Tag_2")

        self.assertEqual(str(t1), "id:1, word=Testowy_Tag_1, created=Testowa_data_1")
        self.assertEqual(str(t2), "id:2, word=Testowy_Tag_2, created=Testowa_data_2")

class BorrowModelTest(TestCase):

    def setUp(self):
        Borrow.objects.create(book="Książka_Testowa_1", user="Testowy_Użytkownik_1", borrowed="Testowa_data_1")
        Borrow.objects.create(book="Książka_Testowa_2", user="Testowy_Użytkownik_2", borrowed="Testowa_data_2")

    def test_book_str(self):
        b1 = Borrow.objects.get(book="Książka_Testowa_1")
        b2 = Borrow.objects.get(book="Książka_Testowa_2")

        self.assertEqual(str(b1), "id:1, book=Książka_Testowa_1, user=Testowy_Użytkownik_1, borrowed=Testowa_data_1")
        self.assertEqual(str(b2), "id:2, book=Książka_Testowa_2, user=Testowy_Użytkownik_2, borrowed=Testowa_data_2")