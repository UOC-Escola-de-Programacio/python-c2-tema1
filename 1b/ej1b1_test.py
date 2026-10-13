"""
Tests para el ejercicio ej1b1 (carpeta ej1b1/).
Comprueba que se ha instalado la dependencia "mkdocs-material" y que el
tema configurado es "material", así como las funciones Python asociadas.
"""

import os

import yaml

from ej1b1 import dependencias, tema_configurado

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1b1")


def load_config():
    path = os.path.join(EJ_DIR, "mkdocs.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_requirements():
    path = os.path.join(EJ_DIR, "requirements.txt")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_theme_is_material():
    config = load_config()
    assert "theme" in config, "Falta la clave 'theme' en el archivo de configuración"
    theme = config["theme"]
    name = theme.get("name") if isinstance(theme, dict) else theme
    assert name == "material", "El tema configurado debe ser 'material'"


def test_requirements_include_mkdocs_material():
    requirements = load_requirements().lower()
    assert "mkdocs-material" in requirements, (
        "Falta la dependencia 'mkdocs-material' en el archivo de requisitos"
    )


def test_tema_configurado():
    assert tema_configurado() == "material"


def test_dependencias_include_mkdocs_material():
    deps = dependencias()
    assert isinstance(deps, list)
    assert any("mkdocs-material" in dep for dep in deps)
    assert all(not dep.strip().startswith("#") for dep in deps)
