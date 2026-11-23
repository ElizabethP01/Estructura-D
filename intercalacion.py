"""
Ejercicio 1: Intercalación

"""

def siguiente(archivo):
    """Lee el siguiente número del archivo; devuelve None si ya no hay más."""
    linea = archivo.readline()
    return int(linea) if linea.strip() else None


def intercalar(ruta_a, ruta_b, ruta_salida):
    """Intercala los archivos A y B (ordenados) en el archivo de salida."""
    with open(ruta_a) as fa, open(ruta_b) as fb, open(ruta_salida, "w") as fs:
        a = siguiente(fa)
        b = siguiente(fb)

        # Mientras ambos archivos tengan datos, se escribe el menor
        while a is not None and b is not None:
            if a <= b:
                fs.write(f"{a}\n")
                a = siguiente(fa)
            else:
                fs.write(f"{b}\n")
                b = siguiente(fb)

        # Se copia lo que sobre del archivo que aún tenga datos
        while a is not None:
            fs.write(f"{a}\n")
            a = siguiente(fa)
        while b is not None:
            fs.write(f"{b}\n")
            b = siguiente(fb)


def leer_todo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().split()]


if __name__ == "__main__":
    # Se crean dos archivos de prueba ya ordenados
    with open("a.txt", "w") as f:
        f.write("\n".join(map(str, [3, 8, 15, 22, 40])) + "\n")
    with open("b.txt", "w") as f:
        f.write("\n".join(map(str, [1, 8, 10, 30, 35, 50, 60])) + "\n")

    print("Archivo A:", leer_todo("a.txt"))
    print("Archivo B:", leer_todo("b.txt"))

    intercalar("a.txt", "b.txt", "salida.txt")
    print("Intercalado:", leer_todo("salida.txt"))
