from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Post_testowy_1", content="Testowy_wpis_1")
        Post.objects.create(title="Post_testowy_2", content="Testowy_wpis_2")

    def test_book_str(self):
        p1 = Post.objects.get(title="Post_testowy_1")
        p2 = Post.objects.get(title="Post_testowy_2")

        self.assertEqual(str(p1), "Post_testowy_1 | None")
        self.assertEqual(str(p2), "Post_testowy_2 | None")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="User_1", email="test1@wp.pl")
        Author.objects.create(nick="user_2",email="test2@wp.pl")

    def test_author_str(self):
        a1 = Author.objects.get(nick="User_1")
        a2 = Author.objects.get(nick="User_2")

        self.assertEqual(str(a1), "User_1")
        self.assertEqual(str(a2), "User_2")
