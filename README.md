# Tema 1. Documentación de proyectos con MkDocs y Sphinx

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás tener configurado tu entorno de python.

### Librerias

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

```bash
pip install -r requirements.txt
```

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciados

Todos los ejercicios de este tema tienen una parte en Markdown/RST y/o YAML (redactar una página, completar una configuración...) **y** una parte en Python: cada ejercicio se organiza en su propia carpeta (por ejemplo `1a/ej1a1/`, `1c/ej1c1/`) que contiene tanto el archivo de contenido/configuración como un módulo `__init__.py` con funciones que debes completar y que trabajan sobre ese contenido. El enunciado completo se encuentra repartido entre el `README.md` de la carpeta y los comentarios/docstrings del propio `__init__.py`. Algunos ejercicios, por ser mini-proyectos en forma de paquete de Python con varios módulos (por ejemplo `1c/ej1c1/`, `1c/ej1c4/` o `1g/ej1g1/`), incluyen además módulos adicionales junto al `__init__.py`.

El tema se divide en dos partes que cubren las dos herramientas de documentación más usadas en Python:

- **MkDocs** (apartados a, b y c): redacción en Markdown, personalización con el tema Material, y documentación automática de la API con `mkdocstrings`.
- **Sphinx** (apartados e, f y g): redacción en reStructuredText (RST), personalización con el tema Read the Docs, y documentación automática de la API con `sphinx.ext.autodoc`/`napoleon`. Es una adaptación directa de los apartados a, b y c, pero usando Sphinx y docstrings en formato reST en lugar de Google.

El archivo de tests de cada ejercicio (`ejXaY_test.py`) se encuentra en la carpeta del apartado (`1a/`, `1b/`...), al mismo nivel que la carpeta del ejercicio.

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios |
| -------- | ---------- |
| a. Redacción y estructuración en Markdown (MkDocs) | [ej1a1](1a/ej1a1/) [ej1a2](1a/ej1a2/) [ej1a3](1a/ej1a3/) [ej1a4](1a/ej1a4/) |
| b. Personalización con Material for MkDocs | [ej1b1](1b/ej1b1/) [ej1b2](1b/ej1b2/) |
| c. Documentación automatizada con mkdocstrings | [ej1c1](1c/ej1c1/) [ej1c2](1c/ej1c2/) [ej1c3](1c/ej1c3/) [ej1c4](1c/ej1c4/) |
| e. Redacción y estructuración en reStructuredText (Sphinx) | [ej1e1](1e/ej1e1/) [ej1e2](1e/ej1e2/) [ej1e3](1e/ej1e3/) |
| f. Personalización con el tema Read the Docs | [ej1f1](1f/ej1f1/) [ej1f2](1f/ej1f2/) |
| g. Documentación automatizada con Sphinx autodoc | [ej1g1](1g/ej1g1/) [ej1g2](1g/ej1g2/) [ej1g3](1g/ej1g3/) |

> Nota: el ejercicio [ej1a1](1a/ej1a1/) incluye, además de la configuración del menú `nav`, la construcción en Python del comando `mkdocs serve` para previsualizar la documentación localmente.

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta.

Cuando hayas propuesto una implementación, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor.

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos

En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad.

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest
```
```bash
python -m pip install -r requirements.txt
```
Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.

### MkDocs

Para levantar un servidor local de previsualización de la documentación:
```bash
mkdocs serve
```

Para generar los archivos estáticos finales:
```bash
mkdocs build
```

### Sphinx

Para generar los archivos estáticos finales a partir de un proyecto Sphinx (ejecutado desde la carpeta que contiene `conf.py`):
```bash
sphinx-build -b html . _build
```
