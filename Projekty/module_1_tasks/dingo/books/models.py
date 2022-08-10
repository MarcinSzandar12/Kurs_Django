from django.db import models
from django.urls import reverse

OPTIONS = (
    ("hard", "Twarda okładka" ), 
    ("soft","Miękka okładka")
    )

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover = models.CharField(max_length=50, choices=OPTIONS, blank=True, null=True)
    tags = models.ManyToManyField("books.Tag", blank=True)
    author = models.ForeignKey(
        'books.Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__ (self):
        return self.first_name + ' ' + self.last_name

class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True)
   created = models.DateTimeField(auto_now_add=True)

