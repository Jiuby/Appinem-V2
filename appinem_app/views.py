from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def actualizaciones_view(request):
    return render(request, 'actualizaciones.html')

def noticias_view(request):
    return render(request, 'noticias.html')

def login_view(request):
    return render(request, 'Login.html')

def login_admin_view(request):
    return render(request, 'LoginAdmin.html')

def login_profesores_view(request):
    return render(request, 'LoginProfesores.html')
