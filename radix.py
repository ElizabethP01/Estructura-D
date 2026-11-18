def counting_sort_por_digito(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10
    for num in lista:
        conteo[(num // exp) % 10] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    for num in reversed(lista):          # reversed mantiene la estabilidad
        d = (num // exp) % 10
        conteo[d] -= 1
        salida[conteo[d]] = num
    return salida


def radix_positivos(lista):
    if not lista:
        return lista
    maximo = max(lista)
    exp = 1
    while maximo // exp > 0:
        lista = counting_sort_por_digito(lista, exp)
        exp *= 10
    return lista


def radix_sort(lista):
    negativos = [-x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]
    negativos = [-x for x in reversed(radix_positivos(negativos))]
    return negativos + radix_positivos(positivos)


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
    menu("RADIX SORT", radix_sort)
