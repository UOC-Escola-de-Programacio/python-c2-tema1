# Ejercicio ej1b1: tema Material + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`mkdocs.yml`, `requirements.txt`)**: añadir la
   dependencia `mkdocs-material` y cambiar el tema a `material`.
2. **Python (`__init__.py`)**: implementar `tema_configurado` y
   `dependencias`, que leen esos dos archivos.

## Por qué una carpeta

El ejercicio combina configuración y requisitos con el código Python que
los analiza, así que se agrupan en `ej1b1/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1b1`.

## Cómo probar tu solución

Desde la carpeta `1b/`:

```bash
python -m pytest ej1b1_test.py -v
```
