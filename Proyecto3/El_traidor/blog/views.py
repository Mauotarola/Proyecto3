from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def desayuno(request):
    return render(request, 'blog/Desayuno.html')

def almuerzo(request):
    return render(request, 'blog/Almuerzo.html')

def postre(request):
    return render(request, 'blog/Postre.html')

def cena(request):
    return render(request, 'blog/Cena.html')

def reposteria(request):
    return render(request, 'blog/Reposteria.html')

def banqueteria(request):
    return render(request, 'blog/Banqueteria.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

