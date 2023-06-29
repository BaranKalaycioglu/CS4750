from django.db import models
from django.utils import  timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

class Game(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    price = models.IntegerField()
    # addedDateTime = models.DateTimeField(default= timezone.now(),verbose_name= 'Added Date & Time ')
    def __str__ (self):
        return self.name

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField()
    achievements = models.TextField()
    playtime: models.IntegerField()

