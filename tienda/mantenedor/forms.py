from django import forms
from django.forms import ModelForm
from core.models import Producto

def crearProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombreProducto', 'descripcionProducto', 'categoriaProducto', 'activoProducto', 'precioProducto', 'imagenProducto', 'stockProducto', 'pymeProducto']