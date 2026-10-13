"""
Enunciado:
Incorporación de cajas de alerta o admonitions (parte en Python).

Una vez hayas completado "notas.md" con las admonitions "!!! note" y
"!!! warning", implementa en este módulo la función:

1. "admonitions": devuelve un diccionario {tipo: contenido} con el
   contenido (sin indentar) de cada admonition de la página, usando como
   clave el tipo ("note", "warning", etc.).
"""

import os
import re
from typing import Dict

EJ_DIR = os.path.dirname(__file__)
NOTAS_PATH = os.path.join(EJ_DIR, "notas.md")


def admonitions(ruta: str = NOTAS_PATH) -> Dict[str, str]:
    """Devuelve el contenido de cada admonition de la página.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Diccionario que asocia el tipo de admonition ("note", "warning",
        etc.) con su contenido, sin la indentación de 4 espacios.
    """
    # TODO: busca todas las admonitions "!!! tipo" y devuelve un
    # diccionario tipo -> contenido (sin indentar).
    raise NotImplementedError


if __name__ == "__main__":
    print("Admonitions:", admonitions())
