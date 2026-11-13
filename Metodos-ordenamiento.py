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


# EJERCICIO 2: MÉTODO DE INSERCIÓN
# Situación: acabas de cambiar de celular y tus contactos de
# WhatsApp están todos revueltos; quieres ponerlos en orden
# alfabético.
# Idea: se toma cada contacto y se "inserta" en su lugar correcto
# dentro de la parte que ya está ordenada (como ordenar las cartas
# de un juego en tu mano).
# Complejidad: O(n^2), muy bueno si la lista ya está casi ordenada.

def ordenamiento_insercion(contactos):
    for i in range(1, len(contactos)):
        actual = contactos[i]
        j = i - 1
        while j >= 0 and contactos[j] > actual:
            contactos[j + 1] = contactos[j]  # desplaza a la derecha
            j -= 1
        contactos[j + 1] = actual
    return contactos


def ejercicio_2():
    print("EJERCICIO 2: Inserción - Contactos de WhatsApp en orden alfabético")
    contactos = ["Valeria", "Diego", "Sofi", "Mamá", "Andrés", "Camila", "Luis"]
    print("Original :", contactos)
    print("Ordenada :", ordenamiento_insercion(contactos.copy()))
    print()


# EJERCICIO 3: MÉTODO DE SELECCIÓN
# Situación: jugaste una partida con tus amigos en un videojuego y
# quieres armar el ranking, del que más puntos hizo al que menos.
# Idea: en cada pasada se busca al jugador con mayor puntaje entre
# los que faltan por ordenar y se coloca en su posición del ranking.
# Complejidad: O(n^2), pero hace pocos intercambios.
def ordenamiento_seleccion(jugadores):
    n = len(jugadores)
    for i in range(n - 1):
        indice_mayor = i
        for j in range(i + 1, n):
            # jugadores[j] = (nombre, puntos)
            if jugadores[j][1] > jugadores[indice_mayor][1]:
                indice_mayor = j
        jugadores[i], jugadores[indice_mayor] = jugadores[indice_mayor], jugadores[i]
    return jugadores


def ejercicio_3():
    print("EJERCICIO 3: Selección - Ranking de la partida")
    jugadores = [
        ("Diego", 1520),
        ("Valeria", 2300),
        ("Andrés", 980),
        ("Camila", 2750),
        ("Luis", 1800),
    ]
    print("Resultados sin ordenar:")
    for nombre, puntos in jugadores:
        print(f"  {nombre}: {puntos} pts")

    print("Ranking final:")
    ranking = ordenamiento_seleccion(jugadores.copy())
    for posicion, (nombre, puntos) in enumerate(ranking, start=1):
        print(f"  {posicion}. {nombre}: {puntos} pts")
    print()


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
