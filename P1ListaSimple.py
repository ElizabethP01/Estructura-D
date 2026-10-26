class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None          # <-- antes faltaba definir 'liga'


class ListaSimple:
    def __init__(self):
        self.p = None

    def insertar_inicio(self):
        dato = input("Ingrese el dato: ")
        nuevo = Nodo(dato)
        nuevo.liga = self.p
        self.p = nuevo
        print("Nodo insertado al inicio.")

    def insertar_final(self):
        dato = input("Ingrese el dato: ")
        nuevo = Nodo(dato)
        if self.p is None:
            self.p = nuevo
        else:
            actual = self.p
            while actual.liga is not None:
                actual = actual.liga
            actual.liga = nuevo
        print("Nodo insertado al final.")

    def eliminar_inicio(self):
        if self.p is None:
            print("La lista está vacía.")
        else:
            eliminado = self.p.info
            self.p = self.p.liga
            print("Se eliminó:", eliminado)

    def eliminar_final(self):
        if self.p is None:
            print("La lista está vacía.")
        elif self.p.liga is None:
            eliminado = self.p.info
            self.p = None
            print("Se eliminó:", eliminado)
        else:
            actual = self.p
            while actual.liga.liga is not None:
                actual = actual.liga
            eliminado = actual.liga.info
            actual.liga = None
            print("Se eliminó:", eliminado)

    def insertar_antes(self):
        x = input("Ingrese el dato X: ")
        dato = input("Ingrese el nuevo dato: ")
        if self.p is None:
            print("La lista está vacía.")
            return
        if self.p.info == x:
            nuevo = Nodo(dato)
            nuevo.liga = self.p
            self.p = nuevo
            print("Nodo insertado antes de X.")
            return
        anterior = self.p
        actual = self.p.liga
        while actual is not None and actual.info != x:
            anterior = actual
            actual = actual.liga
        if actual is None:
            print("No se encontró el dato X.")
        else:
            nuevo = Nodo(dato)
            nuevo.liga = actual
            anterior.liga = nuevo
            print("Nodo insertado antes de X.")

    def insertar_despues(self):
        x = input("Ingrese el dato X: ")
        dato = input("Ingrese el nuevo dato: ")
        actual = self.p
        while actual is not None and actual.info != x:
            actual = actual.liga
        if actual is None:
            print("No se encontró el dato X.")
        else:
            nuevo = Nodo(dato)
            nuevo.liga = actual.liga
            actual.liga = nuevo
            print("Nodo insertado después de X.")

    def mostrar(self):
        actual = self.p
        if actual is None:
            print("La lista está vacía.")
            return
        while actual is not None:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")


if __name__ == "__main__":
    lista = ListaSimple()
    while True:
        print("\n--- LISTA SIMPLEMENTE LIGADA ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar el inicio")
        print("4. Eliminar el final")
        print("5. Insertar antes de X")
        print("6. Insertar después de X")
        print("7. Mostrar lista")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            lista.insertar_inicio()
        elif opcion == "2":
            lista.insertar_final()
        elif opcion == "3":
            lista.eliminar_inicio()
        elif opcion == "4":
            lista.eliminar_final()
        elif opcion == "5":
            lista.insertar_antes()
        elif opcion == "6":
            lista.insertar_despues()
        elif opcion == "7":
            lista.mostrar()
        elif opcion == "8":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")