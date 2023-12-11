# chatbot/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
import speech_recognition as sr
from .chatbot import chatear
from .voz import sintetizar_voz
import datetime

def grabar_audio(request):
    if request.method == 'POST':
            recognizer = sr.Recognizer()

            '''
            with sr.Microphone() as source:
                
                audio = recognizer.listen(source)
            '''
            
            try:
                template_name = request.POST.get('template_name')
                template2=f'{template_name}.html'
                #texto_grabado = recognizer.recognize_google(audio, language='es-ES') 
                texto_grabado = 'hola'
                respuesta = chatear(texto_grabado)
                
                if respuesta == '../juegos':
                    return redirect(f'{respuesta}')
                if respuesta == '../calendario':
                    return redirect(f'{respuesta}')
                if respuesta =='dia':
                    fecha=datetime.now()
                    respuesta=f'Hoy es día {fecha.day} de {fecha.month} de {fecha.year}'
                    sintetizar_voz(respuesta)
                if respuesta =='hora':
                    fecha=datetime.now()
                    respuesta=f'Son las {fecha.hour} y {fecha.minute}'
                    sintetizar_voz(respuesta)
                

                # Renderizar la plantilla con la respuesta
                
                return render(request, template2, {'texto_grabado': texto_grabado,'respuesta': respuesta,'template_name': template_name})
            except sr.UnknownValueError:
                texto_grabado = "Google Speech Recognition no pudo entender el audio"
                return render(request, template2, {'texto_grabado': texto_grabado})

            except sr.RequestError as e:
                texto_grabado = f"Error en la solicitud a Google Speech Recognition; {e}"
                return render(request, template2, {'texto_grabado': texto_grabado})
    return render(request, 'chatbot/mostrar_transcripcion.html')
