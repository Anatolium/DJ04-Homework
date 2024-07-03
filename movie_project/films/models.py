from django.db import models

class MovieDatabase(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    short_description = models.CharField('Описание фильма', max_length=200)
    text = models.TextField('Отзыв о фильме')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

