# Ejercicio ej1a4: admonitions + análisis en Python

Este ejercicio combina dos tareas:

1. **Redacción (`notas.md`)**: añadir una admonition `!!! note` y otra
   `!!! warning`, cada una con contenido indentado.
2. **Python (`__init__.py`)**: implementar `admonitions`, que extrae el
   tipo y el contenido de cada admonition con expresiones regulares.

## Por qué una carpeta

El ejercicio combina una página Markdown con el código Python que la
analiza, así que ambos archivos se agrupan en `ej1a4/`. El código se
escribe en `__init__.py`, el archivo que se importa con `import ej1a4`.

## Cómo probar tu solución

Desde la carpeta `1a/`:

```bash
python -m pytest ej1a4_test.py -v
```
