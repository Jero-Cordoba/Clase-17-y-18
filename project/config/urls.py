from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/", views.saludo),
    path("saludar_vista/", views.saludo_vista),
    path("nombre/<nombre>/<apellido>", views.nombre),
    path("probando_template/", views.probando_template),
]
