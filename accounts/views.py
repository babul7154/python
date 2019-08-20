from  django.shortcuts  import   render

# Create your views here.from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(CreateView):
    form_class=UserCreationForm  #/  it must be in  subclass
    template_name='templates/signup.html'
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
