from django.urls import path

from .views import BlogDetailView, BlogListView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
]
