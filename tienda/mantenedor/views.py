from django.shortcuts import render, redirect
from core.models import Producto
from .forms import ProductosForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def listar (request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

@login_required
def crear_producto (request):
    
    datos = {
        'form' : ProductosForm()
        }
    if request.method == 'POST':
        formulario = ProductosForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado_productos")
    
    return render(request, 'listar.html', datos)

@login_required
def modificar_producto (request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductosForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST,  instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente'
    
    return render(request, 'listar.html', datos)

@login_required
def eliminar_producto (request, id):
    producto = Producto.objects.get(idproducto=id)
    producto.delete()
    if request.method == 'DELETE':
        formulario = ProductosForm(data=request.DELETE, instance=producto)

        if formulario.is_valid:
            formulario.save()

    return redirect(to="listado_productos")

def listado_productos(request):
    r = request.get('http://127.0.0.1:8000/api/lista-productos')

    datos = {
        'productos': r.json()
    }

    return render(request, 'listar.html', datos)