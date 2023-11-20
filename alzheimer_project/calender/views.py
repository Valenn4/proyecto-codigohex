from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activity
from .forms import FormActivity, FormAction, FormObject,FormGame, FormMusic
# Create your views here.

@login_required(redirect_field_name=None, login_url='login')
def calender(request):
    if request.method == 'POST':
        if 'formAction' in request.POST:
            formAction = FormAction(request.POST)
            if formAction.is_valid():
                id = formAction.save()
                Activity.objects.create(user=request.user, 
                                        date=formAction.data["date"], 
                                        time=formAction.data["time"],
                                        id_action=id)
        elif 'formObject' in request.POST:
                formObject = FormObject(request.POST)
                if formObject.is_valid():
                    id = formObject.save()
                    Activity.objects.create(user=request.user, 
                                            date=formObject.data["date"], 
                                            time=formObject.data["time"],
                                            id_object=id)  
        elif 'formGame' in request.POST:
                formGame = FormGame(request.POST)
                if formGame.is_valid():
                    id = formGame.save()
                    Activity.objects.create(user=request.user, 
                                            date=formGame.data["date"], 
                                            time=formGame.data["time"],
                                            id_game=id)  
        elif 'formMusic' in request.POST:
                formMusic = FormMusic(request.POST)
                if formMusic.is_valid():
                    id = formMusic.save()
                    Activity.objects.create(user=request.user, 
                                            date=formMusic.data["date"], 
                                            time=formMusic.data["time"],
                                            id_music=id)  
        formAction = FormAction()
        formObject = FormObject()
        formGame = FormGame()
        formMusic = FormMusic()
    else:
        formAction = FormAction()
        formObject = FormObject()
        formGame = FormGame()
        formMusic = FormMusic()
    context = {
        "activities": Activity.objects.filter(user=request.user),
        'formAction': formAction,
        'formObject': formObject,
        'formGame': formGame,
        'formMusic': formMusic
    }
    return render(request,'calender/calender.html', context)
