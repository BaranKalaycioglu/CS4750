from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'developer', 'platform', 'price']
        labels = {'name': "Game Name", 'developer': "Game Developer", 'platform': "Platform", 'price': "Game Price"}