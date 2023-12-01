from django.shortcuts import render

# Create your views here.


def games(request):
    return render(request, 'games/games.html')

def tetris(request):
    return render(request, 'games/tetris.html')