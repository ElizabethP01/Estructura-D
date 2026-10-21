class Cola:
    """Cola (FIFO): el primero que entra es el primero que sale."""

    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def sumar_colas(cola_a, cola_b):
    resultado = Cola()
    while not cola_a.esta_vacia() or not cola_b.esta_vacia():
        a = cola_a.desencolar() if not cola_a.esta_vacia() else 0
        b = cola_b.desencolar() if not cola_b.esta_vacia() else 0
        resultado.encolar(a + b)
    return resultado


if __name__ == "__main__":
    cola_a = Cola()
    cola_b = Cola()

    for n in [3, 4, 2, 8, 12]:
        cola_a.encolar(n)
    for n in [6, 2, 9, 11, 3]:
        cola_b.encolar(n)

    print("Cola A:", cola_a)
    print("Cola B:", cola_b)
    print("Cola Resultado:", sumar_colas(cola_a, cola_b))
