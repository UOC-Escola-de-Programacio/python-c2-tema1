"""
Tests para el mini-proyecto "agenda" (ej1g1).
Comprueban el comportamiento de las clases "Contacto" y "Agenda", la
función de entrada "cargar_agenda_inicial", y la presencia de docstrings
en formato reST (estilo Sphinx: campos ":param:", ":type:", ":return:",
":rtype:" y, cuando corresponda, ":raises:") en las clases y métodos del
paquete.
"""

import pytest

from ej1g1 import cargar_agenda_inicial
from ej1g1.agenda import Agenda
from ej1g1.contacto import Contacto
from ej1g1.excepciones import ContactoNoEncontradoError


# --- Comportamiento de "Contacto" ----------------------------------------------


def test_contacto_se_crea_no_favorito():
    contacto = Contacto("Ana", "600111222")
    assert contacto.nombre == "Ana"
    assert contacto.telefono == "600111222"
    assert contacto.favorito is False


def test_contacto_marcar_como_favorito():
    contacto = Contacto("Ana", "600111222")
    contacto.marcar_como_favorito()
    assert contacto.favorito is True


def test_contacto_repr_incluye_nombre_y_telefono():
    contacto = Contacto("Ana", "600111222")
    texto = repr(contacto)
    assert "Ana" in texto
    assert "600111222" in texto


def test_contacto_igualdad_por_telefono():
    contacto1 = Contacto("Ana", "600111222")
    contacto2 = Contacto("Ana García", "600111222")
    contacto3 = Contacto("Otro", "600333444")
    assert contacto1 == contacto2
    assert contacto1 != contacto3


# --- Comportamiento de "Agenda" -------------------------------------------------


@pytest.fixture
def agenda_con_contactos():
    agenda = Agenda("Agenda de pruebas")
    agenda.añadir_contacto(Contacto("Ana", "600111222"))
    agenda.añadir_contacto(Contacto("Bruno", "600333444"))
    agenda.añadir_contacto(Contacto("Carla", "600555666"))
    return agenda


def test_agenda_len(agenda_con_contactos):
    assert len(agenda_con_contactos) == 3


def test_agenda_buscar_por_telefono(agenda_con_contactos):
    contacto = agenda_con_contactos.buscar_por_telefono("600333444")
    assert contacto.nombre == "Bruno"


def test_agenda_buscar_por_telefono_inexistente(agenda_con_contactos):
    with pytest.raises(ContactoNoEncontradoError):
        agenda_con_contactos.buscar_por_telefono("999999999")


def test_agenda_buscar_favoritos(agenda_con_contactos):
    agenda_con_contactos.buscar_por_telefono("600111222").marcar_como_favorito()
    favoritos = agenda_con_contactos.buscar_favoritos()
    assert {c.telefono for c in favoritos} == {"600111222"}


# --- Punto de entrada "ej1g1" ---------------------------------------------------


def test_cargar_agenda_inicial():
    agenda = cargar_agenda_inicial()
    assert isinstance(agenda, Agenda)
    assert len(agenda) >= 3


# --- Documentación (docstrings en formato reST / Sphinx) -----------------------


def assert_rest_docstring(obj, fields=(":param", ":return")):
    doc = obj.__doc__ or ""
    for field in fields:
        assert field in doc, (
            f"El docstring de '{getattr(obj, '__name__', obj)}' debe incluir "
            f"un campo '{field}' (formato reST)"
        )


def test_contacto_class_and_methods_have_rest_docstrings():
    assert_rest_docstring(Contacto.__init__, fields=(":param", ":type"))
    assert_rest_docstring(Contacto.marcar_como_favorito, fields=(":return", ":rtype"))
    assert_rest_docstring(Contacto.__repr__, fields=(":return", ":rtype"))
    assert_rest_docstring(Contacto.__eq__, fields=(":param", ":return"))


def test_agenda_class_and_methods_have_rest_docstrings():
    assert_rest_docstring(Agenda.__init__, fields=(":param", ":type"))
    assert_rest_docstring(Agenda.añadir_contacto, fields=(":param",))
    assert_rest_docstring(
        Agenda.buscar_por_telefono, fields=(":param", ":return", ":raises")
    )
    assert_rest_docstring(Agenda.buscar_favoritos, fields=(":return", ":rtype"))
    assert_rest_docstring(Agenda.__len__, fields=(":return", ":rtype"))


def test_excepcion_has_docstring():
    doc = ContactoNoEncontradoError.__doc__ or ""
    assert doc.strip(), (
        "La excepción 'ContactoNoEncontradoError' debe tener un docstring"
    )


def test_cargar_agenda_inicial_has_rest_docstring():
    assert_rest_docstring(cargar_agenda_inicial, fields=(":return", ":rtype"))
