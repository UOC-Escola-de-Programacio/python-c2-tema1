"""
Tests para el ejercicio ej1e3 (carpeta ej1e3/).
Comprueba que la página de instalación contiene bloques de código y
admonitions, y que las funciones Python de análisis funcionan
correctamente.
"""

import os
import re

from ej1e3 import admonitions, bloques_de_codigo, comando_de_instalacion

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1e3")


def load_content():
    path = os.path.join(EJ_DIR, "instalacion.rst")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_bash_code_block():
    content = load_content()
    assert re.search(r"(?m)^\.\.\s*code-block::\s*bash\s*$", content), (
        "Falta un bloque '.. code-block:: bash' con el comando de instalación"
    )


def test_has_python_code_block():
    content = load_content()
    assert re.search(r"(?m)^\.\.\s*code-block::\s*python\s*$", content), (
        "Falta un bloque '.. code-block:: python' con un script de ejemplo"
    )


def test_has_note_and_warning_admonitions():
    content = load_content()
    assert re.search(r"(?m)^\.\.\s*note::", content), (
        "Falta una admonition '.. note::'"
    )
    assert re.search(r"(?m)^\.\.\s*warning::", content), (
        "Falta una admonition '.. warning::'"
    )


def test_bloques_de_codigo():
    bloques = bloques_de_codigo()
    assert isinstance(bloques, list)
    langs = [lang for lang, _ in bloques]
    assert "bash" in langs and "python" in langs


def test_comando_de_instalacion():
    comando = comando_de_instalacion()
    assert comando is not None
    assert "pip install" in comando


def test_admonitions():
    result = admonitions()
    assert isinstance(result, dict)
    assert "note" in result and result["note"].strip()
    assert "warning" in result and result["warning"].strip()
    assert not result["note"].startswith(" ")
