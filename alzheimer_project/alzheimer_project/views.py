from django.shortcuts import render, redirect
from authentication.models import User

def about(request):
    
    return render(request,"about.html")

def profile(request):
    etapas_alzheimer = [
            'Etapa 1. No existe demencia.',
            "Etapa 2. Pérdida.",
            "Etapa 3. Deterioro cognitivo leve.",
            "Etapa 4. Declive cognitivo leve.(Demencia leve).",
            "Etapa 5. Declive cognitivo moderado."
        ]
    etapas_alzheimer.remove(request.user.etapa)
    context = {
        "etapas_alzheimer": etapas_alzheimer
    }
    
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.fecha_nacimiento = request.POST["fecha_nacimiento"]
        user.direccion = request.POST["direccion"]
        user.codigo_postal = request.POST["codigo_postal"]
        user.medicacion = request.POST["medicacion"]
        user.etapa = request.POST["etapa"]
        user.numero_telefono = request.POST["numero_telefono"]

        user.save()
        print(user.etapa)
        return redirect("profile")
    return render(request,"profile.html", context)
    