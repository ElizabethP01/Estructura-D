"""
Ejercicio 2: Mezcla Directa (Direct Merge Sort externo)
"""
import random


def siguiente(archivo):
    linea = archivo.readline()
    return int(linea) if linea.strip() else None


def distribuir(origen, aux1, aux2, tam):
    """Reparte el archivo origen en aux1 y aux2, alternando bloques de 'tam'."""
    with open(origen) as fo, open(aux1, "w") as f1, open(aux2, "w") as f2:
        destino = f1
        contador = 0
        x = siguiente(fo)
        while x is not None:
            destino.write(f"{x}\n")
            contador += 1
            if contador == tam:            # termina el bloque: se cambia de archivo
                destino = f2 if destino is f1 else f1
                contador = 0
            x = siguiente(fo)


def mezclar(aux1, aux2, destino, tam):
    """Mezcla bloque por bloque (de tamaño 'tam') aux1 y aux2 hacia destino."""
    with open(aux1) as f1, open(aux2) as f2, open(destino, "w") as fd:
        a = siguiente(f1)
        b = siguiente(f2)
        while a is not None or b is not None:
            ca = cb = 0                     # elementos tomados en este bloque
            while (a is not None and ca < tam) or (b is not None and cb < tam):
                hay_a = a is not None and ca < tam
                hay_b = b is not None and cb < tam
                if hay_a and (not hay_b or a <= b):
                    fd.write(f"{a}\n")
                    a = siguiente(f1)
                    ca += 1
                else:
                    fd.write(f"{b}\n")
                    b = siguiente(f2)
                    cb += 1


def mezcla_directa(ruta):
    """Ordena el archivo 'ruta' (un entero por línea) con mezcla directa."""
    with open(ruta) as f:
        n = sum(1 for linea in f if linea.strip())

    tam = 1
    pasada = 1
    while tam < n:
        distribuir(ruta, "aux1.txt", "aux2.txt", tam)
        mezclar("aux1.txt", "aux2.txt", ruta, tam)
        print(f"Pasada {pasada}: bloques de tamaño {tam} -> {leer_todo(ruta)}")
        tam *= 2
        pasada += 1


def leer_todo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().split()]


if __name__ == "__main__":
    random.seed(7)
    datos = [random.randint(1, 99) for _ in range(12)]
    with open("datos.txt", "w") as f:
        f.write("\n".join(map(str, datos)) + "\n")

    print("Original:", datos)
    mezcla_directa("datos.txt")
    print("Ordenado:", leer_todo("datos.txt"))
    assert leer_todo("datos.txt") == sorted(datos)
