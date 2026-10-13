# Ejercicio ej1e2: página con títulos, listas y referencias cruzadas (RST)

Este ejercicio combina dos tareas:

1. **Redacción (`overview.rst`)**: escribir una página en RST con un
   título de nivel 1, una lista de al menos 3 elementos y referencias
   cruzadas internas (`:doc:`) a `instalacion` y `api`.
2. **Python (`__init__.py`)**: implementar `titulo_principal`,
   `elementos_de_lista` y `referencias_cruzadas`, que analizan
   `overview.rst` con expresiones regulares.

## Por qué una carpeta

El ejercicio combina una página RST con el código Python que la analiza,
así que ambos se agrupan en `ej1e2/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1e2`.

## Cómo probar tu solución

Desde la carpeta `1e/`:

```bash
python -m pytest ej1e2_test.py -v
```
