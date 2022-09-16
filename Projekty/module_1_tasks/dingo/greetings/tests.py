from django.test import TestCase
from django.urls import resolve
from greetings.views import welcome

class TestUrls(TestCase):
   def test_resolution_for_homepage(self):
       resolver = resolve('welcome/')
       self.assertEqual(resolver.func, welcome)
