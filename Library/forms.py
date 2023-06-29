from django import forms
from .models import Game, UserGame
from django.core.exceptions import ValidationError

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'developer', 'platform', 'price']

class UserGameForm(forms.ModelForm):
    class Meta:
        model = UserGame
        fields = ['game', 'rating', 'achievements', 'playtime']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if rating < 0 or rating > 10:
            raise ValidationError('Rating must be between 0 and 10')

        return rating