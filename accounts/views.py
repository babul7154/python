from  django.shortcuts  import   render

# Create your views here.from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.generic import CreateView
from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class=UserCreationForm  #/  UsercreationForm must be in  subclass
    template_name='templates/signup.html'
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
