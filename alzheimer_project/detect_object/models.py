from django.db import models

# Create your models here.

class DetectObject(models.Model):
    imagen = models.ImageField(upload_to="objects/")
