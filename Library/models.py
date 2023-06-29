from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

class Game(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class UserGame(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)  # change to PROTECT
    rating = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    achievements = models.TextField()
    playtime = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return {self.game.name}
