from django.urls import path
from . import views

url_patterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
]