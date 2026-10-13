"""
TODO: completa el docstring de este módulo.
Debe indicar brevemente que este módulo define la clase "Agenda", que
representa una colección de contactos ("Contacto").
"""

from .excepciones import ContactoNoEncontradoError


class Agenda:
    """
    TODO: completa este docstring en formato reST (estilo Sphinx).
    Debe describir la clase y documentar sus atributos usando los campos
    ":ivar nombre:" y ":ivar contactos:".
    """

    def __init__(self, nombre):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar el parámetro "nombre" usando ":param nombre:" y
        ":type nombre:".
        """
        # TODO: guarda "nombre" como atributo.
        # TODO: inicializa un atributo "contactos" como una lista vacía.
        pass

    def añadir_contacto(self, contacto):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar el parámetro "contacto" usando ":param contacto:"
        y ":type contacto:".
        """
        # TODO: añade "contacto" a la lista de contactos.
        pass

    def buscar_por_telefono(self, telefono):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar el parámetro "telefono" (":param telefono:",
        ":type telefono:"), el valor devuelto (":return:", ":rtype:") y
        la excepción que puede lanzar (":raises ContactoNoEncontradoError:").
        """
        # TODO: busca y devuelve el contacto con ese teléfono.
        # TODO: si no se encuentra, lanza "ContactoNoEncontradoError".
        pass

    def buscar_favoritos(self):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar el valor devuelto usando ":return:" y ":rtype:".
        """
        # TODO: devuelve la lista de contactos marcados como favoritos.
        pass

    def __len__(self):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar el valor devuelto usando ":return:" y ":rtype:".
        """
        # TODO: devuelve el número de contactos de la agenda.
        pass
