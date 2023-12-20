from django.urls import path
from authentication import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", views.home, name="home")
]