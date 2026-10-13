# Ejercicio ej1g1: mini-proyecto "agenda" documentado con reST (Sphinx)

Este ejercicio te pide construir una pequeña agenda de contactos como
paquete de Python, igual que en el ejercicio `ej1c1` del bloque de
MkDocs, pero esta vez documentando el código con el formato de docstring
**nativo de Sphinx** (reStructuredText), usando campos como:

```python
def buscar_por_telefono(self, telefono):
    """Busca un contacto por su número de teléfono.

    :param telefono: Teléfono del contacto a buscar.
    :type telefono: str
    :return: El contacto encontrado.
    :rtype: Contacto
    :raises ContactoNoEncontradoError: Si no existe ningún contacto con
        ese teléfono.
    """
```

## Estructura del paquete

- `__init__.py`: punto de entrada del paquete (lo que se ejecuta con
  `python -m ej1g1` o se importa con `import ej1g1`), con la función
  `cargar_agenda_inicial`.
- `contacto.py`: clase `Contacto`.
- `agenda.py`: clase `Agenda` (colección de contactos).
- `excepciones.py`: excepción `ContactoNoEncontradoError`.

## Por qué una carpeta

Este ejercicio es un mini-proyecto con varios módulos, así que se agrupan
en la carpeta `ej1g1/`, con `__init__.py` como punto de entrada.

## Cómo probar tu solución

Desde la carpeta `1g/`:

```bash
python -m pytest ej1g1_test.py -v
```
