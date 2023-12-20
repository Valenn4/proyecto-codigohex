from django.urls import path
from calender import views

urlpatterns = [
    path('calendario/',views.calender, name='calender')
]