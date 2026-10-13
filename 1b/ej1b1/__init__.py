"""
Enunciado:
Instalación del paquete de diseño avanzado y cambio del tema por defecto
(parte en Python).

Una vez hayas completado "mkdocs.yml" y "requirements.txt", implementa en
este módulo las funciones:

1. "tema_configurado": devuelve el nombre del tema configurado en
   "mkdocs.yml".
2. "dependencias": devuelve la lista de paquetes (sin comentarios ni
   líneas en blanco) declarados en "requirements.txt".
"""

import os
from typing import List

import yaml

EJ_DIR = os.path.dirname(__file__)
MKDOCS_CONFIG_PATH = os.path.join(EJ_DIR, "mkdocs.yml")
REQUIREMENTS_PATH = os.path.join(EJ_DIR, "requirements.txt")


def tema_configurado(ruta_config: str = MKDOCS_CONFIG_PATH) -> str:
    """Devuelve el nombre del tema configurado en "mkdocs.yml".

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Nombre del tema configurado (por ejemplo, "material").
    """
    # TODO: carga el archivo YAML y devuelve "theme.name".
    raise NotImplementedError


def dependencias(ruta_requirements: str = REQUIREMENTS_PATH) -> List[str]:
    """Devuelve la lista de dependencias declaradas en "requirements.txt".

    Args:
        ruta_requirements: Ruta al archivo de requisitos que se quiere leer.

    Returns:
        Lista de nombres de paquetes, sin comentarios ni líneas en blanco.
    """
    # TODO: lee el archivo de requisitos y devuelve la lista de paquetes,
    # ignorando las líneas vacías y las que empiezan por "#".
    raise NotImplementedError


if __name__ == "__main__":
    print("Tema:", tema_configurado())
    print("Dependencias:", dependencias())
