from django.shortcuts import render
from django.views.generic import ListView, DetailView
from books.models import Book, Author

class Homepage(ListView):
    model = Book
    template_name = 'books/home.html'

class BookList(ListView):
    model = Book
    template_name = 'books/books_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'

class AuthorList(ListView):
    model = Author
    template_name = 'books/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_details.html'

def author_books(request):
    auth = Author.objects.all()
    works = auth.book_set.all()

    works_list = list(works)
    books = {"work_list" : works_list}
    return render(
        request=request,
        template_name="books/author_details.html",
        context=books
    )