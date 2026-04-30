from django.contrib import admin
from .models import Elemento


@admin.register(Elemento)
class ElementoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'creado_en')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
    list_editable = ('activo',)
