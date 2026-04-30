"""
URLs raíz del proyecto evaluaciones_heidy.

Rutas registradas:
  /admin/          → Panel de administración de Django
  /login/          → Login  (django.contrib.auth.views.LoginView)
  /logout/         → Logout (django.contrib.auth.views.LogoutView)
  /calificaciones/ → App calificaciones_heidy

Sistema de autenticación:
  - Usa vistas integradas de Django (django.contrib.auth.views)
  - LOGIN_URL redirige a /login/ si no hay sesión
  - LOGIN_REDIRECT_URL redirige a /calificaciones/ tras login exitoso
  - LOGOUT_REDIRECT_URL redirige a /login/ tras logout
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # -----------------------------------------------------------------------
    # Panel de administración
    # -----------------------------------------------------------------------
    path('admin/', admin.site.urls),

    # -----------------------------------------------------------------------
    # Autenticación — vistas integradas de Django
    # -----------------------------------------------------------------------
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),

    # -----------------------------------------------------------------------
    # App de calificaciones
    # -----------------------------------------------------------------------
    path('calificaciones/', include('calificaciones_heidy.urls')),
]
