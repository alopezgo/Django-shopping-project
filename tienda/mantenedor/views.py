from django.shortcuts import render
from core.models import Producto
from .forms import crearProductoForm
# Create your views here.

def listar (request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_producto (request):
    
    return render(request, 'create.html', {'form': crearProductoForm()})