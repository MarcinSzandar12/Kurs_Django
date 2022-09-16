from unittest import TestCase
from django.urls import resolve
from posts.views import Homepage, PostDetailView, AddPost, EditPost, DeletePost, AuthorList, AuthorDetailView

class TestUrls(TestCase):
   def test_resolution_for_homepage(self):
       resolver = resolve('/posts/home/')
       self.assertEqual(resolver.func.__name__, Homepage.as_view().__name__)

   def test_resolution_for_postdetailview(self):
       resolver = resolve('/posts/post_detail/1/')
       self.assertEqual(resolver.func.__name__, PostDetailView.as_view().__name__)

   def test_resolution_for_addpost(self):
       resolver = resolve('/posts/add_post/')
       self.assertEqual(resolver.func.__name__, AddPost.as_view().__name__)

   def test_resolution_for_editpost(self):
       resolver = resolve('/posts/post/edit/1/')
       self.assertEqual(resolver.func.__name__, EditPost.as_view().__name__)

   def test_resolution_for_deletepost(self):
       resolver = resolve('/posts/post/delete/1/')
       self.assertEqual(resolver.func.__name__, DeletePost.as_view().__name__)

   def test_resolution_for_authorlist(self):
       resolver = resolve('/posts/author_list/')
       self.assertEqual(resolver.func.__name__, AuthorList.as_view().__name__)

   def test_resolution_for_authordetailview(self):
       resolver = resolve('/posts/author_detail/1/')
       self.assertEqual(resolver.func.__name__, AuthorDetailView.as_view().__name__)