from django import forms
from .models import Estudiante
from django.contrib.auth.forms import AuthenticationForm

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['tarjeta', 'clave']

class EstudianteLoginForm(AuthenticationForm):
    tarjeta = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tarjeta de Identidad'}))
    clave = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

