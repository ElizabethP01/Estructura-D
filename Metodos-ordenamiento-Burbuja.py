# EJERCICIO 1: MÉTODO DE LA BURBUJA
# Situación: tu playlist tiene canciones con distinta duración y
# quieres verlas de la más corta a la más larga.
# Idea: se comparan pares de elementos vecinos y se intercambian si
# están en el orden incorrecto. En cada pasada, la canción más larga
# "sube" al final como una burbuja.
# Complejidad: O(n^2)

def ordenamiento_burbuja(canciones):
    n = len(canciones)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            # canciones[j] = (nombre, duracion_en_minutos)
            if canciones[j][1] > canciones[j + 1][1]:
                canciones[j], canciones[j + 1] = canciones[j + 1], canciones[j]
                hubo_intercambio = True
        if not hubo_intercambio:  # si ya está ordenada, se detiene
            break
    return canciones


def ejercicio_1():
    print("EJERCICIO 1: Burbuja - Mi playlist de la más corta a la más larga")
    playlist = [
        ("Cancion A", 3.45),
        ("Cancion B", 2.10),
        ("Cancion C", 4.80),
        ("Cancion D", 1.95),
        ("Cancion E", 3.05),
        ("Cancion F", 5.20),
    ]
    print("Original:")
    for nombre, minutos in playlist:
        print(f"  {nombre} - {minutos} min")

    print("Ordenada:")
    for nombre, minutos in ordenamiento_burbuja(playlist.copy()):
        print(f"  {nombre} - {minutos} min")
    print()

if __name__ == "__main__":
    ejercicio_1() 

