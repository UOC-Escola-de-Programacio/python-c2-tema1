"""
Tests para el ejercicio ej1c3 (carpeta ej1c3/).
Comprueba que la página de referencia de la API incluye las directivas de
mkdocstrings para los módulos "ej1c1.libro" y "ej1c1.coleccion", y la
función Python asociada.
"""

import os
import re

from ej1c3 import modulos_referenciados

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1c3")


def load_content():
    path = os.path.join(EJ_DIR, "api.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_mkdocstrings_directive_for_libro():
    content = load_content()
    assert re.search(r"(?m)^:::\s*ej1c1\.libro\s*$", content), (
        "Falta la directiva '::: ej1c1.libro' de mkdocstrings"
    )


def test_has_mkdocstrings_directive_for_coleccion():
    content = load_content()
    assert re.search(r"(?m)^:::\s*ej1c1\.coleccion\s*$", content), (
        "Falta la directiva '::: ej1c1.coleccion' de mkdocstrings"
    )


def test_has_title():
    content = load_content()
    assert re.search(r"(?m)^#\s+\S", content), (
        "La página debe incluir un título de nivel 1"
    )


def test_modulos_referenciados():
    modulos = modulos_referenciados()
    assert "ej1c1.libro" in modulos
    assert "ej1c1.coleccion" in modulos
