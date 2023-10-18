from django.shortcuts import render, redirect
from .forms import EstudianteForm, EstudianteLoginForm
from .models import Estudiante
from django.contrib.auth import authenticate, login

def index_view(request):
    return render(request, 'index.html')

def actualizaciones_view(request):
    return render(request, 'actualizaciones.html')

def noticias_view(request):
    return render(request, 'noticias.html')


def login_view(request):
    if request.method == 'POST':
        # Si se está intentando iniciar sesión
        login_form = EstudianteLoginForm(request, data=request.POST)
        if login_form.is_valid():
            tarjeta = login_form.cleaned_data['tarjeta']
            clave = login_form.cleaned_data['clave']
            user = authenticate(request, username=tarjeta, password=clave)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        login_form = EstudianteLoginForm()

    # Si no se está intentando iniciar sesión, se puede estar intentando registrar
    if request.method == 'POST':
        registro_form = EstudianteForm(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            # Puedes redirigir a donde desees después del registro
            return redirect('index')
    else:
        registro_form = EstudianteForm()

    return render(request, 'Login.html', {'login_form': login_form, 'registro_form': registro_form})


def login_admin_view(request):
    return render(request, 'LoginAdmin.html')

def login_profesores_view(request):
    return render(request, 'LoginProfesores.html')
