from rest_framework import serializers
from core.models import Producto, EmpresaPyme

class ProductoSerializer(serializers.ModelSerializer):

    desc_categoria = serializers.CharField(source="categoriaProducto")
    desc_pyme = serializers.CharField(source="pymeProducto")

    class Meta:
        model = Producto
        fields = "__all__"