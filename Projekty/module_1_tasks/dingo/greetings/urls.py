from django.urls import path
from .views import hello, hello_someone

urlpatterns = [
   path('', hello),
   path('<name>', hello_someone),
]