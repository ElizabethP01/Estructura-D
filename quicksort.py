def quicksort(lista, bajo=0, alto=None):
    if alto is None:
        alto = len(lista) - 1
    if bajo < alto:
        p = particion(lista, bajo, alto)
        quicksort(lista, bajo, p - 1)
        quicksort(lista, p + 1, alto)
    return lista


def particion(lista, bajo, alto):
    pivote = lista[alto]                 # el último elemento es el pivote
    i = bajo - 1
    for j in range(bajo, alto):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1


def pedir_numeros():
    """Pide la cantidad de numeros y luego cada numero (enteros)."""
    while True:
        try:
            n = int(input("¿Cuántos números quieres ordenar? "))
            if n > 0:
                break
            print("Escribe un número mayor que 0.")
        except ValueError:
            print("Entrada inválida, escribe un entero.")
    numeros = []
    for i in range(n):
        while True:
            try:
                numeros.append(int(input(f"Número {i + 1}: ")))
                break
            except ValueError:
                print("Entrada inválida, escribe un entero.")
    return numeros


def menu(nombre, funcion):
    """Menú principal: se repite hasta que el usuario decida salir."""
    while True:
        print(f"\n===== {nombre} =====")
        print("1. Ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            numeros = pedir_numeros()
            print("Lista original:", numeros)
            print("Lista ordenada:", funcion(numeros.copy()))
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu("QUICKSORT", quicksort)
