"""
TODO: completa el docstring de este módulo.
Debe indicar brevemente que este módulo define la clase "Contacto", que
representa un contacto de una agenda telefónica.
"""


class Contacto:
    """
    TODO: completa este docstring en formato reST (estilo Sphinx).
    Debe describir la clase y documentar sus atributos usando los campos
    ":ivar nombre:", ":ivar telefono:" y ":ivar favorito:".
    """

    def __init__(self, nombre, telefono):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe documentar los parámetros "nombre" y "telefono" usando los
        campos ":param nombre:", ":type nombre:", ":param telefono:" y
        ":type telefono:".
        """
        # TODO: guarda "nombre" y "telefono" como atributos.
        # TODO: inicializa un atributo "favorito" a False.
        pass

    def marcar_como_favorito(self):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe describir que marca el contacto como favorito, documentando
        en un campo ":return:" y ":rtype:" que no devuelve ningún valor
        (devuelve "None").
        """
        # TODO: establece el atributo "favorito" a True.
        pass

    def __repr__(self):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe describir que devuelve una representación en texto del
        contacto, incluyendo como mínimo el nombre y el teléfono,
        documentando el valor devuelto con ":return:" y ":rtype:".
        """
        # TODO: devuelve un string con, por ejemplo, el formato:
        # "<nombre> (<telefono>)"
        pass

    def __eq__(self, other):
        """
        TODO: completa este docstring en formato reST (estilo Sphinx).
        Debe describir que dos contactos se consideran iguales si tienen
        el mismo teléfono, documentando el parámetro "other" con
        ":param other:"/":type other:" y el valor devuelto con
        ":return:"/":rtype:".
        """
        # TODO: si "other" no es una instancia de "Contacto", devuelve
        # "NotImplemented".
        # TODO: en caso contrario, devuelve True si ambos teléfonos
        # coinciden.
        pass
