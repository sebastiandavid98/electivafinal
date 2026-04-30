"""
Vistas de la aplicación calificaciones_heidy.

Todas las vistas requieren autenticación mediante @login_required.
Las rutas no autenticadas redirigen a LOGIN_URL (/login/).
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CalificacionForm
from .models import Calificacion


@login_required
def lista_calificaciones(request):
    """Muestra todas las calificaciones registradas."""
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificaciones_heidy/lista.html', {
        'calificaciones': calificaciones,
    })


@login_required
def crear_calificacion(request):
    """Crea una nueva calificación."""
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones_heidy:lista')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones_heidy/formulario.html', {
        'form': form,
        'titulo': 'Nueva calificación',
    })


@login_required
def editar_calificacion(request, pk):
    """Edita una calificación existente."""
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones_heidy:lista')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones_heidy/formulario.html', {
        'form': form,
        'titulo': f'Editar — {calificacion.nombre_estudiante}',
    })


@login_required
def eliminar_calificacion(request, pk):
    """Elimina una calificación tras confirmación POST."""
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones_heidy:lista')
    return render(request, 'calificaciones_heidy/confirmar_eliminar.html', {
        'calificacion': calificacion,
    })
