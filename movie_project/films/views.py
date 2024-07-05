from django.shortcuts import render, redirect
from .models import MovieDatabase
from .forms import MovieDatabaseForm


def movie_list(request):
    movies = MovieDatabase.objects.all()
    return render(request, 'films/movie_list.html', {'movies': movies, 'picture': "films/img/film-logo.png"})


def add_movie(request):
    error = ""
    if request.method == 'POST':
        form = MovieDatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else:
            error = "Форма заполнена неверно"
    form = MovieDatabaseForm()
    return render(request, 'films/add_movie.html', {'form': form, 'picture': "films/img/film-logo.png", 'error': error})
