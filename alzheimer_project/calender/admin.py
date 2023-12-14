from django.contrib import admin
from .models import  Activity, Music, Game, Action
# Register your models here.

admin.site.register(Activity)
admin.site.register(Music)
admin.site.register(Game)
admin.site.register(Action)