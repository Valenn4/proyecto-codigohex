from django.shortcuts import render
from detect_object.detect_object import object
from .forms import FormObject
# Create your views here.


def detect_object(request):
    if request.method == 'POST':
        form = FormObject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            objeto = object(f'C:/Users/mati/Desktop/proyecto-codigohex/alzheimer_project/media/objects/{request.FILES["imagen"]}')
            return render(request, 'detect_object/detect_object.html', {'form':form, 'object':objeto})
    else:
        form = FormObject(request.POST)
    context = {'form':form}
    return render(request, 'detect_object/detect_object.html', context)