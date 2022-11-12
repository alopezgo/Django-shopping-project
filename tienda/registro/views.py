from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .forms import  RegistroForm

def registro(response):
    if response.method == "POST":
        form = RegistroForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/")
    else:
        form = RegistroForm()
    return render(response, "registro.html", {"form" : form})


def login (response):
    return render (response, 'login.html')

@login_required
def perfil(request):
    data = JSONParser().parse(request)
    
    username= data['username']
    password = data['password']
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario inválido')
    
    pass_validate = check_password(password, user.password)
    if not pass_validate:
        return Response('Password incorrecta')
    
    # #permite crear o recuperar el token de acceso
    # token, created = Token.objects.get_or_create(user=user)

    return render(request, 'perfil.html')

@login_required
def logout(request):
    response = redirect(login)
    response.delete_cookie('sessionid')
    response.delete_cookie('csrftoken')
    return response