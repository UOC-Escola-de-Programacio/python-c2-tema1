# Ejercicio ej1a2: página principal + análisis en Python

Este ejercicio combina dos tareas:

1. **Redacción (`index.md`)**: escribir la página principal de la
   documentación con un título de nivel 1, una lista de al menos 3
   elementos y enlaces internos a `instalacion.md` y `api.md`.
2. **Python (`__init__.py`)**: implementar tres funciones que analizan
   `index.md` con expresiones regulares:
   - `titulo_principal`
   - `elementos_de_lista`
   - `enlaces_internos`

## Por qué una carpeta

El ejercicio combina una página Markdown con el código Python que la
analiza, así que ambos archivos se agrupan en `ej1a2/`. El código se
escribe en `__init__.py`, el archivo que se importa con `import ej1a2`.

## Cómo probar tu solución

Desde la carpeta `1a/`:

```bash
python -m pytest ej1a2_test.py -v
```
