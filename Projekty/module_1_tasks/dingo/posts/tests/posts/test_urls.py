from unittest import TestCase
from django.urls import resolve
from posts.views import Homepage, PostDetailView, AddPost, EditPost, DeletePost, AuthorList, AuthorDetailView

class TestUrls(TestCase):
   def test_resolution_for_homepage(self):
       resolver = resolve('home/')
       self.assertEqual(resolver.func, Homepage)

   def test_resolution_for_postdetailview(self):
       resolver = resolve('post_detail/1/')
       self.assertEqual(resolver.func, PostDetailView)

   def test_resolution_for_addpost(self):
       resolver = resolve('add_post/')
       self.assertEqual(resolver.func, AddPost)

   def test_resolution_for_editpost(self):
       resolver = resolve('post/edit/1/')
       self.assertEqual(resolver.func, EditPost)

   def test_resolution_for_deletepost(self):
       resolver = resolve('post/delete/1/')
       self.assertEqual(resolver.func, DeletePost)

   def test_resolution_for_authorlist(self):
       resolver = resolve('author_list/')
       self.assertEqual(resolver.func, AuthorList)

   def test_resolution_for_authordetailview(self):
       resolver = resolve('author_detail/1/')
       self.assertEqual(resolver.func, AuthorDetailView)