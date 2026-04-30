# Templates Documentation

## Estructura de Templates

Los templates están organizados en la siguiente estructura:

```
templates/
├── registration/
│   └── login.html          # Formulario de login
└── calificaciones_heidy/
    ├── lista.html          # Listado de calificaciones
    ├── formulario.html     # Crear/editar calificación
    └── confirmar_eliminar.html  # Confirmación de eliminación
```

## Templates Implementados

### registration/login.html
- Formulario de autenticación
- Diseño responsive
- Tema verde (#0c4b33)
- Validación de errores

### calificaciones_heidy/lista.html
- Tabla de calificaciones
- Acciones: editar, eliminar
- Navegación y sesión de usuario
- Botón para crear nueva calificación

### calificaciones_heidy/formulario.html
- Formulario para crear/editar
- Validación de campos
- Botones de guardar/cancelar
- Mensajes de error

### calificaciones_heidy/confirmar_eliminar.html
- Confirmación antes de eliminar
- Información del registro a eliminar
- Botones de confirmar/cancelar

## Características

- ✅ Diseño responsive
- ✅ Tema consistente
- ✅ CSRF protection
- ✅ Accesibilidad
- ✅ Navegación clara
