from django.db import models
from django.contrib.auth.models import User
from enum import Enum
# Create your models here.

class Types(Enum):
    ACTION='Accion'
    MUSIC='Musica'
    GAME='Juegos'
    OBJECT='Objeto'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value)for i in cls)
    
class Types(Enum):
    ACTION='Accion'
    MUSIC='Musica'
    GAME='Juegos'
    OBJECT='Objeto'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value)for i in cls)
    
class Game(models.Model):
    name=models.CharField(max_length=50, null=False)
    description=models.TextField(null=False)
    cognitive_level=models.IntegerField()




class Activity(models.Model):
    user = models.ForeignKey(to=User, null=False, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=False)
    description=models.TextField()
    type=models.CharField(max_length=50, choices=Types.choices(), null=False)
    date=models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.user.username} - {self.name}'