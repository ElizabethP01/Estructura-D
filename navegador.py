class Pila:


    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def vaciar(self):
        self.items = []


class Navegador:

    def __init__(self):
        self.atras = Pila()
        self.adelante = Pila()
        self.actual = None

    def visitar(self, sitio):
        if self.actual is not None:
            self.atras.push(self.actual)
        self.actual = sitio
        self.adelante.vaciar()  # al visitar un sitio nuevo se pierde el "adelante"
        print(f"Visitando: {self.actual}")

    def retroceder(self):
        if self.atras.esta_vacia():
            print("No hay páginas anteriores.")
            return
        self.adelante.push(self.actual)
        self.actual = self.atras.pop()
        print(f"Página actual: {self.actual}")

    def avanzar(self):
        if self.adelante.esta_vacia():
            print("No hay páginas siguientes.")
            return
        self.atras.push(self.actual)
        self.actual = self.adelante.pop()
        print(f"Página actual: {self.actual}")

    def mostrar_historial(self):
        print("\n--- Historial ---")
        if self.actual is None:
            print("(vacío)")
            return
        # Más reciente primero: actual y luego las de la pila "atrás"
        print(f"-> {self.actual}  (actual)")
        for sitio in reversed(self.atras.items):
            print(f"   {sitio}")
        print(f"Páginas para avanzar: {self.adelante.tamanio()}\n")


def main():
    navegador = Navegador()

    while True:
        print("=== Navegador web ===")
        print("1. Visitar sitio")
        print("2. Retroceder")
        print("3. Avanzar")
        print("4. Ver historial")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            sitio = input("URL o nombre del sitio: ").strip()
            if sitio:
                navegador.visitar(sitio)
            else:
                print("Escribe un sitio válido.")
        elif opcion == "2":
            navegador.retroceder()
        elif opcion == "3":
            navegador.avanzar()
        elif opcion == "4":
            navegador.mostrar_historial()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
        print()


if __name__ == "__main__":
    main()
    
