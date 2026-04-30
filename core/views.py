from django.shortcuts import render


def inicio(request):
    """Vista principal de la aplicación."""
    contexto = {
        'titulo': 'Bienvenido a Mi Proyecto Django',
        'mensaje': 'Tu proyecto está funcionando correctamente.',
    }
    return render(request, 'core/inicio.html', contexto)
