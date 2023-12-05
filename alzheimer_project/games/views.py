from django.shortcuts import render
from calender.models import Game
# Create your views here.


def games(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request, 'games/games.html', context)

def tetris(request):
    return render(request, 'games/tetris.html')

def memory(request):
    return render(request, 'games/memory.html')

def sopa_de_letras(request):
    return render(request, 'games/sopa_de_letras.html')