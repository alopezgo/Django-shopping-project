from django import forms
from django.forms import ModelForm
from core.models import Producto

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

