from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import User


class FormRegister(UserCreationForm):
    error_messages = {
        'exists_user': 'Ya existe un usuario con el mismo nombre',
        "password_mismatch": "Las contraseñas no coinciden"
    }
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class FormLogin(AuthenticationForm):
    error_messages = {
        'invalid_login':"Datos incorrectos. Vuelve a intentarlo"
    }

    class Meta:
        model = User
        fields = ["username", "password"]