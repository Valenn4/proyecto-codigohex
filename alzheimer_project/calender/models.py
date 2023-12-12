from django.db import models
from authentication.models import User
from enum import Enum
# Create your models here.

class Game(models.Model):
    name=models.CharField(max_length=50, null=False)
    description=models.TextField(null=False)
    cognitive_level=models.IntegerField()

class Action(models.Model):
    name= models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    video = models.FileField(upload_to="videos/", null=False)

class Music(models.Model):
    id_music = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, null=False)

class Object(models.Model):
    name= models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="images/", null=False)

class Activity(models.Model):
    user = models.ForeignKey(to=User, null=False, on_delete=models.CASCADE)
    date=models.DateField(null=False)
    time=models.TimeField(null=True)
    id_game = models.ForeignKey(to=Game, null=True, blank=True, on_delete=models.CASCADE)
    id_action = models.ForeignKey(to=Action, null=True, blank=True, on_delete=models.CASCADE)
    id_music = models.ForeignKey(to=Music, null=True, blank=True, on_delete=models.CASCADE)
    id_object = models.ForeignKey(to=Object, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
