from django.shortcuts import render, redirect
from core.models import Producto
from .forms import crearProductoForm
# import ipdb; ipdb.set_trace()
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
        print('entro primer if')
        if formulario.is_valid():
            try:
                print('entro segundo if')
                formulario.save()
                datos['mensaje'] = 'Producto almacenado correctamente'
                redirect ("listar")
            except: print('NO SE CREÓ EL PRODUCTO')
    
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

def eliminar_producto (request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect("listar")