from django.db import models


class Elemento(models.Model):
    """Modelo de ejemplo. Reemplázalo con tus propios modelos."""
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        ordering = ['-creado_en']

    def __str__(self):
        return self.nombre
