"""
Tests para el ejercicio ej1c2 (carpeta ej1c2/).
Comprueba que el plugin mkdocstrings está configurado con la ruta del
código fuente, que la dependencia necesaria está en los requisitos, y las
funciones Python asociadas.
"""

import os

import yaml

from ej1c2 import plugins_configurados, rutas_de_mkdocstrings

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1c2")


def load_config():
    path = os.path.join(EJ_DIR, "mkdocs.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_requirements():
    path = os.path.join(EJ_DIR, "requirements.txt")
    with open(path, encoding="utf-8") as f:
        return f.read()


def find_plugin(plugins, name):
    for plugin in plugins:
        if plugin == name:
            return {}
        if isinstance(plugin, dict) and name in plugin:
            return plugin[name] or {}
    return None


def test_plugins_include_search_and_mkdocstrings():
    config = load_config()
    plugins = config.get("plugins", [])
    assert find_plugin(plugins, "search") is not None, (
        "Falta el plugin 'search' en la lista de 'plugins'"
    )
    mkdocstrings_config = find_plugin(plugins, "mkdocstrings")
    assert mkdocstrings_config is not None, (
        "Falta el plugin 'mkdocstrings' en la lista de 'plugins'"
    )


def test_mkdocstrings_paths_include_src():
    config = load_config()
    plugins = config.get("plugins", [])
    mkdocstrings_config = find_plugin(plugins, "mkdocstrings") or {}
    paths = (
        mkdocstrings_config.get("handlers", {})
        .get("python", {})
        .get("paths", [])
    )
    assert "src" in paths, (
        "La configuración de 'mkdocstrings' debe incluir 'src' en "
        "'handlers.python.paths'"
    )


def test_requirements_include_mkdocstrings():
    requirements = load_requirements().lower()
    assert "mkdocstrings" in requirements, (
        "Falta la dependencia 'mkdocstrings[python]' en el archivo de requisitos"
    )


def test_plugins_configurados():
    plugins = plugins_configurados()
    assert "search" in plugins
    assert "mkdocstrings" in plugins


def test_rutas_de_mkdocstrings():
    rutas = rutas_de_mkdocstrings()
    assert "src" in rutas
