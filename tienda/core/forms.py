from django import forms
from django.forms import ModelForm
from .models import Cliente
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"