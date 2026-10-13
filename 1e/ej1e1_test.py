"""
Tests para el ejercicio ej1e1 (carpeta ej1e1/).
Comprueba que "conf.py" define "project" y "author", que "index.rst"
declara las páginas esperadas en su "toctree", y las funciones Python
asociadas.
"""

import os
import re

from ej1e1 import info_proyecto, paginas_del_indice

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1e1")


def load_conf_text():
    path = os.path.join(EJ_DIR, "conf.py")
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_index_text():
    path = os.path.join(EJ_DIR, "index.rst")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_conf_defines_project_and_author():
    content = load_conf_text()
    assert re.search(r'(?m)^project\s*=\s*"[^"]+"', content), (
        "Falta asignar un valor no vacío a 'project' en conf.py"
    )
    assert re.search(r'(?m)^author\s*=\s*"[^"]+"', content), (
        "Falta asignar un valor no vacío a 'author' en conf.py"
    )


def test_index_toctree_contains_expected_pages():
    content = load_index_text()
    match = re.search(r"\.\.\s*toctree::\n((?:.*\n)*)", content)
    assert match, "Falta el bloque '.. toctree::' en index.rst"
    lines = [
        line.strip()
        for line in match.group(1).splitlines()
        if line.strip() and not line.strip().startswith(":")
    ]
    assert lines == ["instalacion", "api", "despliegue"], (
        "El 'toctree' debe incluir, en orden, 'instalacion', 'api' y "
        "'despliegue'"
    )


def test_info_proyecto():
    info = info_proyecto()
    assert info.get("project") == "Mi Proyecto Documentado"
    assert info.get("author")


def test_paginas_del_indice():
    assert paginas_del_indice() == ["instalacion", "api", "despliegue"]
