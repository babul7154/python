from  django.urls import path
from .views import  home,who,how,whatwe,contact,about
urlpatterns = [
    path("",home.as_view(),name='home'),
    path('who/',who.as_view(),name='who'),
    path('how/',how.as_view(), name='how'),
    path('whatwe/', whatwe.as_view(), name='whatwe'),
    path('contact/', contact.as_view(), name='contact'),
    path('about/', about.as_view(), name='about'),
]