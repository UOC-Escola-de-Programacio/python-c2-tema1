"""
Tests para el ejercicio ej1a4 (carpeta ej1a4/).
Comprueba que la página contiene admonitions de tipo "note" y "warning", y
que la función Python de análisis funciona correctamente.
"""

import os
import re

from ej1a4 import admonitions

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1a4")


def load_content():
    path = os.path.join(EJ_DIR, "notas.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_note_admonition():
    content = load_content()
    assert re.search(r"(?m)^!!!\s+note", content), (
        "Falta una admonition de tipo 'note' (!!! note)"
    )


def test_has_warning_admonition():
    content = load_content()
    assert re.search(r"(?m)^!!!\s+warning", content), (
        "Falta una admonition de tipo 'warning' (!!! warning)"
    )


def test_admonitions_have_content():
    content = load_content()
    for admonition in ("note", "warning"):
        match = re.search(
            rf"(?m)^!!!\s+{admonition}.*\n((?:[ \t]+.+\n?)+)", content
        )
        assert match and match.group(1).strip(), (
            f"La admonition '{admonition}' debe tener contenido indentado"
        )


def test_admonitions_function():
    result = admonitions()
    assert isinstance(result, dict)
    assert "note" in result and result["note"].strip()
    assert "warning" in result and result["warning"].strip()
    assert not result["note"].startswith(" ")
