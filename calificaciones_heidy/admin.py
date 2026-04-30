from django.contrib import admin
from .models import Calificacion


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_estudiante', 'identificacion',
        'asignatura', 'nota1', 'nota2', 'nota3', 'promedio',
    )
    list_filter = ('asignatura',)
    search_fields = ('nombre_estudiante', 'identificacion', 'asignatura')
    # 'promedio' es editable=False, Django lo excluye del form automáticamente
    readonly_fields = ('promedio',)
