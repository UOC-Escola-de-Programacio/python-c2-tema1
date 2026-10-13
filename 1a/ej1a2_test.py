"""
Tests para el ejercicio ej1a2 (carpeta ej1a2/).
Comprueba que la página principal contiene un título, una lista y enlaces
internos, y que las funciones Python de análisis funcionan correctamente.
"""

import os
import re

from ej1a2 import elementos_de_lista, enlaces_internos, titulo_principal

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1a2")


def load_content():
    path = os.path.join(EJ_DIR, "index.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_title():
    content = load_content()
    assert re.search(r"(?m)^#\s+\S", content), (
        "La página debe incluir un título de nivel 1 (encabezado '# ')"
    )
    assert "TODO" not in re.search(r"(?m)^#.*$", content).group(0), (
        "Sustituye el título de ejemplo por el título real del proyecto"
    )


def test_has_list_with_at_least_three_items():
    content = load_content()
    unordered = re.findall(r"(?m)^\s*[-*]\s+\S.*$", content)
    ordered = re.findall(r"(?m)^\s*\d+\.\s+\S.*$", content)
    assert len(unordered) + len(ordered) >= 3, (
        "La página debe incluir una lista con al menos 3 elementos"
    )


def test_has_internal_links():
    content = load_content()
    links = dict(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content))
    targets = list(links.values())
    assert any("instalacion.md" in t for t in targets), (
        "Falta un enlace interno a 'instalacion.md'"
    )
    assert any("api.md" in t for t in targets), (
        "Falta un enlace interno a 'api.md'"
    )


def test_titulo_principal():
    content = load_content()
    expected = re.search(r"(?m)^#\s+(\S.*)$", content).group(1).strip()
    assert titulo_principal() == expected


def test_elementos_de_lista_count():
    elementos = elementos_de_lista()
    assert isinstance(elementos, list)
    assert len(elementos) >= 3, "Debe devolver al menos 3 elementos"
    assert all(
        not item.lstrip().startswith(("-", "*")) and not re.match(r"^\d+\.", item.lstrip())
        for item in elementos
    ), "Los elementos no deben incluir el marcador de la lista"


def test_enlaces_internos():
    enlaces = enlaces_internos()
    assert isinstance(enlaces, dict)
    assert any("instalacion.md" in ruta for ruta in enlaces.values())
    assert any("api.md" in ruta for ruta in enlaces.values())
