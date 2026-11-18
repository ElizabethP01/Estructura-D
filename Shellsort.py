"""Ordenamiento ShellSort (Shell Sort)."""


def shell_sort(lista):
    n = len(lista)
    brecha = n // 2                      # salto inicial
    while brecha > 0:
        # insertion sort con saltos de tamaño 'brecha'
        for i in range(brecha, n):
            temp = lista[i]
            j = i
            while j >= brecha and lista[j - brecha] > temp:
                lista[j] = lista[j - brecha]
                j -= brecha
            lista[j] = temp
        brecha //= 2                     # se reduce el salto
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
    menu("SHELL SORT", shell_sort)
