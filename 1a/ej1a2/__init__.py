"""
Enunciado:
Redacción de la página principal utilizando títulos, listas y enlaces
internos entre documentos (parte en Python).

Una vez hayas redactado "index.md", completa en este módulo las funciones
que analizan su contenido mediante expresiones regulares:

1. "titulo_principal": devuelve el texto del título de nivel 1 (sin el
   "# " inicial).
2. "elementos_de_lista": devuelve la lista de elementos (como cadenas de
   texto, sin el marcador "-", "*" o "1.") de la primera lista Markdown
   encontrada en la página.
3. "enlaces_internos": devuelve un diccionario {texto_del_enlace: ruta}
   con todos los enlaces internos en formato Markdown "[texto](ruta)".
"""

import os
import re
from typing import Dict, List

EJ_DIR = os.path.dirname(__file__)
INDEX_PATH = os.path.join(EJ_DIR, "index.md")


def _leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def titulo_principal(ruta: str = INDEX_PATH) -> str:
    """Devuelve el título de nivel 1 de la página.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Texto del título de nivel 1, sin el "# " inicial.
    """
    # TODO: busca la primera línea que empieza por "# " y devuelve su
    # contenido (sin el "# " inicial ni espacios sobrantes).
    raise NotImplementedError


def elementos_de_lista(ruta: str = INDEX_PATH) -> List[str]:
    """Devuelve los elementos de la primera lista Markdown de la página.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Lista con el texto de cada elemento (sin el marcador "-", "*" o
        "1.", "2.", etc.).
    """
    # TODO: localiza las líneas de lista (ordenada o no ordenada) y
    # devuelve su contenido, sin el marcador inicial.
    raise NotImplementedError


def enlaces_internos(ruta: str = INDEX_PATH) -> Dict[str, str]:
    """Devuelve los enlaces internos en formato Markdown de la página.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Diccionario que asocia el texto visible de cada enlace con la ruta
        a la que apunta, por ejemplo
        {"Instalación": "instalacion.md"}.
    """
    # TODO: busca todas las coincidencias de "[texto](ruta)" y devuélvelas
    # como un diccionario texto -> ruta.
    raise NotImplementedError


if __name__ == "__main__":
    print("Título:", titulo_principal())
    print("Lista:", elementos_de_lista())
    print("Enlaces:", enlaces_internos())
