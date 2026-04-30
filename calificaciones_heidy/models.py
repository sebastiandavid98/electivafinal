"""
Modelos de la aplicación calificaciones_heidy.

Define el modelo Calificacion con cálculo automático de promedio.
"""

from decimal import Decimal, ROUND_HALF_UP
from django.db import models


def calcular_promedio(nota1: Decimal, nota2: Decimal, nota3: Decimal) -> Decimal:
    """
    Calcula el promedio de tres notas y lo redondea a dos decimales.

    Args:
        nota1: Primera nota.
        nota2: Segunda nota.
        nota3: Tercera nota.

    Returns:
        Decimal redondeado a dos cifras decimales.
    """
    promedio = (nota1 + nota2 + nota3) / Decimal('3')
    return promedio.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


class Calificacion(models.Model):
    """
    Almacena las calificaciones de un estudiante para una asignatura.
    El campo `promedio` se calcula automáticamente al guardar.
    """

    nombre_estudiante = models.CharField(
        max_length=150,
        verbose_name='Nombre del estudiante',
    )
    identificacion = models.CharField(
        max_length=15,
        verbose_name='Identificación',
    )
    asignatura = models.CharField(
        max_length=100,
        verbose_name='Asignatura',
    )
    nota1 = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Nota 1',
    )
    nota2 = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Nota 2',
    )
    nota3 = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Nota 3',
    )
    promedio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Promedio',
        editable=False,   # no aparece en formularios ni en el admin
        default=Decimal('0.00'),
    )

    class Meta:
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
        ordering = ['nombre_estudiante', 'asignatura']

    def save(self, *args, **kwargs):
        """Calcula el promedio antes de persistir el registro."""
        self.promedio = calcular_promedio(self.nota1, self.nota2, self.nota3)
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'{self.nombre_estudiante} | {self.asignatura} | '
            f'Promedio: {self.promedio}'
        )
