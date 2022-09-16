from rest_framework import serializers

from books.models import Book, Author, Tag, Borrow

class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ('id', 'title', 'description', 'cover', 'tags', 'author', 'image')

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('id', 'first_name', 'last_name', 'description', 'image')

class TagSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tag
       fields = ('id', 'word', 'created')

class BorrowSerializer(serializers.ModelSerializer):
   class Meta:
       model = Borrow
       fields = ('id', 'book', 'user', 'borrowed', 'returned')