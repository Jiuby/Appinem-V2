from django.shortcuts import render, redirect
from .forms import EstudianteForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
def index_view(request):
    return render(request, 'index.html')

def actualizaciones_view(request):
    return render(request, 'actualizaciones.html')

def noticias_view(request):
    return render(request, 'noticias.html')


def login_view(request):
    return render(request, 'Login.html')


def registro_view(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm()

    return render(request, "registro.html", {'form': form})
def login_admin_view(request):
    return render(request, 'LoginAdmin.html')

def login_profesores_view(request):
    return render(request, 'LoginProfesores.html')

def appinemEstudiantes_view(request):
    return render(request, 'appinemEstudiantes.html')

def appinemProfesores_view(request):
    return render(request, 'appinemProfesores.html')

def appinemAdmin_view(request):
    return render(request, 'appinemAdmin.html')