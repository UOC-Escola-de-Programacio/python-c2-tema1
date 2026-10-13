"""
Tests para el ejercicio ej1f2 (carpeta ej1f2/).
Comprueba que "html_theme_options" está configurado en "conf.py" con las
claves esperadas, así como la función Python asociada.
"""

import os

from ej1f2 import opciones_del_tema

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1f2")


def load_conf_text():
    path = os.path.join(EJ_DIR, "conf.py")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_html_theme_options_configured():
    namespace = {}
    exec(load_conf_text(), namespace)
    opciones = namespace.get("html_theme_options", {})
    assert opciones.get("logo_only") is True, (
        "Falta configurar 'logo_only' en 'html_theme_options'"
    )
    assert opciones.get("navigation_depth") == 4, (
        "Falta configurar 'navigation_depth' en 'html_theme_options'"
    )


def test_opciones_del_tema():
    opciones = opciones_del_tema()
    assert opciones.get("logo_only") is True
    assert opciones.get("navigation_depth") == 4
