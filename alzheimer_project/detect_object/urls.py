from django.urls import path
from .views import detect_object
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('detect_object/', detect_object, name="detect_object")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
