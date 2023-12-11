from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Activity, Game
from .forms import FormAction, FormObject, FormMusic
# Create your views here.

@login_required(redirect_field_name=None, login_url='login')
def calender(request):
    if request.method == 'POST':
        if Activity.objects.filter(date=request.POST["date"], time=request.POST["time"]).count()>0:
            formAction = FormAction()
            formObject = FormObject()
            formMusic = FormMusic()
            context = {
                "activities": Activity.objects.filter(user=request.user),
                'games': Game.objects.all(),
                'formAction': formAction,
                'formObject': formObject,
                'formMusic': formMusic,
                'error':'Ya hay cargada una tarea en el mismo horario.'
            }
            return render(request,'calender/calender.html', context)
        
        if 'formAction' in request.POST:
            formAction = FormAction(request.POST, request.FILES)
            if formAction.is_valid():
                id = formAction.save()
                Activity.objects.create(user=request.user, 
                                        date=formAction.data["date"], 
                                        time=formAction.data["time"],
                                        id_action=id)
        elif 'formObject' in request.POST:
                formObject = FormObject(request.POST, request.FILES)
                if formObject.is_valid():
                    id = formObject.save()
                    Activity.objects.create(user=request.user, 
                                            date=formObject.data["date"], 
                                            time=formObject.data["time"],
                                            id_object=id)  
        elif 'formGame' in request.POST:
                
                game = Game.objects.get(name=request.POST["game"])

                Activity.objects.create(user=request.user, 
                                        date=request.POST["date"], 
                                        time=request.POST["time"],
                                        id_game=game)  
        elif 'formMusic' in request.POST:
                formMusic = FormMusic(request.POST)
                if formMusic.is_valid():
                    id = formMusic.save()
                    Activity.objects.create(user=request.user, 
                                            date=formMusic.data["date"], 
                                            time=formMusic.data["time"],
                                            id_music=id)  
                    return redirect('calender')
        formAction = FormAction()
        formObject = FormObject()
        formMusic = FormMusic()
    else:
        formAction = FormAction()
        formObject = FormObject()
        formMusic = FormMusic()
    context = {
        "activities": Activity.objects.filter(user=request.user),
        'games': Game.objects.all(),
        'formAction': formAction,
        'formObject': formObject,
        'formMusic': formMusic
    }
    return render(request,'calender/calender.html', context)
