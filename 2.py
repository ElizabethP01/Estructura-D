
INF = float("inf")

distancias = [
    [0,   4,   2,   INF, INF],
    [4,   0,   1,   5,   INF],
    [2,   1,   0,   8,   10],
    [INF, 5,   8,   0,   2],
    [INF, INF, 10,  2,   0]
]

n = len(distancias)

for k in range(n):
    for i in range(n):
        for j in range(n):
            nueva_distancia = distancias[i][k] + distancias[k][j]

            if nueva_distancia < distancias[i][j]:
                distancias[i][j] = nueva_distancia

print("Matriz de distancias mínimas:")

for fila in distancias:
    print(" ".join(
        "INF" if valor == INF else str(int(valor))
        for valor in fila
    ))

