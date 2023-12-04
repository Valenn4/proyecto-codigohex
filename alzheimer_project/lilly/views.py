# chatbot/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

import speech_recognition as sr
from .chatbot import chatear
from .voz import sintetizar_voz

def grabar_audio(request):
    if request.method == 'POST':
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Habla algo:")
            audio = recognizer.listen(source)
        
        
        try:
            texto_grabado = recognizer.recognize_google(audio, language='es-ES')
            respuesta = chatear(texto_grabado)
            if respuesta == 'games.html':
                return redirect(f'{respuesta}')
            sintetizar_voz(respuesta)

            # Renderizar la plantilla con la respuesta
            return render(request, 'grabar_audio.html', {'texto_grabado': texto_grabado, 'respuesta': respuesta})

        except sr.UnknownValueError:
            texto_grabado = "Google Speech Recognition no pudo entender el audio"
            return render(request, 'grabar_audio.html', {'texto_grabado': texto_grabado})

        except sr.RequestError as e:
            texto_grabado = f"Error en la solicitud a Google Speech Recognition; {e}"
            return render(request, 'grabar_audio.html', {'texto_grabado': texto_grabado})

    return render(request, 'grabar_audio.html')
#def mostrar_transcripcion(request):
 #   texto_grabado = request.session.get('texto_grabado', 'No hay texto grabado')

  #  return render(request, 'mostrar_transcripcion.html', {'texto_grabado': texto_grabado})