from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import RegistroForm

# def registro(response):
#     if response.method == "POST":
#         form = RegistroForm(response.POST)
#         if form.is_valid():
#             form.save()
        
#         return redirect("/")
#     else:
#         form = RegistroForm()
#     return render(response, "registro/registro.html", {"form" : form})

def login (response):
    return render (response, 'login.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')