from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
#    return render(request, 'home.html', {})

class Homepage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-modified']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')