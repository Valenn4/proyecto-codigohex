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



def home(request):
    if request.method == 'POST':
            if 'formAudio' in request.POST:
                recognizer = sr.Recognizer()
                '''
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                '''
                try:
                    #texto_grabado = recognizer.recognize_google(audio, language='es-ES') 
                    texto_grabado = 'hola'
                    respuesta = chatear(texto_grabado)
                    sintetizar_voz(respuesta)
                    if respuesta == '../juegos':
                        return redirect(f'{respuesta}')
                    if respuesta == '../calendario':
                        return redirect(f'{respuesta}')
                
                    # Renderizar la plantilla con la respuesta
                    
                    return render(request, 'home.html', {'texto_grabado': texto_grabado,'respuesta': respuesta, 'visible_chatbot':True})
                except sr.UnknownValueError:
                    texto_grabado = "Google Speech Recognition no pudo entender el audio"
                    return render(request, 'home.html', {'texto_grabado': texto_grabado})

                except sr.RequestError as e:
                    texto_grabado = f"Error en la solicitud a Google Speech Recognition; {e}"
                    return render(request, 'home.html', {'texto_grabado': texto_grabado})
    


    
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