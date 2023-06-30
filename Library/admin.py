from django.contrib import admin
from .models import Game, UserGame

class GameFilter(admin.ModelAdmin):
    list_display = ('name', 'genre', 'developer', 'platform')
    list_filter = ('genre', 'developer', 'platform')
    list_editable = ('genre', 'developer', 'platform')
    #list_display_links = ('name')

class UserGameAdmin(admin.ModelAdmin):
    list_display = ('game', 'rating', 'achievements', 'playtime', 'addedDateTime')
    list_filter = ('rating', 'achievements', 'playtime')
    list_editable = ('rating', 'achievements', 'playtime')
    #list_display_links = ('game')

admin.site.register(UserGame, UserGameAdmin)
admin.site.register(Game, GameFilter)
