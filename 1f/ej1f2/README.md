# Ejercicio ej1f2: opciones del tema + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`conf.py`)**: añadir la clave `html_theme_options`
   con `logo_only: True` y `navigation_depth: 4`.
2. **Python (`__init__.py`)**: implementar `opciones_del_tema`, que lee
   esa configuración.

## Por qué una carpeta

El ejercicio combina configuración con el código Python que la analiza,
así que ambos se agrupan en `ej1f2/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1f2`.

## Cómo probar tu solución

Desde la carpeta `1f/`:

```bash
python -m pytest ej1f2_test.py -v
```
