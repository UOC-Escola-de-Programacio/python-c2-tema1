"""
TODO: completa el docstring de este módulo.
Debe indicar brevemente que este módulo define la clase "Libro", que
representa un libro físico de una biblioteca.
"""


class Libro:
    """
    TODO: completa este docstring en formato Google.
    Debe describir la clase y documentar sus atributos en una sección
    "Attributes:" (titulo, autor, anio, isbn y prestado).
    """

    def __init__(self, titulo, autor, anio, isbn):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar los parámetros "titulo", "autor", "anio" e "isbn"
        en una sección "Args:".
        """
        # TODO: guarda "titulo", "autor", "anio" e "isbn" como atributos.
        # TODO: inicializa un atributo "prestado" a False (el libro
        # empieza disponible).
        pass

    def prestar(self):
        """
        TODO: completa este docstring en formato Google.
        Debe describir que marca el libro como prestado, y documentar en
        una sección "Returns:" que devuelve True si se ha podido prestar
        (no estaba ya prestado) y False en caso contrario.
        """
        # TODO: si el libro ya está prestado, devuelve False sin hacer
        # nada más.
        # TODO: si el libro no está prestado, márcalo como prestado
        # (atributo "prestado" a True) y devuelve True.
        pass

    def devolver(self):
        """
        TODO: completa este docstring en formato Google.
        Debe describir que marca el libro como devuelto (disponible de
        nuevo), estableciendo el atributo "prestado" a False.
        """
        # TODO: marca el libro como disponible (atributo "prestado" a
        # False).
        pass

    def __repr__(self):
        """
        TODO: completa este docstring en formato Google.
        Debe describir que devuelve una representación en texto del
        libro, incluyendo como mínimo el título y el autor, en una
        sección "Returns:".
        """
        # TODO: devuelve un string con, por ejemplo, el formato:
        # "'<titulo>' de <autor> (<anio>)"
        pass

    def __eq__(self, other):
        """
        TODO: completa este docstring en formato Google.
        Debe describir que dos libros se consideran iguales si tienen el
        mismo ISBN, documentando el parámetro "other" en una sección
        "Args:" y el valor devuelto en una sección "Returns:".
        """
        # TODO: si "other" no es una instancia de "Libro", devuelve
        # "NotImplemented".
        # TODO: en caso contrario, devuelve True si ambos ISBN coinciden.
        pass
