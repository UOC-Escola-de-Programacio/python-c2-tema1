# Ejercicio ej1c3: referencia de la API + análisis en Python

Este ejercicio combina dos tareas:

1. **Redacción (`api.md`)**: añadir las directivas de mkdocstrings
   `::: ej1c1.libro` y `::: ej1c1.coleccion`.
2. **Python (`__init__.py`)**: implementar `modulos_referenciados`, que
   extrae esas directivas con expresiones regulares.

## Por qué una carpeta

El ejercicio combina una página Markdown con el código Python que la
analiza, así que ambos se agrupan en `ej1c3/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1c3`.

## Cómo probar tu solución

Desde la carpeta `1c/`:

```bash
python -m pytest ej1c3_test.py -v
```
