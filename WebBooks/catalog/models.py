from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги', verbose_name='Жанр книги')

    