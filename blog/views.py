from django.shortcuts import render

# Create your views here.
from django.views.generic  import  TemplateView

class  home(TemplateView):
    template_name = "home.html"

class contact(TemplateView):
    template_name = "contact.html"

class whatwe(TemplateView):
    template_name = "whatwe.html"

class who(TemplateView):
    template_name = "who.html"

class how(TemplateView):
    template_name = "how.html"

class about(TemplateView):
    template_name = "about.html"





