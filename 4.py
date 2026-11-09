
def buscar(padres, nodo):
    if padres[nodo] != nodo:
        padres[nodo] = buscar(padres, padres[nodo])

    return padres[nodo]


def unir(padres, rangos, a, b):
    raiz_a = buscar(padres, a)
    raiz_b = buscar(padres, b)

    if raiz_a == raiz_b:
        return False

    if rangos[raiz_a] < rangos[raiz_b]:
        padres[raiz_a] = raiz_b

    elif rangos[raiz_a] > rangos[raiz_b]:
        padres[raiz_b] = raiz_a

    else:
        padres[raiz_b] = raiz_a
        rangos[raiz_a] += 1

    return True


def kruskal(nodos, aristas):
    padres = {nodo: nodo for nodo in nodos}
    rangos = {nodo: 0 for nodo in nodos}

    arbol = []
    costo_total = 0

    aristas_ordenadas = sorted(
        aristas, key=lambda arista: arista[2]
    )

    for a, b, peso in aristas_ordenadas:

        if unir(padres, rangos, a, b):
            arbol.append((a, b, peso))
            costo_total += peso

            if len(arbol) == len(nodos) - 1:
                break

    return arbol, costo_total


nodos = ["A", "B", "C", "D", "E"]

aristas = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2)
]

arbol, costo = kruskal(nodos, aristas)

print("Aristas seleccionadas para el árbol mínimo:")

for a, b, peso in arbol:
    print(f"{a} - {b}: {peso}")

print("Costo total:", costo)