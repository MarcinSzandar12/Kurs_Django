from django.contrib import admin
from .models import Post, Author

class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "content", "author"]
   list_filter = ["author"]
   search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email']


