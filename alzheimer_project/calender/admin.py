from django.contrib import admin
from .models import  Activity, Object, Music, Game, Action
# Register your models here.

admin.site.register(Activity)
admin.site.register(Object)
admin.site.register(Music)
admin.site.register(Game)
admin.site.register(Action)