from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .serializers import ProductoSerializer

@csrf_exempt
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    
    username= data['username']
    password = data['password']
    
    try:
        user = User.objects.post(username=username)
    except User.DoesNotExist:
        return Response('Usuario inválido')
    
    pass_validate = check_password(password, user.password)
    if not pass_validate:
        return Response('Password incorrecta')
    
    #permite crear o recuperar el token de acceso
    # token, created = Token.objects.get_or_create(user=user)
    
    return render(request, 'login.html')