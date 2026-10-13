"""
Tests para el ejercicio ej1g2 (carpeta ej1g2/).
Comprueba que las extensiones "sphinx.ext.autodoc" y "sphinx.ext.napoleon"
están activadas en "conf.py", que se añade la ruta del paquete "ej1g1" a
"sys.path", que la dependencia "sphinx" está en los requisitos, y las
funciones Python asociadas.
"""

import os
import re

from ej1g2 import extensiones_activadas, rutas_en_sys_path

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1g2")


def load_conf_text():
    path = os.path.join(EJ_DIR, "conf.py")
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_requirements():
    path = os.path.join(EJ_DIR, "requirements.txt")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_extensions_include_autodoc_and_napoleon():
    content = load_conf_text()
    assert re.search(r'extensions\s*=.*\[[^\]]*"sphinx\.ext\.autodoc"', content, re.DOTALL), (
        "Falta 'sphinx.ext.autodoc' en la lista 'extensions'"
    )
    assert re.search(
        r'extensions\s*=.*\[[^\]]*"sphinx\.ext\.napoleon"', content, re.DOTALL
    ), "Falta 'sphinx.ext.napoleon' en la lista 'extensions'"


def test_sys_path_is_modified():
    content = load_conf_text()
    assert re.search(r"sys\.path\.(insert|append)\(", content), (
        "Falta una llamada a 'sys.path.insert' o 'sys.path.append' para "
        "que Sphinx encuentre el paquete 'ej1g1'"
    )


def test_requirements_include_sphinx():
    requirements = load_requirements().lower()
    assert "sphinx" in requirements, (
        "Falta la dependencia 'sphinx' en el archivo de requisitos"
    )


def test_extensiones_activadas():
    extensiones = extensiones_activadas()
    assert "sphinx.ext.autodoc" in extensiones
    assert "sphinx.ext.napoleon" in extensiones


def test_rutas_en_sys_path():
    rutas = rutas_en_sys_path()
    assert isinstance(rutas, list)
    assert len(rutas) >= 1
