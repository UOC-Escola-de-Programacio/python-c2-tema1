"""
Tests para el mini-proyecto "biblioteca" (ej1c1).
Comprueban el comportamiento de las clases "Libro" y "ColeccionLibros", la
función de entrada "cargar_libros_iniciales", y la presencia de docstrings
en formato Google (secciones "Args:", "Returns:" y, cuando corresponda,
"Raises:") en las clases y métodos del paquete.
"""

import pytest

from ej1c1 import cargar_libros_iniciales
from ej1c1.coleccion import ColeccionLibros
from ej1c1.excepciones import LibroNoEncontradoError
from ej1c1.libro import Libro


# --- Comportamiento de "Libro" -------------------------------------------------


def test_libro_se_crea_disponible():
    libro = Libro("Dune", "Frank Herbert", 1965, "0001")
    assert libro.titulo == "Dune"
    assert libro.autor == "Frank Herbert"
    assert libro.anio == 1965
    assert libro.isbn == "0001"
    assert libro.prestado is False


def test_libro_prestar_y_devolver():
    libro = Libro("Dune", "Frank Herbert", 1965, "0001")
    assert libro.prestar() is True
    assert libro.prestado is True
    assert libro.prestar() is False, "No se debería poder prestar dos veces"
    libro.devolver()
    assert libro.prestado is False


def test_libro_repr_incluye_titulo_y_autor():
    libro = Libro("Dune", "Frank Herbert", 1965, "0001")
    texto = repr(libro)
    assert "Dune" in texto
    assert "Frank Herbert" in texto


def test_libro_igualdad_por_isbn():
    libro1 = Libro("Dune", "Frank Herbert", 1965, "0001")
    libro2 = Libro("Dune (reedición)", "F. Herbert", 2000, "0001")
    libro3 = Libro("Otro libro", "Otro autor", 1999, "0002")
    assert libro1 == libro2
    assert libro1 != libro3


# --- Comportamiento de "ColeccionLibros" ---------------------------------------


@pytest.fixture
def coleccion_con_libros():
    coleccion = ColeccionLibros("Biblioteca de pruebas")
    coleccion.añadir_libro(Libro("Dune", "Frank Herbert", 1965, "0001"))
    coleccion.añadir_libro(Libro("Fundación", "Isaac Asimov", 1951, "0002"))
    coleccion.añadir_libro(Libro("Los robots", "Isaac Asimov", 1950, "0003"))
    return coleccion


def test_coleccion_len(coleccion_con_libros):
    assert len(coleccion_con_libros) == 3


def test_coleccion_buscar_por_isbn(coleccion_con_libros):
    libro = coleccion_con_libros.buscar_por_isbn("0002")
    assert libro.titulo == "Fundación"


def test_coleccion_buscar_por_isbn_inexistente(coleccion_con_libros):
    with pytest.raises(LibroNoEncontradoError):
        coleccion_con_libros.buscar_por_isbn("9999")


def test_coleccion_buscar_por_autor(coleccion_con_libros):
    libros = coleccion_con_libros.buscar_por_autor("Isaac Asimov")
    assert {libro.isbn for libro in libros} == {"0002", "0003"}


def test_coleccion_prestar_libro(coleccion_con_libros):
    assert coleccion_con_libros.prestar_libro("0001") is True
    assert coleccion_con_libros.buscar_por_isbn("0001").prestado is True
    assert coleccion_con_libros.prestar_libro("0001") is False


def test_coleccion_prestar_libro_inexistente(coleccion_con_libros):
    with pytest.raises(LibroNoEncontradoError):
        coleccion_con_libros.prestar_libro("9999")


def test_coleccion_listar_disponibles(coleccion_con_libros):
    coleccion_con_libros.prestar_libro("0001")
    disponibles = coleccion_con_libros.listar_disponibles()
    assert {libro.isbn for libro in disponibles} == {"0002", "0003"}


# --- Punto de entrada "ej1c1.py" -----------------------------------------------


def test_cargar_libros_iniciales():
    coleccion = cargar_libros_iniciales()
    assert isinstance(coleccion, ColeccionLibros)
    assert len(coleccion) == 3


# --- Documentación (docstrings en formato Google) ------------------------------


def assert_google_docstring(obj, sections=("Args:", "Returns:")):
    doc = obj.__doc__ or ""
    for section in sections:
        assert section in doc, (
            f"El docstring de '{getattr(obj, '__name__', obj)}' debe incluir "
            f"la sección '{section}'"
        )


def test_libro_class_and_methods_have_google_docstrings():
    assert_google_docstring(Libro, sections=("Attributes:",))
    assert_google_docstring(Libro.__init__, sections=("Args:",))
    assert_google_docstring(Libro.prestar, sections=("Returns:",))


def test_libro_devolver_has_docstring():
    doc = Libro.devolver.__doc__ or ""
    assert doc.strip(), "El método 'devolver' debe tener un docstring"


def test_libro_eq_has_google_docstring():
    assert_google_docstring(Libro.__eq__, sections=("Args:", "Returns:"))


def test_coleccion_class_and_methods_have_google_docstrings():
    assert_google_docstring(ColeccionLibros, sections=("Attributes:",))
    assert_google_docstring(ColeccionLibros.__init__, sections=("Args:",))
    assert_google_docstring(ColeccionLibros.añadir_libro, sections=("Args:",))
    assert_google_docstring(
        ColeccionLibros.buscar_por_isbn, sections=("Args:", "Returns:", "Raises:")
    )
    assert_google_docstring(
        ColeccionLibros.buscar_por_autor, sections=("Args:", "Returns:")
    )
    assert_google_docstring(
        ColeccionLibros.prestar_libro, sections=("Args:", "Returns:", "Raises:")
    )
    assert_google_docstring(ColeccionLibros.listar_disponibles, sections=("Returns:",))
    assert_google_docstring(ColeccionLibros.__len__, sections=("Returns:",))


def test_cargar_libros_iniciales_has_google_docstring():
    assert_google_docstring(cargar_libros_iniciales, sections=("Returns:",))
