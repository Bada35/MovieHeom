from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

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
    # reviews = models.ManyToManyField('Review', related_name='movies')

    def __str__(self):
        return self.title

# 영화에 대한 리뷰
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    content = models.TextField(max_length=200)
    # 최솟값과 최대값 설정
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 리뷰에 대한 대댓글
class ReviewComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)