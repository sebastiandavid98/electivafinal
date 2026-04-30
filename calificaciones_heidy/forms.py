from django import forms
from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    """
    Formulario para crear y editar registros de Calificacion.
    El campo `promedio` se excluye porque se calcula automáticamente
    en el método save() del modelo.
    """

    class Meta:
        model = Calificacion
        # Excluimos 'promedio': es de solo lectura, lo gestiona el modelo.
        exclude = ('promedio',)
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. María García López',
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 1234567890',
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Matemáticas',
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
        }
        labels = {
            'nombre_estudiante': 'Nombre del estudiante',
            'identificacion': 'Identificación',
            'asignatura': 'Asignatura',
            'nota1': 'Nota 1',
            'nota2': 'Nota 2',
            'nota3': 'Nota 3',
        }

    def clean(self):
        """Valida que cada nota esté en el rango 0.00 – 5.00."""
        cleaned_data = super().clean()
        for campo in ('nota1', 'nota2', 'nota3'):
            valor = cleaned_data.get(campo)
            if valor is not None:
                if valor < 0 or valor > 5:
                    self.add_error(
                        campo,
                        f'{self.fields[campo].label} debe estar entre 0.00 y 5.00.',
                    )
        return cleaned_data
