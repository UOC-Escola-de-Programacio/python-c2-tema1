# Ejercicio ej1c4: typing + mkdocstrings + docstrings en formato Google

## 📝 Enunciado

Este ejercicio combina tres ideas del tema:

1. El **tipado estático** de Python (módulo [`typing`](https://docs.python.org/3/library/typing.html)), usando `List` y `Optional` para anotar parámetros y valores de retorno.
2. Los **docstrings en formato Google**, que documentan qué hace cada
   función/método y qué representa cada parámetro o valor devuelto.
3. La integración de ambos en **`mkdocstrings`**: cuando una función ya
   tiene anotaciones de tipo, `mkdocstrings` puede mostrarlas
   automáticamente en la documentación generada, así que **el docstring
   no necesita repetir el tipo**, solo describir su significado.

Al igual que en `ej1c1`, este ejercicio es un pequeño paquete de Python
(carpeta `1c/ej1c4/`), con el código a completar en su `__init__.py`:

```
ej1c4/
├── __init__.py   # Punto de entrada: clase "Producto" y funciones del
│                   inventario, a completar con type hints + docstrings.
└── ej1c4.yml     # Configuración de mkdocstrings para mostrar los tipos.
```

### Tu tarea

1. **`__init__.py`**: completa la clase `Producto` (con atributos
   anotados `nombre: str`, `precio: float`, `stock: int`, y el método
   `vender(cantidad: int) -> bool`) y las funciones `buscar_producto` y
   `valor_total_inventario`, añadiendo:
   - Anotaciones de tipo completas, usando `List` y `Optional` de
     `typing`.
   - Docstrings en formato Google que **no dupliquen** el tipo ya
     indicado en la anotación (por ejemplo: `nombre: nombre del
     producto.` en lugar de `nombre (str): nombre del producto.`).
2. **`ej1c4.yml`**: completa las opciones del handler de Python de
   `mkdocstrings` (`docstring_style: google` y
   `show_signature_annotations: true`) para que la documentación
   generada muestre automáticamente los tipos anotados.

## ✅ Cómo comprobar tu solución

Los tests de este ejercicio se encuentran en `1c/ej1c4_test.py`. Ejecuta,
desde la raíz del repositorio:

```bash
pytest 1c/ej1c4_test.py
```
