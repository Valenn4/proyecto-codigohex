from django.shortcuts import render, redirect
import cv2
import threading
from authentication.opencv.detect_object import object
from detect_object.forms import FormObject

def about(request):
    
    return render(request,"about.html")




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