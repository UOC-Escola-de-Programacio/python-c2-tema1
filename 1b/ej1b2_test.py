"""
Tests para el ejercicio ej1b2 (carpeta ej1b2/).
Comprueba que la paleta de colores y las funcionalidades de la interfaz
están configuradas en el tema Material, y las funciones Python asociadas.
"""

import os

import yaml

from ej1b2 import funcionalidades_activadas, paleta_de_colores

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1b2")


def load_config():
    path = os.path.join(EJ_DIR, "mkdocs.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_palette_configured():
    config = load_config()
    theme = config.get("theme", {})
    palette = theme.get("palette")
    assert palette, "Falta la clave 'palette' dentro de 'theme'"
    assert "primary" in palette, "Falta el color 'primary' en la paleta"
    assert "accent" in palette, "Falta el color 'accent' en la paleta"


def test_features_include_navigation_tabs():
    config = load_config()
    theme = config.get("theme", {})
    features = theme.get("features", [])
    assert "navigation.tabs" in features, (
        "Falta la funcionalidad 'navigation.tabs' en 'theme.features'"
    )


def test_paleta_de_colores():
    paleta = paleta_de_colores()
    assert isinstance(paleta, dict)
    assert "primary" in paleta and "accent" in paleta


def test_funcionalidades_activadas():
    funcionalidades = funcionalidades_activadas()
    assert isinstance(funcionalidades, list)
    assert "navigation.tabs" in funcionalidades
