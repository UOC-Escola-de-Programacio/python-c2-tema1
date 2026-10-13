# Ejercicio ej1e3: bloques de código y admonitions en RST

Este ejercicio combina dos tareas:

1. **Redacción (`instalacion.rst`)**: añadir bloques `.. code-block::`
   para `bash` (con un comando `pip install`) y `python`, y admonitions
   `.. note::` y `.. warning::`.
2. **Python (`__init__.py`)**: implementar `bloques_de_codigo`,
   `comando_de_instalacion` y `admonitions`, que extraen esa información
   con expresiones regulares.

## Por qué una carpeta

El ejercicio combina una página RST con el código Python que la analiza,
así que ambos se agrupan en `ej1e3/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1e3`.

## Cómo probar tu solución

Desde la carpeta `1e/`:

```bash
python -m pytest ej1e3_test.py -v
```
