import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import ActivitySerializer, ObjectSerializer, GameSerializer, ActionSerializer, MusicSerializer
from calender.models import Activity
from authentication.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

'''
class ObjectView(viewsets.ViewSet):

    def create(self, request):
        data = request.data

        serializer = ObjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response('Objecto agregado correctamente', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GameView(viewsets.ViewSet):

    def create(self, request):
        data = request.data

        serializer = GameSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response('Juego agregado correctamente', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ActionView(viewsets.ViewSet):

    def create(self, request):
        data = request.data

        serializer = ActionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response('Accion agregada correctamente', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MusicView(viewsets.ViewSet):

    def create(self, request):
        data = request.data

        serializer = MusicSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response('Musica agregada correctamente', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

class ActivityByUserDateView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, id, year, month, day):
        if request.user.id == id:
            queryset = Activity.objects.filter(user=User.objects.get(id=id), date=datetime.date(year, month, day))
            serializer = ActivitySerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No tienes acceso a este sitio", status=status.HTTP_401_UNAUTHORIZED)
        
class ActivityByUserView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, id):
        if request.user.id == id:
            queryset = Activity.objects.filter(user=User.objects.get(id=id))
            serializer = ActivitySerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No tienes acceso a este sitio", status=status.HTTP_401_UNAUTHORIZED)
        
    def create(self, request, id):
        data = request.data

        serializer = ActivitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response('Actividad agregada correctamente', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)