"""
Vistas de la aplicación calificaciones_heidy.

Todas las vistas requieren autenticación mediante @login_required.
Las rutas no autenticadas redirigen a LOGIN_URL (/login/).
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg

from .forms import CalificacionForm
from .models import Calificacion


@login_required
def lista_calificaciones(request):
    """Muestra todas las calificaciones registradas."""
    calificaciones = Calificacion.objects.all()
    # Calcular el promedio general de todos los promedios
    promedio_general = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones_heidy/lista.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general,
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
        'titulo': 'Editar calificación',
    })


@login_required
def eliminar_calificacion(request, pk):
    """Elimina una calificación existente."""
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones_heidy:lista')
    return render(request, 'calificaciones_heidy/confirmar_eliminar.html', {
        'calificacion': calificacion,
    })


@login_required
def promedio_general(request):
    """
    Vista especial que muestra el promedio general de todas las calificaciones.
    Utiliza agregación de base de datos para calcular el promedio.
    """
    promedio = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    total_calificaciones = Calificacion.objects.count()
    return render(request, 'calificaciones_heidy/promedio_general.html', {
        'promedio': promedio,
        'total_calificaciones': total_calificaciones,
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
