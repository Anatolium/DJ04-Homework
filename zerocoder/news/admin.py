from django.contrib import admin
from .models import NewsPost, WeatherNewsPost

admin.site.register(NewsPost)
admin.site.register(WeatherNewsPost)
