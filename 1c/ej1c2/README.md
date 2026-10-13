# Ejercicio ej1c2: plugin mkdocstrings + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`mkdocs.yml`, `requirements.txt`)**: activar los
   plugins `search` y `mkdocstrings`, configurando
   `handlers.python.paths: [src]`, y añadir la dependencia
   `mkdocstrings[python]`.
2. **Python (`__init__.py`)**: implementar `plugins_configurados` y
   `rutas_de_mkdocstrings`, que leen esa configuración.

## Por qué una carpeta

El ejercicio combina configuración y requisitos con el código Python que
los analiza, así que se agrupan en `ej1c2/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1c2`.

## Cómo probar tu solución

Desde la carpeta `1c/`:

```bash
python -m pytest ej1c2_test.py -v
```
