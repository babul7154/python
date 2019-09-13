from django.urls import path
from core.views import MovieList,MovieDetail
urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]