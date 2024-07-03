from django.shortcuts import render, redirect
from .models import NewsPost, WeatherNewsPost
from .forms import NewsPostForm


def news(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news, 'picture': "main/img/news-icon.jpg"})


def weather(request):
    weather_news = WeatherNewsPost.objects.all()
    return render(request, 'news/weather.html', {'news': weather_news, 'picture': "main/img/weather-icon.jpg"})


def create_news(request):
    err = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            err = "Форма заполнена неверно"
    form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'picture': "main/img/news-icon.jpg", 'error': err})
