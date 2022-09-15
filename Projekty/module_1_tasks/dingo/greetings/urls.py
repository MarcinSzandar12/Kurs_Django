from django.urls import path
from .views import about, contact, home
from posts.views import Homepage
from books.views import Homepage

app_name="greetings"
urlpatterns = [
       path('', home, name="home"),
       path('about/', about, name="about"),
       path('posts/home/', Homepage.as_view(), name="posts_home"),
       path('books/home/', Homepage.as_view(), name="books_home"),
       path('contact/', contact, name="contact"),
]