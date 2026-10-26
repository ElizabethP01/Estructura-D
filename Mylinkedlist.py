class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # ---------- consulta ----------
    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        actual = self.head
        while actual is not None:
            yield actual.info
            actual = actual.next

    def get_nth(self, pos):
        if pos < 1 or pos > self._size:
            return None
        actual = self.head
        for _ in range(pos - 1):
            actual = actual.next
        return actual.info

    def show(self):
        if self.is_empty():
            print("La lista está vacía.")
            return
        for dato in self:
            print(dato, end=" -> ")
        print("None")

    # ---------- inserción ----------
    def insert_start(self, info):
        nuevo = Node(info)
        nuevo.next = self.head
        self.head = nuevo
        if self.tail is None:       # la lista estaba vacía
            self.tail = nuevo
        self._size += 1

    def insert_end(self, info):
        nuevo = Node(info)
        if self.is_empty():
            self.head = nuevo
        else:
            self.tail.next = nuevo
        self.tail = nuevo
        self._size += 1

    def insert_before(self, x, info):
        """Inserta info antes del dato x. Devuelve False si x no existe."""
        if self.is_empty():
            return False
        if self.head.info == x:
            self.insert_start(info)
            return True
        anterior = self.head
        actual = self.head.next
        while actual is not None and actual.info != x:
            anterior = actual
            actual = actual.next
        if actual is None:
            return False
        nuevo = Node(info)
        nuevo.next = actual
        anterior.next = nuevo
        self._size += 1
        return True

    def insert_after(self, x, info):
        """Inserta info después del dato x. Devuelve False si x no existe."""
        actual = self.head
        while actual is not None and actual.info != x:
            actual = actual.next
        if actual is None:
            return False
        nuevo = Node(info)
        nuevo.next = actual.next
        actual.next = nuevo
        if actual is self.tail:
            self.tail = nuevo
        self._size += 1
        return True

    # ---------- eliminación ----------
    def delete_start(self):
        """Elimina y devuelve el primer dato. None si está vacía."""
        if self.is_empty():
            return None
        eliminado = self.head.info
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return eliminado

    def delete_end(self):
        """Elimina y devuelve el último dato. None si está vacía."""
        if self.is_empty():
            return None
        if self.head is self.tail:
            return self.delete_start()
        actual = self.head
        while actual.next is not self.tail:
            actual = actual.next
        eliminado = self.tail.info
        actual.next = None
        self.tail = actual
        self._size -= 1
        return eliminado