# Pull Requests — Evaluaciones Heidy

Este documento describe los PRs que deben ser creados para integrar las features en `dev`.

---

## PR #1: Models — Calificacion Model Implementation

**Base:** `dev`  
**Compare:** `feature/models`  
**Estado:** Ready for Review

### Descripción

Implementa el modelo `Calificacion` con cálculo automático de promedio.

### Cambios

- ✅ Modelo `Calificacion` con campos: nombre_estudiante, identificacion, asignatura
- ✅ Tres campos decimales: nota1, nota2, nota3
- ✅ Campo `promedio` no editable, calculado automáticamente
- ✅ Función `calcular_promedio()` con redondeo a dos decimales (ROUND_HALF_UP)
- ✅ Override de `save()` para cálculo automático
- ✅ Migración inicial generada

### Commits

```
94eb99c feat(models): Add module documentation for Calificacion model
```

### Checklist

- [x] Modelo implementado correctamente
- [x] Validaciones en el modelo
- [x] Migraciones generadas
- [x] Documentación incluida
- [x] Tests pasando

---

## PR #2: Authentication — Django Auth Integration

**Base:** `dev`  
**Compare:** `feature/authentication`  
**Estado:** Ready for Review

### Descripción

Configura el sistema de autenticación usando vistas integradas de Django.

### Cambios

- ✅ Rutas `/login/` y `/logout/` configuradas
- ✅ Uso de `django.contrib.auth.views.LoginView`
- ✅ Uso de `django.contrib.auth.views.LogoutView`
- ✅ Template `registration/login.html` configurado
- ✅ Redirecciones configuradas en settings.py

### Commits

```
f6a41dd feat(auth): Configure Django authentication routes with LoginView and LogoutView
```

### Checklist

- [x] LoginView funcionando
- [x] LogoutView funcionando
- [x] Redirecciones correctas
- [x] Template de login responsive
- [x] CSRF protection habilitada

---

## PR #3: Forms — CalificacionForm Implementation

**Base:** `dev`  
**Compare:** `feature/forms`  
**Estado:** Ready for Review

### Descripción

Implementa `CalificacionForm` usando ModelForm con validaciones personalizadas.

### Cambios

- ✅ `CalificacionForm` extendiendo `ModelForm`
- ✅ Campo `promedio` excluido (auto-calculado)
- ✅ Validación de notas entre 0.00 y 5.00
- ✅ Widgets con clases Bootstrap
- ✅ Placeholders y labels descriptivos

### Commits

```
0384f3d feat(forms): Implement CalificacionForm with ModelForm and validation
```

### Checklist

- [x] Formulario valida correctamente
- [x] Exclusión de promedio funciona
- [x] Validaciones personalizadas funcionan
- [x] Estilos Bootstrap aplicados
- [x] Mensajes de error claros

---

## PR #4: Views — CRUD Views with Authentication

**Base:** `dev`  
**Compare:** `feature/views`  
**Estado:** Ready for Review

### Descripción

Implementa vistas CRUD protegidas con autenticación.

### Cambios

- ✅ `lista_calificaciones()` — listado de registros
- ✅ `crear_calificacion()` — crear nuevo registro
- ✅ `editar_calificacion()` — editar registro existente
- ✅ `eliminar_calificacion()` — eliminar con confirmación
- ✅ Decorador `@login_required` en todas las vistas
- ✅ Uso de `get_object_or_404` para seguridad

### Commits

```
be5c2f0 feat(views): Implement CRUD views with authentication protection
```

### Checklist

- [x] Todas las vistas requieren autenticación
- [x] Redirecciones correctas
- [x] Manejo de errores 404
- [x] Formularios procesados correctamente
- [x] Mensajes de éxito/error

---

## PR #5: Templates — Responsive HTML Templates

**Base:** `dev`  
**Compare:** `feature/templates`  
**Estado:** Ready for Review

### Descripción

Crea templates HTML responsive para autenticación y CRUD.

### Cambios

- ✅ `registration/login.html` — formulario de login
- ✅ `calificaciones_heidy/lista.html` — tabla de registros
- ✅ `calificaciones_heidy/formulario.html` — crear/editar
- ✅ `calificaciones_heidy/confirmar_eliminar.html` — confirmación
- ✅ Tema verde consistente (#0c4b33)
- ✅ Diseño responsive
- ✅ CSRF protection en formularios

### Commits

```
fd437c3 feat(templates): Create responsive HTML templates for authentication and CRUD
```

### Checklist

- [x] Templates renderean correctamente
- [x] Diseño responsive en móvil
- [x] Navegación funcional
- [x] Formularios accesibles
- [x] Estilos consistentes

---

## PR #6: Configuration — Settings and Dependencies

**Base:** `master`  
**Compare:** `dev`  
**Estado:** Ready for Review

### Descripción

Integra todas las features en `dev` con configuración centralizada.

### Cambios

- ✅ `settings.py` actualizado con documentación
- ✅ `.gitignore` para Python/Django
- ✅ `requirements.txt` con Django 6.0.3
- ✅ Configuración de autenticación
- ✅ Configuración de templates y static files

### Commits

```
dfd0d59 chore(config): Update settings.py documentation and structure
66228de chore(git): Add .gitignore for Python and Django projects
af42102 chore(deps): Add requirements.txt with Django dependency
```

### Checklist

- [x] Settings.py bien documentado
- [x] .gitignore completo
- [x] requirements.txt actualizado
- [x] Todas las apps registradas
- [x] Redirecciones configuradas

---

## Instrucciones para crear los PRs en GitHub

### Opción 1: Usando GitHub Web UI

1. Ve a https://github.com/sebastiandavid98/ElectivaFinal
2. Haz clic en "Pull requests"
3. Haz clic en "New pull request"
4. Selecciona:
   - **Base:** `dev`
   - **Compare:** `feature/models`
5. Completa el título y descripción (usa el contenido de arriba)
6. Haz clic en "Create pull request"
7. Repite para cada feature

### Opción 2: Usando GitHub CLI (si está instalado)

```bash
cd evaluaciones_heidy

# PR #1: Models
gh pr create --base dev --head feature/models \
  --title "feat(models): Implement Calificacion model" \
  --body "Implementa el modelo Calificacion con cálculo automático de promedio"

# PR #2: Authentication
gh pr create --base dev --head feature/authentication \
  --title "feat(auth): Configure Django authentication" \
  --body "Configura LoginView y LogoutView con redirecciones"

# PR #3: Forms
gh pr create --base dev --head feature/forms \
  --title "feat(forms): Implement CalificacionForm" \
  --body "Implementa ModelForm con validaciones personalizadas"

# PR #4: Views
gh pr create --base dev --head feature/views \
  --title "feat(views): Implement CRUD views" \
  --body "Vistas CRUD protegidas con @login_required"

# PR #5: Templates
gh pr create --base dev --head feature/templates \
  --title "feat(templates): Create HTML templates" \
  --body "Templates responsive para autenticación y CRUD"

# PR #6: Configuration (dev → master)
gh pr create --base master --head dev \
  --title "chore(config): Merge dev into master" \
  --body "Integración de todas las features en dev"
```

---

## Estado de las ramas

```
master (806414f)
  └── dev (af42102)
      ├── feature/models (94eb99c)
      ├── feature/authentication (f6a41dd)
      ├── feature/forms (0384f3d)
      ├── feature/views (be5c2f0)
      └── feature/templates (fd437c3)
```

---

## Próximos pasos

1. ✅ Ramas creadas y pusheadas a GitHub
2. ⏳ Crear PRs en GitHub
3. ⏳ Revisar y aprobar PRs
4. ⏳ Mergear a `dev`
5. ⏳ Mergear `dev` a `master` (release)

