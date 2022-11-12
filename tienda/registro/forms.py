from django import forms
from core.forms import FormularioCliente
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm (UserCreationForm):
    form_cliente = FormularioCliente
    
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]

