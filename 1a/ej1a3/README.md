# Ejercicio ej1a3: bloques de código + análisis en Python

Este ejercicio combina dos tareas:

1. **Redacción (`instalacion.md`)**: añadir un bloque de código `bash` con
   el comando de instalación (`pip install ...`) y un bloque `python` con
   un pequeño script de ejemplo.
2. **Python (`__init__.py`)**: implementar `bloques_de_codigo` y
   `comando_de_instalacion`, que extraen esa información con expresiones
   regulares.

## Por qué una carpeta

El ejercicio combina una página Markdown con el código Python que la
analiza, así que ambos archivos se agrupan en `ej1a3/`. El código se
escribe en `__init__.py`, el archivo que se importa con `import ej1a3`.

## Cómo probar tu solución

Desde la carpeta `1a/`:

```bash
python -m pytest ej1a3_test.py -v
```
