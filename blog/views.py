from django.shortcuts import render

# Create your views here.
from django.views.generic  import  TemplateView

class  home(TemplateView):
    template_name = "home.html"

class about(TemplateView):
    template_name = "about.html"

class video(TemplateView):
    template_name = "video.html"


