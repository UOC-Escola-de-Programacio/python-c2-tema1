"""
Tests para el ejercicio ej1e2 (carpeta ej1e2/).
Comprueba que la página contiene un título, una lista y referencias
cruzadas internas, y que las funciones Python de análisis funcionan
correctamente.
"""

import os
import re

from ej1e2 import elementos_de_lista, referencias_cruzadas, titulo_principal

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1e2")


def load_content():
    path = os.path.join(EJ_DIR, "overview.rst")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_title():
    content = load_content()
    match = re.search(r"(?m)^(\S.*)\n=+\s*$", content)
    assert match, "La página debe incluir un título seguido de una línea de '='"
    assert "TODO" not in match.group(1), (
        "Sustituye el título de ejemplo por el título real del proyecto"
    )


def test_has_list_with_at_least_three_items():
    content = load_content()
    items = re.findall(r"(?m)^-\s+\S.*$", content)
    assert len(items) >= 3, "La página debe incluir una lista con al menos 3 elementos"


def test_has_cross_references():
    content = load_content()
    refs = re.findall(r":doc:`(?:[^<`]*<([^>`]+)>|([^`]+))`", content)
    targets = [a or b for a, b in refs]
    assert any("instalacion" in t for t in targets), (
        "Falta una referencia cruzada (:doc:) a 'instalacion'"
    )
    assert any("api" in t for t in targets), (
        "Falta una referencia cruzada (:doc:) a 'api'"
    )


def test_titulo_principal():
    content = load_content()
    match = re.search(r"(?m)^(\S.*)\n=+\s*$", content)
    assert titulo_principal() == match.group(1).strip()


def test_elementos_de_lista_count():
    elementos = elementos_de_lista()
    assert isinstance(elementos, list)
    assert len(elementos) >= 3
    assert all(not item.lstrip().startswith("-") for item in elementos)


def test_referencias_cruzadas():
    refs = referencias_cruzadas()
    assert any("instalacion" in r for r in refs)
    assert any("api" in r for r in refs)
