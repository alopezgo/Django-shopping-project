from django.contrib import admin
from .models import Categoria, EmpresaPyme, Producto


# Register your models here.
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ('idCategoria', 'nombreCategoria')
admin.site.register(Categoria, CategoriaAdmin)

class EmpresaAdmin (admin.ModelAdmin):
    list_display = ('idPyme','nombrePyme', 'rutPyme')
admin.site.register(EmpresaPyme, EmpresaAdmin)

class ProductoAdmin (admin.ModelAdmin):
    list_display = ('idProducto', 'nombreProducto', 'categoriaProducto', 'pymeProducto','precioProducto', 'stockProducto')
    list_filterm = ('activoProducto','pymeProducto', 'categoriaProducto')
admin.site.register(Producto, ProductoAdmin)

