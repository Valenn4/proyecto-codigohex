from django.urls import path
from games import views

urlpatterns = [
    path('', views.games, name="games"),
    path('tetris/', views.tetris, name="tetris"),
    path('memory/', views.memory, name="memory"),
    path('sopa de letras/', views.sopa_de_letras, name="sopa de letras")
]