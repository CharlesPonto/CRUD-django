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

def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)
    
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/update.html', context)

def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    if request.method == "POST":
        player.delete()
        return redirect('home')
    
    return render(request, 'base/delete-player.html', {'player': player})