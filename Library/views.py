from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, UserGame
from .forms import GameForm, UserGameForm, ReviewForm

def landingPage(request):
    user_games = UserGame.objects.filter()
    return render(request, 'landingPage.html', {'user_games': user_games})

def add_to_library(request):
    if request.method == "POST":
        form = UserGameForm(request.POST)
        if form.is_valid():
            user_game = form.save(commit=False)
            user_game.save()
            return redirect('library')  # update to the new library view
    else:
        form = UserGameForm()
    return render(request, 'add_to_library.html', {'form': form})

def usergame_edit(request, pk):
    usergame = get_object_or_404(UserGame, pk=pk)
    if request.method == "POST":
        form = UserGameForm(request.POST, instance=usergame)
        if form.is_valid():
            usergame = form.save(commit=False)
            usergame.save()
            return redirect('library')  # update to the new library view
    else:
        form = UserGameForm(instance=usergame)
    return render(request, 'game_edit.html', {'form': form})  # reusing the same template

def usergame_details(request, pk):
    usergame = get_object_or_404(UserGame, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=usergame)
        if form.is_valid():
            usergame = form.save()
            return redirect('library')
    else:
        form = ReviewForm(instance=usergame)
    return render(request, 'game_details.html', {'form': form, 'usergame': usergame})

def usergame_delete(request, pk):
    usergame = UserGame.objects.get(pk=pk)
    if request.method == 'POST':
        usergame.delete()
        return redirect('library')  # update to the new library view
    return render(request, 'game_confirm_delete.html', {'usergame': usergame})
