from django.urls import path
from . import views

app_name = 'mantenedor'

urlpatterns = [
    path('listar', views.listar, name="listar"),
    path('crear', views.crear_producto, name="crear"),
    ]