from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/new', views.game_add, name='game_add'),
    path('game/<int:pk>/delete', views.game_delete, name='game_delete'),
]
