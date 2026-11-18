def heapify(lista, n, raiz):
    mayor = raiz
    izq = 2 * raiz + 1
    der = 2 * raiz + 2
    if izq < n and lista[izq] > lista[mayor]:
        mayor = izq
    if der < n and lista[der] > lista[mayor]:
        mayor = der
    if mayor != raiz:
        lista[raiz], lista[mayor] = lista[mayor], lista[raiz]
        heapify(lista, n, mayor)


def heapsort(lista):
    n = len(lista)
    # 1) construir el montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    # 2) extraer el máximo y colocarlo al final
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista


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
    menu("HEAPSORT", heapsort)
