from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

# Create your views here.
def home(request):
    players = Player.objects.all()
    context=  {'players': players}
    return render(request, 'base/home.html', context)
    
def createPlayer(request):
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/create-player.html', context)

def updatePlayer():
    pass

def deletePlayer():
    pass