from django.urls import path
from .views import Homepage, PostDetailView, AddPost, EditPost, DeletePost, AuthorList, AuthorDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name="posts"
urlpatterns = [
   path('home/', Homepage.as_view(), name='home'),
   path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_details'),
   path('add_post/', AddPost.as_view(), name='add_post'),
   path('post/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
   path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
   path('author_list/', AuthorList.as_view(), name='author_list'),
   path('author_detail/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)