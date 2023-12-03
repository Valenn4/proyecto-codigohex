from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(blank=True, null=True, max_length=6)
    medicacion = models.CharField(max_length=200, blank=True, null=True)
    numero_telefono = models.DecimalField(blank=True, max_digits=20, decimal_places=0, null=True)
    etapa = models.CharField(max_length=200, blank=True, null=True)
