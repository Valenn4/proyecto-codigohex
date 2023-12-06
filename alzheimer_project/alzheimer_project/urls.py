from django.contrib import admin
from django.urls import path, include
from .views import about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('', include('calender.urls')),
    path('api/', include('api.urls')),
    path('juegos/', include('games.urls')),
    path('sobre_nosotros/',about,name='about'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


