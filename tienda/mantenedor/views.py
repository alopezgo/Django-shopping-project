from django.shortcuts import render, redirect
from core.models import Producto
from .forms import crearProductoForm
# Create your views here.

def listar (request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_producto (request):
    
    datos = {
        'form' : crearProductoForm()
        }
    if request.method == 'POST':
        formulario = crearProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            formulario['mensaje'] = 'Producto almacenado correctamente'
            return redirect("listar")
    
    return render(request, 'create.html', datos)

def modificar_producto (request, id):
    producto = Producto.objects.get(idProducto=id)
    print(producto)
    datos = {
        'form': crearProductoForm(instance=producto)
    }
    print("entro a la funcion")
    print(datos)
    
    if request.method == 'POST':
        formulario = crearProductoForm(data=request.POST,  instance=producto)
        print(formulario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente'
            print("me modifico")
    
    return render(request, 'update.html', datos)