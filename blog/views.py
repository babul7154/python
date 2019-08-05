from django.shortcuts import render
from django.views.generic import (ListView)

# Create your views here.
from .models import post

class blogListView(ListView):
    model = post
    template_name = "home.html"
