from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "description", "author"]
   list_filter = ["author"]
   search_fields = ["title", "description"]

admin.site.register(Book, BookAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'first_name', 'last_name']
