# Crear Pull Requests en GitHub

## 📍 Estado actual

Todas las ramas están pusheadas a GitHub y listas para crear PRs:

```
✅ feature/models (863219a)
✅ feature/authentication (e5f0764)
✅ feature/forms (868d7c9)
✅ feature/views (cf86277)
✅ feature/templates (f092fb1)
✅ dev (eb9237d)
```

---

## 🔗 Crear PRs manualmente en GitHub

### PR #1: Models

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/models
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `feat(models): Implement Calificacion model with automatic promedio calculation`
   - **Description:**
     ```
     ## Descripción
     Implementa el modelo Calificacion con cálculo automático de promedio.

     ## Cambios
     - ✅ Modelo Calificacion con campos: nombre_estudiante, identificacion, asignatura
     - ✅ Tres campos decimales: nota1, nota2, nota3
     - ✅ Campo promedio no editable, calculado automáticamente
     - ✅ Función calcular_promedio() con redondeo a dos decimales (ROUND_HALF_UP)
     - ✅ Override de save() para cálculo automático
     - ✅ Migración inicial generada

     ## Checklist
     - [x] Modelo implementado correctamente
     - [x] Validaciones en el modelo
     - [x] Migraciones generadas
     - [x] Documentación incluida
     ```
4. Haz clic en "Create pull request"

---

### PR #2: Authentication

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/authentication
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `feat(auth): Configure Django authentication routes with LoginView and LogoutView`
   - **Description:**
     ```
     ## Descripción
     Configura el sistema de autenticación usando vistas integradas de Django.

     ## Cambios
     - ✅ Rutas /login/ y /logout/ configuradas
     - ✅ Uso de django.contrib.auth.views.LoginView
     - ✅ Uso de django.contrib.auth.views.LogoutView
     - ✅ Template registration/login.html configurado
     - ✅ Redirecciones configuradas en settings.py

     ## Checklist
     - [x] LoginView funcionando
     - [x] LogoutView funcionando
     - [x] Redirecciones correctas
     - [x] Template de login responsive
     - [x] CSRF protection habilitada
     ```
4. Haz clic en "Create pull request"

---

### PR #3: Forms

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/forms
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `feat(forms): Implement CalificacionForm with ModelForm and validation`
   - **Description:**
     ```
     ## Descripción
     Implementa CalificacionForm usando ModelForm con validaciones personalizadas.

     ## Cambios
     - ✅ CalificacionForm extendiendo ModelForm
     - ✅ Campo promedio excluido (auto-calculado)
     - ✅ Validación de notas entre 0.00 y 5.00
     - ✅ Widgets con clases Bootstrap
     - ✅ Placeholders y labels descriptivos

     ## Checklist
     - [x] Formulario valida correctamente
     - [x] Exclusión de promedio funciona
     - [x] Validaciones personalizadas funcionan
     - [x] Estilos Bootstrap aplicados
     - [x] Mensajes de error claros
     ```
4. Haz clic en "Create pull request"

---

### PR #4: Views

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/views
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `feat(views): Implement CRUD views with authentication protection`
   - **Description:**
     ```
     ## Descripción
     Implementa vistas CRUD protegidas con autenticación.

     ## Cambios
     - ✅ lista_calificaciones() — listado de registros
     - ✅ crear_calificacion() — crear nuevo registro
     - ✅ editar_calificacion() — editar registro existente
     - ✅ eliminar_calificacion() — eliminar con confirmación
     - ✅ Decorador @login_required en todas las vistas
     - ✅ Uso de get_object_or_404 para seguridad

     ## Checklist
     - [x] Todas las vistas requieren autenticación
     - [x] Redirecciones correctas
     - [x] Manejo de errores 404
     - [x] Formularios procesados correctamente
     - [x] Mensajes de éxito/error
     ```
4. Haz clic en "Create pull request"

---

### PR #5: Templates

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/templates
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `feat(templates): Create responsive HTML templates for authentication and CRUD`
   - **Description:**
     ```
     ## Descripción
     Crea templates HTML responsive para autenticación y CRUD.

     ## Cambios
     - ✅ registration/login.html — formulario de login
     - ✅ calificaciones_heidy/lista.html — tabla de registros
     - ✅ calificaciones_heidy/formulario.html — crear/editar
     - ✅ calificaciones_heidy/confirmar_eliminar.html — confirmación
     - ✅ Tema verde consistente (#0c4b33)
     - ✅ Diseño responsive
     - ✅ CSRF protection en formularios

     ## Checklist
     - [x] Templates renderean correctamente
     - [x] Diseño responsive en móvil
     - [x] Navegación funcional
     - [x] Formularios accesibles
     - [x] Estilos consistentes
     ```
4. Haz clic en "Create pull request"

---

### PR #6: Configuration (dev → main)

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/compare/main...dev
2. Haz clic en "Create pull request"
3. Completa:
   - **Title:** `chore(config): Merge dev into main - Release v1.0.0`
   - **Description:**
     ```
     ## Descripción
     Integra todas las features de desarrollo en main para release.

     ## Features incluidas
     - ✅ PR #1: Models
     - ✅ PR #2: Authentication
     - ✅ PR #3: Forms
     - ✅ PR #4: Views
     - ✅ PR #5: Templates

     ## Cambios
     - ✅ settings.py actualizado con documentación
     - ✅ .gitignore para Python/Django
     - ✅ requirements.txt con Django 6.0.3
     - ✅ Configuración de autenticación
     - ✅ Configuración de templates y static files

     ## Checklist
     - [x] Settings.py bien documentado
     - [x] .gitignore completo
     - [x] requirements.txt actualizado
     - [x] Todas las apps registradas
     - [x] Redirecciones configuradas
     - [x] Todos los PRs de features mergeados
     ```
4. Haz clic en "Create pull request"

---

## 📊 URLs directas para crear PRs

| PR | URL |
|----|-----|
| #1 Models | https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/models |
| #2 Auth | https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/authentication |
| #3 Forms | https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/forms |
| #4 Views | https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/views |
| #5 Templates | https://github.com/sebastiandavid98/ElectivaFinal/compare/dev...feature/templates |
| #6 Release | https://github.com/sebastiandavid98/ElectivaFinal/compare/main...dev |

---

## ✅ Después de crear los PRs

1. **Revisar** cada PR en la sección de Pull Requests
2. **Mergear** los PRs de features a `dev` (en orden)
3. **Mergear** `dev` a `main` para release
4. **Crear tag** de release:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0 - Initial release"
   git push origin v1.0.0
   ```

---

## 🔍 Verificar ramas en GitHub

Ve a: https://github.com/sebastiandavid98/ElectivaFinal/branches

Deberías ver:
- ✅ `dev`
- ✅ `feature/models`
- ✅ `feature/authentication`
- ✅ `feature/forms`
- ✅ `feature/views`
- ✅ `feature/templates`

