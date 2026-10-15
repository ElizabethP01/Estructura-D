import time

def torre_hanoi(n, origen, auxiliar, destino):
    
    Resuelve la Torre de Hanoi de forma recursiva.
    Devuelve el número de movimientos realizados.
    
    if n == 1:
        return 1

    movimientos = torre_hanoi(n - 1, origen, destino, auxiliar)
    movimientos += 1
    movimientos += torre_hanoi(n - 1, auxiliar, origen, destino)

    return movimientos


def medir_tiempo(n):
    inicio = time.perf_counter()

    movimientos = torre_hanoi(n, "A", "B", "C")

    fin = time.perf_counter()
    tiempo = fin - inicio

    print(f"Discos: {n}")
    print(f"Movimientos: {movimientos:,}")
    print(f"Tiempo: {tiempo:.6f} segundos")
    print("-" * 35)


if __name__ == "__main__":
    for discos in [5, 10, 30, 64]:
        medir_tiempo(discos)
