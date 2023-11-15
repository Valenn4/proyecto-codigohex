from django.shortcuts import render, redirect
from .forms import FormRegister, FormLogin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name=None, login_url="login")
def home(request):
    return render(request, 'home.html')

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
    return render(request, 'login.html', context)

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
    return render(request, 'register.html', context)