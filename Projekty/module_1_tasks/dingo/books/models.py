from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

COVERS = (
    ("hard", "Twarda okładka" ), 
    ("soft","Miękka okładka")
    )

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover = models.CharField(max_length=50, choices=COVERS, blank=True, null=True)
    tags = models.ManyToManyField("books.Tag", blank=True)
    image = models.ImageField(null=True, blank=True)
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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def is_available(self):
        current_borrow = self.borrow_set.filter(returned=None)
        if current_borrow:
            return "Wypożyczona"
        return "Dostępna"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__ (self):
        return self.first_name + ' ' + self.last_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True)
   created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.word

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    borrowed = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return str(self.book)