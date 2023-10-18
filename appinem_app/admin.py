from django.contrib import admin
from .models import Estudiante, Profesor, Admin

admin.site.register(Estudiante)

# Registrar el modelo Profesor
admin.site.register(Profesor)

# Registrar el modelo Admin
admin.site.register(Admin)