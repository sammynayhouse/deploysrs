from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=300)
    genre_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_director = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_title
