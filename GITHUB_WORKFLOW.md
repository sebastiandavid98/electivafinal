# GitHub Workflow — Evaluaciones Heidy

Guía completa para gestionar los Pull Requests y el flujo de trabajo en GitHub.

---

## 📊 Estado actual del repositorio

### Ramas creadas y pusheadas

```
master (806414f) ← rama principal (protegida)
  └── dev (8ede5c9) ← rama de desarrollo
      ├── feature/models (94eb99c)
      ├── feature/authentication (f6a41dd)
      ├── feature/forms (0384f3d)
      ├── feature/views (be5c2f0)
      └── feature/templates (fd437c3)
```

### Commits en dev

```
8ede5c9 docs(scripts): Add PR creation scripts for bash and PowerShell
7eea29d docs(pr): Add pull request templates and instructions
af42102 chore(deps): Add requirements.txt with Django dependency
66228de chore(git): Add .gitignore for Python and Django projects
dfd0d59 chore(config): Update settings.py documentation and structure
806414f Initial commit: Project structure and configuration
```

---

## 🔄 Flujo de trabajo recomendado

### Paso 1: Crear los Pull Requests

#### Opción A: Usando GitHub CLI (recomendado)

```bash
cd evaluaciones_heidy

# Ejecutar el script de creación de PRs
./create_prs.ps1  # En Windows PowerShell
# o
./create_prs.sh   # En Linux/Mac/Git Bash
```

#### Opción B: Crear manualmente en GitHub Web UI

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/pulls
2. Haz clic en "New pull request"
3. Para cada feature, selecciona:
   - **Base:** `dev`
   - **Compare:** `feature/[nombre]`
4. Completa el título y descripción

#### Opción C: Crear con curl (API de GitHub)

```bash
# Necesitas un token de GitHub en la variable GITHUB_TOKEN
export GITHUB_TOKEN="tu_token_aqui"

# PR #1: Models
curl -X POST https://api.github.com/repos/sebastiandavid98/ElectivaFinal/pulls \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "feat(models): Implement Calificacion model",
    "body": "Implementa el modelo Calificacion con cálculo automático de promedio",
    "head": "feature/models",
    "base": "dev"
  }'
```

---

### Paso 2: Revisar los Pull Requests

1. Ve a: https://github.com/sebastiandavid98/ElectivaFinal/pulls
2. Revisa cada PR:
   - ✅ Verifica que los cambios sean correctos
   - ✅ Revisa los commits
   - ✅ Comprueba que no hay conflictos
   - ✅ Valida que pase los checks (si están configurados)

### Paso 3: Aprobar y Mergear PRs de Features

Para cada PR de feature (models, auth, forms, views, templates):

1. Haz clic en "Review changes"
2. Selecciona "Approve"
3. Haz clic en "Merge pull request"
4. Selecciona "Squash and merge" o "Create a merge commit"
5. Confirma el merge

**Orden recomendado:**
1. feature/models
2. feature/authentication
3. feature/forms
4. feature/views
5. feature/templates

### Paso 4: Mergear dev a master

Una vez que todos los PRs de features estén mergeados a `dev`:

1. Abre el PR de `dev` → `master`
2. Revisa que todos los cambios estén incluidos
3. Aprueba y mergea
4. Crea un tag de release:

```bash
git tag -a v1.0.0 -m "Release v1.0.0 - Initial release"
git push origin v1.0.0
```

---

## 📋 Checklist de PRs

### PR #1: Models
- [ ] Modelo Calificacion creado
- [ ] Campos correctos (nombre_estudiante, identificacion, asignatura, nota1, nota2, nota3)
- [ ] Campo promedio no editable
- [ ] Función calcular_promedio() implementada
- [ ] Redondeo a dos decimales (ROUND_HALF_UP)
- [ ] Migraciones generadas
- [ ] Documentación incluida

### PR #2: Authentication
- [ ] Rutas /login/ y /logout/ configuradas
- [ ] LoginView funcionando
- [ ] LogoutView funcionando
- [ ] Template registration/login.html creado
- [ ] Redirecciones configuradas en settings.py
- [ ] CSRF protection habilitada

### PR #3: Forms
- [ ] CalificacionForm creado
- [ ] Campo promedio excluido
- [ ] Validaciones de notas (0.00 - 5.00)
- [ ] Widgets con Bootstrap
- [ ] Placeholders y labels descriptivos
- [ ] Mensajes de error claros

### PR #4: Views
- [ ] lista_calificaciones() implementada
- [ ] crear_calificacion() implementada
- [ ] editar_calificacion() implementada
- [ ] eliminar_calificacion() implementada
- [ ] @login_required en todas las vistas
- [ ] get_object_or_404 para seguridad
- [ ] Redirecciones correctas

### PR #5: Templates
- [ ] registration/login.html creado
- [ ] calificaciones_heidy/lista.html creado
- [ ] calificaciones_heidy/formulario.html creado
- [ ] calificaciones_heidy/confirmar_eliminar.html creado
- [ ] Diseño responsive
- [ ] Tema verde consistente
- [ ] CSRF tokens en formularios

### PR #6: Configuration (dev → master)
- [ ] settings.py bien documentado
- [ ] .gitignore completo
- [ ] requirements.txt actualizado
- [ ] Todas las apps registradas
- [ ] Redirecciones configuradas
- [ ] Todos los PRs de features mergeados

---

## 🔐 Protección de ramas (recomendado)

Para proteger `master` y `dev`, configura en GitHub:

1. Ve a: Settings → Branches
2. Haz clic en "Add rule"
3. Para `master`:
   - Require pull request reviews before merging: ✅
   - Require status checks to pass: ✅
   - Require branches to be up to date: ✅
   - Dismiss stale pull request approvals: ✅
   - Require code owner reviews: ✅

4. Para `dev`:
   - Require pull request reviews before merging: ✅
   - Require status checks to pass: ✅

---

## 📝 Convenciones de commits

Todos los commits siguen el formato Conventional Commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Tipos de commits

- `feat` — nueva característica
- `fix` — corrección de bug
- `docs` — cambios en documentación
- `style` — cambios de formato (sin cambios de lógica)
- `refactor` — refactorización de código
- `perf` — mejoras de rendimiento
- `test` — adición o modificación de tests
- `chore` — tareas de mantenimiento

### Ejemplos

```
feat(models): Implement Calificacion model with automatic promedio calculation

- Add Calificacion model with required fields
- Implement calcular_promedio() function
- Override save() method for automatic calculation

Closes #123
```

---

## 🚀 Comandos útiles

### Ver estado de ramas

```bash
# Ver todas las ramas
git branch -a

# Ver ramas remotas
git branch -r

# Ver ramas locales
git branch -l
```

### Ver commits

```bash
# Ver commits en una rama
git log feature/models

# Ver commits entre dos ramas
git log dev..feature/models

# Ver árbol de commits
git log --oneline --all --graph
```

### Sincronizar ramas

```bash
# Actualizar dev desde master
git checkout dev
git pull origin master

# Actualizar feature desde dev
git checkout feature/models
git rebase dev
git push -f origin feature/models
```

### Limpiar ramas locales

```bash
# Eliminar rama local
git branch -d feature/models

# Eliminar rama remota
git push origin --delete feature/models

# Limpiar referencias a ramas eliminadas
git fetch --prune
```

---

## 📞 Soporte

Si tienes problemas:

1. Verifica que GitHub CLI esté instalado: `gh --version`
2. Verifica que estés autenticado: `gh auth status`
3. Verifica que estés en la rama correcta: `git branch`
4. Verifica que los cambios estén pusheados: `git push origin [rama]`

---

## 📚 Referencias

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Git Documentation](https://git-scm.com/doc)

