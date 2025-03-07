from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class movieModel(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class reviewModel(models.Model):
    movie = models.ForeignKey(movieModel, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    def __str__(self):
        return f'Review for {self.movie.title}'
