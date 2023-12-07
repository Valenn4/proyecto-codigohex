# chatbot/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
import speech_recognition as sr
from .chatbot import chatear
from .voz import sintetizar_voz

def grabar_audio(request):
    if request.method == 'POST':
        if 'formAudio' in request.POST:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                
                audio = recognizer.listen(source)
            
            
            try:
                template_name = request.POST['template_name']
                template2=f'{template_name}.html'
                texto_grabado = recognizer.recognize_google(audio, language='es-ES') 
                respuesta = chatear(texto_grabado)
                if respuesta == '../juegos':
                    return JsonResponse({'redirect': respuesta})
                if respuesta == '../calendario':
                    return JsonResponse({'redirect': respuesta})
                
                # Renderizar la plantilla con la respuesta
                print(respuesta)
            except sr.UnknownValueError:
                texto_grabado = "Google Speech Recognition no pudo entender el audio"
                return JsonResponse({'error': texto_grabado})
            except sr.RequestError as e:
                texto_grabado = f"Error en la solicitud a Google Speech Recognition; {e}"
                return JsonResponse({'error': texto_grabado})

    return render(request, 'grabar_audio.html')
