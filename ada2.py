import random, time

def mostrar_tabla(matriz, nombre_fila, nombre_col, max_filas=8, max_cols=8):
    # Solo mostramos un pedazo para que no imprima miles de datos
    filas = min(len(matriz), max_filas)
    cols = min(len(matriz[0]), max_cols)

    # Encabezado (Materia 1, Materia 2, ...)
    print(" " * 12 + "".join(f"{nombre_col} {c+1}".rjust(12) for c in range(cols)))

    # Cada fila con su nombre (Alumno 1, Alumno 2, ...)
    for f in range(filas):
        print(f"{nombre_fila} {f+1}".ljust(12) + "".join(str(matriz[f][c]).rjust(12) for c in range(cols)))

    print(f"(Se muestran {filas} de {len(matriz)} filas y {cols} de {len(matriz[0])} columnas)\n")

alumnos = 1000
materias = 100

# Forma 1: filas = alumnos, columnas = materias
m1 = [[random.randint(0, 100) for _ in range(materias)] for _ in range(alumnos)]

# Forma 2: filas = materias, columnas = alumnos
m2 = [[random.randint(0, 100) for _ in range(alumnos)] for _ in range(materias)]

print("FORMA 1: Alumnos en filas, Materias en columnas")
mostrar_tabla(m1, "Alumno", "Materia")

print("FORMA 2: Materias en filas, Alumnos en columnas")
mostrar_tabla(m2, "Materia", "Alumno")

# Buscar alumno 321 y materia 5 (índices 320 y 4)
inicio = time.perf_counter()
nota1 = m1[320][4]
t1 = time.perf_counter() - inicio

inicio = time.perf_counter()
nota2 = m2[4][320]
t2 = time.perf_counter() - inicio

print("BÚSQUEDA: Alumno 321, Materia 5")
print(f"Forma 1: {nota1}  ({t1:.9f} s)")
print(f"Forma 2: {nota2}  ({t2:.9f} s)")