# chatbot/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
import speech_recognition as sr
from .chatbot import chatear
from .voz import sintetizar_voz
import datetime

def grabar_audio(request):
    
    return render(request, 'chatbot/mostrar_transcripcion.html')
