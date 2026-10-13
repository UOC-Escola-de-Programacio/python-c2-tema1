"""
Tests para el ejercicio ej1a1 (carpeta ej1a1/).
Comprueba que el menú de navegación global (nav) de mkdocs.yml está
correctamente configurado y que las funciones Python asociadas
(titulos_del_menu, comando_mkdocs_serve) funcionan correctamente.
"""

import os

import yaml

from ej1a1 import comando_mkdocs_serve, titulos_del_menu

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1a1")


def load_config():
    path = os.path.join(EJ_DIR, "mkdocs.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def nav_as_dict(nav):
    """Convierte la lista de "nav" de MkDocs en un diccionario título -> ruta."""
    result = {}
    for entry in nav:
        assert isinstance(entry, dict) and len(entry) == 1, (
            "Cada elemento de 'nav' debe ser un diccionario con una única clave"
        )
        title, path = next(iter(entry.items()))
        result[title] = path
    return result


def test_nav_exists():
    config = load_config()
    assert "nav" in config, "Falta la clave 'nav' en mkdocs.yml"
    assert isinstance(config["nav"], list) and len(config["nav"]) > 0, (
        "'nav' debe ser una lista no vacía"
    )


def test_nav_contains_expected_pages():
    config = load_config()
    nav = nav_as_dict(config["nav"])

    assert nav.get("Inicio") == "index.md"
    assert nav.get("Instalación") == "instalacion.md"
    assert nav.get("Referencia de la API") == "api.md"
    assert nav.get("Despliegue") == "despliegue.md"


def test_nav_order():
    config = load_config()
    titles = [next(iter(entry.keys())) for entry in config["nav"]]
    assert titles == ["Inicio", "Instalación", "Referencia de la API", "Despliegue"], (
        "El orden de las páginas en 'nav' no coincide con el enunciado"
    )


def test_titulos_del_menu_matches_nav():
    config = load_config()
    expected = [next(iter(entry.keys())) for entry in config["nav"]]
    assert titulos_del_menu() == expected, (
        "'titulos_del_menu' debe devolver los títulos de 'nav', en orden"
    )


def test_comando_mkdocs_serve_default_port():
    comando = comando_mkdocs_serve()
    assert comando == ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8000"], (
        "El comando por defecto debe servir en el puerto 8000"
    )


def test_comando_mkdocs_serve_custom_port():
    comando = comando_mkdocs_serve(puerto=9000)
    assert comando == ["mkdocs", "serve", "--dev-addr", "127.0.0.1:9000"], (
        "El comando debe respetar el puerto indicado"
    )
