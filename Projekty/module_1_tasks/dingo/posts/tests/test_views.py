from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Post, Author
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_list_url = reverse('posts:home')
        self.post_details_url = reverse('posts:post_details', args=['1'])

        self.author_list_url = reverse('posts:author_list')
        self.author_details_url = reverse('posts:author_details', args=['1'])

        
        self.author1 = Author.objects.create(id=1, nick="User_1", email="test@wp.pl")
        self.post1 = Post.objects.create(id=1, title="Post 1", content="Coś tam", author=self.author1)
        self.user = User.objects.create(username="adam")



    def test_posts_list_GET(self):
        response = self.client.get(self.post_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/home.html')

    def test_post_details_GET(self):
        response = self.client.get(self.post_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/post_details.html')

    def test_add_post_POST(self):
        Post.objects.create(
            title="post 2",
            content="Coś tam 2",
            author=self.author1
        )

        response = self.client.post(self.post_list_url, {
            'title':"post 2",
            'content':"Coś tam 2",
            'author':self.author1
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.post1.title.first(), 'post 2')



    def test_authors_list_GET(self):
        response = self.client.get(self.author_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/author_list.html')

    def test_author_details_GET(self):
        response = self.client.get(self.author_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/author_details.html')