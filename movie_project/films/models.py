from django.db import models

class MovieDatabase(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    short_description = models.CharField('Описание фильма', max_length=1000)
    text = models.TextField('Отзыв о фильме')

    def __str__(self):
        return self.title
