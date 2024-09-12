from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20, verbose_name='Directors Name')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Movie Title')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', verbose_name='Director')

    def __str__(self):
        return self.title
