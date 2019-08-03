from  django.urls import path
from .views import  home,about,video
urlpatterns = [
    path("",home.as_view(),name='home'),
    path('about/',about.as_view(),name='about'),
    path('video/', video.as_view(), name='video'),
]