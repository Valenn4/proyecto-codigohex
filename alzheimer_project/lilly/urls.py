from django.urls import path
from . import views
urlpatterns=[
    path('grabar_audio',views.grabar_audio, name="grabar_audio"),
    #path('mostrar_transcripcion', views.mostrar_transcripcion, name='mostrar_transcripcion'),
]