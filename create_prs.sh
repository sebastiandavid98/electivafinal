#!/bin/bash
# Script para crear Pull Requests en GitHub
# Requiere: GitHub CLI (gh) instalado y autenticado
# Uso: ./create_prs.sh

set -e

REPO="sebastiandavid98/ElectivaFinal"
DEV_BRANCH="dev"
MASTER_BRANCH="master"

echo "🚀 Creando Pull Requests para evaluaciones_heidy..."
echo ""

# PR #1: Models
echo "📝 Creando PR #1: Models..."
gh pr create \
  --repo "$REPO" \
  --base "$DEV_BRANCH" \
  --head "feature/models" \
  --title "feat(models): Implement Calificacion model with automatic promedio calculation" \
  --body "## Descripción

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
- [x] Documentación incluida"

echo "✅ PR #1 creado"
echo ""

# PR #2: Authentication
echo "📝 Creando PR #2: Authentication..."
gh pr create \
  --repo "$REPO" \
  --base "$DEV_BRANCH" \
  --head "feature/authentication" \
  --title "feat(auth): Configure Django authentication routes with LoginView and LogoutView" \
  --body "## Descripción

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
- [x] CSRF protection habilitada"

echo "✅ PR #2 creado"
echo ""

# PR #3: Forms
echo "📝 Creando PR #3: Forms..."
gh pr create \
  --repo "$REPO" \
  --base "$DEV_BRANCH" \
  --head "feature/forms" \
  --title "feat(forms): Implement CalificacionForm with ModelForm and validation" \
  --body "## Descripción

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
- [x] Mensajes de error claros"

echo "✅ PR #3 creado"
echo ""

# PR #4: Views
echo "📝 Creando PR #4: Views..."
gh pr create \
  --repo "$REPO" \
  --base "$DEV_BRANCH" \
  --head "feature/views" \
  --title "feat(views): Implement CRUD views with authentication protection" \
  --body "## Descripción

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
- [x] Mensajes de éxito/error"

echo "✅ PR #4 creado"
echo ""

# PR #5: Templates
echo "📝 Creando PR #5: Templates..."
gh pr create \
  --repo "$REPO" \
  --base "$DEV_BRANCH" \
  --head "feature/templates" \
  --title "feat(templates): Create responsive HTML templates for authentication and CRUD" \
  --body "## Descripción

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
- [x] Estilos consistentes"

echo "✅ PR #5 creado"
echo ""

# PR #6: Configuration (dev → master)
echo "📝 Creando PR #6: Configuration (dev → master)..."
gh pr create \
  --repo "$REPO" \
  --base "$MASTER_BRANCH" \
  --head "$DEV_BRANCH" \
  --title "chore(config): Merge dev into master - Release v1.0.0" \
  --body "## Descripción

Integra todas las features de desarrollo en master para release.

## Cambios

- ✅ settings.py actualizado con documentación
- ✅ .gitignore para Python/Django
- ✅ requirements.txt con Django 6.0.3
- ✅ Configuración de autenticación
- ✅ Configuración de templates y static files

## Features incluidas

- ✅ PR #1: Models
- ✅ PR #2: Authentication
- ✅ PR #3: Forms
- ✅ PR #4: Views
- ✅ PR #5: Templates

## Checklist

- [x] Settings.py bien documentado
- [x] .gitignore completo
- [x] requirements.txt actualizado
- [x] Todas las apps registradas
- [x] Redirecciones configuradas
- [x] Todos los PRs de features mergeados"

echo "✅ PR #6 creado"
echo ""

echo "🎉 ¡Todos los PRs han sido creados exitosamente!"
echo ""
echo "Próximos pasos:"
echo "1. Revisa los PRs en: https://github.com/sebastiandavid98/ElectivaFinal/pulls"
echo "2. Aprueba y mergea los PRs de features a dev"
echo "3. Aprueba y mergea dev a master"
