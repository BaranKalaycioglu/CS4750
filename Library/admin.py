from django.contrib import admin
from .models import Game

class GameFilter(admin.ModelAdmin):
    list_display = ('name', 'genre', 'developer', 'platform')
    list_filter = ('genre', 'developer', 'platform')
    list_editable = ('genre', 'developer', 'platform')
    list_display_links = ('name',)

admin.site.register(Game, GameFilter)
