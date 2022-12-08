from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('carrito', views.carrito, name="carrito"),
    path('agregar/<int:producto_id>/',views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/',views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/',views.restar_producto, name="Sub"),
    path('limpiar/',views.limpiar_carrito, name="CLS"),
    
    ]