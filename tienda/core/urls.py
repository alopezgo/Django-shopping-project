from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('supermercado', views.tienda, name="supermercado"),
    path('producto/<int:id>', views.show, name="show"),
    path('contacto', views.contacto, name="contacto"),
    path('nosotros', views.nosotros, name="nosotros"),
    ]