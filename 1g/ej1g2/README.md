# Ejercicio ej1g2: extensiones autodoc/napoleon + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`conf.py`, `requirements.txt`)**: activar las
   extensiones `sphinx.ext.autodoc` y `sphinx.ext.napoleon`, insertar la
   ruta del paquete `ej1g1` en `sys.path`, y declarar la dependencia
   `sphinx`.
2. **Python (`__init__.py`)**: implementar `extensiones_activadas` y
   `rutas_en_sys_path`, que leen esa configuración.

## Por qué una carpeta

El ejercicio combina configuración y requisitos con el código Python que
los analiza, así que se agrupan en `ej1g2/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1g2`.

## Cómo probar tu solución

Desde la carpeta `1g/`:

```bash
python -m pytest ej1g2_test.py -v
```
