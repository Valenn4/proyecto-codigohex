from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from .forms import FormRegister, FormLogin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from authentication.models import User, Contact
import cv2
import threading
from time import sleep


# Create your views here.
class VideoCaptureThread(threading.Thread):
    def __init__(self, result_emotion_callback):
        super().__init__()
        self.result_emotion_callback = result_emotion_callback
        self.stop_event = threading.Event()

    def run(self):
        cap = cv2.VideoCapture(0)
        while not self.stop_event.is_set():
            ret, frame = cap.read()
            if ret:
                result_emotion = capture_faces(frame)
                self.result_emotion_callback(result_emotion)
        cap.release()

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
    # Leemos el modelo
    net = cv2.dnn.readNetFromCaffe("C:/Users/mati/Desktop/proyecto-codigohex/alzheimer_project/authentication/opencv/opencv_face_detector.prototxt", "C:/Users/mati/Desktop/proyecto-codigohex/alzheimer_project/authentication/opencv/res10_300x300_ssd_iter_140000.caffemodel")

    # Parametros del modelo
    # Tamaño
    anchonet = 300
    altonet = 300
    # Valores medios de los canales de color
    media = [104, 117, 123]
    umbral = 0.7

    while True:
        # Realizamos conversion de forma
        frame = cv2.flip(imagen, 1)

        # Extraemos info de los frames
        altoframe = frame.shape[0]
        anchoframe = frame.shape[1]

        # Preprocesamos la imagen
        # Images - Factor de escala - tamaño - media de color - Formato de color(BGR-RGB) - Recorte
        blob = cv2.dnn.blobFromImage(frame, 1.0, (anchonet, altonet), media, swapRB = False, crop = False)

        # Corremos el modelo
        net.setInput(blob)
        detecciones = net.forward()

        # Iteramos
        for i in range(detecciones.shape[2]):
            # Extraemos la confianza de esa deteccion
            conf_detect = detecciones[0,0,i,2]
            # Si superamos el umbral (70% de probabilidad de que sea un rostro)
            if conf_detect > umbral:
                # Extraemos las coordenadas
                xmin = int(detecciones[0, 0, i, 3] * anchoframe)
                ymin = int(detecciones[0, 0, i, 4] * altoframe)
                xmax = int(detecciones[0, 0, i, 5] * anchoframe)
                ymax = int(detecciones[0, 0, i, 6] * altoframe)

                # Dibujamos el rectangulo
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,0,255), 2)
                # Texto que vamos a mostrar
                label = "Confianza de deteccion: %.4f" % conf_detect
                # Tamaño del fondo del label
                label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                # Colocamos fondo al texto
                cv2.rectangle(frame, (xmin, ymin - label_size[1]), (xmin + label_size[0], ymin + base_line),
                            (0,0,0), cv2.FILLED)
                # Colocamps el texto
                cv2.putText(frame, label, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
                #cv2.imshow("Imagen", cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
                return 'Es un rostro'
            return 'No es un rostro'

def home(request):
    '''
    result_emotion_lock = threading.Lock()
    def result_emotion_callback(emotion):
        with result_emotion_lock:
            requests.post(f'http://127.0.0.1:8000/api/feeling/{request.user.id}', data={"feeling":emotion})
            sleep(0.2)


    start_video_capture(result_emotion_callback)
    '''
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
        # MODEL USER
        user = User.objects.get(id=request.user.id)
        if request.FILES["avatar"] != '':
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