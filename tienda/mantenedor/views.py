from django.shortcuts import render
from core.models import Producto
from . import forms

# Create your views here.

def listar (request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_form (request):
    
    return render(request, 'create.html', {'form': forms.crearProductoForm})