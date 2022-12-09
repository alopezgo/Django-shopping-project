from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):

    categorias = Categoria.objects.all()    
    return render(request, 'index.html', { 'categorias': categorias })

def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')
    
def vista_producto (request, idProducto):
    producto= Producto.objects.get(idProducto=idProducto)
    return render(request, 'vistaproducto.html',{'productos': producto})

def tienda(request):
    page_number = request.GET.get('page')
    allproducts_page = Paginator(Producto.objects.all(), 10)
    
    try:
        allproducts = allproducts_page.page(page_number)
    except PageNotAnInteger:
        allproducts = allproducts_page.page(1)
    except EmptyPage:
        allproducts = allproducts_page.page(1)        
    
    return render(request, 'tienda.html', { 'productos': allproducts })

@login_required
def perfil(request):
    return render(request, 'perfil.html')


def mensaje (request, id):
    #Producto = get_object_or_404(Producto,id=id)


    messages.warning(request, "no se encuentra ningun comentario ")
    