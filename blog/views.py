from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import BookInfo
class BlogListView(ListView):
    model = BookInfo
    template_name = "home.html"
