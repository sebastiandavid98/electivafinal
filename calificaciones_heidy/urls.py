"""
URLs de la app calificaciones_heidy.
Todas las rutas requieren autenticación (se controla en las vistas).
"""

from django.urls import path
from . import views

app_name = 'calificaciones_heidy'

urlpatterns = [
    # Listado de calificaciones
    path('', views.lista_calificaciones, name='lista'),
    # Crear nueva calificación
    path('nueva/', views.crear_calificacion, name='crear'),
    # Editar calificación existente
    path('<int:pk>/editar/', views.editar_calificacion, name='editar'),
    # Eliminar calificación
    path('<int:pk>/eliminar/', views.eliminar_calificacion, name='eliminar'),
]
