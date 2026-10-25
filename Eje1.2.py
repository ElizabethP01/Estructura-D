from abc import ABC, abstractmethod

class Order:
    def __init__(self, qtty, customer):
        self.__customer = customer
        self.__qtty = qtty

    def get_qtty(self):
        return self.__qtty

    def get_customer(self):
        return self.__customer

    def print(self):
        print("    Customer: " + str(self.get_customer()))
        print("    Quantity: " + str(self.get_qtty()))
        print("    ------------")



class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_info(self):
        return self.info

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        """Número de elementos de la cola."""

    @abstractmethod
    def is_empty(self):
        """True si está vacía, False si no."""

    @abstractmethod
    def front(self):
        """Primer elemento SIN quitarlo. None si está vacía."""

    @abstractmethod
    def enqueue(self, info):
        """Agrega un elemento al final de la cola."""

    @abstractmethod
    def dequeue(self):
        """Primer elemento QUITÁNDOLO. None si está vacía."""


class Queue(QueueInterface):
    def __init__(self):
        self.top = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.top is None

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        nuevo = Node(info)
        if self.is_empty():
            self.top = nuevo            # primer nodo: es cabeza y cola
        else:
            self.tail.set_next(nuevo)   # enlaza después del último
        self.tail = nuevo
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.get_info()
        self.top = self.top.get_next()  # desenlaza la cabeza
        if self.top is None:            # la cola quedó vacía
            self.tail = None
        self._size -= 1
        return info

    def print_info(self):
        """Muestra el tamaño y recorre la cola imprimiendo cada elemento."""
        print("********* QUEUE DUMP *********")
        print("   Size:", self.size())
        node = self.top
        i = 1
        while node is not None:
            print("   ** Element", i)
            node.get_info().print()
            node = node.get_next()
            i += 1
        print("******************************")

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento SIN borrarlo (posiciones desde 1).
        Devuelve None si la posición no es válida."""
        if pos < 1 or pos > self._size:
            return None
        node = self.top
        for _ in range(pos - 1):
            node = node.get_next()
        return node.get_info()


def main():
    # ---------- Ejercicio 1 ----------
    print(">>> EJERCICIO 1: probando la cola\n")
    cola = Queue()

    print("Cola vacía -> front():", cola.front(), "| dequeue():", cola.dequeue())
    print("is_empty():", cola.is_empty(), "\n")

    pedidos = [
        Order(20, "cust1"),
        Order(30, "cust2"),
        Order(40, "cust3"),
        Order(50, "cust3"),
    ]

    for p in pedidos:
        print(f"--- enqueue (cliente={p.get_customer()}, cantidad={p.get_qtty()})")
        cola.enqueue(p)
        cola.print_info()

    print("\n--- front() (no quita el elemento)")
    cola.front().print()
    cola.print_info()

    print("\n--- dequeue() (quita el primero)")
    cola.dequeue().print()
    cola.print_info()

    print("\n--- dequeue() otra vez")
    cola.dequeue().print()
    cola.print_info()

    # ---------- Ejercicio 2 ----------
    print("\n>>> EJERCICIO 2: get_nth\n")
    cola2 = Queue()
    for i, cliente in enumerate(["A", "B", "C", "D"], start=1):
        cola2.enqueue(Order(i * 10, cliente))
    cola2.print_info()

    print("\nget_nth(3) -> el tercero:")
    cola2.get_nth(3).print()

    print("get_nth(0) ->", cola2.get_nth(0))
    print("get_nth(5) ->", cola2.get_nth(5))
    print("Tamaño después de get_nth (no borra):", cola2.size())


if __name__ == "__main__":
    main()
