from .models import MovieDatabase
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class MovieDatabaseForm(ModelForm):
    class Meta:
        model = MovieDatabase
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
        }
