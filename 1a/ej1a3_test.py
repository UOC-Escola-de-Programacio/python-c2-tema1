"""
Tests para el ejercicio ej1a3 (carpeta ej1a3/).
Comprueba que la página de instalación contiene bloques de código con
resaltado de sintaxis para "bash" y "python", y que las funciones Python de
análisis funcionan correctamente.
"""

import os
import re

from ej1a3 import bloques_de_codigo, comando_de_instalacion

EJ_DIR = os.path.join(os.path.dirname(__file__), "ej1a3")


def load_content():
    path = os.path.join(EJ_DIR, "instalacion.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_has_bash_code_block():
    content = load_content()
    assert re.search(r"```bash\n.+?```", content, re.DOTALL), (
        "Falta un bloque de código ```bash con el comando de instalación"
    )


def test_has_python_code_block():
    content = load_content()
    assert re.search(r"```python\n.+?```", content, re.DOTALL), (
        "Falta un bloque de código ```python con un script de ejemplo"
    )


def test_bash_block_contains_pip_install():
    content = load_content()
    match = re.search(r"```bash\n(.+?)```", content, re.DOTALL)
    assert match and "pip install" in match.group(1), (
        "El bloque 'bash' debe contener un comando 'pip install'"
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
