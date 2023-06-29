from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('add_to_library/', views.add_to_library, name='add_to_library'),
    path('usergame/<int:pk>/edit', views.usergame_edit, name='usergame_edit'),
    path('usergame/<int:pk>/delete', views.usergame_delete, name='usergame_delete'),
]

