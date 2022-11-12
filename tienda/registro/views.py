from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  RegistroForm
from core.views import index

def registro(response):
    if response.method == "POST":
        form = RegistroForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/")
    else:
        form = RegistroForm()
    return render(response, "registro.html", {"form" : form})


@login_required
def perfil(request):
    return render(request, 'perfil.html')
    

@login_required
def logout(request):
    response = redirect("/")
    response.delete_cookie('sessionid')
    response.delete_cookie('csrftoken')
    return response
