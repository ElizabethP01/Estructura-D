"""Ejercicio 2: Búsqueda binaria.

Escenario: lista de matrículas de alumnos YA ORDENADA de menor a mayor.
Se busca una matrícula dividiendo el rango de búsqueda a la mitad en
cada paso.
"""


def busqueda_binaria(lista, objetivo):
    """Devuelve (indice, comparaciones). Requiere lista ordenada."""
    inicio, fin = 0, len(lista) - 1
    comparaciones = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, comparaciones


def ejecutar():
    matriculas = [
        1001, 1005, 1012, 1020, 1033, 1047, 1050, 1068,
        1074, 1089, 1095, 1102, 1118, 1130, 1147, 1160,
    ]
    print("\n=== BÚSQUEDA BINARIA ===")
    print("Matrículas (ordenadas):", matriculas)
    try:
        objetivo = int(input("Matrícula a buscar: "))
    except ValueError:
        print("Debes ingresar un número entero.")
        return

    indice, comparaciones = busqueda_binaria(matriculas, objetivo)
    if indice != -1:
        print(f"Matrícula {objetivo} encontrada en la posición {indice}.")
    else:
        print(f"La matrícula {objetivo} no existe en la lista.")
    print(f"Comparaciones realizadas: {comparaciones}")


if __name__ == "__main__":
    ejecutar()
