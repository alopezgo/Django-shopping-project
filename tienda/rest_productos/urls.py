from django.urls import path
from rest_productos.views import lista_productos
from rest_productos.viewsLogin import login

app_name = 'api'

urlpatterns = [
    path('lista-productos', lista_productos, name="lista_productos"),
    path('login', login, name="login")
 

]