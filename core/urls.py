from django.urls import path
from .views import MovieDetailView,MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='moviedetail'),
]
