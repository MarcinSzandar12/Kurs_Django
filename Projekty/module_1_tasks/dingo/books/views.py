from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from books.models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.timezone import now

class LibHomepage(ListView):
    model = Book
    template_name = 'books/home.html'

def all_and_borrowed_books_count(request):
    count_all= Book.objects.all().count()    
    count_borrowed= Borrow.objects.all().count()    
    context= {
        'count_all':count_all,
        'count_borrowed':count_borrowed
        }        
    return render(request, 'books/home.html', context)

class BookList(ListView):
    paginate_by = 3
    model = Book
    template_name = 'books/books_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'

class AuthorList(ListView):
    paginate_by = 4
    model = Author
    template_name = 'books/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_details.html'

def BorrowBook(request, id):
    book = Book.objects.get(id=id)
    user = request.user
    Borrow.objects.create(book=book, user=user)
    return HttpResponseRedirect(reverse('books:borrowed_books'))

class BorrowedBooks(ListView):
    paginate_by = 3
    model = Borrow
    template_name = 'books/borrowed_books.html'

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user).filter(returned=None)

class BorrowHistory(ListView):
    paginate_by = 10
    model = Borrow
    template_name = 'books/borrow_history.html'

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)

def ReturnBook(request, id):
    book = Borrow.objects.get(id=id)
    if book.returned==None:
        book.returned = now()
        book.save()
    return HttpResponseRedirect(reverse("books:borrowed_books"))