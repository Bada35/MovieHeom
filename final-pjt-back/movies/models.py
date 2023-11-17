from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    released_date = models.DateField()
    vote_avg = models.FloatField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title