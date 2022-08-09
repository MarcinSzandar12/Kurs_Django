from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Test post 1", content="This is first test post!")
        Post.objects.create(title="Test post 2", content="This is second test post!")

    def test_post_str(self):
        p1 = Post.objects.get(title="Test post 1")
        p2 = Post.objects.get(title="Test post 2")

        self.assertEqual(str(p1), "id:1, a=1, b=2, op=add")
        self.assertEqual(str(p2), "id:2, a=20, b=30, op=sub")

#class AuthorModelTest(TestCase):
