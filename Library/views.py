from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm

def landingPage(request):
    games = Game.objects.all()
    return render(request, 'landingPage.html', {'games': games})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_add(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'game_edit.html', {'form': form})

def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'game_confirm_delete.html', {'game': game})