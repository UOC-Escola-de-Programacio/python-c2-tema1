# Ejercicio ej1c1: mini-proyecto "biblioteca"

## 📝 Enunciado

Este ejercicio consiste en completar un pequeño paquete de Python que
modela una biblioteca (una colección de libros), documentándolo
completamente con docstrings en formato **Google**. Esta documentación es
la que se usará más adelante (ejercicios `ej1c2` y `ej1c3`) para generar
automáticamente la referencia de la API con `mkdocstrings`.

A diferencia de otros ejercicios del tema, este se organiza en una carpeta
(`1c/ej1c1/`) con varios ficheros, porque es un mini-proyecto en forma de
**paquete de Python** y no un único script:

```
ej1c1/
├── __init__.py      # Punto de entrada del paquete: expone su API pública
│                      y la función "cargar_libros_iniciales".
├── libro.py         # Clase "Libro".
├── coleccion.py     # Clase "ColeccionLibros".
└── excepciones.py   # Excepción "LibroNoEncontradoError".
```

### Tu tarea

1. **`excepciones.py`**: completa el docstring de la excepción
   `LibroNoEncontradoError`.
2. **`libro.py`**: completa la clase `Libro` (atributos, `prestar()`,
   `devolver()`, `__repr__` y `__eq__`), con sus docstrings en formato
   Google.
3. **`coleccion.py`**: completa la clase `ColeccionLibros` (añadir libros,
   buscar por ISBN/autor, prestar, listar disponibles y `__len__`), con
   sus docstrings en formato Google.
4. **`__init__.py`**: importa las clases y la excepción anteriores (con
   imports relativos, p. ej. `from .libro import Libro`), completa
   `__all__`, y completa la función `cargar_libros_iniciales()`.

### ¿Por qué el código vive en `__init__.py`?

Cuando un ejercicio de Python necesita más de un fichero, en lugar de un
único script suelto se organiza como un **paquete** (una carpeta con un
`__init__.py`). El `__init__.py` es el punto de entrada del paquete: es el
fichero que se ejecuta al hacer `import ej1c1`, y por eso es el lugar
natural para exponer la API pública del paquete (qué clases y funciones
están disponibles desde fuera) y para implementar la lógica de "entrada"
del mini-proyecto.

## ✅ Cómo comprobar tu solución

Los tests de este ejercicio se encuentran en `1c/ej1c1_test.py`. Ejecuta,
desde la raíz del repositorio:

```bash
pytest 1c/ej1c1_test.py
```
