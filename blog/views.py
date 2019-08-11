from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_update.html"
    fields=['title','body']
    

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    fields=['title','body']
    success_url=reverse_lazy('home')
