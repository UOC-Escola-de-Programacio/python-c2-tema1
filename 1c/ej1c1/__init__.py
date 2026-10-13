"""
Enunciado:
Escritura de funciones en Python documentadas mediante docstrings
estructurados en formato Google.

En este ejercicio vas a construir una pequeña librería en forma de paquete
de Python ("ej1c1/", el propio directorio donde se encuentra este
archivo), con sus propias clases, y la documentarás completamente usando
docstrings en formato Google. Esta documentación es la que luego se usará,
en los ejercicios "ej1c2" y "ej1c3", para generar automáticamente la
referencia de la API con "mkdocstrings".

El paquete contiene los siguientes módulos, que deberás completar:

- "excepciones.py": una excepción personalizada "LibroNoEncontradoError".
- "libro.py": la clase "Libro", que representa un libro físico.
- "coleccion.py": la clase "ColeccionLibros", que gestiona una colección de
  objetos "Libro".

Tu tarea en este archivo ("__init__.py"), que actúa a la vez como punto de
entrada del paquete y como fichero que expone su API pública, es:

1. Importar "Libro", "ColeccionLibros" y "LibroNoEncontradoError" desde sus
   respectivos módulos (import relativo, p. ej. "from .libro import
   Libro").
2. Completar la lista "__all__" con esos tres nombres.
3. Completar la función "cargar_libros_iniciales" para que devuelva una
   "ColeccionLibros" con 3 libros de ejemplo ya añadidos, documentándola
   con un docstring en formato Google (con una sección "Returns:").
"""

# TODO: importa "Libro" desde ".libro" (import relativo).
# TODO: importa "ColeccionLibros" desde ".coleccion" (import relativo).
# TODO: importa "LibroNoEncontradoError" desde ".excepciones" (import
# relativo).

# TODO: completa "__all__" con los nombres de las clases/excepciones
# importadas anteriormente, además de "cargar_libros_iniciales".
__all__ = []


def cargar_libros_iniciales():
    """
    TODO: completa este docstring en formato Google.
    Debe describir la función y documentar el valor devuelto en una
    sección "Returns:".
    """
    # TODO: crea una "ColeccionLibros" llamada, por ejemplo, "Mi biblioteca"
    # y añádele 3 objetos "Libro" de ejemplo (con título, autor, año e
    # ISBN distintos). Devuelve la colección resultante.
    pass


if __name__ == "__main__":
    coleccion = cargar_libros_iniciales()
    print(f"Colección: {coleccion.nombre} ({len(coleccion)} libros)")
    for libro in coleccion.listar_disponibles():
        print(f" - {libro}")
