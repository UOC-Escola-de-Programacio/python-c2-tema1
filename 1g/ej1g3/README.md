# Ejercicio ej1g3: referencia de la API + análisis en Python

Este ejercicio combina dos tareas:

1. **Redacción (`api.rst`)**: añadir las directivas `.. automodule::
   ej1g1.contacto` y `.. automodule:: ej1g1.agenda`, ambas con
   `:members:`.
2. **Python (`__init__.py`)**: implementar `modulos_referenciados`, que
   extrae esas directivas con expresiones regulares.

## Por qué una carpeta

El ejercicio combina una página RST con el código Python que la analiza,
así que ambos se agrupan en `ej1g3/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1g3`.

## Cómo probar tu solución

Desde la carpeta `1g/`:

```bash
python -m pytest ej1g3_test.py -v
```
