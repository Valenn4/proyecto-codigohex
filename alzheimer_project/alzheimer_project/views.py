from django.shortcuts import render, redirect
import cv2
import threading
from authentication.opencv.detect_object import object




def about(request):
    
    return render(request,"about.html")

def detect_object(request):
    if request.method == 'POST':
        print(request.POST)
        objeto = object(request.FILES['img_object'])
        print(objeto)
        
    return render(request, 'detect_object/detect_object.html')