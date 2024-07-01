from django.shortcuts import render
from .models import NewsPost, WeatherNewsPost

def news(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news, 'picture': "main/img/news-icon.jpg"})

def weather(request):
    weather_news = WeatherNewsPost.objects.all()
    return render(request, 'news/weather.html', {'news': weather_news, 'picture': "main/img/weather-icon.jpg"})

