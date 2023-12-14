from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
import requests
from .forms import FormRegister, FormLogin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from authentication.models import User, Contact
import speech_recognition as sr
from lilly.chatbot import chatear
from lilly.voz import sintetizar_voz
import cv2
import threading
from time import sleep
from .opencv.opencv_emociones import detectar_emociones_en_rostro, detectar_emociones, detectar_rostros


# Create your views here.
class VideoCaptureThread(threading.Thread):
    def __init__(self, result_emotion_callback):
        super().__init__()
        self.result_emotion_callback = result_emotion_callback
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()

                if not ret:
                    break

                # Aplicar la detección de emociones en rostros
                self.result_emotion_callback(detectar_emociones_en_rostro(frame))


                # Salir si se presiona 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Liberar la captura y cerrar la ventana
            cap.release()
            cv2.destroyAllWindows()

            while True:
                ret, frame = cap.read()

                if not ret:
                    break
                
                self.result_emotion_callback(detectar_emociones_en_rostro(frame))
                # Aplicar la detección de emociones en rostros
                frame_con_emociones = detectar_emociones_en_rostro(frame)

                cv2.imshow('Deteccion de Emociones en vivo', frame_con_emociones)

                # Salir si se presiona 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            

    def stop(self):
        self.stop_event.set()
video_capture_thread = None
def start_video_capture(result_emotion_callback):
    global video_capture_thread
    video_capture_thread = VideoCaptureThread(result_emotion_callback)
    video_capture_thread.start()
def stop_video_capture():
    global video_capture_thread
    if video_capture_thread:
        video_capture_thread.stop()
        video_capture_thread.join()
        video_capture_thread = None
def capture_faces(imagen):
    while True:
        return detectar_emociones_en_rostro(imagen)



def home(request):
    if request.method == 'POST':
            if 'formAudio' in request.POST:
                recognizer = sr.Recognizer()

                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                try:
                    texto_grabado = recognizer.recognize_google(audio, language='es-ES') 
                    texto_grabado = 'hola'
                    respuesta = chatear(texto_grabado)
                    
                    if respuesta == '../juegos':
                        return redirect(f'{respuesta}')
                    if respuesta == '../calendario':
                        return redirect(f'{respuesta}')
                
                    # Renderizar la plantilla con la respuesta
                    
                    return render(request, 'home.html', {'texto_grabado': texto_grabado,'respuesta': respuesta})
                except sr.UnknownValueError:
                    texto_grabado = "Google Speech Recognition no pudo entender el audio"
                    return render(request, 'home.html', {'texto_grabado': texto_grabado})

                except sr.RequestError as e:
                    texto_grabado = f"Error en la solicitud a Google Speech Recognition; {e}"
                    return render(request, 'home.html', {'texto_grabado': texto_grabado})
    
    result_emotion_lock = threading.Lock()
    def result_emotion_callback(emotion):
        with result_emotion_lock:
            print(emotion)
            requests.post(f'http://127.0.0.1:8000/api/feeling/{request.user.id}', data={"feeling":emotion})
            sleep(0.1)


    start_video_capture(result_emotion_callback)
    
    return render(request, 'home.html')

@login_required(redirect_field_name=None, login_url="login")
def profile(request):
    etapas_alzheimer = [
            'Etapa 1. No existe demencia.',
            "Etapa 2. Pérdida.",
            "Etapa 3. Deterioro cognitivo leve.",
            "Etapa 4. Declive cognitivo leve.(Demencia leve).",
            "Etapa 5. Declive cognitivo moderado."
        ]

    if request.user.etapa != None:
        etapas_alzheimer.remove(request.user.etapa)

    contact_user = ''
    if Contact.objects.filter(user=request.user).count()!=0:
        contact_user = Contact.objects.get(user=request.user)

    context = {
        "etapas_alzheimer": etapas_alzheimer,
        "contact_user": contact_user
    }

    if request.method == 'POST':
        print(request.FILES)
        # MODEL USER
        user = User.objects.get(id=request.user.id)
        if 'avatar' in request.FILES:
            user.avatar = request.FILES["avatar"]
        if request.POST["fecha_nacimiento"] != '':
            user.fecha_nacimiento = request.POST["fecha_nacimiento"]
        user.direccion = request.POST["direccion"]
        user.codigo_postal = request.POST["codigo_postal"]
        user.medicacion = request.POST["medicacion"]
        user.etapa = request.POST["etapa"]
        if request.POST["numero_telefono"] != '':
            user.numero_telefono = request.POST["numero_telefono"]
        user.save()

        # MODEL CONTACT
        if Contact.objects.filter(user=request.user).count()!=0:
            contact = Contact.objects.get(user=request.user)
            if 'avatar_contact' in request.FILES:
                contact.avatar = request.FILES["avatar_contact"]
            contact.firstname = request.POST["firstname_contact"]
            contact.lastname = request.POST["lastname_contact"]
            contact.number_phone = request.POST["phone_contact"]
            contact.address = request.POST["address_contact"]
            contact.email = request.POST["email_contact"]
            contact.save()
        else:
            new_contact = Contact.objects.create(
                user = request.user,
                firstname = request.POST["firstname_contact"],
                lastname = request.POST["lastname_contact"],
                number_phone = request.POST["phone_contact"],
                address = request.POST["address_contact"],
                email = request.POST["email_contact"]
            )
            new_contact.save()

        return redirect("profile")
    return render(request,"authentication/profile.html", context)
    

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.data["username"], password=form.data["password"])
            if user:
                auth_login(request, user)
                return redirect("home")
        else:
            error = form.error_messages["invalid_login"]
    else:
        form = FormLogin()
        error = ''

    context = {
        'form':form,
        'error':error
    }
    return render(request, 'authentication/login.html', context)

def register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        elif form.data["password1"]!=form.data["password2"]:
            error = form.error_messages["password_mismatch"]
        else:
            error = form.error_messages["exists_user"]
    else:
        form = FormRegister()
        error = ''

    context = {
        'form':form,
        'error':error
    }
    return render(request, 'authentication/register.html', context)