"""
Ejercicio 3: Mezcla Equilibrada (Balanced Merge, versión natural)

"""
import os
import random
import shutil
import tempfile


class Lector:
    """Lee un archivo número por número, con el valor actual a la vista."""

    def __init__(self, ruta):
        self.f = open(ruta)
        self.actual = self._leer()

    def _leer(self):
        linea = self.f.readline()
        return int(linea) if linea.strip() else None

    def avanzar(self):
        x = self.actual
        self.actual = self._leer()
        return x

    def cerrar(self):
        self.f.close()


def distribuir_tramos(origen, ruta1, ruta2):
    """Reparte los tramos naturales del origen, alternando entre 2 archivos."""
    lector = Lector(origen)
    with open(ruta1, "w") as f1, open(ruta2, "w") as f2:
        destino = f1
        ultimo = None
        while lector.actual is not None:
            if ultimo is not None and lector.actual < ultimo:
                destino = f2 if destino is f1 else f1    # termina un tramo
            ultimo = lector.avanzar()
            destino.write(f"{ultimo}\n")
    lector.cerrar()


def mezclar_un_tramo(la, lb, salida):
    """Mezcla un tramo ordenado de A con un tramo ordenado de B."""
    ultimo_a = ultimo_b = None
    while True:
        hay_a = la.actual is not None and (ultimo_a is None or la.actual >= ultimo_a)
        hay_b = lb.actual is not None and (ultimo_b is None or lb.actual >= ultimo_b)
        if not hay_a and not hay_b:
            break
        if hay_a and (not hay_b or la.actual <= lb.actual):
            ultimo_a = la.avanzar()
            salida.write(f"{ultimo_a}\n")
        else:
            ultimo_b = lb.avanzar()
            salida.write(f"{ultimo_b}\n")


def mezclar_pasada(entrada1, entrada2, salida1, salida2):
    """Una pasada: mezcla tramos de las 2 entradas y los reparte en 2 salidas."""
    la, lb = Lector(entrada1), Lector(entrada2)
    with open(salida1, "w") as s1, open(salida2, "w") as s2:
        destino = s1
        while la.actual is not None or lb.actual is not None:
            mezclar_un_tramo(la, lb, destino)
            destino = s2 if destino is s1 else s1
    la.cerrar()
    lb.cerrar()


def leer_todo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().split()]


def mezcla_equilibrada(ruta):
    """Ordena el archivo 'ruta' con mezcla equilibrada (4 archivos)."""
    with tempfile.TemporaryDirectory() as carpeta:
        e1, e2, s1, s2 = (os.path.join(carpeta, n) for n in
                          ("f1.txt", "f2.txt", "f3.txt", "f4.txt"))
        distribuir_tramos(ruta, e1, e2)
        print("Distribución inicial:")
        print("  F1:", leer_todo(e1))
        print("  F2:", leer_todo(e2))

        pasada = 1
        while True:
            mezclar_pasada(e1, e2, s1, s2)
            print(f"Pasada {pasada}:")
            print("  F3:", leer_todo(s1))
            print("  F4:", leer_todo(s2))
            if os.path.getsize(s2) == 0:        # todo quedó en un solo archivo
                shutil.copy(s1, ruta)
                break
            e1, e2, s1, s2 = s1, s2, e1, e2     # las salidas pasan a ser entradas
            pasada += 1


if __name__ == "__main__":
    random.seed(3)
    datos = [random.randint(1, 99) for _ in range(14)]
    with open("datos.txt", "w") as f:
        f.write("\n".join(map(str, datos)) + "\n")

    print("Original:", datos)
    mezcla_equilibrada("datos.txt")
    print("Ordenado:", leer_todo("datos.txt"))
    assert leer_todo("datos.txt") == sorted(datos)
