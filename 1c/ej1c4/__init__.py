"""
Enunciado:
Documentación automatizada con tipado estático (typing), mkdocstrings y
docstrings en formato Google.

Cuando una función o método ya tiene anotaciones de tipo (type hints), el
plugin "mkdocstrings" es capaz de mostrar automáticamente esos tipos en la
documentación generada, por lo que **no hace falta repetirlos** dentro del
docstring. Por ejemplo, en formato Google, en lugar de escribir:

    Args:
        nombre (str): el nombre del producto.

cuando ya existe la anotación "nombre: str" en la firma de la función,
basta con escribir:

    Args:
        nombre: el nombre del producto.

En este ejercicio vas a completar un pequeño paquete ("ej1c4/", el propio
directorio donde se encuentra este archivo) que modela el inventario de
una tienda, usando el módulo "typing" para anotar los tipos y docstrings
en formato Google que no dupliquen esa información.

Tu tarea es completar, en este archivo ("__init__.py"):

1. La clase "Producto", con sus atributos anotados ("nombre: str",
   "precio: float", "stock: int") y sus métodos:
   - "__init__": inicializa el producto con stock 0 por defecto.
   - "vender(cantidad: int) -> bool": descuenta stock si hay suficiente y
     devuelve True; si no hay stock suficiente, no modifica nada y
     devuelve False.
2. La función "buscar_producto(productos: List[Producto], nombre: str) ->
   Optional[Producto]", que devuelve el primer producto cuyo nombre
   coincida, o "None" si no se encuentra ninguno.
3. La función "valor_total_inventario(productos: List[Producto]) ->
   float", que devuelve la suma de "precio * stock" de todos los
   productos.

Todas las funciones y métodos deben tener:
- Anotaciones de tipo completas (parámetros y valor de retorno), usando
  "List" y "Optional" del módulo "typing".
- Un docstring en formato Google (con las secciones "Args:"/"Attributes:"
  y "Returns:" según corresponda) que **no repita los tipos** ya indicados
  mediante las anotaciones.

Consulta también "ej1c4.yml", donde deberás configurar las opciones de
"mkdocstrings" para que se muestren estas anotaciones de tipo en la
documentación generada.
"""

# TODO: importa "List" y "Optional" desde "typing".


class Producto:
    """
    TODO: completa este docstring en formato Google.
    Debe describir la clase y documentar sus atributos en una sección
    "Attributes:", sin repetir los tipos (ya indicados mediante type
    hints en el código).
    """

    def __init__(self, nombre, precio, stock=0):
        """
        TODO: añade anotaciones de tipo a "nombre" (str), "precio" (float)
        y "stock" (int), y completa el docstring con una sección "Args:"
        (sin repetir los tipos).
        """
        # TODO: guarda "nombre", "precio" y "stock" como atributos.
        pass

    def vender(self, cantidad):
        """
        TODO: añade anotaciones de tipo a "cantidad" (int) y al valor de
        retorno (bool), y completa el docstring con las secciones
        "Args:" y "Returns:" (sin repetir los tipos).
        """
        # TODO: si no hay stock suficiente ("cantidad" > "stock"), no
        # modifiques nada y devuelve False.
        # TODO: si hay stock suficiente, descuenta "cantidad" de "stock" y
        # devuelve True.
        pass


def buscar_producto(productos, nombre):
    """
    TODO: añade anotaciones de tipo a "productos" (List[Producto]) y
    "nombre" (str), así como al valor de retorno (Optional[Producto]), y
    completa el docstring con las secciones "Args:" y "Returns:" (sin
    repetir los tipos).
    """
    # TODO: devuelve el primer producto de "productos" cuyo nombre
    # coincida con "nombre", o "None" si no se encuentra ninguno.
    pass


def valor_total_inventario(productos):
    """
    TODO: añade anotaciones de tipo a "productos" (List[Producto]) y al
    valor de retorno (float), y completa el docstring con las secciones
    "Args:" y "Returns:" (sin repetir los tipos).
    """
    # TODO: devuelve la suma de "precio * stock" de todos los productos de
    # "productos" (0.0 si la lista está vacía).
    pass
