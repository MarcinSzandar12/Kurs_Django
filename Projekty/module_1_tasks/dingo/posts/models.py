from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Author(models.Model):
    nick = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(
        max_length=255,
        unique=True
    )
