from django.urls import path
from appinem_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index_view, name='index'),
    path('actualizaciones/', views.actualizaciones_view, name='actualizaciones'),
    path('noticias/', views.noticias_view, name='noticias'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('login-admin/', views.login_admin_view, name='login_admin'),
    path('login-profesores/', views.login_profesores_view, name='login_profesores'),
    path('appinemEstudiantes/', views.appinemEstudiantes_view, name='appinemEstudiantes'),
    path('appinemProfesores/', views.appinemProfesores_view, name='appinemProfesores'),
    path('appinemAdmin/', views.appinemAdmin_view, name='appinemAdmin'),
    # Otras URLs...
]
