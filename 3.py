
alcance = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

n = len(alcance)

for k in range(n):
    for i in range(n):
        for j in range(n):

            if alcance[i][k] == 1 and alcance[k][j] == 1:
                alcance[i][j] = 1

print("Matriz de alcanzabilidad:")

for fila in alcance:
    print(" ".join(map(str, fila)))
