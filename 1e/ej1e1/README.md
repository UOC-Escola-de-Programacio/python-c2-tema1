# Ejercicio ej1e1: proyecto Sphinx (`conf.py`) + índice (`index.rst`)

Este ejercicio combina dos tareas:

1. **Configuración (`conf.py`, `index.rst`)**: completar las variables
   `project` y `author` de la configuración de Sphinx, y el bloque
   `.. toctree::` del índice principal con las páginas `instalacion`,
   `api` y `despliegue`, en ese orden.
2. **Python (`__init__.py`)**: implementar `info_proyecto` y
   `paginas_del_indice`, que leen esos dos archivos.

## Por qué una carpeta

El ejercicio combina la configuración de Sphinx con el código Python que
la analiza, así que se agrupan en `ej1e1/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1e1`.

## Cómo probar tu solución

Desde la carpeta `1e/`:

```bash
python -m pytest ej1e1_test.py -v
```
