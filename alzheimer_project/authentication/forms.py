from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FormRegister(UserCreationForm):
    error_messages = {
        'exists_user': 'Ya existe un usuario con el mismo nombre',
        "password_mismatch": "Las contraseñas nocoinciden"
    }
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class FormLogin(AuthenticationForm):
    error_messages = {
        'invalid_login':"Datos incorrectos. Vuelve a intentarlo"
    }

    class Meta:
        model = User
        fields = ["username", "password"]