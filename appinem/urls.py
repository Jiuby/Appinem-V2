from django.urls import path
from appinem_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index_view, name='index'),
    path('actualizaciones/', views.actualizaciones_view, name='actualizaciones'),
    path('noticias/', views.noticias_view, name='noticias'),
    path('login/', views.login_view, name='login'),
    path('login-admin/', views.login_admin_view, name='login_admin'),
    path('login-profesores/', views.login_profesores_view, name='login_profesores'),
    # Otras URLs...
]
