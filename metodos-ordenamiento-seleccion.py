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

if __name__ == "__main__":
    ejercicio_3()
