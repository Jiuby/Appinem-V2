from django.db import models

class Estudiante(models.Model):
    tarjeta = models.CharField(max_length=50)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f'Estudiante: {self.tarjeta}'

class Profesor(models.Model):
    cedula = models.CharField(max_length=50)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f'Profesor: {self.cedula}'

class Admin(models.Model):
    cedula = models.CharField(max_length=50)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f'Admin: {self.cedula}'
