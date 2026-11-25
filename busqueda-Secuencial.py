"""Ejercicio 1: Búsqueda secuencial (lineal).

Escenario: inventario de una tienda con productos en el orden en que
fueron registrados (lista SIN ordenar). Se busca un producto por nombre.
"""


def busqueda_secuencial(lista, objetivo):
    """Recorre la lista elemento por elemento.

    Devuelve (indice, comparaciones). Si no lo encuentra, indice = -1.
    """
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento.lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones


def ejecutar():
    inventario = [
        "Lapiz", "Cuaderno", "Borrador", "Regla", "Tijeras",
        "Pegamento", "Marcador", "Calculadora", "Mochila", "Libreta",
    ]
    print("\n=== BÚSQUEDA SECUENCIAL ===")
    print("Inventario (sin ordenar):", inventario)
    producto = input("Producto a buscar: ").strip()

    indice, comparaciones = busqueda_secuencial(inventario, producto)
    if indice != -1:
        print(f"'{producto}' encontrado en la posición {indice}.")
    else:
        print(f"'{producto}' no está en el inventario.")
    print(f"Comparaciones realizadas: {comparaciones}")


if __name__ == "__main__":
    ejecutar()
