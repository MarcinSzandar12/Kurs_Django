from rest_framework import routers
from books import api_views as books_views

router = routers.DefaultRouter()
router.register('books', books_views.BookViewset)
router.register('authors', books_views.AuthorViewset)