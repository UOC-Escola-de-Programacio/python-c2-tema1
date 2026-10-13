"""
Tests para el ejercicio ej1f1 (carpeta ej1f1/).
Comprueba que se ha instalado la dependencia "sphinx-rtd-theme" y que el
tema configurado es "sphinx_rtd_theme", así como las funciones Python
asociadas.
"""

import os

from ej1f1 import dependencias, tema_configurado

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1f1")


def load_conf_text():
    path = os.path.join(EJ_DIR, "conf.py")
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_requirements():
    path = os.path.join(EJ_DIR, "requirements.txt")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_theme_is_sphinx_rtd_theme():
    namespace = {}
    exec(load_conf_text(), namespace)
    assert namespace.get("html_theme") == "sphinx_rtd_theme", (
        "El tema configurado debe ser 'sphinx_rtd_theme'"
    )


def test_requirements_include_sphinx_rtd_theme():
    requirements = load_requirements().lower()
    assert "sphinx-rtd-theme" in requirements, (
        "Falta la dependencia 'sphinx-rtd-theme' en el archivo de requisitos"
    )


def test_tema_configurado():
    assert tema_configurado() == "sphinx_rtd_theme"


def test_dependencias_include_sphinx_rtd_theme():
    deps = dependencias()
    assert isinstance(deps, list)
    assert any("sphinx-rtd-theme" in dep for dep in deps)
    assert all(not dep.strip().startswith("#") for dep in deps)
