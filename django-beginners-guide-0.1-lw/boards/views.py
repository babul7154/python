from django.shortcuts import render
from .models import Board

def home(request):
    boards =Board.object.all()
    return render(request, 'home.html', {'boards': boards})