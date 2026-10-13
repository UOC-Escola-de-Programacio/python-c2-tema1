# Ejercicio ej1f1: tema Read the Docs + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`conf.py`, `requirements.txt`)**: añadir la
   dependencia `sphinx-rtd-theme` y cambiar `html_theme` a
   `sphinx_rtd_theme`.
2. **Python (`__init__.py`)**: implementar `tema_configurado` y
   `dependencias`, que leen esos dos archivos.

## Por qué una carpeta

El ejercicio combina configuración y requisitos con el código Python que
los analiza, así que se agrupan en `ej1f1/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1f1`.

## Cómo probar tu solución

Desde la carpeta `1f/`:

```bash
python -m pytest ej1f1_test.py -v
```
