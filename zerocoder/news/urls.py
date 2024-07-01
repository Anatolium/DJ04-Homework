from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news_home'),
    path('weather/', views.weather, name='weather_home'),
]
