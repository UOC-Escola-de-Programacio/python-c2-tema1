"""
Tests para el ejercicio ej1g3 (carpeta ej1g3/).
Comprueba que la página de referencia de la API incluye las directivas
"automodule" para los módulos "ej1g1.contacto" y "ej1g1.agenda", y la
función Python asociada.
"""

import os
import re

from ej1g3 import modulos_referenciados

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1g3")


def load_content():
    path = os.path.join(EJ_DIR, "api.rst")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_automodule_directive_for_contacto():
    content = load_content()
    assert re.search(r"(?m)^\.\.\s*automodule::\s*ej1g1\.contacto\s*$", content), (
        "Falta la directiva '.. automodule:: ej1g1.contacto'"
    )


def test_has_automodule_directive_for_agenda():
    content = load_content()
    assert re.search(r"(?m)^\.\.\s*automodule::\s*ej1g1\.agenda\s*$", content), (
        "Falta la directiva '.. automodule:: ej1g1.agenda'"
    )


def test_automodule_directives_use_members_option():
    content = load_content()
    assert content.count(":members:") >= 2, (
        "Cada directiva 'automodule' debe incluir la opción ':members:'"
    )


def test_has_title():
    content = load_content()
    assert re.search(r"(?m)^(\S.*)\n=+\s*$", content), (
        "La página debe incluir un título de nivel 1"
    )


def test_modulos_referenciados():
    modulos = modulos_referenciados()
    assert "ej1g1.contacto" in modulos
    assert "ej1g1.agenda" in modulos
