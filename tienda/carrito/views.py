from django.shortcuts import render
from core.models import Producto
# Create your views here.

def carrito (request):
    return render(request, 'carrito.html')