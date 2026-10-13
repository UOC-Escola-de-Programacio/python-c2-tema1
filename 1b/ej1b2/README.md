# Ejercicio ej1b2: paleta de colores + análisis en Python

Este ejercicio combina dos tareas:

1. **Configuración (`mkdocs.yml`)**: añadir la clave `palette` (con
   `primary` y `accent`) y la funcionalidad `navigation.tabs` en
   `features`.
2. **Python (`__init__.py`)**: implementar `paleta_de_colores` y
   `funcionalidades_activadas`, que leen esa configuración.

## Por qué una carpeta

El ejercicio combina configuración con el código Python que la analiza,
así que ambos se agrupan en `ej1b2/`. El código se escribe en
`__init__.py`, el archivo que se importa con `import ej1b2`.

## Cómo probar tu solución

Desde la carpeta `1b/`:

```bash
python -m pytest ej1b2_test.py -v
```
