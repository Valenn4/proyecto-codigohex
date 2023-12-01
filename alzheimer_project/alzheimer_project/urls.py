from django.contrib import admin
from django.urls import path, include
from .views import about, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('', include('calender.urls')),
    path('api/', include('api.urls')),
    path('sobre_nosotros/',about,name='about'),
    path('perfil/',profile,name='profile')
    
]


