"""
Tests para el ejercicio ej1c4 (typing + mkdocstrings + Google docstrings).
Comprueban el comportamiento de la clase "Producto" y las funciones del
inventario, que las anotaciones de tipo estén presentes y sean correctas,
que los docstrings en formato Google no dupliquen los tipos ya anotados, y
que la configuración de mkdocstrings muestre las anotaciones de tipo.
"""

import inspect
import os
import re
import typing

import yaml

from ej1c4 import Producto, buscar_producto, valor_total_inventario

EJ_DIR = os.path.dirname(__file__)


# --- Comportamiento --------------------------------------------------------


def test_producto_se_crea_con_stock_por_defecto():
    producto = Producto("Teclado", 25.5)
    assert producto.nombre == "Teclado"
    assert producto.precio == 25.5
    assert producto.stock == 0


def test_producto_vender_descuenta_stock():
    producto = Producto("Ratón", 10.0, stock=5)
    assert producto.vender(3) is True
    assert producto.stock == 2


def test_producto_vender_sin_stock_suficiente():
    producto = Producto("Monitor", 150.0, stock=1)
    assert producto.vender(2) is False
    assert producto.stock == 1


def test_buscar_producto_encuentra():
    productos = [Producto("Teclado", 25.5, 3), Producto("Ratón", 10.0, 5)]
    encontrado = buscar_producto(productos, "Ratón")
    assert encontrado is not None
    assert encontrado.nombre == "Ratón"


def test_buscar_producto_no_encuentra():
    productos = [Producto("Teclado", 25.5, 3)]
    assert buscar_producto(productos, "Monitor") is None


def test_valor_total_inventario():
    productos = [Producto("Teclado", 25.0, 2), Producto("Ratón", 10.0, 5)]
    assert valor_total_inventario(productos) == 25.0 * 2 + 10.0 * 5


def test_valor_total_inventario_vacio():
    assert valor_total_inventario([]) == 0


# --- Anotaciones de tipo (typing) -------------------------------------------


def test_producto_init_tiene_anotaciones_de_tipo():
    hints = typing.get_type_hints(Producto.__init__)
    assert hints.get("nombre") is str
    assert hints.get("precio") is float
    assert hints.get("stock") is int


def test_producto_vender_tiene_anotaciones_de_tipo():
    hints = typing.get_type_hints(Producto.vender)
    assert hints.get("cantidad") is int
    assert hints.get("return") is bool


def test_buscar_producto_tiene_anotaciones_de_tipo():
    hints = typing.get_type_hints(buscar_producto)

    productos_hint = hints.get("productos")
    assert productos_hint is not None, "Falta anotar el parámetro 'productos'"
    assert typing.get_origin(productos_hint) is list
    assert typing.get_args(productos_hint) == (Producto,)

    nombre_hint = hints.get("nombre")
    assert nombre_hint is str

    return_hint = hints.get("return")
    assert return_hint is not None, "Falta anotar el valor de retorno"
    origin = typing.get_origin(return_hint)
    assert origin is typing.Union, (
        "El valor de retorno debe anotarse con 'Optional[Producto]'"
    )
    args = typing.get_args(return_hint)
    assert Producto in args and type(None) in args


def test_valor_total_inventario_tiene_anotaciones_de_tipo():
    hints = typing.get_type_hints(valor_total_inventario)

    productos_hint = hints.get("productos")
    assert productos_hint is not None, "Falta anotar el parámetro 'productos'"
    assert typing.get_origin(productos_hint) is list
    assert typing.get_args(productos_hint) == (Producto,)

    assert hints.get("return") is float


# --- Docstrings en formato Google, sin duplicar los tipos -------------------


def test_producto_class_has_attributes_section():
    doc = Producto.__doc__ or ""
    assert "Attributes:" in doc, (
        "El docstring de 'Producto' debe incluir la sección 'Attributes:'"
    )


def test_producto_init_has_args_section():
    doc = Producto.__init__.__doc__ or ""
    assert "Args:" in doc, (
        "El docstring de '__init__' debe incluir la sección 'Args:'"
    )


def test_producto_vender_has_google_docstring():
    doc = Producto.vender.__doc__ or ""
    assert "Args:" in doc and "Returns:" in doc


def test_buscar_producto_has_google_docstring():
    doc = buscar_producto.__doc__ or ""
    assert "Args:" in doc and "Returns:" in doc


def test_valor_total_inventario_has_google_docstring():
    doc = valor_total_inventario.__doc__ or ""
    assert "Args:" in doc and "Returns:" in doc


def _args_section_lines(doc):
    match = re.search(r"Args:\s*\n((?:[ \t]+.+\n?)+)", doc or "")
    if not match:
        return []
    return [line.strip() for line in match.group(1).splitlines() if line.strip()]


def test_docstrings_no_duplican_el_tipo_en_args():
    # Si un parámetro ya está anotado con un type hint, el docstring en
    # formato Google no debería repetir el tipo entre paréntesis
    # (p. ej. "nombre (str): ..."), solo describirlo (p. ej. "nombre: ...").
    for target in (Producto.__init__, Producto.vender, buscar_producto, valor_total_inventario):
        for line in _args_section_lines(target.__doc__):
            assert not re.match(r"^\w+\s*\([^)]*\)\s*:", line), (
                f"No dupliques el tipo en el docstring de "
                f"'{target.__qualname__}': {line!r}"
            )


# --- Configuración de mkdocstrings (ej1c4.yml) ------------------------------


def load_yml_config():
    path = os.path.join(EJ_DIR, "ej1c4", "ej1c4.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _mkdocstrings_python_options(config):
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "mkdocstrings" in plugin:
            mkdocstrings_config = plugin["mkdocstrings"] or {}
            return (
                mkdocstrings_config.get("handlers", {})
                .get("python", {})
                .get("options", {})
            )
    return {}


def test_mkdocstrings_docstring_style_is_google():
    options = _mkdocstrings_python_options(load_yml_config())
    assert options.get("docstring_style") == "google", (
        "Falta configurar 'docstring_style: google' en las opciones del "
        "handler de Python"
    )


def test_mkdocstrings_shows_signature_annotations():
    options = _mkdocstrings_python_options(load_yml_config())
    assert options.get("show_signature_annotations") is True, (
        "Falta configurar 'show_signature_annotations: true' en las "
        "opciones del handler de Python"
    )
