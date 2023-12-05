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
    feeling = models.CharField(max_length=100, blank=True, null=True)

class Contact(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    number_phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.firstname
