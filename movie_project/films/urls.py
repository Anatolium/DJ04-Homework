from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add_movie/', views.add_movie, name='add_movie'),
]
