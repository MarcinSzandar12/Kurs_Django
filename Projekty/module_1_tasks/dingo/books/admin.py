from django.contrib import admin
from .models import Book, Author, Tag, Borrow

class BookAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "description","is_available", "author"]
   list_filter = ["author"]
   search_fields = ["title", "description"]

admin.site.register(Book, BookAdmin)

class TagAdmin(admin.ModelAdmin):
   list_display = ["word"]
   search_fields = ["word"]

admin.site.register(Tag, TagAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'first_name', 'last_name']

class BorrowAdmin(admin.ModelAdmin):
   list_display = ["id", "book", "user", "borrowed", "returned"]
   search_fields = ["user"]

admin.site.register(Borrow, BorrowAdmin)
