from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.views.generic import ListView,DetailView


class MovieListView(ListView):
    model = Movie
    template_name = "home.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "detail_view.html"

