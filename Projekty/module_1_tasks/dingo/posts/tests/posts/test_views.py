from posts.models import Post, Author
from django.test import TestCase, Client
from django.test.utils import setup_test_environment

class PostViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Test post 1", content="This is first test post!")
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("home/")
        self.assertEqual(response.status_code, 200)